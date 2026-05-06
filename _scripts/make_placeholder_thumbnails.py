"""Render thumbnail PNGs from the actual placeholder binaries.

For every Unit:
    static/downloads/<track>/kl<NN>/unit<NN>_<slug>_worksheet.pdf
        -> static/materials/worksheets/<track>/kl<NN>/unit<NN>_<slug>.png
    static/materials/presentations/<track>/kl<NN>/unit<NN>_<slug>.pptx
        -> static/materials/presentations/<track>/kl<NN>/unit<NN>_<slug>.png

Rendering pipeline:
  - PDFs    -> pypdfium2 (self-contained PDFium binding, no system deps).
  - PPTXs   -> LibreOffice headless converts to PDF, then pypdfium2.
                LibreOffice ships pre-installed on GitHub-hosted Ubuntu
                runners. When unavailable locally (e.g. on Windows
                without LibreOffice), we fall back to a Pillow-rendered
                synthetic title card so local previews still have *some*
                thumbnail. The CI build always uses the real-render path.

When real materials replace the placeholder binaries, this same script
produces real thumbnails — drop a real `.pptx` or `.pdf` at the
canonical path and re-run.
"""
from __future__ import annotations

import argparse
import pathlib
import shutil
import subprocess
import sys
import tempfile

import pypdfium2 as pdfium
import yaml
from PIL import Image, ImageDraw, ImageFont

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent
OUTLINE = REPO / "_resources" / "curriculum_outline.yml"
WORKSHEETS_OUT = REPO / "static" / "materials" / "worksheets"
PRESENTATIONS_OUT = REPO / "static" / "materials" / "presentations"
WORKSHEETS_BIN = REPO / "static" / "downloads"
PRESENTATIONS_BIN = REPO / "static" / "materials" / "presentations"

THUMB_SCALE = 1.5  # PDFium DPI multiplier; ~108 DPI at default 72.
MAX_DIM = 1024     # cap thumbnail max dimension (downscale after render).


def find_libreoffice() -> str | None:
    for cmd in ("soffice", "libreoffice"):
        if shutil.which(cmd):
            return cmd
    # Common Windows install locations.
    for p in (
        r"C:\Program Files\LibreOffice\program\soffice.exe",
        r"C:\Program Files (x86)\LibreOffice\program\soffice.exe",
    ):
        if pathlib.Path(p).is_file():
            return p
    return None


SOFFICE = find_libreoffice()


def render_pdf_first_page(pdf_path: pathlib.Path, out: pathlib.Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    doc = pdfium.PdfDocument(str(pdf_path))
    if len(doc) == 0:
        raise RuntimeError(f"empty PDF: {pdf_path}")
    img = doc[0].render(scale=THUMB_SCALE).to_pil()
    if max(img.size) > MAX_DIM:
        ratio = MAX_DIM / max(img.size)
        img = img.resize((int(img.width * ratio), int(img.height * ratio)),
                         Image.LANCZOS)
    img.save(out, format="PNG", optimize=True)


def render_pptx_first_slide(pptx_path: pathlib.Path, out: pathlib.Path) -> None:
    """LibreOffice -> PDF -> pypdfium2 -> PNG. Falls back to synthesis."""
    if SOFFICE is None:
        _render_pptx_synthetic(pptx_path, out)
        return
    with tempfile.TemporaryDirectory() as td:
        td_path = pathlib.Path(td)
        try:
            result = subprocess.run(
                [SOFFICE, "--headless", "--convert-to", "pdf",
                 "--outdir", str(td_path), str(pptx_path)],
                capture_output=True, text=True, timeout=120,
            )
        except subprocess.TimeoutExpired:
            print(f"  TIMEOUT converting {pptx_path.name}; falling back",
                  file=sys.stderr)
            _render_pptx_synthetic(pptx_path, out)
            return
        if result.returncode != 0:
            print(f"  soffice error on {pptx_path.name}: "
                  f"{result.stderr.strip()[:200]}", file=sys.stderr)
            _render_pptx_synthetic(pptx_path, out)
            return
        produced = td_path / (pptx_path.stem + ".pdf")
        if not produced.is_file():
            _render_pptx_synthetic(pptx_path, out)
            return
        render_pdf_first_page(produced, out)


def _render_pptx_synthetic(pptx_path: pathlib.Path, out: pathlib.Path) -> None:
    """Fallback used when LibreOffice is unavailable. The title is the
    PPTX core property `title`; otherwise the file stem."""
    out.parent.mkdir(parents=True, exist_ok=True)
    title = pptx_path.stem
    try:
        from pptx import Presentation
        title = Presentation(str(pptx_path)).core_properties.title or title
    except Exception:
        pass
    w, h = 800, 450
    img = Image.new("RGB", (w, h), (245, 247, 250))
    draw = ImageDraw.Draw(img)
    draw.rectangle([(0, 0), (w, 8)], fill=(60, 90, 160))
    try:
        font = ImageFont.truetype("DejaVuSans.ttf", 30)
        small = ImageFont.truetype("DejaVuSans.ttf", 16)
    except (OSError, IOError):
        font = ImageFont.load_default()
        small = font
    draw.text((40, 60), "PRESENTATION", font=small, fill=(60, 90, 160))
    draw.text((40, 96), title[:60], font=font, fill=(34, 34, 34))
    draw.text((40, h - 60), "Synthetic preview — install LibreOffice for real render.",
              font=small, fill=(140, 140, 140))
    img.save(out, format="PNG", optimize=True)


def iter_units(outline: dict):
    for course in outline.get("courses", []):
        track = course["track"]
        klasse = int(course["klassenstufe"])
        for unit in course.get("units", []):
            yield {
                "track": track,
                "klasse": klasse,
                "unit_nr": int(unit["unit_nr"]),
                "slug": unit["slug"],
            }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--worksheets-out", default=str(WORKSHEETS_OUT))
    ap.add_argument("--presentations-out", default=str(PRESENTATIONS_OUT))
    ap.add_argument("--worksheets-bin", default=str(WORKSHEETS_BIN))
    ap.add_argument("--presentations-bin", default=str(PRESENTATIONS_BIN))
    args = ap.parse_args()

    if not OUTLINE.exists():
        print(f"WARN: {OUTLINE} not found.", file=sys.stderr)
        return 0

    print(f"LibreOffice: {SOFFICE or 'NOT FOUND (synthetic fallback for .pptx)'}")
    print(f"PDFium:      pypdfium2 ready")

    outline = yaml.safe_load(OUTLINE.read_text(encoding="utf-8")) or {}
    ws_base, pr_base = pathlib.Path(args.worksheets_out), pathlib.Path(args.presentations_out)
    ws_bin, pr_bin = pathlib.Path(args.worksheets_bin), pathlib.Path(args.presentations_bin)

    n_ws = n_pr = 0
    for u in iter_units(outline):
        nn, kk = f"{u['unit_nr']:02d}", f"{u['klasse']:02d}"
        slug, track = u["slug"], u["track"]
        # Worksheet thumbnail.
        pdf = ws_bin / track / f"kl{kk}" / f"unit{nn}_{slug}_worksheet.pdf"
        if pdf.is_file():
            out = ws_base / track / f"kl{kk}" / f"unit{nn}_{slug}.png"
            try:
                render_pdf_first_page(pdf, out)
                n_ws += 1
            except Exception as e:
                print(f"  WS fail {pdf.name}: {e}", file=sys.stderr)
        # Presentation thumbnail.
        pptx = pr_bin / track / f"kl{kk}" / f"unit{nn}_{slug}.pptx"
        if pptx.is_file():
            out = pr_base / track / f"kl{kk}" / f"unit{nn}_{slug}.png"
            try:
                render_pptx_first_slide(pptx, out)
                n_pr += 1
            except Exception as e:
                print(f"  PR fail {pptx.name}: {e}", file=sys.stderr)
    print(f"Wrote {n_ws} worksheet + {n_pr} presentation thumbnails.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
