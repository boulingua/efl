"""Phase 6.2 — Bildungsplan BW live-fetch hard-stop.

For every `_resources/bildungsplan_bw_*.yml` source URL, hit
`bildungsplaene-bw.de` and confirm it returns 200. Per the
post-migration brief: hard-stop on fetch failure. Do NOT fall back
to cached content. Do NOT invent curriculum text.

Caching: a 24h response cache lives at `_resources/.bildungsplan_cache/`
(gitignored). On cache hit a 200 response is the same as a freshly-
fetched 200 (we re-fetch on the next 24h-window expiry). On miss we
fetch live; on a live failure (timeout, 5xx, 4xx, DNS) we exit non-zero.

The cache is a performance optimisation, never a substitute for a
live failure — its TTL is short enough that any real outage on
bildungsplaene-bw.de will surface within a day.
"""
from __future__ import annotations

import json
import ssl
import sys
import time
import urllib.error
import urllib.request
from hashlib import sha1
from pathlib import Path

import yaml

# Use certifi's CA bundle when present (fixes Windows-local SSL trust
# issues). On Ubuntu CI runners the system store works fine; certifi
# is harmless to prefer everywhere.
try:
    import certifi
    _SSL_CTX = ssl.create_default_context(cafile=certifi.where())
except ImportError:
    _SSL_CTX = ssl.create_default_context()

ROOT = Path(__file__).resolve().parents[1]
RESOURCES = ROOT / "_resources"
CACHE = RESOURCES / ".bildungsplan_cache"
CACHE_TTL_S = 24 * 3600
TIMEOUT_S = 30


def cache_path(url: str) -> Path:
    return CACHE / (sha1(url.encode("utf-8")).hexdigest() + ".json")


def fetch(url: str) -> tuple[int, str | None]:
    cp = cache_path(url)
    if cp.is_file():
        try:
            data = json.loads(cp.read_text(encoding="utf-8"))
            if time.time() - data["ts"] < CACHE_TTL_S:
                return data["status"], data.get("err")
        except Exception:
            pass

    try:
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "boulingua-efl-ci/1.0 (+verify_bildungsplan_refs)"},
        )
        with urllib.request.urlopen(req, timeout=TIMEOUT_S, context=_SSL_CTX) as resp:
            status = resp.status
            err = None
    except urllib.error.HTTPError as e:
        status, err = e.code, str(e)
    except Exception as e:
        status, err = 0, f"{type(e).__name__}: {e}"

    CACHE.mkdir(parents=True, exist_ok=True)
    cp.write_text(json.dumps({"ts": time.time(), "status": status, "err": err}),
                  encoding="utf-8")
    return status, err


def collect_urls() -> set[str]:
    urls: set[str] = set()
    for y in RESOURCES.glob("bildungsplan_bw_*.yml"):
        data = yaml.safe_load(y.read_text(encoding="utf-8")) or {}
        for u in data.get("source_urls", []) or []:
            if isinstance(u, str) and u.startswith("http"):
                urls.add(u)
    return urls


def main() -> int:
    urls = collect_urls()
    if not urls:
        print("No bildungsplan source URLs to verify.", file=sys.stderr)
        return 0

    failures: list[tuple[str, int, str | None]] = []
    print(f"Verifying {len(urls)} Bildungsplan BW source URL(s) (live fetch, "
          f"24h cache).")
    for u in sorted(urls):
        status, err = fetch(u)
        ok = status == 200
        marker = "OK " if ok else "FAIL"
        print(f"  [{marker}] {status:>3}  {u}")
        if not ok:
            failures.append((u, status, err))

    if failures:
        print(f"\nGATE FAIL: {len(failures)} Bildungsplan URL(s) "
              f"unreachable. Per the brief: do NOT fall back to cached "
              f"content; do NOT invent curriculum text. Fix the URLs in "
              f"_resources/bildungsplan_bw_*.yml or wait for the source "
              f"site to recover.", file=sys.stderr)
        for u, s, e in failures:
            print(f"  {u}: status={s} err={e}", file=sys.stderr)
        return 1
    print(f"\nAll {len(urls)} Bildungsplan source URLs reachable.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
