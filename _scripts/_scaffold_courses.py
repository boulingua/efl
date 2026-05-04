"""One-shot scaffolder for the 15 course landing pages, schedules,
and units/_metadata.yml files. Run once at Phase 1; do not re-run
after Phase 3 starts (it would overwrite per-course customisations).
"""
import pathlib

REPO = pathlib.Path(__file__).resolve().parent.parent

COURSES = [
    # (track, kk, niveau_label, klasse, cast, title_tagline, theme_blurb)
    ("gm", "05", "G+M", 5,
     "Mia, Theo, Frida the fox, and Mr. Flint",
     "Family, school, friends",
     "concrete and playful: home, school day, weather, food, animals, hobbies"),
    ("gm", "06", "G+M", 6,
     "Sam, Lina, Mr. Flint, and Captain Cody",
     "Adventures and routines",
     "episodic adventures, daily routines, seasons, places in town"),
    ("gm", "07", "G+M", 7,
     "Aisha, Ben, and Ms. Reyes",
     "Identity and the wider world",
     "teen life, peer groups, English-speaking countries, simple media literacy"),
    ("gm", "08", "G+M", 8,
     "Jonas, Hawa, and a global pen-pal class",
     "Belonging and fairness",
     "identity, fairness, school in other countries, opinion writing"),
    ("gm", "09", "G+M", 9,
     "Eli, Naima, and Mr. Yilmaz",
     "Choices and society",
     "career, money, environment, social issues at the local level"),
    ("gm", "10", "G+M", 10,
     "Sam (returning), Maja, and a young-adult ensemble",
     "Transition, work, media",
     "transition to vocational life, work, media literacy, civic English"),
    ("e", "05", "E", 5,
     "Mia, Theo, Frida the fox, and Mr. Flint",
     "Family, school, friends",
     "home, school, weather, food, animals, hobbies, with richer input"),
    ("e", "06", "E", 6,
     "Sam, Lina, Mr. Flint, and Captain Cody",
     "Adventures and routines",
     "episodic adventures, daily routines, seasons, entry-level cultural anchors"),
    ("e", "07", "E", 7,
     "Aisha, Ben, and Ms. Reyes",
     "Identity and the wider world",
     "teen life, the United Kingdom and the United States, simple media literacy"),
    ("e", "08", "E", 8,
     "Jonas, Hawa, and a global pen-pal class",
     "Belonging and fairness",
     "identity, fairness, school across the English-speaking world, intro to mediation"),
    ("e", "09", "E", 9,
     "Eli, Naima, and Mr. Yilmaz",
     "Choices and society",
     "career, environment, social justice, more demanding mediation tasks"),
    ("e", "10", "E", 10,
     "Maja and an ensemble of young adults",
     "Transition and the world",
     "transition, media, science and ethics introduction, intercultural breadth"),
    ("e", "11", "E", 11,
     "narrators and author voices",
     "Cultural entry, literary voice",
     "literature entry: short fiction, poetry, English-speaking cultures; Units tagged E-BF or E-LF"),
    ("e", "12", "E", 12,
     "texts as characters: speakers, writers, public voices",
     "Discourse and analysis",
     "non-fiction discourse, dystopias, science and ethics, advanced mediation"),
    ("e", "13", "E", 13,
     "public voices and contemporary writers",
     "Exam-grade and issue-framed",
     "globalisation, political discourse, exam-grade composition, full Abitur preparation"),
]

INDEX_TPL = """---
title: "Klasse {klasse} English — {tagline}"
pagetitle: "Klasse {klasse} · Track {label} — EFL"
---

::: {{.hero}}
::: {{.kicker}}
TRACK {label} · KLASSE {klasse}
:::
# Klasse {klasse} English — {tagline}

::: {{.lead}}
{theme_blurb}. Twelve Units across the school year, each with an
HTML article, a Reveal.js slide deck, a placeholder worksheet PDF,
and a worked exam example {exam_kind} at Niveau {label_short}.
:::
:::

## The recurring cast

This year's stories follow **{cast}**. Characters reappear across
Units so learners build a continuous sense of place and voice.

## The twelve Units

::: {{.callout-note}}
**Pending:** the twelve Units appear here as a card grid once the
curriculum outline (Phase 2) is approved and the Units are written
(Phases 3–4). Until then, see the [schedule for this course](schedule.qmd)
for the planned Unit slots.
:::

## What you will be able to do by the end of this year

::: {{.callout-tip icon=false title="Bildungsplan-aligned Kompetenzerwartungen"}}
Will be filled in from `_resources/bildungsplan_bw_{track}_kl{kk}.yml`
once the Bildungsplan resource is fetched (Phase 0).
:::

## Use this course in class

- The [schedule](schedule.qmd) lists all twelve Units with their
  placement in the school year.
- Each Unit page links four downloads (article, slides, worksheet,
  exam) so a teacher can pull what they need into class within
  one click.
- Speaker notes on every slide cover timing, transitions, and
  Niveau-aware differentiation prompts for mixed groups.
"""

SCHED_TPL = """---
title: "Schedule — Klasse {klasse} · Track {label}"
pagetitle: "Klasse {klasse} schedule · Track {label} — EFL"
---

The twelve Units of Klasse {klasse} ({label}) across the school
year. Each Unit covers roughly three teaching weeks; total ≈ 36
weeks (Schulwoche 1–40 minus exam weeks and holidays).

::: {{.callout-note}}
**Pending:** Unit titles, slugs, and Bildungsplan anchors will be
filled in here once `_resources/curriculum_outline.yml` is approved
in Phase 2. Until then, the slots below are reserved.
:::

| Unit | Title | Skills focus | Exam type |
|------|-------|--------------|-----------|
| 1  | _to be confirmed_ | _tbd_ | {exam_kind_label} |
| 2  | _to be confirmed_ | _tbd_ | {exam_kind_label} |
| 3  | _to be confirmed_ | _tbd_ | {exam_kind_label} |
| 4  | _to be confirmed_ | _tbd_ | {exam_kind_label} |
| 5  | _to be confirmed_ | _tbd_ | {exam_kind_label} |
| 6  | _to be confirmed_ | _tbd_ | {exam_kind_label} |
| 7  | _to be confirmed_ | _tbd_ | {exam_kind_label} |
| 8  | _to be confirmed_ | _tbd_ | {exam_kind_label} |
| 9  | _to be confirmed_ | _tbd_ | {exam_kind_label} |
| 10 | _to be confirmed_ | _tbd_ | {exam_kind_label} |
| 11 | _to be confirmed_ | _tbd_ | {exam_kind_label} |
| 12 | _to be confirmed_ | _tbd_ | {exam_kind_label} |

[← Back to Klasse {klasse} overview](index.qmd)
"""

META_TPL = '''author: "S. Le Boulanger"
'''


def main() -> None:
    for track, kk, label, klasse, cast, tagline, theme_blurb in COURSES:
        if klasse <= 10:
            exam_kind = "(a Klassenarbeit)"
            exam_kind_label = "Klassenarbeit"
        else:
            exam_kind = "(an Abitur-Prüfungsaufgabe)"
            exam_kind_label = "Abitur-Aufgabe"

        # In Track G+M, Niveau "G+M" means Units carry G or M tags
        # individually; the course banner uses "G+M" as a label.
        label_short = label

        course_dir = REPO / f"track_{track}_kl{kk}"
        units_dir = course_dir / "units"
        units_dir.mkdir(parents=True, exist_ok=True)

        (course_dir / "index.qmd").write_text(
            INDEX_TPL.format(
                klasse=klasse, label=label, label_short=label_short,
                tagline=tagline, cast=cast, theme_blurb=theme_blurb,
                exam_kind=exam_kind, track=track, kk=kk,
            ),
            encoding="utf-8",
        )

        (course_dir / "schedule.qmd").write_text(
            SCHED_TPL.format(
                klasse=klasse, label=label,
                exam_kind_label=exam_kind_label,
            ),
            encoding="utf-8",
        )

        (units_dir / "_metadata.yml").write_text(META_TPL, encoding="utf-8")

    print(f"Wrote {len(COURSES)} course scaffolds.")


if __name__ == "__main__":
    main()
