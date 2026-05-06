#!/usr/bin/env python3
"""Verify VG Wort pixels survived Phase 2 conversion for one grade folder.

Reads vgwort-manifest.csv, finds rows whose qmd_path lives under the given
folder (e.g. `track_gm_kl05`), maps each to its Hugo destination .md and
checks the pixel URL appears verbatim. Exits non-zero if any pixel is
missing or appears more than once.

Usage:
    python _scripts/verify_grade_pixels.py <folder>
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def hugo_slug(name: str) -> str:
    return name.replace("_", "-")


def map_path(qmd_rel: str) -> Path:
    parts = qmd_rel.split("/")
    name = parts[-1]
    stem = name.removesuffix(".qmd")
    parent = parts[:-1]
    new_parent: list[str] = []
    for p in parent:
        m = re.fullmatch(r"track_(e|gm)_kl(\d{2})", p)
        if m:
            new_parent.extend([f"track-{m.group(1)}", f"kl{m.group(2)}"])
        else:
            new_parent.append(hugo_slug(p))
    if stem == "index":
        return ROOT.joinpath("content", *new_parent, "_index.md")
    if not parent:
        return ROOT / "content" / hugo_slug(stem) / "index.md"
    return ROOT.joinpath("content", *new_parent, hugo_slug(stem), "index.md")


def main(argv: list[str]) -> int:
    if len(argv) != 1:
        print("usage: verify_grade_pixels.py <folder>", file=sys.stderr)
        return 2
    prefix = argv[0].rstrip("/") + "/"
    rows = list(csv.DictReader((ROOT / "vgwort-manifest.csv").open(encoding="utf-8")))
    rows = [r for r in rows if r["qmd_path"].startswith(prefix)]
    if not rows:
        print(f"No manifest rows for prefix {prefix!r}.")
        return 0

    ok = miss = dup = 0
    for r in rows:
        qmd = r["qmd_path"]
        url = r["pixel_url"]
        # Underscore-prefixed bodies are inlined into the matching exam wrapper
        # AND the matching unit page; check the wrapper as canonical home.
        if Path(qmd).name.startswith("_unit") and qmd.endswith("_exam_body.qmd"):
            wrapper = qmd.replace("_exam_body.qmd", "_exam.qmd")
            wrapper = wrapper.replace("/_unit", "/unit")
            dest = map_path(wrapper)
        else:
            dest = map_path(qmd)
        if not dest.exists():
            print(f"MISSING dest file: {qmd} -> {dest}")
            miss += 1
            continue
        body = dest.read_text(encoding="utf-8")
        n = body.count(url)
        if n == 0:
            print(f"MISSING pixel: {qmd} (expected {url} in {dest})")
            miss += 1
        elif n > 1:
            print(f"DUPLICATE pixel: {qmd} appears {n}x in {dest}")
            dup += 1
            ok += 1
        else:
            ok += 1
    print(f"\n{prefix}: ok={ok} missing={miss} duplicated={dup} total={len(rows)}")
    return 0 if (miss == 0 and dup == 0) else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
