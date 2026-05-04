"""Emit Phase-0 stub Bildungsplan resource YAMLs (one per course).
Each file ships as `status: needs_fetch` with the live URL to fetch.
"""
import pathlib

REPO = pathlib.Path(__file__).resolve().parent.parent
OUT = REPO / "_resources"

URL_SEK1 = "https://www.bildungsplaene-bw.de/,Lde/LS/BP2016BW/ALLG/SEK1/E"
URL_OBER = "https://www.bildungsplaene-bw.de/,Lde/LS/BP2016BW/ALLG/GYM-OS/E"

STUB = """# Bildungsplan resource — {track_label} · Klasse {klasse}
#
# Status: needs_fetch
# Source: {url}
#
# Fill in by fetching the live page above and extracting the
# prozessbezogene and inhaltsbezogene Kompetenzen verbatim
# (codes + German labels). DO NOT paraphrase or invent codes.

site: "efl"
track: "{track}"
klassenstufe: {klasse}
niveau: {niveau_yaml}
status: "needs_fetch"
source_url: "{url}"

prozessbezogene_kompetenzen: []
  # - code: "2.1.1"
  #   label: "Hör-/Hörsehverstehen"
  #   niveau: ["G", "M"]   # which Niveau(stufen) this Kompetenz applies to

inhaltsbezogene_kompetenzen: []
  # - code: "3.1.1.3"
  #   label: "Umgang mit Texten und Medien"
  #   themen: ["family", "school"]
  #   text_types: ["short narrative", "dialogue"]
  #   grammar: ["present simple", "present continuous"]
  #   vocab: ["family members", "classroom"]
"""

CASES = []
# Track G+M, Sek I, Niveau G + M
for k in range(5, 11):
    CASES.append(("gm", k, "G+M", ["G", "M"], URL_SEK1))
# Track E, Sek I, Niveau E
for k in range(5, 11):
    CASES.append(("e", k, "E", ["E"], URL_SEK1))
# Track E, Oberstufe, Niveau E (BF + LF emerge in 11–13)
for k in range(11, 14):
    CASES.append(("e", k, "E (Oberstufe)", ["E-BF", "E-LF"], URL_OBER))


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for track, klasse, label, niveau_list, url in CASES:
        kk = f"{klasse:02d}"
        p = OUT / f"bildungsplan_bw_{track}_kl{kk}.yml"
        niveau_yaml = "[" + ", ".join(f'"{n}"' for n in niveau_list) + "]"
        p.write_text(
            STUB.format(track=track, track_label=label, klasse=klasse,
                        niveau_yaml=niveau_yaml, url=url),
            encoding="utf-8",
        )
    print(f"Wrote {len(CASES)} bildungsplan stubs.")


if __name__ == "__main__":
    main()
