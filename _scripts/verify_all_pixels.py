#!/usr/bin/env python3
"""Verify every row in vgwort-manifest.csv survived migration to content/.

Walks the whole manifest, maps each .qmd to its Hugo .md destination
(handling underscore-prefixed exam-body partials by checking the wrapper),
and confirms the pixel URL appears exactly once. Exits non-zero on any
discrepancy.
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
        if not parent:
            return ROOT / "content" / "_index.md"
        return ROOT.joinpath("content", *new_parent, "_index.md")
    if not parent:
        return ROOT / "content" / hugo_slug(stem) / "index.md"
    return ROOT.joinpath("content", *new_parent, hugo_slug(stem), "index.md")


def main() -> int:
    rows = list(csv.DictReader((ROOT / "vgwort-manifest.csv").open(encoding="utf-8")))
    ok = miss = dup = 0
    for r in rows:
        qmd = r["qmd_path"]
        url = r["pixel_url"]
        # Underscore-prefixed exam-body partials: pixel travels with body
        # into the matching exam wrapper AND the unit page (it appears in
        # both); count occurrences in the exam wrapper as canonical.
        name = Path(qmd).name
        if name.startswith("_unit") and qmd.endswith("_exam_body.qmd"):
            wrapper = qmd.replace("_exam_body.qmd", "_exam.qmd").replace(
                "/_unit", "/unit"
            )
            dest = map_path(wrapper)
        else:
            dest = map_path(qmd)
        if not dest.exists():
            print(f"MISSING dest: {qmd} -> {dest}")
            miss += 1
            continue
        body = dest.read_text(encoding="utf-8")
        n = body.count(url)
        if n == 0:
            print(f"MISSING pixel: {qmd} (expected {url})")
            miss += 1
        elif n > 1:
            print(f"DUPLICATE pixel: {qmd} appears {n}x in {dest}")
            dup += 1
            ok += 1
        else:
            ok += 1
    print(f"\nok={ok} missing={miss} duplicated={dup} total={len(rows)}")
    return 0 if (miss == 0 and dup == 0) else 1


if __name__ == "__main__":
    raise SystemExit(main())
