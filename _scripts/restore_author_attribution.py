"""Restore explicit `author: "S. Le Boulanger"` to every content page's
frontmatter, where it was inherited from the now-removed
`<course>/units/_metadata.yml` in the Quarto era.

Idempotent. Skips pages that already declare an author.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
AUTHOR = '"S. Le Boulanger"'

FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n?", re.DOTALL)
AUTHOR_RE = re.compile(r"^author:\s*\S", re.MULTILINE)
TITLE_RE = re.compile(r"^title:\s*.+$", re.MULTILINE)


# Same set of "is this a content page" rules as audit_frontmatter.py.
NON_UNIT_PATHS = {
    "content/_index.md", "content/about/index.md",
    "content/get-started/index.md", "content/bildungsplan/index.md",
    "content/schedule/index.md", "content/references/index.md",
    "content/acknowledgements/index.md", "content/impressum/index.md",
    "content/datenschutz/index.md", "content/haftungsausschluss/index.md",
    "content/appendices/teaching-workflow/index.md",
    "content/appendices/skills-decision-tree/index.md",
    "content/appendices/glossary/index.md",
    "content/appendices/common-errors/index.md",
    "content/appendices/writing-rubrics/index.md",
    "content/materials/_index.md",
    "content/materials/presentations/_index.md",
    "content/materials/worksheets/_index.md",
}


def is_content_page(p: Path) -> bool:
    rel = p.relative_to(ROOT).as_posix()
    if rel in NON_UNIT_PATHS:
        return True
    if re.match(r"content/track-(e|gm)/kl\d{2}/(_index|schedule/index)\.md$", rel):
        return True
    if re.match(r"content/track-(e|gm)/kl\d{2}/units/[^/]+/index\.md$", rel):
        return True
    return False


def main() -> int:
    fixed = skipped = 0
    for md in sorted(CONTENT.rglob("*.md")):
        if not is_content_page(md):
            continue
        text = md.read_text(encoding="utf-8")
        m = FRONTMATTER_RE.match(text)
        if not m:
            print(f"  WARN: no frontmatter on {md.relative_to(ROOT).as_posix()}",
                  file=sys.stderr)
            continue
        fm, body = m.group(1), text[m.end():]
        if AUTHOR_RE.search(fm):
            skipped += 1
            continue

        # Insert author immediately after title (or at the top if no title).
        tm = TITLE_RE.search(fm)
        if tm:
            insert_at = tm.end()
            new_fm = fm[:insert_at] + f'\nauthor: {AUTHOR}' + fm[insert_at:]
        else:
            new_fm = f'author: {AUTHOR}\n' + fm

        md.write_text("---\n" + new_fm + "\n---\n" + body, encoding="utf-8")
        fixed += 1

    print(f"Added author to {fixed} pages; skipped {skipped} that already had it.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
