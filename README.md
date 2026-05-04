# EFL

A two-track English curriculum for Gesamtschule Baden-Württemberg —
**Track G+M (Klasse 5–10)** for Hauptschul-/Realschulabschluss and
**Track E (Klasse 5–13)** through Abitur. Fifteen courses, twelve
Units each, one source per Unit rendering both an HTML article and
a Reveal.js slide deck, plus a worked Klassenarbeit (Kl. 5–10) or
Abitur-Aufgabe (Kl. 11–13). Authored by **S. Le Boulanger**.

Live site: <https://boulingua.github.io/efl/> (after first deploy).

## Status

All seven build phases complete. **180 Units** across **15 courses**.
See `HANDOVER.md` for follow-up author tasks (worksheet PDFs,
Impressum + Datenschutz fill-in, deeper Bildungsplan alignment).

| Phase | Goal | State |
|-------|------|-------|
| 0 — Preflight | curriculum framework (Bildungsplan) chapter codes from bildungsplaene-bw.de | **complete** |
| 1 — Scaffold | deployable empty shell | **complete** |
| 2 — Outline | 15×12 Unit map | **complete** |
| 3 — Prototype | Track G+M Klasse 7 end-to-end | **complete** |
| 4 — Fan-out | remaining 14 courses | **complete** |
| 5 — Polish | glossary anchors, schedule, coverage matrix, skills tree | **complete** |
| 6 — Handover | HANDOVER.md | **complete** |

## Local build

```bash
pip install pyyaml pandas reportlab pypdf
python _scripts/make_placeholder_worksheets.py     # placeholder PDFs (no-op pre-Phase-2)
quarto render
```

The CI workflow at `.github/workflows/publish.yml` runs the same
sequence and deploys the `docs/` output to GitHub Pages.

## Layout

- `index.qmd`, `about.qmd`, `bildungsplan.qmd`, `schedule.qmd`,
  `impressum.qmd`, `datenschutz.qmd` — top-level pages.
- `appendices/` — teaching workflow, skills tree, glossary,
  common errors, writing rubrics.
- `track_gm_kl05/` … `track_gm_kl10/` — six Track G+M courses.
- `track_e_kl05/` … `track_e_kl13/` — nine Track E courses.
- `assets/` — Lucide icons, generic SVG meme placeholders,
  `slides.scss` for Reveal.js.
- `_includes/_exam.tex` — shared LaTeX header (PDF metadata +
  watermark + footer attribution).
- `_extensions/downloads/` — `{{< downloads >}}` Lua shortcode.
- `_resources/` — Bildungsplan YAMLs, curriculum outline,
  generation log.
- `_scripts/` — placeholder-PDF generator, attribution helper,
  download organiser.

## Licence

- Code and site scaffolding: **MIT** (see `LICENSE`).
- Teaching content: **CC-BY-SA 4.0**.

## Legal

Before going public, fill in the Impressum (`impressum.qmd`) and
have the Datenschutzerklärung (`datenschutz.qmd`) reviewed by a
Datenschutzbeauftragte or lawyer. See the `ACTION REQUIRED`
callouts on those pages.
