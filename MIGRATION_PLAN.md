# Quarto → Hugo (Coder) Migration Plan — `boulingua/efl`

Phase 0 orientation report. Read-only; no files outside this one have been
modified. Awaiting approval before Phase 1.

---

## 1. Repo identity

| Field | Value |
|---|---|
| GitHub remote | `https://github.com/boulingua/efl.git` |
| Default branch | `main` |
| Site title | `EFL — S. Le Boulanger` |
| Site URL | `https://boulingua.github.io/efl/` |
| Language | English (`en`) |
| Audience | Two-track English curriculum (G+M Klassen 5–10, E Klassen 5–13), Baden-Württemberg Gesamtschule |
| Author | S. Le Boulanger |
| Quarto config | `_quarto.yml` (output → `docs/`) |
| Current deploy | `.github/workflows/publish.yml` — Quarto render → GitHub Pages (artifact + `actions/deploy-pages@v4`) |

## 2. Reference repo (`boulingua/website`) snapshot

Cloned to `C:/Users/raban/AppData/Local/Temp/boulingua-reference`.

- Hugo config: TOML (`hugo.toml`).
- Theme: `github.com/luizdepra/hugo-coder` via Hugo Modules (`go.mod` pins
  pseudo-version `v0.0.0-20260305123245-3d3bbd75d7bb`).
- `markup.goldmark.renderer.unsafe = true` — raw HTML allowed in markdown
  (load-bearing for VG Wort pixels).
- Plausible wired through `layouts/_partials/head/extensions.html` (not via
  config) — same `analytics.hellebo.de` script, only the `data-domain`
  differs.
- Author partial in `layouts/_partials/home/author.html`. Otherwise the
  reference site uses theme defaults.
- Content tree is flat: `_index.md`, `about.md`, `philosophy.md`,
  `platforms.md`, `references.md`, `contact.md`, `impressum.md`,
  `datenschutz.md`. No taxonomy / listing pages — meaning the EFL
  Materials hub (Phase 3) has no template to copy from in the reference;
  it must be hand-built but should re-use Coder's listing patterns and
  the reference's CSS variables for visual continuity.

## 3. Content inventory

| Bucket | Count |
|---|---:|
| `.qmd` files total (excluding `docs/` and `.quarto/`) | **585** |
| Public-facing `.qmd` (no leading underscore) | **405** |
| Underscore-prefixed `_unit<NN>_<slug>_exam_body.qmd` partials (`{{< include >}}`d into both unit page and exam PDF) | 180 |
| Top-level pages | 9 (`index`, `about`, `get_started`, `bildungsplan`, `schedule`, `references`, `acknowledgements`, plus legal: `impressum`, `datenschutz`, `haftungsausschluss`) |
| Appendices | 5 (`teaching_workflow`, `skills_decision_tree`, `glossary`, `common_errors`, `writing_rubrics`) |
| Course folders (`track_{e,gm}_kl{05..13}/`) | 15 (each: `index.qmd`, `schedule.qmd`, `units/`) |
| Per course: 12 unit articles + 12 exam wrappers + 12 exam-body partials | 15 × 36 = 540 |
| **VG Wort Zählmarken** (inline raw HTML, see §6) | **399** |

Asset directories:

- `_extensions/downloads/` — Lua shortcode (`{{< downloads >}}`); needs Hugo replacement.
- `_includes/_exam.tex` — LaTeX preamble for exam PDFs.
- `_resources/*.yml` — curriculum data (Bildungsplan codes, outline,
  coverage matrix). Read by `_scripts/`; not directly served. Move to
  `data/` or leave as-is.
- `_scripts/` — Python emitters + `vgwort.lua` (filter; not used in
  practice, see §6) + `make_placeholder_worksheets.py` +
  `organise_downloads.sh` + `pdf_attribution.py`. Most are author-side
  generation tools, not site code; they keep working as-is.
- `assets/` — `light.scss`, `dark.scss`, `_shared.scss`, `slides.scss`,
  `icons/`, `memes/`. Theming + reveal.js styling.
- `appendices/` — content (already counted above).
- `docs/` — Quarto build output, ignore.

Navigation (current Quarto navbar):

- Left: Home · About · Curriculum · Schedule · `Track G+M` menu (Grades
  5–10) · `Track E` menu (Grades 5–13).
- Right: `Legal` menu (Impressum · Datenschutz · Haftungsausschluss) ·
  GitHub icon.
- Footer: long row of inline links (Get Started, Schedule, Bildungsplan,
  five appendices, References, Acknowledgements, three legal pages,
  Kontakt mailto).

## 4. Quarto features in use

| Construct | Where / how | Hugo target |
|---|---|---|
| **Callouts** (`::: {.callout-note}`, `.callout-tip`, `.callout-warning`, with optional `title=`, `collapse="true"`, `icon=false`) | Pervasive across units, exams, appendices | Custom shortcode `layouts/shortcodes/callout.html` rendering note/tip/warning variants with optional collapsible `<details>`. |
| **Custom divs** with class hooks (`::: {.hero}`, `.kicker`, `.lead`, `.card-grid`, `.card`) | Track index pages, home | Pass through as `<div class="…">` (Goldmark `unsafe = true` + `renderer.unsafe`); style with site CSS. Will likely need custom shortcodes for `card-grid` / `card` to avoid hand-writing div soup, but markdown raw HTML is acceptable as fallback. |
| **`{{< downloads >}}` shortcode** | Top of every unit page (180×); reads `track`, `klassenstufe`, `unit_nr`, `slug` from frontmatter and emits a four-link callout (article / slides / worksheet PDF / exam PDF) | Reimplement as `layouts/shortcodes/downloads.html` reading `.Page.Params`. Article link will move to the page itself; slide-deck link target depends on §5 below. |
| **`{{< include _foo.qmd >}}`** | Exam wrappers `{{< include >}}` the underscore body partials | Hugo: convert body partials to `_index.md`-adjacent `.md` files in a `_partials/` content dir excluded from rendering; render via `{{ partial }}` from the exam page template, OR inline the body content directly into both the unit page and the exam page during migration (simpler, content-stable). Pick **inline** to avoid runtime template indirection. |
| **Reveal.js per-unit slide decks** (`format.revealjs:` block, `output-file: unit<NN>_slides.html`, custom theme `assets/slides.scss`) | 180 unit pages | Hugo has no built-in reveal.js; **two options** — (a) keep the existing rendered `_slides.html` artifacts as static drops under `static/slides/<track>/kl<NN>/`, regenerated externally; (b) drop slide-deck rendering entirely and only ship the `.pptx` from the new Materials hub. **Recommendation: (a)** — preserves existing functionality, low risk. |
| **PDF format** (`format.pdf:` on exam wrappers, with `documentclass: scrartcl`, `_includes/_exam.tex`) | 180 exam wrappers (`unit<NN>_<slug>_exam.qmd`) | Hugo cannot produce LaTeX-rendered PDFs. Treat exam-PDF generation as an **external pipeline**: keep the existing `.qmd` exam wrappers in a separate `_exams/` build directory, render via `quarto render` in CI, copy the PDFs into `static/downloads/<track>/kl<NN>/`. The exam **body content** (the prose, exercises, answer key) still migrates to Hugo as part of the unit's `## Exam example` section. |
| **Cross-refs (`@sec-…`, `@fig-…`, `@tbl-…`)** | None found in current grep | n/a |
| **Tabsets (`::: {.panel-tabset}`)** | None found | n/a |
| **Executable code (`{r}`, `{python}` blocks)** | None found | n/a |
| **Listing pages** | None (no `listing:` in nav) | n/a |
| **Lua filter `_scripts/vgwort.lua`** | Registered globally; reads `vgwort_pixel:` from frontmatter and appends an `<img>`. **Not actually triggered** — pixels are embedded as inline raw HTML (see §6). The filter is dead code, kept for future use. | Drop. Not needed in Hugo. |

## 5. Mapping table (one-glance)

| Quarto | Hugo (Coder) |
|---|---|
| `_quarto.yml` | `hugo.toml` |
| `index.qmd` (per dir) | `_index.md` (section) or `index.md` (single) |
| `*.qmd` (top-level) | `content/*.md` |
| `track_e_kl05/units/unit01_hello-world.qmd` | `content/track-e/kl05/units/unit01-hello-world/index.md` (page bundle, hyphens not underscores in URL slugs) |
| YAML frontmatter (Quarto-flavoured) | YAML frontmatter (Hugo-flavoured): drop `format:`, `editor:`, `pagetitle:` (use Hugo's `linkTitle` if needed); keep `title`, `author`, `subtitle`, `tags`, plus all custom keys (`niveau`, `klassenstufe`, `track`, `unit_nr`, `slug`, `bildungsplan`, `skills_focus`) under top-level params. |
| `::: {.callout-note}` etc. | `{{< callout type="note" title="…" collapse="true" >}}` shortcode |
| `::: {.hero}` / `.lead` / `.kicker` / `.card-grid` / `.card` | Raw HTML divs (Goldmark `unsafe = true`) + shortcodes for `card-grid` / `card` to keep authoring readable |
| `{{< downloads >}}` | `{{< downloads >}}` (re-implemented in `layouts/shortcodes/downloads.html`) |
| `{{< include _foo.qmd >}}` | Inline the partial during migration (no runtime equivalent needed) |
| Reveal.js (`format.revealjs`) | External Quarto-only pipeline; output `*_slides.html` copied to `static/slides/...` |
| Exam PDFs (`format.pdf`) | External Quarto-only pipeline; output `*.pdf` copied to `static/downloads/...` |
| Plausible (in `include-in-header:`) | `layouts/_partials/head/extensions.html` (mirror reference repo wiring); `data-domain="boulingua.github.io/efl"` preserved verbatim |
| VG Wort inline `<img>` block | Same inline raw HTML in `.md` body, untouched (§6) |
| Light/dark SCSS (`flatly` + `darkly` overrides) | Coder ships its own light/dark; port custom palette tokens into `assets/scss/coder.scss` overrides. Match reference site's palette where the choice is cosmetic. |
| Slides SCSS | Stays with the Quarto-only slide pipeline; no Hugo concern. |
| Footer (Quarto) | `layouts/_partials/footer.html` override mirroring reference repo, with the same long inline link row. |

## 6. **CRITICAL — VG Wort & Plausible state**

### Plausible

Currently in `_quarto.yml` lines 96–102 (`include-in-header.text`). Exact tag,
**preserve verbatim**:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<script defer data-domain="boulingua.github.io/efl" src="https://analytics.hellebo.de/js/script.file-downloads.outbound-links.js"></script>
<script>window.plausible = window.plausible || function() { (window.plausible.q = window.plausible.q || []).push(arguments) }</script>
```

Port to `layouts/_partials/head/extensions.html` (same path the reference
repo uses). The `data-domain` value must remain **`boulingua.github.io/efl`**.
Fonts also move into the same partial (Source Sans 3 + JetBrains Mono — the
reference repo uses Permanent Marker, so this differs; keep EFL's fonts).

### VG Wort Zählmarken — INVENTORY-CRITICAL

- **399 `.qmd` files** carry inline VG Wort pixels — registered in commit
  `04e088d feat: register VG Wort Zählmarken on EFL content pages`.
- Pattern: a `::: {.vgwort-pixel}` div containing a raw-HTML fenced block
  (` ```{=html} `) with a comment carrying the public ID and an `<img>`
  pointing to `https://vg0X.met.vgwort.de/na/<32-hex-token>` (server is
  consistently `vg09` in samples checked).
- Pixels are **inline content**, not in frontmatter. The Lua filter
  `_scripts/vgwort.lua` is registered globally but never fires (no `.qmd`
  has a `vgwort_pixel:` key). It is dead code.
- This is the **best possible state for migration**: the pixel travels with
  the body content, not via a templating layer. As long as Goldmark
  `unsafe = true` is on (it is in the reference repo), conversion is a
  near-no-op:
  - Drop the `::: {.vgwort-pixel}` div wrapper (or replace with a plain
    `<div class="vgwort-pixel">` so the same CSS hook works).
  - Drop the ` ```{=html} ` fences (Hugo doesn't need them; the inner HTML
    is already raw HTML).
  - Keep the HTML comment + `<img>` byte-identical.
- Phase 0 commits a manifest **`vgwort-manifest.csv`** before any content
  is touched (columns: `qmd_path, article_slug, public_id, pixel_url,
  source_line`). Conversion is then validated row-by-row against the
  rendered `public/`. (Implementation deferred to Phase 2; Phase 0 only
  flags this as the gating step.)

The migration prompt's "(a) inline body" pattern is the right choice
**for this repo**, not "(b) frontmatter + partial", because the pixels
are already inline and have a `<!-- VG Wort Zählmarke (slb) — public ID:
… -->` provenance comment that should remain visible in source for
future audits. Moving them into a frontmatter key would lose that
comment and create needless diff churn.

## 7. Navigation plan (Hugo)

`hugo.toml` `[[menu.main]]` entries:

1. Home (`/`)
2. About (`/about/`)
3. Curriculum (`/bildungsplan/`)
4. Schedule (`/schedule/`)
5. **Materials** (`/materials/`) — **new**, with two sub-listings (`/materials/presentations/`, `/materials/worksheets/`).
6. Track G+M parent + 6 children (Grade 5 → Grade 10) — Coder supports nested menu via `parent =`.
7. Track E parent + 9 children (Grade 5 → Grade 13).
8. Legal parent + 3 children (Impressum, Datenschutz, Haftungsausschluss).
9. GitHub (params.social — render the GitHub icon as Coder does).

Footer: copy the existing long-row link list verbatim into a custom footer
partial.

## 8. Risk list — items to decide before Phase 1

1. **Slide decks.** Reveal.js is Quarto-only. Recommended: keep an external
   Quarto-only pipeline that emits `*_slides.html` into `static/slides/`,
   triggered from the same CI workflow. Confirm.
2. **Exam PDFs.** Same story (LaTeX). Recommended: same external pipeline,
   output to `static/downloads/<track>/kl<NN>/`. Confirm.
3. **`{{< include >}}` for exam bodies.** Two options: (a) inline the body
   content into both the unit page (`## Exam example` section) and the exam
   PDF source during migration; (b) keep a partial-include mechanism via a
   Hugo shortcode that reads from a sibling `_partials/` content dir.
   **Recommended: (a)** — simpler, content-stable, no template indirection.
   Net effect on word count: zero (content is the same, only file layout
   changes). Confirm.
4. **URL slug changes.** Quarto serves `/track_e_kl05/units/unit01_hello-world.html`;
   Hugo conventionally uses hyphens (`/track-e/kl05/units/unit01-hello-world/`).
   Either (a) accept the URL change and add Hugo `aliases:` redirects from
   the old paths, or (b) configure Hugo `permalinks` to keep underscores
   and `.html` extension. **Recommended: (a)** — cleaner long-term;
   aliases cover SEO and bookmarks. Confirm.
5. **Materials hub thumbnails.** The prompt asks for real one-page
   `.pptx` / `.pdf` placeholders + rendered thumbnails. The repo already
   has `_scripts/make_placeholder_worksheets.py` (reportlab) — reuse and
   add a `.pptx` generator (`python-pptx`). LibreOffice headless or
   `pdf2image` for PNG thumbnails will work in the GitHub Actions Ubuntu
   runner; less reliable on Windows for local builds. Confirm CI is the
   source of truth for placeholder generation.
6. **Per-article materials for non-unit pages.** Phase 3 says "every
   migrated article gets dummy presentation + worksheet". Strictly
   applying this would attach `.pptx` + `.pdf` placeholders to
   `impressum`, `datenschutz`, `references`, etc. — which is wrong.
   **Restrict to the 180 unit pages** (and arguably the 15 course
   index pages? — probably not). Decide before Phase 3.
7. **`hugo-coder` pinning.** Reference repo pins a 2026-03 pseudo-version.
   Use the **same exact pin** for visual consistency (footer credits,
   icon set). Confirm.
8. **Worksheet ↔ Materials-hub overlap.** The existing
   `_scripts/make_placeholder_worksheets.py` already produces real
   `worksheet.pdf` files served at `/downloads/<track>/kl<NN>/...`. The
   new Materials/Worksheets hub from Phase 3 would be a second worksheet
   surface with its own placeholders under `/materials/worksheets/`.
   This is **two parallel worksheet sets** with overlapping intent.
   Likely the right move is to point the new Materials/Worksheets hub at
   the **existing** `unit<NN>_<slug>_worksheet.pdf` artifacts (already
   generated, attribution-checked in CI) and only build the
   Presentations side as net-new. Decide before Phase 3.
9. **Lua filter retirement.** `_scripts/vgwort.lua` is unused. Phase 4
   can delete it (along with the rest of the Quarto-specific scripts
   that survive only because they fed Quarto). Confirm.

## 9. File-by-file migration order (Phase 2)

Batch order, each batch one commit (`content: migrate <section> from
quarto to hugo (N files)`):

1. **Top-level pages** (9): `index`, `about`, `get_started`, `bildungsplan`, `schedule`, `references`, `acknowledgements`, `impressum`, `datenschutz`, `haftungsausschluss`. — small, sets the conventions.
2. **Appendices** (5): `teaching_workflow`, `skills_decision_tree`, `glossary`, `common_errors`, `writing_rubrics`.
3. **Course indexes** (15): `track_{e,gm}_kl{05..13}/index.qmd` + their `schedule.qmd` (30 files).
4. **Track G+M units** Klasse 5 → Klasse 10 (6 batches, ~36 files each batch including unit + exam-wrapper + exam-body inlined): `track_gm_kl05` … `track_gm_kl10`.
5. **Track E units** Klasse 5 → Klasse 13 (9 batches): `track_e_kl05` … `track_e_kl13`.

Validation: after each batch, run `hugo --minify`, run the per-file
word-count diff (>2% drift → flag in §10), verify VG Wort pixel count
matches manifest for the batch.

## 10. Manual review needed

(empty — populated during Phase 2 as drift is detected)

---

## Phase log

### 2026-05-06 — Phase 0 complete

- Inventory: 585 `.qmd`, 399 VG Wort pixels (inline), 180 reveal.js decks,
  180 exam PDFs.
- Reference repo studied; theme pin recorded.
- Quarto features inventoried: callouts, custom divs, `{{< downloads >}}`
  shortcode, `{{< include >}}` (180×). No tabsets, no cross-refs, no
  executable code blocks, no listing pages.
- Plausible snippet captured verbatim. VG Wort pixels confirmed inline
  (not via the Lua filter, which is dead code).
- Nine open decisions logged in §8 — most have a recommended default;
  awaiting approval to proceed.

**Awaiting approval before Phase 1.**

### 2026-05-06 — Phase 1 complete

- Branch `migration/hugo-coder` cut from `main`. Local git author set to
  `s-leboulanger <277736839+s-leboulanger@users.noreply.github.com>`
  for this repo only.
- Hugo skeleton scaffolded at repo root alongside the live Quarto setup:
  - `hugo.toml` (TOML, mirroring reference repo), full `[[menu.main]]`
    tree including the new `Materials` parent + `Presentations` /
    `Worksheets` children, both Track parents with all grade children,
    Legal parent + 3 children, GitHub social link.
  - `go.mod` + `go.sum` pin `github.com/luizdepra/hugo-coder
    v0.0.0-20260305123245-3d3bbd75d7bb` — byte-identical to the
    reference repo's pin.
  - `layouts/_partials/head/extensions.html` carries the full Plausible
    snippet (verbatim `data-domain="boulingua.github.io/efl"` + the
    `analytics.hellebo.de` script src) plus the EFL fonts (Source Sans 3
    + JetBrains Mono).
  - Empty Hugo dirs (`archetypes/`, `assets/scss/`, `data/`, `i18n/`,
    `layouts/shortcodes/`, `static/css/`, `static/materials/{presentations,worksheets}/`,
    `static/downloads/`, `static/slides/`) seeded with `.gitkeep`.
  - `content/_index.md` placeholder for the home page (real copy lands
    in Phase 2).
  - `static/css/custom.css` placeholder (palette/typography overrides
    deferred to Phase 2).
- CI:
  - `.github/workflows/hugo.yml` added: builds on `main` and any
    `migration/**` branch; Pages deploy gated to `main` only so Phase 2
    work doesn't accidentally publish a half-migrated site. Includes a
    grep gate that fails the build if the Plausible `data-domain`
    string is missing from `public/index.html` — first half of the
    Plausible parity check from the prompt.
  - `.github/workflows/publish.yml` renamed → `publish.yml.disabled` so
    Quarto no longer fires while the two setups coexist.
- **`.gitignore` adjustment (one-line decision logged here):** the
  existing `*.html` rule was ignoring every file under `layouts/`,
  which makes Hugo non-functional. Added `!layouts/**/*.html` to
  un-ignore Hugo layout files, plus `/public/`, `/resources/`, and
  `.hugo_build.lock` for Hugo build artefacts. No existing rules were
  removed; the Quarto-relevant entries are intact.
- Quarto setup is **untouched** — `_quarto.yml`, all `.qmd` files,
  `_extensions/`, `_includes/`, `_resources/`, `_scripts/`, `assets/`,
  `appendices/`, all 15 course folders remain in place. Both setups
  coexist on this branch until Phase 4.

**Awaiting approval before Phase 2.**

### 2026-05-06 — Phase 2 complete

- VG Wort manifest committed first (`vgwort-manifest.csv`, 399 rows,
  399 unique public IDs) before any content was touched. Generated by
  `_scripts/build_vgwort_manifest.py`.
- Hugo shortcodes added (`layouts/shortcodes/`): `callout`, `downloads`,
  `card-grid`, `card`, `hero`, `kicker`, `lead`. The `callout`
  shortcode handles the edge-case Quarto attribute string with nested
  double-quotes around `"Bildungsplan"` (escaped as `\"`).
- Migrator (`_scripts/migrate_to_hugo.py`) is deterministic and
  idempotent. Per-file word-count parity checks ran on every file:
  **zero drift across all 405 public-facing `.qmd` files.** The metric
  strips both Quarto and Hugo markup symmetrically and treats `_`, `-`,
  `/` as word separators so URL slug rewrites do not register as drift.
- Content migrated, in 17 commits matching the Phase 0 §9 order:
  - 15 top-level + appendices (1 commit)
  - 30 course indexes + schedules (1 commit)
  - 6 × Track G+M Klassenstufen (6 commits, 24 files each)
  - 9 × Track E Klassenstufen (9 commits, 24 files each)
  - Total: **405 destination `.md` files** (matches Phase 0 inventory).
  - The 180 underscore-prefixed `_unit<NN>_<slug>_exam_body.qmd`
    partials were inlined into both their unit page and their exam
    wrapper (Phase 0 §8 decision (a)), not migrated as their own pages.
- VG Wort verification:
  - `_scripts/verify_all_pixels.py` checked all 399 manifest rows
    against `content/.../index.md`: **399 ok, 0 missing, 0 duplicated**.
  - `_scripts/verify_rendered_pixels.py` checked the same against the
    rendered `public/`: **399 ok**, 414 total occurrences across 855
    HTML pages (the +15 surplus comes from the unit-page + exam-wrapper
    pairs that share an inlined exam-body pixel — identical behaviour
    to the Quarto build).
- Aliases: every migrated page records its old Quarto URL. Hugo
  generated 430 alias-redirect HTML pages. Spot-checked
  `/track_e_kl05/units/unit01_hello-world.html` → 301 to
  `/track-e/kl05/units/unit01-hello-world/`.
- `hugo --minify` build summary: **434 pages, 430 aliases, 11 static
  files, zero errors, 1.8s.**
- Plausible verified in rendered `public/index.html` (the CI grep was
  updated to be quote-tolerant since `--minify` strips quotes around
  attribute values).
- Six fix commits beyond the 17 batch commits:
  - link-rewriter `track_<x>_kl<NN>` handling + `index.qmd`-link
    `//` bug.
  - slug → unit_slug frontmatter rename (Hugo's `slug` is magic and
    overrode bundle-derived URLs).
  - ` ```{mermaid} ` → ` ```mermaid ` (Goldmark attribute-parse error).
  - `lang:` dropped from the three German legal pages (Hugo v0.144
    deprecation).
  - `static/css/custom.css` → `assets/css/custom.css` (Coder runs
    `customCSS` through Hugo Pipes / `resources.Get`).
  - CI Plausible-grep tolerates minified attribute syntax.

### Manual review needed

(empty — no files crossed the 2% drift threshold.)

**Awaiting approval before Phase 3.**

### 2026-05-06 — Phase 3 complete

- Materials hub at `/materials/` with two listings:
  `/materials/presentations/` and `/materials/worksheets/`. Top-level
  `/materials/` is a narrative landing page; the two children are
  auto-generated card grids.
- Per Phase 0 §8 recommended defaults:
  - Per-unit material attachments restricted to **180 unit pages**
    (exam wrappers, schedules, track indexes, top-level pages,
    appendices: skipped). Hub filters via `Params.unit_nr` presence.
  - Worksheets hub points at the **existing**
    `_scripts/make_placeholder_worksheets.py` PDFs at
    `/downloads/<track>/kl<NN>/unit<NN>_<slug>_worksheet.pdf`. Only
    the `--out` base moved (now `static/downloads/`).
  - Presentations hub is **net-new**: 180 placeholder `.pptx` files via
    `_scripts/make_placeholder_presentations.py` (python-pptx,
    one-slide 16:9 deck per unit, `S. Le Boulanger` in core
    properties, "Placeholder — replace with final presentation."
    caption).
  - 180 worksheet + 180 presentation thumbnail PNGs via Pillow
    (`_scripts/make_placeholder_thumbnails.py`). LibreOffice / pdf2image
    skipped — fragile in CI, overkill for placeholders.
- Front-matter augmentation: `_scripts/add_material_frontmatter.py`
  walks every `content/track-*/kl*/units/*/index.md`, skips
  `*-exam` wrappers, and inserts (or rewrites, idempotently) two
  YAML blocks per unit page:
  ```yaml
  presentation:
    file: /materials/presentations/<track>/kl<NN>/unit<NN>_<slug>.pptx
    thumbnail: /materials/presentations/<track>/kl<NN>/unit<NN>_<slug>.png
  worksheet:
    file: /downloads/<track>/kl<NN>/unit<NN>_<slug>_worksheet.pdf
    thumbnail: /materials/worksheets/<track>/kl<NN>/unit<NN>_<slug>.png
  ```
  Verified: 180 unit pages augmented, 180 exam wrappers skipped.
- Hugo plumbing:
  - `layouts/materials/list.html` — single template drives both
    sub-listings (`material_kind: "presentation"` / `"worksheet"`
    in the listing page's front matter selects which card variant
    to render). Top-level `/materials/` falls through to a plain
    content render.
  - `layouts/_partials/page.html` overrides Coder's partial of the
    same name, injecting `layouts/_partials/material-links.html`
    (paired thumbnail-card block) above `.Content` when both
    `presentation:` and `worksheet:` front-matter keys are present.
  - Tag chips: `track-{e,gm}`, `klasse-NN`, `niveau-{e,m,g,…}` —
    derived from existing front matter, **no invented topical tags**.
  - Search: vanilla-JS title-substring filter + multi-select tag
    filter. Pagefind was the prompt's recommended choice but its
    CLI dependency would have added a non-trivial CI step for a
    180-page index; the lighter approach is sufficient for now and
    can be swapped in later without breaking the listing markup.
- Generated artefact strategy: the 720 placeholder binaries
  (180 PDFs + 180 PPTX + 360 PNGs) are **gitignored** and
  regenerated in CI on every build. When real materials ship,
  drop them at the same canonical paths and either relax the
  ignore patterns file-by-file with `!` or remove them entirely.
- CI workflow now installs `python-pptx` + `Pillow` alongside the
  existing `reportlab` + `pypdf` + `pyyaml` deps and runs all three
  placeholder generators before `hugo --minify`.
- Build status: **440 pages, 731 static files, 430 aliases, zero
  errors.**
- VG Wort: still **399 of 399** pixels found in `public/`
  (Materials hub pages do not get pixels — they're navigation, not
  articles, per Phase 0 §8 decision 4).
- Spot-checked: `<title>Presentations · EFL</title>` on the listing,
  180 unique unit hrefs in the presentations grid, 180 in the
  worksheets grid, and the `<aside class="material-links">` block
  appears on every unit page.

**Awaiting approval before Phase 4.**
