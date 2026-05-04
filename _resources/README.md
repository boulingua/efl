# `_resources/`

Single source of truth for the curriculum metadata that drives this
site. Three families of files live here:

## `bildungsplan_bw_*.yml`

One file per (track, Klassenstufe). Holds the verbatim
prozessbezogene and inhaltsbezogene Kompetenzen for that course,
fetched from <https://www.bildungsplaene-bw.de/>.

Naming:

- `bildungsplan_bw_gm_kl05.yml` … `kl10.yml` — Track G+M (Niveau G
  and M side by side, since the BW Sek I Bildungsplan is a single
  Fachplan with Niveau-graded Kompetenzen).
- `bildungsplan_bw_e_kl05.yml` … `kl10.yml` — Track E in Sek I.
- `bildungsplan_bw_e_kl11.yml` … `kl13.yml` — Track E in the
  Oberstufe (gymnasialer Bildungsplan 2021), separately for
  Basisfach (`E-BF`) and Leistungsfach (`E-LF`) where they differ.

**Status:** these files ship as scaffolded stubs marked
`status: needs_fetch`. They MUST be filled by fetching the live
pages from `bildungsplaene-bw.de` before any Unit's
`bildungsplan:` field can be considered complete (Phase 0 of the
generation strategy). Do not invent codes.

## `curriculum_outline.yml`

The 15×12 map of Unit titles, slugs, skills focus, Bildungsplan
anchors, and exam types. Generated and approved in Phase 2 before
any Unit content is written.

## `generation_log.yml`

The status spine for the multi-turn build. Records which phase is
active, which courses are done, which Units have been written and
verified, and the next intended action. Read at the start of every
turn; updated at the end of every turn. See
