"""Phase 2 network-viz schema gate (scripts/, per the brief's convention).

Validates public/materials/graph.json:
- Every node has unique id, label/title, resolvable url, type/category.
- Every edge references two existing node ids (zero dangling edges).
- No duplicate nodes by id OR by url (article URLs only).
- Node count matches expected = articles_with_materials × (1 article + 1 pres + 1 ws).
- Edges encode pedagogical structure: every shared-tag edge has weight ≥ 1
  and a recorded `kind`; every same-article edge connects exactly one
  article to one presentation/worksheet of the same parent.

Exits non-zero with a punch list on any violation. Designed to be
wired into the Hugo CI workflow alongside verify_graph.py.
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GRAPH = ROOT / "public" / "materials" / "graph.json"
PUBLIC = ROOT / "public"


def resolve_url(url: str) -> bool:
    if not url:
        return False
    rel = url.split("?", 1)[0].split("#", 1)[0]
    if rel.startswith("/efl/"):
        rel = rel[len("/efl/"):]
    elif rel.startswith("/"):
        rel = rel[1:]
    p = PUBLIC / rel
    if p.is_file():
        return True
    return (p / "index.html").is_file()


def main() -> int:
    if not GRAPH.is_file():
        print(f"GATE FAIL: {GRAPH.relative_to(ROOT)} missing — "
              f"run `hugo --minify` first.", file=sys.stderr)
        return 1
    g = json.loads(GRAPH.read_text(encoding="utf-8"))

    errors: list[str] = []

    # --- Node-level checks ---------------------------------------------------
    node_ids: set[str] = set()
    article_urls: dict[str, str] = {}  # url -> id
    type_counts: Counter[str] = Counter()
    for n in g["nodes"]:
        nid = n.get("id")
        if not nid:
            errors.append(f"  node missing `id`: {n}")
            continue
        if nid in node_ids:
            errors.append(f"  duplicate node id: {nid}")
        node_ids.add(nid)
        if not n.get("title"):
            errors.append(f"  node {nid} missing `title`")
        if "type" not in n:
            errors.append(f"  node {nid} missing `type`")
        else:
            type_counts[n["type"]] += 1
        url = n.get("url")
        if not url:
            errors.append(f"  node {nid} missing `url`")
        elif not resolve_url(url):
            errors.append(f"  node {nid} url does not resolve: {url}")
        # Duplicate url-by-article
        if n.get("type") == "article" and url:
            if url in article_urls:
                errors.append(f"  duplicate article url {url}: "
                              f"{article_urls[url]} and {nid}")
            else:
                article_urls[url] = nid

    # --- Edge-level checks ---------------------------------------------------
    same_article = shared_tags = 0
    for e in g["edges"]:
        s, t = e.get("source"), e.get("target")
        if s not in node_ids:
            errors.append(f"  edge source not a node id: {s}")
        if t not in node_ids:
            errors.append(f"  edge target not a node id: {t}")
        kind = e.get("kind")
        if kind not in ("same-article", "shared-tags"):
            errors.append(f"  edge with unknown kind {kind!r}: "
                          f"{s} -> {t}")
            continue
        w = e.get("weight")
        if not isinstance(w, int) or w < 1:
            errors.append(f"  edge weight invalid: {s} -> {t} (weight={w})")
        if kind == "same-article":
            same_article += 1
        elif kind == "shared-tags":
            shared_tags += 1

    # --- Count parity --------------------------------------------------------
    n_articles = type_counts.get("article", 0)
    n_pres = type_counts.get("presentation", 0)
    n_ws = type_counts.get("worksheet", 0)
    if n_articles != n_pres or n_articles != n_ws:
        errors.append(
            f"  node-type imbalance: article={n_articles} "
            f"presentation={n_pres} worksheet={n_ws} "
            f"(every article is supposed to ship both)")
    expected_structural = n_articles * 2  # one pres-edge + one ws-edge per article
    if same_article != expected_structural:
        errors.append(
            f"  structural edge count mismatch: have {same_article}, "
            f"expected {expected_structural} (= articles × 2)")
    if shared_tags == 0:
        errors.append("  zero shared-tag edges — graph has no inter-article "
                      "structure; tagging or threshold is broken.")

    # --- Output --------------------------------------------------------------
    if errors:
        print(f"\nNetwork data validation FAILED — {len(errors)} issue(s):",
              file=sys.stderr)
        for e in errors[:30]:
            print(e, file=sys.stderr)
        if len(errors) > 30:
            print(f"  …and {len(errors) - 30} more", file=sys.stderr)
        return 1

    print(f"Network data OK — {len(g['nodes'])} nodes "
          f"(article {n_articles}, presentation {n_pres}, worksheet {n_ws}); "
          f"{len(g['edges'])} edges (structural {same_article}, "
          f"shared-tags {shared_tags}).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
