"""Batch-emit Track E Klasse 9 — all 12 Units.

Niveau E version of Klasse 9: shares cast (Eli, Naima, Mr. Yilmaz)
and theme arc with G+M Klasse 9. Bildungsplan prefix 3.2 (Klassen
7/8/9).
"""
from __future__ import annotations
import pathlib
import importlib.util

REPO = pathlib.Path(__file__).resolve().parent.parent
COURSE = REPO / "track_e_kl09" / "units"

GM_PATH = REPO / "_scripts" / "_emit_kl09_gm_units.py"
spec = importlib.util.spec_from_file_location("kl09_gm", GM_PATH)
gm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gm)
UNITS = [dict(u) for u in gm.UNITS]


UNIT_TPL = """---
title: "Unit {n} — {title}"
subtitle: "Track E · Klasse 9 · Niveau E"
niveau: "E"
klassenstufe: 9
track: "e"
unit_nr: {n}
slug: "{slug}"
bildungsplan:
{bp_yaml}
skills_focus:
{skills_yaml}
format:
  html: {{ toc: true, toc-depth: 3 }}
  revealjs:
    output-file: "unit{nn}_slides.html"
    theme: [default, ../../assets/slides.scss]
    slide-number: c/t
    progress: true
    scrollable: true
    transition: none
---

::: {{.callout-note}}
**Template:** Activate → Input → Practise → Produce → Reflect.\\
**Niveau:** E. class test (Klassenarbeit) at Niveau E (45 BE).
:::

{{{{< downloads >}}}}

## Learning objectives

{objectives}

## curriculum framework (Bildungsplan) alignment

{bp_bullets}

(Source: <https://www.bildungsplaene-bw.de/,Lde/LS/BP2016BW/ALLG/SEK1/E1>)

## Lead-in story

{leadin}

## 1. Activate

{activate}

## 2. Input

{input_sections}

## 3. Practise

### Niveau E — controlled

{practise_g}

### Niveau E — productive

{practise_m}

::: {{.callout-tip collapse="true" title="Answer key"}}
**Controlled.** {answer_g}

**Productive.** {answer_m}
:::

## 4. Produce

{produce}

### Sample

{produce_sample}

## 5. Reflect

{reflect_list}

**One thing in your notebook:** *Write one sentence using something you learned in this Unit.*

## Exam example

{{{{< include _unit{nn}_{slug}_exam_body.qmd >}}}}

## Downloads

{{{{< downloads >}}}}

::: {{.notes}}
**Slide deck timing.** 45 minutes total. Lead-in 4 min · Activate
5 min · Input 14 min · Practise 8 min · Produce 11 min · Reflect 3 min.

**Differentiation.** Below Niveau E: scaffold card with the key
structure. Above Niveau E: extension prompt linking to Klasse 10.
:::

## Common pitfalls

{pitfalls}

## Further reading / listening

{further}
"""

EXAM_BODY_TPL = """::: {{.callout-warning icon=false title="class test (Klassenarbeit) — Niveau E (45 minutes)"}}
**Time.** 45 minutes. **Total.** 45 points.
:::

### Task 1 — Listening (10 BE)

{exam_listening}

### Task 2 — Reading (12 BE)

{exam_reading}

### Task 3 — Use of English (10 BE)

{exam_use}

### Task 4 — Writing (13 BE)

{exam_writing}

::: {{.callout-tip collapse="true" title="Answer key"}}
{exam_keys}
:::

::: {{.callout-tip collapse="true" title="grading scale (Notenschlüssel) (von 45)"}}
| 42–45 | 1 | 36–41 | 2 | 30–35 | 3 |
| 22–29 | 4 | 13–21 | 5 |  0–12 | 6 |
:::
"""

EXAM_WRAP_TPL = """---
title: "class test (Klassenarbeit) — Unit {n}: {title}"
subtitle: "Track E · Klasse 9 · Niveau E · 45 Minuten"
author: "S. Le Boulanger"
niveau: "E"
klassenstufe: 9
track: "e"
unit_nr: {n}
slug: "{slug}"
format:
  pdf:
    documentclass: scrartcl
    papersize: a4
    fontsize: 11pt
    geometry: [margin=22mm]
    include-in-header: ["../../_includes/_exam.tex"]
    keep-tex: false
---

# class test (Klassenarbeit) — Unit {n}: {title}

**Track E · Klasse 9 · Niveau E · 45 Minuten**

{{{{< include _unit{nn}_{slug}_exam_body.qmd >}}}}
"""


def emit() -> None:
    COURSE.mkdir(parents=True, exist_ok=True)
    for u in UNITS:
        nn = f"{u['n']:02d}"
        bp_yaml = "\n".join(f'  - "{c}"' for c in u["bp"])
        skills_yaml = "\n".join(f"  - {s}" for s in u["skills"])
        objectives = "\n".join(f"- *{o}*" for o in u["objectives"])
        bp_bullets = "\n".join(f"- **{c}**" for c in u["bp"])
        input_sections = "\n\n".join(
            f"### {h}\n\n{b}" for h, b in u["input_blocks"]
        )
        practise_g = "\n".join(u["practise_g"])
        practise_m = "\n".join(u["practise_m"])
        reflect_list = "\n".join(f"- [ ] {r}" for r in u["reflect"])
        pitfalls = "\n".join(f"- {p}" for p in u["pitfalls"])
        further = "\n".join(f"- {f}" for f in u["further"])

        unit_md = UNIT_TPL.format(
            n=u["n"], nn=nn, slug=u["slug"], title=u["title"],
            bp_yaml=bp_yaml, skills_yaml=skills_yaml,
            objectives=objectives, bp_bullets=bp_bullets,
            leadin=u["leadin"], activate=u["activate"],
            input_sections=input_sections,
            practise_g=practise_g, practise_m=practise_m,
            answer_g=u["answer_g"], answer_m=u["answer_m"],
            produce=u["produce"], produce_sample=u["produce_sample"],
            reflect_list=reflect_list,
            pitfalls=pitfalls, further=further,
        )
        exam_body_md = EXAM_BODY_TPL.format(
            exam_listening=u["exam_listening"],
            exam_reading=u["exam_reading"],
            exam_use=u["exam_use"],
            exam_writing=u["exam_writing"],
            exam_keys="\n".join(u["exam_keys"]),
        )
        exam_wrap_md = EXAM_WRAP_TPL.format(
            n=u["n"], nn=nn, slug=u["slug"], title=u["title"],
        )

        (COURSE / f"unit{nn}_{u['slug']}.qmd").write_text(unit_md, encoding="utf-8")
        (COURSE / f"_unit{nn}_{u['slug']}_exam_body.qmd").write_text(exam_body_md, encoding="utf-8")
        (COURSE / f"unit{nn}_{u['slug']}_exam.qmd").write_text(exam_wrap_md, encoding="utf-8")

    print(f"Wrote {len(UNITS) * 3} files for Track E Klasse 9.")


if __name__ == "__main__":
    emit()
