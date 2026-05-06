"""Phase 1 front-matter sanity check.

Per the post-migration brief, every content/**/*.md must have:
- title
- author == "S. Le Boulanger" (or contains "Le Boulanger")
- For unit-content pages: klassenstufe + bildungsplan + tags + topic
  (Note: the brief calls the field `bildungsplan_ref`, but this repo
  has used `bildungsplan` since the qmd era — preserved verbatim in
  every unit's frontmatter. Treat the existing key as canonical.)

Reports gaps; does not modify anything. Exits non-zero with a punch
list of every page missing a required field.
"""
from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"

FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n?", re.DOTALL)

# Pages that aren't lesson/unit content and have a different required-fields
# contract. Top-level + appendices + materials hub all live here.
NON_UNIT_PATHS = {
    "content/_index.md",
    "content/about/index.md",
    "content/get-started/index.md",
    "content/bildungsplan/index.md",
    "content/schedule/index.md",
    "content/references/index.md",
    "content/acknowledgements/index.md",
    "content/impressum/index.md",
    "content/datenschutz/index.md",
    "content/haftungsausschluss/index.md",
    "content/appendices/teaching-workflow/index.md",
    "content/appendices/skills-decision-tree/index.md",
    "content/appendices/glossary/index.md",
    "content/appendices/common-errors/index.md",
    "content/appendices/writing-rubrics/index.md",
    "content/materials/_index.md",
    "content/materials/presentations/_index.md",
    "content/materials/worksheets/_index.md",
}


def fm(text: str) -> str:
    m = FRONTMATTER_RE.match(text)
    return m.group(1) if m else ""


def has_key(fm_str: str, key: str) -> bool:
    return bool(re.search(rf"^{re.escape(key)}:\s*\S", fm_str, re.MULTILINE)) or \
           bool(re.search(rf"^{re.escape(key)}:\s*$", fm_str, re.MULTILINE))


def value(fm_str: str, key: str) -> str | None:
    m = re.search(rf"^{re.escape(key)}:\s*(.+)$", fm_str, re.MULTILINE)
    if not m:
        return None
    return m.group(1).strip().strip('"').strip("'") or None


def is_unit_page(p: Path) -> bool:
    """Unit pages live under track-{e,gm}/kl<NN>/units/<slug>/index.md
    and are NOT exam wrappers."""
    rel = p.relative_to(ROOT).as_posix()
    if not re.match(r"content/track-(e|gm)/kl\d{2}/units/[^/]+/index\.md$", rel):
        return False
    if rel.endswith("-exam/index.md"):
        return False
    return True


def is_exam_wrapper(p: Path) -> bool:
    rel = p.relative_to(ROOT).as_posix()
    return rel.endswith("-exam/index.md")


def is_content_page(p: Path) -> bool:
    """Anything that should carry an author + title."""
    rel = p.relative_to(ROOT).as_posix()
    if rel in NON_UNIT_PATHS:
        return True
    if re.match(r"content/track-(e|gm)/kl\d{2}/_index\.md$", rel):
        return True
    if re.match(r"content/track-(e|gm)/kl\d{2}/schedule/index\.md$", rel):
        return True
    if is_unit_page(p) or is_exam_wrapper(p):
        return True
    return False


def main() -> int:
    rows: list[tuple[str, list[str]]] = []
    n_pages = n_units = 0

    for md in sorted(CONTENT.rglob("*.md")):
        if not is_content_page(md):
            continue
        n_pages += 1
        rel = md.relative_to(ROOT).as_posix()
        f = fm(md.read_text(encoding="utf-8"))

        missing: list[str] = []

        if not value(f, "title"):
            missing.append("title")
        # author: either explicit or inherited from the now-removed
        # _metadata.yml. In Hugo we keep author as an explicit param
        # site-wide (params.author = "S. Le Boulanger" in hugo.toml)
        # but content pages should still carry author when feasible.
        if not value(f, "author"):
            missing.append("author")
        else:
            a = value(f, "author") or ""
            if "Le Boulanger" not in a:
                missing.append(f"author!=Le Boulanger ({a!r})")

        if is_unit_page(md):
            n_units += 1
            for k in ("klassenstufe", "track", "unit_nr", "unit_slug",
                      "tags", "topic", "bildungsplan"):
                if not has_key(f, k):
                    missing.append(k)

        if missing:
            rows.append((rel, missing))

    print(f"Audited {n_pages} content pages ({n_units} unit pages).")
    if not rows:
        print("All required front-matter fields present.")
        return 0
    print(f"\n{len(rows)} page(s) missing required front-matter fields:")
    for rel, miss in rows[:30]:
        print(f"  {rel}: {', '.join(miss)}")
    if len(rows) > 30:
        print(f"  …and {len(rows) - 30} more")
    keys = Counter()
    for _, miss in rows:
        for k in miss:
            keys[k.split("!=")[0].split(" ")[0]] += 1
    print("\nMissing-field histogram:")
    for k, v in keys.most_common():
        print(f"  {k}: {v}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
