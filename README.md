# EFL

A two-track English curriculum for comprehensive school —
**Track G+M (Grades 5–10)** for Hauptschul-/Realschulabschluss and
**Track E (Grades 5–13)** through Abitur. Fifteen courses, twelve
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
| 0 — Preflight | curriculum framework ("Bildungsplan") chapter codes from bildungsplaene-bw.de | **complete** |
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

- Teaching content (prose): **[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)** (see `LICENSE`).
- Code and site scaffolding: **[MIT](LICENSE-CODE.md)**.

## Citation

If you use these materials, please cite the site rather than
individual pages. See the
[References](https://boulingua.github.io/efl/references.html#citing-this-course)
page for APA + BibTeX. Short form:

```bibtex
@misc{leboulanger2026efl,
  author       = {Le Boulanger, S.},
  title        = {{EFL}: A Two-Track English Curriculum for
                  Comprehensive School (Grades 5--13)},
  year         = {2026},
  howpublished = {\url{https://boulingua.github.io/efl/}},
  note         = {Open educational resource.
                  Code: MIT; teaching content: CC-BY 4.0}
}
```

## Legal

Before going public, fill in the Impressum (`impressum.qmd`) and
have the Datenschutzerklärung (`datenschutz.qmd`) reviewed by a
Datenschutzbeauftragte or lawyer. See the `ACTION REQUIRED`
callouts on those pages.

## Use of LLM tools

Portions of this project were prepared with assistance from large language model tooling for narrowly defined, non-authorial tasks: copyediting, prose smoothing, Markdown/LaTeX formatting, scaffolding of boilerplate files (CI configs, build scripts), code refactoring. The tools used were Chat AI, the LLM service of KISSKI (GWDG), and a self-hosted Mistral Small (24B, Apache-2.0) run locally via Ollama and the ollamar R package — local inference only, with no data sent to third parties for the self-hosted model.
