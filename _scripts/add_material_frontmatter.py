"""Augment Hugo unit-page front matter with material attachments.

For every `content/track-*/kl<NN>/units/unit<NN>-<slug>/index.md` (the
unit page itself — NOT the `-exam` wrapper, NOT the track index, NOT the
schedule), insert two YAML blocks linking the placeholder presentation
.pptx + thumbnail and the existing worksheet PDF + new thumbnail.

Idempotent: if the keys already exist, replace them. Reads the existing
front-matter `track`, `klassenstufe`, `unit_nr`, `unit_slug` to compute
the canonical paths.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UNITS_GLOB = "content/track-*/kl*/units/*/index.md"

FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n?", re.DOTALL)


def split_fm(text: str) -> tuple[str, str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return "", text
    return m.group(1), text[m.end():]


def yaml_get(fm: str, key: str) -> str | None:
    m = re.search(rf"^{re.escape(key)}:\s*(.*)$", fm, re.MULTILINE)
    if not m:
        return None
    val = m.group(1).strip().strip('"').strip("'")
    return val or None


def strip_existing(fm: str, key: str) -> str:
    """Remove a top-level mapping `key:` and its indented children."""
    lines = fm.splitlines()
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if re.match(rf"^{re.escape(key)}:\s*$", line) or re.match(
                rf"^{re.escape(key)}:\s*\S", line):
            i += 1
            while i < len(lines) and (lines[i].startswith(" ") or
                                       lines[i].startswith("\t") or
                                       lines[i].strip() == ""):
                # Stop at next top-level key
                if lines[i].strip() == "" and (
                        i + 1 < len(lines) and re.match(
                            r"^\S", lines[i + 1])):
                    break
                if re.match(r"^\S", lines[i]):
                    break
                i += 1
            continue
        out.append(line)
        i += 1
    return "\n".join(out).strip("\n")


def material_block(track: str, klasse: str, unit_nr: str,
                   unit_slug: str) -> str:
    kk = f"{int(klasse):02d}"
    nn = f"{int(unit_nr):02d}"
    pres_file = f"/materials/presentations/{track}/kl{kk}/unit{nn}_{unit_slug}.pptx"
    pres_thumb = f"/materials/presentations/{track}/kl{kk}/unit{nn}_{unit_slug}.png"
    ws_file = f"/downloads/{track}/kl{kk}/unit{nn}_{unit_slug}_worksheet.pdf"
    ws_thumb = f"/materials/worksheets/{track}/kl{kk}/unit{nn}_{unit_slug}.png"
    return (
        f"presentation:\n"
        f"  file: {pres_file}\n"
        f"  thumbnail: {pres_thumb}\n"
        f"worksheet:\n"
        f"  file: {ws_file}\n"
        f"  thumbnail: {ws_thumb}"
    )


def process(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    fm, body = split_fm(text)
    if not fm:
        return False

    track = yaml_get(fm, "track")
    klasse = yaml_get(fm, "klassenstufe")
    unit_nr = yaml_get(fm, "unit_nr")
    unit_slug = yaml_get(fm, "unit_slug")
    if not all([track, klasse, unit_nr, unit_slug]):
        return False

    fm = strip_existing(fm, "presentation")
    fm = strip_existing(fm, "worksheet")

    block = material_block(track, klasse, unit_nr, unit_slug)
    new_fm = fm.rstrip() + "\n" + block

    path.write_text("---\n" + new_fm + "\n---\n" + body, encoding="utf-8")
    return True


def main() -> int:
    n = skipped = 0
    for path in sorted(ROOT.glob(UNITS_GLOB)):
        # Skip exam wrappers — exam IS the page, not an attachment.
        if path.parent.name.endswith("-exam"):
            skipped += 1
            continue
        if process(path):
            n += 1
        else:
            skipped += 1
    print(f"Augmented {n} unit pages with material front matter "
          f"(skipped {skipped}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
