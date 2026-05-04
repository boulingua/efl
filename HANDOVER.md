# EFL — Handover

This document records the state of the repository at the end of the
seven-phase build (Phase 6: handover). It is intended for the
author (S. Le Boulanger) and any future maintainer.

## What ships

A two-track English curriculum for a Gesamtschule in Baden-
Württemberg: **Track G+M** (Klassen 5–10) and **Track E** (Klassen
5–13). 15 courses, 12 Units per course, **180 Units total**.

| Layer | Count |
|-------|------:|
| Courses | 15 |
| Units (HTML article + Reveal.js slide deck per source) | 180 |
| Exam-wrapper PDF sources (`unit<NN>_<slug>_exam.qmd`) | 180 |
| Exam-body partials (`_unit<NN>_<slug>_exam_body.qmd`) | 180 |
| **Authored `.qmd` files** | **540** |
| Top-level pages (index, about, get_started, schedule, references, acknowledgements, bildungsplan, impressum, datenschutz) | 9 |
| Appendices (teaching_workflow, skills_decision_tree, glossary, common_errors, writing_rubrics) | 5 |
| curriculum framework (Bildungsplan) resource YAMLs | 15 |
| Build scripts | 16 |

## Phase log

| Phase | Goal | State |
|-------|------|-------|
| 0 — Preflight | curriculum framework (Bildungsplan) chapter codes from <https://www.bildungsplaene-bw.de/> | **complete** (live fetch 2026-04-30; chapter skeleton in 15 YAMLs) |
| 1 — Scaffold | deployable empty shell | **complete** |
| 2 — Outline | 15×12 Unit map approved | **complete** (`_resources/curriculum_outline.yml`) |
| 3 — Prototype | Track G+M Klasse 7 end-to-end (style reference) | **complete** |
| 4 — Fan-out | remaining 14 courses | **complete** |
| 5 — Polish | glossary anchors, schedule, coverage matrix, skills tree | **complete** |
| 6 — Handover | this document | **complete** |

## Recurring cast by Klassenstufe

| Klassenstufe | Cast |
|--------------|------|
| 5 | Mia, Theo, Frida the fox, Mr. Flint |
| 6 | Sam, Lina, Mr. Flint, Captain Cody |
| 7 | Aisha, Ben, Ms. Reyes |
| 8 | Jonas, Hawa, global pen-pal class |
| 9 | Eli, Naima, Mr. Yilmaz |
| 10 G+M | Sam (returning), Maja, young-adult ensemble |
| 10 E | Maja, young-adult ensemble |
| 11 | narrators and author voices (texts as cast) |
| 12 | texts as characters: speakers, writers, public voices |
| 13 | public voices and contemporary writers |

## Set texts cited / used

- *Klara and the Sun* (Ishiguro, 2021) — Klasse 11 Basisfach focus
- *Macbeth* (Shakespeare, 1606) — Klasse 11 Leistungsfach focus
- Sonnet 73 (Shakespeare) — Klasse 12
- *1984* (Orwell, 1949), *Brave New World* (Huxley, 1932), *The
  Handmaid's Tale* (Atwood, 1985) — Klasse 12 dystopia Unit
- *The Dispossessed* (Le Guin, 1974), *Utopia* (More, 1516) —
  Klasse 13 dystopia / utopia Unit
- *Things Fall Apart* (Achebe, 1958), *Purple Hibiscus* (Adichie,
  2003), *A Bend in the River* (Naipaul, 1979) — Klasse 11 + 12
  post-colonial Units
- Contemporary lyric: Vuong, Shire, Long Soldier — Klasse 13

## Conventions

- **Author by metadata.** Each course's `units/_metadata.yml`
  contains `author: "S. Le Boulanger"`; Quarto inherits this into
  every Unit.
- **English (German) form.** When a German technical term appears
  in English prose, write *English term (German term)* on first /
  prominent occurrence (e.g. *class test (Klassenarbeit)*,
  *grading scale (Notenschlüssel)*). Applied via
  `_scripts/_normalize_german_terms.py`.
- **Exam content = single source.** Each Unit's exam material
  lives in `_unit<NN>_<slug>_exam_body.qmd`; both the Unit's
  `## Exam example` section and the standalone PDF wrapper
  `{{< include >}}` it.
- **`{{< downloads >}}` shortcode** at the top and bottom of each
  Unit emits four links (article, slides, worksheet PDF, exam
  PDF).

## Known follow-ups (author tasks)

- **Worksheet PDFs.** Currently shipped as placeholders (one-page
  A4 with attribution + watermark). Drop real worksheets in the
  same canonical paths to replace.
- **`impressum.qmd` + `datenschutz.qmd`** still contain `<TODO:
  Anschrift>` and `<TODO: kontakt@domain.tld>` placeholders.
  Fill in **before going public**. Consider a Datenschutz-
  beauftragte / lawyer review.
- **Niveau-specific Kompetenzaussagen.** The 15 curriculum
  framework (Bildungsplan) YAMLs hold the verbatim chapter
  skeleton (codes + German labels) fetched live from
  bildungsplaene-bw.de. The fine-grained Kompetenzaussagen per
  Niveau (G / M / E or BF / LF) are cited inside individual
  Units as needed; a future pass could pull all of them into the
  YAMLs as structured data.
- **Klasse 7 E.** Generated from the Klasse 7 G+M prototype by
  scripted reframing (`_scripts/_emit_kl07_e_units.py`). A future
  pass could enrich it with one extra grammar nuance per Unit
  the way the kl05_e / kl06_e variants do.
- **Coverage matrix.** `_resources/coverage_matrix.yml` is
  generated from front-matter scans. The current Units cite the
  high-level chapter codes (3.x.y); finer codes (3.x.y.z) appear
  in some Units. A future pass could enforce minimum-three-
  chapters-per-Unit alignment.

## How to build / preview

```bash
pip install pyyaml pandas reportlab pypdf
python _scripts/make_placeholder_worksheets.py
quarto render
```

The CI workflow at `.github/workflows/publish.yml` does the same
and deploys `docs/` to GitHub Pages via the official
`actions/deploy-pages@v4` actions. Pages Source must be set to
"GitHub Actions" on the repo settings.

## How to extend

1. Add a new Unit slot to
   `_resources/curriculum_outline.yml`.
2. Either author the Unit by hand using the prototype course
   (`track_gm_kl07/units/`) as a style reference, or extend the
   relevant `_emit_kl<NN>_<gm|e>_units.py` script.
3. Re-run `python _scripts/_phase5_polish.py` to refresh the
   schedule, coverage matrix, and skills decision tree.
4. `quarto render`.

## How to swap real worksheets in

For each Unit with a real worksheet PDF, place it at
`docs/downloads/<track>/kl<NN>/unit<NN>_<slug>_worksheet.pdf`. The
filename convention is fixed; no site-code change needed. The
attribution helper in `_scripts/pdf_attribution.py` provides a
reusable header/footer/watermark for new generators so the visual
style does not drift.

## Sources of truth

| Object | Source |
|--------|--------|
| Author | each course's `units/_metadata.yml` |
| Bildungsplan codes | `_resources/bildungsplan_bw_*.yml` (live-fetched 2026-04-30) |
| Curriculum outline | `_resources/curriculum_outline.yml` |
| Per-Unit alignment | each Unit's `bildungsplan:` front-matter list |
| Coverage matrix | `_resources/coverage_matrix.yml` (generated) |
| Theme arcs and casts | `_scripts/_phase5_polish.py` (CAST + THEME_ARC dicts) |
| Style reference | `track_gm_kl07/units/unit01_first-day-back.qmd` (prototype) |

## Final status

```
Site:               https://boulingua.github.io/efl/
Total commits:      ~64 (counting from initial scaffold to handover)
Total .qmd files:   540 (Units 180 + wrappers 180 + bodies 180) +
                    9 top-level + 5 appendices + 30 course pages =
                    584 authored .qmd files
Total Bildungsplan: chapter skeleton complete; per-Unit citations
                    complete (3.x.y level)
Phase 6:            COMPLETE.
```
