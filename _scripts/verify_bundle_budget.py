"""Phase 6 perf gate: enforce the JS bundle-size budget for /materials/.

The Materials Discovery Network specifies <=280KB gzipped for the JS
loaded by /materials/. Cytoscape.js is ~150KB on its own; our app code,
filters, search, list, and store add roughly another 5-10KB. Pagefind's
runtime is loaded separately on first keystroke and is not counted here.
"""
from __future__ import annotations

import gzip
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC_JS = ROOT / "public" / "js"

LIMIT_KB = 280


def main() -> int:
    if not PUBLIC_JS.is_dir():
        print(f"GATE FAIL: {PUBLIC_JS.relative_to(ROOT)} missing — "
              f"run `hugo --minify` first.", file=sys.stderr)
        return 1
    bundles = list(PUBLIC_JS.glob("network.bundle.*.js"))
    if not bundles:
        print("GATE FAIL: no network.bundle.*.js produced — "
              "Hugo's js.Build did not emit the entry.", file=sys.stderr)
        return 1
    total_gz = 0
    rows: list[tuple[str, int, int]] = []
    for b in bundles:
        raw = b.read_bytes()
        gz = len(gzip.compress(raw))
        total_gz += gz
        rows.append((b.name, len(raw), gz))
    for name, raw, gz in rows:
        print(f"  {name}: {raw/1024:.1f} KB raw / {gz/1024:.1f} KB gzip")
    print(f"  total: {total_gz/1024:.1f} KB gzipped (budget {LIMIT_KB} KB)")
    if total_gz / 1024 > LIMIT_KB:
        print(f"GATE FAIL: bundle exceeds {LIMIT_KB} KB gzipped.",
              file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
