# Current candidate evidence — 2 November 2026

This review branch is not a full-course release. The dated sections below retain
earlier observations; this section supersedes their material-production and local
validation status. No production deployment or release tag is claimed.

All 180 unit bundles now have 540 independently checked PDFs (2,993 pages)
and 540 matching thumbnails. The deck, learner worksheet and teacher worksheet
preserve source content, symbols, links and answer separation. Publication was
guarded by source/artifact hashes and retains original backups. The repository
receipt is [docs/material-build-2026-10-31.json](docs/material-build-2026-10-31.json),
with actual completion dated 2 November. All 360 active unit/exam review
records now match their current source bytes; exact superseded sources and ledger
revisions are archived. Review states and proposed mappings remain pending.

A13 passes 168 full assessments; twelve explicitly declared Klasse 13 rehearsals remain outside full-paper arithmetic and need an accepted scope disposition. A separate listening audit records 145 learner-visible transcripts and five incomplete standalone stimuli. A revised first-lesson pilot remains staged outside this source tree; no wholesale source promotion is claimed.

The strict Hugo build and all configured engineering checks pass except the
blocking D6 historical-audio gate (611 findings). The final browser run
exercised five representative pages and course-specific journeys, including
light/dark accessibility, downloads, search and no-JavaScript access, with zero
accessibility findings, script errors or failed requests. Existing educational
budget and counting-mark warnings remain visible; they have not been waived.

There are 350 separately staged, source-bound candidate voice clips for this
course. Full decode and input/provenance checks pass, but every clip still awaits
real listening review. Production recordings and their truthful failing D6 result
remain unchanged. The suite's `remediation/audio-candidates/index.html` supplies
transcripts, downloads and the pending review queue.

Use the exact prerequisites and commands in [README.md](README.md) with matching
candidate foundations. Release still requires substantive teaching/assessment
repairs, actual native and pedagogical review, timing/grade decisions, accepted
audio, compatible published foundation pins and successful release checks.

## Historical refinement record

# Refinement record — 30 October 2026

This is a local engineering candidate on `refine/2026-10-30`. No hosted CI,
published release or production deployment of these changes has been observed.
The suite strategy and integration order live in the organisation repository,
`docs/refinement-2026-10-30.md` and `docs/release-candidate-2026-10-30.md`.

## Purpose and improvements

The course contains 180 teaching units and 360 committed PDFs. Unique material keys repair audio-manifest collisions across tracks; 304 recording references match source transcripts, and 36 unmatched passages stay explicitly text-only. Discovery filters preserve parent articles for child downloads, pagination reaches all 180 units, and the graph no longer covers the controls.

Shared kit repairs provide accessible navigation, real search indexing, corrected contrast/text sizing, local asset/link checks and representative browser tests. Local templates are selected by explicit layout independently of frozen URLs. Material templates have been synchronised; existing course PDFs and recordings were preserved.

## Actual validation

Strict Hugo build passed. Desktop/mobile browser journeys, automated WCAG 2.1 AA checks, search, downloads, no-JavaScript content and required local engineering checks passed. A21 now passes after the template migration. D6 remains a **release failure**: historical recordings lack sufficient model/speaker provenance and dated voice approval. A passing website build must not conceal that result. English also retains the recorded C1 mark-registry warning; no mark or published address was changed to silence it.

The strengthened curriculum resolver accepts the in-progress manifest structure, not its proposed educational assertions. Two framework source omissions and native/educational review remain blockers. One representative deck and worksheet were rebuilt and visually reviewed in a disposable copy; the full PDF corpus was not regenerated or pedagogically reapproved.

## Roadmap and acceptance

1. Review the local software candidate with the matching kit, curriculum and organisation checkouts using README.md.
2. Audition the prepared candidate voice or provide human recordings. Record actual reviewer/date/model or recording provenance; regenerate synthetic recordings only after approval, or document verifiable historical provenance. Do not invent approval for existing files.
3. Repair the framework source omissions, independently review the course mappings and assessments, and review regenerated materials before replacing committed PDFs.
4. Publish compatible dependencies and pins, run the hosted gate battery, and deploy only after every blocking gate is green and publication is authorised.

Local engineering improvements are usable for review. This course has not met all educational/audio release criteria.


## 31 October 2026 — keyed unit structure and source preservation

All units now declare the five canonical EQS steps and preserve prior heading
anchors from the rendered site. Original source and before/after hashes are in
`docs/eqs-archive/2026-10-31/`. Course mappings remain proposed; the source-hashed
review ledger is `docs/curriculum-review-2026-10-31.json`. It records actual tasks,
current descriptor statements and remaining coverage cells without fabricated
review decisions. Body/exam length and pedagogical approval remain separate.

All 180 embedded assessments were replaced by pointers after exact comparison
confirmed that their complete content already exists in the sibling exam pages.


## Analytics notice consistency — 31 October 2026

Plausible remains enabled and now names its self-hosted script URL explicitly. The privacy notice states the actual script URL and site identifier; unsupported assertions about server location, retained data and guaranteed anonymity were removed from the Plausible section.

Privacy pages declare their analytics policy, language and built URL. New kit gate C9 checks actual HTML scripts and visible notices against configuration; it rejects missing, duplicate or mismatched scripts and contradictory notices. Six gate regressions and three scaffold tests passed. Representative strict builds/C9 passed for website, nsf, nvt, gfl, Scriptlibrary and all three resource-hub notice languages; the suite integration run verifies the remaining sites. This is configuration/content evidence, not certification of the remote server or legal compliance.


## Explicit release dependencies — 31 October 2026

The shared workflow caller now names the same immutable org commit in `uses` and
`org_ref`; `release-pins.json` records the actual historical kit/framework pins.
These historical pins are explicitly not the remediated release. The new org
workflow rejects absent/malformed versions, mismatched source commits and schema
bytes, and nonconforming course manifests; hubs pin dependencies without claiming
course conformance. The coordinated updater prepares exact published foundation
sets, updates consumers/checksums together and retains rollback inputs. Separate
read-only candidate CI can validate immutable pre-release commits without release
tags or deployment rights. Hosted execution and new foundation publication remain
unobserved. See the org `docs/release-pins.md`.

## Integration with main — 10 November 2026

This branch was updated by merging `main` before integration. Main's published
foundation set (org v2.0.1, kit v2.0.2, curriculum v1.3.0), its regenerated
lesson recordings and audio manifests (5 November) and the analytics section of
its privacy notice replace the historical pins, the earlier audio manifest
mapping and the 31 October analytics wording recorded above; D6 now passes.

1 unit whose recorded input text was revised on this branch no longer matches
its recording: `track-e/kl13/units/unit06-mediation-policy-text`. Before release
it needs a new recording of the revised text, or a decision to keep the recorded
wording.
