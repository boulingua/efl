"""Convert relative `.qmd`-derived links in content/*.md to absolute URLs.

Background
----------
The Phase 2 migrator rewrote `[..](foo.qmd)` to `[..](foo/)` but kept the
result *relative* to the source. That worked when the source pages were
flat .qmd files at the repo root (Quarto's layout), because a relative
target was always peer-of-source. After conversion to Hugo page bundles
(`content/<X>/index.md` rendering at `/<X>/`), browser-side resolution
treats relatives as inside-bundle, so e.g.
`[Haftungsausschluss](haftungsausschluss/)` from `/impressum/` resolves
to `/impressum/haftungsausschluss/` — broken.

Fix
---
Reverse-map every `content/.../*.md` path back to its original `.qmd`
directory, resolve the relative target there, then forward-map the
resulting path through the Phase 2 slug rules to get the new Hugo URL.
This makes every link absolute and topologically correct in one pass.

Files in `content/materials/` did not come from .qmd sources; they're
skipped.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"

LINK_RE = re.compile(r'(\]\()([^)\s][^)\s"]*)((?:\s+"[^"]*")?\))')

EXTERNAL_PREFIXES = ("/", "http://", "https://", "//", "mailto:",
                     "tel:", "data:", "#")


def is_external(target: str) -> bool:
    return target.startswith(EXTERNAL_PREFIXES)


# ---------------------------------------------------------------------------
# Reverse-map: content/.../*.md  ->  the original .qmd's directory parts.
# ---------------------------------------------------------------------------

TRACK_DIR_RE = re.compile(r"track-(e|gm)$")
KL_DIR_RE = re.compile(r"kl(\d{2})$")


def original_qmd_dir(md_path: Path) -> list[str] | None:
    """Return the original .qmd parent dir as Quarto-style path components,
    or None if this content file did not come from a .qmd (e.g. /materials/).
    """
    rel = md_path.relative_to(CONTENT)
    parts = list(rel.parts)
    name = parts[-1]

    # Skip Phase 3 hub content (no .qmd ancestor).
    if parts[0] == "materials":
        return None

    if name == "_index.md":
        # Section index: directory name = original dir's tail.
        hugo_parts = parts[:-1]
    elif name == "index.md":
        # Page bundle <slug>/index.md: original .qmd's dir = bundle's parent.
        hugo_parts = parts[:-2]
    else:
        # Bare <slug>.md (not used by this migration but handled for safety).
        hugo_parts = parts[:-1]

    return hugo_to_qmd_dir(hugo_parts)


def hugo_to_qmd_dir(hugo_parts: list[str]) -> list[str]:
    """Reverse track-X/kl<NN> -> track_X_kl<NN> and undo - -> _ everywhere
    except inside the Klasse number where digits stay intact.

    Note: hyphens inside slug components like "hello-world" should not be
    reverted to underscores at this layer — we only join with the relative
    target and then re-apply forward slug-mapping. The reverse here is
    only about *directory*-level conventions.
    """
    out: list[str] = []
    i = 0
    while i < len(hugo_parts):
        p = hugo_parts[i]
        if TRACK_DIR_RE.fullmatch(p) and i + 1 < len(hugo_parts) and \
                KL_DIR_RE.fullmatch(hugo_parts[i + 1]):
            out.append(f"track_{TRACK_DIR_RE.fullmatch(p).group(1)}_"
                       f"kl{KL_DIR_RE.fullmatch(hugo_parts[i + 1]).group(1)}")
            i += 2
        else:
            # `appendices`, `units` — pass through.
            out.append(p)
            i += 1
    return out


# ---------------------------------------------------------------------------
# Forward-map: original-style path -> Hugo URL.
# ---------------------------------------------------------------------------

def qmd_to_hugo_url(parts: list[str]) -> str:
    out: list[str] = []
    for p in parts:
        m = re.fullmatch(r"track_(e|gm)_kl(\d{2})", p)
        if m:
            out.extend([f"track-{m.group(1)}", f"kl{m.group(2)}"])
        else:
            out.append(p.replace("_", "-"))
    return "/" + "/".join(out)


# ---------------------------------------------------------------------------
# Absolutise one link.
# ---------------------------------------------------------------------------

def absolutise(target: str, src_qmd_dir: list[str]) -> str:
    """Resolve `target` relative to `src_qmd_dir`, return site-absolute URL."""
    # Strip any trailing slash for path math, but remember it.
    has_trailing = target.endswith("/")
    parts = src_qmd_dir + [p for p in target.split("/") if p not in ("",)]

    # Collapse `..` and `.` segments.
    abs_parts: list[str] = []
    for p in parts:
        if p == ".":
            continue
        if p == "..":
            if abs_parts:
                abs_parts.pop()
            continue
        abs_parts.append(p)

    # Forward-map slug shape (track_X_kl<NN> -> track-X/kl<NN>, _ -> -).
    url = qmd_to_hugo_url(abs_parts) if abs_parts else "/"
    if has_trailing and not url.endswith("/"):
        url += "/"
    return url


# ---------------------------------------------------------------------------
# Driver.
# ---------------------------------------------------------------------------

def process(md: Path) -> int:
    src_qmd_dir = original_qmd_dir(md)
    if src_qmd_dir is None:
        return 0  # /materials/ etc.
    text = md.read_text(encoding="utf-8")
    fixed = 0

    def repl(m: re.Match[str]) -> str:
        nonlocal fixed
        prefix, url, suffix = m.group(1), m.group(2), m.group(3)
        if is_external(url):
            return m.group(0)
        new_url = absolutise(url, src_qmd_dir)
        if new_url == url:
            return m.group(0)
        fixed += 1
        return f"{prefix}{new_url}{suffix}"

    new_text = LINK_RE.sub(repl, text)
    if fixed:
        md.write_text(new_text, encoding="utf-8")
    return fixed


def main() -> int:
    total = 0
    files = 0
    for md in CONTENT.rglob("*.md"):
        n = process(md)
        if n:
            total += n
            files += 1
    print(f"Absolutised {total} links across {files} files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
