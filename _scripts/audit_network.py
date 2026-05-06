"""Phase 0 audit for the Materials Discovery Network.

Read-only. Walks every material-bearing article in content/, extracts the
metadata that will feed graph.json, audits tags + topics, prints a
markdown-friendly report to stdout. Does not write anywhere except
producing structured output the human (or MATERIALS_NETWORK_PLAN.md)
can paste into.
"""
from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"

FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n?", re.DOTALL)


def split_fm(text: str) -> tuple[str, str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return "", text
    return m.group(1), text[m.end():]


def yaml_scalar(fm: str, key: str) -> str | None:
    m = re.search(rf"^{re.escape(key)}:\s*(.*)$", fm, re.MULTILINE)
    if not m:
        return None
    val = m.group(1).strip().strip('"').strip("'")
    return val or None


def yaml_list(fm: str, key: str) -> list[str]:
    """Parse a top-level YAML list of scalars (one item per indented line)."""
    m = re.search(rf"^{re.escape(key)}:\s*$", fm, re.MULTILINE)
    if not m:
        return []
    end = fm.find("\n", m.end())
    items: list[str] = []
    for line in fm[end + 1:].splitlines():
        if not line.startswith(("  ", "\t")):
            break
        ml = re.match(r"\s+-\s*(.*)", line)
        if ml:
            v = ml.group(1).strip().strip('"').strip("'")
            if v:
                items.append(v)
    return items


def has_block(fm: str, key: str) -> bool:
    return bool(re.search(rf"^{re.escape(key)}:\s*$", fm, re.MULTILINE))


def derive_url(md: Path) -> str:
    rel = md.relative_to(CONTENT)
    parts = list(rel.parts)
    if parts[-1] in ("index.md", "_index.md"):
        parts = parts[:-1]
    return "/" + "/".join(parts) + "/"


def derive_course(md: Path) -> str | None:
    """Return the course id (track-X/kl<NN>) for a unit page, or None."""
    rel = md.relative_to(CONTENT)
    parts = list(rel.parts)
    if len(parts) >= 4 and parts[0].startswith("track-") and parts[1].startswith("kl"):
        return f"{parts[0]}/{parts[1]}"
    return None


def main() -> None:
    articles: list[dict] = []
    presentation_count = worksheet_count = 0
    tag_counter: Counter[str] = Counter()
    topic_counter: Counter[str] = Counter()
    course_counter: Counter[str] = Counter()
    no_tags: list[str] = []
    no_topic: list[str] = []
    no_date: list[str] = []
    bildungsplan_only: list[str] = []  # tags absent, but bildungsplan present
    no_skills: list[str] = []

    for md in sorted(CONTENT.rglob("*.md")):
        if md.parent.name.endswith("-exam"):
            continue
        text = md.read_text(encoding="utf-8")
        fm, _ = split_fm(text)
        if not has_block(fm, "presentation") and not has_block(fm, "worksheet"):
            continue

        title = yaml_scalar(fm, "title") or md.parent.name
        slug = yaml_scalar(fm, "unit_slug") or md.parent.name
        url = derive_url(md)
        course = derive_course(md)
        topic = yaml_scalar(fm, "topic")
        date = yaml_scalar(fm, "date")
        skills = yaml_list(fm, "skills_focus")
        bildungsplan = yaml_list(fm, "bildungsplan")
        # 'tags' field — the prompt's network expects this name.
        tags = yaml_list(fm, "tags")

        # Skills focus is the closest semantic equivalent to "tags" in the
        # current frontmatter. Surface it as a candidate tag set.
        candidate_tags = list(tags or skills)
        for t in candidate_tags:
            tag_counter[t] += 1
        if topic:
            topic_counter[topic] += 1
        if course:
            course_counter[course] += 1
        presentation_count += 1 if has_block(fm, "presentation") else 0
        worksheet_count += 1 if has_block(fm, "worksheet") else 0

        if not candidate_tags:
            no_tags.append(url)
        if not topic:
            no_topic.append(url)
        if not date:
            no_date.append(url)
        if not skills:
            no_skills.append(url)
        if bildungsplan and not tags:
            bildungsplan_only.append(url)

        articles.append({
            "url": url,
            "title": title,
            "slug": slug,
            "course": course,
            "topic": topic,
            "tags": candidate_tags,
            "skills_focus": skills,
            "bildungsplan": bildungsplan,
            "date": date,
            "has_presentation": has_block(fm, "presentation"),
            "has_worksheet": has_block(fm, "worksheet"),
        })

    print("# audit summary")
    print()
    print(f"- material-bearing articles: **{len(articles)}**")
    print(f"- presentations: **{presentation_count}**")
    print(f"- worksheets: **{worksheet_count}**")
    print(f"- nodes if every article + pres + ws becomes one node: "
          f"**{len(articles) + presentation_count + worksheet_count}**")
    print()
    print(f"## tag/skill taxonomy")
    print(f"- distinct skills_focus values: {len(tag_counter)}")
    print(f"- skills_focus histogram:")
    for k, v in tag_counter.most_common():
        print(f"  - `{k}`: {v}")
    print()
    print(f"## topics")
    print(f"- pages with explicit `topic:` frontmatter: {len(topic_counter)}")
    if topic_counter:
        for k, v in topic_counter.most_common():
            print(f"  - `{k}`: {v}")
    else:
        print("  - **none.** No article carries a `topic:` key.")
    print()
    print(f"## courses (derived from path)")
    for k, v in sorted(course_counter.items()):
        print(f"  - `{k}`: {v}")
    print()
    print("## gaps")
    print(f"- articles without `tags:` AND without `skills_focus:` "
          f"(would be excluded from edge formation): **{len(no_tags)}**")
    print(f"- articles without `topic:`: **{len(no_topic)}**")
    print(f"- articles without `date:`: **{len(no_date)}**")
    print(f"- articles without `skills_focus:` (Hugo-side fallback "
          f"if `tags:` is missing): **{len(no_skills)}**")
    print(f"- articles using `bildungsplan` but no `tags:` "
          f"(curriculum codes available as fallback edges): "
          f"**{len(bildungsplan_only)}**")
    print()
    print("## first 10 articles (sample)")
    for a in articles[:10]:
        print(f"  - {a['url']} — `{a['slug']}` · "
              f"course=`{a['course']}` · topic=`{a['topic']}` · "
              f"tags={a['tags'][:3]}{'…' if len(a['tags'])>3 else ''}")


if __name__ == "__main__":
    main()
