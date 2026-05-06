"""Phase 6.6 — every PDF under static/ must carry author attribution.

Re-implements the Quarto-era inline gate (was hard-coded in the old
publish.yml). Walks every .pdf produced by the placeholder generators
or shipped manually, asserts the /Author core-property contains
"Le Boulanger".

S. Le Boulanger is the author of all content in this repo. PDFs that
ship without correct attribution would be misattributed in any
downstream context (search, citation, archive). Hard-fail.
"""
from __future__ import annotations

import sys
from pathlib import Path

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
ROOTS = (ROOT / "static" / "downloads",)


def main() -> int:
    pdfs: list[Path] = []
    for r in ROOTS:
        if r.is_dir():
            pdfs.extend(r.rglob("*.pdf"))

    if not pdfs:
        # No PDFs is acceptable on a fresh checkout where placeholder
        # generators haven't run yet. CI runs them before this gate.
        print("No PDFs found under static/downloads/ — nothing to check.")
        return 0

    bad: list[tuple[str, str]] = []
    for p in pdfs:
        try:
            r = PdfReader(str(p))
            md = r.metadata or {}
            author = (md.get("/Author") or "").strip() or ""
        except Exception as e:
            bad.append((p.relative_to(ROOT).as_posix(), f"read error: {e}"))
            continue
        if "Le Boulanger" not in author:
            bad.append((p.relative_to(ROOT).as_posix(),
                        f"author={author!r}"))

    print(f"Audited {len(pdfs)} PDF(s).")
    if bad:
        print(f"\nGATE FAIL: {len(bad)} PDF(s) with missing or wrong "
              f"author attribution:", file=sys.stderr)
        for path, why in bad[:20]:
            print(f"  {path}: {why}", file=sys.stderr)
        if len(bad) > 20:
            print(f"  …and {len(bad) - 20} more", file=sys.stderr)
        return 1
    print(f"All {len(pdfs)} PDFs attribute S. Le Boulanger.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
