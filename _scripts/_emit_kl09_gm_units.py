"""Batch-emit Track G+M Klasse 9 — all 12 Units.

Klasse 9 voice: social issues, choices, self-aware humour. Cast:
Eli, Naima, Mr. Yilmaz (mentor figure). Bildungsplan prefix 3.2
(Klassen 7/8/9). Grammar arc continues from Klasse 8: passive in
multiple tenses, third conditional intro, more relative clauses,
gerund vs. infinitive after verbs, formal letter conventions,
phrasal verbs.
"""
from __future__ import annotations
import pathlib

REPO = pathlib.Path(__file__).resolve().parent.parent
COURSE = REPO / "track_gm_kl09" / "units"

UNITS = [
    {
        "n": 1, "slug": "future-careers", "title": "Future Careers",
        "skills": ["reading", "speaking", "language_awareness"],
        "bp": [
            "3.2.1 Soziokulturelles Orientierungswissen / Themen",
            "3.2.3.2 Leseverstehen",
            "3.2.3.3 Sprechen – an Gesprächen teilnehmen",
            "3.2.3.7 Verfügen über sprachliche Mittel – Wortschatz",
            "3.2.3.8 Verfügen über sprachliche Mittel – Grammatik",
        ],
        "objectives": [
            "I can name 12 jobs and describe what they involve.",
            "I can use *want / hope / plan* + to-infinitive.",
            "I can hold a 2-minute conversation about future career interests.",
        ],
        "leadin": (
            "Eli pinned a job ad on the wall above his desk: "
            "*marine biologist, southern Spain, fluent English "
            "required, must enjoy boats*. He has neither a degree, "
            "nor a passport, nor — by his own admission — sea legs. "
            "Mr. Yilmaz says, \"Eli, the ad isn't hiring you. The "
            "ad is keeping you company.\" Eli nods, leaves it on "
            "the wall."
        ),
        "activate": (
            "**Three-job scan.** Write three jobs that exist, three "
            "that didn't exist twenty years ago, and three that "
            "might exist in twenty years. Compare with your partner."
        ),
        "input_blocks": [
            ("Vocabulary — work and careers",
             "*career, profession, vocational training, "
             "apprenticeship, internship, employer, employee, CV, "
             "cover letter, salary, full-time, part-time, "
             "freelance, self-employed, qualification, skills, "
             "soft skills, hard skills.*"),
            ("Grammar — verb + to-infinitive",
             "After *want, hope, plan, decide, aim, learn, "
             "intend, refuse, choose*, use **to-infinitive**:\n"
             "- *I want to study marine biology.*\n"
             "- *She hopes to find an apprenticeship next year.*\n"
             "- *He decided not to apply.*"),
        ],
        "practise_g": [
            "1. Build: *I / want / become / a teacher* → ___ ; *she "
            "/ plan / take / a gap year* → ___ .",
            "2. Match: doctor — hospital, baker — bakery, "
            "electrician — wiring, programmer — code.",
        ],
        "practise_m": [
            "3. Build 4 sentences using *want, hope, plan, decide* "
            "+ to-infinitive.",
        ],
        "answer_g": (
            "1. *I want to become a teacher. She plans to take a "
            "gap year.*\n"
            "2. all true."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Pair speaking — *Future Plans*.** 2 min each. Cover: "
            "one job that interests you, one skill you want to "
            "learn, one obstacle, one step you can take next month."
        ),
        "produce_sample": (
            "*— I'm thinking of an apprenticeship as an "
            "electrician. I want to learn the practical side, but "
            "I also need to keep my English up. Next month I plan "
            "to ask my uncle, who is one, if I can shadow him for "
            "a day.*"
        ),
        "reflect": [
            "I can name 12 jobs.",
            "I can use *want/hope/plan/decide + to-infinitive*.",
            "I can hold a 2-minute career conversation.",
        ],
        "pitfalls": [
            "*I want become* → ✗ / *I want to become* → ✓.",
            "*I'm planning learn* → ✗ / *I'm planning to learn* → ✓.",
            "*Career* in English ≠ German *Karriere* — *career* is "
            "any working life, not necessarily upward.",
        ],
        "further": [
            "BBC Bitesize Careers — accessible job profiles.",
            "National Careers Service (UK) — job-skill matrices.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"Eli wants to study marine biology. He hopes to "
            "spend a year in Spain. He plans to start an "
            "apprenticeship if his university plans don't work "
            "out. He has decided not to give up on the sea, "
            "either way.\"\n\n"
            "1. Wants: ___ . 2. Hopes: ___ . 3. Plan B: ___ . "
            "4. Decided: ___ ."
        ),
        "exam_reading": (
            "Read.\n\n"
            "> \"Naima is finishing Klasse 9. She has decided to "
            "do a one-year apprenticeship at a local bakery before "
            "going back to school. She wants to know whether the "
            "job suits her before committing to four years of "
            "training. Her parents agreed but asked her to keep up "
            "her English in the evenings.\"\n\n"
            "1. Decision: ___ . 2. Reason: ___ . 3. Length: ___ . "
            "4. Parents' condition: ___ ."
        ),
        "exam_use": (
            "**Verb + to-infinitive.**\n\n"
            "1. I __________ (want) study English.\n"
            "2. She __________ (plan) take a gap year.\n"
            "3. He __________ (decide / not) apply.\n"
            "4. We __________ (hope) find an internship."
        ),
        "exam_writing": (
            "Write 120 words about your career plans (real or "
            "imagined). Use 4 verb + to-infinitive structures."
        ),
        "exam_keys": [
            "**T1.** to study marine biology, to spend a year in Spain, an apprenticeship, not to give up on the sea.",
            "**T2.** one-year apprenticeship at a local bakery; wants to test the job before 4 years training; one year; keep up her English in the evenings.",
            "**T3.** want to / plans to / decided not to / hope to.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 2, "slug": "money-and-choices", "title": "Money and Choices",
        "skills": ["reading", "writing", "language_awareness"],
        "bp": [
            "3.2.1 Soziokulturelles Orientierungswissen / Themen",
            "3.2.3.2 Leseverstehen",
            "3.2.3.5 Schreiben",
            "3.2.3.8 Verfügen über sprachliche Mittel – Grammatik",
        ],
        "objectives": [
            "I can read a short text on personal finance and identify the writer's advice.",
            "I can use *should / shouldn't / had better* for advice.",
            "I can write a 120-word reflection on a money decision.",
        ],
        "leadin": (
            "Eli is saving for a second-hand bicycle. Naima is "
            "saving for a one-week language course in Dublin. They "
            "are both keeping notebooks. Eli's is a small green "
            "ledger; Naima's is a sticky note that has migrated "
            "five times in two months. Mr. Yilmaz, who has watched "
            "this, says: \"How you keep the record is part of the "
            "discipline.\""
        ),
        "activate": (
            "**Money quick-think.** In 90 seconds write *one thing "
            "I save for, one thing I waste on, one thing I would "
            "save for if I had a goal*."
        ),
        "input_blocks": [
            ("Vocabulary — money",
             "*to save up, to spend, to waste, to budget, to lend, "
             "to borrow, to owe, salary, wage, pocket money, "
             "interest, debt, savings account, ATM, cash, card, "
             "digital wallet.*"),
            ("Grammar — *should / shouldn't / had better*",
             "Mild advice: *You should save 10 % of your pocket money.*\n"
             "Mild warning: *You shouldn't lend money you can't afford to lose.*\n"
             "Stronger advice / warning: *You'd better keep a "
             "record* (= it would be a mistake not to)."),
        ],
        "practise_g": [
            "1. Choose *should / shouldn't*: You __________ keep a "
            "small notebook. You __________ borrow what you "
            "can't return.",
            "2. Build *had better*: You / save / receipts → ___ .",
        ],
        "practise_m": [
            "3. Build 4 advice sentences (2 *should*, 1 *shouldn't*, "
            "1 *had better*) for a younger student saving for a "
            "trip.",
        ],
        "answer_g": (
            "1. should / shouldn't.\n"
            "2. *You'd better save your receipts.*"
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Reflection, 120 words.** Write about a money "
            "decision — real or invented. Use *should / shouldn't "
            "/ had better* twice and *if* once."
        ),
        "produce_sample": (
            "*Last year I saved for a second-hand bike. I should "
            "have started earlier, because the price went up "
            "twice. I had a small notebook in which I wrote every "
            "amount I added. If I had not kept the notebook, I "
            "would have lost track. My advice to a younger student "
            "would be simple: you should write it down, you "
            "shouldn't try to remember, and you'd better protect "
            "the notebook from siblings.*"
        ),
        "reflect": [
            "I can read a personal-finance text and find advice.",
            "I can use *should / shouldn't / had better*.",
            "I can write a 120-word money reflection.",
        ],
        "pitfalls": [
            "*You should to save* → ✗ / *You should save* → ✓.",
            "*You had better to keep* → ✗ / *You had better keep* → ✓.",
            "*should* and *must* feel different in advice — *must* "
            "is stronger and more imposed.",
        ],
        "further": [
            "BBC Bitesize — *Personal finance* topic.",
            "MoneyHelper UK — accessible articles for teens.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"You should keep a record of every purchase. You "
            "shouldn't lend more than you can afford to lose. You'd "
            "better start small — three months of pocket money is "
            "enough to learn the habit.\"\n\n"
            "1. Should keep: ___ . 2. Shouldn't lend: ___ . "
            "3. Had better: ___ . 4. Length: ___ ."
        ),
        "exam_reading": (
            "Read.\n\n"
            "> \"Eli started a small green notebook. By month four "
            "he could see the shape of his spending: half on food "
            "outside the home, a quarter on small things he didn't "
            "remember buying. He decided to cut the small "
            "things.\"\n\n"
            "1. Notebook colour: ___ . 2. Half spending: ___ . "
            "3. Quarter spending: ___ . 4. Decision: ___ ."
        ),
        "exam_use": (
            "**Fill in *should / shouldn't / had better*.**\n\n"
            "1. You __________ save 10 %.\n"
            "2. You __________ lend what you can't afford.\n"
            "3. You __________ start now, before prices change.\n"
            "4. We __________ keep all receipts."
        ),
        "exam_writing": (
            "Write 120 words about a money decision. Use *should / "
            "shouldn't / had better* (3 in total)."
        ),
        "exam_keys": [
            "**T1.** every purchase, more than you can afford to lose, start small, three months.",
            "**T2.** small green; half — food outside the home; quarter — small things not remembered; cut the small things.",
            "**T3.** should / shouldn't / had better / should.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 3, "slug": "the-environment-locally", "title": "The Environment, Locally",
        "skills": ["reading", "writing", "intercultural"],
        "bp": [
            "3.2.1 Soziokulturelles Orientierungswissen / Themen",
            "3.2.2 Interkulturelle kommunikative Kompetenz",
            "3.2.3.2 Leseverstehen",
            "3.2.3.5 Schreiben",
            "3.2.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can read a short environment text and identify cause and effect.",
            "I can use *if + present, will-future* (first conditional) for predictions.",
            "I can write a 120-word local environment proposal.",
        ],
        "leadin": (
            "Naima's class is mapping the litter on a 200-metre "
            "stretch of street outside the school. They are "
            "using a clipboard, a tally chart, and one rather "
            "reluctant volunteer who brought gloves. After three "
            "days they have 412 plastic items, 201 paper items, "
            "and one extremely confused fox who wants to know "
            "what they're doing."
        ),
        "activate": (
            "**Local-noticing scan.** Spend 60 seconds listing 5 "
            "environment problems you notice within 200 metres of "
            "the school."
        ),
        "input_blocks": [
            ("Vocabulary — environment",
             "*pollution, litter, recycling, single-use plastic, "
             "compost, emissions, carbon footprint, biodiversity, "
             "habitat, extinction, sustainable, renewable, local "
             "authority, council, petition, campaign.*"),
            ("Grammar — first conditional",
             "Form: *If* + present simple, *will* + base verb.\n"
             "- *If we keep the chart, we will see the trend.*\n"
             "- *If the council acts, the litter will decrease.*\n"
             "- *Won't* in the result: *If we do nothing, things "
             "won't change.*"),
        ],
        "practise_g": [
            "1. Build first conditional: *(if / we / map / litter) "
            "/ (we / understand / problem)* → ___ .",
            "2. Match: pollution → litter; compost → biodegradable "
            "waste; recycling → reuse.",
        ],
        "practise_m": [
            "3. Build 4 first-conditional sentences about a local "
            "environment fix.",
        ],
        "answer_g": (
            "1. *If we map the litter, we will understand the "
            "problem.*\n"
            "2. all true."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Local proposal, 120 words.** Write to the school or "
            "local council about a fixable environment issue near "
            "your school. Use 3 first conditionals + 2 advice "
            "structures."
        ),
        "produce_sample": (
            "*Dear Local Council, our class has counted 412 "
            "plastic items over 200 metres of street near our "
            "school. If you place two more bins along this "
            "stretch, the count will probably halve. If the bins "
            "are emptied weekly, they won't overflow. We would "
            "also ask that the school be invited to do a yearly "
            "count, so we can track whether the change is real. "
            "If we measure twice a year, we will know whether "
            "small actions actually work, and the next class "
            "won't have to start again.*"
        ),
        "reflect": [
            "I can identify cause-and-effect in an environment text.",
            "I can use first conditionals correctly.",
            "I can write a 120-word local proposal.",
        ],
        "pitfalls": [
            "*If we will map* → ✗ / *If we map* → ✓.",
            "*if + would* → ✗ in the if-clause for first conditional.",
            "*pollution* is uncountable: *a pollution* → ✗ / *some "
            "pollution* → ✓.",
        ],
        "further": [
            "BBC Newsround — local environment stories.",
            "WWF UK Schools — accessible factsheets.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"If you place two more bins along this 200-metre "
            "stretch, the litter count will halve. If the bins are "
            "emptied weekly, they won't overflow. We will measure "
            "twice a year so we know whether the change is "
            "real.\"\n\n"
            "1. Action 1: ___ . 2. Effect 1: ___ . 3. Action 2: "
            "___ . 4. Measurement frequency: ___ ."
        ),
        "exam_reading": (
            "Read.\n\n"
            "> \"The street outside Klasse 9's school had 412 "
            "plastic items in three days. After the council added "
            "two bins, the number fell to 198 in the next count. "
            "The class has decided to repeat the count every six "
            "months.\"\n\n"
            "1. Initial: ___ . 2. Action: ___ . 3. New count: "
            "___ . 4. Frequency: ___ ."
        ),
        "exam_use": (
            "**First conditional.**\n\n"
            "1. If we __________ (count) the litter, we __________ "
            "(see) the trend.\n"
            "2. If the council __________ (add) bins, the litter "
            "__________ (decrease).\n"
            "3. If we __________ (do / not) anything, things "
            "__________ (not / change).\n"
            "4. If they __________ (empty) the bins weekly, they "
            "__________ (not / overflow)."
        ),
        "exam_writing": (
            "Write 120 words: a proposal to the council on a "
            "local environment issue. Use 3 first conditionals."
        ),
        "exam_keys": [
            "**T1.** add 2 bins; litter halves; empty weekly; twice a year.",
            "**T2.** 412 plastic items in 3 days; council added 2 bins; 198; every 6 months.",
            "**T3.** count / will see; add / will decrease; don't do / won't change; empty / won't overflow.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 4, "slug": "canada-perspectives", "title": "Canada: Perspectives",
        "skills": ["reading", "writing", "intercultural"],
        "bp": [
            "3.2.1 Soziokulturelles Orientierungswissen / Themen",
            "3.2.2 Interkulturelle kommunikative Kompetenz",
            "3.2.3.2 Leseverstehen",
            "3.2.3.5 Schreiben",
            "3.2.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can read a short text about Canada and identify two cultural anchors.",
            "I can use the past passive (*was/were + past participle*).",
            "I can write a 120-word reflection on a region's history.",
        ],
        "leadin": (
            "Naima's geography teacher showed a map of Canada. The "
            "class noticed how few towns were visible in the "
            "north. Mr. Yilmaz, passing the room, mentioned that "
            "his cousin had spent a year in Yukon. The "
            "temperature in Whitehorse, the cousin had written, "
            "*reorganises your priorities for you*. The class "
            "wrote that line down."
        ),
        "activate": (
            "**Canada five.** With your partner, write down five "
            "things you associate with Canada. Test which are "
            "stereotypes and which are facts."
        ),
        "input_blocks": [
            ("Reading — *Whitehorse, Yukon*",
             "*Whitehorse was named after the white-foam rapids "
             "of the Yukon River. The town was founded as a stop "
             "on the gold-rush route. It is now the capital of "
             "the Yukon Territory. Many Indigenous peoples — "
             "First Nations such as the Kwanlin Dün and the Ta'an "
             "Kwäch'än — were already living in the area for "
             "thousands of years before Europeans arrived. Today "
             "their languages are taught in schools alongside "
             "English and French.*"),
            ("Grammar — past passive",
             "Form: *was/were + past participle*.\n"
             "- *Whitehorse **was named** after the rapids.*\n"
             "- *The town **was founded** as a stop on the route.*\n"
             "- *Indigenous languages **were spoken** for thousands "
             "of years before Europeans arrived.*"),
        ],
        "practise_g": [
            "1. Active → past passive: They named the town. → ___ ; "
            "Settlers founded the city. → ___ .",
            "2. Choose: *Indigenous languages __________ (speak / "
            "past passive) for thousands of years.*",
        ],
        "practise_m": [
            "3. Build 3 past-passive sentences about a place's "
            "history.",
        ],
        "answer_g": (
            "1. *The town was named. The city was founded by "
            "settlers.*\n"
            "2. were spoken."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Region reflection, 120 words.** Write about an "
            "English-speaking region (Canada, Australia, New "
            "Zealand, South Africa) — its name origin, who lived "
            "there before, what languages are spoken now. Use 4 "
            "past-passive structures."
        ),
        "produce_sample": (
            "*Whitehorse, the capital of Yukon, was named after "
            "the rapids on the Yukon River. The town was founded "
            "as a stop on the Klondike gold-rush route. The land, "
            "however, had been lived on for thousands of years "
            "before Europeans arrived. Today the languages of the "
            "Kwanlin Dün and Ta'an Kwäch'än First Nations are "
            "taught in schools alongside English and French. In "
            "the long winter, when sunlight is short, daily life "
            "is reorganised around the cold. People joke that "
            "winter is not survived but negotiated.*"
        ),
        "reflect": [
            "I can read a Canada text and find two cultural anchors.",
            "I can build past-passive sentences.",
            "I can write a 120-word region reflection.",
        ],
        "pitfalls": [
            "*The town was found* (= located accidentally) vs. "
            "*was founded* (= established) — different verbs.",
            "Stereotype check: Canada ≠ only ice-hockey + maple "
            "syrup.",
            "Indigenous: capital I; *the Indigenous peoples* "
            "preferred over *natives*.",
        ],
        "further": [
            "CBC Kids News — accessible Canadian news.",
            "Indigenous Tourism Association of Canada — official "
            "perspectives.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"Whitehorse was named after the white-foam rapids "
            "of the Yukon River. The town was founded during the "
            "gold rush. Indigenous languages were spoken in the "
            "area for thousands of years before Europeans arrived. "
            "Today they are taught in schools.\"\n\n"
            "1. Named after: ___ . 2. Founded during: ___ . 3. "
            "Indigenous languages: ___ . 4. Today: ___ ."
        ),
        "exam_reading": (
            "Read the *Whitehorse, Yukon* text above. Answer.\n\n"
            "1. River: ___ . 2. Why founded: ___ . 3. Two First "
            "Nations: ___ . 4. Languages today: ___ ."
        ),
        "exam_use": (
            "**Past passive.**\n\n"
            "1. Whitehorse __________ (name) after the rapids.\n"
            "2. The town __________ (found) during the gold rush.\n"
            "3. Indigenous languages __________ (speak) for "
            "thousands of years.\n"
            "4. Today they __________ (teach) in schools."
        ),
        "exam_writing": (
            "Write 120 words about an English-speaking region's "
            "history. Use 4 past-passive structures."
        ),
        "exam_keys": [
            "**T1.** rapids of Yukon River; gold rush; spoken for thousands of years; taught in schools.",
            "**T2.** Yukon River; gold-rush route stop; Kwanlin Dün and Ta'an Kwäch'än; First Nations languages alongside English and French.",
            "**T3.** was named / was founded / were spoken / are taught.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 5, "slug": "media-literacy", "title": "Media Literacy",
        "skills": ["reading", "listening", "language_awareness"],
        "bp": [
            "3.2.1 Soziokulturelles Orientierungswissen / Themen",
            "3.2.3.1 Hör-/Hörsehverstehen",
            "3.2.3.2 Leseverstehen",
            "3.2.3.7 Verfügen über sprachliche Mittel – Wortschatz",
            "3.2.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can spot 3 signs of misinformation in a short article.",
            "I can use *seem to / appear to / claim to* for hedged claims.",
            "I can write a 120-word media-literacy review.",
        ],
        "leadin": (
            "Eli's uncle forwarded a viral post. The post claimed "
            "a new wonder-fruit could solve everything from sleep "
            "problems to maths grades. Eli read it twice. \"Mr. "
            "Yilmaz,\" he said, \"is *every fruit* like this?\" "
            "Mr. Yilmaz smiled. \"No,\" he said. \"But every "
            "viral post is. Welcome to media literacy.\""
        ),
        "activate": (
            "**Headline scan.** Three real-looking headlines on "
            "the slide. With your partner, mark each one *likely "
            "true / likely false / would need to check*."
        ),
        "input_blocks": [
            ("Vocabulary — media literacy",
             "*source, claim, evidence, fact-check, "
             "misinformation, disinformation, bias, headline, "
             "clickbait, study, statistic, anecdote, primary "
             "source, peer-reviewed, fake news, viral.*"),
            ("Grammar — hedged claims",
             "*seem to / appear to / claim to / be reported to* "
             "+ base verb.\n"
             "- *The fruit **seems to** improve sleep.*\n"
             "- *The article **claims to** be based on a study.*\n"
             "- *Critics **appear to** disagree.*\n"
             "Hedged language is what careful writing sounds like — "
             "neither lying nor over-claiming."),
        ],
        "practise_g": [
            "1. Choose: *seems / claims / appears*: This study "
            "__________ to be peer-reviewed. The article "
            "__________ to support the claim, but the link is "
            "broken.",
            "2. Match: clickbait → exaggerated headline; primary "
            "source → original. (T / F)",
        ],
        "practise_m": [
            "3. Build 4 hedged-claim sentences about a viral post "
            "or article.",
        ],
        "answer_g": (
            "1. claims / appears.\n"
            "2. all true."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Mini-review, 120 words.** Pick a viral post or "
            "article. Write a short review: *Source? Evidence? "
            "Bias?* + *what would change my mind*. Use 3 hedged "
            "claims."
        ),
        "produce_sample": (
            "*The article I read seems to claim that a new fruit "
            "improves sleep, mood, and maths grades. The source is "
            "a small website I have never seen before. The article "
            "appears to cite a study, but the link is broken. The "
            "language is highly enthusiastic, which is a typical "
            "clickbait sign. I am not saying the fruit is bad — I "
            "am saying I cannot tell from this article. What would "
            "change my mind: a peer-reviewed study, a named "
            "researcher, and one critical voice in the article "
            "itself.*"
        ),
        "reflect": [
            "I can spot 3 signs of misinformation.",
            "I can use *seem to / appear to / claim to*.",
            "I can write a 120-word media-literacy review.",
        ],
        "pitfalls": [
            "*The article seems claim* → ✗ / *The article seems "
            "to claim* → ✓.",
            "Don't confuse *fake* with *biased* — biased can still "
            "be factually true.",
            "L1 trap: German *behaupten* → English *claim*, with "
            "neutral tone, not always negative.",
        ],
        "further": [
            "BBC Reality Check.",
            "Snopes — fact-checking site.",
            "FullFact (UK).",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"The post seems to claim that a new fruit improves "
            "sleep, mood, and maths grades. The article appears to "
            "cite a study, but the link is broken. Several "
            "experts claim to have tested the fruit and found no "
            "such effect.\"\n\n"
            "1. The post claims: ___ . 2. The link: ___ . 3. "
            "Experts: ___ . 4. Effect found: ___ ."
        ),
        "exam_reading": (
            "Read.\n\n"
            "> \"Headline: 'WONDER FRUIT FIXES YOUR SLEEP.' The "
            "article cites no study. The named expert is not on "
            "any university website. The website itself was "
            "registered three weeks ago. None of these signs is a "
            "direct lie. Together, they are a warning.\"\n\n"
            "1. Headline style: ___ . 2. Study cited: ___ . 3. "
            "Expert verifiable: ___ . 4. Site age: ___ ."
        ),
        "exam_use": (
            "**Hedged claim.**\n\n"
            "1. The article __________ (seem) to support the "
            "claim.\n"
            "2. Several experts __________ (claim) the post.\n"
            "3. The author __________ (appear) to be a real "
            "person.\n"
            "4. The fruit __________ (be reported) to improve "
            "sleep."
        ),
        "exam_writing": (
            "Write 120 words: a media-literacy review of a viral "
            "post. Use 3 hedged claims."
        ),
        "exam_keys": [
            "**T1.** improvements in sleep / mood / maths grades; broken; have tested it; no such effect.",
            "**T2.** clickbait / exaggerated; no; not on any university website; three weeks old.",
            "**T3.** seems / dispute (or claim against) / appears / is reported.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 6, "slug": "interview-and-portrait", "title": "Interview and Portrait",
        "skills": ["speaking", "writing", "language_awareness"],
        "bp": [
            "3.2.1 Soziokulturelles Orientierungswissen / Themen",
            "3.2.3.3 Sprechen – an Gesprächen teilnehmen",
            "3.2.3.5 Schreiben",
            "3.2.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can prepare 8 open interview questions.",
            "I can hold a 5-minute interview and report it back in writing.",
            "I can write a 150-word portrait of a real person.",
        ],
        "leadin": (
            "Naima is interviewing the school caretaker, Mrs. "
            "Brock, who has worked at the school for 21 years and "
            "claims to remember every student's name. She is "
            "almost certainly exaggerating. Naima has prepared "
            "eight open questions and one fall-back question, "
            "*tell me about a student you remember*, in case the "
            "interview stalls."
        ),
        "activate": (
            "**Open vs. closed.** On the slide are six interview "
            "questions. With your partner, mark each as *open* or "
            "*closed*. Rewrite two closed ones as open ones."
        ),
        "input_blocks": [
            ("Interview vocabulary",
             "*interview, interviewer, interviewee, "
             "open question (Wh-), closed question (yes/no), "
             "follow-up, transcript, off the record, on the record, "
             "quote, paraphrase.*"),
            ("Open question forms",
             "- *Tell me about …*\n"
             "- *Could you describe …?*\n"
             "- *What was it like when …?*\n"
             "- *How did you decide to …?*\n"
             "- *Why did you choose …?*\n"
             "- *What do you remember most about …?*"),
            ("Reporting an interview in writing",
             "Direct: *\"I remember the day,\" she said.*\n"
             "Reported: *She said she remembered the day.*\n"
             "Mixed (allowed in journalism): use one short direct "
             "quote per paragraph + reported speech around it."),
        ],
        "practise_g": [
            "1. Mark open or closed: *Did you enjoy your job? — "
            "Tell me about your first day. — How long have you "
            "been here?*",
            "2. Rewrite as open: *Did you have a favourite "
            "student?* → ___ .",
        ],
        "practise_m": [
            "3. Prepare 8 open interview questions for an "
            "imagined interviewee.",
        ],
        "answer_g": (
            "1. closed / open / open.\n"
            "2. *Tell me about a student you remember.*"
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Interview + 150-word portrait.** In pairs, run a "
            "5-minute interview based on 8 open questions. Then "
            "write a 150-word portrait of your interviewee with "
            "at least one direct quote and 4 sentences of "
            "reported speech."
        ),
        "produce_sample": (
            "*Mrs. Brock has worked at our school for 21 years. "
            "She says she remembers every student's name, and the "
            "way she said this, leaning forward slightly, made me "
            "almost believe her. \"You forget faces but you "
            "remember voices,\" she told me. She came to the school "
            "because her sister-in-law had worked here in the 90s. "
            "She added, smiling, that her favourite part of the "
            "job was the empty corridor between 7:30 and 7:55 in "
            "the morning. \"Best minutes of the building,\" she "
            "said. \"Everything is about to start, and nothing has "
            "gone wrong yet.\"*"
        ),
        "reflect": [
            "I can prepare 8 open interview questions.",
            "I can run a 5-minute interview.",
            "I can write a 150-word portrait with one direct quote.",
        ],
        "pitfalls": [
            "Reading questions off a list robotically — listen "
            "and follow up.",
            "Direct quote without inverted commas → ✗.",
            "Transcribing every word — pick the one quote that "
            "lands.",
        ],
        "further": [
            "BBC News — *In Pictures* / portrait journalism.",
            "The Guardian — *Long reads* (selected).",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"Tell me about your first year here, Mrs. Brock. — "
            "It was a strange year. The boiler broke twice, but "
            "the children were calm. — What do you remember most? — "
            "The day the heating failed in February — we wore "
            "coats in lessons.\"\n\n"
            "1. Open question 1: ___ . 2. First-year fact: ___ . "
            "3. Open question 2: ___ . 4. Memorable day: ___ ."
        ),
        "exam_reading": (
            "Read the portrait sample above. Answer.\n\n"
            "1. Years at school: ___ . 2. One direct quote: ___ . "
            "3. How she came to the school: ___ . 4. Favourite "
            "minutes: ___ ."
        ),
        "exam_use": (
            "**Direct → reported.**\n\n"
            "1. \"I remember every name,\" she said. → ___\n"
            "2. \"Where do you live?\" he asked. → ___\n"
            "3. \"Did you enjoy it?\" he asked. → ___\n"
            "4. \"I am proud of the children,\" she said. → ___"
        ),
        "exam_writing": (
            "Write a 150-word portrait of a real person you can "
            "imagine interviewing. Include one direct quote."
        ),
        "exam_keys": [
            "**T1.** *Tell me about your first year.*; boiler broke twice / children calm; *What do you remember most?*; February — heating failed.",
            "**T2.** 21 years; *\"You forget faces but you remember voices\"* / *\"Best minutes of the building\"*; her sister-in-law had worked there in the 90s; 7:30–7:55 morning corridor.",
            "**T3.** *She said she remembered every name. He asked where I lived. He asked if I had enjoyed it. She said she was proud of the children.*",
            "**T4.** Open.",
        ],
    },
    {
        "n": 7, "slug": "mediation-news-article", "title": "Mediation: A German News Article",
        "skills": ["mediation", "writing", "language_awareness"],
        "bp": [
            "3.2.1 Soziokulturelles Orientierungswissen / Themen",
            "3.2.3.5 Schreiben",
            "3.2.3.6 Sprachmittlung",
            "3.2.3.7 Verfügen über sprachliche Mittel – Wortschatz",
        ],
        "objectives": [
            "I can mediate a German news article into 5–7 English sentences for a peer.",
            "I can keep facts, drop ceremony, and adjust register.",
            "I can use 6 reporting verbs (says, explains, claims, points out, warns, recommends).",
        ],
        "leadin": (
            "Naima's German uncle forwarded a news article about "
            "a bus-route change. Her English-speaking cousin in "
            "Toronto needed to know whether her *favourite shop* "
            "was still reachable. Naima translated nothing. She "
            "explained."
        ),
        "activate": (
            "**Drop or keep?** On the slide are six lines from a "
            "German news article. Mark each as *essential / "
            "paraphrase / drop* depending on the addressee."
        ),
        "input_blocks": [
            ("Source — *German news article (excerpt)*",
             "*Die Stadtverwaltung hat angekündigt, dass die Linie "
             "42 ab dem 1. September einen neuen Fahrplan haben "
             "wird. Die Buslinie wird zwei zusätzliche Haltestellen "
             "im Stadtteil Ost bedienen. Die Fahrtzeit verlängert "
             "sich dadurch um etwa fünf Minuten. Pendler werden "
             "gebeten, die neue Verbindung im Online-Fahrplan zu "
             "überprüfen.*"),
            ("Mediation rules — Klasse 9 version",
             "1. *Who is reading?* — register, formality.\n"
             "2. *What do they need?* — keep facts, drop "
             "decoration.\n"
             "3. *What is the smallest version?* — without losing "
             "meaning.\n"
             "4. *Are there cultural notes that need explaining?*"),
            ("Reporting verbs (extended)",
             "*to say, to explain, to mention, to claim, to "
             "advise, to warn, to recommend, to point out, to "
             "stress, to add, to deny.*"),
        ],
        "practise_g": [
            "1. Match German verb to English: *bestreiten — ?, "
            "betonen — ?, hinzufügen — ?, mahnen — ?*.",
            "2. Choose: *say / claim / explain / warn* — The "
            "article __________ that the route will change. "
            "Critics __________ that this will hurt elderly "
            "passengers.",
        ],
        "practise_m": [
            "3. Build a 5-sentence English mediation of the source "
            "article above.",
        ],
        "answer_g": (
            "1. deny / stress / add / warn.\n"
            "2. says or explains / warn or claim."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Mediation, 6–7 sentences.** Read the German "
            "source above. Write 6–7 English sentences for a "
            "Canadian friend who has asked whether a particular "
            "bus stop is still reachable. Use 4 reporting verbs."
        ),
        "produce_sample": (
            "*Hi Jo, here's the gist of the article. The city "
            "council has announced a new timetable for bus line "
            "42, starting 1 September. The article explains that "
            "two extra stops are being added in the eastern part "
            "of town. It mentions the journey will be about five "
            "minutes longer. Officials advise passengers to check "
            "the online schedule. The article also points out that "
            "all current stops are kept, so your favourite shop "
            "should still be reachable. The change starts in two "
            "weeks.*"
        ),
        "reflect": [
            "I can mediate a German article into 6 English sentences.",
            "I can drop ceremony and keep facts.",
            "I can use 4 reporting verbs.",
        ],
        "pitfalls": [
            "Literal translation kills mediation.",
            "Carrying over German salutations into a peer message.",
            "Cultural notes — when needed, give them; when not, "
            "skip.",
        ],
        "further": [
            "Goethe-Institut — Beispiel-Aufgaben Sprachmittlung.",
            "Landesbildungsserver BW — Mediation-Beispielaufgaben.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"Die Stadtverwaltung hat angekündigt, dass die "
            "Linie 42 ab dem 1. September einen neuen Fahrplan "
            "haben wird. Die Fahrtzeit verlängert sich um etwa "
            "fünf Minuten.\"\n\n"
            "1. Topic: ___ . 2. Date: ___ . 3. Time change: ___ . "
            "4. Source-language: ___ ."
        ),
        "exam_reading": (
            "Read the German source above. Answer in English.\n\n"
            "1. Authority: ___ . 2. Date of change: ___ . 3. Two "
            "extra stops in: ___ . 4. Action requested: ___ ."
        ),
        "exam_use": (
            "**Reporting-verb fill-in.**\n\n"
            "1. The article __________ that line 42 has a new "
            "timetable. (says)\n"
            "2. Officials __________ passengers to check online. "
            "(advise)\n"
            "3. The author __________ that the change is small. "
            "(claims)\n"
            "4. Critics __________ that elderly passengers will "
            "be affected. (warn)"
        ),
        "exam_writing": (
            "Mediate: write 6 English sentences from the German "
            "source for a friend abroad. Use 3 reporting verbs."
        ),
        "exam_keys": [
            "**T1.** new bus line 42 timetable; 1 September; about 5 min longer; German.",
            "**T2.** city council; 1 September; the eastern part of town; check the online timetable.",
            "**T3.** says / advise / claims / warn.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 8, "slug": "inequality-and-voice", "title": "Inequality and Voice",
        "skills": ["reading", "writing", "language_awareness"],
        "bp": [
            "3.2.1 Soziokulturelles Orientierungswissen / Themen",
            "3.2.2 Interkulturelle kommunikative Kompetenz",
            "3.2.3.2 Leseverstehen",
            "3.2.3.5 Schreiben",
            "3.2.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can read a short text on a social issue and identify the writer's perspective.",
            "I can use *despite / in spite of / because of* + noun.",
            "I can write a 150-word reflection that takes a clear position.",
        ],
        "leadin": (
            "Eli's class read a short text about food inequality "
            "in their own town. The school cafeteria is free for "
            "students who qualify. The qualification is invisible — "
            "the cards look the same. Mr. Yilmaz pointed out that "
            "the cards were redesigned three years ago precisely "
            "so they would all look the same. \"That's a small "
            "thing,\" Naima said. Mr. Yilmaz nodded. \"Small things "
            "do most of the work.\""
        ),
        "activate": (
            "**Quick noticing.** Write down 3 places in your daily "
            "life where access is unequal. (Public transport, "
            "school clubs, holidays …) No judgement — just notice."
        ),
        "input_blocks": [
            ("Vocabulary — inequality",
             "*inequality, fairness, access, opportunity, "
             "privilege, disadvantage, support, scholarship, "
             "subsidy, free school meals, social mobility, "
             "discrimination, exclusion, inclusion, voice, "
             "representation.*"),
            ("Grammar — *despite / in spite of / because of*",
             "All three take **a noun** or **-ing verb**, not a "
             "full clause:\n"
             "- *Despite the rain, we played football.*\n"
             "- *In spite of the noise, she focused.*\n"
             "- *Because of the new rule, prices changed.*\n\n"
             "For full clauses, use *although* or *because*."),
        ],
        "practise_g": [
            "1. Choose: *despite / in spite of / because of*: "
            "__________ the rain, we played. __________ the new "
            "policy, prices fell.",
            "2. Build a sentence with *despite + noun*: *(rain / "
            "we / played)* → ___ .",
        ],
        "practise_m": [
            "3. Build 4 sentences using *despite, in spite of, "
            "because of, although* about a fairness topic.",
        ],
        "answer_g": (
            "1. Despite (or In spite of) / Because of.\n"
            "2. *Despite the rain, we played.*"
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Reflection, 150 words.** Take a clear position on a "
            "small fairness issue. Use 2 *despite/because of* + "
            "1 *although* + 1 strong claim sentence."
        ),
        "produce_sample": (
            "*The school redesigned its lunch cards three years "
            "ago, so that the cards of students who qualify for "
            "free meals look exactly the same as everyone else's. "
            "It's a small thing. Despite the small surface, the "
            "effect is real: no student has to walk past a "
            "different-coloured card on the way to the trays. "
            "Although adults sometimes call this kind of detail "
            "cosmetic, I disagree. Because of one design choice, "
            "the cafeteria queue stops being a place where "
            "income is visible. In my view, a school is most "
            "fair when its smallest details have been thought "
            "through this carefully. Posters on the wall are "
            "easy. Cards in pockets are not.*"
        ),
        "reflect": [
            "I can read a fairness text and find the writer's perspective.",
            "I can use *despite / in spite of / because of* with nouns.",
            "I can write a 150-word reflection with a clear position.",
        ],
        "pitfalls": [
            "*Despite I was tired* → ✗ — *despite* takes a noun, "
            "not a full clause.",
            "*Because of + clause* → ✗ — *because + clause* is "
            "right.",
            "Avoid *the poor / the rich* — prefer *students who "
            "qualify for support* or similar.",
        ],
        "further": [
            "BBC News — *Education* social-issue articles.",
            "JRF (Joseph Rowntree Foundation, UK) — accessible reports.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"Despite a small budget, the school redesigned the "
            "lunch cards three years ago. Because of that change, "
            "no student now walks past a different-coloured card. "
            "Although the change looks cosmetic, the effect is "
            "real.\"\n\n"
            "1. *Despite + noun*: ___ . 2. Action: ___ . 3. "
            "Effect: ___ . 4. *Although* clause: ___ ."
        ),
        "exam_reading": (
            "Read.\n\n"
            "> \"Free school meals exist for students whose "
            "families qualify. The cards used to look different, "
            "and the difference was visible in the queue. Now the "
            "cards look the same. Some adults call this cosmetic. "
            "Most students don't.\"\n\n"
            "1. Why free meals: ___ . 2. Old cards: ___ . 3. New "
            "cards: ___ . 4. Adults vs. students: ___ ."
        ),
        "exam_use": (
            "**Fill in *despite / in spite of / because of / "
            "although*.**\n\n"
            "1. ___ the rain, we played football.\n"
            "2. ___ the new policy, prices changed.\n"
            "3. ___ I was tired, I finished the test.\n"
            "4. ___ the small budget, the school redesigned the "
            "cards."
        ),
        "exam_writing": (
            "Write 150 words: take a position on a small fairness "
            "issue. Use 3 of: *despite, in spite of, because of, "
            "although*."
        ),
        "exam_keys": [
            "**T1.** small budget; redesigned the lunch cards; no student walks past a different-coloured card; the change looks cosmetic.",
            "**T2.** for students whose families qualify; visible in queue; now look the same; some adults call cosmetic, most students don't.",
            "**T3.** Despite (or In spite of) / Because of / Although / Despite (or In spite of).",
            "**T4.** Open.",
        ],
    },
    {
        "n": 9, "slug": "short-fiction", "title": "Short Fiction in the Classroom",
        "skills": ["reading", "writing", "language_awareness"],
        "bp": [
            "3.2.1 Soziokulturelles Orientierungswissen / Themen",
            "3.2.3.2 Leseverstehen",
            "3.2.3.5 Schreiben",
            "3.2.3.8 Verfügen über sprachliche Mittel – Grammatik",
            "3.2.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can read a short story and identify protagonist, conflict, theme, and one stylistic choice.",
            "I can use the past perfect with *by the time / before / after*.",
            "I can write a 180-word literary response.",
        ],
        "leadin": (
            "Mr. Yilmaz handed out a one-page short story called "
            "*The Found Letter*. \"Read it twice,\" he said. "
            "\"Once for the plot, once for the writing.\" The "
            "first read took eleven minutes. The second took "
            "twenty-three."
        ),
        "activate": (
            "**Style scan.** On the slide is a single sentence: "
            "*\"By the time the bus came, she had already decided.\"* "
            "With your partner, list three things this single "
            "sentence tells you about the story it might belong to."
        ),
        "input_blocks": [
            ("Reading — *The Found Letter* (extract)",
             "*By the time June found the letter, her grandmother "
             "had been dead for six years. The letter was sealed "
             "and unaddressed. It had been written, June was "
             "almost certain, in the days before her grandmother "
             "had stopped writing entirely. The handwriting was "
             "the same — except for one shaky line at the end, "
             "which June read three times before she put the "
             "letter back into the box. She did not open it that "
             "Tuesday. By the next Sunday, she had decided.*"),
            ("Grammar — past perfect with time conjunctions",
             "Use **past perfect** for the earlier of two past "
             "events.\n"
             "- *By the time June found the letter, her "
             "grandmother **had been** dead for six years.*\n"
             "- *Before she opened it, she **had read** it three "
             "times.*\n"
             "- *After she **had decided**, she stopped checking "
             "the box.*"),
        ],
        "practise_g": [
            "1. Past perfect: *(by the time / I / arrive / the "
            "film / start)* → ___ .",
            "2. Choose tense: When she found the letter, her "
            "grandmother __________ (be) dead for six years. (was "
            "/ had been)",
        ],
        "practise_m": [
            "3. Build 3 past-perfect sentences from a story of your "
            "choice (real or invented).",
        ],
        "answer_g": (
            "1. *By the time I arrived, the film had started.*\n"
            "2. had been."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Literary response, 180 words.** Read the extract "
            "above. Answer in writing: *Who is June? What is the "
            "conflict? What is the theme? Which one detail is doing "
            "the most work?* Use 3 past-perfect structures."
        ),
        "produce_sample": (
            "*By the time June found the letter, her grandmother "
            "had been dead for six years. June is, I imagine, "
            "someone in her late teens — old enough to be "
            "trusted with the box, young enough that the loss "
            "still moves through her unfinished. The conflict is "
            "small but heavy: she must decide whether to open "
            "the letter. The theme is what the dead leave us, "
            "and what we owe them. The detail that does the most "
            "work is the *shaky line at the end* — three words "
            "that tell us this letter was written in a body "
            "already failing. The past perfect throughout the "
            "passage builds the layered time the story needs: "
            "the grandmother had stopped writing, the letter had "
            "been written, June had read it three times. By the "
            "next Sunday, she had decided. The story trusts us "
            "not to ask, yet, what she decided.*"
        ),
        "reflect": [
            "I can identify protagonist, conflict, theme, one stylistic choice.",
            "I can use past perfect with time conjunctions.",
            "I can write a 180-word literary response.",
        ],
        "pitfalls": [
            "*Was been* → ✗ — past perfect of *be* is *had been*.",
            "Past perfect needs a second past event for context.",
            "Don't summarise the plot — analyse the moves.",
        ],
        "further": [
            "Project Gutenberg — short stories at A2/B1 level.",
            "Penguin Modern Classics — extracts and notes.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"By the time June found the letter, her grandmother "
            "had been dead for six years. The letter had been "
            "written before her grandmother had stopped writing "
            "entirely. June read it three times before she put it "
            "back.\"\n\n"
            "1. June found: ___ . 2. Years: ___ . 3. Before "
            "stopping: ___ . 4. Reread: ___ ."
        ),
        "exam_reading": (
            "Read the *Found Letter* extract above.\n\n"
            "1. Time gap: ___ . 2. Letter address: ___ . 3. "
            "Detail that surprises: ___ . 4. Decision day: ___ ."
        ),
        "exam_use": (
            "**Past perfect or past simple?**\n\n"
            "1. By the time June __________ (find) the letter, her "
            "grandmother __________ (be) dead for six years.\n"
            "2. Before she __________ (open) the box, she "
            "__________ (read) it three times.\n"
            "3. After she __________ (decide), she __________ "
            "(stop) checking the box."
        ),
        "exam_writing": (
            "Write 180 words: a literary response to the *Found "
            "Letter* extract. Identify protagonist, conflict, "
            "theme, one stylistic choice. Use 3 past-perfect "
            "structures."
        ),
        "exam_keys": [
            "**T1.** the letter; six years; the letter had been written; before putting it back.",
            "**T2.** six years; sealed and unaddressed; one shaky line at the end; the next Sunday.",
            "**T3.** found / had been; opened / had read; had decided / stopped.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 10, "slug": "application-letter", "title": "Writing an Application Letter",
        "skills": ["reading", "writing", "language_awareness"],
        "bp": [
            "3.2.1 Soziokulturelles Orientierungswissen / Themen",
            "3.2.3.2 Leseverstehen",
            "3.2.3.5 Schreiben",
            "3.2.3.7 Verfügen über sprachliche Mittel – Wortschatz",
        ],
        "objectives": [
            "I can read a job ad and pick out 5 requirements.",
            "I can write a 150-word formal application letter.",
            "I can use formal register (no contractions, no slang, polite phrasings).",
        ],
        "leadin": (
            "Eli is applying for a one-week summer job at a small "
            "hotel in Cornwall. The hotel wants *enthusiastic, "
            "responsible, English-speaking helper*. Eli ticks "
            "*enthusiastic* and *English-speaking* with confidence. "
            "*Responsible*, he hopes, will be obvious from the "
            "letter. He has been writing the letter for two days. "
            "It now has six sentences."
        ),
        "activate": (
            "**Job-ad scan.** On the slide is a short job ad. With "
            "your partner, list 5 requirements and 1 piece of "
            "information that tells you what to put in your "
            "letter."
        ),
        "input_blocks": [
            ("Reading — sample job ad",
             "*Summer Helper Wanted, The Old Cottage Hotel, "
             "Cornwall. Three weeks, July. Duties: helping at "
             "breakfast, cleaning rooms, simple admin. We are "
             "looking for an enthusiastic, responsible, "
             "English-speaking person aged 16+. Please send a "
             "short letter of application by 15 May to "
             "manager@oldcottagehotel.example.*"),
            ("Application letter structure",
             "1. **Address block** (your name + address; date).\n"
             "2. **Salutation:** *Dear Sir or Madam* / *Dear Ms "
             "Smith* if name known.\n"
             "3. **Opening:** *I am writing to apply for …*\n"
             "4. **Body:** 1 paragraph on background, 1 on "
             "skills, 1 on motivation.\n"
             "5. **Close:** *I look forward to hearing from you.*\n"
             "6. **Sign-off:** *Yours faithfully* (no name) / "
             "*Yours sincerely* (named)."),
            ("Formal register",
             "- No contractions: *I am* (not *I'm*).\n"
             "- No slang.\n"
             "- Polite hedging: *I would be grateful if … / "
             "Should you require further information, …*"),
        ],
        "practise_g": [
            "1. Match: *Yours faithfully* — Sir/Madam; *Yours "
            "sincerely* — Ms Smith.",
            "2. Make formal: *Hi! I'd love the job. Cheers, Eli.* "
            "→ ___ .",
        ],
        "practise_m": [
            "3. Build the four key sentences: opening, "
            "qualifications, motivation, close.",
        ],
        "answer_g": (
            "1. correct.\n"
            "2. *Dear Sir or Madam, I am writing to apply for the "
            "position. … Yours faithfully, Eli.*"
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Application letter, 150 words.** Write a full "
            "letter for the *Summer Helper* ad above. Use formal "
            "register and the six structural elements."
        ),
        "produce_sample": (
            "*Dear Sir or Madam,*\n\n"
            "*I am writing to apply for the Summer Helper position "
            "at The Old Cottage Hotel, advertised on your website. "
            "I am 16 years old and live in Stuttgart, Germany. I "
            "have just finished Klasse 9 with a strong focus on "
            "English. I have spent two summers helping at a small "
            "café run by my aunt, where I learnt to handle "
            "breakfast service and simple admin tasks. I would be "
            "grateful for the chance to support your team during "
            "the busy July weeks. I am responsible, organised, "
            "and confident in English. I would be available from 1 "
            "July to 21 July. I look forward to hearing from you.*\n\n"
            "*Yours faithfully,*\n*Eli Becker*"
        ),
        "reflect": [
            "I can read a job ad and pick out 5 requirements.",
            "I can write a 150-word formal application letter.",
            "I can keep formal register throughout.",
        ],
        "pitfalls": [
            "Contractions in formal letters → ✗.",
            "*Yours faithfully* with a named person → ✗ — use "
            "*Yours sincerely*.",
            "Generic opening (*I want this job*) — be specific.",
        ],
        "further": [
            "BBC Bitesize — *Formal letter writing*.",
            "British Council — application-letter samples.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"The Old Cottage Hotel is looking for a summer "
            "helper for three weeks in July. Duties include "
            "helping at breakfast, cleaning rooms, and simple "
            "admin. The person should be 16 or older, "
            "enthusiastic, and an English speaker. Applications "
            "by 15 May.\"\n\n"
            "1. Length: ___ . 2. Three duties: ___ . 3. Age: "
            "___ . 4. Deadline: ___ ."
        ),
        "exam_reading": (
            "Read the sample application letter above. Answer.\n\n"
            "1. Position: ___ . 2. Age: ___ . 3. One previous "
            "experience: ___ . 4. Sign-off: ___ ."
        ),
        "exam_use": (
            "**Make formal.**\n\n"
            "1. *Hi, I'd love the job.* → ___\n"
            "2. *I'm 16.* → ___\n"
            "3. *Cheers,* → ___\n"
            "4. *Get back to me when you can.* → ___"
        ),
        "exam_writing": (
            "Write a 150-word application letter for a summer "
            "job (any). Use formal register and the six "
            "structural elements."
        ),
        "exam_keys": [
            "**T1.** 3 weeks in July; breakfast / cleaning rooms / simple admin; 16+; 15 May.",
            "**T2.** Summer Helper, The Old Cottage Hotel; 16; helping at aunt's café (breakfast service + admin); Yours faithfully, Eli Becker.",
            "**T3.** *Dear Sir or Madam, I am writing to apply for the position. / I am 16. / Yours faithfully, / I look forward to hearing from you.*",
            "**T4.** Open.",
        ],
    },
    {
        "n": 11, "slug": "debate-and-discussion", "title": "Debate and Discussion",
        "skills": ["speaking", "listening", "language_awareness"],
        "bp": [
            "3.2.1 Soziokulturelles Orientierungswissen / Themen",
            "3.2.3.1 Hör-/Hörsehverstehen",
            "3.2.3.3 Sprechen – an Gesprächen teilnehmen",
            "3.2.3.4 Sprechen – zusammenhängendes monologisches Sprechen",
        ],
        "objectives": [
            "I can present a 90-second argument for or against a motion.",
            "I can use 6 debate signposts (*I'd like to argue, my opponent claims, however, in response, finally, to summarise*).",
            "I can listen and respond to one specific point in a peer's argument.",
        ],
        "leadin": (
            "Mr. Yilmaz proposed a class debate. The motion: "
            "*This class would replace one written test per term "
            "with a project-based assessment.* Naima leads the "
            "*for*. Eli leads the *against*. Mr. Yilmaz, who "
            "secretly favours both options, is moderator."
        ),
        "activate": (
            "**Two-minute brainstorm.** With your partner, list 3 "
            "arguments *for* and 3 *against* the motion."
        ),
        "input_blocks": [
            ("Debate vocabulary",
             "*motion, proposition, opposition, moderator, point "
             "of order, rebut, concede, argument, evidence, "
             "anecdote, summary.*"),
            ("Debate signposts",
             "**Opening:** *I'd like to argue / I would like to "
             "speak in favour / against …*\n"
             "**Listing:** *Firstly … Secondly … Lastly …*\n"
             "**Counter:** *My opponent claims … / However, … / In "
             "response, …*\n"
             "**Concession:** *I accept that … but …*\n"
             "**Closing:** *Finally / To summarise / In short, "
             "I would urge you to support / oppose this motion.*"),
        ],
        "practise_g": [
            "1. Choose: *opening / counter / closing*: \"I'd like "
            "to argue …\" → ___ ; \"My opponent claims …\" → ___ ; "
            "\"To summarise …\" → ___ .",
            "2. Match: rebut → counter; concede → accept partly. "
            "(T / F)",
        ],
        "practise_m": [
            "3. Build a 4-sentence opening for or against the "
            "motion using 3 signposts.",
        ],
        "answer_g": (
            "1. opening / counter / closing.\n"
            "2. all true."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Class debate.** Two teams of 4 + 1 moderator. Each "
            "speaker delivers a 90-second argument with 4 "
            "signposts. Listening team prepares one specific "
            "rebuttal per speaker. The moderator times strictly."
        ),
        "produce_sample": (
            "*I'd like to speak in favour of the motion. Firstly, "
            "project-based assessment captures skills that a "
            "written test cannot — research, design, presentation. "
            "Secondly, project-based work tends to involve real "
            "audiences, which makes the writing better. My "
            "opponent will claim that projects can be unfair "
            "across groups. I accept that, but it can be "
            "controlled with clear rubrics. Finally, replacing "
            "*one* test per term is moderate. To summarise: a "
            "small change, a real benefit. I urge you to support "
            "the motion.*"
        ),
        "reflect": [
            "I can present a 90-second argument with 4 signposts.",
            "I can rebut one specific point.",
            "I can concede one point gracefully.",
        ],
        "pitfalls": [
            "Reading from a script flatly.",
            "Generic rebuttals (*you're wrong*) — be specific.",
            "Concession without genuine engagement.",
        ],
        "further": [
            "ESU (English-Speaking Union) — student debate clips.",
            "BBC Sounds — *Question Time* extracts.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"I'd like to speak in favour. Firstly, project work "
            "captures skills tests don't. Secondly, real audiences "
            "improve writing. My opponent will claim that fairness "
            "is hard. I accept that, but a clear rubric solves it. "
            "To summarise: small change, real benefit.\"\n\n"
            "1. Stance: ___ . 2. First reason: ___ . 3. Counter "
            "anticipated: ___ . 4. Closing phrase: ___ ."
        ),
        "exam_reading": (
            "Read the sample debate opening above. Answer.\n\n"
            "1. Speaker stance: ___ . 2. Two reasons: ___ . 3. "
            "Concession: ___ . 4. Sign-off: ___ ."
        ),
        "exam_use": (
            "**Insert the right signpost.**\n\n"
            "1. ___ to support the motion.\n"
            "2. ___ , project work is real.\n"
            "3. ___ , my opponent claims fairness is hard.\n"
            "4. ___ , a small change with real benefit."
        ),
        "exam_writing": (
            "Write a 150-word debate speech (for or against any "
            "motion). Use 4 debate signposts."
        ),
        "exam_keys": [
            "**T1.** in favour; project work captures skills tests don't; fairness is hard; *To summarise*.",
            "**T2.** in favour; project skills + real audiences; *I accept that, but a clear rubric solves it*; *I urge you to support the motion*.",
            "**T3.** I'd like / Firstly / However / To summarise.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 12, "slug": "year-review-portfolio", "title": "Year Review: Portfolio",
        "skills": ["writing", "speaking", "language_awareness"],
        "bp": [
            "3.2.1 Soziokulturelles Orientierungswissen / Themen",
            "3.2.3.4 Sprechen – zusammenhängendes monologisches Sprechen",
            "3.2.3.5 Schreiben",
            "3.2.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can compile a Klasse-9 portfolio with 4 representative pieces.",
            "I can write a 200-word reflection on my year.",
            "I can deliver a 2-minute portfolio talk with one quote from my own writing.",
        ],
        "leadin": (
            "Mr. Yilmaz handed out an empty A3 sheet. \"This is "
            "your portfolio,\" he said. \"Pick four pieces from "
            "this year. One you are proud of. One that surprised "
            "you. One that didn't work. One that you would write "
            "differently now.\""
        ),
        "activate": (
            "**Pick-four scan.** Open your folder. Pick four pieces. "
            "Label each: *proud / surprised / didn't work / "
            "would do differently*."
        ),
        "input_blocks": [
            ("Portfolio structure",
             "1. **Cover sheet** (name, year, date, one-line theme).\n"
             "2. **Four pieces** (with one-line label each).\n"
             "3. **Reflection** (200 words: what changed, what "
             "didn't, one moment of progress, one thing for "
             "Klasse 10).\n"
             "4. **Talk** (2 minutes, one quote from your own "
             "writing)."),
            ("Reflection — useful frames",
             "*At the start of Klasse 9 I … / By December I had "
             "started to … / The piece that surprised me was … "
             "because … / The piece that didn't work taught me "
             "that … / If I rewrote one of these now, I would …*"),
        ],
        "practise_g": [
            "1. Build the four labels for your own folder.",
        ],
        "practise_m": [
            "2. Build a 5-line reflection draft.",
        ],
        "answer_g": "Open.",
        "answer_m": "Open.",
        "produce": (
            "**Portfolio + 200-word reflection + 2-minute talk.** "
            "Each student submits the A3 portfolio and delivers a "
            "2-minute portfolio talk to the class. Audience gives "
            "one feedback sentence using *I noticed that …*"
        ),
        "produce_sample": (
            "*At the start of Klasse 9, I wrote in short sentences "
            "that did the same thing twice. By December I had "
            "started to write longer sentences with a turn in the "
            "middle. The piece I am proudest of is the application "
            "letter — the formal register felt strange but I "
            "understood why it was needed by the third draft. "
            "The piece that didn't work was my Canada reflection "
            "— I tried to cover too much. If I rewrote it now, I "
            "would pick one detail and stay with it. The biggest "
            "thing I learned this year is that careful first "
            "drafts save more time than fast ones, and that a "
            "good question is worth ten paragraphs of answer.*"
        ),
        "reflect": [
            "I can compile a 4-piece portfolio.",
            "I can write a 200-word year reflection.",
            "I can deliver a 2-minute portfolio talk.",
        ],
        "pitfalls": [
            "Reading the talk word-for-word.",
            "Generic claims (*I learned a lot*) — give a concrete "
            "example.",
            "Picking only your best four — the *didn't-work* slot "
            "matters.",
        ],
        "further": [
            "BBC Bitesize — *Reflective writing*.",
            "British Council — *Self-evaluation* tips for learners.",
        ],
        "exam_listening": (
            "Listen twice to a portfolio talk.\n\n"
            "> \"At the start of Klasse 9 I wrote short, repetitive "
            "sentences. By December I had started to vary them. "
            "The piece I am proudest of is the application letter. "
            "The piece that didn't work was my Canada reflection. "
            "If I rewrote it now, I would pick one detail.\"\n\n"
            "1. September: ___ . 2. December: ___ . 3. Proud "
            "piece: ___ . 4. Didn't work: ___ ."
        ),
        "exam_reading": (
            "Read the reflection sample above. Answer.\n\n"
            "1. September writing: ___ . 2. December change: "
            "___ . 3. Proud piece + reason: ___ . 4. Lesson: ___ ."
        ),
        "exam_use": (
            "**Mixed grammar review.**\n\n"
            "1. By December I __________ (start) to write better. "
            "(past perfect)\n"
            "2. If I __________ (rewrite) the piece, I __________ "
            "(pick) one detail. (second conditional)\n"
            "3. The piece __________ (write / passive) in March.\n"
            "4. Although I ___ (struggle), I ___ (learn)."
        ),
        "exam_writing": (
            "Write a 200-word year-review reflection. Use 4 "
            "grammar points from the year."
        ),
        "exam_keys": [
            "**T1.** short repetitive sentences; varied sentences; application letter; Canada reflection.",
            "**T2.** short, repetitive; varied sentences with a turn in the middle; application letter — formal register; first drafts save more time than fast ones, a good question is worth ten paragraphs.",
            "**T3.** had started / rewrote-would pick / was written / struggled-learned.",
            "**T4.** Open.",
        ],
    },
]


UNIT_TPL = """---
title: "Unit {n} — {title}"
subtitle: "Track G+M · Klasse 9 · Niveau G/M"
niveau: "G+M"
klassenstufe: 9
track: "gm"
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
**Niveau:** G/M parallel. Klassenarbeit at Niveau M (45 BE).
:::

{{{{< downloads >}}}}

## Learning objectives

{objectives}

## Bildungsplan alignment

{bp_bullets}

(Source: <https://www.bildungsplaene-bw.de/,Lde/LS/BP2016BW/ALLG/SEK1/E1>)

## Lead-in story

{leadin}

## 1. Activate

{activate}

## 2. Input

{input_sections}

## 3. Practise

### Niveau G

{practise_g}

### Niveau M

{practise_m}

::: {{.callout-tip collapse="true" title="Answer key"}}
**G.** {answer_g}

**M.** {answer_m}
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

**Differentiation.** Niveau G: scaffold card with the key
structure. Above Niveau M: extension prompt linking to Klasse 10.
:::

## Common pitfalls

{pitfalls}

## Further reading / listening

{further}
"""

EXAM_BODY_TPL = """::: {{.callout-warning icon=false title="Klassenarbeit — Niveau M (45 minutes)"}}
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

::: {{.callout-tip collapse="true" title="Notenschlüssel (von 45)"}}
| 42–45 | 1 | 36–41 | 2 | 30–35 | 3 |
| 22–29 | 4 | 13–21 | 5 |  0–12 | 6 |
:::
"""

EXAM_WRAP_TPL = """---
title: "Klassenarbeit — Unit {n}: {title}"
subtitle: "Track G+M · Klasse 9 · Niveau M · 45 Minuten"
author: "S. Le Boulanger"
niveau: "M"
klassenstufe: 9
track: "gm"
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

# Klassenarbeit — Unit {n}: {title}

**Track G+M · Klasse 9 · Niveau M · 45 Minuten**

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

    print(f"Wrote {len(UNITS) * 3} files for Track G+M Klasse 9.")


if __name__ == "__main__":
    emit()
