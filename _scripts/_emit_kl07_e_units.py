"""Emit Track E Klasse 7 — derived from Track G+M Klasse 7 (the
Phase-3 prototype) with Niveau E framing.

Klasse 7 G+M was hand-written one Unit per turn during Phase 3.
The E variant shares cast (Aisha, Ben, Ms. Reyes), theme arc, and
exam content; the framing differs (Niveau E single-track) and the
subtitle is rewritten.
"""
from __future__ import annotations
import pathlib
import re

REPO = pathlib.Path(__file__).resolve().parent.parent
SRC = REPO / "track_gm_kl07" / "units"
DST = REPO / "track_e_kl07" / "units"

REWRITES_UNIT = [
    (re.compile(r'^subtitle: ".+?"$', re.M),
     'subtitle: "Track E · Klasse 7 · Niveau E"'),
    (re.compile(r'^niveau: ".+?"$', re.M),
     'niveau: "E"'),
    (re.compile(r'^track: "gm"$', re.M),
     'track: "e"'),
    (re.compile(r'\*\*Niveau:\*\* G/M parallel\.'),
     '**Niveau:** E.'),
    (re.compile(r'class test \(Klassenarbeit\) at Niveau M'),
     'class test (Klassenarbeit) at Niveau E'),
    (re.compile(r'### Niveau G$', re.M),
     '### Niveau E — controlled'),
    (re.compile(r'### Niveau M$', re.M),
     '### Niveau E — productive'),
]

REWRITES_BODY = [
    (re.compile(r'class test \(Klassenarbeit\) — Niveau M'),
     'class test (Klassenarbeit) — Niveau E'),
]

REWRITES_WRAP = [
    (re.compile(r'^subtitle: ".+?"$', re.M),
     'subtitle: "Track E · Klasse 7 · Niveau E · 45 Minuten"'),
    (re.compile(r'^niveau: ".+?"$', re.M),
     'niveau: "E"'),
    (re.compile(r'^track: "gm"$', re.M),
     'track: "e"'),
    (re.compile(r'Track G\+M · Klasse 7 · Niveau M'),
     'Track E · Klasse 7 · Niveau E'),
]


def transform(text: str, rules) -> str:
    for pattern, replacement in rules:
        text = pattern.sub(replacement, text)
    return text


def main() -> None:
    DST.mkdir(parents=True, exist_ok=True)
    n_unit, n_body, n_wrap = 0, 0, 0
    for src_path in sorted(SRC.glob("*.qmd")):
        if src_path.name == "_metadata.yml":
            continue
        text = src_path.read_text(encoding="utf-8")
        if src_path.name.startswith("_unit") and src_path.name.endswith(
                "_exam_body.qmd"):
            new = transform(text, REWRITES_BODY)
            (DST / src_path.name).write_text(new, encoding="utf-8")
            n_body += 1
        elif src_path.name.endswith("_exam.qmd"):
            new = transform(text, REWRITES_WRAP)
            (DST / src_path.name).write_text(new, encoding="utf-8")
            n_wrap += 1
        elif src_path.name.startswith("unit"):
            new = transform(text, REWRITES_UNIT)
            (DST / src_path.name).write_text(new, encoding="utf-8")
            n_unit += 1

    # Carry over _metadata.yml
    meta = SRC / "_metadata.yml"
    if meta.exists() and not (DST / "_metadata.yml").exists():
        (DST / "_metadata.yml").write_text(
            meta.read_text(encoding="utf-8"), encoding="utf-8")

    print(f"Wrote: {n_unit} units + {n_body} bodies + {n_wrap} wrappers "
          f"= {n_unit + n_body + n_wrap} files for Track E Klasse 7.")


if __name__ == "__main__":
    main()
