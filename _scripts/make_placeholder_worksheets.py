"""Generate placeholder worksheet PDFs for every EFL Unit.

Reads `_resources/curriculum_outline.yml` and emits one A4 PDF per Unit at
`docs/downloads/<track>/kl<NN>/unit<NN>_<slug>_worksheet.pdf`.

Each placeholder carries the standard EFL attribution: PDF metadata,
header line, body block, footer line, and a diagonal author watermark.
When real worksheets exist, drop them at the same canonical path; no
site-code change needed.
"""

from __future__ import annotations

import argparse
import pathlib
import sys

import yaml
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen.canvas import Canvas

# Make sibling helpers importable when running from repo root.
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from pdf_attribution import AttributionContext, apply_attribution  # noqa: E402

REPO = HERE.parent
OUTLINE = REPO / "_resources" / "curriculum_outline.yml"
DOCS = REPO / "docs"


def render_one(out_path: pathlib.Path, ctx: AttributionContext, title: str) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    width, height = A4
    c = Canvas(str(out_path), pagesize=A4)

    # Body content first (drawn under the watermark).
    c.setFont("Helvetica-Bold", 18)
    c.setFillGray(0.15)
    c.drawString(54, height - 100, f"Worksheet — Unit {ctx.unit_nr}: {title}")

    c.setFont("Helvetica", 11)
    c.setFillGray(0.3)
    track_label = "G+M" if ctx.track == "gm" else "E"
    c.drawString(
        54, height - 124,
        f"Niveau {ctx.niveau} · Klasse {ctx.klasse} · Track {track_label}"
    )

    c.setFont("Helvetica-Oblique", 11)
    c.setFillGray(0.25)
    c.drawString(54, height - 170, "Placeholder — worksheet content to follow.")

    c.setFont("Helvetica", 10)
    c.setFillGray(0.4)
    c.drawString(
        54, height - 200,
        "Real exercises (Activate, Input, Practise, Produce, Reflect) will be added "
        "in a later authoring pass."
    )

    apply_attribution(c, ctx, page_size=A4, with_metadata=True)

    c.showPage()
    c.save()


def iter_units(outline: dict):
    for course in outline.get("courses", []):
        track = course["track"]
        klasse = int(course["klassenstufe"])
        niveau = course.get("niveau", "")
        for unit in course.get("units", []):
            yield {
                "track": track,
                "klasse": klasse,
                "niveau": unit.get("niveau", niveau),
                "unit_nr": int(unit["unit_nr"]),
                "slug": unit["slug"],
                "title": unit["title"],
            }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--course", default=None,
                        help="Generate only one course (e.g. track_gm_kl07).")
    parser.add_argument("--out", default=str(DOCS / "downloads"),
                        help="Output base directory (default: docs/downloads).")
    args = parser.parse_args()

    if not OUTLINE.exists():
        print(f"WARN: {OUTLINE} not found — no units to render.", file=sys.stderr)
        print("This is expected before Phase 2 (curriculum outline).", file=sys.stderr)
        return 0

    with OUTLINE.open(encoding="utf-8") as f:
        outline = yaml.safe_load(f) or {}

    out_base = pathlib.Path(args.out)
    count = 0
    for u in iter_units(outline):
        course_id = f"track_{u['track']}_kl{u['klasse']:02d}"
        if args.course and course_id != args.course:
            continue
        nn = f"{u['unit_nr']:02d}"
        kk = f"{u['klasse']:02d}"
        path = out_base / u["track"] / f"kl{kk}" / f"unit{nn}_{u['slug']}_worksheet.pdf"
        ctx = AttributionContext(
            track=u["track"],
            klasse=u["klasse"],
            unit_nr=u["unit_nr"],
            niveau=u["niveau"],
            title=u["title"],
        )
        render_one(path, ctx, u["title"])
        count += 1

    print(f"Wrote {count} placeholder worksheet PDF(s) under {out_base}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
