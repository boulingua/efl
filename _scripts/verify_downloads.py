"""Verify every article's presentation + worksheet + thumbnail URLs
resolve to a real file under public/.

Reads public/materials/graph.json (built by Hugo from
layouts/materials/list.network.json) and checks that:

  - Every node of type=presentation has a `url` and `thumbnail` that
    exists under public/.
  - Every node of type=worksheet ditto.

Fails the CI build if any download URL would 404. Per-article materials
are placeholder binaries during the migration but are real, openable
.pptx / .pdf / .png files (made by the placeholder generators); when
real materials replace them, this gate continues to enforce that every
article advertises only files that actually ship.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"
GRAPH = PUBLIC / "materials" / "graph.json"


def resolve(rel: str) -> Path | None:
    if not rel:
        return None
    # graph.json URLs include the basePath /efl/. Strip it to land in public/.
    rel = rel.split("#", 1)[0].split("?", 1)[0]
    if rel.startswith("/efl/"):
        rel = rel[len("/efl/"):]
    elif rel.startswith("/"):
        rel = rel[1:]
    p = PUBLIC / rel
    return p if p.is_file() else None


def main() -> int:
    if not GRAPH.is_file():
        print(f"GATE FAIL: {GRAPH.relative_to(ROOT)} missing.", file=sys.stderr)
        return 1
    g = json.loads(GRAPH.read_text(encoding="utf-8"))
    n_total = n_missing = 0
    misses: list[tuple[str, str, str]] = []
    for n in g["nodes"]:
        if n["type"] not in ("presentation", "worksheet"):
            continue
        url, thumb = n.get("url"), n.get("thumbnail")
        for kind, target in (("file", url), ("thumbnail", thumb)):
            if not target:
                misses.append((n["id"], kind, "<empty>"))
                n_missing += 1
            elif resolve(target) is None:
                misses.append((n["id"], kind, target))
                n_missing += 1
            n_total += 1
    print(f"Checked {n_total} download URLs across "
          f"{sum(1 for n in g['nodes'] if n['type'] in ('presentation','worksheet'))} "
          f"material nodes.")
    if misses:
        print(f"\n{n_missing} broken download URL(s):", file=sys.stderr)
        for nid, kind, target in misses[:20]:
            print(f"  {nid} [{kind}] -> {target}", file=sys.stderr)
        if len(misses) > 20:
            print(f"  …and {len(misses) - 20} more", file=sys.stderr)
        return 1
    print("All material download + thumbnail URLs resolve.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
