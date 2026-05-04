"""Batch-emit Track E Klasse 12 — all 12 Units (Oberstufe).

Klasse 12 voice: discourse and analysis, exam-grade. Cast: *texts
as characters* — speakers, writers, public voices. curriculum
framework (Bildungsplan) prefixes 3.4 (advanced course /
Leistungsfach) + 3.5 (basic course / Basisfach).

Klausur (assessment) format same as Klasse 11: 90 BE,
Comprehension + Analysis + Composition + Mediation. Klasse 12
includes a full Kommunikationsprüfung mock (Unit 10) and two
distinct Klausur-prep Units (11: Comprehension + Analysis; 12:
Composition + Comment).
"""
from __future__ import annotations
import pathlib

REPO = pathlib.Path(__file__).resolve().parent.parent
COURSE = REPO / "track_e_kl12" / "units"

UNITS = [
    {
        "n": 1, "slug": "dystopias", "title": "Dystopias",
        "skills": ["reading", "writing", "intercultural"],
        "bp": [
            "3.4.1 / 3.5.1 Soziokulturelles Orientierungswissen / Themen",
            "3.4.3.2 / 3.5.3.2 Leseverstehen",
            "3.4.3.5 / 3.5.3.5 Schreiben",
            "3.4.4 / 3.5.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can read extracts from three canonical dystopias (Orwell, Huxley, Atwood) and identify each text's central control mechanism.",
            "I can use the vocabulary of literary dystopia (*surveillance, complicity, conditioning, dehumanisation, language control*).",
            "I can write a 350-word comparative literary essay tracing one motif across three texts.",
        ],
        "leadin": (
            "The class opened the dystopia unit with three short "
            "extracts, one from each of *1984* (Orwell, 1949), "
            "*Brave New World* (Huxley, 1932), and *The "
            "Handmaid's Tale* (Atwood, 1985). The shared question: "
            "*by what means does each regime control its "
            "citizens?* The class noticed quickly that the answer "
            "was different in each — surveillance, conditioning, "
            "and ritual were not interchangeable."
        ),
        "activate": (
            "**Mechanism scan.** With your partner, list 5 "
            "control mechanisms a dystopian regime might use. Mark "
            "each as *physical / psychological / linguistic*."
        ),
        "input_blocks": [
            ("Reading — three extracts (paraphrased)",
             "*Orwell — 1984:* The telescreen watched and "
             "broadcast simultaneously; Newspeak was designed to "
             "narrow the range of thought.\n\n"
             "*Huxley — Brave New World:* Conditioning began in "
             "the bottle; soma dissolved discontent without "
             "argument; pleasure replaced suppression.\n\n"
             "*Atwood — The Handmaid's Tale:* Ritual replaced "
             "law; reading was forbidden to women; the regime's "
             "language was scripture-coded ('Blessed be the "
             "fruit')."),
            ("Vocabulary — literary dystopia",
             "*surveillance, complicity, conditioning, "
             "dehumanisation, ritualisation, language control, "
             "doublespeak, totalitarianism, theocracy, "
             "biopolitics, complicity-of-the-comfortable, "
             "disciplinary apparatus, internal exile.*"),
        ],
        "practise_g": [
            "1. Match: 1984 → ?, Brave New World → ?, The "
            "Handmaid's Tale → ?",
            "2. T or F: Orwell's regime forbids pleasure; "
            "Huxley's regime weaponises pleasure; Atwood's regime "
            "uses scripture-coded language.",
        ],
        "practise_m": [
            "3. Build 4 close-reading sentences using literary-"
            "dystopia vocabulary on the three extracts.",
        ],
        "answer_g": (
            "1. surveillance + linguistic / conditioning + "
            "pharmacological / ritual + scriptural.\n"
            "2. F (Orwell suppresses dissent — pleasure is not "
            "the lever), T, T."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Comparative literary essay, 350 words.** Trace one "
            "motif (language, ritual, surveillance) across the "
            "three texts. Use 3 integrated quotes + 5 academic "
            "discourse markers + 1 cleft."
        ),
        "produce_sample": (
            "*The motif of *language as instrument of control* "
            "appears in all three canonical dystopias under "
            "discussion, but its function differs sharply. In "
            "Orwell's *1984*, Newspeak is engineered to *narrow "
            "the range of thought* — a deliberate, top-down "
            "linguistic project whose end-point is the "
            "impossibility of dissent. In Huxley's *Brave New "
            "World*, by contrast, the controlling language is "
            "advertising-bright: *a gramme is better than a "
            "damn*. The regime does not narrow vocabulary; it "
            "drowns dissent in cheerful, repetitive, "
            "consumer-coded phrases. Accordingly, Huxley's "
            "linguistic critique anticipates a register "
            "Orwell could not have predicted: the marketing "
            "register. In Atwood's *The Handmaid's Tale*, "
            "language control takes a third form: scripture. "
            "Greetings — *Blessed be the fruit*; *May the Lord "
            "open* — replace ordinary speech, and the substitution "
            "is itself the regime's primary instrument. It is "
            "precisely this that makes Atwood's dystopia harder "
            "for the contemporary reader to pre-emptively "
            "reject: many readers grew up inside scripture-coded "
            "speech and recognise the rhythm without recognising "
            "the politics. More specifically, what each text is "
            "doing with language is different in kind, not "
            "merely in degree. Orwell shrinks; Huxley dilutes; "
            "Atwood ritualises. In this regard, the three texts "
            "function as a triangle: each names a control "
            "mechanism the others under-name. The reader's task "
            "is not to choose the most accurate dystopia but to "
            "notice that contemporary regimes typically deploy "
            "all three at once, calibrated to local conditions. "
            "The dystopian canon is, finally, less a prediction "
            "and more a vocabulary.*"
        ),
        "reflect": [
            "I can identify each text's central control mechanism.",
            "I can use 6+ literary-dystopia vocabulary terms.",
            "I can write a 350-word comparative literary essay.",
        ],
        "pitfalls": [
            "Don't conflate the three regimes — name what is "
            "specific to each.",
            "Don't read dystopias as predictions only — they are "
            "vocabularies.",
            "Quote integration matters more in LF register.",
        ],
        "further": [
            "George Orwell, *1984* (1949).",
            "Aldous Huxley, *Brave New World* (1932).",
            "Margaret Atwood, *The Handmaid's Tale* (1985); also "
            "*The Testaments* (2019).",
        ],
        "exam_listening": (
            "Read the *1984* opening (paraphrased above) and "
            "answer:\n\n"
            "1. The telescreen does what two things "
            "simultaneously? 2. Newspeak is designed to do what? "
            "3. The regime's primary linguistic move: ___ . 4. "
            "How does Orwell's regime differ from Huxley's? ___ ."
        ),
        "exam_reading": (
            "Read the *Brave New World* paraphrase and answer:\n\n"
            "1. Where does conditioning begin? 2. What is the "
            "function of soma? 3. Pleasure plays what role? 4. "
            "Compared with Orwell, what is the linguistic "
            "register?"
        ),
        "exam_use": (
            "**Composition prompt:** *Choose one motif. Trace "
            "it across the three dystopias in 250 words. Use 2 "
            "integrated quotes + 3 academic discourse markers + "
            "1 cleft.*"
        ),
        "exam_writing": (
            "**Mediation prompt:** A German review of *The "
            "Handmaid's Tale* describes the novel as *'eine "
            "Warnung mit langer Halbwertszeit'*. Mediate a 250-"
            "word German source for an English-speaking literary "
            "magazine. (Source provided in class.)"
        ),
        "exam_keys": [
            "**Comprehension.** 1. watches AND broadcasts; 2. narrow the range of thought; 3. shrinking vocabulary (Newspeak); 4. Orwell suppresses dissent through linguistic narrowing; Huxley dilutes dissent through pleasure.",
            "**Analysis.** 1. in the bottle (pre-natal conditioning); 2. dissolves discontent without argument; 3. weaponised — pleasure is the control lever; 4. advertising-bright / consumer-coded register.",
            "**Composition.** Open. Reward thesis + integrated quotes.",
            "**Mediation.** Open. Reward register, hedge preservation, cultural notes.",
        ],
    },
    {
        "n": 2, "slug": "globalisation-debates",
        "title": "Globalisation Debates",
        "skills": ["reading", "writing", "intercultural"],
        "bp": [
            "3.4.1 / 3.5.1 Soziokulturelles Orientierungswissen / Themen",
            "3.4.2 / 3.5.2 Interkulturelle kommunikative Kompetenz",
            "3.4.3.2 / 3.5.3.2 Leseverstehen",
            "3.4.3.5 / 3.5.3.5 Schreiben",
            "3.4.4 / 3.5.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can read short pro and contra positions on globalisation and identify the empirical claim each side hangs on.",
            "I can use the vocabulary of contested-policy debate (*supply chain, inequality, externality, comparative advantage, regulatory race*).",
            "I can write a 350-word op-ed that holds two readings of globalisation in productive tension.",
        ],
        "leadin": (
            "The class read a 2025 review piece in *The Economist* "
            "summarising twenty years of globalisation debates. "
            "The piece opened with a number — *world trade as a "
            "share of GDP rose from 39 % in 1990 to 60 % by "
            "2008* — and a counter-number — *and has plateaued "
            "since*. The class spent the lesson learning to read "
            "those two numbers as the same fact."
        ),
        "activate": (
            "**Position scan.** With your partner, list 3 "
            "arguments for and 3 against globalisation that you "
            "would actually defend. Mark each as *empirical / "
            "normative / both*."
        ),
        "input_blocks": [
            ("Reading — *Twenty Years of Globalisation*",
             "*World trade as a share of GDP rose from 39 % in "
             "1990 to 60 % by 2008. It has plateaued since. The "
             "supporters of the post-1990 trade order point to "
             "the lifting of approximately one billion people out "
             "of extreme poverty over the same period — "
             "predominantly in East and South Asia. Critics "
             "respond that intra-country inequality in advanced "
             "economies grew sharply, that supply-chain fragility "
             "was severely under-priced before 2020, and that "
             "environmental externalities were systematically "
             "exported. Both sides hang on empirical claims that "
             "are roughly correct.*"),
            ("Vocabulary — globalisation debate",
             "*supply chain, comparative advantage, "
             "regulatory race / race to the bottom, "
             "externality, intra-country inequality, "
             "trade order, deindustrialisation, reshoring, "
             "near-shoring, friend-shoring, decoupling, "
             "fragmentation, geo-economic.*"),
        ],
        "practise_g": [
            "1. Match: comparative advantage → trade theory; "
            "externality → unpriced cost; reshoring → moving "
            "production back home.",
            "2. T or F: *world trade as a share of GDP* rose from "
            "39 % to 60 % between 1990 and 2008; intra-country "
            "inequality fell in advanced economies during the "
            "same period.",
        ],
        "practise_m": [
            "3. Build 4 sentences using 4 globalisation-debate "
            "terms.",
        ],
        "answer_g": (
            "1. all true.\n"
            "2. T, F (intra-country inequality grew in advanced "
            "economies)."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Op-ed, 350 words.** Hold two readings of "
            "globalisation in tension. Use 5 globalisation-debate "
            "terms + 2 academic hedges + 1 cleft + 1 *despite* / "
            "*given that*."
        ),
        "produce_sample": (
            "*The two strongest arguments about post-1990 "
            "globalisation are both empirical and both roughly "
            "correct, which makes the debate harder, not easier. "
            "It is precisely the simultaneous truth of *one "
            "billion people lifted out of extreme poverty* and "
            "*intra-country inequality in advanced economies "
            "growing sharply* that has produced the curiously "
            "polarised politics of the 2020s. The available "
            "evidence suggests that comparative advantage worked "
            "broadly as the textbooks promised: countries "
            "specialised, output grew, and aggregate welfare in "
            "many regions improved. By contrast, the "
            "distributional question — who, within a country, "
            "captured the gains — was systematically under-asked. "
            "Accordingly, supply-chain fragility was severely "
            "under-priced before 2020. Externalities were "
            "exported; the regulatory race to the bottom on "
            "labour and environmental standards was real. Given "
            "that the politics has now shifted toward reshoring, "
            "near-shoring, and friend-shoring, the more useful "
            "question is not *was globalisation good or bad?* "
            "but *what would the next two decades have to look "
            "like to capture the aggregate gains without "
            "exporting the costs?* The honest answer involves "
            "instruments that are not yet in place — carbon "
            "border adjustments, social-investment funds in "
            "regions hit by deindustrialisation, supply-chain "
            "redundancy buffers. Despite the loud debate, the "
            "interesting work is engineering, not slogans. "
            "Caution is warranted; complacency is not.*"
        ),
        "reflect": [
            "I can identify the empirical claim each side hangs on.",
            "I can use 5+ globalisation-debate terms.",
            "I can write a 350-word op-ed holding two readings in tension.",
        ],
        "pitfalls": [
            "Don't reduce globalisation to one number.",
            "*Race to the bottom* is contested as a description "
            "— flag it.",
            "Both-sidesing without a stake is weak.",
        ],
        "further": [
            "Dani Rodrik, *Straight Talk on Trade* (accessible "
            "chapters).",
            "The Economist — globalisation special reports.",
        ],
        "exam_listening": (
            "Listen / read twice.\n\n"
            "> \"World trade as a share of GDP rose from 39 % in "
            "1990 to 60 % by 2008. It has plateaued since. About "
            "one billion people were lifted out of extreme "
            "poverty in the same period, predominantly in East "
            "and South Asia. Intra-country inequality grew in "
            "advanced economies. Supply-chain fragility was "
            "under-priced.\"\n\n"
            "1. Trade %: ___ . 2. Plateau: ___ . 3. Poverty "
            "reduction: ___ . 4. Hidden cost: ___ ."
        ),
        "exam_reading": (
            "Read the *Twenty Years of Globalisation* extract.\n\n"
            "1. The two simultaneous facts: ___ . 2. Where the "
            "poverty reduction happened: ___ . 3. Three critics' "
            "claims: ___ . 4. The author's neutral move: ___ ."
        ),
        "exam_use": (
            "**Composition prompt:** *Choose one of the three "
            "critics' claims. Defend or refute it in 250 words "
            "using 2 academic hedges + 3 markers.*"
        ),
        "exam_writing": (
            "**Mediation prompt:** A 250-word German economic-"
            "policy paper on *Lieferkettenresilienz* "
            "(supply-chain resilience). Mediate for a English-"
            "speaking trade-policy reader. (Source provided in "
            "class.)"
        ),
        "exam_keys": [
            "**Comprehension.** 1. 39→60 %; 2. since 2008; 3. ~1 billion in East/South Asia; 4. supply-chain fragility under-priced.",
            "**Analysis.** 1. ~1 billion lifted out of extreme poverty AND intra-country inequality grew sharply; 2. East and South Asia; 3. inequality grew / supply-chain fragility under-priced / externalities exported; 4. *both sides hang on claims that are roughly correct*.",
            "**Composition.** Open. Reward integrated argument + hedges.",
            "**Mediation.** Open.",
        ],
    },
    {
        "n": 3, "slug": "science-and-ethics",
        "title": "Science and Ethics",
        "skills": ["reading", "writing", "language_awareness"],
        "bp": [
            "3.4.1 / 3.5.1 Soziokulturelles Orientierungswissen / Themen",
            "3.4.3.2 / 3.5.3.2 Leseverstehen",
            "3.4.3.5 / 3.5.3.5 Schreiben",
            "3.4.4 / 3.5.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can read short ethics-of-science texts (CRISPR, large language models, climate intervention) and identify the consequentialist and deontological moves.",
            "I can use vocabulary of science ethics (*precautionary principle, dual use, informed consent, moratorium, governance*).",
            "I can write a 350-word science-ethics essay with a structured ethical argument.",
        ],
        "leadin": (
            "Mr. Yilmaz set three short ethics-of-science texts: "
            "one on CRISPR germline editing, one on large "
            "language models and academic integrity, one on "
            "climate intervention research (stratospheric aerosol "
            "injection). The class noticed quickly that all three "
            "debates rotated around the same question — *who "
            "decides what we are not allowed to find out?*"
        ),
        "activate": (
            "**Ethics scan.** With your partner, list 3 scientific "
            "research areas you think should be regulated more "
            "strictly. Mark each with the strongest argument for "
            "and against."
        ),
        "input_blocks": [
            ("Reading — *Three Ethics Frames* (paraphrased)",
             "*Consequentialism* asks *what produces the best "
             "outcomes?* — including risks, who bears them, and "
             "across what time horizon. *Deontology* asks *what "
             "are we required to do regardless of "
             "consequences?* — informed consent, dignity, "
             "irreversible-harm thresholds. *Virtue ethics* asks "
             "*what kind of researcher / institution do we want "
             "to be?*. Real-world ethics-of-science debates "
             "almost always combine all three; pretending the "
             "debate is purely consequentialist is itself a "
             "philosophical position.*"),
            ("Vocabulary — science ethics",
             "*precautionary principle, dual-use research, "
             "informed consent, moratorium, governance, "
             "irreversibility, externality, stakeholder "
             "engagement, transparency, peer review, "
             "replication, bioethics committee, IRB.*"),
        ],
        "practise_g": [
            "1. Match: precautionary principle → caution under "
            "uncertainty; dual use → research with both civilian "
            "and military potential; moratorium → temporary halt.",
            "2. T or F: consequentialism rules out informed "
            "consent; deontology rules out cost-benefit thinking.",
        ],
        "practise_m": [
            "3. Build 4 sentences applying consequentialist + "
            "deontological + virtue-ethics moves to the CRISPR "
            "case.",
        ],
        "answer_g": (
            "1. all true.\n"
            "2. F (consequentialism includes consent under "
            "expected-value), F (deontology accepts cost-benefit "
            "as a secondary tool, not primary)."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Science-ethics essay, 350 words.** Pick one case "
            "(CRISPR / LLMs / climate intervention). Build a "
            "structured argument with one consequentialist move "
            "+ one deontological move + one virtue-ethics move + "
            "one disagreement / acknowledgement. Use 4 academic "
            "discourse markers + 1 cleft."
        ),
        "produce_sample": (
            "*The CRISPR-Cas9 germline editing debate is "
            "instructive precisely because all three major ethics "
            "frames push in slightly different directions, and "
            "the resulting policy must be assembled from their "
            "overlap. The consequentialist case for some forms "
            "of germline editing is, on its own terms, strong: "
            "if a single safe intervention can prevent "
            "Huntington's disease in a future child, the expected "
            "welfare gain is large and the risk profile, with "
            "current CRISPR-Cas9 v3 protocols, is modest. By "
            "contrast, the deontological objection is also "
            "strong: the future child cannot consent, and the "
            "principle of informed consent has, since the "
            "Belmont Report (1979), been a non-negotiable in "
            "human-subject research. Accordingly, the most "
            "useful frame here is the precautionary principle — "
            "not the strong version (any risk, no action) but "
            "the weak version (irreversible-harm thresholds plus "
            "stakeholder engagement). The virtue-ethics question "
            "— *what kind of researcher community do we want?* — "
            "tilts toward a moratorium-with-review, partly "
            "because the researcher community after the He "
            "Jiankui case (2018) has, on reflection, agreed that "
            "the breach of governance norms was itself the "
            "primary harm. It is precisely this institutional "
            "self-correction that makes the moratorium-with-"
            "review frame defensible. In this regard, the case "
            "is not *for or against germline editing* but *for "
            "or against doing it inside a peer-reviewed, "
            "consent-respecting governance structure*. The "
            "honest answer is conditional. Some applications, "
            "with strong governance, may be permissible; others, "
            "without it, are not. The frame is what travels.*"
        ),
        "reflect": [
            "I can identify consequentialist, deontological, and virtue-ethics moves.",
            "I can use 6+ science-ethics terms.",
            "I can write a 350-word structured science-ethics essay.",
        ],
        "pitfalls": [
            "Don't reduce ethics-of-science to *yes / no*.",
            "Precautionary principle has a strong and a weak "
            "version — flag which.",
            "Don't quote ethics jargon; integrate it.",
        ],
        "further": [
            "Henry T. Greely, *CRISPR People* (accessible "
            "chapters).",
            "The Atlantic — *Tech Ethics* essays.",
        ],
        "exam_listening": (
            "Read twice.\n\n"
            "> \"Consequentialism asks what produces the best "
            "outcomes; deontology asks what we are required to "
            "do regardless of consequences; virtue ethics asks "
            "what kind of researcher we want to be. Real "
            "debates combine all three.\"\n\n"
            "1. Consequentialism: ___ . 2. Deontology: ___ . 3. "
            "Virtue ethics: ___ . 4. Real debates: ___ ."
        ),
        "exam_reading": (
            "Read the *Three Ethics Frames* paraphrase above.\n\n"
            "1. Consequentialism's question: ___ . 2. "
            "Deontology's commitments: ___ . 3. Virtue ethics' "
            "question: ___ . 4. Why combining frames is itself "
            "philosophical: ___ ."
        ),
        "exam_use": (
            "**Composition prompt:** *Apply the three frames to "
            "large language models in academic writing in 250 "
            "words. Use 2 markers + 1 cleft.*"
        ),
        "exam_writing": (
            "**Mediation prompt:** A 300-word German position "
            "paper from a Bioethik-Kommission. Mediate for an "
            "English-speaking science-policy reader. (Source "
            "provided in class.)"
        ),
        "exam_keys": [
            "**Comprehension.** 1. best outcomes incl. risks / time horizon; 2. required actions regardless of consequence (consent / dignity); 3. what kind of researcher / institution; 4. almost always combine all three.",
            "**Analysis.** 1. *what produces the best outcomes?*; 2. informed consent / dignity / irreversible-harm thresholds; 3. *what kind of researcher / institution do we want to be?*; 4. pretending it is purely consequentialist is itself a philosophical position.",
            "**Composition.** Open. Reward integration of all three frames + at least one specific case detail.",
            "**Mediation.** Open. Reward register + cultural-note brackets where needed.",
        ],
    },
    {
        "n": 4, "slug": "shakespeare-extract",
        "title": "Shakespeare in Extract",
        "skills": ["reading", "writing", "language_awareness"],
        "bp": [
            "3.4.1 / 3.5.1 Soziokulturelles Orientierungswissen / Themen",
            "3.4.3.2 / 3.5.3.2 Leseverstehen",
            "3.4.3.5 / 3.5.3.5 Schreiben",
            "3.4.4 / 3.5.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can close-read a Shakespeare extract (sonnet or short scene) and identify form, voice, and one figurative move.",
            "I can engage Early Modern syntactic inversion and lexical density.",
            "I can write a 400-word literary essay with sustained close reading.",
        ],
        "leadin": (
            "The class read Sonnet 73 (*That time of year thou "
            "mayst in me behold*). Mr. Yilmaz asked: *what does "
            "the speaker want from the addressee?* The class "
            "argued for forty minutes. Maja said: *for the love "
            "to be more, not less, because the time is shorter*. "
            "The class agreed."
        ),
        "activate": (
            "**Inversion scan.** Slide shows a single line: "
            "*\"That time of year thou mayst in me behold\"*. "
            "With your partner, rewrite in modern English word "
            "order. Note what is lost."
        ),
        "input_blocks": [
            ("Reading — Sonnet 73, ll. 1-4",
             "*That time of year thou mayst in me behold,\n"
             "When yellow leaves, or none, or few, do hang\n"
             "Upon those boughs which shake against the cold,\n"
             "Bare ruined choirs, where late the sweet birds "
             "sang.*"),
            ("Vocabulary — Early Modern engagement",
             "*syntactic inversion, periphrasis, "
             "metonymy, synecdoche, conceit, "
             "volta (the turn), iambic pentameter, "
             "Shakespearean (English) sonnet form: 3 quatrains "
             "+ couplet (abab cdcd efef gg).*"),
            ("Close-reading move set",
             "1. **Form** — what does the form do that prose "
             "cannot?\n"
             "2. **Voice** — who is speaking, to whom?\n"
             "3. **One figurative move** — pick the most loaded "
             "metaphor / image / inversion.\n"
             "4. **Volta** — where does the poem turn?"),
        ],
        "practise_g": [
            "1. Modern word-order: *That time of year thou mayst "
            "in me behold* → ___ .",
            "2. Match: volta → the turn; conceit → extended "
            "metaphor; synecdoche → part standing for whole.",
        ],
        "practise_m": [
            "3. Identify in Sonnet 73, ll. 1-4: form, voice, one "
            "figurative move, the implied volta location.",
        ],
        "answer_g": (
            "1. *You may behold that time of year in me.*\n"
            "2. all true."
        ),
        "answer_m": (
            "3. Form: Shakespearean sonnet, opening quatrain, "
            "iambic pentameter. Voice: aging speaker addressing "
            "a younger beloved. Figurative move: the speaker as "
            "*late autumn tree* — *bare ruined choirs* "
            "(synecdoche / metonymy: choir-stalls of a ruined "
            "abbey for the boughs themselves). Volta: at line 13 "
            "(*This thou perceivest, which makes thy love more "
            "strong*)."
        ),
        "produce": (
            "**Literary essay, 400 words.** Sustained close "
            "reading of Sonnet 73. Use 4 integrated quotes + 6 "
            "academic discourse markers + 1 cleft + literary-"
            "analysis vocabulary throughout."
        ),
        "produce_sample": (
            "*Sonnet 73 is, on the surface, a poem about an "
            "ageing speaker watching late autumn from inside his "
            "own body. Beneath the surface, it is a sustained "
            "argument that the addressee should love the speaker "
            "*more*, not less, *because* the time is shorter. The "
            "argument is built across three quatrains, each "
            "offering a more compressed image of "
            "diminution. The first quatrain — *\"that time of year "
            "thou mayst in me behold\"* — opens with syntactic "
            "inversion that places the season-as-mirror image "
            "first. The yellowed leaves are not merely few; they "
            "are *\"yellow leaves, or none, or few\"*, a "
            "tightening rhythm that enacts the loss it names. "
            "Accordingly, the line *\"bare ruined choirs, where "
            "late the sweet birds sang\"* is the quatrain's most "
            "loaded image: the choir-stalls of a ruined abbey "
            "stand, by metonymy, for the boughs themselves, but "
            "the ruination also recalls the dissolution of the "
            "monasteries — historical violence sitting inside an "
            "image of personal mortality. By contrast, the second "
            "quatrain narrows to twilight (a single day's loss); "
            "the third narrows further to the dying fire (an "
            "hour's). It is precisely this acceleration that "
            "earns the volta in the final couplet: *\"This thou "
            "perceivest, which makes thy love more strong, / To "
            "love that well which thou must leave ere long.\"* In "
            "this regard, the poem's thesis is structural rather "
            "than ornamental: love is *intensified* by an "
            "honest reading of time. More specifically, the "
            "couplet refuses sentimentality. The speaker does not "
            "ask the addressee for grief; he asks for "
            "*recognition* of what the foreshortened time makes "
            "of the love itself. Sonnet 73 is, finally, the "
            "argumentative form (Shakespearean sonnet: 3 "
            "quatrains + couplet) doing what only this form can "
            "— building a case across three increasingly tight "
            "images and resolving it in two perfectly weighted "
            "lines.*"
        ),
        "reflect": [
            "I can close-read Sonnet 73 with form, voice, and figurative move.",
            "I can engage Early Modern English syntactic inversion.",
            "I can write a 400-word sustained close reading.",
        ],
        "pitfalls": [
            "Don't paraphrase Shakespeare — analyse what the "
            "form is doing.",
            "*Conceit* is an extended metaphor; don't use it "
            "loosely.",
            "Volta in a Shakespearean sonnet is at line 13, not "
            "9 (that's the Petrarchan sonnet).",
        ],
        "further": [
            "Stephen Booth, *Shakespeare's Sonnets* — accessible "
            "annotations.",
            "Don Paterson, *Reading Shakespeare's Sonnets*.",
        ],
        "exam_listening": (
            "Read twice.\n\n"
            "> \"That time of year thou mayst in me behold, / "
            "When yellow leaves, or none, or few, do hang / Upon "
            "those boughs which shake against the cold, / Bare "
            "ruined choirs, where late the sweet birds sang.\"\n\n"
            "1. Modern word order of l. 1: ___ . 2. The "
            "tightening rhythm of l. 2: ___ . 3. Image l. 4: "
            "___ . 4. What the synecdoche is doing: ___ ."
        ),
        "exam_reading": (
            "Read the four lines above.\n\n"
            "1. Form: ___ . 2. Speaker: ___ . 3. Figurative move: "
            "___ . 4. Implied volta location: ___ ."
        ),
        "exam_use": (
            "**Composition prompt:** *Close-read Sonnet 73 in "
            "300 words. Use 3 integrated quotes + 4 markers.*"
        ),
        "exam_writing": (
            "**Mediation prompt:** A 200-word German Shakespeare "
            "translation note (Schlegel-Tieck). Mediate the "
            "translator's argument for an English-speaking "
            "literary reader. (Source provided in class.)"
        ),
        "exam_keys": [
            "**Comprehension.** 1. *You may behold that time of year in me.*; 2. *yellow leaves, or none, or few* — three options shrinking; 3. *bare ruined choirs* (= boughs as choir-stalls); 4. linking personal mortality to historical ruination.",
            "**Analysis.** Shakespearean sonnet, opening quatrain, iambic pentameter; aging speaker to younger beloved; speaker-as-late-autumn-tree (metonymy with synecdoche); line 13 (couplet).",
            "**Composition.** Open.",
            "**Mediation.** Open.",
        ],
    },
    {
        "n": 5, "slug": "political-discourse",
        "title": "Political Discourse",
        "skills": ["reading", "listening", "language_awareness"],
        "bp": [
            "3.4.1 / 3.5.1 Soziokulturelles Orientierungswissen / Themen",
            "3.4.3.1 / 3.5.3.1 Hör-/Hörsehverstehen",
            "3.4.3.2 / 3.5.3.2 Leseverstehen",
            "3.4.4 / 3.5.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can read / listen to a political speech and identify rhetorical moves (anaphora, antithesis, tricolon, frame-setting).",
            "I can use the vocabulary of rhetorical analysis (*ethos / pathos / logos, kairos, frame, register shift*).",
            "I can write a 400-word rhetorical-analysis essay.",
        ],
        "leadin": (
            "The class read three short speech excerpts from "
            "different decades and political camps: Lincoln's "
            "Gettysburg Address (1863), Margaret Thatcher's *the "
            "lady's not for turning* (1980), and a 2024 climate "
            "speech by a 17-year-old delegate at COP30. Mr. "
            "Yilmaz framed the question: *what makes each of "
            "these technically effective, regardless of whether "
            "you agree with the content?*"
        ),
        "activate": (
            "**Rhetorical-move scan.** With your partner, list 5 "
            "rhetorical moves you have noticed in speeches. Mark "
            "each as *structural / lexical / acoustic*."
        ),
        "input_blocks": [
            ("Reading — three excerpts (paraphrased)",
             "*Lincoln (1863):* *Four score and seven years ago "
             "our fathers brought forth on this continent, a new "
             "nation, conceived in Liberty, and dedicated to the "
             "proposition that all men are created equal.*\n\n"
             "*Thatcher (1980):* *To those waiting with bated "
             "breath for that favourite media catchphrase, the "
             "U-turn, I have only one thing to say. You turn if "
             "you want to. The lady's not for turning.*\n\n"
             "*COP30 delegate (2024):* *I am seventeen. The "
             "policy you write today is the policy I am eighty-"
             "two years old in. I would like, accordingly, to "
             "be more than a footnote in this room.*"),
            ("Vocabulary — rhetorical analysis",
             "*ethos / pathos / logos, kairos (the right "
             "moment), anaphora (repeated opening), antithesis "
             "(balanced opposition), tricolon (three-part "
             "structure), parallelism, frame-setting, register "
             "shift, periodic sentence, asyndeton.*"),
        ],
        "practise_g": [
            "1. Match: ethos → speaker's authority; pathos → "
            "emotional appeal; logos → reasoned argument; kairos "
            "→ timing.",
            "2. Identify: *Four score and seven years ago* uses "
            "what acoustic move? (parallelism / archaic register "
            "/ both)",
        ],
        "practise_m": [
            "3. For each excerpt, identify one structural and "
            "one lexical rhetorical move.",
        ],
        "answer_g": (
            "1. all true.\n"
            "2. archaic register (and also acoustic emphasis "
            "through the high vowels)."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Rhetorical-analysis essay, 400 words.** Pick one "
            "of the three excerpts. Identify ethos / pathos / "
            "logos balance + 3 specific rhetorical moves + 1 "
            "kairos observation. Use 4 integrated quotes + 6 "
            "academic discourse markers + 1 cleft."
        ),
        "produce_sample": (
            "*Margaret Thatcher's 1980 *the lady's not for "
            "turning* line is, technically, one of the most "
            "efficient lines of post-war British political "
            "rhetoric. The mechanics deserve close reading. The "
            "antithesis — *\"You turn if you want to. The lady's "
            "not for turning\"* — sets up two grammatical "
            "subjects (*you / the lady*) and two contrastive "
            "verb phrases. Accordingly, the second clause "
            "borrows the energy of the first while inverting it; "
            "the audience laughs at the *you*, then registers "
            "the *not* before the speaker has to argue for it. "
            "Beneath the antithesis sits a deliberate register "
            "shift: *the lady* — third-person, stately, almost "
            "fairy-tale — replaces the expected first-person "
            "*I*. The shift performs a Thatcher-specific kind of "
            "ethos: she presents her position as institutional, "
            "as if the lady were not the speaker but the office. "
            "More specifically, the line is also a literary "
            "allusion to Christopher Fry's 1948 play *The Lady's "
            "Not for Burning*; the educated audience hears the "
            "reference, the wider audience hears the rhythm. "
            "Both registers do work simultaneously. By contrast "
            "with Lincoln's high-pathos *\"conceived in Liberty\"*, "
            "Thatcher's pathos is dry — almost an anti-pathos — "
            "and the line lands precisely because of the "
            "restraint. Logos is implicit rather than argued: the "
            "audience supplies the reasoning. Kairos is "
            "exemplary: October 1980, three months into a "
            "recession, with media speculation about a U-turn at "
            "its peak. It is precisely the timing that makes "
            "the antithesis political rather than literary. In "
            "this regard, the line is a small masterclass in "
            "compression. Ten words do the work that a paragraph "
            "of conventional defence would have done less well. "
            "The lesson, for the rhetorical analyst, is that "
            "the most-quoted lines in political speech almost "
            "always combine three moves at once.*"
        ),
        "reflect": [
            "I can identify ethos / pathos / logos balance and 3 specific rhetorical moves.",
            "I can use 6+ rhetorical-analysis terms.",
            "I can write a 400-word rhetorical-analysis essay.",
        ],
        "pitfalls": [
            "Don't reduce rhetoric to *good / bad*.",
            "*Pathos* is not synonymous with manipulation.",
            "Quote integration is part of the analysis, not a "
            "decoration.",
        ],
        "further": [
            "Sam Leith, *You Talkin' to Me? Rhetoric from "
            "Aristotle to Obama*.",
            "Brian MacArthur, *The Penguin Book of Twentieth-"
            "Century Speeches*.",
        ],
        "exam_listening": (
            "Listen / read twice.\n\n"
            "> \"To those waiting with bated breath for that "
            "favourite media catchphrase, the U-turn, I have "
            "only one thing to say. You turn if you want to. The "
            "lady's not for turning.\"\n\n"
            "1. Speaker / year: ___ . 2. Antithesis: ___ . 3. "
            "Register shift: ___ . 4. Allusion: ___ ."
        ),
        "exam_reading": (
            "Read the three excerpts above.\n\n"
            "1. Lincoln archaic register: ___ . 2. Thatcher's "
            "ethos move: ___ . 3. COP30 delegate's "
            "frame-setting: ___ . 4. The kairos in each: ___ ."
        ),
        "exam_use": (
            "**Composition prompt:** *Compare the rhetorical "
            "moves in Lincoln and the COP30 delegate in 250 "
            "words. Use 2 integrated quotes + 3 markers + 1 "
            "rhetorical-vocabulary term.*"
        ),
        "exam_writing": (
            "**Mediation prompt:** A 250-word German Bundestag "
            "speech excerpt. Mediate the speaker's rhetorical "
            "stance for an English-speaking political-rhetoric "
            "researcher. (Source provided in class.)"
        ),
        "exam_keys": [
            "**Comprehension.** 1. Thatcher 1980; 2. *You turn ↔ The lady's not for turning*; 3. *the lady* (third-person, stately) for *I*; 4. Christopher Fry, *The Lady's Not for Burning* (1948).",
            "**Analysis.** 1. *Four score and seven years ago* (biblical / register-elevating); 2. *the lady* — ethos as institutional; 3. *the policy you write today is the policy I am eighty-two years old in* (pathos + logos + age-frame); 4. Lincoln 1863 in war / Thatcher 1980 recession / COP30 2024 climate-action urgency.",
            "**Composition.** Open.",
            "**Mediation.** Open.",
        ],
    },
    {
        "n": 6, "slug": "the-non-fiction-essay",
        "title": "The Non-Fiction Essay",
        "skills": ["reading", "writing", "language_awareness"],
        "bp": [
            "3.4.1 / 3.5.1 Soziokulturelles Orientierungswissen / Themen",
            "3.4.3.2 / 3.5.3.2 Leseverstehen",
            "3.4.3.5 / 3.5.3.5 Schreiben",
            "3.4.4 / 3.5.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can read a contemporary non-fiction essay and identify thesis, supporting moves, and stylistic register.",
            "I can use vocabulary of essayistic prose (*premise, claim, qualification, anecdote-as-argument, the moral turn*).",
            "I can write a 400-word non-fiction essay of my own with a clear thesis and one anecdote-as-argument.",
        ],
        "leadin": (
            "Mr. Yilmaz handed out a 1,200-word non-fiction essay "
            "by Zadie Smith — *Speaking in Tongues* (2009). The "
            "class spent the lesson learning to track the "
            "essay's central move: an anecdote that becomes an "
            "argument, an argument that opens onto a moral turn, "
            "a moral turn that returns to the anecdote. Maja "
            "wrote in the margin: *the essay walks like a small "
            "animal that knows the route*."
        ),
        "activate": (
            "**Essay-shape scan.** Open the essay. With your "
            "partner, mark: where the thesis lands (paragraph 2 "
            "or 3?), where the anecdote-as-argument is, where "
            "the moral turn is."
        ),
        "input_blocks": [
            ("Reading — *Speaking in Tongues*, opening (paraphrased)",
             "*The essayist begins with a small autobiographical "
             "scene: code-switching between two voices in her "
             "own family. The anecdote is small, specific, "
             "domestic. By the third paragraph, the anecdote has "
             "become an argument about voice and authenticity. "
             "By the fifth, the argument has opened onto a moral "
             "turn — that *single voice* is a political demand, "
             "not a personal achievement. The closing returns to "
             "the autobiographical scene with new resonance.*"),
            ("Vocabulary — essayistic prose",
             "*premise, claim, qualification, "
             "anecdote-as-argument, register shift, moral turn, "
             "essayist's *I*, address, periodic sentence, "
             "elliptical close.*"),
        ],
        "practise_g": [
            "1. Match: anecdote-as-argument → small story doing "
            "argumentative work; moral turn → the essay's ethical "
            "shift; elliptical close → unfinished but resonant "
            "ending.",
            "2. T or F: the essayist's *I* is the same as the "
            "fiction-writer's narrator; non-fiction essays "
            "always open with the thesis.",
        ],
        "practise_m": [
            "3. Build 3 sentences using essayistic-prose "
            "vocabulary on Smith's opening.",
        ],
        "answer_g": (
            "1. all true.\n"
            "2. F (different conventions: the essayist's *I* "
            "carries personal accountability), F (often the "
            "thesis lands later, after an anecdote)."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Non-fiction essay (your own), 400 words.** Use "
            "the *anecdote-as-argument* move: open with a small "
            "personal scene, develop into an argument by "
            "paragraph 3, hit a moral turn by paragraph 5, "
            "return to the scene at the close. Use 4 academic "
            "discourse markers + 2 hedges + 1 cleft."
        ),
        "produce_sample": (
            "*The first time I noticed I had two voices, I was "
            "fourteen and on the phone with my grandmother. The "
            "voice I used with her — slower, vowel-heavier, "
            "permitted to be sentimental — had nothing in "
            "common with the voice I used at school the next "
            "morning. The realisation was not interesting in "
            "itself; everyone has more than one voice. What was "
            "interesting was my unease. I felt, briefly, as if "
            "one of the two were the *real* one and the other a "
            "small daily betrayal. Accordingly, I tried for some "
            "weeks to merge them — to bring the school voice "
            "home and the home voice to school. Both attempts "
            "embarrassed everyone, including me. By contrast, "
            "the more I read essays by writers who code-switch "
            "professionally — Zadie Smith, James Baldwin, "
            "Jhumpa Lahiri — the more clearly I saw that the "
            "anxiety I had felt was a borrowed anxiety. It is "
            "precisely the demand for a *single* voice that is "
            "the political problem. The literary problem, by "
            "contrast, is the harder one: how do you keep two "
            "registers without flattening either? The essayists "
            "who do this best, in my reading, do not pretend "
            "the two voices are identical. They let the reader "
            "feel the join. Smith's *Speaking in Tongues* "
            "(2009) is, in this regard, a small instruction "
            "manual: the essay's own register shifts twice in "
            "the first three pages, and the shifts are part of "
            "the argument. Caution is warranted; complacency "
            "with one's own voice is not. The phone call with "
            "my grandmother, returning at the close of this "
            "essay, no longer feels like a betrayal. It feels "
            "like a craft problem I have begun to solve.*"
        ),
        "reflect": [
            "I can identify thesis, supporting moves, and stylistic register in a non-fiction essay.",
            "I can use 6+ essayistic-prose terms.",
            "I can write a 400-word non-fiction essay with anecdote-as-argument and moral turn.",
        ],
        "pitfalls": [
            "Anecdote-as-argument ≠ memoir; the anecdote must do "
            "argumentative work.",
            "Moral turn cannot be moralistic — it must remain "
            "earned.",
            "Quote essayists sparingly; their voice is contagious.",
        ],
        "further": [
            "Zadie Smith, *Feel Free* (essays).",
            "James Baldwin, *Notes of a Native Son*.",
            "Jhumpa Lahiri, *In Other Words* (memoir-essay).",
        ],
        "exam_listening": (
            "Read twice the *Speaking in Tongues* paraphrase "
            "above.\n\n"
            "1. Opening: ___ . 2. By paragraph 3: ___ . 3. By "
            "paragraph 5: ___ . 4. Closing: ___ ."
        ),
        "exam_reading": (
            "Read the paraphrase above.\n\n"
            "1. Three structural moves: ___ . 2. The essayist's "
            "central political claim: ___ . 3. The moral turn: "
            "___ . 4. The elliptical close: ___ ."
        ),
        "exam_use": (
            "**Composition prompt:** *Write a 250-word "
            "anecdote-as-argument paragraph on a small "
            "linguistic / cultural observation. Use 2 markers + "
            "1 cleft.*"
        ),
        "exam_writing": (
            "**Mediation prompt:** A 200-word German "
            "Feuilleton-essay opener (e.g. from Zeit-Magazin) "
            "for an English-speaking literary-essay reader. "
            "(Source provided in class.)"
        ),
        "exam_keys": [
            "**Comprehension.** 1. small autobiographical scene of code-switching; 2. anecdote becomes argument about voice and authenticity; 3. moral turn — *single voice* is a political demand, not a personal achievement; 4. return to opening scene with new resonance.",
            "**Analysis.** 1. anecdote → argument → moral turn; 2. *single voice* is a political demand, not a personal achievement; 3. demand for one voice is a political problem; 4. return to autobiographical scene with new weight.",
            "**Composition.** Open.",
            "**Mediation.** Open.",
        ],
    },
    {
        "n": 7, "slug": "mediation-academic-text",
        "title": "Mediation: An Academic Text",
        "skills": ["mediation", "writing", "language_awareness"],
        "bp": [
            "3.4.1 / 3.5.1 Soziokulturelles Orientierungswissen / Themen",
            "3.4.3.5 / 3.5.3.5 Schreiben",
            "3.4.3.6 / 3.5.3.6 Sprachmittlung",
            "3.4.3.7 / 3.5.3.7 Verfügen über sprachliche Mittel – Wortschatz",
        ],
        "objectives": [
            "I can mediate a 500-word German academic text into 15 English sentences for a named addressee.",
            "I can preserve hedge structure, modal nuance, citation conventions, and disciplinary register.",
            "I can use the full reporting-verb toolkit and add cultural / disciplinary notes where needed.",
        ],
        "leadin": (
            "The class received a 500-word German social-science "
            "abstract from a 2026 paper on intergenerational "
            "income mobility in OECD countries. The addressee: an "
            "English-speaking PhD-track economist who reads "
            "abstracts to triage what to read in full. The task: "
            "mediate the abstract honestly enough that the "
            "researcher can decide whether to read the full "
            "paper."
        ),
        "activate": (
            "**Audit scan.** Mark each line of the German "
            "abstract: *findings / methods / hedges / "
            "implications*."
        ),
        "input_blocks": [
            ("Source — *Academic abstract (excerpt, paraphrased)*",
             "*Diese Arbeit untersucht "
             "intergenerationale Einkommensmobilität in 18 "
             "OECD-Ländern für die Geburtskohorten 1970-1990. "
             "Methodisch verwenden wir verlinkte Steuerregister-"
             "daten und einen Two-Sample IV-Schätzer. Die "
             "Hauptergebnisse legen nahe, dass die Mobilität in "
             "den meisten kontinentaleuropäischen Ländern höher "
             "ist als in den Vereinigten Staaten, dass jedoch der "
             "Abstand zwischen den 1970er- und den 1990er-"
             "Kohorten in einigen Ländern (Deutschland, "
             "Frankreich) gewachsen ist. Limitationen umfassen "
             "die unbeobachtete Heterogenität in der "
             "Migrationskohorte. Politische Implikationen "
             "diskutieren wir vorsichtig.*"),
            ("Mediation — academic-register conventions",
             "**Hedges to preserve:** *legen nahe* → *suggest*; "
             "*vorsichtig diskutieren* → *discuss with caution*; "
             "*Limitationen umfassen* → *limitations include*.\n\n"
             "**Modal nuance:** *kann sein* → *may be* (not "
             "*can*); *dürften* → *are likely to*.\n\n"
             "**Citation conventions:** preserve the *(Author, "
             "Year)* format if present.\n\n"
             "**Disciplinary register:** *Two-Sample IV* is a "
             "specific econometric estimator — keep the term, "
             "add a cultural / disciplinary note if needed."),
        ],
        "practise_g": [
            "1. Match German hedge → English: *legen nahe* → ?, "
            "*dürften* → ?, *vorsichtig* → ?",
            "2. Decide for the addressee profile: keep, "
            "paraphrase, or drop — *Two-Sample IV-Schätzer* (for "
            "a PhD-track economist).",
        ],
        "practise_m": [
            "3. Build a 5-sentence English mediation of the "
            "abstract above for a science-journalism reader (NOT "
            "an economist).",
        ],
        "answer_g": (
            "1. suggest / are likely to / with caution.\n"
            "2. keep (and add a 6-word note for a non-economist "
            "reader)."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Academic mediation, 15 sentences.** Read the "
            "source above. Write 15 English sentences for an "
            "English-speaking PhD-track economist. Preserve "
            "hedges + modal nuance + disciplinary register + "
            "use 8 reporting verbs + 1 cultural-disciplinary "
            "note bracket."
        ),
        "produce_sample": (
            "*Hi Jordan, here's a clean mediation of the "
            "abstract — should help your triage. The paper "
            "examines intergenerational income mobility across "
            "18 OECD countries for the 1970-1990 birth cohorts. "
            "Methodologically, the authors use linked tax-"
            "register data with a Two-Sample IV estimator (an "
            "instrumental-variables approach combining two "
            "datasets to handle measurement issues). The main "
            "findings suggest that mobility in most of "
            "continental Europe is higher than in the United "
            "States. By contrast, the authors note that the gap "
            "between the 1970s and 1990s cohorts has, in some "
            "countries (Germany, France), widened. They stress "
            "that limitations include unobserved heterogeneity "
            "in the migration cohort — a non-trivial concern "
            "given migration patterns over the period. The paper "
            "discusses policy implications with caution; it does "
            "not claim that the mobility gap is causally "
            "attributable to specific tax-and-transfer regimes. "
            "What it does is establish a stylised fact base "
            "robust enough to reward a fuller read. The authors "
            "concede that their identification strategy depends "
            "on assumptions standard in the literature but worth "
            "checking against the appendix. They argue, "
            "nonetheless, that the headline finding — widening "
            "gap in the 1990s cohorts in some continental "
            "countries — is robust to most specifications. They "
            "warn against extrapolating to outside-OECD "
            "contexts. They note, finally, that the next paper "
            "in the project will tackle the unobserved-"
            "heterogeneity problem head-on. In short: a paper "
            "worth reading in full, particularly the methods "
            "section.*"
        ),
        "reflect": [
            "I can mediate a 500-word academic abstract into 15 English sentences.",
            "I can preserve hedge structure, modal nuance, and disciplinary register.",
            "I can use 8 reporting verbs accurately.",
        ],
        "pitfalls": [
            "Don't translate disciplinary terms (*Two-Sample IV*) "
            "— keep them; add a brief note for non-experts.",
            "Don't strip the hedges in pursuit of clarity — they "
            "*are* the meaning.",
            "Reporting-verb monotony flattens academic texts.",
        ],
        "further": [
            "Goethe-Institut — Sprachmittlungs-Beispielaufgaben "
            "Oberstufe.",
            "Cambridge — *Translation and Mediation* course "
            "materials.",
        ],
        "exam_listening": (
            "Read twice.\n\n"
            "> \"Diese Arbeit untersucht intergenerationale "
            "Einkommensmobilität in 18 OECD-Ländern. "
            "Methodisch nutzen wir verlinkte "
            "Steuerregisterdaten. Die Hauptergebnisse legen "
            "nahe, dass die Mobilität in Kontinentaleuropa "
            "höher ist als in den USA. Der Abstand zwischen "
            "Kohorten ist in Deutschland und Frankreich "
            "gewachsen.\"\n\n"
            "1. Sample: ___ . 2. Method: ___ . 3. Main finding: "
            "___ . 4. Cross-cohort change: ___ ."
        ),
        "exam_reading": (
            "Read the German abstract above.\n\n"
            "1. Birth cohorts: ___ . 2. Estimator: ___ . 3. "
            "Limitation: ___ . 4. Policy stance: ___ ."
        ),
        "exam_use": (
            "**Match German hedge → English.**\n\n"
            "1. legen nahe → ___ ; 2. dürften → ___ ; 3. "
            "vorsichtig diskutieren → ___ ; 4. Limitationen "
            "umfassen → ___ ."
        ),
        "exam_writing": (
            "**Mediation prompt:** Write 15 English sentences "
            "for the named addressee profile. Preserve hedges + "
            "use 8 reporting verbs + 1 cultural-disciplinary "
            "note bracket."
        ),
        "exam_keys": [
            "**Comprehension.** 1. 18 OECD countries; 2. linked tax-register data; 3. mobility in continental Europe higher than US; 4. gap widened in Germany and France between 1970s and 1990s cohorts.",
            "**Analysis.** 1. 1970-1990 birth cohorts; 2. Two-Sample IV estimator; 3. unobserved heterogeneity in migration cohort; 4. *vorsichtig diskutieren* — discusses policy implications with caution.",
            "**Composition.** suggest / are likely to / discuss with caution / limitations include.",
            "**Mediation.** Open.",
        ],
    },
    {
        "n": 8, "slug": "post-colonial-voices-advanced",
        "title": "Post-Colonial Voices, Advanced",
        "skills": ["reading", "writing", "intercultural"],
        "bp": [
            "3.4.1 / 3.5.1 Soziokulturelles Orientierungswissen / Themen",
            "3.4.2 / 3.5.2 Interkulturelle kommunikative Kompetenz",
            "3.4.3.2 / 3.5.3.2 Leseverstehen",
            "3.4.3.5 / 3.5.3.5 Schreiben",
            "3.4.4 / 3.5.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can read longer post-colonial extracts and identify the writer's stance on the imperial archive in detail.",
            "I can use academic-postcolonial vocabulary (*hybridity, mimicry, the subaltern, double consciousness, world-Anglophone*).",
            "I can write a 400-word essay sustaining a complex post-colonial argument.",
        ],
        "leadin": (
            "Klasse 12 returns to post-colonial writing with a "
            "longer reach: an extract from Salman Rushdie's *East "
            "/ West* (1994), one from Tsitsi Dangarembga's "
            "*Nervous Conditions* (1988), and one from Arundhati "
            "Roy's non-fiction *The Algebra of Infinite Justice* "
            "(2002). The class spent the lesson learning to read "
            "*hybridity* not as celebration but as a working "
            "condition."
        ),
        "activate": (
            "**Stance scan.** With your partner, list 3 post-"
            "colonial writers you can name and one tactic each "
            "uses to engage the imperial archive."
        ),
        "input_blocks": [
            ("Reading — three extracts (paraphrased)",
             "*Rushdie (1994):* The narrator's two surnames sit "
             "side by side on a London library card. The "
             "library card itself is a postcolonial artefact: "
             "two languages, two empires, one borrower.\n\n"
             "*Dangarembga (1988):* The narrator describes her "
             "education in colonial Rhodesia (now Zimbabwe) "
             "with deliberately split self: the educated *I* "
             "and the home-language *I* observe each other "
             "without quite agreeing.\n\n"
             "*Roy (2002):* In an essay on the Indian state "
             "after the 1998 nuclear tests, Roy refuses the "
             "celebratory *we*; her *we* is conditional, audible "
             "and ironised."),
            ("Vocabulary — academic post-colonial",
             "*hybridity (Bhabha), mimicry (Bhabha), "
             "the subaltern (Spivak), double consciousness (Du "
             "Bois), world-Anglophone, decolonisation, the "
             "imperial archive, code-switching, situated knowledge, "
             "epistemic violence, contrapuntal reading (Said).*"),
        ],
        "practise_g": [
            "1. Match: hybridity → Bhabha; subaltern → Spivak; "
            "double consciousness → Du Bois; contrapuntal reading "
            "→ Said.",
            "2. T or F: *mimicry* in Bhabha is a strategy of "
            "compliance; the *subaltern* in Spivak refers to "
            "those without representational access.",
        ],
        "practise_m": [
            "3. Build 4 sentences applying academic post-colonial "
            "vocabulary to the three extracts.",
        ],
        "answer_g": (
            "1. all true.\n"
            "2. F (mimicry is partly destabilising — copy + "
            "difference), T."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Post-colonial essay, 400 words.** Argue a "
            "complex thesis sustained across the three extracts. "
            "Use 3 integrated quotes + 4 academic-postcolonial "
            "terms + 5 academic discourse markers + 1 cleft."
        ),
        "produce_sample": (
            "*Read together, the three extracts — Rushdie 1994, "
            "Dangarembga 1988, Roy 2002 — sketch a small "
            "anthology of how the post-colonial *I* learns to "
            "speak inside English without becoming English. "
            "Rushdie's narrator carries two surnames *side by "
            "side on a London library card*; the card is a "
            "small artefact of hybridity. The hybridity is, "
            "however, not celebratory. By contrast with "
            "earlier readings of Bhabha that flattened the "
            "concept into multicultural cheer, Rushdie's "
            "narrator reads the card as a *working condition*: "
            "two empires, one borrower, no resolution. "
            "Dangarembga's narrator goes further. The "
            "deliberately split self of *Nervous Conditions* — "
            "the educated *I* and the home-language *I* — is "
            "double consciousness in Du Bois's sense, ported "
            "to colonial Rhodesia. Accordingly, the *I* that "
            "writes the novel is not a synthesis of the two; "
            "it is the friction. Roy, writing essayistically in "
            "2002, refuses the celebratory national *we* of "
            "post-1998 Indian nuclear discourse. Her *we* is "
            "audible because it is ironised; the irony is the "
            "instrument. It is precisely the refusal of the "
            "synthetic *we* that aligns Roy with Spivak's "
            "argument that the subaltern's silence is a "
            "structural fact, not a literary gap. More "
            "specifically, what these three writers share is "
            "the willingness to keep the seams visible — "
            "Rushdie's two surnames, Dangarembga's two voices, "
            "Roy's ironised *we*. By contrast with a politics "
            "that demands resolution, post-colonial writing "
            "earns its weight by refusing it. The *imperial "
            "archive* is not erased; it is read contrapuntally "
            "(Said), with the silenced voices held alongside "
            "the dominant ones. In this regard, the central "
            "post-colonial move is not synthesis but a "
            "principled refusal of synthesis.*"
        ),
        "reflect": [
            "I can identify each writer's stance on the imperial archive.",
            "I can use 5+ academic-postcolonial terms.",
            "I can write a 400-word post-colonial essay.",
        ],
        "pitfalls": [
            "Don't reduce *hybridity* to celebration.",
            "*Subaltern* is not synonymous with *minority*.",
            "Don't quote theory without applying it.",
        ],
        "further": [
            "Edward Said, *Orientalism* (1978).",
            "Homi Bhabha, *The Location of Culture* (1994).",
            "Gayatri Chakravorty Spivak, *Can the Subaltern "
            "Speak?* (1988).",
        ],
        "exam_listening": (
            "Read twice.\n\n"
            "> \"The narrator's two surnames sit side by side on "
            "a London library card. The library card itself is "
            "a postcolonial artefact: two languages, two "
            "empires, one borrower.\"\n\n"
            "1. Two surnames where: ___ . 2. Card as: ___ . 3. "
            "Hybridity NOT meaning: ___ . 4. Card as working "
            "condition: ___ ."
        ),
        "exam_reading": (
            "Read the three extracts above.\n\n"
            "1. Rushdie's artefact: ___ . 2. Dangarembga's "
            "split: ___ . 3. Roy's pronominal move: ___ . 4. "
            "Shared central move: ___ ."
        ),
        "exam_use": (
            "**Composition prompt:** *Apply Spivak's *subaltern* "
            "concept to one extract in 250 words. Use 2 markers "
            "+ 1 cleft.*"
        ),
        "exam_writing": (
            "**Mediation prompt:** A 250-word German "
            "post-colonial-studies introduction "
            "(Einführungsband). Mediate for an English-speaking "
            "literature student. (Source provided in class.)"
        ),
        "exam_keys": [
            "**Comprehension.** 1. on a London library card; 2. postcolonial artefact (two languages, two empires, one borrower); 3. multicultural cheer / synthesis; 4. two empires, one borrower, no resolution.",
            "**Analysis.** 1. two surnames on London library card; 2. educated *I* + home-language *I* (double consciousness); 3. ironised *we* refusing celebratory national *we*; 4. principled refusal of synthesis / keeping the seams visible.",
            "**Composition.** Open.",
            "**Mediation.** Open.",
        ],
    },
    {
        "n": 9, "slug": "a-novel-in-full",
        "title": "A Novel in Full",
        "skills": ["reading", "writing", "language_awareness"],
        "bp": [
            "3.4.1 / 3.5.1 Soziokulturelles Orientierungswissen / Themen",
            "3.4.3.2 / 3.5.3.2 Leseverstehen",
            "3.4.3.5 / 3.5.3.5 Schreiben",
            "3.4.4 / 3.5.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can read a complete novel (Atwood's *The Handmaid's Tale* or Ishiguro's *Klara and the Sun*) and write a sustained 500-word essay tracing one motif across the whole work.",
            "I can move between close reading and structural argument fluidly.",
            "I can use the full literary-analysis toolkit at Leistungsfach (advanced course) standard.",
        ],
        "leadin": (
            "The class has been reading *The Handmaid's Tale* "
            "(Atwood, 1985) since Week 12. Today is the whole-"
            "novel essay checkpoint. Students have been keeping a "
            "two-page motif log per chapter; the logs converge, "
            "predictably, on three motifs: language as instrument "
            "of control, the body as site of resistance, the "
            "double meaning of women's collusion."
        ),
        "activate": (
            "**Whole-novel motif scan.** With your partner, "
            "agree on the three strongest motifs in the novel. "
            "Mark each with one chapter where it is most "
            "concentrated."
        ),
        "input_blocks": [
            ("Whole-novel essay — structural moves",
             "1. **Frame the motif** in two sentences.\n"
             "2. **Trace the motif** through three or four "
             "moments — opening, middle, late.\n"
             "3. **Name the structural argument** — what is the "
             "novel saying *through* the motif?\n"
             "4. **Concession + counter-reading** — name an "
             "alternative reading and engage with it.\n"
             "5. **Close** with a sentence that integrates the "
             "thesis."),
            ("Vocabulary — whole-novel analysis",
             "*motif, leitmotif, structural argument, "
             "narrative arc, chapter rhythm, framing device, "
             "epigraph, frame narrative, unreliable narrator, "
             "polyphony, focalisation.*"),
        ],
        "practise_g": [
            "1. Match: leitmotif → recurring motif; framing "
            "device → opening / closing structure; focalisation "
            "→ point-of-view.",
            "2. T or F: a structural argument is the same as a "
            "thematic claim; a motif must appear at least three "
            "times to be a motif.",
        ],
        "practise_m": [
            "3. Build a 4-sentence motif-trace for one motif "
            "across *The Handmaid's Tale*.",
        ],
        "answer_g": (
            "1. all true.\n"
            "2. F (structural argument is *what the novel is "
            "doing* with the theme — process, not theme alone), "
            "F (no fixed minimum, but rough rule-of-thumb)."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Whole-novel essay, 500 words.** Trace one motif "
            "across the whole novel. Use 5 integrated quotes "
            "(across at least three chapters) + 7 academic "
            "discourse markers + 1 cleft + 1 concession + "
            "counter-reading."
        ),
        "produce_sample": (
            "*The motif of *language as instrument of control* "
            "carries Margaret Atwood's *The Handmaid's Tale* "
            "from its opening pages to its Historical Notes. "
            "Reading the novel as a whole, the motif moves "
            "through three phases — colonisation, refusal, and "
            "academic recovery — and the structural argument "
            "rests on the third. Early in the novel, scripture-"
            "coded greetings — *\"Blessed be the fruit\"*; *\"May "
            "the Lord open\"* — replace ordinary speech, and "
            "Offred (the narrator) reports them with a flatness "
            "that is itself a small refusal. By contrast with a "
            "regime that simply forbids speech, Gilead "
            "*re-codes* speech, which is the more durable form "
            "of control. By the middle of the novel, Offred has "
            "begun to compose her account silently — a private "
            "language inside the public one. It is precisely "
            "the existence of this private register, more than "
            "any single act, that the regime cannot reach. "
            "Accordingly, what the novel is doing through the "
            "motif is not just illustrating linguistic "
            "totalitarianism but staging the irreducibility of "
            "private narrative inside public scripture. More "
            "specifically, the *Historical Notes* at the close "
            "— a fictional 2195 academic conference re-reading "
            "Offred's recovered tapes — re-frames the entire "
            "preceding text. The academic voices are themselves "
            "implicated; they laugh, they joke, they "
            "miss-read. In this regard, Atwood's structural "
            "argument is sharper than the surface plot suggests: "
            "the recovery of a silenced voice is itself "
            "vulnerable to a *new* form of instrumentalisation, "
            "this time by the academy. A counter-reading would "
            "argue that the *Historical Notes* simply provide "
            "documentary frame. I find this reading flat: the "
            "satirical edge of the conference tone, especially "
            "the male keynote's small jokes, makes the frame "
            "interpretive rather than documentary. In this "
            "regard, Atwood is not naive about her own readers. "
            "By contrast with a more triumphalist closing, *The "
            "Handmaid's Tale* leaves us inside three layers of "
            "language-control: Gilead's, Offred's silent "
            "counter-narrative, and the academy's well-meaning "
            "future appropriation. The motif of language as "
            "control is not, finally, *about* Gilead. It is "
            "about the difficulty of reading any voice from "
            "across a structural distance.*"
        ),
        "reflect": [
            "I can trace one motif across a whole novel.",
            "I can move between close reading and structural argument.",
            "I can write a 500-word whole-novel essay at Leistungsfach standard.",
        ],
        "pitfalls": [
            "Don't summarise the plot.",
            "Whole-novel essays need 4-5 specific moments, not "
            "two opening pages.",
            "Concession-and-counter-reading must be substantive, "
            "not symbolic.",
        ],
        "further": [
            "Margaret Atwood, *The Handmaid's Tale* (1985); also "
            "*The Testaments* (2019).",
            "Coral Ann Howells, *Margaret Atwood* (Cambridge "
            "Companion).",
        ],
        "exam_listening": (
            "Read twice.\n\n"
            "> \"The motif of *language as control* moves "
            "through three phases: scripture-coded greetings "
            "(*Blessed be the fruit*) early; Offred's silent "
            "private register in the middle; the *Historical "
            "Notes* academic-recovery frame at the close.\"\n\n"
            "1. Phase 1: ___ . 2. Phase 2: ___ . 3. Phase 3: "
            "___ . 4. Atwood's structural argument: ___ ."
        ),
        "exam_reading": (
            "Read your set text. Identify three chapters where "
            "the *language-as-control* motif is most "
            "concentrated.\n\n"
            "1. Early chapter: ___ . 2. Middle chapter: ___ . 3. "
            "Late chapter / Historical Notes: ___ . 4. The "
            "structural arc: ___ ."
        ),
        "exam_use": (
            "**Composition prompt:** *Trace one motif (other "
            "than language) across the novel in 350 words. Use "
            "3 integrated quotes + 4 markers + 1 cleft.*"
        ),
        "exam_writing": (
            "**Mediation prompt:** A 250-word German "
            "literary-criticism review of the novel. Mediate "
            "for an English-speaking literary-magazine reader. "
            "(Source provided in class.)"
        ),
        "exam_keys": [
            "**Comprehension.** 1. scripture-coded greetings; 2. silent private register / private narrative; 3. *Historical Notes* — 2195 academic conference; 4. *the recovery of a silenced voice is itself vulnerable to a new form of instrumentalisation*.",
            "**Analysis.** 1. early chapters with *Blessed be the fruit* greetings; 2. middle chapters with Offred's silent composition; 3. *Historical Notes* — academic appropriation; 4. colonisation → refusal → academic recovery (with the third being the structural argument).",
            "**Composition.** Open.",
            "**Mediation.** Open.",
        ],
    },
    {
        "n": 10, "slug": "kommunikationspruefung-mock",
        "title": "Kommunikationsprüfung Mock",
        "skills": ["speaking", "listening", "language_awareness"],
        "bp": [
            "3.4.1 / 3.5.1 Soziokulturelles Orientierungswissen / Themen",
            "3.4.3.1 / 3.5.3.1 Hör-/Hörsehverstehen",
            "3.4.3.3 / 3.5.3.3 Sprechen – an Gesprächen teilnehmen",
            "3.4.3.4 / 3.5.3.4 Sprechen – zusammenhängendes monologisches Sprechen",
        ],
        "objectives": [
            "I can deliver a 5-minute Abitur-style monologue from a stimulus and respond to a 5-minute examiner dialogue.",
            "I can use the formal spoken-academic register and rebut / concede in real time.",
            "I can self-assess my performance against the BW Abitur Bewertungsraster (grading grid).",
        ],
        "leadin": (
            "Mr. Yilmaz set today's lesson as a full-format mock "
            "Kommunikationsprüfung (oral exam). Format: 5-min "
            "monologue + 5-min examiner dialogue + 2-min closing. "
            "Bewertungsraster (grading grid) provided in advance: "
            "*kommunikative Textgestaltung* and *sprachliche "
            "Korrektheit und Variabilität*, weighted 50/50 in "
            "Basisfach (basic course), 40/60 in Leistungsfach "
            "(advanced course)."
        ),
        "activate": (
            "**Stimulus draw.** Each pair draws a stimulus "
            "card (image, statistic, quote). 90 seconds prep + 2 "
            "minutes outline."
        ),
        "input_blocks": [
            ("Kommunikationsprüfung (oral exam) format",
             "1. **Monologue (5 min).** Frame stimulus → 2-3 "
             "arguments → counter + concession → close.\n"
             "2. **Dialogue (5 min).** Examiner asks 5-7 "
             "follow-ups. Candidate must rebut, concede, "
             "elaborate, and connect to broader knowledge.\n"
             "3. **Close (2 min).** Synthesis + final stance.\n\n"
             "Total ~12 minutes."),
            ("Bewertungsraster — sample categories",
             "**Kommunikative Textgestaltung** (40-50 %): "
             "Aufbau, Kohärenz, Adressatenbezug, Strategien "
             "der Gesprächsführung.\n\n"
             "**Sprachliche Korrektheit und Variabilität** "
             "(50-60 %): Wortschatz, Grammatik, Idiomatik, "
             "Aussprache, Register-Sensibilität."),
        ],
        "practise_g": [
            "1. Match: kommunikative Textgestaltung → structure "
            "+ coherence; sprachliche Korrektheit → vocabulary "
            "+ grammar.",
            "2. T or F: in Leistungsfach (advanced course), "
            "Sprache is weighted higher than Inhalt.",
        ],
        "practise_m": [
            "3. Self-assess your last rehearsed monologue in "
            "two columns: *Aufbau / Sprache*.",
        ],
        "answer_g": (
            "1. all true.\n"
            "2. T (40 / 60 in LF)."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Pair Komm-Prüfung mock.** 12 minutes per pair. "
            "Audience scores using a simplified BW Bewertungsraster "
            "(grading grid). Class debrief at the end with each "
            "pair receiving one specific feedback sentence."
        ),
        "produce_sample": (
            "*Let me start with the stimulus image — a 2025 "
            "photograph of a flooded Bangladesh street with three "
            "rickshaws still operating. I would argue that the "
            "image is doing two things at once: documenting "
            "climate-induced displacement and resisting the "
            "framing of climate-vulnerable countries as purely "
            "passive. The available evidence suggests that the "
            "rickshaw economy in Bangladesh has, over the past "
            "fifteen years, adapted faster to seasonal flooding "
            "than urban planning has — through informal route "
            "shifts, raised platforms at intersections, and "
            "neighbourhood phone trees. The photograph captures "
            "this. Accordingly, what I am not saying is that "
            "the flooding is not a crisis; what I am saying is "
            "that the dominant Western framing of climate "
            "vulnerability tends to crop out the adaptation. "
            "Let me concede one point first: vulnerability is "
            "real, and the rickshaw economy itself has limits. "
            "When the floods exceed waist-height, the system "
            "breaks down. By contrast, between 2015 and 2025, "
            "the system handled approximately 80 % of seasonal "
            "events without major service disruption. On "
            "reflection, what the image is asking me to do is "
            "hold the crisis and the adaptation in the same "
            "frame. If I had to commit, I would say that "
            "international policy frames are, in this regard, "
            "ten years behind the photographs. The honest "
            "question for English-language climate journalism is "
            "not *how vulnerable are these countries?* but *what "
            "have they already taught us that we have not yet "
            "absorbed?*.*"
        ),
        "reflect": [
            "I can deliver a 5-minute monologue from a stimulus.",
            "I can hold a 5-minute examiner dialogue.",
            "I can self-assess against the Bewertungsraster (grading grid).",
        ],
        "pitfalls": [
            "Reading off prep notes during the monologue.",
            "Generic concessions; name the specific point.",
            "Missing the *connect to broader knowledge* "
            "expectation in the dialogue phase.",
        ],
        "further": [
            "Bildungsplan-aligned Komm-Prüfung mock-stimulus "
            "collections (Klett, Stark).",
            "BBC Sounds — *Question Time* extracts for "
            "examiner-style follow-up rhythm.",
        ],
        "exam_listening": (
            "Listen twice to a sample monologue (above).\n\n"
            "1. Stimulus type: ___ . 2. Two arguments: ___ . 3. "
            "Concession + statistic: ___ . 4. Closing question: "
            "___ ."
        ),
        "exam_reading": (
            "Read the sample monologue above.\n\n"
            "1. Two things the image is doing: ___ . 2. The "
            "*not saying / saying* contrast: ___ . 3. The "
            "specific concession: ___ . 4. Final commit: ___ ."
        ),
        "exam_use": (
            "**Composition prompt:** *Write a 4-minute Komm-"
            "Prüfung-style monologue script (~280 words) on a "
            "stimulus of your choice. Use 6 spoken-academic "
            "phrases + 1 specific statistic.*"
        ),
        "exam_writing": (
            "**Mediation prompt:** A 200-word German "
            "Klimawandel-Rede excerpt. Mediate the speaker's "
            "rhetorical stance for an English-speaking climate-"
            "policy reader. (Source provided in class.)"
        ),
        "exam_keys": [
            "**Comprehension.** 1. 2025 photograph (flooded Bangladesh street with rickshaws); 2. (a) documenting climate-induced displacement (b) resisting passive framing; 3. system handles 80 % of seasonal events without major disruption (2015-2025); 4. *what have these countries taught us that we have not yet absorbed?*",
            "**Analysis.** documenting + resisting passive framing; *not saying flooding isn't a crisis — saying Western framing crops out adaptation*; vulnerability + rickshaw-economy waist-height limit; international policy frames are ten years behind the photographs.",
            "**Composition.** Open.",
            "**Mediation.** Open.",
        ],
    },
    {
        "n": 11, "slug": "klausur-comprehension-analysis",
        "title": "Klausur: Comprehension and Analysis",
        "skills": ["reading", "writing", "language_awareness"],
        "bp": [
            "3.4.1 / 3.5.1 Soziokulturelles Orientierungswissen / Themen",
            "3.4.3.2 / 3.5.3.2 Leseverstehen",
            "3.4.3.5 / 3.5.3.5 Schreiben",
            "3.4.4 / 3.5.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can answer a Klausur Comprehension section (~24 BE) on a literary or journalistic source under timed conditions.",
            "I can write a Klausur Analysis section (~18 BE) with sustained close reading and integrated quotation.",
            "I can deploy time-management discipline across the two sections.",
        ],
        "leadin": (
            "This Unit is the first of two dedicated Klausur-prep "
            "Units in Klasse 12. Today's focus: Comprehension + "
            "Analysis, the two sections most reliant on close "
            "reading. Mr. Yilmaz set the source — a 1,000-word "
            "extract from a 2026 *New Yorker* essay on attention "
            "economies — and gave the class 90 minutes."
        ),
        "activate": (
            "**Reading-budget scan.** Before opening the source, "
            "decide: *first read* (orienting, 10 min) + *second "
            "read* (close, 15 min). What do you do differently "
            "in the second read?"
        ),
        "input_blocks": [
            ("Comprehension section — pattern",
             "Typical Comprehension question types:\n"
             "1. *State / outline* — gives you the question; "
             "you answer in your own words with one or two "
             "specifics.\n"
             "2. *Explain* — needs *because* / *the reason is "
             "that* + a specific from the text.\n"
             "3. *Compare / contrast* — needs both elements "
             "named + the relation.\n\n"
             "**Sprache check:** answer in your own words, "
             "preserving named specifics from the text. Don't "
             "quote whole sentences; embed fragments."),
            ("Analysis section — pattern",
             "Typical Analysis question types:\n"
             "1. *Analyse the writer's stance / argumentative "
             "strategy.* — needs 3+ specific moves + an "
             "integrated quote per move.\n"
             "2. *Analyse the language / register / structural "
             "features.* — needs technical vocabulary + close "
             "reading.\n\n"
             "**Sprache check:** integrated quotation, academic "
             "register, no plot summary."),
        ],
        "practise_g": [
            "1. Match: *outline* → state in own words; *explain* "
            "→ give reason; *analyse* → identify and discuss "
            "moves.",
            "2. T or F: *outline* allows quoting full sentences; "
            "*analyse* requires integrated quotation; "
            "*compare* needs both elements named.",
        ],
        "practise_m": [
            "3. Build a 4-sentence Analysis answer on the "
            "writer's stance using 2 integrated quotes + 2 "
            "academic discourse markers.",
        ],
        "answer_g": (
            "1. all true.\n"
            "2. F (outline = own words, no full quotes), T, T."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Klausur sections, timed.** 90 minutes total. 30 "
            "min Comprehension (24 BE) + 50 min Analysis (18 "
            "BE) + 10 min review. Submit. Class debriefs "
            "collectively with focus on time and integrated "
            "quotation."
        ),
        "produce_sample": (
            "(See *Reflection on the rehearsal* — the "
            "production task is the timed sections themselves.)"
        ),
        "reflect": [
            "I can answer a Comprehension section under timed conditions.",
            "I can write an Analysis section with sustained close reading.",
            "I can deploy time-management discipline across the two sections.",
        ],
        "pitfalls": [
            "Spending too long on Comprehension because it feels "
            "safe.",
            "Using full block-quotes in Analysis — integrate.",
            "Plot-summary instead of analysis.",
        ],
        "further": [
            "Bildungsplan-aligned Klausur collections.",
            "Past Abitur papers (BW), with caution: format "
            "familiarity only.",
        ],
        "exam_listening": (
            "Read the source (provided in class) twice. "
            "**Comprehension prompt:** *In your own words, "
            "outline the writer's central claim about attention "
            "economies (5 BE). Explain how the writer "
            "distinguishes *attention* from *engagement* (10 "
            "BE). Compare the writer's framing with one "
            "alternative framing the writer references (9 "
            "BE).*"
        ),
        "exam_reading": (
            "**Analysis prompt:** *Analyse the writer's "
            "argumentative strategy in 18 BE. Identify three "
            "specific moves with integrated quotation. Use 4 "
            "academic discourse markers.*"
        ),
        "exam_use": (
            "**(No additional Composition section in this "
            "Unit.)** Time-budget exercise:\n\n"
            "Allocate the 90 minutes: ___ min reading; ___ min "
            "Comprehension; ___ min Analysis; ___ min review."
        ),
        "exam_writing": (
            "**(No Mediation in this Unit.)** Reflection prompt: "
            "*In 150 words, reflect on which of the two sections "
            "(Comprehension / Analysis) cost you more time and "
            "why. What would you change in next week's "
            "rehearsal?*"
        ),
        "exam_keys": [
            "**Comprehension.** Reward own-words paraphrase + named specifics + clear structure.",
            "**Analysis.** Reward 3+ integrated quotes + 4 markers + technical vocabulary + close reading (not plot summary).",
            "**Time budget.** Suggested: 25 min reading / 30 min Comprehension / 25 min Analysis / 10 min review.",
            "**Reflection.** Open.",
        ],
    },
    {
        "n": 12, "slug": "klausur-composition-and-comment",
        "title": "Klausur: Composition and Comment",
        "skills": ["writing", "language_awareness"],
        "bp": [
            "3.4.1 / 3.5.1 Soziokulturelles Orientierungswissen / Themen",
            "3.4.3.5 / 3.5.3.5 Schreiben",
            "3.4.3.6 / 3.5.3.6 Sprachmittlung",
            "3.4.4 / 3.5.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can complete a Klausur Composition section (~18 BE) — argument or creative response — under timed conditions.",
            "I can complete a Klausur Mediation section (~30 BE) for a named English-speaking addressee.",
            "I can manage time across the second half of the Klausur.",
        ],
        "leadin": (
            "Second of two Klausur-prep Units. Today's focus: "
            "Composition + Mediation — the two sections most "
            "reliant on producing original text under time "
            "pressure. The class is using the same source as "
            "Unit 11 to build a complete 90-BE Klausur "
            "experience across the two Units."
        ),
        "activate": (
            "**Composition-vs.-Mediation budget scan.** Of the "
            "remaining ~110 min, how do you split 18 BE "
            "(Composition) vs. 30 BE (Mediation)?"
        ),
        "input_blocks": [
            ("Composition section — pattern",
             "Typical Composition tasks:\n"
             "1. *Discuss / comment* — 250-300 words, your own "
             "argument grounded in the source.\n"
             "2. *Creative response* — letter, diary entry, "
             "speech: shifts genre but keeps the source's "
             "argumentative weight.\n\n"
             "**Sprache check:** clear thesis in first 2 "
             "sentences, evidence + counter, conclusion. "
             "Academic discourse markers + cleft + 1 "
             "integrated quote."),
            ("Mediation section — pattern",
             "Typical Mediation tasks:\n"
             "1. *For a named English-speaking addressee, "
             "mediate the German source* in ~250 words / 12-15 "
             "sentences.\n"
             "2. **Sprache check:** preserve hedges + modal "
             "nuance; drop ceremony; use 7+ reporting verbs; "
             "add cultural notes where needed.\n\n"
             "Mediation is Inhalt-weighted but Sprache-checked. "
             "Both axes count."),
        ],
        "practise_g": [
            "1. Match Composition task → likely word count: "
            "*discuss / comment* → 250-300 words; *creative "
            "response* → 250-300 words.",
            "2. T or F: Mediation rewards literal translation; "
            "Composition rewards original argument.",
        ],
        "practise_m": [
            "3. Outline a 250-word Composition response to a "
            "*comment on the writer's central claim* prompt.",
        ],
        "answer_g": (
            "1. all true.\n"
            "2. F (Mediation rewards addressee-fit + register, "
            "not literal translation), T."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Klausur sections, timed.** 110 minutes total. 50 "
            "min Composition (18 BE) + 50 min Mediation (30 BE) "
            "+ 10 min review. Submit. Class debriefs collectively "
            "with focus on production speed under time."
        ),
        "produce_sample": (
            "(See *Reflection on the rehearsal* — the "
            "production task is the timed sections themselves.)"
        ),
        "reflect": [
            "I can complete a Composition section under timed conditions.",
            "I can complete a Mediation section for a named addressee.",
            "I can manage time across the second half of the Klausur.",
        ],
        "pitfalls": [
            "Spending 70 min on Composition because it feels more "
            "creative — Mediation is 30 BE, not 18.",
            "Carrying source language directly into Composition "
            "(plagiarism risk).",
            "Dropping reporting-verb variety in Mediation under "
            "time pressure.",
        ],
        "further": [
            "Bildungsplan-aligned Klausur collections.",
            "Goethe-Institut Sprachmittlungs-Beispielaufgaben "
            "Oberstufe.",
        ],
        "exam_listening": (
            "**Composition prompt:** *Discuss the writer's "
            "central claim about attention economies in 280 "
            "words. Use 1 integrated quote + 4 academic "
            "discourse markers + 1 cleft + 2 hedges.*"
        ),
        "exam_reading": (
            "**Mediation prompt:** *For an English-speaking "
            "media-policy researcher, mediate a 250-word German "
            "Bundestags-Anhörung extract on attention regulation "
            "(Aufmerksamkeitsregulierung). Use 8 reporting "
            "verbs + 2 cultural-note brackets.* (Source provided "
            "in class.)"
        ),
        "exam_use": (
            "**Time-budget exercise.** Allocate 110 minutes: "
            "___ min Composition; ___ min Mediation; ___ min "
            "review. Justify in 2 sentences."
        ),
        "exam_writing": (
            "**Reflection prompt:** *In 200 words, reflect on "
            "your full 90-BE Klausur experience across Units 11 "
            "and 12. Which section did you handle best? Which "
            "needs the most rehearsal before Klasse 13?*"
        ),
        "exam_keys": [
            "**Comprehension.** Reward thesis + integrated quote + 4 markers + 1 cleft + 2 hedges + clear structure.",
            "**Analysis.** Reward addressee-fit + register + 8 reporting verbs + 2 cultural notes + preserved hedges + appropriate modal mapping.",
            "**Time budget.** Suggested: 50 min Composition / 50 min Mediation / 10 min review.",
            "**Reflection.** Open.",
        ],
    },
]


UNIT_TPL = """---
title: "Unit {n} — {title}"
subtitle: "Track E · Klasse 12 · Niveau E (Basisfach / Leistungsfach)"
niveau: "E"
klassenstufe: 12
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
**Niveau:** E. Klausur (assessment) at Niveau E (90 BE).\\
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
**Slide deck timing.** 90 minutes total (Doppelstunde). Lead-in
6 min · Activate 8 min · Input 25 min · Practise 15 min · Produce
30 min · Reflect 6 min.

**Differentiation.** Basisfach (basic course): tighter argument,
clearer moves. Leistungsfach (advanced course): sustained
analysis, integrated quotation, complex thesis.
:::

## Common pitfalls

{pitfalls}

## Further reading / listening

{further}
"""

EXAM_BODY_TPL = """::: {{.callout-warning icon=false title="Klausur (assessment) — Niveau E (full paper, 90 BE)"}}
**Time.** 4 hours including 20 minutes of breaks (220 active
minutes). **Total.** 90 BE.\\
**Inhalt / Sprache split.** Basisfach (basic course): 50/50.
Leistungsfach (advanced course): 40/60.
:::

### Part A — Comprehension (~24 BE)

{exam_listening}

### Part B — Analysis (~18 BE)

{exam_reading}

### Part C — Composition (~18 BE)

{exam_use}

### Mediation (~30 BE)

{exam_writing}

::: {{.callout-tip collapse="true" title="Expected-answer profile (Erwartungshorizont) — sample"}}
{exam_keys}
:::

::: {{.callout-tip collapse="true" title="grading scale (Notenschlüssel) (von 90 BE)"}}
| 86–90 | 1+ | 81–85 | 1   | 76–80 | 1- |
| 71–75 | 2+ | 66–70 | 2   | 61–65 | 2- |
| 56–60 | 3+ | 51–55 | 3   | 46–50 | 3- |
| 41–45 | 4+ | 36–40 | 4   | 30–35 | 4- |
| 22–29 | 5  |  0–21 | 6   |       |    |
:::
"""

EXAM_WRAP_TPL = """---
title: "Klausur (assessment) — Unit {n}: {title}"
subtitle: "Track E · Klasse 12 · Niveau E · 4 Stunden"
author: "S. Le Boulanger"
niveau: "E"
klassenstufe: 12
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

**Track E · Klasse 12 · Niveau E · 4 Stunden (incl. breaks) · 90 BE**

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

    print(f"Wrote {len(UNITS) * 3} files for Track E Klasse 12.")


if __name__ == "__main__":
    emit()
