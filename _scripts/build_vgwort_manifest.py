#!/usr/bin/env python3
"""Build vgwort-manifest.csv from inline VG Wort Zählmarken in .qmd files.

Source of truth for the migration: every row records where a pixel lives now
and what its public ID + URL are. After the Hugo migration, every row must
still match a rendered page in public/.
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Skip generated/cache and the new Hugo content tree (Phase 2 not run yet).
SKIP = {"docs", ".quarto", "_freeze", "_site", "public", "resources",
        ".git", "node_modules", ".venv"}

PIXEL_RE = re.compile(
    r'<img\s+src="(https://vg\d+\.met\.vgwort\.de/na/([0-9a-f]{32}))"',
    re.IGNORECASE,
)


def iter_qmd(root: Path):
    for p in root.rglob("*.qmd"):
        if any(part in SKIP for part in p.relative_to(root).parts):
            continue
        yield p


def slug_from(path: Path) -> str:
    # E.g. track_e_kl05/units/unit01_hello-world.qmd -> "unit01_hello-world"
    return path.stem


def main() -> int:
    rows: list[dict[str, str]] = []
    seen_ids: dict[str, str] = {}  # public_id -> qmd_path (catch duplicates)

    for qmd in sorted(iter_qmd(ROOT)):
        text = qmd.read_text(encoding="utf-8", errors="replace")
        for lineno, line in enumerate(text.splitlines(), start=1):
            m = PIXEL_RE.search(line)
            if not m:
                continue
            pixel_url, public_id = m.group(1), m.group(2)
            qmd_rel = qmd.relative_to(ROOT).as_posix()
            if public_id in seen_ids and seen_ids[public_id] != qmd_rel:
                print(f"WARN duplicate public_id {public_id}: "
                      f"{seen_ids[public_id]} and {qmd_rel}",
                      file=sys.stderr)
            seen_ids[public_id] = qmd_rel
            rows.append({
                "qmd_path": qmd_rel,
                "article_slug": slug_from(qmd),
                "public_id": public_id,
                "pixel_url": pixel_url,
                "source_line": str(lineno),
            })

    out = ROOT / "vgwort-manifest.csv"
    with out.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=["qmd_path", "article_slug", "public_id",
                        "pixel_url", "source_line"],
        )
        w.writeheader()
        w.writerows(rows)

    print(f"Wrote {len(rows)} rows to {out.relative_to(ROOT)}")
    print(f"Unique public IDs: {len(seen_ids)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
