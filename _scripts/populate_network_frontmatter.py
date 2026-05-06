"""Populate `tags:` + `topic:` on every material-bearing unit page.

Reads each `content/track-*/kl*/units/*/index.md` (skipping `*-exam`
wrappers) and inserts:

* `tags:` — union of existing `skills_focus` values + the chapter
  codes from `bildungsplan:` (e.g. `"3.1.3.3"`). Per Phase 0 decision A3.
  Skill values stay as-is; chapter strings of the form
  `"3.1.3.3 Sprechen – an Gesprächen teilnehmen"` are reduced to their
  numeric prefix (`3.1.3.3`) so the tag-chip UI shows clean codes.

* `topic:` — derived from the dominant `bildungsplan` chapter:
    3.x.1 -> themen
    3.x.2 -> interkulturell
    3.x.3 -> kommunikativ
    3.x.4 -> text-medien
  When an article cites multiple chapters (the common case),
  the topic is whichever family appears most often. Ties are broken by
  the canonical order above (themen first, text-medien last) so the
  result is deterministic and stable across re-runs.

Idempotent: running twice produces the same output. Safe to invoke
in CI before `hugo --minify`.
"""
from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"

FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n?", re.DOTALL)
CHAPTER_RE = re.compile(r"^(\d+\.\d+(?:\.\d+){0,2})")  # 3.1, 3.1.3, 3.1.3.8

TOPIC_BY_FAMILY = {
    "1": "themen",
    "2": "interkulturell",
    "3": "kommunikativ",
    "4": "text-medien",
}
# Topic priority is from MOST DISCRIMINATING to LEAST:
#   interkulturell — cited by ~25% of articles (46/180), strongest signal.
#   text-medien    — cited by ~60% (107/180).
#   themen         — cited by ~100% (180/180), least discriminating but
#                    captures everything-without-an-ic-or-tm-hook.
#   kommunikativ   — also ~100% but maps to functional skills, which are
#                    already exposed via `skills_focus` tags. We omit it
#                    from data/topics.yml deliberately so the topic axis
#                    encodes what an article is ABOUT, not which skills
#                    it teaches.
TOPIC_PRIORITY = ["interkulturell", "text-medien", "themen"]


def split_fm(text: str) -> tuple[str, str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return "", text
    return m.group(1), text[m.end():]


def yaml_list(fm: str, key: str) -> list[str]:
    m = re.search(rf"^{re.escape(key)}:\s*$", fm, re.MULTILINE)
    if not m:
        return []
    end = fm.find("\n", m.end())
    items: list[str] = []
    for line in fm[end + 1:].splitlines():
        if not line.startswith(("  ", "\t")):
            break
        ml = re.match(r"\s+-\s*(.*)", line)
        if ml:
            v = ml.group(1).strip().strip('"').strip("'")
            if v:
                items.append(v)
    return items


def has_block(fm: str, key: str) -> bool:
    return bool(re.search(rf"^{re.escape(key)}:\s*$", fm, re.MULTILINE))


def strip_block(fm: str, key: str) -> str:
    """Remove a top-level mapping `key:` and its indented children."""
    lines = fm.splitlines()
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if (re.match(rf"^{re.escape(key)}:\s*$", line) or
                re.match(rf"^{re.escape(key)}:\s*\S", line)):
            i += 1
            while i < len(lines) and (lines[i].startswith(" ") or
                                       lines[i].startswith("\t")):
                if not lines[i].startswith((" ", "\t")):
                    break
                i += 1
            continue
        out.append(line)
        i += 1
    return "\n".join(out).rstrip("\n")


def chapter_code(bildungsplan_entry: str) -> str | None:
    m = CHAPTER_RE.match(bildungsplan_entry.strip())
    return m.group(1) if m else None


def topic_for_codes(codes: list[str]) -> str | None:
    """Map a list of chapter codes (e.g. ["3.1.3.3", "3.1.1"]) to one topic."""
    counts: Counter[str] = Counter()
    for c in codes:
        # The family is the third dotted component: 3.X.<family>... or 3.<family> (Sek II uses 3.2.X).
        parts = c.split(".")
        # Codes look like "3.1.3.x" (Sek I) or "3.2.3.x" (Sek II). The family
        # digit is the third component (index 2).
        if len(parts) < 3:
            continue
        fam = parts[2]
        topic = TOPIC_BY_FAMILY.get(fam)
        if topic:
            counts[topic] += 1
    if not counts:
        return None
    # Pick the highest-priority topic that's cited at all. Count is used
    # only as a secondary tie-breaker between equally-prioritised topics
    # (in practice never triggers because the priority list is total).
    cited = set(counts)
    for t in TOPIC_PRIORITY:
        if t in cited:
            return t
    return None


def derive_tags(skills: list[str], bildungsplan: list[str]) -> list[str]:
    codes = [c for c in (chapter_code(b) for b in bildungsplan) if c]
    seen: set[str] = set()
    out: list[str] = []
    for t in [*skills, *codes]:
        if t not in seen:
            seen.add(t)
            out.append(t)
    return out


def fmt_tags_block(tags: list[str]) -> str:
    return "tags:\n" + "\n".join(f'  - "{t}"' for t in tags)


def process(md: Path) -> bool:
    text = md.read_text(encoding="utf-8")
    fm, body = split_fm(text)
    if not fm:
        return False
    if not has_block(fm, "presentation"):
        return False  # not a material-bearing article

    skills = yaml_list(fm, "skills_focus")
    bildungsplan = yaml_list(fm, "bildungsplan")

    tags = derive_tags(skills, bildungsplan)
    topic = topic_for_codes(
        [c for c in (chapter_code(b) for b in bildungsplan) if c]
    )
    if not tags or not topic:
        print(f"  WARN insufficient data: {md.relative_to(ROOT).as_posix()}",
              file=sys.stderr)
        return False

    new_fm = strip_block(fm, "tags")
    new_fm = strip_block(new_fm, "topic")
    new_fm = new_fm.rstrip() + "\n" + fmt_tags_block(tags) + f"\ntopic: {topic}"

    md.write_text("---\n" + new_fm + "\n---\n" + body, encoding="utf-8")
    return True


def main() -> int:
    n = 0
    skipped = 0
    for md in sorted(CONTENT.rglob("*.md")):
        if md.parent.name.endswith("-exam"):
            continue
        if md.parent.parent.name != "units":
            continue
        if process(md):
            n += 1
        else:
            skipped += 1
    print(f"Populated tags+topic on {n} pages (skipped {skipped}).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
