"""Verify every URL on the deployed Quarto site resolves in the new Hugo build.

Fetches https://boulingua.github.io/efl/sitemap.xml (the live Quarto-built
site), extracts every <loc> entry, normalises it to the path relative to
the site root, and checks that the path resolves under public/ either as
a directly-rendered file or as a Hugo alias-redirect.

Exits 0 if every old URL has a destination, non-zero with a punch list
otherwise.

Usage:
    python _scripts/verify_url_parity.py [--sitemap-url URL] [--public DIR]
"""
from __future__ import annotations

import argparse
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

DEFAULT_SITEMAP = "https://boulingua.github.io/efl/sitemap.xml"
DEFAULT_PUBLIC = "public"
SITE_BASE = "/efl"


def fetch_sitemap_urls(url: str) -> list[str]:
    print(f"Fetching {url}…", file=sys.stderr)
    with urllib.request.urlopen(url, timeout=30) as resp:
        body = resp.read()
    root = ET.fromstring(body)
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    return [el.text for el in root.findall("sm:url/sm:loc", ns) if el.text]


def url_to_relpath(url: str) -> str:
    """Strip scheme/host, return the path inside the site root."""
    p = urllib.parse.urlparse(url).path
    if p.startswith(SITE_BASE + "/"):
        p = p[len(SITE_BASE):]
    elif p == SITE_BASE:
        p = "/"
    return p or "/"


def resolves(rel: str, public: Path) -> tuple[bool, str]:
    """Return (resolved, how) — either ('direct', 'alias', or 'missing')."""
    # Hugo writes index.html at directory paths, alias HTML at the named
    # path itself. So /foo/ may resolve to public/foo/index.html, and
    # /foo.html may resolve to public/foo.html as an alias-redirect file.
    if rel.endswith("/"):
        target = public / rel.lstrip("/") / "index.html"
        if target.is_file():
            return True, "direct"
    if rel.endswith(".html"):
        target = public / rel.lstrip("/")
        if target.is_file():
            txt = target.read_text(encoding="utf-8", errors="replace")[:600]
            if "http-equiv=refresh" in txt or 'http-equiv="refresh"' in txt:
                return True, "alias"
            return True, "direct"
    # Fallbacks: try with index.html appended even if no trailing slash.
    target = public / rel.lstrip("/") / "index.html"
    if target.is_file():
        return True, "direct"
    target = public / rel.lstrip("/")
    if target.is_file():
        return True, "direct"
    return False, "missing"


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sitemap-url", default=DEFAULT_SITEMAP)
    ap.add_argument("--public", default=DEFAULT_PUBLIC)
    args = ap.parse_args(argv)

    public = Path(args.public).resolve()
    if not public.is_dir():
        print(f"ERROR: {public} not found — run `hugo --minify` first.",
              file=sys.stderr)
        return 2

    urls = fetch_sitemap_urls(args.sitemap_url)
    print(f"Sitemap URLs: {len(urls)}", file=sys.stderr)

    direct = alias = missing = 0
    misses: list[tuple[str, str]] = []
    for u in urls:
        rel = url_to_relpath(u)
        ok, how = resolves(rel, public)
        if how == "direct":
            direct += 1
        elif how == "alias":
            alias += 1
        else:
            missing += 1
            misses.append((u, rel))

    print(f"\nResolved: direct={direct}  alias={alias}  missing={missing}  total={len(urls)}")
    if misses:
        print("\nMissing URLs (first 25):")
        for u, rel in misses[:25]:
            print(f"  {u}  ->  {rel}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
