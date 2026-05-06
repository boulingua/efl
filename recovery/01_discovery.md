# Phase 1 Discovery — Track G+M and Track E

**Read-only inventory.** No files modified outside this report. Stop and
confirm before Phase 2.

---

## TL;DR

**The premise of the prompt is not supported by the current repo state.**
Both tracks are fully present, frontmatter-rich, prose-rich, materials
wired, VG Wort coverage at 100%. No content was lost in the
Quarto → Hugo migration; the migration delivered all 180 unit pages and
180 exam wrappers exactly as planned (180 = 12 units × 15 courses).

If you are seeing something that looks "missing" on the deployed site,
it is more likely a rendering/styling bug or a navigation discoverability
problem than a content gap. **Recommend:** name the specific
(track, Klasse, unit) you expected to find before Phase 2 runs — if
that tuple is in the table below, no recovery is needed; if it isn't,
that's the precise gap to chase.

---

## 1.1 Repo identity

| Field | Value |
|---|---|
| `git remote.origin.url` | `https://github.com/boulingua/efl.git` |
| Hugo `title` | `EFL` |
| Hugo `baseURL` | `https://boulingua.github.io/efl/` |
| `languageCode` | `en` |
| `_quarto.yml` | absent (migration phase 4 removed it cleanly) |
| Repo identity | **EFL BW** — English, Gesamtschule Baden-Württemberg, two-track curriculum |

## 1.2 Current Hugo content tree

### Track presence

```
content/track-gm/{kl05, kl06, kl07, kl08, kl09, kl10}              ← 6 Klassenstufen
content/track-e/ {kl05, kl06, kl07, kl08, kl09, kl10, kl11, kl12, kl13}  ← 9 Klassenstufen
```

### Per-Klasse unit + exam counts

| Klasse | Track G+M (units / exams) | Track E (units / exams) |
|---|---:|---:|
| 5 | 12 / 12 | 12 / 12 |
| 6 | 12 / 12 | 12 / 12 |
| 7 | 12 / 12 | 12 / 12 |
| 8 | 12 / 12 | 12 / 12 |
| 9 | 12 / 12 | 12 / 12 |
| 10 | 12 / 12 | 12 / 12 |
| 11 | — | 12 / 12 |
| 12 | — | 12 / 12 |
| 13 | — | 12 / 12 |
| **Total** | **72 / 72** | **108 / 108** |

**Aggregate: 180 unit pages + 180 exam wrappers = 360 content pages.**
Matches the original migration inventory exactly.

### Page substance

| Metric | Value |
|---|---:|
| Pages flagged `draft: true` | 0 |
| Pages under 200 bytes (potential stubs) | 0 |
| Smallest unit page | 5,940 B (`track-gm/kl05/unit08-hobbies-and-sports`) |
| Median unit page | ~7,440 B |
| Largest unit page | 15,571 B (`track-gm/kl07/unit02-growing-up`) |
| **Aggregate prose volume across 180 unit pages** | **227,085 words** |

### Structural sections

| Heading | Coverage |
|---|---:|
| `## Learning objectives` | 180 / 180 |
| `## Exam example` | 180 / 180 |
| `## Common pitfalls` | 180 / 180 |
| `## Activate / Input / Practise / Produce / Reflect` (5-step template) | 0 / 180 |

The 5-step template appears in `HANDOVER.md` as the design pattern,
but the actual page bodies use the curriculum-aligned section names
(Learning objectives → unit body → Exam example → Common pitfalls →
Further reading) rather than the abstract Activate→Reflect labels.
This is **author intent**, not a migration gap; do not rewrite.

### Frontmatter completeness (sample: `track-gm/kl07/units/unit01-first-day-back/index.md`)

```yaml
title: "Unit 1 — First Day Back"
author: "S. Le Boulanger"
subtitle: "Track G+M · Klasse 7 · Niveau G/M"
niveau: "G+M"
klassenstufe: 7
track: "gm"
unit_nr: 1
unit_slug: "first-day-back"
bildungsplan:
  - "3.2.1 Soziokulturelles Orientierungswissen / Themen"
  - "3.2.3.1 Hör-/Hörsehverstehen"
  - "3.2.3.3 Sprechen – an Gesprächen teilnehmen"
  - "3.2.3.5 Schreiben"
  - "3.2.4 Text- und Medienkompetenz"
skills_focus: [speaking, listening, writing, language_awareness]
aliases:
  - /track_gm_kl07/units/unit01_first-day-back.html
presentation: { file: ..., thumbnail: ... }
worksheet:    { file: ..., thumbnail: ... }
tags:  [...]
topic: ...
```

Every required field present on every page (verified separately in
post-migration verification Phase 1, see `MIGRATION_NOTES.md` § Phase 1).

### Materials wired

180 / 180 unit pages carry `presentation:` + `worksheet:` frontmatter
pointing to flat-named binaries under
`static/materials/{presentations,worksheets}/track-{e,gm}_kl<NN>_unit<NN>-<slug>.{pptx,pdf,png}`.

### VG Wort coverage

`data/vgwort.yaml` contains **360 entries** covering every unit page
**and** its exam wrapper — every editorial page registered.

## 1.3 Pre-Hugo content — historical sources

### Branches

```
* main
  migration/hugo-coder        ← migration branch, kept for record
  remotes/origin/main
  remotes/origin/migration/hugo-coder
```

No `quarto`, `pre-hugo`, `legacy`, `backup`, `main-old`, or
`migration-*` branches besides the one above.

### Quarto-source touch-points in history

The single commit that operated on the entire `.qmd` corpus is
`8d75f0a chore(migration): remove quarto setup — hugo is the build
(Phase 4)` — the clean-removal commit at the end of the
Quarto → Hugo migration. Before that, the migration's Phase 2 commits
(`ffe7d4a` … `04472b9`) wrote the converted `.md` while the `.qmd`
sources still co-existed. **No partial migration; the conversion was
complete before the .qmd were removed.**

### Working-tree leftovers

- No `_archive*`, `backup*`, `_legacy*`, `.trash*`, `_site`,
  `public_old`, `_book`, `old*` folders.
- No residual `.qmd`, `.Rmd`, `.ipynb` files on disk.
- `git stash list` empty.
- `git reflog` shows only this session's commits — no orphaned commits
  with lost content.

### `.gitignore` / `.git/info/exclude` review

Standard ignores for build artefacts (`/public/`, `/resources/`,
`/static/downloads/`, `/static/materials/{presentations,worksheets}/`).
None of these would hide content sources.

## 1.4 External hints in current files

`grep -rIn -E "(track[ -]?(g\\+m|e)|spur|niveau|gymnasium|hauptschule|
realschule|werkreal)" content/ hugo.toml layouts/` returns the expected
references (track-e / track-gm / niveau-e / niveau-g+m mentions in
frontmatter and listing pages) — no TODO / stub markers, no broken
links flagged.

## 1.5 Build artefacts and PDFs

| Path | Count | State |
|---|---:|---|
| `static/materials/presentations/*.pptx` | 180 | placeholder + real-render thumbnail |
| `static/materials/presentations/*.png` | 180 | thumbnail |
| `static/materials/worksheets/*.pdf` | 180 | placeholder + author metadata |
| `static/materials/worksheets/*.png` | 180 | thumbnail |

All four sets cover both tracks (filenames carry track + Klasse + unit
provenance: `track-{e,gm}_kl<NN>_unit<NN>-<slug>`).

## 1.6 Source candidate table (per the prompt's required schema)

| Location | Track | Klassen covered | File types | Approx. unit count | Notes |
|---|---|---|---|---:|---|
| `content/track-gm/kl05` … `kl10/units/*/index.md` (current `main`) | G+M | 5–10 | `.md` page bundles | 72 unit pages + 72 exam wrappers | **Live, complete, in production.** |
| `content/track-e/kl05` … `kl13/units/*/index.md` (current `main`) | E | 5–13 | `.md` page bundles | 108 unit pages + 108 exam wrappers | **Live, complete, in production.** |
| `migration/hugo-coder` branch | both | as above | identical to `main` | identical | Migration record; no exclusive content. |
| Pre-removal `.qmd` (commit `04e088d` and earlier) | both | as above | `.qmd` | 180 unit articles + 180 exam wrappers + 180 exam-body partials | All 180 articles converted to `.md` in migration Phase 2 with **0 % word-count drift** (per `MIGRATION_PLAN.md`). |

### Units in current Hugo tree vs. units missing or stubs

**Missing or stub units: 0.** Every (track, Klasse, unit_nr) tuple in
the canonical 180-unit roster (`_resources/curriculum_outline.yml`)
has a corresponding live page bundle.

---

## 1.7 Recommendation — STOP before Phase 2

The prompt's premise — "content for Track G+M and Track E appears to
have been lost or only partially carried over" — is not corroborated
by the repo state. **Recovery is not needed.**

Three possibilities for what may have prompted the request:

1. **Rendering / styling bug on the live site.** The previous user
   message ("network appears as a single line", "tiles need to align
   with dark and light mode", "sheets need to be centered") flags
   visual issues that have just been fixed in `23820be`. The content
   was always there — it was the listing page's CSS that made it look
   absent / clipped on the screenshot.

2. **Navigation discoverability.** The 5-entry navbar (Home / About /
   Track G+M / Track E / Materials / Impressum) routes to track parents
   that show 12 unit cards each. If these landing pages aren't rendering
   properly, content can look "lost". Worth probing the live deploy.

3. **A specific (track, Klasse, unit) tuple actually missing.** If
   anyone is looking for a particular unit not in the 180-roster,
   that's a real authorial-gap — not a migration recovery — and
   should be recorded as a new unit to author from scratch.

**Awaiting confirmation:** if (1) is the answer, the recovery prompt's
Phases 2–6 should not run. If (3), name the missing tuple before
Phase 2 starts.

---

*Phase 1 complete. Stopping per the prompt's "Stop and report at the
end of each phase" rule.*
