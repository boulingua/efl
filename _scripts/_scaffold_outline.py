"""Emit a Phase-2 *proposal* curriculum_outline.yml for EFL.

This file is a starting point for the human-author review. Themes
follow the BW Bildungsplan progression (concrete + personal in Kl.
5–6, widening to cultural and global in Kl. 7–9, critical and
analytical in Kl. 10–13). The Bildungsplan codes per Unit are
left empty — they MUST be filled from the live
`_resources/bildungsplan_bw_*.yml` resources after Phase 0
finalises.

Run once; the resulting YAML should be edited by the author rather
than re-running this script.
"""
from __future__ import annotations

import pathlib

import yaml

REPO = pathlib.Path(__file__).resolve().parent.parent
OUT = REPO / "_resources" / "curriculum_outline.yml"

# Theme ladders per Klassenstufe. Twelve themes per (track, klasse),
# in roughly the school-year order. Paired G+M / E share titles in
# Kl. 5–10 with the same themes; the Niveau cap differs in the
# Units themselves.

GM_E_5 = [
    ("hello-world", "Hello World", ["speaking", "listening", "language_awareness"]),
    ("my-family", "My Family", ["speaking", "writing", "language_awareness"]),
    ("home-and-room", "Home and My Room", ["reading", "writing", "language_awareness"]),
    ("school-day", "A School Day", ["listening", "speaking", "language_awareness"]),
    ("food-and-drinks", "Food and Drinks", ["reading", "speaking", "language_awareness"]),
    ("animals-and-pets", "Animals and Pets", ["reading", "writing", "language_awareness"]),
    ("weather-and-seasons", "Weather and Seasons", ["listening", "writing", "language_awareness"]),
    ("hobbies-and-sports", "Hobbies and Sports", ["speaking", "listening", "language_awareness"]),
    ("birthday-and-friends", "Birthday and Friends", ["speaking", "writing", "language_awareness"]),
    ("a-day-in-london", "A Day in London", ["reading", "listening", "intercultural"]),
    ("clothes-and-colours", "Clothes and Colours", ["speaking", "writing", "language_awareness"]),
    ("review-and-show", "Review and Show", ["speaking", "writing", "language_awareness"]),
]

GM_E_6 = [
    ("a-new-year-at-school", "A New Year at School", ["speaking", "writing", "language_awareness"]),
    ("on-holiday", "On Holiday", ["listening", "speaking", "intercultural"]),
    ("in-the-city", "In the City", ["reading", "speaking", "language_awareness"]),
    ("food-around-the-world", "Food Around the World", ["reading", "writing", "intercultural"]),
    ("daily-routines", "Daily Routines", ["speaking", "writing", "language_awareness"]),
    ("friends-and-feelings", "Friends and Feelings", ["speaking", "writing", "language_awareness"]),
    ("an-adventure-story", "An Adventure Story", ["reading", "writing", "language_awareness"]),
    ("school-around-the-world", "School Around the World", ["reading", "writing", "intercultural"]),
    ("body-and-health", "Body and Health", ["listening", "speaking", "language_awareness"]),
    ("travelling-by-train", "Travelling by Train", ["listening", "speaking", "language_awareness"]),
    ("captain-codys-map", "Captain Cody's Map", ["reading", "writing", "language_awareness"]),
    ("year-end-festival", "Year-End Festival", ["speaking", "writing", "intercultural"]),
]

GM_E_7 = [
    ("first-day-back", "First Day Back", ["speaking", "writing", "language_awareness"]),
    ("growing-up", "Growing Up", ["reading", "writing", "language_awareness"]),
    ("media-in-our-lives", "Media in Our Lives", ["listening", "writing", "language_awareness"]),
    ("a-trip-to-scotland", "A Trip to Scotland", ["reading", "listening", "intercultural"]),
    ("the-united-states-today", "The United States Today", ["reading", "writing", "intercultural"]),
    ("food-cultures", "Food Cultures", ["reading", "speaking", "intercultural"]),
    ("being-a-friend", "Being a Friend", ["speaking", "writing", "language_awareness"]),
    ("first-mediation", "Erste Mediation: A German E-mail", ["mediation", "writing", "language_awareness"]),
    ("school-rules-and-rights", "School Rules and Rights", ["reading", "writing", "language_awareness"]),
    ("a-short-story", "Reading a Short Story", ["reading", "writing", "language_awareness"]),
    ("plans-for-the-summer", "Plans for the Summer", ["speaking", "writing", "language_awareness"]),
    ("year-review-and-podcast", "Year Review: A Class Podcast", ["speaking", "listening", "language_awareness"]),
]

GM_E_8 = [
    ("identities", "Identities", ["reading", "writing", "intercultural"]),
    ("school-life-elsewhere", "School Life Elsewhere", ["reading", "speaking", "intercultural"]),
    ("fairness-at-school", "Fairness at School", ["speaking", "writing", "language_awareness"]),
    ("ireland-stories", "Ireland: Stories from the Island", ["reading", "writing", "intercultural"]),
    ("digital-friendships", "Digital Friendships", ["listening", "writing", "language_awareness"]),
    ("opinion-writing", "Writing an Opinion", ["reading", "writing", "language_awareness"]),
    ("teen-magazine-mediation", "Mediation: A Teen Magazine", ["mediation", "writing", "language_awareness"]),
    ("music-and-belonging", "Music and Belonging", ["listening", "speaking", "intercultural"]),
    ("rural-and-urban", "Rural and Urban Lives", ["reading", "writing", "intercultural"]),
    ("a-novella-in-class", "A Novella in Class", ["reading", "writing", "language_awareness"]),
    ("public-speaking", "Public Speaking: A Short Talk", ["speaking", "listening", "language_awareness"]),
    ("school-magazine-issue", "Class Magazine Issue", ["writing", "speaking", "language_awareness"]),
]

GM_E_9 = [
    ("future-careers", "Future Careers", ["reading", "speaking", "language_awareness"]),
    ("money-and-choices", "Money and Choices", ["reading", "writing", "language_awareness"]),
    ("the-environment-locally", "The Environment, Locally", ["reading", "writing", "intercultural"]),
    ("canada-perspectives", "Canada: Perspectives", ["reading", "writing", "intercultural"]),
    ("media-literacy", "Media Literacy", ["reading", "listening", "language_awareness"]),
    ("interview-and-portrait", "Interview and Portrait", ["speaking", "writing", "language_awareness"]),
    ("mediation-news-article", "Mediation: A German News Article", ["mediation", "writing", "language_awareness"]),
    ("inequality-and-voice", "Inequality and Voice", ["reading", "writing", "language_awareness"]),
    ("short-fiction", "Short Fiction in the Classroom", ["reading", "writing", "language_awareness"]),
    ("application-letter", "Writing an Application Letter", ["reading", "writing", "language_awareness"]),
    ("debate-and-discussion", "Debate and Discussion", ["speaking", "listening", "language_awareness"]),
    ("year-review-portfolio", "Year Review: Portfolio", ["writing", "speaking", "language_awareness"]),
]

GM_10 = [
    ("transition-after-grade-10", "Transition After Grade 10", ["reading", "writing", "language_awareness"]),
    ("the-world-of-work", "The World of Work", ["reading", "speaking", "intercultural"]),
    ("digital-lives-at-work", "Digital Lives at Work", ["reading", "writing", "language_awareness"]),
    ("australia-now", "Australia Now", ["reading", "listening", "intercultural"]),
    ("media-and-truth", "Media and Truth", ["reading", "writing", "language_awareness"]),
    ("contemporary-short-fiction", "Contemporary Short Fiction", ["reading", "writing", "language_awareness"]),
    ("mediation-workplace-text", "Mediation: A Workplace Text", ["mediation", "writing", "language_awareness"]),
    ("civic-english", "Civic English: Rights and Voices", ["reading", "speaking", "language_awareness"]),
    ("youth-and-the-future", "Youth and the Future", ["reading", "writing", "intercultural"]),
    ("project-and-presentation", "Project and Presentation", ["speaking", "listening", "language_awareness"]),
    ("a-short-novel", "A Short Novel", ["reading", "writing", "language_awareness"]),
    ("year-review-graduation", "Year Review: Graduation Exam Prep", ["writing", "speaking", "language_awareness"]),
]

E_10 = [
    ("identity-in-a-global-world", "Identity in a Global World", ["reading", "writing", "intercultural"]),
    ("the-world-of-work", "The World of Work", ["reading", "speaking", "intercultural"]),
    ("digital-lives", "Digital Lives", ["reading", "writing", "language_awareness"]),
    ("australia-and-new-zealand", "Australia and New Zealand", ["reading", "listening", "intercultural"]),
    ("media-and-democracy", "Media and Democracy", ["reading", "writing", "language_awareness"]),
    ("contemporary-short-fiction", "Contemporary Short Fiction", ["reading", "writing", "language_awareness"]),
    ("mediation-feature-article", "Mediation: A German Feature Article", ["mediation", "writing", "language_awareness"]),
    ("science-and-society", "Science and Society", ["reading", "writing", "language_awareness"]),
    ("youth-protest-movements", "Youth Protest Movements", ["reading", "speaking", "intercultural"]),
    ("a-short-novel", "A Short Novel", ["reading", "writing", "language_awareness"]),
    ("public-speaking-and-debate", "Public Speaking and Debate", ["speaking", "listening", "language_awareness"]),
    ("year-review-toward-oberstufe", "Year Review: Toward Oberstufe", ["writing", "speaking", "language_awareness"]),
]

E_11 = [
    ("british-cultural-anchors", "British Cultural Anchors", ["reading", "writing", "intercultural"]),
    ("the-american-dream", "The American Dream", ["reading", "writing", "intercultural"]),
    ("post-colonial-voices-intro", "Post-Colonial Voices: An Introduction", ["reading", "writing", "intercultural"]),
    ("short-stories-and-style", "Short Stories and Style", ["reading", "writing", "language_awareness"]),
    ("poetry-from-the-anthology", "Poetry from the Anthology", ["reading", "writing", "language_awareness"]),
    ("media-literacy-advanced", "Media Literacy, Advanced", ["reading", "listening", "language_awareness"]),
    ("mediation-as-a-skill", "Mediation as a Skill", ["mediation", "writing", "language_awareness"]),
    ("opinion-essay-writing", "Opinion Essay Writing", ["reading", "writing", "language_awareness"]),
    ("a-modern-novel-bf", "A Modern Novel (Basisfach focus)", ["reading", "writing", "language_awareness"]),
    ("a-classic-text-lf", "A Classic Text (Leistungsfach focus)", ["reading", "writing", "language_awareness"]),
    ("public-speaking-prep", "Public Speaking: Toward the Komm-Prüfung", ["speaking", "listening", "language_awareness"]),
    ("klausur-prep-exam-rehearsal", "Klausur Prep: Exam Rehearsal", ["reading", "writing", "language_awareness"]),
]

E_12 = [
    ("dystopias", "Dystopias", ["reading", "writing", "intercultural"]),
    ("globalisation-debates", "Globalisation Debates", ["reading", "writing", "intercultural"]),
    ("science-and-ethics", "Science and Ethics", ["reading", "writing", "language_awareness"]),
    ("shakespeare-extract", "Shakespeare in Extract", ["reading", "writing", "language_awareness"]),
    ("political-discourse", "Political Discourse", ["reading", "listening", "language_awareness"]),
    ("the-non-fiction-essay", "The Non-Fiction Essay", ["reading", "writing", "language_awareness"]),
    ("mediation-academic-text", "Mediation: An Academic Text", ["mediation", "writing", "language_awareness"]),
    ("post-colonial-voices-advanced", "Post-Colonial Voices, Advanced", ["reading", "writing", "intercultural"]),
    ("a-novel-in-full", "A Novel in Full", ["reading", "writing", "language_awareness"]),
    ("kommunikationspruefung-mock", "Kommunikationsprüfung Mock", ["speaking", "listening", "language_awareness"]),
    ("klausur-comprehension-analysis", "Klausur: Comprehension and Analysis", ["reading", "writing", "language_awareness"]),
    ("klausur-composition-and-comment", "Klausur: Composition and Comment", ["reading", "writing", "language_awareness"]),
]

E_13 = [
    ("globalisation-and-the-self", "Globalisation and the Self", ["reading", "writing", "intercultural"]),
    ("political-discourse-advanced", "Political Discourse, Advanced", ["reading", "listening", "language_awareness"]),
    ("dystopias-and-utopias", "Dystopias and Utopias", ["reading", "writing", "language_awareness"]),
    ("contemporary-poetry", "Contemporary Poetry", ["reading", "writing", "language_awareness"]),
    ("media-and-public-opinion", "Media and Public Opinion", ["reading", "writing", "language_awareness"]),
    ("mediation-policy-text", "Mediation: A German Policy Text", ["mediation", "writing", "language_awareness"]),
    ("the-abitur-essay", "The Abitur Essay", ["reading", "writing", "language_awareness"]),
    ("the-abitur-comprehension", "The Abitur Comprehension Task", ["reading", "writing", "language_awareness"]),
    ("the-abitur-analysis", "The Abitur Analysis Task", ["reading", "writing", "language_awareness"]),
    ("kommunikationspruefung-full-mock", "Kommunikationsprüfung: Full Mock", ["speaking", "listening", "language_awareness"]),
    ("issue-framed-debate", "Issue-Framed Debate", ["speaking", "listening", "language_awareness"]),
    ("year-review-and-handover", "Year Review and Handover", ["writing", "speaking", "language_awareness"]),
]

CAST = {
    5: ["Mia", "Theo", "Frida the fox", "Mr. Flint"],
    6: ["Sam", "Lina", "Mr. Flint", "Captain Cody"],
    7: ["Aisha", "Ben", "Ms. Reyes"],
    8: ["Jonas", "Hawa", "global pen-pal class"],
    9: ["Eli", "Naima", "Mr. Yilmaz"],
    10: ["Maja", "young-adult ensemble"],
    11: ["narrators and author voices"],
    12: ["public voices, writers, speakers"],
    13: ["public voices, contemporary writers"],
}

THEME_ARC = {
    5: "concrete and personal: home, school, weather, food, animals, hobbies",
    6: "episodic adventures and routines, light cultural anchors",
    7: "identity and the wider world, English-speaking countries entry-level",
    8: "belonging and fairness, identity, intro to mediation",
    9: "choices and society, environment, social justice, more demanding mediation",
    10: "transition, work, media, science and ethics introduction",
    11: "cultural and literary entry, Basisfach vs Leistungsfach tagging begins",
    12: "discourse and analysis, dystopias, science and ethics, advanced mediation",
    13: "exam-grade and issue-framed, full Abitur preparation",
}


def units(track: str, klasse: int, theme_list, default_niveau: str, exam_type: str):
    out = []
    for i, (slug, title, skills) in enumerate(theme_list, start=1):
        out.append({
            "unit_nr": i,
            "slug": slug,
            "title": title,
            "niveau": default_niveau,
            "skills_focus": skills,
            "bildungsplan": [],   # to be filled from _resources/bildungsplan_bw_*.yml
            "theme_arc_position": i,
            "exam_type": exam_type,
            "summary": "",
        })
    return out


def main() -> None:
    courses = []

    SEK1_TRACKS = [("gm", "G+M"), ("e", "E")]

    THEMES = {
        5: GM_E_5, 6: GM_E_6, 7: GM_E_7, 8: GM_E_8, 9: GM_E_9,
    }
    for klasse in range(5, 10):
        for track, label in SEK1_TRACKS:
            courses.append({
                "track": track,
                "klassenstufe": klasse,
                "niveau": label,
                "cast": CAST[klasse],
                "theme_arc": THEME_ARC[klasse],
                "units": units(track, klasse, THEMES[klasse], label,
                               "klassenarbeit"),
            })

    # Klasse 10 — different theme lists for G+M vs E
    courses.append({
        "track": "gm", "klassenstufe": 10, "niveau": "G+M",
        "cast": CAST[10], "theme_arc": THEME_ARC[10],
        "units": units("gm", 10, GM_10, "G+M", "klassenarbeit"),
    })
    courses.append({
        "track": "e", "klassenstufe": 10, "niveau": "E",
        "cast": CAST[10], "theme_arc": THEME_ARC[10],
        "units": units("e", 10, E_10, "E", "klassenarbeit"),
    })

    # Oberstufe — Track E only, exam types alternate / mark
    OBER = [
        (11, E_11, "abitur_bf"),
        (12, E_12, "abitur_lf"),
        (13, E_13, "abitur_lf"),
    ]
    for klasse, theme_list, exam_type in OBER:
        # Niveau tag in 11–13 splits BF / LF; default mark with E,
        # human reviewer assigns E-BF or E-LF per Unit.
        courses.append({
            "track": "e", "klassenstufe": klasse, "niveau": "E",
            "cast": CAST[klasse], "theme_arc": THEME_ARC[klasse],
            "units": units("e", klasse, theme_list, "E", exam_type),
        })

    out = {
        "site": "efl",
        "status": "proposal_phase2_pending_approval",
        "notes": (
            "Proposal generated by _scripts/_scaffold_outline.py. "
            "Themes follow the BW Bildungsplan progression. "
            "Per-Unit `bildungsplan:` codes are intentionally empty — "
            "they must be filled from _resources/bildungsplan_bw_*.yml "
            "after the live fetches are committed in Phase 0."
        ),
        "courses": courses,
    }

    OUT.write_text(yaml.safe_dump(out, sort_keys=False, allow_unicode=True),
                   encoding="utf-8")
    n_units = sum(len(c["units"]) for c in courses)
    print(f"Wrote {OUT} — {len(courses)} courses, {n_units} units total.")


if __name__ == "__main__":
    main()
