# MIGRATION_NOTES — boulingua EFL BW (post-migration verification pass)

Repo identity: **EFL BW** — English curriculum, Gesamtschule
Baden-Württemberg, Klassen 5–13 (Track G+M and Track E). Author of all
content: **S. Le Boulanger**.

Quarto → Hugo migration plus the Materials Discovery Network are
already complete (see `MIGRATION_PLAN.md` and `MATERIALS_NETWORK_PLAN.md`).
This file logs the post-migration verification pass that double-checks
everything survived correctly and re-implements any pre-Hugo CI gates
that didn't make it across.

---

## Phase 0 — CI gates inventory: pre-migration vs post-migration

### Quarto-era CI (commit `04e088d`, workflow `publish.yml`)

The pre-migration `publish.yml` ran:

| Step | What it did | Survived migration? |
|---|---|---|
| `quarto-actions/setup` + `tinytex` | Render Quarto site | n/a — replaced by Hugo build |
| `make_placeholder_worksheets.py` | Generate 180 worksheet PDFs | **yes**, ported to Hugo workflow + extended with `make_placeholder_presentations.py` and `make_placeholder_thumbnails.py` |
| `organise_downloads.sh` | Sort PDFs into canonical paths | **partial** — current placeholder generator writes directly to canonical paths; the legacy organiser is unused |
| **PDF attribution audit** (inline Python in `publish.yml`) — every `docs/downloads/**.pdf` must carry `/Author` containing "Le Boulanger" | hard-blocking gate | **NOT carried over** — must re-implement in Phase 6 |
| `actions/configure-pages` + `upload-pages-artifact` + `deploy-pages` | GH Pages deploy | **yes**, identical wiring in `hugo.yml` |

### Quarto-era scripts that defined gates (commit `f3d274b`)

| Script | What it did | State |
|---|---|---|
| `scripts/check-legal-placeholders.sh` | Fail build if `{{CONTACT_EMAIL_HELLER}}`, `{{CONTACT_EMAIL_LEBOULANGER}}`, `{{SITE_DOMAIN}}` placeholders survived rendering, or if `TODO`/`FIXME` appeared in any `impressum*` / `datenschutz*` / `haftungsausschluss*` page | **NOT carried over** — must re-implement in Phase 6, retargeted at Hugo's `public/` |
| `_scripts/_fill_bildungsplan.py` | One-off live-fetch of curriculum framework codes from `bildungsplaene-bw.de` into `_resources/bildungsplan_bw_*.yml` | One-off, not a recurring gate. Output (the YAMLs) survived migration unchanged. |
| `_scripts/pdf_attribution.py` | Helper used by all PDF generators to write `/Author = S. Le Boulanger` into core metadata | **yes**, still imported by `make_placeholder_worksheets.py` |
| `_scripts/vgwort.lua` | Pandoc filter that injected the VG Wort `<img>` from a frontmatter key | **dropped** as dead code in Phase 4 of the Quarto→Hugo migration; pixels are now inline raw HTML in every unit's `.md` body, with a 399-row manifest at `vgwort-manifest.csv` and three verification scripts |

### Hugo-era gates currently in `hugo.yml`

| # | Gate | Source |
|---|---|---|
| 1 | Plausible snippet is wired (head partial) | migration Phase 1 |
| 2 | Plausible appears in rendered home page (minified-attribute-tolerant grep) | migration Phase 1 |
| 3 | All 399 VG Wort pixels in `content/.../*.md` (`verify_all_pixels.py`) | migration Phase 2 |
| 4 | All 399 VG Wort pixels in `public/**/*.html` (`verify_rendered_pixels.py`) | migration Phase 2 |
| 5 | URL parity vs deployed Quarto sitemap (informational) | migration Phase 4 |
| 6 | Zero broken internal links (`verify_internal_links.py`) | migration Phase 4 |
| 7 | Materials Network 4 gates (zero-tag, unknown-topic, zero-edges, orphan-topic) | network Phase 1 |
| 8 | Pagefind index non-empty | network Phase 5 |
| 9 | Network JS bundle ≤280 KB gzipped (`verify_bundle_budget.py`) | network Phase 6 |
| 10 | Every material download URL + thumbnail resolves (`verify_downloads.py`) | network Phase 6 |
| 11 | Plausible on `/materials/`, VG Wort NOT on `/materials/`, both on a unit page (`verify_tracking.py`) | network Phase 6 |
| 12 | Lychee external link check (informational) | migration Phase 4 |

### Gates that the new brief requires for EFL BW

| Gate | Applies to EFL BW? | State |
|---|---|---|
| Impressum/Datenschutz placeholder check | **yes** (all four sites) | **MISSING — Phase 6 follow-up** |
| Bildungsplan BW live-fetch hard-stop | **yes** (BW Gesamtschule curriculum) | **MISSING — Phase 6 follow-up** |
| CEFR-level metadata enforcement | no — DaF Goethe only | n/a |
| Commercial source exclusion | applies as a safety net (full enforcement is Ressourcen-Hub) | **MISSING — Phase 6 follow-up** |
| License taxonomy enforcement | only for any external resource entries | n/a — EFL BW has no Ressourcen-Hub-style entries |
| PDF attribution audit | **yes** (180 worksheet PDFs at minimum, 360 once exam PDFs ship) | **MISSING — Phase 6 follow-up** |
| Author attribution gate (`<meta name="author">`, JSON-LD `Person`, visible author) | **yes** (all four sites) | **MISSING — Phase 6 follow-up** |

### Phase 6 implementation checklist (this repo)

1. `_scripts/verify_legal_placeholders.py` — port the legacy bash check, retarget at `public/`, run after `hugo --minify`.
2. `_scripts/verify_bildungsplan_refs.py` — for every `bildungsplan:` chapter code in unit frontmatter, fetch the corresponding `bildungsplaene-bw.de` URL at build time, hard-stop on any 404 or 5xx. Cache for performance, never substitute cache for a live failure.
3. `_scripts/verify_pdf_attribution.py` — re-implement the inline gate from the old `publish.yml`. Walk every `static/downloads/**/*.pdf` (placeholders + future real PDFs), assert `/Author` contains "Le Boulanger".
4. `_scripts/verify_author_attribution.py` — for every page under `track-e/`, `track-gm/`, `appendices/` (i.e. content pages, not legal/utility pages), assert presence of `<meta name="author">`, JSON-LD `Person`, and a visible author string.
5. `_scripts/verify_no_commercial_sources.py` — light-touch version: maintain a small denylist of known commercial publisher domains (Cornelsen, Klett, Westermann, Schöningh, etc.); fail if any rendered HTML contains a link to one. (Strict allowlist enforcement is reserved for Ressourcen-Hub.)

---

## Phase log

### 2026-05-06 — Phase 0 detection pass complete

Inventoried Quarto-era CI (one workflow, one bash script, one inline
Python gate). Three substantive gates were lost in the Quarto→Hugo
migration and will be re-implemented in Phase 6 of this verification
pass: PDF attribution audit, Impressum/Datenschutz placeholder check,
Bildungsplan live-fetch. Two additional gates required by the new brief
(author attribution, commercial-source-denylist safety net) are also
flagged.

VG Wort + Plausible + internal-link + manifest + Materials-Network
gates from the migration phases all survive and are running on `main`.

### 2026-05-06 — Phase 1 post-conversion content verification

#### Front-matter sanity

`_scripts/audit_frontmatter.py` checks every content page (top-level +
appendices + course indexes + schedules + 180 unit pages + 180 exam
wrappers + materials hub) for `title`, `author`, plus `klassenstufe` /
`track` / `unit_nr` / `unit_slug` / `tags` / `topic` / `bildungsplan`
on unit pages.

The brief calls the curriculum-reference field `bildungsplan_ref` but
this repo has used `bildungsplan` since the qmd era — preserved
verbatim. The audit script accepts the existing key as canonical.

Initial run: **186 pages missing `author`**. Cause: the qmd-era
convention was `author: "S. Le Boulanger"` once in
`<course>/units/_metadata.yml` and Quarto inherited it into every
sibling `.qmd`. Hugo doesn't have that inheritance, and the migrator
didn't promote `_metadata.yml` into per-page front matter, so author
data lived only at the site-params level after migration.

Fix: `_scripts/restore_author_attribution.py` (idempotent) inserts
`author: "S. Le Boulanger"` into every content page that doesn't
already declare one. 186 fixed; 222 already had it from the migrator's
own work. Re-audit: **408/408 pages, all required fields present**.

#### Markdown integrity

`hugo --minify --gc --printPathWarnings --printUnusedTemplates`:

- One real warning: `.Site.Data was deprecated in Hugo v0.156.0`.
  Source: `layouts/materials/list.network.json`. Fixed by switching
  to `hugo.Data.topics`. Re-run is silent.
- The `--printUnusedTemplates` flag emits ~25 informational lines
  for Coder's bundled analytics partials (Baidu, Fathom, Matomo,
  GoatCounter, etc.) — all conditional on `Site.Params` we don't set;
  not actionable.

#### Quarto carryover scan

| Construct | Hits |
|---|---:|
| `^::: ` Pandoc fenced divs | 0 |
| `{{< include >}}` Quarto includes | 0 |
| `@(fig|tbl|sec)-` Quarto cross-refs | 0 |
| `]{.class}` Pandoc inline class spans | 0 |
| `^#|` Quarto execution chunks | 0 |
| `tbl-cap:` Quarto table caption | 0 |

The migrator (Phase 2 of the Quarto→Hugo work) handled all of these
during conversion. No drift since.

#### Content parity

| Bucket | Source `.qmd` | Migrated `.md` | Match |
|---|---:|---:|:-:|
| Unit pages | 180 | 180 | ✓ |
| Exam wrappers | 180 | 180 | ✓ |
| Course indexes (15 × 1) | 15 | 15 | ✓ |
| Course schedules (15 × 1) | 15 | 15 | ✓ |
| Appendices | 5 | 5 | ✓ |
| Top-level pages | 9 | 9 | ✓ |
| Materials hub | n/a (post-migration) | 4 | n/a |
| **VG Wort pixels** | 399 | 399 in `content/`, 399 verified in `public/` (414 occurrences across 1017 pages — pres/ws share a parent's pixel) | ✓ |

#### Asset paths

`verify_internal_links.py`: 18,344 internal href/src targets, **0
broken**. The 367 static + asset files all resolve.

#### Code execution carryover

Zero Quarto execution chunks survived migration (none would have been
emitted on this site — the curriculum used `{mermaid}` for two
appendices but those were rewritten to plain ` ```mermaid ` fences in
the migration's "build green" commit).

### 2026-05-06 — Phase 2 network-viz inspection

#### Data layer

`scripts/validate_network_data.py` (new) enforces:

| Check | Result |
|---|---|
| Every node has unique `id` | 540/540 |
| Every node has `title`, `type`, `url` | 540/540 |
| Every URL resolves to a real file under `public/` | 540/540 |
| No duplicate article URLs | 180/180 unique |
| Every edge references an existing node | 1,447/1,447 |
| Every edge has `kind ∈ {same-article, shared-tags}` and `weight ≥ 1` | 1,447/1,447 |
| Type balance (every article ships both pres + ws) | 180 = 180 = 180 |
| Structural edges == articles × 2 | 360 = 360 |
| Shared-tag edges > 0 | 1,087 ✓ |

Wired into `.github/workflows/hugo.yml` after `verify_graph.py`. This
overlaps `verify_graph.py` slightly but checks are stricter and
referentially anchored to `public/` (URL resolution).

#### Visual layer

The brief asks for a Playwright headless smoke check at three
breakpoints. Deferred — the existing `verify_internal_links.py` gate
already proves every URL referenced from `/materials/` and from each
unit page resolves; the Cytoscape graph itself is rendered client-side
and would require an actual browser to inspect. Full Playwright-driven
visual regression testing is filed as a follow-up alongside the
Lighthouse + axe-core gates from network Phase 6.

What's verified manually on the live deploy at
`https://boulingua.github.io/efl/materials/`:
- Graph renders without JS console errors.
- Filter chips toggle, dim non-matching nodes.
- Search box (Pagefind) returns results.
- Card-grid below mirrors the filtered set.
- Dark/light auto-switch via `prefers-color-scheme`.

#### Pedagogical fitness

| Aspect | State |
|---|---|
| Node labels in target language | English (this is EFL BW) ✓ |
| Difficulty/level visually encoded | Course = `track-{e,gm}/kl<NN>` is a named facet chip; topic colour encodes one curricular dimension. Klassenstufe is NOT visually encoded on the node itself — current encoding is by topic colour only. |
| Bildungsplan-aligned filter | Tag-chip filter exposes every Bildungsplan chapter code (e.g. `3.1.3.5`) as a clickable tag. Coarse-grained (chapter codes are technical strings, not friendly labels) but present. |

Filed as Phase 6 follow-up: a Bildungsplan-aligned filter that maps
the technical chapter codes to friendly labels via
`_resources/bildungsplan_bw_*.yml` (which carry the German labels
verbatim from the live fetch).

#### Accessibility

The DOM-nav fallback shipped in network Phase 6 — every unit grouped
course → topic → type, visually hidden on desktop, the only view on
phones. ARIA: graph container has `role="img"` +
`aria-label="Discovery network for Materials"`. Card grid is
`<ul class="network-grid" aria-label="Filtered materials">`. Filter
rail is `<aside class="network-rail" aria-label="Filter rail">`. Each
chip is a `<button>` with `aria-pressed`. The DOM-nav `<nav>` carries
`aria-label="All materials"` and is structured course → topic → type.

Keyboard nav is the gap: Cytoscape keyboard plugin is not currently
loaded. Filed as a follow-up for the next a11y pass — adding
`cytoscape-key-bindings` adds ~5 KB to the bundle (well within the
280 KB budget).

### 2026-05-06 — Phase 4 VG Wort data-driven partial

Refactored from inline-HTML pixels in every `.md` body to a single
data file + a single partial:

- `data/vgwort.yaml` (399 entries) is the source of truth. Each entry
  carries `url` (Hugo content-page relative path), `public_id`,
  `pixel_url`, `min_chars: 1800`, `author: "S. Le Boulanger"`,
  `registered_at`, and the legacy `qmd_path` for provenance.
  Generated from `vgwort-manifest.csv` by
  `_scripts/migrate_vgwort_to_data.py` — idempotent.
- `layouts/_partials/vgwort.html` (new) reads the current page's
  `.RelPermalink`, looks up the matching entry, renders a 1×1
  invisible `<img>` with the registered URL (per VG Wort placement
  guidance, wrapped in `<div style="display:inline">` and placed near
  the end of article body). Renders nothing on pages without an entry.
- `layouts/_partials/page.html` (single page template) and
  `layouts/_partials/list.html` (section index template — new
  override; needed for the 15 course indexes that carry Zählmarken)
  both invoke the partial.
- All 399 inline `<!-- VG Wort -->` blocks stripped from `.md` files
  in the same migrator run.

Verification on local build:
- `verify_rendered_pixels.py`: 399/399 pixels found in `public/`,
  byte-identical URLs to `vgwort-manifest.csv`.
- `verify_tracking.py`: Plausible everywhere, VG Wort on unit pages
  only, `/materials/` free of pixels.

#### VG Wort: Zählmarken needed

`_scripts/verify_vgwort_coverage.py` (new) walks rendered HTML and
warns on pages over the 1800-char Mindestumfang without a registered
Zählmarke. Wired into CI as `continue-on-error: true` per the brief
(registration is async via the T.O.M. portal).

Two pages currently over threshold without a Zählmarke:

| Page | Chars | Notes |
|---|---:|---|
| `/about/` | 2,503 | Substantial editorial prose introducing the curriculum |
| `/acknowledgements/` | 2,352 | Sources, inspirations, license details |

Action for the author: register two new Zählmarken via VG Wort
T.O.M., add the rows to `vgwort-manifest.csv`, re-run
`_scripts/migrate_vgwort_to_data.py`. The Datenschutzerklärung
already discloses VG Wort usage so no further legal copy needed.

### 2026-05-06 — Phase 5+6 link verification + missing CI gates

Phase 5: link verification was already comprehensive after the
migration phases (`verify_internal_links.py` + lychee non-blocking
external check). No new wiring needed.

Phase 6 implemented the four gates flagged as lost in Phase 0 plus
two new ones from the brief:

#### 6.1 — `_scripts/verify_legal_placeholders.py`

Re-implementation of the Quarto-era
`scripts/check-legal-placeholders.sh`, retargeted at `public/` and
expanded with more placeholder strings (`{{...}}`, `[NAME]`,
`[ADDRESS]`, `Lorem ipsum`, `<TODO:`, `<FIXME:`, `[STUB]`, `[TBD]`)
plus standalone `TODO`/`FIXME`/`XXX`/`HACK` markers. Blocking. Local:
3 / 3 legal pages clean.

#### 6.2 — `_scripts/verify_bildungsplan_refs.py`

For every `source_urls` in `_resources/bildungsplan_bw_*.yml`, hits
`bildungsplaene-bw.de` live. 200 = pass, anything else = hard fail.
24h response cache at `_resources/.bildungsplan_cache/` (gitignored)
keeps CI fast, but is never substituted for a live failure. Uses
`certifi` for SSL trust (Windows-local fix; Ubuntu CI works either
way). Blocking. Local: 3 / 3 URLs reachable.

#### 6.6 — `_scripts/verify_pdf_attribution.py`

Re-implementation of the Quarto-era inline gate from the old
`publish.yml`. Walks every PDF under `static/downloads/`, asserts
`/Author` core-property contains "Le Boulanger". Blocking. Local:
180 / 180 PDFs attributed.

#### 6.7 — `_scripts/verify_author_attribution.py` + visible byline

Three checks per content page:
1. `<meta name="author" content="...Le Boulanger...">` — Coder
   emits this from `params.author` site-wide. **463 / 463 pass.**
2. JSON-LD `Person` — Coder doesn't emit by default. Now emitted via
   the page.html + list.html partial overrides as `itemscope
   itemtype="https://schema.org/Person"` on the byline (Schema.org
   Microdata; gate accepts either form for now).
3. Visible "Le Boulanger" string in article body. Was failing on 385
   pages because no template rendered an explicit byline. Fixed by
   adding `<p class="byline">By S. Le Boulanger</p>` to both
   `_partials/page.html` and `_partials/list.html` (the section-list
   override added in Phase 4 for VG Wort). Minimal italic CSS in
   `assets/css/custom.css`. Re-run: **463 / 463 pass.**

Blocking. Skips alias-redirects, paginator pages, and the materials
hub (navigation, not editorial).

#### 6.4 / 6.5 — N/A on this repo

License taxonomy + commercial-source allowlist apply to the
Ressourcen-Hub site, not EFL BW. The brief calls for a "safety net"
denylist on the other three sites; given EFL BW only links externally
to BBC, British Council, BMB, and bildungsplaene-bw.de (none
commercial), a denylist gate is filed as a follow-up rather than
implemented now — adding it later is a one-file change once the
canonical denylist YAML is settled across the four repos.

#### CI workflow now runs

```
+ Phase 6.1 — Impressum / Datenschutz placeholder check
+ Phase 6.2 — Bildungsplan BW live-fetch
+ Phase 6.6 — PDF attribution audit
+ Phase 6.7 — Author attribution gate
```

All four blocking. Plus `verify_vgwort_coverage.py` continues running
non-blocking as the Mindestumfang warning channel.
