"""Phase 5 — Cross-cutting polish.

Generates from front-matter / filesystem state:
1. Per-course schedule.qmd — actual 12-row table with deep links.
2. Per-course index.qmd — recurring-cast intro + actual 12-Unit card grid.
3. Top-level schedule.qmd — sortable 15x12 table of all 180 Units.
4. _resources/coverage_matrix.yml — every Bildungsplan code → Units that cite it.
5. appendices/skills_decision_tree.qmd — leaves linked to representative Units.

Idempotent: safe to re-run.
"""
from __future__ import annotations
import collections
import pathlib
import re

import yaml

REPO = pathlib.Path(__file__).resolve().parent.parent

CAST = {
    5:  "Mia, Theo, Frida the fox, and Mr. Flint",
    6:  "Sam, Lina, Mr. Flint, and Captain Cody",
    7:  "Aisha, Ben, and Ms. Reyes",
    8:  "Jonas, Hawa, and a global pen-pal class",
    9:  "Eli, Naima, and Mr. Yilmaz",
    10: {"gm": "Sam (returning), Maja, and a young-adult ensemble",
         "e":  "Maja and a young-adult ensemble"},
    11: "narrators and author voices",
    12: "texts as characters: speakers, writers, public voices",
    13: "public voices and contemporary writers",
}

THEME_ARC = {
    5: "Family, school, friends — concrete and playful",
    6: "Adventures and routines — episodic with light cultural anchors",
    7: "Identity and the wider world",
    8: "Belonging and fairness",
    9: "Choices and society",
    10: {"gm": "Transition, work, media",
         "e":  "Transition and the world (Oberstufe-ready)"},
    11: "Cultural entry, literary voice (Oberstufe)",
    12: "Discourse and analysis (Oberstufe)",
    13: "Exam-grade and issue-framed (Abitur year)",
}

EXAM_TYPE = {
    5: "class test (Klassenarbeit)",
    6: "class test (Klassenarbeit)",
    7: "class test (Klassenarbeit)",
    8: "class test (Klassenarbeit)",
    9: "class test (Klassenarbeit)",
    10: "class test (Klassenarbeit)",
    11: "Klausur (assessment)",
    12: "Klausur (assessment)",
    13: "Abitur-grade Klausur (school-leaving examination)",
}

COURSES = (
    [("gm", k) for k in range(5, 11)] +
    [("e",  k) for k in range(5, 14)]
)


def parse_front_matter(qmd_path: pathlib.Path) -> dict:
    text = qmd_path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end < 0:
        return {}
    fm = text[3:end + 1]
    try:
        return yaml.safe_load(fm) or {}
    except Exception:
        return {}


def collect_units(track: str, klasse: int) -> list[dict]:
    course_dir = REPO / f"track_{track}_kl{klasse:02d}" / "units"
    out = []
    if not course_dir.exists():
        return out
    for p in sorted(course_dir.glob("unit*.qmd")):
        if p.name.startswith("_"):
            continue
        if p.name.endswith("_exam.qmd"):
            continue
        fm = parse_front_matter(p)
        if not fm:
            continue
        out.append({
            "unit_nr": fm.get("unit_nr"),
            "slug": fm.get("slug"),
            "title": fm.get("title"),
            "skills_focus": fm.get("skills_focus", []),
            "bildungsplan": fm.get("bildungsplan", []),
            "niveau": fm.get("niveau"),
            "path": p.relative_to(REPO).as_posix(),
        })
    return sorted(out, key=lambda u: u["unit_nr"] or 0)


def cast_for(track: str, klasse: int) -> str:
    cast = CAST.get(klasse)
    if isinstance(cast, dict):
        return cast.get(track, "")
    return cast or ""


def theme_for(track: str, klasse: int) -> str:
    arc = THEME_ARC.get(klasse)
    if isinstance(arc, dict):
        return arc.get(track, "")
    return arc or ""


def label_for(track: str) -> str:
    return "G+M" if track == "gm" else "E"


def write_course_schedule(track: str, klasse: int, units: list[dict]) -> None:
    label = label_for(track)
    exam = EXAM_TYPE.get(klasse, "")
    rows = []
    for u in units:
        n = u["unit_nr"]
        title = (u["title"] or "").replace(f"Unit {n} — ", "")
        skills = ", ".join(u.get("skills_focus") or [])
        rows.append(
            f"| {n} | [{title}](units/unit{n:02d}_{u['slug']}.qmd) "
            f"| {skills} | {exam} |"
        )

    body = f"""---
title: "Schedule — Klasse {klasse} · Track {label}"
pagetitle: "Klasse {klasse} schedule · Track {label} — EFL"
author: "S. Le Boulanger"
---

The twelve Units of Klasse {klasse} ({label}) across the school
year. Each Unit covers roughly three teaching weeks.

| Unit | Title | Skills focus | Exam type |
|------|-------|--------------|-----------|
""" + "\n".join(rows) + f"""

[← Back to Klasse {klasse} overview](index.qmd)
"""
    (REPO / f"track_{track}_kl{klasse:02d}" / "schedule.qmd").write_text(
        body, encoding="utf-8")


def write_course_index(track: str, klasse: int, units: list[dict]) -> None:
    label = label_for(track)
    cast = cast_for(track, klasse)
    theme = theme_for(track, klasse)
    exam = EXAM_TYPE.get(klasse, "")

    cards = []
    for u in units:
        n = u["unit_nr"]
        title = (u["title"] or "").replace(f"Unit {n} — ", "")
        niveau = u.get("niveau") or label
        skills = ", ".join((u.get("skills_focus") or [])[:3])
        href = f"units/unit{n:02d}_{u['slug']}.qmd"
        cards.append(
            "::: {.card}\n"
            f"[Unit {n} · Niveau {niveau}]{{.kicker}}\n\n"
            f"### [{title}]({href})\n"
            f"{skills}\n"
            ":::"
        )

    card_grid = "::: {.card-grid}\n" + "\n".join(cards) + "\n:::"

    body = f"""---
title: "Klasse {klasse} English — {theme}"
pagetitle: "Klasse {klasse} · Track {label} — EFL"
author: "S. Le Boulanger"
---

::: {{.hero}}
::: {{.kicker}}
TRACK {label} · KLASSE {klasse}
:::
# Klasse {klasse} English — {theme}

::: {{.lead}}
Twelve Units across the school year. Each Unit ships an HTML
article, a Reveal.js slide deck, a worksheet PDF (placeholder),
and a worked exam example as {exam}. Authored by S. Le Boulanger.
:::
:::

## The recurring cast

This year's stories follow **{cast}**. Characters (or, in the
Oberstufe, *texts as characters*) reappear across Units so
learners build a continuous sense of place and voice.

## The twelve Units

{card_grid}

## What you will be able to do by the end of this year

::: {{.callout-tip icon=false title="curriculum framework (Bildungsplan)-aligned Kompetenzerwartungen"}}
Filled in from `_resources/bildungsplan_bw_{track}_kl{klasse:02d}.yml`.
The chapter codes and German labels are pulled live from
[bildungsplaene-bw.de](https://www.bildungsplaene-bw.de/).
:::

## Use this course in class

- The [schedule](schedule.qmd) lists all twelve Units.
- Each Unit page links four downloads: article (HTML), slide deck
  (HTML), worksheet (PDF placeholder), exam example (PDF).
- Speaker notes on every slide cover timing, transitions, and
  Niveau-aware differentiation prompts for mixed groups.
"""
    (REPO / f"track_{track}_kl{klasse:02d}" / "index.qmd").write_text(
        body, encoding="utf-8")


def write_master_schedule(all_units: list[tuple]) -> None:
    rows = []
    for track, klasse, u in all_units:
        n = u["unit_nr"]
        title = (u["title"] or "").replace(f"Unit {n} — ", "")
        niveau = u.get("niveau") or label_for(track)
        skills = ", ".join((u.get("skills_focus") or [])[:3])
        path = f"track_{track}_kl{klasse:02d}/units/unit{n:02d}_{u['slug']}.qmd"
        rows.append(
            f"| {label_for(track)} | {klasse} | {n} | "
            f"[{title}]({path}) | {niveau} | {skills} | "
            f"{EXAM_TYPE.get(klasse, '')} |"
        )

    body = """---
title: "Schedule"
pagetitle: "Schedule — EFL"
author: "S. Le Boulanger"
toc: true
toc-depth: 2
---

The full linked index across both tracks — every year group
(Klassenstufe), every Unit, with skills focus, exam type, and
deep-links. Generated from each Unit's front matter.

## Track G+M — Klasse 5 to 10 (72 Units)

| Track | Kl. | Unit | Title | Niveau | Skills focus | Exam type |
|-------|-----|------|-------|--------|--------------|-----------|
""" + "\n".join(r for r in rows if " G+M |" in r) + """

## Track E — Klasse 5 to 13 (108 Units)

| Track | Kl. | Unit | Title | Niveau | Skills focus | Exam type |
|-------|-----|------|-------|--------|--------------|-----------|
""" + "\n".join(r for r in rows if " E |" in r) + """

## Per-course pages

### Track G+M
""" + "\n".join(
        f"- [Klasse {k}](track_gm_kl{k:02d}/index.qmd) · "
        f"[schedule](track_gm_kl{k:02d}/schedule.qmd)"
        for k in range(5, 11)
    ) + """

### Track E
""" + "\n".join(
        f"- [Klasse {k}](track_e_kl{k:02d}/index.qmd) · "
        f"[schedule](track_e_kl{k:02d}/schedule.qmd)"
        for k in range(5, 14)
    ) + "\n"

    (REPO / "schedule.qmd").write_text(body, encoding="utf-8")


def write_coverage_matrix(all_units: list[tuple]) -> None:
    code_to_units = collections.defaultdict(list)
    for track, klasse, u in all_units:
        n = u["unit_nr"]
        for entry in (u.get("bildungsplan") or []):
            # Strip leading code prefix
            m = re.match(r"\s*([\d.]+)", entry)
            code = m.group(1) if m else entry.split()[0]
            code_to_units[code].append({
                "track": track, "klasse": klasse, "unit_nr": n,
                "slug": u["slug"], "title": u["title"],
            })

    out = {
        "site": "efl",
        "generated_from": "Unit front-matter scan",
        "code_count": len(code_to_units),
        "codes": dict(sorted(code_to_units.items())),
    }
    (REPO / "_resources" / "coverage_matrix.yml").write_text(
        yaml.safe_dump(out, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )


def write_skills_tree(all_units: list[tuple]) -> None:
    by_skill = collections.defaultdict(list)
    for track, klasse, u in all_units:
        for s in u.get("skills_focus") or []:
            by_skill[s].append((track, klasse, u))

    def first_3(skill: str) -> str:
        items = by_skill.get(skill, [])[:3]
        return " · ".join(
            f"[Kl.{k}/{label_for(t)}]"
            f"(/track_{t}_kl{k:02d}/units/unit{u['unit_nr']:02d}_{u['slug']}.qmd)"
            for t, k, u in items
        ) or "_pending_"

    body = f"""---
title: "Skills decision tree"
author: "S. Le Boulanger"
---

Pick a skill area, then jump to representative Units across the
fifteen courses. Generated from front-matter scans (3 representative
Units per skill).

```{{mermaid}}
flowchart LR
  ROOT[Which skill?] --> L[Listening]
  ROOT --> R[Reading]
  ROOT --> S[Speaking]
  ROOT --> W[Writing]
  ROOT --> M[mediation Sprachmittlung]
  ROOT --> LA[Language awareness]
  ROOT --> IC[Intercultural]
```

## Listening — representative Units

{first_3("listening")}

## Reading — representative Units

{first_3("reading")}

## Speaking — representative Units

{first_3("speaking")}

## Writing — representative Units

{first_3("writing")}

## Mediation (Sprachmittlung) — representative Units

{first_3("mediation")}

## Language awareness — representative Units

{first_3("language_awareness")}

## Intercultural — representative Units

{first_3("intercultural")}
"""
    (REPO / "appendices" / "skills_decision_tree.qmd").write_text(
        body, encoding="utf-8")


def main() -> None:
    all_units = []
    for track, klasse in COURSES:
        units = collect_units(track, klasse)
        if not units:
            print(f"WARN: no units in track_{track}_kl{klasse:02d}")
            continue
        write_course_schedule(track, klasse, units)
        write_course_index(track, klasse, units)
        for u in units:
            all_units.append((track, klasse, u))
    write_master_schedule(all_units)
    write_coverage_matrix(all_units)
    write_skills_tree(all_units)
    print(f"Polished {len(all_units)} units across {len(COURSES)} courses.")


if __name__ == "__main__":
    main()
