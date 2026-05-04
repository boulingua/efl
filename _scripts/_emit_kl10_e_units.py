"""Batch-emit Track E Klasse 10 — all 12 Units.

Track E Klasse 10 is the bridge to the Oberstufe. Voice: argument-
driven, cultural and literary entry-level, issue-based. Cast: Maja
plus a young-adult ensemble. curriculum framework (Bildungsplan)
prefix 3.3 (Klasse 10).

Theme arc differs from G+M Kl. 10: identity in a global world, the
world of work, digital lives, Australia + New Zealand, media and
democracy, contemporary short fiction, mediation of a feature
article, science and society, youth protest movements, a short
novel, public speaking and debate, year-review toward the
Oberstufe.

Grammar arc readies students for the Oberstufe: full conditional
set incl. mixed conditionals, advanced reporting, sophisticated
relative clauses, formal academic register, hedged claims.
"""
from __future__ import annotations
import pathlib

REPO = pathlib.Path(__file__).resolve().parent.parent
COURSE = REPO / "track_e_kl10" / "units"

UNITS = [
    {
        "n": 1, "slug": "identity-in-a-global-world",
        "title": "Identity in a Global World",
        "skills": ["reading", "writing", "intercultural"],
        "bp": [
            "3.3.1 Soziokulturelles Orientierungswissen / Themen",
            "3.3.2 Interkulturelle kommunikative Kompetenz",
            "3.3.3.2 Leseverstehen",
            "3.3.3.5 Schreiben",
            "3.3.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can read a short essay on transnational identity and identify the writer's main claim and one supporting move.",
            "I can use mixed conditionals to discuss how past choices shape present identity.",
            "I can write a 200-word identity reflection that goes past flag-and-passport thinking.",
        ],
        "leadin": (
            "Maja's older cousin lives in Brisbane, works for a "
            "company headquartered in Singapore, holds a German "
            "passport, and dreams in English. When asked at customs "
            "where she is *from*, she sometimes says *Stuttgart*, "
            "sometimes *Brisbane*, sometimes *the airport waiting "
            "lounge*. None of these is a joke. All of them are "
            "true."
        ),
        "activate": (
            "**Three-card identity scan.** On three sticky notes "
            "write: a place that shaped you, a language that lives "
            "in your kitchen, a thing you do that says something "
            "about you. Compare with another pair."
        ),
        "input_blocks": [
            ("Reading — *Where Are You From, Really?*",
             "*The question 'where are you from?' is rarely as "
             "simple as the asker thinks. For many people, the "
             "honest answer involves three places, two languages "
             "and one airport. Identity, in a more globalised "
             "world, has stopped being a single sticker on a "
             "passport. It is now closer to a set of overlapping "
             "memberships, some of which contradict each other "
             "without being false. The interesting question is no "
             "longer 'which one are you?' but 'how do these get on "
             "together?'*"),
            ("Grammar — mixed conditionals",
             "Mixed conditionals link a **past unreal** condition "
             "to a **present unreal** result, or vice versa.\n\n"
             "- *If I had moved to Brisbane in 2015* (past unreal), "
             "*I would be living there now* (present result).\n"
             "- *If I were less curious* (present unreal), *I "
             "would not have applied for the exchange* (past "
             "result).\n\n"
             "Form: *if + past perfect, would + base verb* OR "
             "*if + past simple, would have + past participle*."),
        ],
        "practise_g": [
            "1. Choose mixed conditional: *(past unreal → present "
            "result)* If she __________ (move) earlier, she "
            "__________ (live) there now.",
            "2. Match: globalisation → cross-border movement; "
            "transnational → across nations; cosmopolitan → "
            "city-of-the-world.",
        ],
        "practise_m": [
            "3. Build 4 mixed conditional sentences about a real "
            "or imagined identity / decision.",
        ],
        "answer_g": (
            "1. had moved / would be living.\n"
            "2. all true."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Identity reflection, 200 words.** Write past flag-"
            "and-passport identity. Use 2 mixed conditionals + 1 "
            "third conditional + 1 *both … and …*"
        ),
        "produce_sample": (
            "*If I had grown up in only one country, I would "
            "probably trust the question 'where are you from?' "
            "more than I do. As it is, the honest answer involves "
            "two cities, one language at the kitchen table and "
            "another in the school corridor, and a grandmother who "
            "switches between three sentences for the same "
            "instruction. If my parents had not moved when they "
            "did, I would not be sitting here writing this in "
            "English. I am both German and not-only-German, and "
            "the *not-only* is not a missing piece — it is part of "
            "the actual answer. The question I prefer to ask is "
            "different: how do my different memberships get on "
            "together day by day? Some Sundays they argue. Most "
            "weekdays they cooperate. None of them is fake. None "
            "of them, on its own, would explain my breakfast.*"
        ),
        "reflect": [
            "I can identify a writer's main claim and one supporting move in a short essay.",
            "I can use mixed conditionals.",
            "I can write a 200-word identity reflection.",
        ],
        "pitfalls": [
            "*If I would have moved earlier, I would live there* "
            "→ ✗ — *if* clause uses past perfect, not *would have*.",
            "Mixed ≠ random tense salad — both clauses must "
            "actually be unreal.",
            "Stereotype check: don't reduce identity to a single "
            "label.",
        ],
        "further": [
            "TED Ideas — short essays on identity.",
            "The Atlantic — *Identity* essays.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"Identity is no longer a single sticker on a "
            "passport. It is closer to a set of overlapping "
            "memberships, some of which contradict each other "
            "without being false. If my parents had not moved when "
            "they did, I would not be living between two cities "
            "now.\"\n\n"
            "1. Identity now: ___ . 2. Memberships: ___ . 3. "
            "Counterfactual: ___ . 4. Result: ___ ."
        ),
        "exam_reading": (
            "Read the *Where Are You From, Really?* extract above.\n\n"
            "1. Common assumption about the question: ___ . 2. "
            "Honest answer: ___ . 3. Identity has stopped being: "
            "___ . 4. Better question: ___ ."
        ),
        "exam_use": (
            "**Mixed conditional or third conditional?**\n\n"
            "1. *(mixed)* If I __________ (grow up) elsewhere, my "
            "answer __________ (be) different now.\n"
            "2. *(third)* If she __________ (apply) earlier, she "
            "__________ (get) the place.\n"
            "3. *(mixed)* If he __________ (be) less curious, he "
            "__________ (not / take) that risk last year.\n"
            "4. *(third)* They __________ (find) out earlier if "
            "they __________ (look) carefully."
        ),
        "exam_writing": (
            "Write 200 words: an identity reflection past flag-"
            "and-passport thinking. Use 2 mixed conditionals."
        ),
        "exam_keys": [
            "**T1.** overlapping memberships, not single sticker; some contradict without being false; if parents hadn't moved; would not be living between two cities.",
            "**T2.** simpler than the asker thinks; three places, two languages, one airport; a single sticker on a passport; how do these get on together?",
            "**T3.** had grown up / would be; had applied / would have got; were / wouldn't have taken; would have found / had looked.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 2, "slug": "the-world-of-work",
        "title": "The World of Work",
        "skills": ["reading", "speaking", "intercultural"],
        "bp": [
            "3.3.1 Soziokulturelles Orientierungswissen / Themen",
            "3.3.2 Interkulturelle kommunikative Kompetenz",
            "3.3.3.2 Leseverstehen",
            "3.3.3.3 Sprechen – an Gesprächen teilnehmen",
            "3.3.3.7 Verfügen über sprachliche Mittel – Wortschatz",
        ],
        "objectives": [
            "I can read a job-profile and pick out 8 facts.",
            "I can hold a 5-minute structured job-interview role-play.",
            "I can write a 200-word reflection on my future career interests.",
        ],
        "leadin": (
            "Maja is preparing for a one-week internship at a "
            "small architecture firm in Stuttgart. She has read the "
            "firm's portfolio twice. She has prepared four "
            "questions and one polite refusal in case the coffee "
            "they offer is, as her aunt warned, *the kind that "
            "looks like coffee but isn't*."
        ),
        "activate": (
            "**Job-shadow scan.** With your partner, list four "
            "fields you would want a one-week internship in, plus "
            "one specific reason for each."
        ),
        "input_blocks": [
            ("Reading — *Inside an Architecture Firm* (extract)",
             "*The firm has been working on small-scale public "
             "buildings — kindergartens, libraries, a community "
             "centre — for the past fifteen years. The senior "
             "architect, who founded the firm at 31, says the "
             "biggest professional change of her career has been "
             "the shift from drawing on paper to building on "
             "screen. The biggest skill, she adds, has not "
             "changed: listening to a brief twice before "
             "answering once.*"),
            ("Vocabulary — workplace (extended)",
             "*portfolio, brief, milestone, deliverable, "
             "stakeholder, senior / junior, line manager, "
             "probation, performance review, mentor, mentee, "
             "feedback loop, pivot, lateral move, soft skills, "
             "hard skills.*"),
        ],
        "practise_g": [
            "1. Match: brief → instructions; milestone → checkpoint; "
            "deliverable → finished output.",
            "2. T or F: the senior architect said the biggest skill "
            "is drawing.",
        ],
        "practise_m": [
            "3. Build 5 sentences using 5 workplace-vocabulary "
            "words about a real or imagined internship.",
        ],
        "answer_g": (
            "1. all true.\n"
            "2. F (the biggest skill is listening to a brief twice "
            "before answering once)."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Structured job-interview role-play.** 5 minutes "
            "each direction. 6 questions including: experience, "
            "motivation, mistake / lesson, future ambition. Use 2 "
            "present perfect continuous + 1 third conditional + 1 "
            "*despite* / *because of*."
        ),
        "produce_sample": (
            "*— What experience do you bring?*\n"
            "*— I have been doing weekend shifts at a café for "
            "two years. Despite the limited scope, the work has "
            "taught me to read a busy room. If I had started "
            "earlier, I would already have line-manager "
            "experience.*"
        ),
        "reflect": [
            "I can pick out 8 facts in a job-profile.",
            "I can run a 5-minute structured job-interview.",
            "I can write a 200-word career reflection.",
        ],
        "pitfalls": [
            "Vague claims (*I am a hard worker*) — replace with "
            "one specific example.",
            "*am working since* → ✗ / *have been working since* "
            "→ ✓.",
            "Don't romanticise a sector — name one specific "
            "downside you've considered.",
        ],
        "further": [
            "BBC Worklife — short articles.",
            "Harvard Business Review — accessible career articles.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"The senior architect founded the firm at 31. The "
            "biggest professional change of her career has been "
            "the shift from drawing on paper to building on screen. "
            "The biggest skill, she adds, has not changed: "
            "listening to a brief twice before answering once.\"\n\n"
            "1. Founded at age: ___ . 2. Biggest change: ___ . 3. "
            "Biggest skill: ___ . 4. The skill specifically: ___ ."
        ),
        "exam_reading": (
            "Read the *Inside an Architecture Firm* extract above.\n\n"
            "1. Building types: ___ . 2. Years on small-scale "
            "work: ___ . 3. Founder's age at start: ___ . 4. "
            "Constant skill: ___ ."
        ),
        "exam_use": (
            "**Mixed grammar.**\n\n"
            "1. The firm __________ (work) on small-scale "
            "buildings for 15 years. (perfect cont.)\n"
            "2. If she __________ (start) earlier, she __________ "
            "(have) more experience. (third)\n"
            "3. ___ the limited scope, the café work taught me "
            "rhythm. (despite)\n"
            "4. The biggest skill __________ (not / change)."
        ),
        "exam_writing": (
            "Write 200 words: a career reflection. Use 2 perfect "
            "continuous + 1 third conditional + 1 *despite*."
        ),
        "exam_keys": [
            "**T1.** 31; drawing on paper → building on screen; listening; listen to a brief twice before answering once.",
            "**T2.** kindergartens, libraries, a community centre; 15 years; 31; listening to a brief twice before answering once.",
            "**T3.** has been working / had started — would have had / Despite / has not changed.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 3, "slug": "digital-lives",
        "title": "Digital Lives",
        "skills": ["reading", "writing", "language_awareness"],
        "bp": [
            "3.3.1 Soziokulturelles Orientierungswissen / Themen",
            "3.3.3.2 Leseverstehen",
            "3.3.3.5 Schreiben",
            "3.3.3.8 Verfügen über sprachliche Mittel – Grammatik",
            "3.3.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can read a short essay on digital life and identify the writer's stance and one nuance.",
            "I can use complex sentences with subordinate clauses (*although, even though, while, whereas, given that*).",
            "I can write a 200-word digital-life reflection.",
        ],
        "leadin": (
            "Maja read an article in which the author claimed that "
            "*digital life* is now a redundant phrase, because life "
            "has, for nearly all the people she knows, become "
            "digital and offline at the same time, woven together "
            "rather than alternating. Maja agreed with most of "
            "this, disagreed with the *for nearly all*, and was "
            "annoyed by the certainty of the phrase *redundant*."
        ),
        "activate": (
            "**Two-column scan.** Board: *digital life is …* / "
            "*digital life is not …* — class fills four honest "
            "items under each."
        ),
        "input_blocks": [
            ("Reading — *Digital, Honestly*",
             "*The phrase 'digital life' is increasingly "
             "redundant. For most readers under 30, the digital "
             "and the offline are no longer alternating modes; "
             "they are woven together. While this can be a problem "
             "for attention, it is rarely the catastrophe older "
             "commentators describe. Even though there are real "
             "harms — the steep, well-documented effects on sleep, "
             "for instance — the picture is more local and more "
             "specific than 'a generation ruined by phones'.*"),
            ("Grammar — complex sentences with subordinate clauses",
             "**Concession** (admitting a partial counter-point):\n"
             "- *Although the harms are real, the picture is more "
             "specific than the headlines suggest.*\n"
             "- *Even though I agree with most of this, I object "
             "to the certainty.*\n\n"
             "**Contrast:**\n"
             "- *While this can be a problem for attention, it is "
             "rarely a catastrophe.*\n"
             "- *Whereas older commentators see ruin, younger ones "
             "see overlap.*\n\n"
             "**Causal-given:**\n"
             "- *Given that we cannot un-build the internet, the "
             "honest question is what to do with it.*"),
        ],
        "practise_g": [
            "1. Choose: *although / while / given that / even "
            "though*: ___ digital life feels normal, the harms are "
            "real. ___ we cannot un-build the internet, the "
            "question is what to do.",
            "2. Match: concession → although; contrast → whereas; "
            "given that → reasoning premise.",
        ],
        "practise_m": [
            "3. Build 4 complex sentences using 4 different "
            "subordinators about a digital-life topic.",
        ],
        "answer_g": (
            "1. Although (or While) / Given that.\n"
            "2. all true."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Reflection, 200 words.** Take a position on whether "
            "*'digital life'* is a redundant phrase. Use 4 "
            "subordinators (one of each: concession, contrast, "
            "addition, causal)."
        ),
        "produce_sample": (
            "*Although I agree with most of the article's argument, "
            "I object to the certainty of the word 'redundant'. "
            "While the digital and the offline are clearly woven "
            "together for most readers under 30, calling the "
            "distinction redundant assumes that the weave is even "
            "across people, which it isn't. Even though my "
            "schoolmates seem to live the integrated version, I "
            "know younger neighbours who still do most of their "
            "social life face-to-face. Given that the picture is "
            "uneven, the more useful question is not 'is it "
            "redundant?' but 'for whom and when?' Whereas older "
            "commentators tend to see ruin, the article tends to "
            "see seamlessness — both pictures are partial. The "
            "honest answer probably involves naming specific "
            "harms (sleep, attention) without inflating them, and "
            "naming specific benefits (reach, friendship across "
            "cities) without romanticising them.*"
        ),
        "reflect": [
            "I can identify the writer's stance and one nuance in a digital-life essay.",
            "I can use 4 subordinators correctly.",
            "I can write a 200-word position paragraph.",
        ],
        "pitfalls": [
            "*Although + but* → ✗ — pick one.",
            "*Given that* in casual writing can read pompous; use "
            "it deliberately.",
            "Concession without engagement (*although X, still Y*) "
            "without engaging X — weak.",
        ],
        "further": [
            "The Atlantic — *Technology* essays.",
            "Cal Newport, *Digital Minimalism* — accessible "
            "chapters.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"For most readers under 30, the digital and the "
            "offline are no longer alternating modes. While this "
            "can be a problem for attention, it is rarely a "
            "catastrophe. Even though the harms — for instance on "
            "sleep — are real, the picture is more local than 'a "
            "generation ruined by phones'.\"\n\n"
            "1. Audience: ___ . 2. Concession: ___ . 3. Specific "
            "harm: ___ . 4. Stance against: ___ ."
        ),
        "exam_reading": (
            "Read the *Digital, Honestly* extract above.\n\n"
            "1. Claim: ___ . 2. For whom: ___ . 3. One real "
            "harm: ___ . 4. What the picture is NOT: ___ ."
        ),
        "exam_use": (
            "**Insert the right subordinator.**\n\n"
            "1. ___ I agree with most of this, I object to the "
            "certainty.\n"
            "2. ___ this can be a problem for attention, it is "
            "rarely a catastrophe.\n"
            "3. ___ we cannot un-build the internet, the question "
            "is what to do.\n"
            "4. ___ older commentators see ruin, younger ones see "
            "overlap."
        ),
        "exam_writing": (
            "Write 200 words: a position paragraph on a digital-"
            "life topic. Use 4 subordinators."
        ),
        "exam_keys": [
            "**T1.** under-30 readers; can be problem for attention; sleep effects; rarely a catastrophe / 'a generation ruined by phones'.",
            "**T2.** 'digital life' is redundant; under-30 readers; sleep effects; not a catastrophe / not a generation ruined.",
            "**T3.** Although / While / Given that / Whereas.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 4, "slug": "australia-and-new-zealand",
        "title": "Australia and New Zealand",
        "skills": ["reading", "listening", "intercultural"],
        "bp": [
            "3.3.1 Soziokulturelles Orientierungswissen / Themen",
            "3.3.2 Interkulturelle kommunikative Kompetenz",
            "3.3.3.1 Hör-/Hörsehverstehen",
            "3.3.3.2 Leseverstehen",
            "3.3.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can read a short comparative text on Australia and New Zealand and identify three points of difference.",
            "I can recognise basic Māori-English vocabulary and Aboriginal-English place names in context.",
            "I can write a 200-word comparative regional portrait.",
        ],
        "leadin": (
            "Maja's class compared two pen-pal letters: one from "
            "Brisbane, one from Wellington. The Brisbane letter "
            "talked about heat and cricket. The Wellington letter "
            "talked about wind, te reo Māori in the cafés, and a "
            "national mood that the writer described as *small-"
            "country, big-listening*."
        ),
        "activate": (
            "**Two-flag scan.** Quick map exercise: locate "
            "Australia and New Zealand on the slide. Write three "
            "differences (geography, population, language)."
        ),
        "input_blocks": [
            ("Reading — *Two Pen-Pals*",
             "*Australia is a continent of about 26 million; New "
             "Zealand is two main islands of about 5.2 million. "
             "While both share British colonial history, "
             "Indigenous languages are visible on different "
             "scales. In New Zealand, te reo Māori is widely "
             "audible in news, cafés and government — *kia ora* "
             "is the everyday hello. In Australia, hundreds of "
             "Aboriginal languages survive, often more locally "
             "audible than nationally so. Place names like "
             "*Wagga Wagga* and *Wollongong* preserve those "
             "languages in plain sight, even when the city itself "
             "looks British.*"),
            ("Vocabulary — Māori-English (basic)",
             "*kia ora (hello / good health), whānau (extended "
             "family), aroha (love / compassion), iwi (tribe), "
             "marae (meeting ground), te reo (the language).*"),
            ("Vocabulary — Aboriginal-English place names",
             "*Wagga Wagga (place of many crows / Wiradjuri), "
             "Wollongong (sound of the sea / Dharawal), Parramatta "
             "(place where eels lie down / Darug), Toowoomba (place "
             "of swamp), Canberra (meeting place).*"),
        ],
        "practise_g": [
            "1. Match: kia ora → hello; whānau → family; iwi → "
            "tribe.",
            "2. T or F: NZ has c. 5.2 million people; Australia is "
            "less populous than NZ; Wagga Wagga has a Wiradjuri "
            "origin.",
        ],
        "practise_m": [
            "3. Build 4 sentences comparing AU and NZ on language, "
            "geography, population, and Indigenous visibility.",
        ],
        "answer_g": (
            "1. all true.\n"
            "2. T, F (Australia is more populous), T."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Comparative portrait, 200 words.** Compare Australia "
            "and New Zealand past stereotypes. Use 2 comparatives "
            "/ superlatives + 1 *whereas* + 1 *kia ora* or "
            "Indigenous place name in context."
        ),
        "produce_sample": (
            "*Australia and New Zealand share a British colonial "
            "history but diverge sharply in scale. Australia is a "
            "continent of about 26 million; New Zealand, two main "
            "islands of about 5.2 million. The most striking "
            "linguistic difference is the visibility of Indigenous "
            "languages: in New Zealand, te reo Māori is widely "
            "audible in news, cafés, and government — *kia ora* is "
            "the everyday hello. Whereas in Australia, hundreds of "
            "Aboriginal languages survive, often more locally "
            "audible than nationally so. Place names like Wagga "
            "Wagga (Wiradjuri) and Parramatta (Darug) preserve "
            "those languages in the streetscape, even when the "
            "city itself looks British. Australia is climatically "
            "harder; New Zealand is, by most measures, less "
            "extreme. Wellington's reputation, however, suggests "
            "that 'less extreme' does not mean 'gentle' — the "
            "city is the windiest capital in the world.*"
        ),
        "reflect": [
            "I can identify three differences between AU and NZ.",
            "I can recognise 6 Māori-English / Aboriginal-English words.",
            "I can write a 200-word comparative regional portrait.",
        ],
        "pitfalls": [
            "*New Zealanders speak Māori* (over-claim) → ✗. About "
            "20 % of NZ population identifies as Māori; te reo is "
            "widely audible but not the home language of all.",
            "*Aboriginal* refers to mainland Australia. *Torres "
            "Strait Islander* peoples are a distinct group.",
            "Stereotype check: AU ≠ outback only; NZ ≠ Lord of the "
            "Rings.",
        ],
        "further": [
            "ABC Australia News, RNZ News (NZ).",
            "Te Papa Tongarewa (NZ national museum) — accessible "
            "online articles.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"In New Zealand, te reo Māori is widely audible — "
            "kia ora is the everyday hello. About 5.2 million "
            "people live there. In Australia, hundreds of "
            "Aboriginal languages survive, often more locally "
            "audible than nationally. Wagga Wagga is a Wiradjuri "
            "place name.\"\n\n"
            "1. NZ greeting: ___ . 2. NZ population: ___ . 3. AU "
            "languages: ___ . 4. Wagga Wagga origin: ___ ."
        ),
        "exam_reading": (
            "Read the *Two Pen-Pals* extract above.\n\n"
            "1. Population gap: ___ . 2. Shared history: ___ . 3. "
            "te reo visibility: ___ . 4. AU language visibility: "
            "___ ."
        ),
        "exam_use": (
            "**Match.**\n\n"
            "1. kia ora → ___ ; 2. whānau → ___ ; 3. iwi → ___ ; "
            "4. Wagga Wagga origin: ___ ."
        ),
        "exam_writing": (
            "Write 200 words: a comparative AU / NZ portrait. Use "
            "2 comparatives + 1 Māori or Aboriginal place name."
        ),
        "exam_keys": [
            "**T1.** kia ora; about 5.2 million; hundreds of Aboriginal languages; Wiradjuri.",
            "**T2.** ~26m vs ~5.2m; British colonial; widely audible incl. news / cafés / government; often more locally audible than nationally.",
            "**T3.** hello / extended family / tribe / Wiradjuri (place of many crows).",
            "**T4.** Open.",
        ],
    },
    {
        "n": 5, "slug": "media-and-democracy",
        "title": "Media and Democracy",
        "skills": ["reading", "writing", "language_awareness"],
        "bp": [
            "3.3.1 Soziokulturelles Orientierungswissen / Themen",
            "3.3.3.2 Leseverstehen",
            "3.3.3.5 Schreiben",
            "3.3.3.7 Verfügen über sprachliche Mittel – Wortschatz",
            "3.3.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can read a short text linking media and democratic life and identify three causal claims.",
            "I can use academic register hedges (*it has been argued that, the available evidence suggests, in some contexts*).",
            "I can write a 220-word op-ed on a media-democracy topic.",
        ],
        "leadin": (
            "Maja's class read a one-page essay about local "
            "newspapers. The essay opened with a fact that "
            "surprised most of the class: more than 200 local UK "
            "papers have closed in the past two decades, and "
            "research has linked their absence to lower voter "
            "turnout in the affected districts. Maja underlined "
            "the verb *has linked*. \"Linked is not caused,\" she "
            "said. \"Useful word.\""
        ),
        "activate": (
            "**Source-trust scan.** With your partner, rank five "
            "media types from *most* to *least* trustworthy and "
            "explain why for each."
        ),
        "input_blocks": [
            ("Reading — *Local Papers, Local Voters*",
             "*More than 200 local newspapers in the UK have "
             "closed in the past two decades. Research has linked "
             "their disappearance to lower voter turnout, less "
             "scrutiny of local councils and slower response to "
             "local environmental issues. The link is not "
             "necessarily causal — districts that lose papers "
             "are also often districts under broader economic "
             "stress — but it is consistent across studies. In "
             "some contexts, hyper-local newsletters and citizen "
             "journalism have replaced the papers; in others, "
             "they have not.*"),
            ("Vocabulary — media and democracy",
             "*free press, press freedom, accountability, "
             "scrutiny, oversight, opinion vs. reporting, "
             "editorial independence, conflict of interest, "
             "sponsored content, public-interest journalism, "
             "civic information, local press desert.*"),
            ("Academic-register hedges",
             "*It has been argued that … / The available evidence "
             "suggests that … / In some contexts … / This is not "
             "necessarily causal … / The link is consistent "
             "across studies … / Critics maintain that … / "
             "Caution is warranted.*"),
        ],
        "practise_g": [
            "1. Choose hedge: *It has been argued / The evidence "
            "suggests / Critics maintain* — ___ that local papers "
            "support voter turnout. ___ that the link is causal.",
            "2. Match: free press → press freedom; oversight → "
            "scrutiny; sponsored content → paid promotion.",
        ],
        "practise_m": [
            "3. Build 4 academic-register sentences on the local-"
            "press topic.",
        ],
        "answer_g": (
            "1. The evidence suggests / Critics maintain.\n"
            "2. all true."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Op-ed, 220 words.** Take a position on a media-"
            "democracy topic of your choice. Use 4 academic-"
            "register hedges + 1 cautious-claim phrase + 1 "
            "complex-sentence subordinator."
        ),
        "produce_sample": (
            "*The available evidence suggests that the closure of "
            "more than 200 local newspapers in the UK over the "
            "past two decades has had measurable democratic "
            "consequences. Research has linked their disappearance "
            "to lower voter turnout, less scrutiny of councils, "
            "and slower response to local environmental issues. "
            "It has been argued, with reason, that the link is not "
            "necessarily causal — districts that lose papers are "
            "often districts under broader economic stress. "
            "However, the consistency of the link across studies "
            "warrants attention. In some contexts, hyper-local "
            "newsletters and citizen journalism have replaced the "
            "papers; in others, they have not. Critics maintain "
            "that volunteer-run replacements lack the staff time "
            "for sustained scrutiny, which is the part of "
            "journalism most at risk in a press desert. Although "
            "the picture is uneven, the policy implication is "
            "fairly clear: support for local public-interest "
            "journalism — through grant schemes, regulatory "
            "tweaks, or simply paid subscriptions — is one of the "
            "cheaper democratic investments available. Caution is "
            "warranted; complacency is not.*"
        ),
        "reflect": [
            "I can identify 3 causal claims in a media-democracy text.",
            "I can use 4 academic-register hedges.",
            "I can write a 220-word op-ed.",
        ],
        "pitfalls": [
            "*The evidence proves* — overstatement; *suggests*, "
            "*indicates*, *is consistent with* are safer.",
            "*correlation* mistaken for *causation*.",
            "Avoid the lecture voice — keep paragraphs short and "
            "argumentative.",
        ],
        "further": [
            "The Guardian — *Comment is free*.",
            "Reuters Institute — accessible digital news report.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"More than 200 local UK papers have closed. The "
            "evidence suggests this is linked to lower voter "
            "turnout and less scrutiny of councils. The link is "
            "not necessarily causal — affected districts also tend "
            "to be under economic stress. The link is, however, "
            "consistent across studies.\"\n\n"
            "1. Number closed: ___ . 2. Two effects: ___ . 3. "
            "Caveat: ___ . 4. Reliability: ___ ."
        ),
        "exam_reading": (
            "Read the *Local Papers, Local Voters* extract above.\n\n"
            "1. Three linked effects: ___ . 2. Caveat about "
            "causality: ___ . 3. Replacement examples: ___ . 4. "
            "Whether replacements work: ___ ."
        ),
        "exam_use": (
            "**Insert academic hedge.**\n\n"
            "1. ___ that local papers strengthen civic information.\n"
            "2. ___ that the link is causal.\n"
            "3. ___ , citizen journalism has filled the gap.\n"
            "4. ___ ; the variation across districts is real."
        ),
        "exam_writing": (
            "Write 220 words: an op-ed on a media-democracy "
            "topic. Use 4 academic hedges."
        ),
        "exam_keys": [
            "**T1.** 200+; lower voter turnout / less scrutiny of councils; districts also under economic stress; consistent across studies.",
            "**T2.** lower voter turnout / less scrutiny of councils / slower response on local environment; districts often under broader economic stress; hyper-local newsletters and citizen journalism; in some contexts yes, in others no.",
            "**T3.** The evidence suggests / Critics maintain / In some contexts / Caution is warranted.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 6, "slug": "contemporary-short-fiction",
        "title": "Contemporary Short Fiction",
        "skills": ["reading", "writing", "language_awareness"],
        "bp": [
            "3.3.1 Soziokulturelles Orientierungswissen / Themen",
            "3.3.3.2 Leseverstehen",
            "3.3.3.5 Schreiben",
            "3.3.3.8 Verfügen über sprachliche Mittel – Grammatik",
            "3.3.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can read a short story and identify protagonist arc, theme, narrator stance, and one stylistic move.",
            "I can use participle clauses for concise narrative description (*walking home, she …*).",
            "I can write a 250-word literary essay.",
        ],
        "leadin": (
            "The class read an imagined contemporary short story "
            "called *Late Bus, Cold Bench*. By page two, half the "
            "class had decided it was about loneliness. By page "
            "three, the other half had decided it was about "
            "kindness. By the end, both halves agreed it was about "
            "a thing that happens between strangers when no one is "
            "performing."
        ),
        "activate": (
            "**Story shape sketch.** Draw the rise and fall of "
            "*Late Bus, Cold Bench* in one line. Add three "
            "specific words from the text."
        ),
        "input_blocks": [
            ("Reading — *Late Bus, Cold Bench* (extract)",
             "*Walking home through the empty plaza, she heard the "
             "bus pull away two minutes early. The shelter was "
             "empty except for an old man drinking from a paper "
             "cup. She sat down, pulled her coat over her knees, "
             "and admitted, silently, that the universe had "
             "designed this evening for her. The man, having "
             "noticed her sitting, slid the paper cup toward her "
             "without speaking. The cup was full of warm tea.*"),
            ("Grammar — participle clauses (concise narrative)",
             "Replace one full clause with an *-ing* or *-ed* "
             "phrase to keep narrative momentum.\n\n"
             "**-ing (active):**\n"
             "- *She walked home. She thought about the day.* → "
             "*Walking home, she thought about the day.*\n\n"
             "**-ed (passive / completed):**\n"
             "- *Tired by the day, she sat down.*\n\n"
             "**Having + past participle (sequence):**\n"
             "- *Having noticed her, the man slid the cup toward "
             "her.*"),
        ],
        "practise_g": [
            "1. Build a participle clause: *(walk home / she / "
            "hear)* → ___ ; *(tire by the day / she / sit)* → "
            "___ .",
            "2. Match: -ing → active; -ed → passive / completed; "
            "having + pp → sequence.",
        ],
        "practise_m": [
            "3. Rewrite 4 short sentences using participle "
            "clauses.",
        ],
        "answer_g": (
            "1. *Walking home, she heard. Tired by the day, she "
            "sat.*\n"
            "2. all true."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Literary essay, 250 words.** Read the extract. "
            "Answer: *Who is the narrator? What is the conflict? "
            "What is the theme? Which one move does the most "
            "work?* Use 3 participle clauses + 1 direct quote + 1 "
            "*whereas*."
        ),
        "produce_sample": (
            "*Walking home through the empty plaza in the opening "
            "lines of *Late Bus, Cold Bench*, the narrator is "
            "already framed as a person who notices her own "
            "loneliness without dramatising it. Tired by the day, "
            "she sits down on a cold bench and admits silently "
            "that the universe has, indeed, arranged this evening "
            "for her. Whereas a more sentimental story would "
            "linger here, the author tightens immediately: an old "
            "man, having noticed her sitting, slides his paper "
            "cup of warm tea toward her without speaking. The "
            "stylistic move doing the most work is the absence of "
            "speech. Words would over-explain it. The cup is the "
            "argument. The conflict is small — a missed bus, a "
            "cold bench — but the theme is older and deeper: the "
            "kindness that occurs between strangers when no one "
            "is performing, and the way that small, deliberate "
            "wordlessness can communicate more than dialogue. "
            "*'She admitted, silently, that the universe had "
            "designed this evening for her,'* the narrator tells "
            "us. The *silently* matters. By the time the warm cup "
            "moves across the bench, that silence has been earned. "
            "The story trusts that we will hear it.*"
        ),
        "reflect": [
            "I can identify protagonist arc, theme, narrator stance, one stylistic move.",
            "I can use participle clauses for concise narrative.",
            "I can write a 250-word literary essay.",
        ],
        "pitfalls": [
            "Dangling participle: *Walking home, the rain "
            "started.* → ✗ (the rain wasn't walking).",
            "Don't overload: 3 participle clauses per page is "
            "generous.",
            "Don't summarise plot — analyse moves.",
        ],
        "further": [
            "The New Yorker — *The Writer's Voice* podcast.",
            "Granta — short fiction archive.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"Walking home, she heard the bus pull away two "
            "minutes early. The shelter was empty except for an "
            "old man with a paper cup. Having noticed her, he slid "
            "the cup toward her without speaking. The cup was full "
            "of warm tea.\"\n\n"
            "1. When was the bus: ___ . 2. Other person: ___ . 3. "
            "His action: ___ . 4. Cup's contents: ___ ."
        ),
        "exam_reading": (
            "Read the *Late Bus, Cold Bench* extract above.\n\n"
            "1. Setting: ___ . 2. The narrator's silent admission: "
            "___ . 3. What the man does: ___ . 4. What he does "
            "NOT do: ___ ."
        ),
        "exam_use": (
            "**Build a participle clause.**\n\n"
            "1. (walk home / she / think) → ___\n"
            "2. (tire by the day / she / sit) → ___\n"
            "3. (having notice her / he / slide / cup) → ___\n"
            "4. (read the line / the class / fall silent) → ___"
        ),
        "exam_writing": (
            "Write 250 words: a literary essay on the *Late Bus, "
            "Cold Bench* extract. Use 3 participle clauses + 1 "
            "quote."
        ),
        "exam_keys": [
            "**T1.** 2 minutes early; old man with paper cup; slid cup toward her without speaking; warm tea.",
            "**T2.** empty plaza, late evening, cold bench shelter; the universe had designed this evening for her; an old man slides his warm tea toward her in silence; speak.",
            "**T3.** *Walking home, she thought. Tired by the day, she sat. Having noticed her, he slid the cup. Reading the line, the class fell silent.*",
            "**T4.** Open.",
        ],
    },
    {
        "n": 7, "slug": "mediation-feature-article",
        "title": "Mediation: A German Feature Article",
        "skills": ["mediation", "writing", "language_awareness"],
        "bp": [
            "3.3.1 Soziokulturelles Orientierungswissen / Themen",
            "3.3.3.5 Schreiben",
            "3.3.3.6 Sprachmittlung",
            "3.3.3.7 Verfügen über sprachliche Mittel – Wortschatz",
        ],
        "objectives": [
            "I can mediate a 250-word German feature article into 8 English sentences.",
            "I can preserve voice and register; mark hedged claims; drop ceremony.",
            "I can use 8 reporting verbs.",
        ],
        "leadin": (
            "Maja's German aunt forwarded a feature article from a "
            "national paper about a small-town mayor who had "
            "rebuilt the local library on a near-zero budget. "
            "Maja's English-speaking pen-pal in Toronto, who is "
            "studying public administration, asked for a real "
            "summary, not a textbook one."
        ),
        "activate": (
            "**Voice scan.** Slide shows three lines from the German "
            "source. Mark each as *fact / opinion / colour*."
        ),
        "input_blocks": [
            ("Source — *German feature article (excerpt)*",
             "*Bürgermeisterin Anna Vogel hat ihre kleine Gemeinde, "
             "deren Bibliothek seit Jahren geschlossen war, mit "
             "einem unkonventionellen Plan zurück auf die Karte "
             "gebracht. Statt auf große Zuschüsse zu warten, "
             "organisierte sie eine Reihe von Sonntags-Workshops, "
             "in denen Bewohner gespendete Bücher sortierten und "
             "Regale bauten. \"Ich habe nicht erwartet, dass es "
             "funktioniert,\" gab Vogel zu, \"aber die Leute kamen "
             "zuverlässig.\" Die neue Bibliothek wurde nach acht "
             "Monaten eröffnet. Kritiker werfen ihr vor, das Modell "
             "sei nicht skalierbar.*"),
            ("Mediation — feature-article moves",
             "*Voice* — keep the speaker's voice via reported "
             "speech with the right verb (*admitted, claimed, "
             "added, argued*).\n"
             "*Register* — match the addressee. A peer-message "
             "drops the *Bürgermeisterin* honorifics; a public-"
             "admin reader keeps role + name.\n"
             "*Hedge* — preserve the journalist's hedging "
             "(*Critics argue …*) without inventing certainty."),
            ("Reporting verbs (extended)",
             "*to admit, to claim, to argue, to add, to confirm, "
             "to deny, to point out, to stress, to note, to "
             "concede, to dismiss, to maintain.*"),
        ],
        "practise_g": [
            "1. Match German verb → English: zugeben → ?, "
            "behaupten → ?, hinzufügen → ?, abstreiten → ?",
            "2. Choose the most accurate verb for: *Vogel said: "
            "'I didn't expect it to work, but people came.'*",
        ],
        "practise_m": [
            "3. Build a 6-sentence English mediation of the source "
            "above.",
        ],
        "answer_g": (
            "1. admit / claim / add / deny.\n"
            "2. *admitted* (it carries the surprise that *said* "
            "would lose)."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Mediation, 8 sentences.** Read the German source "
            "above. Write 8 English sentences for an English-"
            "speaking public-administration student. Preserve "
            "voice + use 5 reporting verbs."
        ),
        "produce_sample": (
            "*Hi Jordan, here's the gist of that feature on "
            "small-town public administration. Mayor Anna Vogel "
            "rebuilt her town's library — closed for years — with "
            "a near-zero budget. Rather than waiting for grants, "
            "she organised a series of Sunday workshops in which "
            "residents sorted donated books and built shelves "
            "themselves. Vogel admitted that she hadn't expected "
            "the plan to work; she added, with some surprise, that "
            "people had shown up reliably. The library opened "
            "eight months later. Critics argue, however, that the "
            "model is not scalable beyond small towns. The article "
            "stresses that Vogel doesn't claim it is — only that "
            "it worked here. The reporting tone is admiring but "
            "cautious.*"
        ),
        "reflect": [
            "I can mediate a feature article into 8 English sentences.",
            "I can preserve voice and register.",
            "I can use 5 reporting verbs accurately.",
        ],
        "pitfalls": [
            "*sagte* automatically translated as *said* — pick the "
            "verb that carries the speaker's stance.",
            "Carrying *Bürgermeisterin* into peer-talk → use *Mayor "
            "Vogel* or *Anna Vogel* depending on register.",
            "Inventing the journalist's certainty by dropping the "
            "hedge.",
        ],
        "further": [
            "Goethe-Institut — Sprachmittlungs-Beispielaufgaben "
            "Oberstufe.",
            "The Atlantic — *CityLab* features for register "
            "comparison.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"Bürgermeisterin Vogel rebuilt her town's library "
            "with a near-zero budget. She organised Sunday "
            "workshops in which residents sorted books and built "
            "shelves. She admitted she hadn't expected it to work. "
            "Critics argue the model is not scalable.\"\n\n"
            "1. Project: ___ . 2. Method: ___ . 3. Vogel admitted: "
            "___ . 4. Critics' view: ___ ."
        ),
        "exam_reading": (
            "Read the German source above.\n\n"
            "1. Mayor's name: ___ . 2. Project length: ___ . 3. "
            "Vogel's quoted line: ___ . 4. Critics' line: ___ ."
        ),
        "exam_use": (
            "**Choose the right reporting verb.**\n\n"
            "1. Vogel ___ that she had not expected it to work. "
            "(admitted)\n"
            "2. Critics ___ that the model is not scalable. "
            "(argue)\n"
            "3. The article ___ that residents came reliably. "
            "(notes)\n"
            "4. Vogel did not ___ that the model is universal. "
            "(claim)"
        ),
        "exam_writing": (
            "Mediate: write 8 English sentences from the source "
            "for a public-administration student. Use 5 reporting "
            "verbs."
        ),
        "exam_keys": [
            "**T1.** rebuild closed library; near-zero budget, Sunday workshops with residents sorting books / building shelves; she hadn't expected it to work but people came reliably; not scalable.",
            "**T2.** Anna Vogel; 8 months; *I didn't expect it to work, but people came reliably*; *the model is not scalable*.",
            "**T3.** admitted / argue / notes / claim.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 8, "slug": "science-and-society",
        "title": "Science and Society",
        "skills": ["reading", "writing", "intercultural"],
        "bp": [
            "3.3.1 Soziokulturelles Orientierungswissen / Themen",
            "3.3.3.2 Leseverstehen",
            "3.3.3.5 Schreiben",
            "3.3.3.7 Verfügen über sprachliche Mittel – Wortschatz",
            "3.3.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can read a short popular-science article and identify the main finding and one limitation.",
            "I can use vocabulary of scientific reasoning (*hypothesis, control group, sample size, peer review*).",
            "I can write a 220-word science-and-society reflection.",
        ],
        "leadin": (
            "Maja read a popular-science article about a four-day "
            "school week trial in a small Belgian district. Test "
            "scores were unchanged. Pupil well-being scores were "
            "higher. Cost savings were real. *And the catch?* Maja "
            "wrote in the margin. Two paragraphs later: *the "
            "Friday childcare problem*."
        ),
        "activate": (
            "**Question scan.** With your partner, write three "
            "policy-and-science questions you would actually want "
            "answered. Compare with another pair."
        ),
        "input_blocks": [
            ("Reading — *Four Days, Five Lessons*",
             "*A two-year trial of a four-day school week in a "
             "small Belgian district found test scores unchanged, "
             "pupil well-being scores higher, and modest cost "
             "savings. The trial included 14 schools, with a "
             "matched control group of 14 nearby schools. The "
             "results were peer-reviewed and published in 2027. "
             "The study notes one important limitation: many "
             "families struggled to arrange childcare for the "
             "extra Friday, and the burden fell unevenly on "
             "lower-income parents. The authors caution against "
             "scaling up before this is solved.*"),
            ("Vocabulary — scientific reasoning",
             "*hypothesis, variable, control group, sample size, "
             "peer review, replication, statistical significance, "
             "confidence interval, limitation, scaling, "
             "generalisability.*"),
        ],
        "practise_g": [
            "1. Match: control group → comparison; peer review → "
            "expert check; replication → re-running. (T / F)",
            "2. T or F from text: 14 trial schools, 14 control "
            "schools, peer-reviewed, no limitations.",
        ],
        "practise_m": [
            "3. Build 4 sentences using science-of-evidence "
            "vocabulary about the four-day school week trial.",
        ],
        "answer_g": (
            "1. all true.\n"
            "2. T, T, T, F (the study notes the childcare "
            "limitation)."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Reflection, 220 words.** Take a position on "
            "whether you would support a four-day school week "
            "trial in your area. Use 4 scientific-reasoning terms + "
            "2 hedges + 1 *despite* / *given that*."
        ),
        "produce_sample": (
            "*A two-year trial of a four-day school week in a "
            "small Belgian district found test scores unchanged, "
            "well-being higher, and modest cost savings. The trial "
            "included 14 schools and a matched control group. The "
            "results, peer-reviewed in 2027, are encouraging but "
            "specific to that context. The study notes one "
            "limitation that I take seriously: many families "
            "struggled to arrange childcare for the extra Friday, "
            "and the burden fell unevenly on lower-income parents. "
            "Given that the well-being gains depend on what "
            "happens on Friday, and not only on what happens "
            "Monday-to-Thursday, scaling up before this is solved "
            "would risk turning a class-blind reform into a class-"
            "biased one. Despite my interest in the model, I "
            "would not support a trial in my area until two "
            "things are in place: a publicly-funded Friday "
            "childcare option, and a generalisability check — a "
            "second trial in a context closer to ours. The "
            "authors' caution is the right one. Replication and "
            "policy-design need to come together; otherwise we "
            "risk borrowing the result without the conditions that "
            "produced it.*"
        ),
        "reflect": [
            "I can identify a main finding and one limitation in a popular-science article.",
            "I can use 6 scientific-reasoning terms.",
            "I can write a 220-word science-and-society reflection.",
        ],
        "pitfalls": [
            "*proves* in science writing → almost always wrong; "
            "*supports / is consistent with* is safer.",
            "*Sample size* of 14 schools is small — note before "
            "claiming generalisability.",
            "Don't borrow the result without the conditions that "
            "produced it.",
        ],
        "further": [
            "BBC Science Focus — accessible articles.",
            "Nature — *News & Views* short-form.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"A two-year trial of a four-day school week in a "
            "small Belgian district found test scores unchanged, "
            "well-being higher, and modest cost savings. The "
            "trial included 14 schools with a matched control "
            "group. The study notes one limitation: families "
            "struggled with Friday childcare.\"\n\n"
            "1. Length: ___ . 2. Three findings: ___ . 3. Sample: "
            "___ . 4. Limitation: ___ ."
        ),
        "exam_reading": (
            "Read the *Four Days, Five Lessons* extract above.\n\n"
            "1. Three findings: ___ . 2. Sample size: ___ . 3. "
            "Year of publication: ___ . 4. Authors' warning: ___ ."
        ),
        "exam_use": (
            "**Insert scientific-reasoning vocabulary.**\n\n"
            "1. The ___ for this study was 14 schools.\n"
            "2. The ___ included 14 nearby schools as comparison.\n"
            "3. The results were ___ in 2027.\n"
            "4. The authors caution against ___ before the "
            "limitation is solved."
        ),
        "exam_writing": (
            "Write 220 words: a science-and-society reflection on "
            "the trial. Use 4 scientific-reasoning terms."
        ),
        "exam_keys": [
            "**T1.** 2 years; test scores unchanged / well-being higher / modest cost savings; 14 schools + 14-school control; Friday childcare burden on lower-income parents.",
            "**T2.** test scores unchanged / well-being higher / modest cost savings; 14 schools (with 14-school control); 2027; do not scale up before childcare burden is solved.",
            "**T3.** sample size / control group / peer-reviewed / scaling up.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 9, "slug": "youth-protest-movements",
        "title": "Youth Protest Movements",
        "skills": ["reading", "speaking", "intercultural"],
        "bp": [
            "3.3.1 Soziokulturelles Orientierungswissen / Themen",
            "3.3.2 Interkulturelle kommunikative Kompetenz",
            "3.3.3.2 Leseverstehen",
            "3.3.3.3 Sprechen – an Gesprächen teilnehmen",
            "3.3.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can read a comparative text on two youth movements and identify their tactics, demands, and outcomes.",
            "I can use cleft-sentence emphasis (*it is precisely the demand that …*).",
            "I can hold a 5-minute panel-style discussion in formal English.",
        ],
        "leadin": (
            "Maja's class compared two youth movements: a climate "
            "school-strike movement of the late 2010s and a "
            "housing-rights movement that began in Lisbon in "
            "2024. Same age range, similar visibility online, very "
            "different policy outcomes. Mr. Yilmaz framed the "
            "question: *what made one of them legible to the "
            "system, and the other not?*"
        ),
        "activate": (
            "**Movement-mapping scan.** With your partner, list "
            "two youth movements you have heard of in the past "
            "five years and one tactic each used."
        ),
        "input_blocks": [
            ("Reading — *Two Youth Movements, Compared*",
             "*The school-strike climate movement of 2018-2020 "
             "drew millions of young people into weekly walk-outs "
             "across more than 130 countries. Its central demand "
             "— that governments listen to climate scientists — "
             "was clear, and its tactic — visible absence — was "
             "easily understood by the public. The Lisbon housing "
             "movement of 2024-2026, by contrast, used "
             "occupations of empty buildings and detailed policy "
             "papers. Its demands were narrower and harder to "
             "summarise. It is precisely the legibility of the "
             "first movement, some commentators argue, that made "
             "it useful to politicians; and precisely the "
             "specificity of the second that has produced sharper "
             "policy results.*"),
            ("Grammar — cleft-sentence emphasis",
             "**It is/was X that/who …** structure highlights one "
             "element.\n"
             "- *It is precisely the legibility of the first "
             "movement that made it useful.*\n"
             "- *It was the specificity that produced sharper "
             "results.*\n"
             "- *What made the difference was the specificity.*"),
        ],
        "practise_g": [
            "1. Build a cleft sentence: emphasise *the legibility* "
            "in *the legibility of the first movement made it "
            "useful*.",
            "2. T or F from text: school-strike was in 130+ "
            "countries; Lisbon housing demands were broad; "
            "specificity produced sharper results.",
        ],
        "practise_m": [
            "3. Build 4 cleft sentences emphasising different "
            "elements of the same fact.",
        ],
        "answer_g": (
            "1. *It was precisely the legibility of the first "
            "movement that made it useful.*\n"
            "2. T, F (narrower), T."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Panel-style discussion (5 min).** Groups of 4. Each "
            "speaker delivers a 60-second opening on: *what makes "
            "a youth movement effective?* Use 1 cleft + 1 hedge + "
            "1 specific example. Other speakers ask 1 follow-up."
        ),
        "produce_sample": (
            "*What makes a youth movement effective is, I would "
            "argue, the legibility of its central demand. It is "
            "precisely when a movement can summarise itself in one "
            "sentence — *listen to climate scientists* — that the "
            "public can stand behind it without having to do "
            "homework. However, this comes at a cost. The Lisbon "
            "housing movement of 2024 was less legible; its "
            "demands were narrower and required several pages of "
            "explanation. And yet, the available evidence "
            "suggests, it was the specificity of those demands "
            "that produced sharper policy results within two "
            "years. Both kinds of movement matter. The lesson, "
            "perhaps, is that legibility wins attention, while "
            "specificity wins the policy.*"
        ),
        "reflect": [
            "I can identify tactics, demands, and outcomes of two youth movements.",
            "I can use cleft-sentence emphasis.",
            "I can hold a 5-minute panel-style discussion.",
        ],
        "pitfalls": [
            "Romanticising movements without naming a specific "
            "tactic.",
            "Cleft overload — one per paragraph is enough.",
            "Don't confuse public visibility with policy "
            "outcome.",
        ],
        "further": [
            "BBC News — youth-movement profiles.",
            "The Conversation — academic-leaning analysis.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"The school-strike movement drew millions across "
            "more than 130 countries. Its demand — that "
            "governments listen to climate scientists — was clear "
            "and its tactic, visible absence, was easily "
            "understood. The Lisbon housing movement used "
            "building occupations and detailed policy papers; its "
            "demands were narrower.\"\n\n"
            "1. School-strike scale: ___ . 2. School-strike demand: "
            "___ . 3. Lisbon tactic: ___ . 4. Lisbon demands: ___ ."
        ),
        "exam_reading": (
            "Read the *Two Youth Movements* extract above.\n\n"
            "1. Years of school-strike: ___ . 2. School-strike "
            "tactic: ___ . 3. Lisbon years + tactic: ___ . 4. The "
            "argument about legibility vs. specificity: ___ ."
        ),
        "exam_use": (
            "**Build a cleft sentence emphasising the underlined "
            "phrase.**\n\n"
            "1. *the legibility* of the first movement made it "
            "useful → ___\n"
            "2. *the specificity* of the second produced sharper "
            "results → ___\n"
            "3. *the public* eventually decided the issue → ___\n"
            "4. *the writers* were responsible for the framing → "
            "___"
        ),
        "exam_writing": (
            "Write 220 words: a comparison of two youth movements "
            "with one cleft + 2 hedges."
        ),
        "exam_keys": [
            "**T1.** millions across 130+ countries; listen to climate scientists; building occupations + policy papers; narrower / harder to summarise.",
            "**T2.** 2018-2020; visible absence (school walk-outs); 2024-2026 / building occupations + policy papers; legibility wins attention, specificity wins policy.",
            "**T3.** *It was the legibility … that made it useful. It was the specificity … that produced sharper results. It was the public that decided. It was the writers that were responsible.*",
            "**T4.** Open.",
        ],
    },
    {
        "n": 10, "slug": "a-short-novel",
        "title": "A Short Novel",
        "skills": ["reading", "writing", "language_awareness"],
        "bp": [
            "3.3.1 Soziokulturelles Orientierungswissen / Themen",
            "3.3.3.2 Leseverstehen",
            "3.3.3.5 Schreiben",
            "3.3.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can read three chapters of a contemporary short novel and identify protagonist arc, setting, theme, and one stylistic move.",
            "I can write a 300-word literary essay with two quotes.",
            "I can use varied register markers (formal *however / nevertheless* alongside everyday *though, still, anyway*).",
        ],
        "leadin": (
            "The class read three chapters of an imagined "
            "contemporary novel called *The Slow Hour*. Six "
            "characters, one bus stop, three weeks. By the end of "
            "chapter three, half the class had decided it was a "
            "love story; the other half, a small civic tragedy; "
            "Mr. Yilmaz said it was *both, depending on which "
            "character you read most carefully*."
        ),
        "activate": (
            "**Three-chapter sketch.** With your partner, draw "
            "the arc across chapters: *what changes for whom*."
        ),
        "input_blocks": [
            ("Reading — *The Slow Hour*, ch. 3 (extract)",
             "*By the third week, the bus stop had become a small "
             "kingdom. The same six people, every weekday morning, "
             "in the same approximate order. Anya, who could "
             "predict each arrival down to the second, had stopped "
             "predicting; the predictability itself had become the "
             "comfort. Nevertheless, on Wednesday, one of the six "
             "was missing. Anya did not yet know that the missing "
             "person was the one who had, without telling anyone, "
             "been keeping the kingdom together.*"),
            ("Register variety",
             "*Formal / academic:* however, nevertheless, "
             "moreover, furthermore, indeed.\n"
             "*Everyday / narrative:* though, still, anyway, "
             "either way, mind you.\n"
             "*Use both with intent.* Academic register fits an "
             "essay claim; narrative register fits a quoted "
             "voice."),
        ],
        "practise_g": [
            "1. Match: however → formal; though → everyday; "
            "nevertheless → formal.",
            "2. Choose register: *(in a literary essay)* → ___ ; "
            "*(in dialogue)* → ___ .",
        ],
        "practise_m": [
            "3. Build 3 essay sentences (formal) + 3 narrative "
            "sentences (everyday).",
        ],
        "answer_g": (
            "1. all true.\n"
            "2. *however / though.*"
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Literary essay, 300 words.** Read the extract. "
            "Answer: *Who is Anya? What is the arc? What is the "
            "theme? Which two stylistic moves do the most work?* "
            "Use 2 quotes + 1 cleft + 2 academic register markers."
        ),
        "produce_sample": (
            "*By chapter three of *The Slow Hour*, the bus stop "
            "has, in the narrator's words, *become a small "
            "kingdom*. The repetition of arrivals — *the same six "
            "people, every weekday morning, in the same "
            "approximate order* — is the novel's quietly central "
            "image. It is precisely the predictability of the "
            "stop, the narrator suggests, that has made it bearable. "
            "Anya is the protagonist whose interior arc the author "
            "is most carefully tracking. She has stopped predicting "
            "the arrivals, not because the rhythm has changed, but "
            "because she has finally trusted it. Nevertheless, on "
            "the Wednesday of the third week, one of the six is "
            "missing. The chapter ends on the reveal of who that "
            "person was: not the most visible of the six, but the "
            "one who had been, *without telling anyone*, holding "
            "the kingdom together. The two stylistic moves doing "
            "the most work are the controlled use of "
            "*nevertheless* and the late, dropped fact of the "
            "missing person's role. The first gives the chapter "
            "its essayistic gravity; the second is what turns the "
            "predictability of the morning routine into something "
            "fragile and real. The theme, I think, is the "
            "invisibility of the people who keep small communities "
            "running, and the moral weight that lands on a "
            "narrator only when those people stop. Indeed, the "
            "novel uses an ordinary bus stop to ask a serious civic "
            "question.*"
        ),
        "reflect": [
            "I can identify protagonist arc, setting, theme, two stylistic moves.",
            "I can use formal and everyday register markers with intent.",
            "I can write a 300-word literary essay with two quotes.",
        ],
        "pitfalls": [
            "Mixing register without intent — *however* in dialogue "
            "or *anyway* in an essay can flatten both.",
            "Don't summarise plot — analyse moves.",
            "Two quotes per essay is plenty; more reads as "
            "padding.",
        ],
        "further": [
            "London Review of Books — short essays.",
            "The Paris Review — *Art of Fiction* interviews.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"By the third week, the bus stop had become a small "
            "kingdom. The same six people, every weekday morning. "
            "Anya had stopped predicting each arrival; the "
            "predictability itself had become the comfort. "
            "Nevertheless, on Wednesday, one was missing.\"\n\n"
            "1. Time: ___ . 2. Number of regulars: ___ . 3. Anya's "
            "shift: ___ . 4. Wednesday event: ___ ."
        ),
        "exam_reading": (
            "Read the *Slow Hour* ch. 3 extract above.\n\n"
            "1. Setting: ___ . 2. Anya's relationship to the "
            "rhythm: ___ . 3. The absent person's hidden role: "
            "___ . 4. The chapter's reveal: ___ ."
        ),
        "exam_use": (
            "**Build the cleft + register match.**\n\n"
            "1. Cleft on *the predictability*: → ___\n"
            "2. Cleft on *the missing person*: → ___\n"
            "3. Choose: *however / though* in *(an essay sentence)* "
            "→ ___\n"
            "4. Choose: *however / though* in *(a quoted line of "
            "dialogue)* → ___"
        ),
        "exam_writing": (
            "Write 300 words: a literary essay on the *Slow Hour* "
            "extract. Use 2 quotes + 1 cleft + 2 register markers."
        ),
        "exam_keys": [
            "**T1.** third week; six; stopped predicting — predictability became the comfort; one missing.",
            "**T2.** bus stop, third week of mornings; she stopped predicting because she had finally trusted the rhythm; the missing person had been keeping the kingdom together; the chapter ends on the reveal of that person's role.",
            "**T3.** *It was the predictability that had become the comfort. It was the missing person who had been keeping the kingdom together. however / though.*",
            "**T4.** Open.",
        ],
    },
    {
        "n": 11, "slug": "public-speaking-and-debate",
        "title": "Public Speaking and Debate",
        "skills": ["speaking", "listening", "language_awareness"],
        "bp": [
            "3.3.1 Soziokulturelles Orientierungswissen / Themen",
            "3.3.3.1 Hör-/Hörsehverstehen",
            "3.3.3.3 Sprechen – an Gesprächen teilnehmen",
            "3.3.3.4 Sprechen – zusammenhängendes monologisches Sprechen",
        ],
        "objectives": [
            "I can deliver a 4-minute argued speech with three movements.",
            "I can rebut one specific point and concede one gracefully.",
            "I can listen to a peer's speech and respond with one targeted argument.",
        ],
        "leadin": (
            "Maja's class is rehearsing for the school debate "
            "society. The motion: *This house would replace one "
            "written test per term with a project-based "
            "assessment.* The team in favour was, predictably, the "
            "one with the project-people. The team against was, "
            "less predictably, also the one with one project-"
            "person — Mr. Yilmaz had drawn names from a hat."
        ),
        "activate": (
            "**Argument scan.** With your partner, list 3 best "
            "arguments *for* and 3 *against* the motion. Mark each "
            "as *strong / mid / weak*."
        ),
        "input_blocks": [
            ("Speech — three movements (extended)",
             "1. **Frame** (45 sec): the motion in your own words "
             "+ why now.\n"
             "2. **Argument** (3 min): two points, each with one "
             "source / example, plus one anticipated counter and "
             "one specific rebuttal.\n"
             "3. **Close** (15 sec): one sentence + one ask.\n\n"
             "Plus 30 sec buffer."),
            ("Debate signposts (extended)",
             "**Opening:** *I'd like to argue / The motion before "
             "us …*\n"
             "**Listing:** *Firstly … Secondly … Lastly …*\n"
             "**Counter:** *My opponent will claim … / However, "
             "this misses … / In response, …*\n"
             "**Concession:** *I accept that … but …*\n"
             "**Closing:** *I urge you to support / oppose this "
             "motion.*"),
        ],
        "practise_g": [
            "1. Match phrase to function: *In response* → counter; "
            "*I accept that* → concession; *To summarise* → "
            "closing.",
            "2. Build a 3-line opening for *for* the motion.",
        ],
        "practise_m": [
            "3. Build a 4-minute argued speech outline (bullets) "
            "for or against the motion.",
        ],
        "answer_g": "1. all true. 2. Open.",
        "answer_m": "3. Open.",
        "produce": (
            "**Class debate (4 minutes per speaker).** Two teams "
            "of 4. Each speaker delivers a 4-minute argued "
            "speech. Listening team prepares one specific "
            "rebuttal per speaker. Moderator times strictly."
        ),
        "produce_sample": (
            "*The motion before us is that this house would "
            "replace one written test per term with a project-"
            "based assessment. I'd like to argue in favour. "
            "Firstly, project-based assessment captures skills "
            "that a written test cannot — research, design, "
            "presentation, and the management of one's own time. "
            "The available evidence — including a 2024 OECD review "
            "of 18 OECD countries — suggests modest improvements "
            "in transferable skill scores when project assessment "
            "is added to the mix. Secondly, project work tends to "
            "involve real audiences, which improves the writing. "
            "My opponent will claim, fairly, that fairness is "
            "harder to police across project formats. I accept "
            "that, but a clear marking rubric, agreed in advance, "
            "solves the lion's share of that problem. To "
            "summarise: replacing one test per term is moderate; "
            "the gain is real; the fairness concern is "
            "manageable. I urge you to support the motion.*"
        ),
        "reflect": [
            "I can deliver a 4-minute argued speech with three movements.",
            "I can rebut and concede with specifics.",
            "I can respond to a peer with a targeted argument.",
        ],
        "pitfalls": [
            "Reading flatly from a script.",
            "Generic rebuttal (*you're wrong*) — name the specific "
            "claim you reject.",
            "Concession without engagement.",
        ],
        "further": [
            "ESU (English-Speaking Union) — student debate "
            "footage.",
            "BBC Sounds — *Question Time* extracts.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"I'd like to argue in favour. Firstly, project-"
            "based assessment captures skills tests don't. Evidence "
            "from a 2024 OECD review suggests modest improvement. "
            "My opponent will claim fairness is harder. I accept "
            "that, but a clear rubric solves most of it. I urge "
            "you to support the motion.\"\n\n"
            "1. Stance: ___ . 2. Source: ___ . 3. Counter "
            "anticipated: ___ . 4. Concession-resolution: ___ ."
        ),
        "exam_reading": (
            "Read the sample speech above.\n\n"
            "1. Two arguments: ___ . 2. Source cited: ___ . 3. "
            "Counter + rebuttal: ___ . 4. Closing ask: ___ ."
        ),
        "exam_use": (
            "**Insert debate signpost.**\n\n"
            "1. ___ to argue in favour.\n"
            "2. ___ , project work captures wider skills.\n"
            "3. ___ , fairness is harder to police.\n"
            "4. ___ you to support the motion."
        ),
        "exam_writing": (
            "Write a 4-minute debate-speech script (~250 words) "
            "for or against any motion. Use 5 debate signposts."
        ),
        "exam_keys": [
            "**T1.** in favour; 2024 OECD review of 18 countries; fairness is harder; clear rubric, agreed in advance, solves most.",
            "**T2.** project skills + real audiences; 2024 OECD review; fairness — clear rubric solves most; *I urge you to support the motion*.",
            "**T3.** I'd like / Firstly / However / I urge.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 12, "slug": "year-review-toward-oberstufe",
        "title": "Year Review: Toward Oberstufe",
        "skills": ["writing", "speaking", "language_awareness"],
        "bp": [
            "3.3.1 Soziokulturelles Orientierungswissen / Themen",
            "3.3.3.4 Sprechen – zusammenhängendes monologisches Sprechen",
            "3.3.3.5 Schreiben",
            "3.3.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can compile an Oberstufe-readiness portfolio with 5 representative pieces.",
            "I can write a 300-word year reflection demonstrating wide grammar range.",
            "I can deliver a 4-minute portfolio talk with two quotes from my own writing.",
        ],
        "leadin": (
            "Mr. Yilmaz wrote on the board: *one folder, five "
            "pieces, one decision*. The class understood. The "
            "*decision* was the Oberstufe choice — Basisfach or "
            "Leistungsfach Englisch. Maja had decided. Half the "
            "class had decided. The other half were still reading "
            "leaflets, which is, Mr. Yilmaz said, *the right "
            "amount of patience for the wrong amount of "
            "time*."
        ),
        "activate": (
            "**Pick-five scan.** Open your folder. Pick five "
            "pieces. Label each: *proudest / surprised me / didn't "
            "work / would rewrite / connects to next year*."
        ),
        "input_blocks": [
            ("Portfolio structure (Oberstufe-readiness)",
             "1. **Cover sheet** (name, year, theme, intended "
             "Oberstufe path).\n"
             "2. **Five pieces** (one-line label each).\n"
             "3. **Reflection** (300 words: arc of the year, two "
             "specific moments of progress, one disappointment, "
             "one connection to Oberstufe).\n"
             "4. **Talk** (4 minutes; two quotes from your own "
             "writing).\n"
             "5. **Forward letter** (200 words to your Oberstufe "
             "self)."),
            ("Reflection — useful frames",
             "*At the start of Klasse 10 I … / By Christmas I had "
             "started to … / The piece that surprised me was … / "
             "The piece that didn't work taught me that … / The "
             "thread I want to keep going is … / Whichever path I "
             "choose, the most useful skill from this year is …*"),
        ],
        "practise_g": [
            "1. Build the five labels for your own folder.",
        ],
        "practise_m": [
            "2. Build a 7-line reflection draft using mixed "
            "tenses (past simple, past perfect, present perfect, "
            "future perfect, mixed conditional).",
        ],
        "answer_g": "Open.",
        "answer_m": "Open.",
        "produce": (
            "**Portfolio + 300-word reflection + 4-minute talk + "
            "200-word forward letter.** Submit the portfolio and "
            "deliver a 4-minute talk. Audience gives one feedback "
            "sentence."
        ),
        "produce_sample": (
            "*At the start of Klasse 10 I wrote in three modes: "
            "translated, formal, and quietly imitating other "
            "people. By Christmas I had started to write in a "
            "fourth mode that I would call *paying attention*. "
            "The piece I am proudest of is the *Late Bus, Cold "
            "Bench* essay, which taught me that the smallest "
            "stylistic moves often do the most analytical work. "
            "The piece that surprised me was the four-day school "
            "week reflection: I had not expected to find the "
            "limitation more interesting than the headline finding. "
            "If I had paid attention to the limitation earlier in "
            "the year, I would have written less confidently and "
            "more usefully. By the end of the Oberstufe I will "
            "have written somewhere between 30 and 50 essays "
            "longer than this one. The thread I want to keep going "
            "is *naming the limitation* — both in writing and in "
            "speaking. I have decided to take Englisch as a "
            "Leistungsfach. Whichever way the next two years go, "
            "the most useful skill from this year, I think, is "
            "the small repeated discipline of writing one careful "
            "paragraph rather than three confident ones. I owe "
            "that, mostly, to the slow lanes of Klasse 10.*"
        ),
        "reflect": [
            "I can compile a 5-piece Oberstufe-readiness portfolio.",
            "I can write a 300-word year reflection.",
            "I can deliver a 4-minute portfolio talk.",
        ],
        "pitfalls": [
            "Reading the talk verbatim.",
            "Generic claims (*I learned a lot*).",
            "Picking only the best five — the *didn't-work* slot "
            "matters.",
        ],
        "further": [
            "BBC Bitesize — *Reflective writing*.",
            "British Council — *Self-evaluation* materials.",
        ],
        "exam_listening": (
            "Listen twice to a portfolio talk.\n\n"
            "> \"At the start of Klasse 10 I wrote in three modes: "
            "translated, formal, and imitating others. By Christmas "
            "I had started a fourth mode I'd call *paying "
            "attention*. The piece I'm proudest of is *Late Bus, "
            "Cold Bench*. By the end of Oberstufe I will have "
            "written 30 to 50 longer essays. I am taking Englisch "
            "as a Leistungsfach.\"\n\n"
            "1. Three September modes: ___ . 2. Christmas: ___ . "
            "3. Proudest piece: ___ . 4. Decision: ___ ."
        ),
        "exam_reading": (
            "Read the reflection sample above.\n\n"
            "1. Four writing modes: ___ . 2. Most surprising "
            "piece + reason: ___ . 3. Lesson learnt: ___ . 4. "
            "Decision: ___ ."
        ),
        "exam_use": (
            "**Mixed grammar review.**\n\n"
            "1. By Christmas I __________ (start) a new mode. "
            "(past perfect)\n"
            "2. If I __________ (pay) attention earlier, I "
            "__________ (write) more carefully. (third)\n"
            "3. By the end of Oberstufe, I __________ (write) "
            "30-50 essays. (future perfect)\n"
            "4. The thread I want to keep going is ___ ."
        ),
        "exam_writing": (
            "Write 300 words: an Oberstufe-readiness reflection. "
            "Use 6 grammar points from Klasse 9 + 10."
        ),
        "exam_keys": [
            "**T1.** translated / formal / imitating; *paying attention*; *Late Bus, Cold Bench*; Leistungsfach Englisch.",
            "**T2.** translated, formal, imitating, paying attention; the four-day school week reflection — the limitation was more interesting than the headline; the small repeated discipline of writing one careful paragraph; Leistungsfach Englisch.",
            "**T3.** had started / had paid — would have written / will have written / *naming the limitation*.",
            "**T4.** Open.",
        ],
    },
]


UNIT_TPL = """---
title: "Unit {n} — {title}"
subtitle: "Track E · Klasse 10 · Niveau E"
niveau: "E"
klassenstufe: 10
track: "e"
unit_nr: {n}
slug: "{slug}"
bildungsplan:
{bp_yaml}
skills_focus:
{skills_yaml}
format:
  html: {{ toc: true, toc-depth: 3 }}
  revealjs:
    output-file: "unit{nn}_slides.html"
    theme: [default, ../../assets/slides.scss]
    slide-number: c/t
    progress: true
    scrollable: true
    transition: none
---

::: {{.callout-note}}
**Template:** Activate → Input → Practise → Produce → Reflect.\\
**Niveau:** E. class test (Klassenarbeit) at Niveau E (45 BE).
:::

{{{{< downloads >}}}}

## Learning objectives

{objectives}

## curriculum framework (Bildungsplan) alignment

{bp_bullets}

(Source: <https://www.bildungsplaene-bw.de/,Lde/LS/BP2016BW/ALLG/SEK1/E1>)

## Lead-in story

{leadin}

## 1. Activate

{activate}

## 2. Input

{input_sections}

## 3. Practise

### Niveau E — controlled

{practise_g}

### Niveau E — productive

{practise_m}

::: {{.callout-tip collapse="true" title="Answer key"}}
**Controlled.** {answer_g}

**Productive.** {answer_m}
:::

## 4. Produce

{produce}

### Sample

{produce_sample}

## 5. Reflect

{reflect_list}

**One thing in your notebook:** *Write one sentence using something you learned in this Unit.*

## Exam example

{{{{< include _unit{nn}_{slug}_exam_body.qmd >}}}}

## Downloads

{{{{< downloads >}}}}

::: {{.notes}}
**Slide deck timing.** 45 minutes total. Lead-in 4 min · Activate
5 min · Input 14 min · Practise 8 min · Produce 11 min · Reflect 3 min.

**Differentiation.** Below Niveau E: scaffold card. Above Niveau E /
into Oberstufe: extension prompt linking to Klasse 11
(Basisfach / Leistungsfach choice).
:::

## Common pitfalls

{pitfalls}

## Further reading / listening

{further}
"""

EXAM_BODY_TPL = """::: {{.callout-warning icon=false title="class test (Klassenarbeit) — Niveau E (45 minutes)"}}
**Time.** 45 minutes. **Total.** 45 points.
:::

### Task 1 — Listening (10 BE)

{exam_listening}

### Task 2 — Reading (12 BE)

{exam_reading}

### Task 3 — Use of English (10 BE)

{exam_use}

### Task 4 — Writing (13 BE)

{exam_writing}

::: {{.callout-tip collapse="true" title="Answer key"}}
{exam_keys}
:::

::: {{.callout-tip collapse="true" title="grading scale (Notenschlüssel) (von 45)"}}
| 42–45 | 1 | 36–41 | 2 | 30–35 | 3 |
| 22–29 | 4 | 13–21 | 5 |  0–12 | 6 |
:::
"""

EXAM_WRAP_TPL = """---
title: "class test (Klassenarbeit) — Unit {n}: {title}"
subtitle: "Track E · Klasse 10 · Niveau E · 45 Minuten"
author: "S. Le Boulanger"
niveau: "E"
klassenstufe: 10
track: "e"
unit_nr: {n}
slug: "{slug}"
format:
  pdf:
    documentclass: scrartcl
    papersize: a4
    fontsize: 11pt
    geometry: [margin=22mm]
    include-in-header: ["../../_includes/_exam.tex"]
    keep-tex: false
---

# class test (Klassenarbeit) — Unit {n}: {title}

**Track E · Klasse 10 · Niveau E · 45 Minuten**

{{{{< include _unit{nn}_{slug}_exam_body.qmd >}}}}
"""


def emit() -> None:
    COURSE.mkdir(parents=True, exist_ok=True)
    for u in UNITS:
        nn = f"{u['n']:02d}"
        bp_yaml = "\n".join(f'  - "{c}"' for c in u["bp"])
        skills_yaml = "\n".join(f"  - {s}" for s in u["skills"])
        objectives = "\n".join(f"- *{o}*" for o in u["objectives"])
        bp_bullets = "\n".join(f"- **{c}**" for c in u["bp"])
        input_sections = "\n\n".join(
            f"### {h}\n\n{b}" for h, b in u["input_blocks"]
        )
        practise_g = "\n".join(u["practise_g"])
        practise_m = "\n".join(u["practise_m"])
        reflect_list = "\n".join(f"- [ ] {r}" for r in u["reflect"])
        pitfalls = "\n".join(f"- {p}" for p in u["pitfalls"])
        further = "\n".join(f"- {f}" for f in u["further"])

        unit_md = UNIT_TPL.format(
            n=u["n"], nn=nn, slug=u["slug"], title=u["title"],
            bp_yaml=bp_yaml, skills_yaml=skills_yaml,
            objectives=objectives, bp_bullets=bp_bullets,
            leadin=u["leadin"], activate=u["activate"],
            input_sections=input_sections,
            practise_g=practise_g, practise_m=practise_m,
            answer_g=u["answer_g"], answer_m=u["answer_m"],
            produce=u["produce"], produce_sample=u["produce_sample"],
            reflect_list=reflect_list,
            pitfalls=pitfalls, further=further,
        )
        exam_body_md = EXAM_BODY_TPL.format(
            exam_listening=u["exam_listening"],
            exam_reading=u["exam_reading"],
            exam_use=u["exam_use"],
            exam_writing=u["exam_writing"],
            exam_keys="\n".join(u["exam_keys"]),
        )
        exam_wrap_md = EXAM_WRAP_TPL.format(
            n=u["n"], nn=nn, slug=u["slug"], title=u["title"],
        )

        (COURSE / f"unit{nn}_{u['slug']}.qmd").write_text(unit_md, encoding="utf-8")
        (COURSE / f"_unit{nn}_{u['slug']}_exam_body.qmd").write_text(exam_body_md, encoding="utf-8")
        (COURSE / f"unit{nn}_{u['slug']}_exam.qmd").write_text(exam_wrap_md, encoding="utf-8")

    print(f"Wrote {len(UNITS) * 3} files for Track E Klasse 10.")


if __name__ == "__main__":
    emit()
