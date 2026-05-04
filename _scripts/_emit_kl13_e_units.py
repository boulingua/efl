"""Batch-emit Track E Klasse 13 — all 12 Units (Abitur year).

Klasse 13 voice: exam-grade and issue-framed. Cast: *public voices
and contemporary writers* — the year is structured around the
Abitur (school-leaving examination). curriculum framework
(Bildungsplan) prefixes 3.4 (advanced course / Leistungsfach) +
3.5 (basic course / Basisfach).

Three Units (7-9) are dedicated to the schriftliches Abitur — one
per Abitur-task type (Comprehension, Analysis, Composition).
Unit 10 is a full-format Kommunikationsprüfung (oral exam). Unit
12 is the year-end handover, including a 300-word forward letter
to the post-Abitur self.
"""
from __future__ import annotations
import pathlib

REPO = pathlib.Path(__file__).resolve().parent.parent
COURSE = REPO / "track_e_kl13" / "units"

UNITS = [
    {
        "n": 1, "slug": "globalisation-and-the-self",
        "title": "Globalisation and the Self",
        "skills": ["reading", "writing", "intercultural"],
        "bp": [
            "3.4.1 / 3.5.1 Soziokulturelles Orientierungswissen / Themen",
            "3.4.2 / 3.5.2 Interkulturelle kommunikative Kompetenz",
            "3.4.3.2 / 3.5.3.2 Leseverstehen",
            "3.4.3.5 / 3.5.3.5 Schreiben",
            "3.4.4 / 3.5.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can read essays on identity-under-globalisation (Sen, Appiah, Lahiri) and identify each writer's framework.",
            "I can use the vocabulary of cosmopolitanism (*rooted cosmopolitanism, hospitality, situated identity, contributory belonging*).",
            "I can write a 400-word essay developing my own position on identity-and-globalisation.",
        ],
        "leadin": (
            "Klasse 13 opens with three short essay extracts: "
            "Amartya Sen on plural identity (*Identity and "
            "Violence*, 2006); Kwame Anthony Appiah on rooted "
            "cosmopolitanism (*Cosmopolitanism: Ethics in a World "
            "of Strangers*, 2006); Jhumpa Lahiri on writing in a "
            "second language (*In Other Words*, 2015 / 2016 EN). "
            "The class agreed that all three are arguing against "
            "the same cartoon — the cartoon of identity as a "
            "single sticker."
        ),
        "activate": (
            "**Identity-frame scan.** With your partner, list 3 "
            "ways a person you know holds two identities at "
            "once. Mark each as *rooted / hyphenated / "
            "shifting*."
        ),
        "input_blocks": [
            ("Reading — three frames (paraphrased)",
             "*Sen — plural identity:* No human being is reducible "
             "to a single belonging. The illusion of singular "
             "identity is the precondition of identitarian "
             "violence.\n\n"
             "*Appiah — rooted cosmopolitanism:* We can be "
             "loyal to a particular place AND committed to a "
             "general moral horizon at the same time. Both "
             "loyalties are real.\n\n"
             "*Lahiri — language and self:* To write in a "
             "second language is to undertake a small, "
             "voluntary self-displacement that produces a "
             "third version of yourself."),
            ("Vocabulary — cosmopolitanism",
             "*plural identity, rooted cosmopolitanism, "
             "hospitality, the moral horizon, situated "
             "identity, contributory belonging, "
             "essentialism, identitarian, the politics of "
             "recognition.*"),
        ],
        "practise_g": [
            "1. Match: Sen → plural identity; Appiah → rooted "
            "cosmopolitanism; Lahiri → language-as-self.",
            "2. T or F: rooted cosmopolitanism rejects local "
            "loyalty; plural identity is the same as multiple "
            "passports.",
        ],
        "practise_m": [
            "3. Build 4 sentences applying cosmopolitan "
            "vocabulary to one of the three frames.",
        ],
        "answer_g": (
            "1. all true.\n"
            "2. F (it accepts both local and general loyalties), "
            "F (plural identity is conceptual, not "
            "documentary)."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Position essay, 400 words.** Argue your own "
            "position on identity-and-globalisation. Use 5 "
            "cosmopolitan vocabulary terms + 6 academic "
            "discourse markers + 1 cleft + 1 integrated quote "
            "from one of the three writers."
        ),
        "produce_sample": (
            "*The most useful framework I have read this year for "
            "thinking about identity-under-globalisation is Kwame "
            "Anthony Appiah's *rooted cosmopolitanism*, partly "
            "because it refuses the easy choice between local "
            "loyalty and a general moral horizon. The available "
            "evidence — anthropological, historical, and personal "
            "— suggests that human beings have, in practice, "
            "always held more than one belonging at once. "
            "Accordingly, what Sen calls the *illusion of "
            "singular identity* is, in my reading, less a mistake "
            "than a political construction; the illusion is "
            "useful to actors who require an enemy. By contrast, "
            "Appiah's frame asks something harder: to hold local "
            "and general loyalties simultaneously without "
            "collapsing one into the other. It is precisely "
            "this dual loyalty that the politics of the 2020s "
            "has been bad at. More specifically, Lahiri's *In "
            "Other Words* — *\"a small, voluntary self-"
            "displacement\"* — names the personal version of the "
            "Appiah claim: writing in a second language produces "
            "a third self that is neither hyphenated nor "
            "synthetic but situational. In this regard, the "
            "three frames converge. Plural identity (Sen) is "
            "the *fact*; rooted cosmopolitanism (Appiah) is the "
            "*political stance*; the third self (Lahiri) is the "
            "*practical experience*. My own position, after a "
            "year reading these three, is that the most useful "
            "civic skill of the next decade is the willingness to "
            "hold two loyalties without resolving them. Caution "
            "is warranted; identitarian movements work by "
            "demanding a singular belonging that the human "
            "evidence does not actually support. Appiah's "
            "argument is, finally, an argument for everyday "
            "moral patience.*"
        ),
        "reflect": [
            "I can identify each writer's framework on identity-and-globalisation.",
            "I can use 5+ cosmopolitan vocabulary terms.",
            "I can write a 400-word position essay.",
        ],
        "pitfalls": [
            "Don't conflate *cosmopolitanism* with *rootless*.",
            "*Plural identity* is conceptual, not documentary.",
            "Quote cosmopolitan theorists sparingly; their "
            "registers are contagious.",
        ],
        "further": [
            "Amartya Sen, *Identity and Violence* (2006).",
            "Kwame Anthony Appiah, *Cosmopolitanism: Ethics in "
            "a World of Strangers* (2006).",
            "Jhumpa Lahiri, *In Other Words* (Italian 2015 / "
            "English 2016).",
        ],
        "exam_listening": (
            "Read twice.\n\n"
            "> \"Sen argues that no human being is reducible to a "
            "single belonging. Appiah argues for rooted "
            "cosmopolitanism — local and general loyalties at "
            "once. Lahiri describes writing in a second language "
            "as a small voluntary self-displacement.\"\n\n"
            "1. Sen's claim: ___ . 2. Appiah's claim: ___ . 3. "
            "Lahiri's experience: ___ . 4. The three convergence: "
            "___ ."
        ),
        "exam_reading": (
            "Read the three paraphrased frames above.\n\n"
            "1. Sen's central claim: ___ . 2. Appiah's framework "
            "name: ___ . 3. Lahiri's metaphor for second-"
            "language writing: ___ . 4. What all three reject: "
            "___ ."
        ),
        "exam_use": (
            "**Composition prompt:** *Develop your position on "
            "identity-and-globalisation in 250 words. Use 3 "
            "cosmopolitan terms + 1 cleft + 1 integrated quote.*"
        ),
        "exam_writing": (
            "**Mediation prompt:** A 250-word German "
            "Feuilleton-essay on Heimat. Mediate for an English-"
            "speaking literary-essay reader. (Source provided in "
            "class.)"
        ),
        "exam_keys": [
            "**Comprehension.** 1. plural identity (no single belonging); 2. rooted cosmopolitanism (local + general loyalties); 3. small voluntary self-displacement → third self; 4. all reject the cartoon of identity as a single sticker.",
            "**Analysis.** plural identity is the fact, rooted cosmopolitanism is the political stance, third self is the practical experience; *rooted cosmopolitanism*; *a small voluntary self-displacement that produces a third version of yourself*; the singular-identity cartoon.",
            "**Composition.** Open.",
            "**Mediation.** Open.",
        ],
    },
    {
        "n": 2, "slug": "political-discourse-advanced",
        "title": "Political Discourse, Advanced",
        "skills": ["reading", "listening", "language_awareness"],
        "bp": [
            "3.4.1 / 3.5.1 Soziokulturelles Orientierungswissen / Themen",
            "3.4.3.1 / 3.5.3.1 Hör-/Hörsehverstehen",
            "3.4.3.2 / 3.5.3.2 Leseverstehen",
            "3.4.4 / 3.5.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can read / listen to longer political discourse and identify rhetorical structure, register-shifts, and dog-whistle vocabulary.",
            "I can use advanced rhetorical-analysis vocabulary (*dog whistle, framing battle, scripted spontaneity, agenda-control, loaded antithesis*).",
            "I can write a 450-word rhetorical-analysis essay sustaining argument.",
        ],
        "leadin": (
            "The class read the full text of three Westminster "
            "Prime Minister's Questions (PMQs) sessions from "
            "different administrations. The shared question: "
            "*how does each speaker control the agenda of the "
            "exchange when given six minutes?* The class noticed "
            "that agenda-control is rarely about the topic; it "
            "is about which question gets answered with which "
            "answer."
        ),
        "activate": (
            "**Agenda-control scan.** With your partner, list 3 "
            "tactics a politician uses to redirect a question "
            "without obviously refusing to answer."
        ),
        "input_blocks": [
            ("Reading — three PMQs paraphrased",
             "*Speaker A* answers a question on housing by "
             "shifting to the broader cost-of-living frame. "
             "*Speaker B* answers a question on immigration by "
             "deploying a loaded antithesis (*not whether but "
             "how*). *Speaker C* answers a question on climate "
             "policy by attacking the questioner's "
             "constituency record. All three speakers are, "
             "technically, answering. None is doing what the "
             "question asked."),
            ("Vocabulary — advanced rhetorical analysis",
             "*dog whistle, framing battle, scripted "
             "spontaneity, agenda-control, loaded antithesis, "
             "ad hominem, whataboutism, ideological "
             "scaffolding, prebuttal, talking-point discipline, "
             "register-shifting.*"),
        ],
        "practise_g": [
            "1. Match: dog whistle → coded signal to a base; "
            "whataboutism → deflect via counter-accusation; "
            "scripted spontaneity → rehearsed casualness.",
            "2. T or F: agenda-control means refusing to answer; "
            "register-shifting means changing accent; loaded "
            "antithesis hides agreement inside contrast.",
        ],
        "practise_m": [
            "3. Identify in each PMQs paraphrase: agenda-control "
            "tactic + register-shift + one rhetorical move.",
        ],
        "answer_g": (
            "1. all true.\n"
            "2. F (agenda-control means redirecting), F "
            "(register-shifting = formal-to-informal etc.), T."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Rhetorical-analysis essay, 450 words.** Pick one "
            "of the three PMQs. Identify rhetorical structure, "
            "register-shifts, and any dog-whistle vocabulary. "
            "Use 6 advanced rhetorical terms + 4 integrated "
            "quotes + 7 academic discourse markers + 2 cleft "
            "structures."
        ),
        "produce_sample": (
            "*Speaker B's answer to the housing question is, "
            "technically, an answer; politically, it is a "
            "framing battle conducted at speed. The questioner "
            "asked: *what will the government do about the "
            "47,000 social-housing waiting list in this "
            "constituency?* The Speaker's response opens with a "
            "loaded antithesis — *the question is not whether "
            "but how* — that refuses the binary the questioner "
            "implicitly offered. Accordingly, by the third "
            "sentence the topic has migrated from social housing "
            "to the broader cost-of-living frame, where the "
            "Speaker has prepared talking-point discipline. The "
            "agenda-control move is recognisable but not, in "
            "this case, dishonest; it is, more specifically, a "
            "register-shift from constituency-particular to "
            "national-general, and the data the Speaker cites is "
            "real. By contrast, the dog-whistle vocabulary is "
            "where the analyst has to be most careful. The "
            "phrase *those who play the system* sits inside "
            "what looks like a neutral defence of housing "
            "allocation rules; the phrase, however, has a "
            "documented coded history in this party's "
            "communications since 2018. It is precisely the "
            "phrase, more than any single argument, that signals "
            "to the activist base. More specifically, the "
            "scripted-spontaneity at the close — a self-correction "
            "that lets the Speaker repeat the dog-whistle phrase "
            "while appearing to reject it — is the most "
            "structurally manipulative move in the answer. In "
            "this regard, what looks like agenda-control is also "
            "a small, repeatable trick: include the loaded "
            "phrase, frame it inside a self-correction, and "
            "trust the activist base to hear the phrase, not "
            "the correction. It is precisely the layered "
            "structure that makes the answer rhetorically "
            "effective and analytically interesting. The "
            "questioner's reply, in the next exchange, "
            "successfully forces the Speaker back to the 47,000 "
            "figure. The Speaker concedes the figure. The "
            "*concession* is, predictably, framed inside a "
            "second loaded antithesis — *not whether the figure "
            "is real but what we are doing about it*. The PMQs "
            "format rewards this kind of layered control. Caution "
            "is warranted; not every redirected answer is a "
            "dog whistle. Some are simply policy disagreement.*"
        ),
        "reflect": [
            "I can identify rhetorical structure, register-shifts, and dog-whistle vocabulary.",
            "I can use 6+ advanced rhetorical-analysis terms.",
            "I can write a 450-word rhetorical-analysis essay.",
        ],
        "pitfalls": [
            "Don't accuse without evidence — *dog whistle* "
            "claims need a documented coded history.",
            "*Agenda-control* is not synonymous with *bad faith*.",
            "Quote integration is part of the analysis, not a "
            "decoration.",
        ],
        "further": [
            "Sam Leith, *You Talkin' to Me?* (later chapters).",
            "George Lakoff, *Don't Think of an Elephant!* "
            "(framing).",
        ],
        "exam_listening": (
            "Listen / read twice.\n\n"
            "> \"Speaker B's answer opens with a loaded antithesis "
            "— *the question is not whether but how* — that "
            "refuses the binary the questioner offered. The "
            "topic migrates to the cost-of-living frame. The "
            "phrase *those who play the system* is a documented "
            "dog whistle in this party's communications since "
            "2018.\"\n\n"
            "1. Loaded antithesis: ___ . 2. Topic migration: "
            "___ . 3. Dog whistle: ___ . 4. Documented since: "
            "___ ."
        ),
        "exam_reading": (
            "Read the three PMQs paraphrases above.\n\n"
            "1. Speaker A's tactic: ___ . 2. Speaker B's tactic: "
            "___ . 3. Speaker C's tactic: ___ . 4. The shared "
            "feature: ___ ."
        ),
        "exam_use": (
            "**Composition prompt:** *Analyse the rhetorical "
            "structure of Speaker A in 350 words. Use 4 "
            "advanced rhetorical terms + 3 markers + 1 cleft.*"
        ),
        "exam_writing": (
            "**Mediation prompt:** A 250-word German "
            "Bundestag-Rede excerpt with documented dog-"
            "whistle vocabulary. Mediate the rhetorical stance "
            "for an English-speaking political-rhetoric "
            "researcher. (Source provided in class.)"
        ),
        "exam_keys": [
            "**Comprehension.** 1. *not whether but how*; 2. social housing → cost-of-living; 3. *those who play the system*; 4. 2018.",
            "**Analysis.** 1. shifts to broader cost-of-living frame; 2. loaded antithesis (*not whether but how*); 3. ad-hominem on questioner's constituency record; 4. all three answer technically without doing what the question asked.",
            "**Composition.** Open.",
            "**Mediation.** Open.",
        ],
    },
    {
        "n": 3, "slug": "dystopias-and-utopias",
        "title": "Dystopias and Utopias",
        "skills": ["reading", "writing", "language_awareness"],
        "bp": [
            "3.4.1 / 3.5.1 Soziokulturelles Orientierungswissen / Themen",
            "3.4.3.2 / 3.5.3.2 Leseverstehen",
            "3.4.3.5 / 3.5.3.5 Schreiben",
            "3.4.4 / 3.5.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can read short utopian extracts (Le Guin, More) alongside dystopian extracts (Atwood) and identify the structural mirror between the genres.",
            "I can use vocabulary of utopia / dystopia (*positive utopia, ambiguous utopia, dystopian inversion, eutopia, the imaginary blueprint*).",
            "I can write a 450-word essay arguing how utopian writing illuminates dystopian writing.",
        ],
        "leadin": (
            "The class returns to *The Handmaid's Tale* alongside "
            "two utopian extracts: Thomas More's *Utopia* (1516) "
            "and Ursula K. Le Guin's *The Dispossessed* (1974). "
            "Mr. Yilmaz set the question: *what does Le Guin's "
            "subtitle — \"An Ambiguous Utopia\" — tell us about "
            "what utopia is allowed to look like?*"
        ),
        "activate": (
            "**Utopia / dystopia mirror scan.** With your "
            "partner, list 3 features that appear in both "
            "Atwood's Gilead and More's Utopia (or Le Guin's "
            "Anarres). Mark each as *control / equality / "
            "ritual*."
        ),
        "input_blocks": [
            ("Reading — three extracts (paraphrased)",
             "*More — Utopia (1516):* The island of Utopia has "
             "no private property and limited working hours; "
             "decisions are made by elected magistrates; the "
             "regime is humane but homogeneous.\n\n"
             "*Le Guin — The Dispossessed (1974):* The "
             "anarchist moon Anarres has no government, no "
             "property, no money — and a very real culture of "
             "informal social pressure that makes dissent "
             "exhausting. The subtitle *An Ambiguous Utopia* is "
             "load-bearing.\n\n"
             "*Atwood — The Handmaid's Tale:* Gilead's regime "
             "speaks the *language of utopia* (purity, order, "
             "fertility) while functioning as dystopia. The "
             "structural mirror is exact."),
            ("Vocabulary — utopia / dystopia",
             "*positive utopia, ambiguous utopia, eutopia "
             "(good place / nowhere), dystopia, dystopian "
             "inversion, the imaginary blueprint, social "
             "engineering, informal coercion, "
             "homogeneity-as-control.*"),
        ],
        "practise_g": [
            "1. Match: eutopia → good-place / nowhere; "
            "ambiguous utopia → utopia with disclosed costs; "
            "dystopian inversion → utopia turned inside out.",
            "2. T or F: More's *Utopia* is straightforwardly "
            "humane; Le Guin's *Dispossessed* hides its costs; "
            "Atwood's Gilead speaks utopia's vocabulary.",
        ],
        "practise_m": [
            "3. Build 4 sentences applying utopia-dystopia "
            "vocabulary to one extract pair.",
        ],
        "answer_g": (
            "1. all true.\n"
            "2. F (More's *Utopia* is also disturbingly "
            "homogeneous), F (Le Guin discloses the costs — "
            "that is the point), T."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Comparative essay, 450 words.** Argue that "
            "Le Guin's *ambiguous utopia* clarifies Atwood's "
            "Gilead. Use 4 integrated quotes + 7 academic "
            "discourse markers + 2 cleft structures."
        ),
        "produce_sample": (
            "*Ursula K. Le Guin's subtitle to *The Dispossessed* "
            "— *An Ambiguous Utopia* — is the most useful "
            "single phrase for reading Margaret Atwood's *The "
            "Handmaid's Tale*. The reason is structural rather "
            "than thematic. Le Guin's anarchist moon Anarres has "
            "no government, no property, and no money. By "
            "contrast with More's classical *Utopia* (1516), "
            "however, Le Guin discloses the costs of her "
            "imaginary society as part of the imagining. "
            "Anarres is held together by informal social "
            "pressure that the novel describes as exhausting. "
            "*\"To break a promise to a stranger is the smallest "
            "thing,\"* one character thinks; *\"to break a "
            "promise to a comrade is to be unmade.\"* "
            "Accordingly, the utopia is not corrupted into "
            "dystopia — the dystopian element is structurally "
            "embedded from the start. It is precisely this "
            "ambiguity that Atwood's Gilead inverts. Gilead "
            "*speaks* the language of utopia — purity, order, "
            "fertility — while *functioning* as dystopia. The "
            "two novels are mirror images: Le Guin discloses "
            "the costs of a humane society; Atwood discloses "
            "the cosmetic that hides an inhumane one. By "
            "contrast with More's homogeneous *Utopia*, both "
            "Le Guin and Atwood understand that homogeneity is "
            "itself a form of social engineering. More "
            "specifically, the *Historical Notes* of *The "
            "Handmaid's Tale* enact the third move that More's "
            "1516 text could not: a satirical reading of the "
            "act of academic recovery itself. Where More gives "
            "us a single voice, Atwood gives us three layers — "
            "Gilead's utopian rhetoric, Offred's silent "
            "counter-narrative, and the academy's well-meaning "
            "future appropriation. In this regard, reading "
            "Atwood through Le Guin clarifies that the "
            "dystopian inversion is not the opposite of utopia "
            "but its disclosed underside. Both genres ask the "
            "same question: *what would a deliberately "
            "imagined society have to be willing to lose?* "
            "More gives one answer; Le Guin a more honest "
            "one; Atwood the most disturbing — that the "
            "society in question may already be losing it.*"
        ),
        "reflect": [
            "I can identify the structural mirror between utopia and dystopia.",
            "I can use 5+ utopia-dystopia terms.",
            "I can write a 450-word comparative essay.",
        ],
        "pitfalls": [
            "Don't reduce utopia to *good* and dystopia to "
            "*bad* — both are imaginary blueprints with "
            "disclosed costs.",
            "*Ambiguous utopia* is Le Guin's specific term — "
            "credit her.",
            "The structural mirror is not a thematic claim; it "
            "is a formal one.",
        ],
        "further": [
            "Thomas More, *Utopia* (1516).",
            "Ursula K. Le Guin, *The Dispossessed* (1974).",
            "Tom Moylan, *Demand the Impossible: Science Fiction "
            "and the Utopian Imagination*.",
        ],
        "exam_listening": (
            "Read twice.\n\n"
            "> \"Le Guin's anarchist moon Anarres has no "
            "government, no property, and no money — and a very "
            "real culture of informal social pressure that "
            "makes dissent exhausting. The subtitle *An "
            "Ambiguous Utopia* is load-bearing.\"\n\n"
            "1. Three absences: ___ . 2. Hidden cost: ___ . 3. "
            "Subtitle: ___ . 4. Subtitle's role: ___ ."
        ),
        "exam_reading": (
            "Read the three extracts above.\n\n"
            "1. More — defining feature: ___ . 2. Le Guin — "
            "disclosed cost: ___ . 3. Atwood — relation to "
            "utopia: ___ . 4. Shared structural insight: ___ ."
        ),
        "exam_use": (
            "**Composition prompt:** *Argue that Atwood's "
            "Gilead speaks utopia's vocabulary while functioning "
            "as dystopia in 350 words. Use 3 integrated quotes "
            "+ 4 markers + 1 cleft.*"
        ),
        "exam_writing": (
            "**Mediation prompt:** A 250-word German "
            "literary-criticism essay on utopian fiction. "
            "Mediate for an English-speaking literary-magazine "
            "reader. (Source provided in class.)"
        ),
        "exam_keys": [
            "**Comprehension.** 1. no government / no property / no money; 2. informal social pressure; 3. *An Ambiguous Utopia*; 4. load-bearing — utopia is structured to disclose its costs.",
            "**Analysis.** 1. no private property + elected magistrates + humane but homogeneous; 2. dissent is exhausting; 3. speaks utopia's vocabulary while functioning as dystopia; 4. dystopian inversion is utopia's disclosed underside.",
            "**Composition.** Open.",
            "**Mediation.** Open.",
        ],
    },
    {
        "n": 4, "slug": "contemporary-poetry",
        "title": "Contemporary Poetry",
        "skills": ["reading", "writing", "language_awareness"],
        "bp": [
            "3.4.1 / 3.5.1 Soziokulturelles Orientierungswissen / Themen",
            "3.4.3.2 / 3.5.3.2 Leseverstehen",
            "3.4.3.5 / 3.5.3.5 Schreiben",
            "3.4.4 / 3.5.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can close-read three contemporary poems (an Ocean Vuong-style lyric, a Warsan Shire-style political lyric, a Layli Long Soldier-style document poem) and identify form, voice, and one figurative move per poem.",
            "I can use vocabulary of contemporary poetic form (*document poem, fragmentary lyric, prose poem, polyvocal lyric*).",
            "I can write a 400-word poetic-analysis essay tracing one move across three poems.",
        ],
        "leadin": (
            "Klasse 13 returns to poetry with three contemporary "
            "lyric forms. Mr. Yilmaz set the question: *what is "
            "contemporary poetry doing that 19th-century lyric "
            "could not do?* The class spent the lesson noticing "
            "the document poem, the fragmentary lyric, and the "
            "polyvocal lyric — three forms that share a refusal "
            "of the unified Romantic *I*."
        ),
        "activate": (
            "**Form scan.** With your partner, list 3 features "
            "of contemporary lyric (post-2000) that you have "
            "noticed. Mark each as *formal / vocal / "
            "political*."
        ),
        "input_blocks": [
            ("Reading — three poetic moves (paraphrased)",
             "*The fragmentary lyric* refuses syntactic "
             "completeness; lines break off mid-thought; the "
             "white space is part of the meaning.\n\n"
             "*The document poem* uses found material — court "
             "transcripts, government documents, treaty texts — "
             "and re-arranges or annotates them; the *I* is "
             "ironised.\n\n"
             "*The polyvocal lyric* allows multiple speakers / "
             "voices inside a single poem, often without quote "
             "marks; the boundary between speakers is "
             "deliberately uncertain."),
            ("Vocabulary — contemporary poetic form",
             "*document poem (or documentary poetics), "
             "fragmentary lyric, prose poem, polyvocal lyric, "
             "found poem, ekphrastic poem, the broken line, "
             "the white space, polyphony, ironised *I*, "
             "elliptical lyric.*"),
        ],
        "practise_g": [
            "1. Match: document poem → uses found material; "
            "polyvocal → multiple speakers; fragmentary lyric → "
            "broken syntax + white space.",
            "2. T or F: contemporary lyric typically uses "
            "regular meter; document poems are usually "
            "sentimental.",
        ],
        "practise_m": [
            "3. Build 3 sentences applying contemporary-poetic "
            "vocabulary to one of the three forms.",
        ],
        "answer_g": (
            "1. all true.\n"
            "2. F (often free verse), F (often archival, "
            "ironic, or political — rarely sentimental)."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Poetic-analysis essay, 400 words.** Trace the "
            "*ironised I* across the three forms. Use 4 "
            "contemporary-poetic terms + 6 academic discourse "
            "markers + 1 cleft + 1 quote per poem."
        ),
        "produce_sample": (
            "*The most useful single move for reading "
            "contemporary lyric is the *ironised I* — the speaker "
            "who refuses to claim the unified Romantic position "
            "and whose *I* is structurally compromised. In the "
            "fragmentary lyric, the *I* is interrupted by white "
            "space: a line breaks mid-thought, and the silence "
            "that follows is part of the speaker. *\"What I "
            "wanted to say / was — \"* leaves the verb open. "
            "Accordingly, the speaker becomes a person "
            "interrupted, not a person speaking. By contrast, "
            "the document poem ironises the *I* by refusing it "
            "almost entirely: court transcripts, treaty texts, "
            "and government documents replace the lyric voice. "
            "*\"The party of the first part hereby agrees — \"* "
            "is, in Layli Long Soldier-style work, both a quote "
            "and a confrontation. The reader is forced to read "
            "the *I*'s absence as itself a poetic move. More "
            "specifically, the polyvocal lyric ironises the *I* "
            "by multiplying it: two or more voices share the "
            "poem without quote marks, and the boundary between "
            "speakers is the formal site of meaning. *\"I said. "
            "She said. We said.\"* — the rhythm of pronoun "
            "shift performs the polyphony. It is precisely this "
            "shared refusal — fragmentary, document-based, or "
            "polyvocal — that distinguishes post-2000 lyric "
            "from its 19th-century inheritance. In this regard, "
            "what looks like formal experimentation is "
            "structural critique: the unified Romantic *I* is "
            "treated as one historical option among others, "
            "not as the natural form of lyric voice. Caution "
            "is warranted; not every fragmented line is a "
            "fragmentary lyric. The form is a stance, not a "
            "decoration. The reader's task is to register the "
            "stance and to ask, in each case, *what would the "
            "Romantic version of this poem have lost?*. The "
            "answer, more often than not, is precisely the "
            "thing the contemporary form is preserving.*"
        ),
        "reflect": [
            "I can identify form, voice, and one figurative move in three contemporary lyric forms.",
            "I can use 6+ contemporary-poetic terms.",
            "I can write a 400-word poetic-analysis essay tracing one move across three poems.",
        ],
        "pitfalls": [
            "Don't read every fragment as a fragmentary lyric — "
            "the form is a stance.",
            "Document poems require attention to the source "
            "context.",
            "Polyvocal ≠ confused — the boundary is the meaning.",
        ],
        "further": [
            "Ocean Vuong, *Night Sky with Exit Wounds* (2016).",
            "Warsan Shire, *Bless the Daughter Raised by a Voice "
            "in Her Head* (2022).",
            "Layli Long Soldier, *WHEREAS* (2017).",
        ],
        "exam_listening": (
            "Read twice.\n\n"
            "> \"The fragmentary lyric refuses syntactic "
            "completeness; lines break off mid-thought; the "
            "white space is part of the meaning. The document "
            "poem uses found material — court transcripts, "
            "treaties — and the *I* is ironised. The polyvocal "
            "lyric allows multiple speakers without quote "
            "marks.\"\n\n"
            "1. Fragmentary lyric: ___ . 2. Document poem: ___ . "
            "3. Polyvocal lyric: ___ . 4. Shared refusal: ___ ."
        ),
        "exam_reading": (
            "Read the three forms paraphrased above.\n\n"
            "1. The role of white space: ___ . 2. The "
            "documentary source: ___ . 3. The polyvocal "
            "boundary: ___ . 4. The ironised *I*: ___ ."
        ),
        "exam_use": (
            "**Composition prompt:** *Apply the *ironised I* "
            "to one short poem (provided in class) in 350 "
            "words. Use 3 contemporary-poetic terms + 4 "
            "markers.*"
        ),
        "exam_writing": (
            "**Mediation prompt:** A 200-word German "
            "literary-essay paragraph on contemporary "
            "Lyrik. Mediate for an English-speaking poetry "
            "magazine. (Source provided in class.)"
        ),
        "exam_keys": [
            "**Comprehension.** 1. broken syntax + white space as meaning; 2. uses found material (court, government, treaty); 3. multiple speakers without quote marks; 4. refusal of the unified Romantic *I*.",
            "**Analysis.** 1. white space as part of speaker's silence; 2. archival material confronts the lyric *I*; 3. boundary between speakers is the formal site of meaning; 4. structurally compromised *I*.",
            "**Composition.** Open.",
            "**Mediation.** Open.",
        ],
    },
    {
        "n": 5, "slug": "media-and-public-opinion",
        "title": "Media and Public Opinion",
        "skills": ["reading", "writing", "language_awareness"],
        "bp": [
            "3.4.1 / 3.5.1 Soziokulturelles Orientierungswissen / Themen",
            "3.4.3.2 / 3.5.3.2 Leseverstehen",
            "3.4.3.5 / 3.5.3.5 Schreiben",
            "3.4.4 / 3.5.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can read short texts on platform algorithms and public opinion (Tufekci, Wu) and identify the writer's central causal claim.",
            "I can use vocabulary of platform-media analysis (*algorithmic amplification, attention rent, recommendation system, network effect, platform governance*).",
            "I can write a 450-word media-analysis essay sustaining a complex causal argument.",
        ],
        "leadin": (
            "The class read short extracts from Zeynep Tufekci's "
            "*Twitter and Tear Gas* (2017) and Tim Wu's *The "
            "Attention Merchants* (2016). Mr. Yilmaz framed the "
            "question: *what is the difference between public "
            "opinion and aggregated platform behaviour?* The "
            "class noticed quickly that the answer is not "
            "*nothing* and not *everything*."
        ),
        "activate": (
            "**Causal-claim scan.** With your partner, list 3 "
            "causal claims you have heard about social media + "
            "politics. Mark each as *plausible / contested / "
            "tabloid*."
        ),
        "input_blocks": [
            ("Reading — two extracts (paraphrased)",
             "*Tufekci (2017):* Algorithmic amplification "
             "produces attention asymmetries that are not the "
             "same as public opinion. The *visible majority* on "
             "a platform is a function of the platform's "
             "ranking signals, not of the underlying population.\n\n"
             "*Wu (2016):* The history of mass media is the "
             "history of *attention merchants* — actors whose "
             "business model is the harvest, packaging, and "
             "resale of attention. Platforms inherit and "
             "intensify this model."),
            ("Vocabulary — platform-media analysis",
             "*algorithmic amplification, attention rent, "
             "recommendation system, network effect, platform "
             "governance, content moderation, attention "
             "economy, asymmetric visibility, the visible "
             "majority, micro-targeting.*"),
        ],
        "practise_g": [
            "1. Match: algorithmic amplification → ranking-"
            "driven visibility; attention rent → the price of "
            "your attention; the visible majority → not the "
            "same as the actual majority.",
            "2. T or F: platforms inherit the attention-"
            "merchant model; algorithmic amplification reflects "
            "underlying public opinion 1:1.",
        ],
        "practise_m": [
            "3. Build 4 sentences applying platform-media "
            "vocabulary to a recent online controversy.",
        ],
        "answer_g": (
            "1. all true.\n"
            "2. T, F (it is shaped by ranking signals)."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Media-analysis essay, 450 words.** Argue a "
            "complex causal claim about platforms and public "
            "opinion. Use 6 platform-media terms + 7 academic "
            "discourse markers + 2 cleft structures + 2 "
            "integrated quotes + 1 hedge."
        ),
        "produce_sample": (
            "*The single most useful conceptual distinction in "
            "this year's reading on platform media is Zeynep "
            "Tufekci's between *public opinion* and the "
            "*visible majority*. The available evidence "
            "suggests that algorithmic amplification produces "
            "attention asymmetries that systematically diverge "
            "from the underlying distribution of views in a "
            "given population. Accordingly, what looks like a "
            "consensus on a platform — a trending hashtag, a "
            "saturated reply space, a viral take — is not, in "
            "the strict sense, public opinion. It is a function "
            "of the platform's ranking signals interacting with "
            "user behaviour. By contrast with the older mass-"
            "media model, where editorial gatekeepers were "
            "visible and contestable, platform amplification is "
            "structurally opaque. It is precisely this opacity "
            "that makes Tim Wu's *attention merchant* genealogy "
            "useful: the business model is continuous with "
            "earlier media, but the visibility of the gatekeepers "
            "has decreased while the precision of micro-"
            "targeting has increased. More specifically, the "
            "common claim that *the algorithm is showing what "
            "people want* is, on inspection, a circular one. "
            "The algorithm is showing what its ranking signals "
            "treat as engaging; engagement-as-measured is "
            "shaped by what the algorithm previously elevated. "
            "The system is, in this regard, a feedback loop "
            "with no neutral baseline. Critics will counter, "
            "fairly, that *some* signal of underlying interest "
            "is preserved — otherwise the platform would lose "
            "users. I accept that, but the signal is filtered "
            "through ranking choices that are themselves "
            "political-economic. The honest analytical move is "
            "to decompose the visible majority into three "
            "components: underlying preferences (real but "
            "partial), ranking-induced amplification (large "
            "and shaping), and feedback-loop reinforcement "
            "(non-trivial). It is precisely this decomposition "
            "that the public discourse has been bad at. "
            "Caution is warranted; the next decade of platform "
            "governance will, in my reading, hinge on whether "
            "regulators can compel transparency on the second "
            "and third components. Without that, *public "
            "opinion* and *aggregated platform behaviour* will "
            "continue to be confused — to the political "
            "advantage of whoever sets the ranking signals.*"
        ),
        "reflect": [
            "I can identify the writer's central causal claim in a platform-media text.",
            "I can use 6+ platform-media terms.",
            "I can write a 450-word media-analysis essay with a complex causal argument.",
        ],
        "pitfalls": [
            "*The algorithm is showing what people want* is "
            "circular — flag it.",
            "Don't conflate engagement with preference.",
            "Causal claims need decomposition, not assertion.",
        ],
        "further": [
            "Zeynep Tufekci, *Twitter and Tear Gas* (2017).",
            "Tim Wu, *The Attention Merchants* (2016).",
            "Joseph Bernstein — accessible journalism on "
            "platforms.",
        ],
        "exam_listening": (
            "Read twice.\n\n"
            "> \"Algorithmic amplification produces attention "
            "asymmetries that are not the same as public "
            "opinion. The *visible majority* on a platform is "
            "a function of the platform's ranking signals, "
            "not of the underlying population.\"\n\n"
            "1. Amplification produces: ___ . 2. Visible "
            "majority is: ___ . 3. Function of: ___ . 4. NOT "
            "the same as: ___ ."
        ),
        "exam_reading": (
            "Read the two paraphrased extracts above.\n\n"
            "1. Tufekci's distinction: ___ . 2. Wu's "
            "genealogical claim: ___ . 3. The shared "
            "underlying argument: ___ . 4. The political "
            "consequence: ___ ."
        ),
        "exam_use": (
            "**Composition prompt:** *Decompose the *visible "
            "majority* concept in 350 words. Use 4 platform-"
            "media terms + 4 markers + 1 cleft.*"
        ),
        "exam_writing": (
            "**Mediation prompt:** A 250-word German "
            "Plattform-regulierungs-Bericht (e.g. Bundeskartellamt) "
            "for an English-speaking platform-policy reader. "
            "(Source provided in class.)"
        ),
        "exam_keys": [
            "**Comprehension.** 1. attention asymmetries; 2. function of platform's ranking signals; 3. ranking signals; 4. public opinion / underlying population.",
            "**Analysis.** 1. public opinion vs. visible majority; 2. attention merchants — business model continuous, gatekeepers less visible, micro-targeting more precise; 3. platforms shape what they appear to measure; 4. regulatory transparency as the political question.",
            "**Composition.** Open.",
            "**Mediation.** Open.",
        ],
    },
    {
        "n": 6, "slug": "mediation-policy-text",
        "title": "Mediation: A German Policy Text",
        "skills": ["mediation", "writing", "language_awareness"],
        "bp": [
            "3.4.1 / 3.5.1 Soziokulturelles Orientierungswissen / Themen",
            "3.4.3.5 / 3.5.3.5 Schreiben",
            "3.4.3.6 / 3.5.3.6 Sprachmittlung",
            "3.4.3.7 / 3.5.3.7 Verfügen über sprachliche Mittel – Wortschatz",
        ],
        "objectives": [
            "I can mediate a 600-word German policy text into 18 English sentences for a named addressee profile.",
            "I can preserve modal nuance, hedge structure, citation style, and disciplinary register simultaneously.",
            "I can use the full reporting-verb toolkit and add layered cultural / disciplinary notes where needed.",
        ],
        "leadin": (
            "Final mediation Unit. The source is a 600-word "
            "extract from the 2027 federal report on "
            "Bildungsgerechtigkeit in Germany. The addressee: "
            "an English-speaking comparative-education "
            "researcher writing for the OECD. The task: "
            "mediate honestly enough that the OECD reader can "
            "decide whether to commission a full translation."
        ),
        "activate": (
            "**Audit scan.** Mark each section of the source: "
            "*executive summary / methods / findings / hedges "
            "/ implications / German-specific institutional "
            "context*."
        ),
        "input_blocks": [
            ("Source — *Bildungsgerechtigkeit-Bericht 2027 (excerpt)*",
             "*Der vorliegende Bericht untersucht die "
             "Entwicklung der Bildungsgerechtigkeit in "
             "Deutschland zwischen 2010 und 2025 und bezieht "
             "sich auf eine bundesweite Stichprobe von 1,2 "
             "Millionen Schülerinnen und Schülern. "
             "Methodisch nutzen wir mehrebenenanalytische "
             "Modelle. Die Ergebnisse legen nahe, dass die "
             "Korrelation zwischen sozio-ökonomischem "
             "Hintergrund und PISA-Ergebnis in den Stadt-"
             "staaten Berlin, Hamburg und Bremen leicht "
             "abgenommen hat, in den Flächenländern hingegen "
             "stabil geblieben ist. Bildungspolitische "
             "Implikationen diskutieren wir vorsichtig. Eine "
             "kausale Interpretation der Korrelationen ist "
             "auf Basis der vorliegenden Daten nicht "
             "möglich.*"),
            ("Mediation conventions for policy texts",
             "**German-specific institutional terms:** "
             "*Stadtstaaten* (German city-states — Berlin, "
             "Hamburg, Bremen), *Flächenländer* (German federal "
             "states with rural areas), *Bildungsgerechtigkeit* "
             "(educational equity / fairness), *Mehrebenen-"
             "analyse* (multilevel modelling).\n\n"
             "**Hedge preservation:** *legen nahe* → *suggest*; "
             "*kausale Interpretation … nicht möglich* → "
             "*causal inference is not possible from the "
             "available data*.\n\n"
             "**Citation style:** preserve dataset references "
             "(e.g. *PISA, NEPS*) — these are recognisable to "
             "comparative-education researchers."),
        ],
        "practise_g": [
            "1. Match German term → English: *Stadtstaaten* → ?, "
            "*Flächenländer* → ?, *Bildungsgerechtigkeit* → ?, "
            "*Mehrebenenanalyse* → ?",
            "2. Decide for the OECD addressee: keep + "
            "explain in brackets / paraphrase / drop entirely "
            "— *Stadtstaaten*, *PISA*, *Mehrebenenanalyse*.",
        ],
        "practise_m": [
            "3. Build a 6-sentence English mediation of the "
            "source above.",
        ],
        "answer_g": (
            "1. German city-states / federal states with rural "
            "areas / educational equity / multilevel modelling.\n"
            "2. *Stadtstaaten*: keep + 5-word note. *PISA*: "
            "keep without note. *Mehrebenenanalyse*: keep + "
            "3-word note for non-statisticians."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Final mediation, 18 sentences.** Read the source "
            "above. Write 18 English sentences for an OECD "
            "comparative-education researcher. Preserve modal "
            "nuance + hedge structure + citation style. Use 10 "
            "reporting verbs + 3 cultural / institutional "
            "note brackets."
        ),
        "produce_sample": (
            "*Hi Eva, here is a clean mediation of the "
            "*Bildungsgerechtigkeit-Bericht 2027* — should be "
            "useful for your OECD review. The report examines "
            "the development of educational equity in Germany "
            "between 2010 and 2025. The authors note that the "
            "study draws on a nationwide sample of 1.2 million "
            "school students. Methodologically, they use "
            "multilevel modelling (a statistical approach for "
            "data nested within institutions). The main "
            "findings suggest that the correlation between "
            "socio-economic background and PISA outcomes has "
            "decreased slightly in the German *Stadtstaaten* "
            "(city-states: Berlin, Hamburg, Bremen). By "
            "contrast, the report observes that the "
            "correlation has remained stable in the "
            "*Flächenländer* (the larger federal states with "
            "rural areas). The authors stress that they "
            "discuss policy implications with caution. They "
            "claim, more specifically, that causal "
            "interpretation of the observed correlations is "
            "not possible from the available data. They note, "
            "in addition, that the city-state finding is "
            "robust to several specifications. They concede "
            "that the rural-state finding is more sensitive to "
            "model choice. The report points out that the "
            "results are consistent with earlier NEPS work "
            "(German National Educational Panel Study). It "
            "warns against extrapolating to non-OECD contexts. "
            "The authors argue that the next data collection "
            "(planned for 2028) will permit stronger causal "
            "inference. They concede that funding for that "
            "collection is not yet secured. They confirm that "
            "the dataset will be made available to OECD "
            "researchers under standard access protocols. "
            "Overall, this is a paper worth reading in full, "
            "particularly the methods chapter and the regional "
            "decomposition.*"
        ),
        "reflect": [
            "I can mediate a 600-word German policy text into 18 English sentences.",
            "I can preserve modal nuance, hedges, citation style, and institutional notes.",
            "I can use 10 reporting verbs accurately.",
        ],
        "pitfalls": [
            "Don't translate institutional terms (*Stadtstaaten*) "
            "— keep + explain.",
            "*kausale Interpretation nicht möglich* is the "
            "report's central hedge; preserve it.",
            "OECD readers expect both German specificity and "
            "international comparability.",
        ],
        "further": [
            "Goethe-Institut — Sprachmittlungs-Beispielaufgaben "
            "Oberstufe.",
            "OECD Education at a Glance — comparative-education "
            "register samples.",
        ],
        "exam_listening": (
            "Read twice.\n\n"
            "> \"Der Bericht untersucht Bildungsgerechtigkeit "
            "zwischen 2010 und 2025 mit einer Stichprobe von 1,2 "
            "Millionen Schülerinnen und Schülern. Die "
            "Korrelation zwischen sozio-ökonomischem "
            "Hintergrund und PISA-Ergebnis hat in den "
            "Stadtstaaten leicht abgenommen, in den "
            "Flächenländern ist sie stabil geblieben. Eine "
            "kausale Interpretation ist nicht möglich.\"\n\n"
            "1. Period: ___ . 2. Sample size: ___ . 3. "
            "Stadtstaaten finding: ___ . 4. Flächenländer "
            "finding: ___ ."
        ),
        "exam_reading": (
            "Read the German source above.\n\n"
            "1. Sample: ___ . 2. Method: ___ . 3. Hedge: ___ . "
            "4. Limitation: ___ ."
        ),
        "exam_use": (
            "**Match institutional term → English-(German) form.**\n\n"
            "1. Stadtstaaten → ___ ; 2. Flächenländer → ___ ; "
            "3. Bildungsgerechtigkeit → ___ ; 4. Mehrebenenanalyse "
            "→ ___ ."
        ),
        "exam_writing": (
            "**Mediation prompt:** Write 18 English sentences "
            "for the OECD addressee. Preserve hedges + use 10 "
            "reporting verbs + 3 cultural-note brackets."
        ),
        "exam_keys": [
            "**Comprehension.** 1. 2010-2025; 2. 1.2 million school students; 3. correlation slightly decreased; 4. correlation stable.",
            "**Analysis.** 1. nationwide; 2. multilevel modelling; 3. *legen nahe* → *suggest*; 4. *eine kausale Interpretation … nicht möglich*.",
            "**Composition.** *Stadtstaaten (German city-states: Berlin, Hamburg, Bremen) / Flächenländer (federal states with rural areas) / educational equity (Bildungsgerechtigkeit) / multilevel modelling (Mehrebenenanalyse).*",
            "**Mediation.** Open.",
        ],
    },
    {
        "n": 7, "slug": "the-abitur-essay",
        "title": "The Abitur Essay",
        "skills": ["writing", "language_awareness"],
        "bp": [
            "3.4.1 / 3.5.1 Soziokulturelles Orientierungswissen / Themen",
            "3.4.3.5 / 3.5.3.5 Schreiben",
            "3.4.4 / 3.5.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can plan a 90-minute Abitur Composition (Composition / Comment, ~25 BE Basisfach / ~35 BE Leistungsfach) under timed conditions.",
            "I can produce a 350-450 word Abitur-grade argumentative or creative response.",
            "I can self-assess against the Abitur Bewertungsraster (grading grid).",
        ],
        "leadin": (
            "First of three Abitur-prep Units. Today's focus: "
            "the Composition / Comment task. Mr. Yilmaz set a "
            "real-format prompt linked to a 1,000-word source "
            "extract. 90 minutes. Submit. Class debriefs against "
            "the official Bewertungsraster (grading grid) — "
            "Inhalt and Sprache scored separately."
        ),
        "activate": (
            "**Time-budget scan.** 90 minutes for the "
            "Composition section. Allocate: ___ min plan; ___ "
            "min draft; ___ min review."
        ),
        "input_blocks": [
            ("Composition / Comment — task patterns",
             "**Argumentative comment:** *Comment on the "
             "writer's central claim* / *Discuss the position "
             "presented in the source*. 350-450 words. Thesis + "
             "evidence + counter + conclusion.\n\n"
             "**Creative response:** *Write a letter, diary "
             "entry, or speech in the voice of [character / "
             "speaker]*. 350-450 words. Genre-shifts but "
             "preserves argumentative weight.\n\n"
             "**Both task types:** integrate one quote from the "
             "source; sustain academic discourse markers; "
             "preserve the source's argumentative weight."),
            ("Bewertungsraster — Inhalt + Sprache",
             "**Inhalt** (content): thesis clarity, evidence "
             "use, engagement with source, completeness of "
             "argument.\n\n"
             "**Sprache** (language): vocabulary range, "
             "grammatical accuracy, register, idiomaticity, "
             "cohesion.\n\n"
             "**Weighting:** Basisfach (basic course) 50/50; "
             "Leistungsfach (advanced course) 40/60 (Sprache "
             "weighted higher in LF)."),
        ],
        "practise_g": [
            "1. Match: argumentative comment → discuss claim; "
            "creative response → genre shift; both → integrate "
            "quote.",
            "2. T or F: Bewertungsraster scores Inhalt and "
            "Sprache together; Sprache weighted higher in LF; "
            "both task types preserve argumentative weight.",
        ],
        "practise_m": [
            "3. Outline a 400-word argumentative comment on a "
            "1,000-word source (provided in class).",
        ],
        "answer_g": (
            "1. all true.\n"
            "2. F (separately), T, T."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Abitur Composition rehearsal, 90 minutes.** Real-"
            "format prompt + 1,000-word source. Submit. Class "
            "debriefs collectively with focus on time-management "
            "and Inhalt / Sprache balance."
        ),
        "produce_sample": (
            "(See *Reflection on the rehearsal* — the "
            "production task is the timed Composition itself.)"
        ),
        "reflect": [
            "I can plan and produce a 350-450 word Abitur Composition under timed conditions.",
            "I can sustain Abitur-grade Inhalt and Sprache.",
            "I can self-assess against the Bewertungsraster.",
        ],
        "pitfalls": [
            "Spending more than 15 min planning eats drafting "
            "time.",
            "Carrying source language directly into your "
            "argument (plagiarism risk).",
            "Drafting without a thesis at the top of paragraph 1.",
        ],
        "further": [
            "Bildungsplan-aligned Abitur-prep collections "
            "(Klett, Stark).",
            "Past Abitur papers (BW), with caution: format "
            "familiarity only.",
        ],
        "exam_listening": (
            "**Composition / Comment prompt** (sample): *On the "
            "basis of the 1,000-word source provided in class, "
            "comment on the writer's central claim that "
            "*'public opinion'* and *'aggregated platform "
            "behaviour'* are increasingly conflated in "
            "contemporary democratic discourse. Write an "
            "argumentative response of 350-450 words. Use at "
            "least one integrated quote, four academic "
            "discourse markers, and a clear thesis-evidence-"
            "counter-conclusion structure.*"
        ),
        "exam_reading": (
            "**Time budget.** Allocate the 90 minutes: ___ "
            "min plan; ___ min draft; ___ min review. "
            "Justify in 2 sentences."
        ),
        "exam_use": (
            "**Reflection prompt:** *In 200 words, reflect on "
            "your Composition rehearsal. What worked? What "
            "needs the most rehearsal before the actual "
            "Abitur?*"
        ),
        "exam_writing": (
            "**(No Mediation in this Unit — dedicated "
            "Mediation Unit was Unit 6.)**"
        ),
        "exam_keys": [
            "**Comprehension.** Reward thesis + integrated quote + 4 markers + clear structure + register match.",
            "**Analysis.** Reward 15 plan / 65 draft / 10 review (or similar) + Sprache check.",
            "**Composition.** Open.",
            "**Reflection.** Open.",
        ],
    },
    {
        "n": 8, "slug": "the-abitur-comprehension",
        "title": "The Abitur Comprehension Task",
        "skills": ["reading", "writing", "language_awareness"],
        "bp": [
            "3.4.1 / 3.5.1 Soziokulturelles Orientierungswissen / Themen",
            "3.4.3.2 / 3.5.3.2 Leseverstehen",
            "3.4.3.5 / 3.5.3.5 Schreiben",
            "3.4.4 / 3.5.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can answer a 60-minute Abitur Comprehension task (~24 BE) on a 1,000-1,200-word source.",
            "I can produce concise own-words paraphrase, embedded fragments, and structural sub-answers.",
            "I can manage the time across 3-5 sub-questions of varying BE-weight.",
        ],
        "leadin": (
            "Second of three Abitur-prep Units. Today's focus: "
            "the Comprehension task — the section that students "
            "most often over-spend on at the expense of "
            "later sections. 60 minutes. Three sub-questions of "
            "varying BE-weight. Submit. Debrief against "
            "Bewertungsraster (grading grid)."
        ),
        "activate": (
            "**BE-budget scan.** Three sub-questions weighted "
            "5 BE / 10 BE / 9 BE. Allocate the 60 minutes "
            "proportionally."
        ),
        "input_blocks": [
            ("Comprehension — sub-question types",
             "1. **State / outline** (lower BE) — own-words "
             "paraphrase + 1-2 specifics from text.\n"
             "2. **Explain** (mid BE) — *because* / *the reason "
             "is that* + specific from text.\n"
             "3. **Compare / contrast** (higher BE) — both "
             "elements named + the relation."),
            ("Sprache check — Comprehension",
             "**Own words:** paraphrase, don't quote whole "
             "sentences.\n\n"
             "**Embedded fragments:** integrate 3-5 word "
             "fragments inside your sentence.\n\n"
             "**Structural sub-answers:** match the structure of "
             "the question (*compare* answers compare; *outline* "
             "answers outline)."),
        ],
        "practise_g": [
            "1. Match: state → own words; explain → reason; "
            "compare → both elements + relation.",
            "2. T or F: full quotes are rewarded in "
            "Comprehension; embedded fragments are rewarded in "
            "Comprehension; sub-questions of higher BE deserve "
            "more time.",
        ],
        "practise_m": [
            "3. Build a 4-sentence answer to a 10-BE *explain* "
            "question on a 1,000-word source.",
        ],
        "answer_g": (
            "1. all true.\n"
            "2. F (own words preferred), T, T."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Abitur Comprehension rehearsal, 60 minutes.** "
            "1,000-word source + three sub-questions (5 / 10 "
            "/ 9 BE). Submit. Debrief against Bewertungsraster."
        ),
        "produce_sample": (
            "(See *Reflection on the rehearsal* — the "
            "production task is the timed Comprehension "
            "itself.)"
        ),
        "reflect": [
            "I can answer a 60-minute Abitur Comprehension task across 3 sub-questions of varying BE.",
            "I can produce own-words paraphrase + embedded fragments.",
            "I can manage time proportionally to BE-weight.",
        ],
        "pitfalls": [
            "Over-spending on the first sub-question because it "
            "feels safe.",
            "Block-quoting instead of embedding.",
            "Answering structurally wrong (*outline* when the "
            "question said *compare*).",
        ],
        "further": [
            "Bildungsplan-aligned Abitur-prep collections.",
            "Past Abitur papers (BW), with caution.",
        ],
        "exam_listening": (
            "**Comprehension prompt** (sample): *Read the "
            "1,000-word source provided in class. Answer the "
            "following:*\n\n"
            "1. *In your own words, outline the writer's "
            "central claim about platform algorithms (5 BE).*\n"
            "2. *Explain the writer's distinction between "
            "*public opinion* and the *visible majority*. "
            "Refer to specific paragraphs (10 BE).*\n"
            "3. *Compare the writer's framing of platforms with "
            "Tim Wu's *attention merchants* genealogy as "
            "presented in the source. Identify both elements "
            "and the relation between them (9 BE).*"
        ),
        "exam_reading": (
            "**Time budget.** Allocate the 60 minutes "
            "proportionally to 5 / 10 / 9 BE."
        ),
        "exam_use": (
            "**Reflection prompt:** *In 200 words, reflect on "
            "your Comprehension rehearsal. Which sub-question "
            "was hardest? What does this tell you about your "
            "weakest skill?*"
        ),
        "exam_writing": "**(No Composition / Mediation in this Unit.)**",
        "exam_keys": [
            "**Comprehension.** Reward own-words paraphrase + named specifics + embedded fragments + structural match.",
            "**Analysis.** Suggested time: 12 / 25 / 23 (proportional to BE).",
            "**Composition.** Open.",
            "**Reflection.** Open.",
        ],
    },
    {
        "n": 9, "slug": "the-abitur-analysis",
        "title": "The Abitur Analysis Task",
        "skills": ["reading", "writing", "language_awareness"],
        "bp": [
            "3.4.1 / 3.5.1 Soziokulturelles Orientierungswissen / Themen",
            "3.4.3.2 / 3.5.3.2 Leseverstehen",
            "3.4.3.5 / 3.5.3.5 Schreiben",
            "3.4.4 / 3.5.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can produce a 60-90 minute Abitur Analysis task (~18 BE Basisfach / ~25 BE Leistungsfach) on a 1,000-1,200-word source.",
            "I can sustain integrated close reading across 3+ paragraphs with technical vocabulary.",
            "I can self-assess Sprache against Abitur expectations.",
        ],
        "leadin": (
            "Third of three Abitur-prep Units. Today's focus: "
            "the Analysis task — the section that rewards "
            "sustained close reading and Sprache range, and "
            "where Leistungsfach (advanced course) candidates "
            "are most clearly distinguished from Basisfach "
            "(basic course). 60 (BF) / 90 (LF) minutes. Submit. "
            "Debrief against Bewertungsraster."
        ),
        "activate": (
            "**Move scan.** Read the source. Identify three "
            "specific moves (rhetorical / structural / "
            "linguistic) you would build the Analysis around. "
            "Mark each as *strong / mid / weak*."
        ),
        "input_blocks": [
            ("Analysis — sub-task patterns",
             "1. **Analyse the writer's stance / argumentative "
             "strategy.** 3+ specific moves with integrated "
             "quotes.\n"
             "2. **Analyse the language / register / structural "
             "features.** Technical vocabulary + close reading.\n"
             "3. **Analyse the relationship between form and "
             "content.** (Leistungsfach only) — sustained "
             "argument across 3-4 paragraphs."),
            ("Sprache range — Analysis",
             "**Vocabulary:** *frame, register, syntax, "
             "diction, juxtaposition, parallelism, antithesis, "
             "irony, hedge, modal, periodic sentence, "
             "asyndeton, polysyndeton.*\n\n"
             "**Cohesion:** academic discourse markers, "
             "lexical chains, anaphoric reference.\n\n"
             "**Quote integration:** embedded fragments + "
             "integrated full quotes; no block-quotes."),
        ],
        "practise_g": [
            "1. Match: stance / strategy → 3+ moves; language / "
            "structure → technical close reading; form / "
            "content → LF only, sustained argument.",
            "2. T or F: block-quotes are rewarded in Analysis; "
            "technical vocabulary is rewarded in Analysis; LF "
            "Analysis is longer than BF Analysis.",
        ],
        "practise_m": [
            "3. Build a 5-sentence Analysis paragraph on a "
            "writer's argumentative strategy with 2 integrated "
            "quotes + 3 markers.",
        ],
        "answer_g": (
            "1. all true.\n"
            "2. F, T, T."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Abitur Analysis rehearsal, 60 (BF) / 90 (LF) "
            "minutes.** 1,000-1,200 word source + Analysis "
            "prompt. Submit. Debrief against Bewertungsraster."
        ),
        "produce_sample": (
            "(See *Reflection on the rehearsal* — the "
            "production task is the timed Analysis itself.)"
        ),
        "reflect": [
            "I can produce a 60-90 minute Abitur Analysis on a 1,000-1,200-word source.",
            "I can sustain integrated close reading with technical vocabulary.",
            "I can self-assess Sprache against Abitur expectations.",
        ],
        "pitfalls": [
            "Plot summary instead of analysis.",
            "Block-quoting instead of integrating.",
            "Sprache loss in the third paragraph because "
            "content-energy ran out.",
        ],
        "further": [
            "Bildungsplan-aligned Abitur-prep collections.",
            "Past Abitur papers (BW), with caution.",
        ],
        "exam_listening": (
            "**Analysis prompt** (sample): *On the basis of the "
            "1,000-1,200-word source provided in class, analyse "
            "the writer's argumentative strategy. Identify "
            "three specific rhetorical, structural, or "
            "linguistic moves and discuss what each contributes "
            "to the central argument. Use integrated quotation "
            "throughout. Word count: 350-450 (BF) / 450-550 "
            "(LF).*"
        ),
        "exam_reading": (
            "**Time budget.** Allocate the 60 (BF) / 90 (LF) "
            "minutes."
        ),
        "exam_use": (
            "**Reflection prompt:** *In 200 words, reflect on "
            "your Analysis rehearsal. Which moves did you "
            "identify most strongly? Which Sprache element did "
            "you lose toward the end?*"
        ),
        "exam_writing": "**(No Composition / Mediation in this Unit.)**",
        "exam_keys": [
            "**Comprehension.** Reward 3+ moves + integrated quotes + technical vocabulary + sustained close reading.",
            "**Analysis.** Suggested BF: 15 plan / 35 draft / 10 review. LF: 20 plan / 60 draft / 10 review.",
            "**Composition.** Open.",
            "**Reflection.** Open.",
        ],
    },
    {
        "n": 10, "slug": "kommunikationspruefung-full-mock",
        "title": "Kommunikationsprüfung: Full Mock",
        "skills": ["speaking", "listening", "language_awareness"],
        "bp": [
            "3.4.1 / 3.5.1 Soziokulturelles Orientierungswissen / Themen",
            "3.4.3.1 / 3.5.3.1 Hör-/Hörsehverstehen",
            "3.4.3.3 / 3.5.3.3 Sprechen – an Gesprächen teilnehmen",
            "3.4.3.4 / 3.5.3.4 Sprechen – zusammenhängendes monologisches Sprechen",
        ],
        "objectives": [
            "I can deliver a full-format Abitur Kommunikationsprüfung (~15 minutes total: 5-min monologue + 8-min dialogue + 2-min close).",
            "I can sustain academic-spoken register for fifteen minutes under pressure.",
            "I can self-assess against the official Abitur Bewertungsraster.",
        ],
        "leadin": (
            "Today is the full-format Kommunikationsprüfung mock. "
            "Mr. Yilmaz has invited a colleague to play the "
            "examiner-pair so the format matches the actual "
            "Abitur. 15 minutes per candidate. Stimulus drawn at "
            "random. Bewertungsraster (grading grid) used. The "
            "mock is itself the lesson."
        ),
        "activate": (
            "**Stimulus draw.** Each candidate draws a stimulus "
            "card. 5-minute prep period: outline a 5-min "
            "monologue with 3 movements + anticipated counter-"
            "questions."
        ),
        "input_blocks": [
            ("Full Komm-Prüfung format (~15 minutes)",
             "1. **Monologue (5 min).** Frame stimulus → 2-3 "
             "arguments → counter + concession → close.\n"
             "2. **Dialogue (8 min).** Examiner-pair asks 6-8 "
             "follow-ups. Candidate must rebut, concede, "
             "elaborate, connect to broader knowledge, and "
             "engage at least one cross-Unit theme.\n"
             "3. **Close (2 min).** Synthesis + final stance + "
             "one open question for the examiners.\n\n"
             "**Total ~15 minutes.**"),
            ("Bewertungsraster — Komm-Prüfung",
             "**Kommunikative Textgestaltung** (50 % BF, "
             "40 % LF): structure, coherence, addressee-"
             "awareness, conversation-management.\n\n"
             "**Sprachliche Korrektheit + Variabilität** "
             "(50 % BF, 60 % LF): vocabulary range, "
             "grammatical accuracy, idiomaticity, "
             "pronunciation, register-sensitivity."),
        ],
        "practise_g": [
            "1. Build a 4-line monologue opening from a stimulus "
            "(provided in class).",
            "2. Match Bewertungsraster category → focus: "
            "Textgestaltung → structure; Sprache → vocabulary + "
            "grammar.",
        ],
        "practise_m": [
            "3. Draft a full bullet outline for a 15-minute Komm-"
            "Prüfung performance.",
        ],
        "answer_g": "1. Open. 2. all true.",
        "answer_m": "3. Open.",
        "produce": (
            "**Full mock Komm-Prüfung.** 15 minutes per "
            "candidate. Examiner-pair scores using official "
            "Bewertungsraster. 5-minute debrief per candidate."
        ),
        "produce_sample": (
            "(See *Reflection on the mock* — the production "
            "task is the 15-minute oral exam itself.)"
        ),
        "reflect": [
            "I can deliver a 15-minute Komm-Prüfung at full Abitur format.",
            "I can sustain academic-spoken register under pressure.",
            "I can self-assess against the Bewertungsraster.",
        ],
        "pitfalls": [
            "Reading from prep notes during the monologue.",
            "Failing to connect across Units in the dialogue.",
            "Closing without one open question for the "
            "examiners.",
        ],
        "further": [
            "Bildungsplan-aligned Komm-Prüfung mock-stimulus "
            "collections.",
            "BBC Sounds — *Question Time* extracts (examiner-"
            "style follow-up rhythm).",
        ],
        "exam_listening": (
            "**Stimulus card** (sample): *A 2025 photograph "
            "of three school students in Mumbai working at an "
            "open-air computer cluster powered by a single "
            "solar panel. Caption: 'After school, before "
            "tutorial.' Speak for five minutes on what the "
            "image suggests about contemporary education and "
            "infrastructure. Then expect 8 minutes of examiner "
            "dialogue.*"
        ),
        "exam_reading": (
            "**Self-assessment prompt:** *In 250 words, "
            "self-assess your Komm-Prüfung performance against "
            "the official Bewertungsraster. Identify one "
            "Textgestaltung strength and one Sprache "
            "weakness.*"
        ),
        "exam_use": (
            "**Performance recording (in class).** Each "
            "candidate's 15-minute mock is recorded for self-"
            "review. Recording is destroyed after the debrief."
        ),
        "exam_writing": "**(No written Mediation in this Unit.)**",
        "exam_keys": [
            "**Comprehension.** Open. Reward structure + register + addressee-awareness + conversation-management.",
            "**Analysis.** Open. Reward Sprache range + idiomaticity + register-sensitivity.",
            "**Composition.** Open.",
            "**Mediation.** Open (in this case: self-assessment).",
        ],
    },
    {
        "n": 11, "slug": "issue-framed-debate",
        "title": "Issue-Framed Debate",
        "skills": ["speaking", "listening", "language_awareness"],
        "bp": [
            "3.4.1 / 3.5.1 Soziokulturelles Orientierungswissen / Themen",
            "3.4.3.1 / 3.5.3.1 Hör-/Hörsehverstehen",
            "3.4.3.3 / 3.5.3.3 Sprechen – an Gesprächen teilnehmen",
            "3.4.3.4 / 3.5.3.4 Sprechen – zusammenhängendes monologisches Sprechen",
        ],
        "objectives": [
            "I can deliver a 5-minute argued speech in an issue-framed debate, with one rebuttal of a specific previous-speaker claim.",
            "I can chair a 30-minute panel-format debate.",
            "I can synthesise a 3-minute closing statement for a team.",
        ],
        "leadin": (
            "Final speaking Unit. Mr. Yilmaz set up an issue-"
            "framed debate at quasi-Oxford-Union format: two "
            "teams of three, each speaker has 5 minutes, plus "
            "a 3-minute team closing. The motion: *This house "
            "would treat platform algorithms as public utilities "
            "subject to mandatory transparency.* The debate "
            "lasts 30 minutes and is chaired by a student."
        ),
        "activate": (
            "**Argument-stack scan.** Teams of three. Each "
            "team prepares 3 strongest arguments for their side "
            "+ 3 anticipated rebuttals."
        ),
        "input_blocks": [
            ("Debate format (~30 minutes)",
             "1. **Proposition Speaker 1 (5 min).** Frame motion "
             "+ 1st argument.\n"
             "2. **Opposition Speaker 1 (5 min).** Frame counter "
             "+ 1st argument + 1 rebuttal.\n"
             "3. **Proposition Speaker 2 (5 min).** 2nd argument "
             "+ 2 rebuttals.\n"
             "4. **Opposition Speaker 2 (5 min).** 2nd argument "
             "+ 2 rebuttals.\n"
             "5. **Proposition Speaker 3 closing (3 min).** "
             "Synthesis + final urge.\n"
             "6. **Opposition Speaker 3 closing (3 min).** "
             "Synthesis + final urge."),
            ("Chair role",
             "**Chair (1 student):** introduces motion, calls "
             "speakers, manages time, opens floor for 2 short "
             "questions per team, calls the close. Chair must "
             "remain neutral on the motion."),
        ],
        "practise_g": [
            "1. Match: Speaker 1 → frame + 1st argument; "
            "Speaker 2 → 2nd argument + rebuttals; Speaker 3 "
            "closing → synthesis + urge.",
            "2. T or F: chair argues the motion; rebuttals must "
            "name the specific previous-speaker claim; closing "
            "speaker can introduce a new argument.",
        ],
        "practise_m": [
            "3. Draft Speaker 2's bullets: 2nd argument + 2 "
            "named rebuttals.",
        ],
        "answer_g": (
            "1. all true.\n"
            "2. F (chair is neutral), T, F (no new arguments in "
            "closing — synthesis only)."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Class issue-framed debate (30 minutes).** Two "
            "teams of three + chair. Audience scores each "
            "speaker on Bewertungsraster (Textgestaltung + "
            "Sprache). Class debrief at the end."
        ),
        "produce_sample": (
            "*Madam Chair, I'd like to argue in favour of the "
            "motion. Firstly, the available evidence suggests "
            "that platform algorithms — like electricity grids "
            "before them — produce systematic externalities "
            "(privacy erosion, attention rents, civic-discourse "
            "distortion) that the market has consistently "
            "under-priced. Accordingly, the structural "
            "comparison to public utilities is not metaphor; it "
            "is policy. Secondly, the regulatory experience of "
            "energy and telecoms shows that mandatory "
            "transparency (capacity reporting, allocation "
            "reporting, tariff publication) is a precondition "
            "of competition rather than its enemy. Speaker 1 "
            "of the opposition will, I anticipate, claim that "
            "transparency requirements would expose trade "
            "secrets. I accept that some transparency designs "
            "would; the OFT-style compromise of the 1990s "
            "energy privatisation showed that *commercial-in-"
            "confidence aggregation* permits both transparency "
            "and competition. By contrast with the opposition's "
            "expected framing, the motion does not require "
            "open-source algorithms; it requires aggregate "
            "amplification reporting. In response to the "
            "anticipated *innovation* counter-argument, I "
            "would point out, more specifically, that the "
            "regulated-utility comparison has not historically "
            "killed innovation — it has redirected it toward "
            "infrastructure improvement. To summarise: the "
            "motion is moderate, the comparison is "
            "structural, and the precedent exists. I urge "
            "this house to support the motion.*"
        ),
        "reflect": [
            "I can deliver a 5-minute argued speech in issue-framed format with one specific rebuttal.",
            "I can chair a 30-minute panel debate.",
            "I can synthesise a 3-minute team closing.",
        ],
        "pitfalls": [
            "Generic rebuttals; name the specific previous-"
            "speaker claim.",
            "New arguments in closing; synthesis only.",
            "Chair drift toward one side.",
        ],
        "further": [
            "ESU (English-Speaking Union) — student debate "
            "footage.",
            "Oxford Union — selected debate recordings (with "
            "caution: register varies).",
        ],
        "exam_listening": (
            "Listen / read twice the Speaker-1-in-favour sample "
            "above.\n\n"
            "1. Frame: ___ . 2. Two arguments: ___ . 3. "
            "Anticipated rebuttal: ___ . 4. Final urge: ___ ."
        ),
        "exam_reading": (
            "Read the sample speech above.\n\n"
            "1. Structural comparison: ___ . 2. Specific "
            "rebuttal: ___ . 3. Concession + qualifying move: "
            "___ . 4. Closing summary: ___ ."
        ),
        "exam_use": (
            "**Composition prompt:** *Write Speaker 2 of the "
            "opposition's 5-minute speech (~400 words). Use 5 "
            "debate signposts + 2 named rebuttals + 1 cleft.*"
        ),
        "exam_writing": (
            "**Reflection prompt:** *In 200 words, reflect on "
            "your performance in the class debate. Which "
            "Bewertungsraster category was strongest? Which "
            "needs the most rehearsal before the actual "
            "Komm-Prüfung?*"
        ),
        "exam_keys": [
            "**Comprehension.** 1. platform algorithms as public utilities; 2. systematic externalities + transparency-as-precondition-of-competition; 3. transparency would expose trade secrets; 4. *I urge this house to support the motion*.",
            "**Analysis.** 1. platform algorithms as public utilities (energy / telecoms parallel); 2. *commercial-in-confidence aggregation* OFT-style compromise; 3. *some designs would expose trade secrets, but…*; 4. *the motion is moderate, the comparison is structural, and the precedent exists*.",
            "**Composition.** Open.",
            "**Reflection.** Open.",
        ],
    },
    {
        "n": 12, "slug": "year-review-and-handover",
        "title": "Year Review and Handover",
        "skills": ["writing", "speaking", "language_awareness"],
        "bp": [
            "3.4.1 / 3.5.1 Soziokulturelles Orientierungswissen / Themen",
            "3.4.3.4 / 3.5.3.4 Sprechen – zusammenhängendes monologisches Sprechen",
            "3.4.3.5 / 3.5.3.5 Schreiben",
            "3.4.4 / 3.5.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can compile a graduation portfolio with 6 representative pieces from Klasse 11-13.",
            "I can write a 400-word year-review reflection demonstrating Abitur-grade Sprache range.",
            "I can deliver a 5-minute graduation talk + write a 300-word forward letter to my post-Abitur self.",
        ],
        "leadin": (
            "The final Unit. The Abitur is in two months. "
            "Today's task: compile a portfolio of six pieces "
            "from Klasse 11-13, write a 400-word reflection, "
            "deliver a 5-minute graduation talk, and write a "
            "300-word forward letter to the post-Abitur self. "
            "Mr. Yilmaz said, characteristically: *the talk is "
            "the celebration; the letter is the receipt.*"
        ),
        "activate": (
            "**Pick-six scan.** Open the three folders (Kl. 11, "
            "12, 13). Pick six pieces — two per year. Label "
            "each: *proudest / surprised me / didn't work / "
            "would rewrite / connects to next step / single "
            "best paragraph*."
        ),
        "input_blocks": [
            ("Final portfolio structure",
             "1. **Cover sheet** — name, year, three-line "
             "intellectual self-portrait, intended path.\n"
             "2. **Six pieces** (one-line label each, two per "
             "year).\n"
             "3. **Reflection** (400 words: arc across three "
             "years, three specific moments of progress, one "
             "disappointment, one connection to post-Abitur "
             "life).\n"
             "4. **Talk** (5 minutes; two quotes from your own "
             "writing; one cross-Unit synthesis).\n"
             "5. **Forward letter** (300 words to the post-"
             "Abitur self)."),
            ("Reflection — useful frames",
             "*At the start of Klasse 11 I … / By the end of "
             "Klasse 12 I had begun to … / The piece that "
             "surprised me most was … because … / The piece "
             "that didn't work taught me that … / The thread I "
             "want to keep going is … / Whichever path I take "
             "after May, the most useful skill from these "
             "three years is …*"),
        ],
        "practise_g": [
            "1. Build the six labels for your portfolio.",
        ],
        "practise_m": [
            "2. Build a 8-line reflection draft using mixed "
            "tenses (past simple, past perfect, present "
            "perfect, present perfect continuous, future "
            "perfect, third conditional, mixed conditional).",
        ],
        "answer_g": "Open.",
        "answer_m": "Open.",
        "produce": (
            "**Final portfolio + 400-word reflection + 5-min "
            "graduation talk + 300-word forward letter.** Submit "
            "the portfolio. Deliver the talk to the class. "
            "Audience gives one feedback sentence per talk. "
            "The reflection and forward letter are private to "
            "the student and Mr. Yilmaz."
        ),
        "produce_sample": (
            "*At the start of Klasse 11 I wrote in three modes: "
            "translated, formal, and quietly imitating other "
            "people. By the end of Klasse 12 I had begun to "
            "write in a fourth mode that I would call *paying "
            "attention*. The piece that surprised me most is "
            "the *Late Bus, Cold Bench* essay from Klasse 10; "
            "it taught me that the smallest stylistic moves "
            "often do the most analytical work. By contrast, "
            "the piece that didn't work was my first "
            "*Macbeth* close reading; I summarised the "
            "rhetorical moves rather than analysing them. If "
            "I had written that essay six months later, I "
            "would have noticed the verse-rhythm collapse in "
            "5.5 — what I now think is the heart of the "
            "soliloquy. By the end of the Oberstufe, I will "
            "have written somewhere between 35 and 45 essays "
            "longer than this one. The thread I want to keep "
            "going is *naming the limitation* — both in "
            "writing and in speaking. I have decided to "
            "study English literature alongside political "
            "science. Whichever way the next three years go, "
            "the most useful skill from Klasse 11-13, in my "
            "reading, is the small repeated discipline of "
            "writing one careful paragraph rather than three "
            "confident ones. I owe that, mostly, to the slow "
            "lanes of Klasse 10. The Abitur is in two months. "
            "I am, on reflection, more nervous than I was a "
            "year ago — because I now have a better sense of "
            "what I would like to be able to do, and a "
            "clearer view of what I cannot yet do. That "
            "asymmetry is, I think, the right amount of "
            "nervousness.*"
        ),
        "reflect": [
            "I can compile a 6-piece graduation portfolio across three years.",
            "I can write a 400-word year-review reflection at Abitur-grade Sprache.",
            "I can deliver a 5-minute graduation talk + 300-word forward letter.",
        ],
        "pitfalls": [
            "Reading the talk verbatim.",
            "Generic claims (*I learned a lot*) without specific "
            "examples.",
            "Forward letter that flatters rather than instructs "
            "the post-Abitur self.",
        ],
        "further": [
            "BBC Bitesize — *Reflective writing* (later "
            "secondary).",
            "British Council — *Self-evaluation* materials.",
        ],
        "exam_listening": (
            "Listen twice to the sample reflection above.\n\n"
            "1. Three Klasse-11 modes: ___ . 2. Klasse-12 "
            "shift: ___ . 3. Klasse-10 piece named: ___ . 4. "
            "Final commit: ___ ."
        ),
        "exam_reading": (
            "Read the sample reflection above.\n\n"
            "1. Four writing modes across three years: ___ . "
            "2. Most surprising piece + reason: ___ . 3. "
            "Lesson learnt: ___ . 4. Decision: ___ ."
        ),
        "exam_use": (
            "**Mixed grammar review.**\n\n"
            "1. By Klasse 12 I __________ (begin) a fourth "
            "mode. (past perfect)\n"
            "2. If I __________ (write) that essay six months "
            "later, I __________ (notice) the verse-rhythm "
            "collapse. (third)\n"
            "3. By the end of Oberstufe, I __________ (write) "
            "35-45 longer essays. (future perfect)\n"
            "4. The asymmetry between knowing-what-I-want and "
            "knowing-what-I-cannot-do is ___ ."
        ),
        "exam_writing": (
            "Write 400 words: a year-review reflection across "
            "Klasse 11-13. Use 6 grammar points + 2 quotes "
            "from your own writing."
        ),
        "exam_keys": [
            "**Comprehension.** 1. translated / formal / imitating; 2. *paying attention*; 3. *Late Bus, Cold Bench* essay; 4. study English literature alongside political science.",
            "**Analysis.** 1. translated, formal, imitating, paying attention; 2. *Late Bus, Cold Bench* — smallest stylistic moves do the most analytical work; 3. naming the limitation; 4. study English literature + political science.",
            "**Composition.** had begun / had written-would have noticed / will have written / the right amount of nervousness.",
            "**Reflection.** Open.",
        ],
    },
]


UNIT_TPL = """---
title: "Unit {n} — {title}"
subtitle: "Track E · Klasse 13 · Niveau E (Basisfach / Leistungsfach) · Abitur year"
niveau: "E"
klassenstufe: 13
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
**Niveau:** E. Abitur (school-leaving examination) Klausur prep
across the year.\\
**Course tagging:** basic course (Basisfach, E-BF) and advanced
course (Leistungsfach, E-LF).
:::

{{{{< downloads >}}}}

## Learning objectives

{objectives}

## curriculum framework (Bildungsplan) alignment

{bp_bullets}

(Sources: <https://www.bildungsplaene-bw.de/,Lde/LS/BP2016BW/ALLG/GYM/E1/IK/11-12-LF> /
<https://www.bildungsplaene-bw.de/,Lde/LS/BP2016BW/ALLG/GYM/E1/IK/11-12-BF>)

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
**Slide deck timing.** 90 minutes total (Doppelstunde — typical
in the Oberstufe). Lead-in 6 min · Activate 8 min · Input 25 min
· Practise 15 min · Produce 30 min · Reflect 6 min.

**Differentiation.** Basisfach (basic course): tighter argument,
clearer moves. Leistungsfach (advanced course): sustained
analysis, integrated quotation, complex thesis. Some Klasse 13
Units (e.g. Unit 9 Analysis) explicitly differentiate by
candidate path.
:::

## Common pitfalls

{pitfalls}

## Further reading / listening

{further}
"""

EXAM_BODY_TPL = """::: {{.callout-warning icon=false title="Klausur (assessment) — Niveau E (Abitur-grade)"}}
**This Unit's exam example follows the Abitur task pattern named
in the Unit. Some Units focus on a single Abitur-task type
(Comprehension / Analysis / Composition / Mediation /
Kommunikationsprüfung); the full 90-BE Klausur is rehearsed in
Klasse 12 Units 11-12 and continues in Klasse 13 Units 7-9.**\\
**Inhalt / Sprache split.** Basisfach (basic course): 50/50.
Leistungsfach (advanced course): 40/60.
:::

### Comprehension

{exam_listening}

### Analysis

{exam_reading}

### Composition / Mediation / Reflection

{exam_use}

### Additional task

{exam_writing}

::: {{.callout-tip collapse="true" title="Expected-answer profile (Erwartungshorizont) — sample"}}
{exam_keys}
:::

::: {{.callout-tip collapse="true" title="grading scale (Notenschlüssel) — Abitur-grade Klausuren"}}
| 86–90 | 1+ | 81–85 | 1   | 76–80 | 1- |
| 71–75 | 2+ | 66–70 | 2   | 61–65 | 2- |
| 56–60 | 3+ | 51–55 | 3   | 46–50 | 3- |
| 41–45 | 4+ | 36–40 | 4   | 30–35 | 4- |
| 22–29 | 5  |  0–21 | 6   |       |    |

(Single-section Klausuren in this year scale to the proportional
BE-weight of the section in the full Klausur.)
:::
"""

EXAM_WRAP_TPL = """---
title: "Klausur (assessment) — Unit {n}: {title}"
subtitle: "Track E · Klasse 13 · Niveau E · Abitur-prep"
author: "S. Le Boulanger"
niveau: "E"
klassenstufe: 13
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

# Klausur (assessment) — Unit {n}: {title}

**Track E · Klasse 13 · Niveau E · Abitur-prep**

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

    print(f"Wrote {len(UNITS) * 3} files for Track E Klasse 13.")


if __name__ == "__main__":
    emit()
