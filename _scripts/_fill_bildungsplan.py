"""Fill _resources/bildungsplan_bw_*.yml with the verbatim Kompetenz-
chapter codes and German labels fetched from bildungsplaene-bw.de.

Sources (fetched 2026-04-30):
- Sek I, Englisch 1. FS:        https://www.bildungsplaene-bw.de/,Lde/LS/BP2016BW/ALLG/SEK1/E1
- Gym 11/12 Leistungsfach:      https://www.bildungsplaene-bw.de/,Lde/LS/BP2016BW/ALLG/GYM/E1/IK/11-12-LF
- Gym 11/12 Basisfach:          https://www.bildungsplaene-bw.de/,Lde/LS/BP2016BW/ALLG/GYM/E1/IK/11-12-BF

The Sek I plan groups Klassenstufen into three Bänder:
  3.1.x — Klassen 5/6
  3.2.x — Klassen 7/8/9
  3.3.x — Klasse 10
The Gymnasium chapter is reused for Niveau E in Sek I (5–10) per
the prompt's Track-E definition; the same chapter codes apply to
Track G+M because the Bildungsplan (Niveau G/M/E) shares structure.

Oberstufe (Kl. 11–13) splits Leistungsfach (3.4.x) and Basisfach
(3.5.x). The codes for Klassenstufenband 11/12 are reused for Kl.
13 as the planning frame; the Bildungsplan itself is structured as
"Kursstufe" rather than per-class.

Per-Unit `bildungsplan:` front-matter cites these codes; the Unit
content tags which Niveau (G/M/E or E-BF/E-LF) it primarily serves.
"""
from __future__ import annotations

import datetime as dt
import pathlib

import yaml

REPO = pathlib.Path(__file__).resolve().parent.parent
OUT = REPO / "_resources"

PROZESS = [
    {"code": "2.1", "label": "Sprachbewusstheit"},
    {"code": "2.2", "label": "Sprachlernkompetenz"},
]


def inhalt(prefix: str) -> list[dict]:
    """Build the inhaltsbezogene-Kompetenzen list for a given chapter prefix
    (e.g. "3.1" for Sek I Kl. 5/6).
    """
    p = prefix
    return [
        {"code": f"{p}.1", "label": "Soziokulturelles Orientierungswissen / Themen"},
        {"code": f"{p}.2", "label": "Interkulturelle kommunikative Kompetenz"},
        {"code": f"{p}.3", "label": "Funktionale kommunikative Kompetenz"},
        {"code": f"{p}.3.1", "label": "Hör-/Hörsehverstehen"},
        {"code": f"{p}.3.2", "label": "Leseverstehen"},
        {"code": f"{p}.3.3", "label": "Sprechen – an Gesprächen teilnehmen"},
        {"code": f"{p}.3.4", "label": "Sprechen – zusammenhängendes monologisches Sprechen"},
        {"code": f"{p}.3.5", "label": "Schreiben"},
        {"code": f"{p}.3.6", "label": "Sprachmittlung"},
        {"code": f"{p}.3.7", "label": "Verfügen über sprachliche Mittel – Wortschatz"},
        {"code": f"{p}.3.8", "label": "Verfügen über sprachliche Mittel – Grammatik"},
        {"code": f"{p}.3.9", "label": "Verfügen über sprachliche Mittel – Aussprache und Intonation"},
        {"code": f"{p}.4", "label": "Text- und Medienkompetenz"},
    ]


def case(track: str, klasse: int, niveau_list: list[str], prefix: str,
         band_label: str, source_url: str, additional_prefix: str = None,
         additional_label: str = None) -> dict:
    """Build one full bildungsplan_bw_*.yml record."""
    inhalt_blocks = []
    inhalt_blocks.append({
        "kompetenzbereich": band_label,
        "kompetenzen": inhalt(prefix),
    })
    if additional_prefix:
        inhalt_blocks.append({
            "kompetenzbereich": additional_label,
            "kompetenzen": inhalt(additional_prefix),
        })

    return {
        "site": "efl",
        "track": track,
        "klassenstufe": klasse,
        "niveau": niveau_list,
        "status": "live_fetched_chapter_skeleton",
        "fetched_at": "2026-04-30",
        "source_urls": [source_url] if isinstance(source_url, str) else list(source_url),
        "notes": (
            "Verbatim Kapitelcodes und deutsche Labels von bildungsplaene-bw.de. "
            "Die feinkörnigen Kompetenzaussagen pro Niveau (G/M/E bzw. BF/LF) "
            "stehen als Detailtext auf den jeweiligen Unterseiten der Quelle "
            "und werden in den Unit-Front-Matter-Feldern bildungsplan:[] "
            "punktgenau zitiert, sobald die einzelnen Units geschrieben werden."
        ),
        "prozessbezogene_kompetenzen": PROZESS,
        "inhaltsbezogene_kompetenzen": inhalt_blocks,
    }


SEK1_URL = "https://www.bildungsplaene-bw.de/,Lde/LS/BP2016BW/ALLG/SEK1/E1"
GYM_LF_URL = "https://www.bildungsplaene-bw.de/,Lde/LS/BP2016BW/ALLG/GYM/E1/IK/11-12-LF"
GYM_BF_URL = "https://www.bildungsplaene-bw.de/,Lde/LS/BP2016BW/ALLG/GYM/E1/IK/11-12-BF"


def main() -> None:
    written = []

    # Track G+M, Klassen 5–10
    for klasse in range(5, 11):
        if klasse in (5, 6):
            prefix, band = "3.1", "Klassen 5/6"
        elif klasse in (7, 8, 9):
            prefix, band = "3.2", "Klassen 7/8/9"
        else:
            prefix, band = "3.3", "Klasse 10"
        rec = case(
            track="gm", klasse=klasse, niveau_list=["G", "M"],
            prefix=prefix, band_label=band, source_url=SEK1_URL,
        )
        p = OUT / f"bildungsplan_bw_gm_kl{klasse:02d}.yml"
        p.write_text(yaml.safe_dump(rec, sort_keys=False, allow_unicode=True),
                     encoding="utf-8")
        written.append(p)

    # Track E, Klassen 5–10 (same Sek I plan, Niveau E)
    for klasse in range(5, 11):
        if klasse in (5, 6):
            prefix, band = "3.1", "Klassen 5/6"
        elif klasse in (7, 8, 9):
            prefix, band = "3.2", "Klassen 7/8/9"
        else:
            prefix, band = "3.3", "Klasse 10"
        rec = case(
            track="e", klasse=klasse, niveau_list=["E"],
            prefix=prefix, band_label=band, source_url=SEK1_URL,
        )
        p = OUT / f"bildungsplan_bw_e_kl{klasse:02d}.yml"
        p.write_text(yaml.safe_dump(rec, sort_keys=False, allow_unicode=True),
                     encoding="utf-8")
        written.append(p)

    # Track E, Klassen 11–13 (Oberstufe — Leistungsfach 3.4 + Basisfach 3.5)
    for klasse in (11, 12, 13):
        rec = case(
            track="e", klasse=klasse, niveau_list=["E-BF", "E-LF"],
            prefix="3.4", band_label="Leistungsfach (Kursstufe)",
            additional_prefix="3.5", additional_label="Basisfach (Kursstufe)",
            source_url=[GYM_LF_URL, GYM_BF_URL],
        )
        p = OUT / f"bildungsplan_bw_e_kl{klasse:02d}.yml"
        p.write_text(yaml.safe_dump(rec, sort_keys=False, allow_unicode=True),
                     encoding="utf-8")
        written.append(p)

    print(f"Wrote {len(written)} bildungsplan YAMLs.")


if __name__ == "__main__":
    main()
