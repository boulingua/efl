"""Phase 1 CI gates for the Materials Discovery Network.

Reads `public/materials/graph.json` (built by Hugo from
`layouts/materials/list.network.json`) and `data/topics.yml`, then
enforces:

  1. Every material-bearing article has at least one tag.
     -> graph.json should not contain any node of type=article with empty tags.
  2. Every article's `topic` is present in data/topics.yml.
  3. graph.json contains at least one shared-tag edge (the network is
     not a star around same-article structural edges).
  4. Every topic in data/topics.yml has at least one article.
  5. (deferred to Phase 5) Pagefind index is non-empty.

Exits non-zero with a loud, specific error on any violation.
Single-purpose: run after `hugo --minify`, before deploy.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
GRAPH = ROOT / "public" / "materials" / "graph.json"
TOPICS = ROOT / "data" / "topics.yml"


def main() -> int:
    if not GRAPH.is_file():
        print(f"GATE FAIL: {GRAPH.relative_to(ROOT)} missing — "
              f"run `hugo --minify` first.", file=sys.stderr)
        return 1
    if not TOPICS.is_file():
        print(f"GATE FAIL: {TOPICS.relative_to(ROOT)} missing.",
              file=sys.stderr)
        return 1

    g = json.loads(GRAPH.read_text(encoding="utf-8"))
    topics = yaml.safe_load(TOPICS.read_text(encoding="utf-8"))
    topic_ids = {t["id"] for t in topics}

    errors: list[str] = []

    # Gate 1: zero-tag articles.
    untagged = [n for n in g["nodes"]
                if n["type"] == "article" and not n.get("tags")]
    if untagged:
        for n in untagged[:5]:
            errors.append(
                f"  zero-tag article: {n['url']} ({n['id']})")
        if len(untagged) > 5:
            errors.append(f"  …and {len(untagged) - 5} more zero-tag articles")
        errors.append(
            f"GATE 1 FAIL: {len(untagged)} article(s) have empty tags. "
            f"Add `tags:` (or `skills_focus:` + `bildungsplan:`) to each.")

    # Gate 2: unknown topic.
    unknown_topics: dict[str, list[str]] = {}
    for n in g["nodes"]:
        if n["type"] != "article":
            continue
        t = n.get("topic")
        if t and t not in topic_ids:
            unknown_topics.setdefault(t, []).append(n["url"])
    if unknown_topics:
        for tid, urls in unknown_topics.items():
            errors.append(
                f"  topic={tid!r} (used by {len(urls)} articles, e.g. {urls[0]}) "
                f"is not in data/topics.yml")
        errors.append(
            f"GATE 2 FAIL: {len(unknown_topics)} topic id(s) referenced but "
            f"not declared. Add to data/topics.yml or fix frontmatter.")

    # Gate 3: zero shared-tag edges.
    shared = sum(1 for e in g["edges"] if e.get("kind") == "shared-tags")
    if shared == 0:
        errors.append(
            "GATE 3 FAIL: graph.json has zero shared-tag edges. The "
            "network has no inter-article structure — tagging is too "
            "sparse or the threshold in list.network.json is too high.")

    # Gate 4: orphan topic in data/topics.yml.
    article_topics = {n.get("topic") for n in g["nodes"]
                      if n["type"] == "article"}
    orphans = sorted(t for t in topic_ids if t not in article_topics)
    if orphans:
        for t in orphans:
            errors.append(
                f"  topic={t!r} declared in data/topics.yml but used by "
                f"zero articles")
        errors.append(
            f"GATE 4 FAIL: {len(orphans)} orphan topic(s). Either delete "
            f"them from data/topics.yml or assign articles to them.")

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1

    n_articles = sum(1 for n in g["nodes"] if n["type"] == "article")
    n_st = shared
    n_sa = sum(1 for e in g["edges"] if e.get("kind") == "same-article")
    density = n_st / max(1, n_articles * (n_articles - 1) / 2)
    print(f"GATES OK — {len(g['nodes'])} nodes, {len(g['edges'])} edges "
          f"(structural {n_sa}, shared-tags {n_st}); article-graph "
          f"density {density:.3f}; topics {len(topic_ids)} all populated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
