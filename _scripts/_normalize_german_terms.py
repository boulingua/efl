"""Apply the project convention: when a BW-specific German technical
term appears in English prose, write *English term (German term)*.

Targets the most common terms. Skipped contexts:
- `_docs/` (upstream prompt files, kept verbatim).
- `_resources/` (YAML data; technical fields keep German labels).
- Front-matter title / subtitle / niveau lines (the heading IS the
  canonical German label).
- Exam wrapper *_exam.qmd files (their headings include the
  Klassenarbeit label as the canonical exam-name).
- Lines that already contain the English-(German) pattern.

Idempotent — running it twice does not stack the parentheses.
"""
from __future__ import annotations
import pathlib
import re

REPO = pathlib.Path(__file__).resolve().parent.parent

# Order matters — check longer phrases first.
RULES = [
    ("Mittlerer Bildungsabschluss", "Mittlerer Bildungsabschluss",
     "secondary school certificate"),
    ("Hauptschulabschluss", "Hauptschulabschluss",
     "basic secondary school certificate"),
    ("Realschulabschluss", "Realschulabschluss",
     "intermediate secondary certificate"),
    ("Kommunikationsprüfung", "Kommunikationsprüfung",
     "oral exam"),
    ("Erwartungshorizont", "Erwartungshorizont",
     "expected-answer profile"),
    ("Bewertungsraster", "Bewertungsraster", "grading grid"),
    ("Kompetenzerwartung", "Kompetenzerwartung",
     "competency expectation"),
    ("Notenschlüssel", "Notenschlüssel", "grading scale"),
    ("Schulleitung", "Schulleitung", "school administration"),
    ("Sprachmittlung", "Sprachmittlung", "language mediation"),
    ("Klassenarbeit", "Klassenarbeit", "class test"),
    ("Klassenstufe", "Klassenstufe", "year group"),
    ("Bildungsplan", "Bildungsplan", "curriculum framework"),
    ("Leistungsfach", "Leistungsfach", "advanced course"),
    ("Basisfach", "Basisfach", "basic course"),
    ("Gymnasium", "Gymnasium", "grammar school"),
    ("Gesamtschule", "Gesamtschule", "comprehensive school"),
    ("Mediation", "Mediation", "mediation"),  # already English-y
    ("Abitur", "Abitur", "school-leaving examination"),
]

EXCLUDE_PREFIXES = ("_docs/", "_resources/", "_scripts/", ".git/", "docs/")


def is_excluded(rel: str) -> bool:
    return any(rel.startswith(x) for x in EXCLUDE_PREFIXES)


def is_in_frontmatter(text: str, idx: int) -> bool:
    """Return True if idx is within a YAML front-matter block."""
    if not text.startswith("---"):
        return False
    end = text.find("\n---", 3)
    return 0 <= idx <= end + 4


def apply_rule_line(line: str, en: str, de: str) -> str:
    """Apply *en (de)* expansion to the FIRST occurrence of de in line.
    Skip lines that already have the en (de) form, are headings (#),
    are part of a Markdown table cell labeling exam-task names, or
    are already English-(German) elsewhere.
    """
    if f"({de})" in line:  # already has the (German) form
        return line
    if f"{en} ({de})" in line:
        return line
    # Skip lines that are pure heading/title with the term
    if re.match(r"^\s*#{1,6}\s", line) and de in line:
        return line
    # Skip Klassenarbeit row in table headers like "| Punkte | Note |"
    if line.strip().startswith("|") and de in line:
        return line
    # Skip lines starting with "Klassenarbeit" (heading or label)
    if line.lstrip().startswith(de + " "):
        return line
    if line.lstrip().startswith(de + "—") or line.lstrip().startswith(de + " —"):
        return line
    # Pattern: standalone de word (not already in parens, not in a slug)
    pattern = re.compile(rf"(?<![A-Za-zÄÖÜäöüß]){re.escape(de)}(?![A-Za-zÄÖÜäöüß])")
    m = pattern.search(line)
    if not m:
        return line
    # If de is immediately followed by " (", skip
    if line[m.end():m.end()+2] == " (":
        return line
    # If preceded by "(" (already inside parentheses), skip
    pre = line[:m.start()].rstrip()
    if pre.endswith("("):
        return line
    # Replace ONLY this first occurrence in this line
    new = line[:m.start()] + en + " (" + de + ")" + line[m.end():]
    return new


def normalize_text(text: str) -> str:
    """Run all rules over the text, line-by-line, skipping front-matter."""
    fm_end = 0
    if text.startswith("---"):
        end = text.find("\n---", 3)
        fm_end = end + 4 if end > 0 else 0
    head = text[:fm_end]
    body = text[fm_end:]

    out_lines = []
    for line in body.split("\n"):
        new_line = line
        for de, _, en in RULES:
            new_line = apply_rule_line(new_line, en, de)
        out_lines.append(new_line)
    return head + "\n".join(out_lines)


def main() -> None:
    n = 0
    for p in REPO.rglob("*.qmd"):
        rel = p.relative_to(REPO).as_posix()
        if is_excluded(rel):
            continue
        # Skip the standalone exam wrappers — they're thin, the title IS Klassenarbeit
        if rel.endswith("_exam.qmd"):
            continue
        text = p.read_text(encoding="utf-8")
        new = normalize_text(text)
        if new != text:
            p.write_text(new, encoding="utf-8")
            n += 1
    print(f"Normalised {n} .qmd file(s).")


if __name__ == "__main__":
    main()
