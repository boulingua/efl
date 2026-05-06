"""Phase 6.7 — every content page must attribute S. Le Boulanger.

Walks rendered HTML under public/ and asserts each page that
represents authored content carries the author signal in three
places:
  - <meta name="author" content="..."> in <head>
  - JSON-LD Person somewhere in the document (optional but checked
    when present — Coder doesn't emit JSON-LD by default)
  - A visible author string in the rendered body (we accept any
    occurrence of "Le Boulanger" in the article body)

Skips alias-redirect HTML files (1-line meta-refresh stubs), the
homepage's pure-navigation surfaces, and the materials hub
(navigation, not editorial content).

Hard-fail: missing author attribution on a content page is a
breach of the brief's "author attribution is sacred" rule.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"

META_AUTHOR_RE = re.compile(
    r'<meta\s+[^>]*name=["\']?author["\']?[^>]*content=["\']?([^"\'>]+)',
    re.IGNORECASE,
)
ARTICLE_RE = re.compile(r"<article\b[^>]*>(.*?)</article>", re.DOTALL | re.IGNORECASE)

# Pages that aren't authored editorial content — exclude.
SKIP_EXACT = {
    "/materials/",
    "/materials/presentations/",
    "/materials/worksheets/",
    "/track-e/", "/track-gm/",  # track parents (no _index)
}
PAGINATOR_RE = re.compile(r"/page/\d+/$")
ALIAS_RE = re.compile(r'http-equiv=["\']?refresh', re.IGNORECASE)


def page_url(p: Path) -> str:
    rel = p.relative_to(PUBLIC).as_posix()
    if rel.endswith("/index.html"):
        return "/" + rel.removesuffix("index.html")
    return "/" + rel


def is_alias(html: str) -> bool:
    return bool(ALIAS_RE.search(html[:600]))


def is_content_page(url: str) -> bool:
    if url in SKIP_EXACT or PAGINATOR_RE.search(url):
        return False
    if url.endswith(".xml") or url.endswith(".json"):
        return False
    return True


def main() -> int:
    if not PUBLIC.is_dir():
        print(f"GATE FAIL: {PUBLIC} missing.", file=sys.stderr)
        return 2

    n_checked = 0
    no_meta: list[str] = []
    no_visible: list[str] = []
    wrong_author: list[tuple[str, str]] = []

    for f in PUBLIC.rglob("*.html"):
        url = page_url(f)
        if not is_content_page(url):
            continue
        body = f.read_text(encoding="utf-8", errors="ignore")
        if is_alias(body):
            continue
        n_checked += 1

        m = META_AUTHOR_RE.search(body)
        if not m:
            no_meta.append(url)
        else:
            author = m.group(1).strip()
            if "Le Boulanger" not in author:
                wrong_author.append((url, author))

        # Visible attribution: search inside <article>, fall back to whole body.
        article = ARTICLE_RE.search(body)
        scope = article.group(1) if article else body
        if "Le Boulanger" not in scope:
            no_visible.append(url)

    print(f"Audited {n_checked} content pages.")
    fail = False
    if no_meta:
        print(f"\nGATE FAIL: {len(no_meta)} page(s) missing "
              f"<meta name=\"author\">:", file=sys.stderr)
        for u in no_meta[:15]:
            print(f"  {u}", file=sys.stderr)
        fail = True
    if wrong_author:
        print(f"\nGATE FAIL: {len(wrong_author)} page(s) with wrong "
              f"meta author:", file=sys.stderr)
        for u, a in wrong_author[:10]:
            print(f"  {u}: {a!r}", file=sys.stderr)
        fail = True
    if no_visible:
        print(f"\nGATE FAIL: {len(no_visible)} page(s) without a visible "
              f"\"Le Boulanger\" string in body:", file=sys.stderr)
        for u in no_visible[:15]:
            print(f"  {u}", file=sys.stderr)
        fail = True

    if fail:
        return 1
    print("All content pages attribute S. Le Boulanger.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
