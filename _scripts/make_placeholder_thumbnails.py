"""Render thumbnail PNGs for placeholder worksheets and presentations.

Both placeholder generators (`make_placeholder_worksheets.py` and
`make_placeholder_presentations.py`) write binary content but no
thumbnails. Real LibreOffice/Poppler-based rendering is fragile in CI
and overkill for placeholder material; instead, this script produces a
matching one-page thumbnail PNG using Pillow that mirrors what the
binary file's first page contains.

Per Unit:
    static/materials/worksheets/<track>/kl<NN>/unit<NN>_<slug>.png
    static/materials/presentations/<track>/kl<NN>/unit<NN>_<slug>.png

When real materials replace the placeholder binaries, the same path
convention applies — drop a real PNG thumbnail beside the binary and
the Materials hub picks it up.
"""
from __future__ import annotations

import argparse
import pathlib
import sys

import yaml
from PIL import Image, ImageDraw, ImageFont

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent
OUTLINE = REPO / "_resources" / "curriculum_outline.yml"
WORKSHEETS_OUT = REPO / "static" / "materials" / "worksheets"
PRESENTATIONS_OUT = REPO / "static" / "materials" / "presentations"


def _font(size: int) -> ImageFont.ImageFont:
    # Pillow ships a default bitmap font; for placeholders that's enough.
    try:
        return ImageFont.truetype("DejaVuSans.ttf", size)
    except (OSError, IOError):
        try:
            return ImageFont.truetype("arial.ttf", size)
        except (OSError, IOError):
            return ImageFont.load_default()


def render_thumbnail(out_path: pathlib.Path, kind: str, track: str,
                     klasse: int, niveau: str, unit_nr: int,
                     title: str) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)

    # 16:9 for presentation thumbs, 1:sqrt(2) ~ A4 portrait for worksheets.
    if kind == "presentation":
        w, h = 800, 450
        bg, fg, accent = (245, 247, 250), (34, 34, 34), (60, 90, 160)
    else:
        w, h = 600, 848  # ~A4 ratio
        bg, fg, accent = (250, 246, 240), (34, 34, 34), (160, 90, 60)

    img = Image.new("RGB", (w, h), bg)
    draw = ImageDraw.Draw(img)

    pad = 40
    # Top accent bar.
    draw.rectangle([(0, 0), (w, 8)], fill=accent)

    # Kind label.
    label = "Presentation" if kind == "presentation" else "Worksheet"
    draw.text((pad, pad), label.upper(), font=_font(18), fill=accent)

    # Title — wrap manually if long.
    title_text = f"Unit {unit_nr}: {title}"
    title_font = _font(34 if kind == "presentation" else 28)
    wrapped: list[str] = []
    line = ""
    for word in title_text.split():
        candidate = (line + " " + word).strip()
        bbox = draw.textbbox((0, 0), candidate, font=title_font)
        if bbox[2] - bbox[0] > w - 2 * pad and line:
            wrapped.append(line)
            line = word
        else:
            line = candidate
    if line:
        wrapped.append(line)

    y = pad + 36
    for ln in wrapped:
        draw.text((pad, y), ln, font=title_font, fill=fg)
        y += title_font.size + 8

    # Subtitle.
    track_label = "G+M" if track == "gm" else "E"
    sub = f"Track {track_label} · Klasse {klasse} · Niveau {niveau}"
    draw.text((pad, y + 12), sub, font=_font(18), fill=(80, 80, 80))

    # Footer "placeholder" caption.
    caption = "Placeholder — replace with final material."
    draw.text((pad, h - pad - 36), caption, font=_font(16),
              fill=(120, 120, 120))
    draw.text((pad, h - pad - 14),
              f"© S. Le Boulanger · CC-BY-SA 4.0",
              font=_font(12), fill=(140, 140, 140))

    img.save(out_path, format="PNG", optimize=True)


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
    ap = argparse.ArgumentParser()
    ap.add_argument("--worksheets-out", default=str(WORKSHEETS_OUT))
    ap.add_argument("--presentations-out", default=str(PRESENTATIONS_OUT))
    args = ap.parse_args()

    if not OUTLINE.exists():
        print(f"WARN: {OUTLINE} not found.", file=sys.stderr)
        return 0

    with OUTLINE.open(encoding="utf-8") as f:
        outline = yaml.safe_load(f) or {}

    ws_base = pathlib.Path(args.worksheets_out)
    pr_base = pathlib.Path(args.presentations_out)
    n = 0
    for u in iter_units(outline):
        nn = f"{u['unit_nr']:02d}"
        kk = f"{u['klasse']:02d}"
        ws_path = (ws_base / u["track"] / f"kl{kk}" /
                   f"unit{nn}_{u['slug']}.png")
        pr_path = (pr_base / u["track"] / f"kl{kk}" /
                   f"unit{nn}_{u['slug']}.png")
        render_thumbnail(ws_path, "worksheet", u["track"], u["klasse"],
                         u["niveau"], u["unit_nr"], u["title"])
        render_thumbnail(pr_path, "presentation", u["track"], u["klasse"],
                         u["niveau"], u["unit_nr"], u["title"])
        n += 1
    print(f"Wrote {n} worksheet + {n} presentation thumbnail PNG(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
