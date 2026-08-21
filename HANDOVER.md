# EFL — Handover: conformance audit & roadmap

> **Scope.** This document audits the `boulingua/efl` repository against two authorities and lays out the work to bring it into conformance:
> 1. **pagegen** (`boulingua/pagegen`) — the canonical course *template*: repo layout, config, content model, design system, gates, VG Wort standard.
> 2. **curriculum** (`boulingua/curriculum`) — the CEFR *framework*: descriptor-ID scheme (`{LEVEL}.{DOMAIN}.{SCALE}.{SEQ}`), conformance levels, and the machine-readable scope manifest a consumer must publish.
>
> Reviewer notes are marked ⟨decision⟩. File paths are repo-relative to `efl/` unless prefixed.

---

## 1. Executive summary

EFL is the **most mature and closest-to-template** of the boulingua courses. It is a fully built Hugo + hugo-coder site with page-bundle content (~180 units + **181 first-class exam bundles**, 411 `.md` files total), a working shortcode set, a rich generation/verification script suite in `_scripts/`, filled legal pages, and — crucially — it **already runs the target VG Wort model**: `data/vgwort.yaml` (≈402 registered marks) resolved through the shared `layouts/_partials/vgwort/url.html` partial. VG Wort is EFL's single strongest dimension and needs only cleanup, not migration.

Against the two targets, EFL is roughly **75% template-conformant** and **~10% curriculum-conformant**. The structural gaps are mechanical (renames, config normalisation, script consolidation); the curriculum gap is substantive (a whole ID-mapping layer does not yet exist).

**The 5 biggest gaps (highest leverage first):**

1. **Front-matter schema divergence.** EFL uses the *old* flat fork (`niveau`/`klassenstufe`/`track` + a `bildungsplan:` code list) with **no `page_type` discriminator** (0 pages) and **no polymorphic `curriculum:` block** (0 pages). pagegen's superset schema requires both. `skills_focus` also uses a non-standard enum (`speaking`, `language_awareness`) vs the standard split (`speaking_interaction`/`speaking_production`).
2. **No curriculum descriptor IDs at all.** EFL references Bildungsplan-BW codes (`3.1.3.3`) but **zero** curriculum IDs of the form `{LEVEL}.{DOMAIN}.{SCALE}.{SEQ}`. It publishes **no `conformance.yml`** and cannot yet declare any conformance level or pass a consumer-side ID resolution check.
3. **Materials pipeline is CI-generated, not committed.** `build_materials_latex.py` runs **inside** `hugo.yml` with a full **TeX Live install** in the deploy path; `static/materials/{presentations,worksheets}` are git-ignored. pagegen mandates *locally generated + committed*, CI *verifies only*.
4. **Config + design-system drift.** `hugo.toml` carries a ~40-entry inline `[[menu.main]]`, **no `[taxonomies]`**, and **no `params.code`**; `data/accents.yaml` is **absent** (accent hard-coded rather than data-driven). Shortcodes live under the legacy `layouts/shortcodes/` rather than `layouts/_shortcodes/`.
5. **Script + gate sprawl.** Logic is split across `_scripts/` (~40 files: generators *and* verifiers) and `scripts/` (2 files); `hugo.yml` is a 7.4 KB bespoke pipeline vs pagegen's lean `build-deploy.yml`. Verifier names largely match pagegen's `scripts/` but live in the wrong directory and are wired to a different workflow.

**Effort estimate.** ~3–4 focused engineering days for full template conformance (Phases 1–4), the bulk being the front-matter migration (scriptable across 361 bundles) and the materials-commit switch. Curriculum conformance (Phase 5) is a **separate, content-heavy effort** — realistically 1–2 weeks of authoring/mapping to credibly declare `core`, because it requires mapping every unit's can-dos to real CV descriptor IDs, not a mechanical transform.

---

## 2. Audit — template (pagegen) conformance

| Dimension | CURRENT in efl | TARGET in pagegen | GAP |
|---|---|---|---|
| **Repo layout** | `content/ layouts/ data/ scripts/ _scripts/ _materials/ _resources/ archetypes/ static/ assets/ i18n/`; extra `recovery/`, `MATERIALS_NETWORK_PLAN.md`, `vgwort-manifest.csv` | `content/ layouts/ data/ scripts/ archetypes/ docs/ _materials/ …`; single `scripts/`, `docs/` present | Split `_scripts/`+`scripts/`; no `docs/`; stray `recovery/`, legacy `vgwort-manifest.csv`; `archetypes/` is **empty** (pagegen ships 5 archetypes) |
| **`hugo.toml`** | inline ~40-entry `[[menu.main]]`; **no `[taxonomies]`**; **no `params.code`/`navTitle`/`license`**; custom `[outputFormats.network]`; Plausible block present (correctly last) | templated header; declared `[taxonomies]` (tag/skill/level/topic); `params.code` selects accent; compact section-mirroring menu; Plausible last | Add `[taxonomies]`, `params.code="efl"`, `navTitle`, `license`; collapse the menu; decide fate of `network` output format (EFL extension, not in template) |
| **`go.mod`** | `module github.com/boulingua/efl`, go 1.26.1, hugo-coder pinned identically | same pin | **Conformant.** No action |
| **Content model** | page bundles `content/track-{e,gm}/kl{05–13}/units/<unitNN-slug>/index.md`; exams as **first-class sibling bundles** `<unitNN-slug>-exam/index.md` (181); `_index.md` section landings; appendices bundles | identical shape; flat course key (`e-kl05`) suggested but nesting acceptable | **Structurally conformant** — this is why EFL is closest. Only the *front-matter inside* the bundles diverges (next row) |
| **Front-matter schema** | flat `niveau`/`klassenstufe`/`track`/`unit_slug`/`bildungsplan:[…]`; `skills_focus` non-standard enum; `tags` duplicate BW codes; **no `page_type`** (0); **no `curriculum:` block** (0); exams lack `duration_min`/`total_points`/`notenschluessel` fields (data is in prose) | `page_type` discriminator on every page; polymorphic `curriculum: {framework: bildungsplan-bw, niveau, klassenstufe, track, codes}`; standard `skills_focus` enum; `materials_status`; exam-only structured fields | **Largest structural gap.** Migrate all 361 unit+exam bundles: add `page_type`, wrap Bildungsplan fields in `curriculum:`, normalise `skills_focus`, lift exam metadata out of prose |
| **Layouts / partials** | `header.html`, `page.html`, `list.html`, `about/courses/list.html`, `materials/list.html`+`.network.json`, `audio-block.html`, `material-links.html`, `head/{extensions,custom-icons}.html`, `body/extensions.html`; **legacy `vgwort.html`** + `vgwort/url.html` | `home.html`, `header.html`, `footer.html`, `page.html`, `material-links.html`, `head/extensions.html`, `body/extensions.html`, `vgwort/url.html` + **`vgwort/pixel.html`** | Missing `footer.html`, `home.html`; has legacy `vgwort.html` where template uses `vgwort/pixel.html`; EFL carries extra layouts for its Materials-Network extension (keep, but document as EFL-specific) |
| **Design system** | accent hard-coded; **no `data/accents.yaml`**; `brand/icon.{svg,png}` present but no `make_icon.py` | accent driven by `data/accents.yaml` keyed on `params.code`; `brand/make_icon.py` regenerates pentagon + favicons | Add `data/accents.yaml` (EFL green `#248D19` already defined in the template's copy) + `params.code`; port `brand/make_icon.py` |
| **Shortcodes** | `layouts/shortcodes/` (**legacy path**): callout, card, card-grid, downloads, hero, kicker, lead | `layouts/_shortcodes/` (Hugo ≥0.146): same set **plus `details.html`** | Move dir to `_shortcodes/`; add `details.html`; confirm parity with template versions |
| **Scripts & CI gates** | `_scripts/` (~40: generators `_emit_*`, `_scaffold_*` + verifiers `verify_*`) + `scripts/` (2); `hugo.yml` 7.4 KB, installs TeX Live, **generates materials in CI**, runs ~20 steps, Pagefind, network gates | one `scripts/` (verifiers + build helpers); `build-deploy.yml` lean: `hugo --minify --gc` then gate battery, **no TeX Live** | Consolidate verifiers into `scripts/`; keep generators in `_scripts/` (author-only) or `_scripts/generate/`; strip material generation + TeX Live from the deploy workflow |
| **Materials & audio** | `build_materials_latex.py` + `build_audio.py` run in CI; `static/materials/{presentations,worksheets}` **git-ignored**; `data/audio/` present; `_materials/` has LaTeX styles + fonts | generate **locally**, **commit** PDFs/audio under `static/materials`+`static/downloads`; CI only `verify_downloads.py` | Flip the model: generate + commit artefacts; remove TeX Live from CI; keep `_materials/` templates |
| **VG Wort** | `data/vgwort.yaml` (~402 marks) + shared `vgwort/url.html` resolver + `<head>` preload + eager body pixel; legacy `vgwort-manifest.csv` still tracked | identical resolver + `data/vgwort.yaml` model | **Already the target model.** Only cleanup: retire `vgwort-manifest.csv`, rename `vgwort.html`→`vgwort/pixel.html`, keep the usage registry out-of-repo |
| **Legal / compliance** | `impressum`/`datenschutz`/`haftungsausschluss` **filled** (real § 5 DDG data, no placeholders); `LEGAL.md`, `LICENSE`, `LICENSE-CODE.md`, `CITATION.cff` | same three pages with ⟨…⟩ placeholders for a course to fill; MIT + CC BY-SA 4.0 | **Ahead of template** (already filled). Confirm `verify_legal_placeholders.py` passes with zero remaining ⟨…⟩; align licence files with template naming (`LICENSE-CONTENT.md`) |

**Net:** every *structural* divergence is mechanical. The content model (page bundles + first-class exams) is already correct; the work is normalising what lives *inside* the bundles and *around* them (config, scripts, materials).

---

## 3. Audit — curriculum (CEFR framework) conformance

**Does EFL reference curriculum descriptor IDs?** **No.** A repo-wide grep for `{LEVEL}.{DOMAIN}.{SCALE}.{SEQ}` (`preA1|A1|…|C2 . REC|PROD|INT|MED|PLUR|LING|SOC|PRAG . slug . NN`) returns **0** matches. EFL references **Bildungsplan-BW** codes (`3.1.3.3`, `3.1.1`) in a `bildungsplan:` list and mirrors them into `tags:`. These are a *different, orthogonal* identifier system (Baden-Württemberg competence areas), not the boulingua CEFR IDs the curriculum repo mints.

**Can it declare a conformance level today?** **No.** Per `curriculum/docs/conformance.md`, a consumer must *publish, machine-readably, the set of scales it implements and, per scale, the levels covered vs `no-official-descriptor`.* EFL publishes no such manifest and mints no IDs, so it cannot credibly claim `core`, `full`, or `complete`.

**What level is realistically attainable?** EFL spans Klasse 5–13, i.e. roughly **CEFR A1 → B2/C1** (Abitur ≈ B2–C1). That footprint could support a **`core` (A1–B1)** declaration with documented gaps and a partial reach into `full`. But `curriculum/docs/conformance.md` is explicit that *a silently missing in-scope scale is a conformance failure* while a declared gap is not — so `core` is only honest once **every in-scope scale carrying an A1/A2/B1 descriptor** is either implemented or recorded as a declared gap. Given EFL's thin mediation/plurilingual coverage (a handful of `mediation` units), expect to **declare gaps** in `MED`/`PLUR` initially. ⟨decision⟩ Target **`core`, partial**, mirroring `curriculum/examples/de-a1/conformance.yml`'s `declared_conformance: partial` posture, and grow toward full `core` scale coverage.

**Machine-readable manifest to publish.** A top-level `conformance.yml` following `curriculum/examples/de-a1/conformance.yml`:
```yaml
framework: boulingua-curriculum
framework_version: 1.0.0
language: en
level: A1            # highest floor claimed; or a range note
declared_conformance: partial
realizations:
  - implements_id: A1.INT.conversation.01
    en: "I can introduce myself and ask simple personal questions."
    where: /track-e/kl05/units/unit01-hello-world/
  - …
```
Each `implements_id` **must resolve** to a statement in `curriculum/levels/*.md`. The framework's level-file audit script validates the *framework's own* level files (format, uniqueness, registry resolution) — it takes no manifest argument and globs `levels/*.md` under its own repo root, so it can **never** ingest a consumer's `conformance.yml`. Pointed at `efl/` it audits the framework's 1170 statements and exits 0 whatever EFL contains. So EFL needs a **consumer-side resolver check** (see Phase 5, Task 5.4) that loads `conformance.yml`, loads the framework's minted IDs, and fails if any `implements_id` is unknown — the same guarantee `examples/de-a1` relies on.

**Which gate proves the claim?** The reusable workflow `boulingua/.github/.github/workflows/course-build.yml@v1` runs
`python .curriculum/scripts/conformance_audit.py resolve --manifest conformance.yml --content content`.
The framework's own level-file audit script cannot validate this repo — it audits the framework's level files and nothing else, so wiring it here would produce a green gate that has read none of EFL. Do not wire it here; Task 5.4 authors the consumer side of the same check.

**Mapping task (the substantive work).** For each unit, translate its learning-objective can-dos ("*I can introduce myself…*") into curriculum IDs by looking up the matching `(DOMAIN, scale, level)` in `curriculum/levels/`. This is authoring, not a transform: the CV descriptor for a given (scale, level) must actually cover the unit's claim. Bildungsplan codes and CEFR IDs will coexist in the polymorphic `curriculum:` block (`framework: bildungsplan-bw` keeps BW `codes:`; an added `implements:` list carries the CEFR IDs), so no data is lost.

---

## 4. Task roadmap

Effort tags: **S** ≤2 h · **M** ≤1 day · **L** multi-day. Phases are dependency-ordered; within a phase, tasks are value-ordered.

### Phase 1 — Quick structural wins (config + layout hygiene)
- **1.1 (S)** Add `[taxonomies]` (tag/skill/level/topic) and `params.code = "efl"`, `params.navTitle`, `params.license = "CC BY-SA 4.0"` to `hugo.toml`. *AC:* `hugo` builds clean; taxonomy pages render.
- **1.2 (S)** Add `data/accents.yaml` (EFL entry already defined in the template) and confirm `assets/css/custom.css` selects the accent by `params.code`. *AC:* green accent resolves from data, not hard-coded.
- **1.3 (S)** Move `layouts/shortcodes/` → `layouts/_shortcodes/`; add `details.html`; diff each shortcode against the pagegen version. *AC:* all shortcodes resolve; `callout`/`downloads` unchanged in output.
- **1.4 (S)** Collapse the ~40-entry inline `[[menu.main]]` into the compact section-mirroring shape (Track G+M / Track E / Materials / About / Legal groups with `parent`/`weight`). *AC:* navbar renders the same top-level entries; grade pages still reachable.
- **1.5 (S)** Add `layouts/_partials/footer.html` and `layouts/home.html` from the template; port `brand/make_icon.py`. *AC:* footer renders; `python brand/make_icon.py` regenerates `brand/icon.*`.
- **1.6 (S)** Populate `archetypes/` from pagegen (`unit.md`, `exam.md`, `section.md`, `appendix.md`, `default.md`). *AC:* `hugo new … --kind exam` scaffolds a conformant bundle.

### Phase 2 — Front-matter schema migration (the core structural gap)
- **2.1 (M)** Write `_scripts/migrate_frontmatter.py`: for every `content/**/units/**/index.md`, add `page_type` (`unit` vs `exam` by dir suffix), move `niveau`/`klassenstufe`/`track`/`bildungsplan` under a `curriculum: {framework: bildungsplan-bw, …, codes: […]}` block, and add `materials_status`. *AC:* idempotent; a dry-run diff on 10 sample bundles reviewed before bulk apply.
- **2.2 (S)** Normalise `skills_focus` enum: `speaking` → `speaking_interaction`/`speaking_production` (choose per unit intent), keep `listening`/`reading`/`writing`/`mediation`/`intercultural`/`language_awareness`. *AC:* every value is in the standard enum; a gate (`verify_frontmatter.py`) enforces it.
- **2.3 (M)** Lift exam metadata (`duration_min`, `total_points`, `notenschluessel`) out of prose into front matter for all 181 exams; keep the rendered Notenschlüssel table. *AC:* structured fields present; `page.html`/exam layout can render them.
- **2.4 (S)** De-duplicate BW codes out of `tags:` (they belong in `curriculum.codes`); regenerate discovery tags from structured fields via the existing `populate_network_frontmatter.py`. *AC:* `tags` carry topical/skill tags only.

### Phase 3 — Scripts, gates & CI consolidation
- **3.1 (M)** Split `_scripts/` into `_scripts/generate/` (author-only: `_emit_*`, `_scaffold_*`, `make_materials.py`, `build_*`) and move all `verify_*` gates into `scripts/`. *AC:* `scripts/` holds only verifiers + build helpers, matching pagegen's directory.
- **3.2 (M)** Rewrite `.github/workflows/hugo.yml` toward pagegen's `build-deploy.yml`: `hugo --minify --gc` then the gate battery; **remove TeX Live install and material generation** from the deploy path (depends on Phase 4). *AC:* CI green with no `apt-get texlive`; deploy only from `main`.
- **3.3 (S)** Reconcile the duplicated "Populate Materials Network frontmatter" step (currently listed twice in `hugo.yml`) and the `continue-on-error` gates; document which stay warnings (VG Wort coverage, URL parity, lychee). *AC:* no duplicate steps; each gate's blocking/non-blocking status is intentional and commented.

### Phase 4 — Materials & audio: switch to commit-and-verify
- **4.1 (M)** Run `_scripts/generate/build_materials_latex.py` + `build_audio.py` **locally**; commit outputs under `static/materials/{presentations,worksheets,audio}` and `static/downloads/`. *AC:* artefacts tracked in git; `.gitignore` no longer excludes them.
- **4.2 (S)** Update `.gitignore` to stop ignoring committed material dirs (keep `_materials/build/` and LaTeX aux ignored). *AC:* `git status` clean after a local rebuild.
- **4.3 (S)** Keep only `verify_downloads.py` + `verify_pdf_attribution.py` in CI for materials. *AC:* every `presentation.file`/`worksheet.file`/`exam.file` URL resolves to a committed asset.

### Phase 5 — Curriculum conformance (descriptor-ID mapping) — separate effort
- **5.1 (L)** Author `conformance.yml` at repo root: declare `framework_version`, `declared_conformance: partial`, and a `realizations:` list mapping unit can-dos → curriculum IDs (start with Track E kl05–kl08 ≈ A1–A2). *AC:* file validates against the consumer resolver (5.4).
- **5.2 (L)** Extend the `curriculum:` block per unit with an `implements: ["A1.INT.conversation.01", …]` list alongside the BW `codes:`. *AC:* every A1/A2/B1 unit carries ≥1 resolvable ID.
- **5.3 (M)** Produce a **coverage manifest** (`docs/curriculum-coverage.yml`): per in-scope scale, the levels covered vs `no-official-descriptor` vs *declared gap*, per `curriculum/docs/conformance.md`. *AC:* no in-scope scale is silently missing; gaps are explicit.
- **5.4 (M)** Add `scripts/verify_curriculum_conformance.py`: load `conformance.yml` + unit `implements:` IDs, load the framework's minted IDs (from a pinned `curriculum` checkout), fail on any unresolved ID or malformed format. Wire as a **blocking** CI gate. *AC:* passes; breaks the build on a bogus ID (mirrors `curriculum/examples/de-a1`'s guarantee).
- **5.5 (S)** Document the declared conformance level + known gaps (MED/PLUR/C2) in `README.md`, echoing `conformance.md`'s "declare the gap, don't hide it" stance. *AC:* level and gaps stated honestly.

### Phase 6 — Cleanup & parity
- **6.1 (S)** Retire legacy `vgwort-manifest.csv` (superseded by `data/vgwort.yaml`); remove `recovery/` and one-shot `MATERIALS_NETWORK_PLAN.md` or move to `docs/`. *AC:* no dead tracked files.
- **6.2 (S)** Rename `layouts/_partials/vgwort.html` → `layouts/_partials/vgwort/pixel.html` to match the template; update the `body/extensions.html` reference. *AC:* body pixel still renders; render gate green.
- **6.3 (S)** Add `docs/` mirroring pagegen (`front-matter-fields.md`, `vgwort-standard.md`) so EFL is self-documenting. *AC:* docs present and EFL-accurate.

---

## 5. VG Wort — pixel assignment for ALL new content pages (non-skippable)

**This is a first-class, blocking roadmap item.** EFL already runs the target VG Wort model (`data/vgwort.yaml` + `vgwort/url.html` resolver + `<head>` preload + eager body `<img>`), with **≈402 marks already registered** covering essentially every unit and exam bundle plus appendices. That head-start does **not** exempt any *new* page the roadmap introduces — every qualifying new page must get its own Zählmarke before it can be considered done, per `pagegen/docs/vgwort-standard.md`.

**How many new content pages does the roadmap create?** The Phase 1–4 work is overwhelmingly a *transform of existing pages* (bundle dir names — and therefore URLs — are preserved), so it mints **few new URLs**. The genuinely new/newly-qualifying pages are:

1. **Phase 5 curriculum pages** — any new CEFR-level landing page, mediation/plurilingual **units authored to close declared `core` gaps** (5.1–5.3). Each new unit ≥1800 rendered characters is a new *Sprachwerk* and **must** carry a mark. Estimate: however many gap-filling units are written (expect a handful to a few dozen as `MED`/`PLUR` coverage grows).
2. **Any restructured page that changes URL** — if a bundle is re-slugged during migration, its old mark is keyed to the old `url:` and will silently stop resolving. Treat a URL change as a *new page*: re-key the entry (or move to `path:`-keyed matching) so the mark follows the content.
3. **New editorial prose pages** — e.g. an expanded course-overview or a curriculum-mapping narrative ≥1800 chars.

**Mandatory procedure for every such page** (follow `pagegen/docs/vgwort-standard.md` §3–§9 exactly):

1. **Qualify.** Only original creative prose **≥1800 rendered characters** (VG Wort *Mindestumfang*) gets a mark. **Never** mark navigation surfaces (section `_index.md` landings, `/materials/`, tag indexes, paginated `/page/2/`) or the **templated legal pages** (Impressum/Datenschutz/Haftungsausschluss). Short exams below 1800 chars are excluded.
2. **Draw a fresh public code** ("Öffentlicher Identifikationscode", 32-hex) from the author's VG Wort **T.O.M.** account. **Never invent codes; never reuse an assigned code; never expose the private code.**
3. **Register in `data/vgwort.yaml`**, keyed by `url:` (base-stripped `RelPermalink`) **or** `path:` (`content/<File.Path>`), with `pixel_url` + `public_id` + `min_chars: 1800` + `author` + `registered_at`. (Alternatively per-page `vgwort_pixel:` front matter — but `data/vgwort.yaml` is the house style.)
4. **Render via the shared resolver only** — `layouts/_partials/vgwort/url.html` feeds both the `<head>` preload and the body pixel; do not add markup anywhere else.
5. **Record in the usage registry** (§8) — the private `Used/Projekt/Sprache/Niveau/Kurstitel/URL/Pixel_URL` ledger — kept **outside** the repo (author's local VG Wort working dir), never under `content/` or `static/`.
6. **Verify via the gates:** the **coverage audit** (`verify_vgwort_coverage.py`, warning) must show **0** unregistered editorial pages ≥1800 chars; the **render verify** (`verify_rendered_pixels.py`, blocking) must confirm each `pixel_url` appears on exactly its one page; the **hub guard** must confirm `met.vgwort.de` is **absent** from `/materials/`.

**Acceptance criterion for Phases 4–5:** the coverage audit reports zero unregistered ≥1800-char editorial pages (legal pages excepted), the render-verify gate is green, and every new page's code is recorded in the out-of-repo registry. A roadmap task that adds an editorial page is **not complete** until its Zählmarke is drawn, registered, rendered, and verified.

---

## 6. Risks & open decisions

- **⟨Exam migrate-vs-keep⟩** EFL's 181 exams are already first-class sibling bundles — the template's target shape — so unlike the sister repos there is **no migrate-vs-delete question**; the risk is narrower: the front-matter migration (2.1–2.3) must **preserve exam URLs and their existing VG Wort marks**. Any re-slug silently orphans a mark (§5 pt 2). *Mitigation:* freeze bundle dir names during migration; add a gate asserting every `data/vgwort.yaml` `url:` still resolves to a built page.
- **⟨Materials: CI-generated vs committed⟩** Flipping to committed artefacts (Phase 4) removes TeX Live from CI but makes the **author's local toolchain** (XeLaTeX + `_materials/` styles + Piper voices) the source of truth. *Risk:* artefacts drift from unit content if regeneration is skipped. *Decision needed:* keep a **non-deploy** "materials-freshness" check (regenerate in a scratch job, diff hashes, warn) vs trust discipline. Recommend the warn-only freshness job.
- **⟨Conformance level to declare⟩** `core` (A1–B1) is the honest ceiling for the near term, and only as **`partial`** until every in-scope A1/A2/B1 scale is implemented or explicitly gap-declared. *Risk:* over-claiming `full`/`complete` violates `conformance.md`'s "silently missing scale is a failure" rule. *Decision:* declare `core, partial`; enumerate MED/PLUR/C2 gaps openly (5.5).
- **⟨Dual identifier systems⟩** Bildungsplan-BW codes and curriculum CEFR IDs will coexist in the `curriculum:` block. *Risk:* authors conflate them or map loosely (a unit claiming a descriptor the CV text does not actually support). *Mitigation:* 5.4's resolver gate catches *unresolvable* IDs but **cannot** catch a *wrong-but-valid* mapping — those need human review against `curriculum/levels/`.
- **⟨Materials-Network extension⟩** EFL's `[outputFormats.network]`, `materials/list.network.json`, Cytoscape bundle, and `verify_graph.py`/`verify_bundle_budget.py` are **EFL-specific features not in pagegen**. *Decision:* keep them as a documented EFL extension (don't force-strip to match the template), but isolate them so they don't block the core gate battery.
- **⟨Framework version pinning⟩** 5.4 resolves IDs against `curriculum` — which is a separate repo at `framework_version: 1.0.0`. *Risk:* framework updates renumber nothing (IDs are immutable per `id-scheme.md`) but *add* scales; EFL must pin the version it validated against. *Mitigation:* record `framework_version` in `conformance.yml` and pin the `curriculum` checkout SHA in CI.
- **⟨Legal licence-file naming⟩** EFL ships `LICENSE-CODE.md`; the template uses `LICENSE-CONTENT.md` for the CC BY-SA content licence. Confirm both code (MIT) and content (CC BY-SA 4.0) licences are present under the template's names to keep `verify_pdf_attribution.py`/attribution gates aligned.
