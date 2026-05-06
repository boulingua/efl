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
