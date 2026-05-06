#!/usr/bin/env python3
"""Convert Quarto .qmd files to Hugo-flavoured .md page bundles.

Deterministic and idempotent — running twice on the same source produces
the same output. Designed to be invoked per batch (top-level / appendices /
course-indexes / per-track-grade) so each batch can be reviewed and
committed independently.

Conventions
-----------
* Page bundles. `track_e_kl05/units/unit01_hello-world.qmd`
  becomes `content/track-e/kl05/units/unit01-hello-world/index.md`.
* Section indexes. Any `index.qmd` in a directory with sub-pages becomes
  `_index.md` (Hugo section); top-level leaf pages become `index.md`
  bundles named after the slug.
* Underscore-prefixed exam-body partials are NOT migrated as their own
  pages. They are inlined wherever `{{< include _foo.qmd >}}` references
  them (per Phase 0 §8 decision (a)).
* Aliases. Every migrated page records its old Quarto URL under
  `aliases:` so existing bookmarks 301 to the new location.
* Word-count parity. After conversion, the script computes a word-count
  diff between source body and dest body (with frontmatter and shortcodes
  stripped). Drift > 2% appends a row to MIGRATION_PLAN.md "Manual
  review needed" via stdout (the caller pipes it).

Usage
-----
    python _scripts/migrate_to_hugo.py <qmd_path> [<qmd_path> ...]

Each path is resolved relative to the repo root. Running with no
arguments is a no-op (intentionally, to avoid accidental whole-repo
runs).
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


# ---------------------------------------------------------------------------
# Path mapping
# ---------------------------------------------------------------------------

def is_track_root_index(qmd: Path) -> bool:
    """Track root indexes (track_e_kl05/index.qmd) become Hugo sections."""
    rel = qmd.relative_to(ROOT)
    parts = rel.parts
    return len(parts) == 2 and parts[0].startswith("track_") and parts[1] == "index.qmd"


def hugo_slug(name: str) -> str:
    """Convert underscore-style slug to hyphen-style."""
    return name.replace("_", "-")


def map_path(qmd: Path) -> Path | None:
    """Return the destination .md path under content/, or None to skip.

    Skips:
        * underscore-prefixed body partials (inlined elsewhere).
        * exam-PDF wrappers? — we DO migrate them; their content is the
          same exam exercises and learners may link to them. They become
          their own page bundle ending in `-exam`.
    """
    rel = qmd.relative_to(ROOT)
    parts = list(rel.parts)
    name = parts[-1]

    if name.startswith("_"):
        return None  # body partial, inlined into includer
    if name == "_metadata.yml":
        return None

    stem = qmd.stem
    parent_parts = parts[:-1]

    # Top-level index.qmd -> content/_index.md
    if not parent_parts and stem == "index":
        return ROOT / "content" / "_index.md"

    # Top-level leaf, e.g. about.qmd -> content/about/index.md (page bundle)
    if not parent_parts:
        return ROOT / "content" / hugo_slug(stem) / "index.md"

    # Map directory parts: track_e_kl05 -> track-e/kl05
    new_parent: list[str] = []
    for part in parent_parts:
        if re.fullmatch(r"track_(e|gm)_kl\d{2}", part):
            track, kl = part.split("_kl")
            new_parent.extend([hugo_slug(track), f"kl{kl}"])
        else:
            new_parent.append(hugo_slug(part))

    # An index.qmd inside a directory becomes that directory's _index.md
    if stem == "index":
        return ROOT.joinpath("content", *new_parent, "_index.md")

    # Otherwise: page bundle <slug>/index.md
    return ROOT.joinpath("content", *new_parent, hugo_slug(stem), "index.md")


def hugo_url(dest: Path) -> str:
    """Return the rendered URL for a destination .md file."""
    rel = dest.relative_to(ROOT / "content")
    if rel.name == "_index.md":
        url_parts = list(rel.parts[:-1])
    elif rel.name == "index.md":
        url_parts = list(rel.parts[:-1])
    else:
        url_parts = [*rel.parts[:-1], rel.stem]
    if not url_parts:
        return "/"
    return "/" + "/".join(url_parts) + "/"


def quarto_url(qmd: Path) -> str:
    """Return the URL Quarto would have rendered this .qmd to."""
    rel = qmd.relative_to(ROOT).as_posix()
    return "/" + rel.removesuffix(".qmd") + ".html"


# ---------------------------------------------------------------------------
# Frontmatter
# ---------------------------------------------------------------------------

FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n?", re.DOTALL)

# Top-level YAML keys to drop entirely (Quarto-specific, no Hugo equivalent
# or actively harmful). The whole block under each key is dropped, including
# nested mappings (e.g. format: { html: {...}, revealjs: {...}, pdf: {...} }).
DROP_KEYS = {"format", "editor", "pagetitle", "filters"}


def split_frontmatter(text: str) -> tuple[str, str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return "", text
    return m.group(1), text[m.end():]


def strip_dropped_keys(fm: str) -> str:
    """Remove entire top-level YAML blocks for keys in DROP_KEYS."""
    lines = fm.splitlines(keepends=False)
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if m and m.group(1) in DROP_KEYS:
            # Skip this line and any indented continuation block.
            i += 1
            while i < len(lines):
                nxt = lines[i]
                if nxt.strip() == "":
                    i += 1
                    continue
                if nxt[:1] in (" ", "\t", "-"):
                    i += 1
                    continue
                break
            continue
        out.append(line)
        i += 1
    return "\n".join(out).strip()


def add_aliases(fm: str, alias: str) -> str:
    """Append an aliases: list to frontmatter (or extend existing)."""
    if re.search(r"^aliases\s*:", fm, re.MULTILINE):
        # Already has aliases; append if not present.
        if alias in fm:
            return fm
        return re.sub(
            r"^aliases\s*:\s*\n((?:\s+-\s+.*\n)*)",
            lambda m: m.group(0) + f"  - {alias}\n",
            fm + "\n",
            count=1,
            flags=re.MULTILINE,
        ).rstrip()
    return fm + f"\naliases:\n  - {alias}"


# ---------------------------------------------------------------------------
# Body conversion
# ---------------------------------------------------------------------------

# Pandoc allows ::: blocks with 3 *or more* colons (`::::`, `:::::`, etc.).
# We treat any sequence of >=3 colons as a fence. Closing fence is the same
# shape with no class attribute (`:::` of any matching length).
FENCE_RE = re.compile(r"^(:{3,})\s*(?:\{(.*?)\})?\s*$")

# Inline span classes: [text]{.class}
INLINE_CLASS_RE = re.compile(r"\[([^\]]+)\]\{\.([a-z][\w-]*)\}")

# .qmd link targets in [text](path.qmd) — rewrite to Hugo URL form.
QMD_LINK_RE = re.compile(r"(\]\()([^)\s]+?\.qmd)((?:#[^)\s]*)?\))")

INCLUDE_RE = re.compile(r"\{\{<\s*include\s+([^\s>]+)\s*>\}\}")


@dataclass
class Block:
    kind: str       # "callout-note", "hero", "card", "vgwort-pixel", ...
    attrs: str      # raw attr string for callouts (icon, collapse, title)
    content: list[str]


def parse_attrs_callout(attrs: str) -> tuple[str, str | None, bool, bool]:
    """Return (type, title, collapse, icon).

    Tolerates a literal `"` inside the title value (Quarto allows it).
    """
    m = re.match(r"\.callout-(\w+)", attrs)
    ctype = m.group(1) if m else "note"

    # Greedy match: title attribute is conventionally the last on the line,
    # so capture from `title="` to the final `"` before line end.
    title_m = re.search(r'title="(.*)"\s*$', attrs)
    title = title_m.group(1) if title_m else None

    collapse_m = re.search(r'collapse="(\w+)"', attrs)
    collapse = collapse_m.group(1) == "true" if collapse_m else False

    icon_m = re.search(r"icon=(\w+)", attrs)
    icon = True if not icon_m else icon_m.group(1) != "false"

    return ctype, title, collapse, icon


def render_block_open(block: Block) -> str | None:
    """Return the opening shortcode line, or None if this is a div passthrough."""
    if block.kind.startswith("callout-"):
        ctype = block.kind.removeprefix("callout-")
        _, title, collapse, icon = parse_attrs_callout("." + block.kind + " " + block.attrs)
        # Re-parse from the original attrs for consistent quoting:
        _, title, collapse, icon = parse_attrs_callout(f".{block.kind} {block.attrs}")
        parts = [f'type="{ctype}"']
        if title is not None:
            # Escape internal " → &quot; for shortcode arg safety.
            safe = title.replace('\\', '\\\\').replace('"', '\\"')
            parts.append(f'title="{safe}"')
        if collapse:
            parts.append('collapse="true"')
        if not icon:
            parts.append('icon="false"')
        return "{{< callout " + " ".join(parts) + " >}}"
    if block.kind in ("hero", "lead", "kicker", "card-grid", "card"):
        return "{{< " + block.kind + " >}}"
    if block.kind == "vgwort-pixel":
        return None  # handled specially in convert_body
    # Unknown div class — pass through as raw HTML <div class="...">
    return f'<div class="{block.kind}">'


def render_block_close(block: Block) -> str:
    if block.kind.startswith("callout-"):
        return "{{< /callout >}}"
    if block.kind in ("hero", "lead", "kicker", "card-grid", "card"):
        return "{{< /" + block.kind + " >}}"
    if block.kind == "vgwort-pixel":
        return ""
    return "</div>"


def expand_includes(text: str, qmd: Path) -> str:
    """Replace `{{< include foo.qmd >}}` with the include target's body
    (frontmatter stripped). Recursive — partials may include other partials."""
    def repl(m: re.Match[str]) -> str:
        target = m.group(1)
        target_path = (qmd.parent / target).resolve()
        if not target_path.exists():
            print(f"  WARN include target not found: {target} (in {qmd.name})",
                  file=sys.stderr)
            return m.group(0)
        body_text = target_path.read_text(encoding="utf-8")
        _, body = split_frontmatter(body_text)
        # Recursively expand within the included body.
        return expand_includes(body, target_path).rstrip()

    return INCLUDE_RE.sub(repl, text)


def convert_body(body: str, qmd: Path) -> str:
    """Apply all body-level transformations."""
    # 1. Inline {{< include foo.qmd >}} (must run BEFORE block parsing so
    #    nested fences from the partial participate in the same stack).
    body = expand_includes(body, qmd)

    # 2. Walk lines with a fence stack to convert ::: blocks.
    lines = body.split("\n")
    out: list[str] = []
    stack: list[Block] = []
    in_code = False
    code_fence = ""
    in_vgwort_html_block = False  # inside ```{=html} inside vgwort-pixel

    for line in lines:
        # Track fenced code blocks so we don't parse fences inside them.
        cm = re.match(r"^(```+|~~~+)(.*)$", line)
        if cm and not in_code:
            in_code = True
            code_fence = cm.group(1)
            info = cm.group(2).strip()
            # Special case: ```{=html} inside .vgwort-pixel -> drop the fence
            # itself, keep the inner HTML raw.
            if (stack and stack[-1].kind == "vgwort-pixel"
                    and info == "{=html}"):
                in_vgwort_html_block = True
                continue
            out.append(line)
            continue
        if cm and in_code and cm.group(1) == code_fence:
            in_code = False
            if in_vgwort_html_block:
                in_vgwort_html_block = False
                continue
            out.append(line)
            continue
        if in_code:
            if in_vgwort_html_block:
                # Pass through the raw HTML body untouched.
                out.append(line)
            else:
                out.append(line)
            continue

        m = FENCE_RE.match(line)
        if m:
            colons, attrs = m.group(1), (m.group(2) or "").strip()
            if attrs:
                # Opening fence.
                kind: str
                cm2 = re.match(r"\.(callout-\w+|hero|lead|kicker|card-grid|card|vgwort-pixel)\b(.*)$",
                               attrs)
                if cm2:
                    kind = cm2.group(1)
                    rest = cm2.group(2).strip()
                else:
                    cm3 = re.match(r"\.([\w-]+)(.*)$", attrs)
                    kind = cm3.group(1) if cm3 else "div"
                    rest = (cm3.group(2) if cm3 else "").strip()
                blk = Block(kind=kind, attrs=rest, content=[])
                stack.append(blk)
                opener = render_block_open(blk)
                if opener is not None:
                    out.append(opener)
                continue
            # Closing fence (bare ::: or :::: of matching length).
            if stack:
                blk = stack.pop()
                closer = render_block_close(blk)
                if closer:
                    out.append(closer)
                continue
            # Unmatched closer — pass through.
            out.append(line)
            continue

        out.append(line)

    body = "\n".join(out)

    # 3. Inline span classes [text]{.class} -> <span class="class">text</span>
    body = INLINE_CLASS_RE.sub(
        lambda m: f'<span class="{m.group(2)}">{m.group(1)}</span>',
        body,
    )

    # 4. Rewrite [..](foo.qmd) links — map .qmd path to Hugo URL form.
    def rewrite_qmd_link(m: re.Match[str]) -> str:
        prefix, target, suffix = m.group(1), m.group(2), m.group(3)
        # Strip .qmd, hyphenate the basename, append trailing slash before any anchor.
        path_part = target.removesuffix(".qmd")
        # Hyphenate only the basename (so `units/unit01_hello-world` -> `units/unit01-hello-world`).
        if "/" in path_part:
            head, _, base = path_part.rpartition("/")
            path_part = f"{head}/{hugo_slug(base)}"
        else:
            path_part = hugo_slug(path_part)
        # If basename was "index", the URL is the directory itself.
        if path_part.endswith("/index"):
            path_part = path_part[: -len("index")]
        return f"{prefix}{path_part}/{suffix.lstrip(')')})"

    body = QMD_LINK_RE.sub(rewrite_qmd_link, body)

    return body


# ---------------------------------------------------------------------------
# Word-count parity
# ---------------------------------------------------------------------------

WORD_RE = re.compile(r"\b[\w'-]+\b", re.UNICODE)
SHORTCODE_RE = re.compile(r"\{\{[<%].*?[%>]\}\}", re.DOTALL)
HTML_TAG_RE = re.compile(r"<[^>]+>", re.DOTALL)
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
QUARTO_FENCE_LINE_RE = re.compile(r"^:{3,}\s*(?:\{[^}]*\})?\s*$", re.MULTILINE)
INLINE_CLASS_KEEP_TEXT_RE = re.compile(r"\[([^\]]+)\]\{\.[a-z][\w-]*\}")
RAW_HTML_FENCE_RE = re.compile(r"```\{=html\}\s*\n.*?\n```\s*$", re.DOTALL | re.MULTILINE)


def normalize_for_count(text: str) -> str:
    """Strip both Quarto and Hugo markup so word counts are comparable."""
    # Drop raw-HTML fences entirely (Quarto's ```{=html} ... ``` and the
    # bare HTML they leave behind in Hugo are both pure markup, not prose).
    text = RAW_HTML_FENCE_RE.sub(" ", text)
    text = HTML_COMMENT_RE.sub(" ", text)
    text = SHORTCODE_RE.sub(" ", text)
    text = HTML_TAG_RE.sub(" ", text)
    # Pandoc fence lines: ::: {.card} or bare :::
    text = QUARTO_FENCE_LINE_RE.sub(" ", text)
    # Inline class: [text]{.class} -> text
    text = INLINE_CLASS_KEEP_TEXT_RE.sub(lambda m: m.group(1), text)
    # Strip link targets entirely — they're URL machinery, not prose, and
    # the migration intentionally rewrites slug shape (.qmd → /, _ → -).
    text = re.sub(r"\]\([^)]*\)", "]", text)
    # Treat underscore + hyphen + slash as word separators so "unit01_hello-world"
    # and "unit01-hello-world" (or just "unit01 hello world") count alike.
    text = re.sub(r"[_/]", " ", text)
    return text


def word_count(text: str) -> int:
    return len(WORD_RE.findall(normalize_for_count(text)))


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------

@dataclass
class Result:
    src: Path
    dest: Path
    src_words: int
    dest_words: int
    drift: float


def migrate_one(qmd: Path) -> Result | None:
    dest = map_path(qmd)
    if dest is None:
        return None  # underscore partial or non-content file
    src_text = qmd.read_text(encoding="utf-8")
    fm_src, body_src = split_frontmatter(src_text)

    fm_clean = strip_dropped_keys(fm_src)
    fm_clean = add_aliases(fm_clean, quarto_url(qmd))

    body_new = convert_body(body_src, qmd)

    dest.parent.mkdir(parents=True, exist_ok=True)
    out_text = "---\n" + fm_clean + "\n---\n" + body_new
    if not out_text.endswith("\n"):
        out_text += "\n"
    dest.write_text(out_text, encoding="utf-8")

    # Expand includes on source side too so the source word count covers
    # the same logical content as the destination (which has them inlined).
    src_w = word_count(expand_includes(body_src, qmd))
    dest_w = word_count(body_new)
    drift = abs(dest_w - src_w) / src_w if src_w else 0.0
    return Result(src=qmd, dest=dest, src_words=src_w,
                  dest_words=dest_w, drift=drift)


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("paths", nargs="*", type=Path)
    ap.add_argument("--threshold", type=float, default=0.02,
                    help="word-count drift threshold (default 0.02)")
    args = ap.parse_args(argv)

    if not args.paths:
        print("No paths given; nothing to do.", file=sys.stderr)
        return 0

    flagged: list[Result] = []
    n_ok = 0
    n_skip = 0
    for p in args.paths:
        qmd = p if p.is_absolute() else (ROOT / p)
        if not qmd.exists():
            print(f"SKIP missing: {p}", file=sys.stderr)
            n_skip += 1
            continue
        result = migrate_one(qmd)
        if result is None:
            n_skip += 1
            continue
        flag = ""
        if result.drift > args.threshold:
            flagged.append(result)
            flag = f"  [DRIFT {result.drift:.2%}]"
        print(f"  {qmd.relative_to(ROOT)} -> "
              f"{result.dest.relative_to(ROOT)} "
              f"(src {result.src_words}w / dst {result.dest_words}w){flag}")
        n_ok += 1

    print(f"\nMigrated {n_ok}, skipped {n_skip}, flagged {len(flagged)}.")
    if flagged:
        print("\nFlagged for manual review:")
        for r in flagged:
            print(f"  - `{r.src.relative_to(ROOT).as_posix()}` "
                  f"(src {r.src_words}w / dst {r.dest_words}w, "
                  f"drift {r.drift:.2%})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
