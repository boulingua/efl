"""Phase 6 tracking gates.

1. /materials/ loads Plausible — discovery hub is part of the site.
2. /materials/ does NOT carry a VG Wort pixel — the hub is navigation,
   not editorial content (Phase 0 §8 decision 4 + the prompt's Phase 6
   spec).
3. A representative unit page does carry a VG Wort pixel — pixels are
   per-article and must travel with the migrated content.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"

PLAUSIBLE_RE = re.compile(r'data-domain="?boulingua\.github\.io/efl"?')
PIXEL_RE = re.compile(r"vg0\d\.met\.vgwort\.de/na/[0-9a-f]{32}")


def page_html(rel: str) -> str | None:
    p = PUBLIC / rel.strip("/") / "index.html"
    if not p.is_file():
        return None
    return p.read_text(encoding="utf-8")


def main() -> int:
    errors: list[str] = []

    materials = page_html("materials")
    if materials is None:
        errors.append("GATE FAIL: public/materials/index.html missing.")
    else:
        if not PLAUSIBLE_RE.search(materials):
            errors.append("GATE FAIL: /materials/ has no Plausible script.")
        if PIXEL_RE.search(materials):
            errors.append("GATE FAIL: /materials/ carries a VG Wort pixel "
                          "(navigation pages must not).")

    # Pick the canonical first unit page that survives all migration phases.
    unit = page_html("track-e/kl05/units/unit01-hello-world")
    if unit is None:
        errors.append("GATE FAIL: canonical unit page missing.")
    else:
        if not PIXEL_RE.search(unit):
            errors.append("GATE FAIL: unit page has no VG Wort pixel.")
        if not PLAUSIBLE_RE.search(unit):
            errors.append("GATE FAIL: unit page has no Plausible script.")

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("Tracking gates OK: Plausible everywhere, VG Wort on unit pages "
          "only, /materials/ free of pixels.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
