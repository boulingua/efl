"""Batch-emit Track G+M Klasse 10 — all 12 Units.

Klasse 10 voice: transition, work, media, civic English, an
argument-driven undertone. Cast: Sam (returning from Klasse 6),
Maja, plus a young-adult ensemble. Bildungsplan prefix 3.3
(Klasse 10).

Grammar arc consolidates Klasse 9 and adds: third conditional,
present perfect continuous, gerund vs. infinitive after verbs,
defining vs. non-defining relative clauses, formal CV / cover
letter conventions, more advanced reporting.
"""
from __future__ import annotations
import pathlib

REPO = pathlib.Path(__file__).resolve().parent.parent
COURSE = REPO / "track_gm_kl10" / "units"

UNITS = [
    {
        "n": 1, "slug": "transition-after-grade-10",
        "title": "Transition After Grade 10",
        "skills": ["reading", "writing", "language_awareness"],
        "bp": [
            "3.3.1 Soziokulturelles Orientierungswissen / Themen",
            "3.3.3.2 Leseverstehen",
            "3.3.3.5 Schreiben",
            "3.3.3.8 Verfügen über sprachliche Mittel – Grammatik",
        ],
        "objectives": [
            "I can read a short text on post-Klasse-10 paths and identify three options.",
            "I can use the third conditional (*if I had …, I would have …*).",
            "I can write a 150-word reflection on a decision I am facing.",
        ],
        "leadin": (
            "Sam, who is back after a year abroad with his cousins, "
            "is sitting in the Klasse 10 corridor. He is "
            "reconsidering everything. Maja, who is more decisive on "
            "principle, has already chosen an apprenticeship — "
            "though she keeps reading Berufsbildung pamphlets just "
            "in case. Mr. Yilmaz says, *every Klasse 10 corridor "
            "has at least one person re-reading a leaflet they have "
            "already memorised*."
        ),
        "activate": (
            "**Three-path scan.** In your notebook write three "
            "post-Klasse-10 paths you might consider. Mark each as "
            "*serious / curious / not for me*."
        ),
        "input_blocks": [
            ("Vocabulary — transition",
             "*apprenticeship, vocational training (Berufsausbildung), "
             "FOS/BOS (Fachoberschule / Berufsoberschule), gap year, "
             "internship, certificate, application, deadline, "
             "shortlist, interview, on-the-job training, dual "
             "system, employer reference.*"),
            ("Reading — *Three Paths from Maja's Class*",
             "*Three students from Maja's class chose three different "
             "paths. Lukas signed an apprenticeship contract with a "
             "local electrician. Lina applied to the FOS in Stuttgart. "
             "Adam took a gap year and wrote that a year of working "
             "as a forest ranger had changed his sense of time.*"),
            ("Grammar — third conditional",
             "Use **third conditional** for past unreal regrets / "
             "alternatives.\n"
             "Form: *If* + past perfect, *would have* + past "
             "participle.\n\n"
             "- *If I had applied earlier, I would have got a place.*\n"
             "- *If she had not taken the gap year, she wouldn't have "
             "met that mentor.*\n"
             "- *I wouldn't have decided so fast if I had known.*"),
        ],
        "practise_g": [
            "1. Build the third conditional: *(if / I / apply / "
            "earlier / I / get / a place)* → ___ .",
            "2. Match path → action: apprenticeship → contract; FOS "
            "→ application; gap year → trial work.",
        ],
        "practise_m": [
            "3. Build 4 third-conditional sentences about a real or "
            "imagined past decision.",
        ],
        "answer_g": (
            "1. *If I had applied earlier, I would have got a "
            "place.*\n"
            "2. all true."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Reflection, 150 words.** Write about a decision you "
            "are facing or a past one. Use 2 third conditionals + 1 "
            "second conditional + 1 *despite/because of*."
        ),
        "produce_sample": (
            "*If I had been more open in Klasse 8, I would have "
            "applied to more apprenticeships. I wasn't, so I am now "
            "reading every leaflet twice. Despite the pressure of "
            "deciding, I think the right path is the FOS — partly "
            "because I want a longer track, partly because I am "
            "curious. If I were absolutely sure today, I would "
            "probably worry less. But if I had waited another six "
            "months for certainty, I would have missed the deadline. "
            "Imperfect decisions, made on time, are still real "
            "decisions. That is what I am telling myself this "
            "week.*"
        ),
        "reflect": [
            "I can identify three post-Klasse-10 paths.",
            "I can use the third conditional with reason.",
            "I can write a 150-word reflection on a decision.",
        ],
        "pitfalls": [
            "*If I would have applied* → ✗ — German *Konjunktiv II* "
            "trap; English uses *if + past perfect*.",
            "*If I had applied, I would got* → ✗ / *I would have "
            "got* → ✓.",
            "Don't mix third (past unreal) and second (present "
            "unreal) carelessly.",
        ],
        "further": [
            "BBC Bitesize Careers — *Choices after 16*.",
            "Bundesagentur für Arbeit — *BERUFENET* (auf Deutsch, "
            "but accessible).",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"Three students from Maja's class chose three different "
            "paths. Lukas signed an apprenticeship contract. Lina "
            "applied to the FOS. Adam took a gap year and wrote "
            "that working as a forest ranger had changed his sense "
            "of time.\"\n\n"
            "1. Lukas: ___ . 2. Lina: ___ . 3. Adam: ___ . 4. Adam's "
            "discovery: ___ ."
        ),
        "exam_reading": (
            "Read.\n\n"
            "> \"If Maja had applied to the FOS in November, she "
            "would already have a place. She didn't, partly because "
            "her family wanted her to consider the apprenticeship "
            "first. She is now waiting for the second-round response "
            "and reading every leaflet twice.\"\n\n"
            "1. November application: ___ . 2. Reason for delay: "
            "___ . 3. Now waiting for: ___ . 4. Coping mechanism: "
            "___ ."
        ),
        "exam_use": (
            "**Build third conditional or second conditional.**\n\n"
            "1. *(third)* If Maja __________ (apply) earlier, she "
            "__________ (get) a place.\n"
            "2. *(second)* If I __________ (be) more decisive, life "
            "__________ (be) easier.\n"
            "3. *(third)* I __________ (not / regret) the gap year "
            "if I __________ (plan) it better.\n"
            "4. *(third)* They __________ (find) it earlier if they "
            "__________ (look) carefully."
        ),
        "exam_writing": (
            "Write 150 words: a reflection on a real or imagined "
            "decision. Use 2 third conditionals + 1 second "
            "conditional."
        ),
        "exam_keys": [
            "**T1.** apprenticeship contract; applied to FOS; took a gap year; working as a forest ranger changed his sense of time.",
            "**T2.** would already have a place; family wanted her to consider apprenticeship; second-round response; reading every leaflet twice.",
            "**T3.** had applied / would have got; were / would be; wouldn't have regretted / had planned; would have found / had looked.",
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
            "I can read a short job-profile and pick out 6 facts.",
            "I can use the present perfect continuous (*I have been working …*).",
            "I can hold a 3-minute job-interview role-play.",
        ],
        "leadin": (
            "Sam is doing a one-day work-shadowing visit at a small "
            "bakery in the city. He arrives at 5 a.m. The owner, a "
            "woman called Mrs Dahl, is already kneading. \"You're "
            "early,\" she says. \"For me,\" Sam says, \"this is "
            "early. For you, it's mid-morning.\" She smiles. *Welcome,*"
            " she says, *to the only profession where 'mid-morning' "
            "is at five.*"
        ),
        "activate": (
            "**Job-shadow scan.** With your partner, list four jobs "
            "you would actually want to spend a full day shadowing. "
            "Then, the harder one: name a job you would NOT shadow "
            "and one specific reason."
        ),
        "input_blocks": [
            ("Vocabulary — workplace",
             "*shift, line manager, colleague, deadline, "
             "expectation, salary, wage, contract, probation, "
             "feedback, promotion, performance review, "
             "headquarters, branch, freelance, gig work, remote, "
             "hybrid.*"),
            ("Reading — *A Day at the Bakery* (extract)",
             "*Mrs Dahl has been running the bakery for thirty-two "
             "years. She has been kneading dough by hand for most of "
             "that time. Her three apprentices have been showing up "
             "at five every morning, six days a week. \"It is not "
             "romantic,\" she said when Sam asked, \"but it is "
             "honest.\"*"),
            ("Grammar — present perfect continuous",
             "Form: *have/has + been + -ing*.\n"
             "Use: an action that started in the past and is **still "
             "going on** (or recent enough to feel ongoing).\n\n"
             "- *Mrs Dahl **has been running** the bakery for 32 "
             "years.*\n"
             "- *I **have been waiting** for the apprenticeship "
             "letter.*\n"
             "- *They **have been working** since 5 a.m.*\n\n"
             "Compare with present perfect simple:\n"
             "- *I **have written** five applications.* (completed "
             "actions, focus on result)\n"
             "- *I **have been writing** all morning.* (focus on "
             "duration / activity)"),
        ],
        "practise_g": [
            "1. Choose: present perfect simple or continuous: *Mrs "
            "Dahl __________ (run) the bakery for 32 years. I "
            "__________ (write) three applications this morning.*",
            "2. Match: shift → 8-hour block; deadline → due date; "
            "feedback → review.",
        ],
        "practise_m": [
            "3. Build 4 sentences with present perfect continuous "
            "about your real recent activity.",
        ],
        "answer_g": (
            "1. has been running / have written.\n"
            "2. all true."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Job-interview role-play.** Pairs. 3 minutes each "
            "direction. Interviewer asks 5 questions; interviewee "
            "uses 2 present perfect continuous + 2 third "
            "conditional structures."
        ),
        "produce_sample": (
            "*— What experience do you bring?*\n"
            "*— I have been doing weekend shifts at my aunt's café "
            "for two years. If I had started earlier, I would have "
            "more management experience, but I have learned the "
            "basics — shift handover, customer questions, food "
            "safety.*"
        ),
        "reflect": [
            "I can pick out 6 facts in a job-profile.",
            "I can use present perfect continuous correctly.",
            "I can run a 3-minute job-interview role-play.",
        ],
        "pitfalls": [
            "*I am working since 2023* → ✗ / *I have been working "
            "since 2023* → ✓.",
            "Some verbs (*know, believe, have* in *I have a car*) "
            "don't take continuous forms.",
            "*Have* of possession can't be progressive: *I have "
            "been having a car* → ✗.",
        ],
        "further": [
            "BBC Worklife — short articles.",
            "The Guardian — *Working Lives*.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"Mrs Dahl has been running the bakery for 32 years. "
            "She has been kneading dough by hand for most of that "
            "time. Her three apprentices have been showing up at "
            "five every morning, six days a week.\"\n\n"
            "1. Years running: ___ . 2. Method: ___ . 3. "
            "Apprentices: ___ . 4. Days per week: ___ ."
        ),
        "exam_reading": (
            "Read.\n\n"
            "> \"Sam has been visiting different workplaces this "
            "term: a bakery, a small electrician's, a graphic-design "
            "studio. He has been writing one paragraph after each "
            "visit. So far the bakery has surprised him most — "
            "because of the silence at 5 a.m.\"\n\n"
            "1. Activity: ___ . 2. Three workplaces: ___ . 3. "
            "After-visit task: ___ . 4. Most surprising: ___ ."
        ),
        "exam_use": (
            "**Present perfect simple or continuous?**\n\n"
            "1. Mrs Dahl __________ (run) the bakery for 32 years.\n"
            "2. I __________ (write) three applications this "
            "morning.\n"
            "3. They __________ (work) since 5 a.m.\n"
            "4. We __________ (have) two interviews this week."
        ),
        "exam_writing": (
            "Write 150 words about a workplace you would like to "
            "shadow for a day. Use 3 present perfect continuous "
            "structures."
        ),
        "exam_keys": [
            "**T1.** 32, kneading dough by hand, three, six days a week.",
            "**T2.** visiting workplaces; bakery / electrician's / graphic-design studio; one paragraph after each visit; the bakery — silence at 5 a.m.",
            "**T3.** has been running / have written / have been working / have had.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 3, "slug": "digital-lives-at-work",
        "title": "Digital Lives at Work",
        "skills": ["reading", "writing", "language_awareness"],
        "bp": [
            "3.3.1 Soziokulturelles Orientierungswissen / Themen",
            "3.3.3.2 Leseverstehen",
            "3.3.3.5 Schreiben",
            "3.3.3.8 Verfügen über sprachliche Mittel – Grammatik",
            "3.3.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can read a short text on remote / hybrid work and identify the writer's stance.",
            "I can use gerunds and to-infinitives after verbs of preference.",
            "I can write a 150-word opinion piece on remote vs. office work.",
        ],
        "leadin": (
            "Maja's older sister works hybrid: two days at home, "
            "three at the office. She enjoys working from her "
            "kitchen table — the cat, the smell of coffee, no "
            "commute. She also misses being able to walk to a "
            "colleague's desk and ask a small question. Both things "
            "are true at the same time, which is, Maja thinks, what "
            "*hybrid* really means."
        ),
        "activate": (
            "**Two-column scan.** Board: *Remote / In-office*. Class "
            "fills five honest pros under each."
        ),
        "input_blocks": [
            ("Vocabulary — digital workplace",
             "*remote work, hybrid, on-site, video call, "
             "asynchronous, synchronous, time zone, work-life "
             "balance, digital fatigue, coworking space, freelance, "
             "team channel, deliverable, milestone.*"),
            ("Reading — *Hybrid, Honestly*",
             "*Many workers say they enjoy working from home for "
             "two reasons: no commute and quieter focus. Many also "
             "admit that they miss bumping into colleagues. The "
             "common compromise — hybrid — gets defended weakly. "
             "Most people prefer hybrid because it minimises the "
             "downsides of both options, not because it maximises "
             "either.*"),
            ("Grammar — gerund vs. to-infinitive",
             "After **enjoy, miss, admit, finish, mind, suggest, "
             "avoid, recommend, can't help**: gerund (-ing).\n"
             "- *I enjoy working from home.*\n"
             "- *They miss bumping into colleagues.*\n\n"
             "After **want, plan, decide, choose, hope, refuse, "
             "agree, manage, learn**: to-infinitive.\n"
             "- *They chose to work hybrid.*\n"
             "- *He decided to leave the office at 5.*\n\n"
             "After **like, love, hate, prefer, start, begin, "
             "continue**: both forms with very small meaning shift."),
        ],
        "practise_g": [
            "1. Choose: gerund or to-infinitive: *I enjoy* "
            "__________ (work) from home. *I plan* __________ "
            "(apply) for a remote job.",
            "2. Match: enjoy → -ing; want → to-infinitive; admit "
            "→ -ing.",
        ],
        "practise_m": [
            "3. Build 5 sentences using 5 different verbs that take "
            "gerund vs. to-infinitive.",
        ],
        "answer_g": (
            "1. working / to apply.\n"
            "2. all true."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Opinion piece, 150 words.** *Should young workers "
            "look for hybrid jobs?* Take a position. Use 2 "
            "gerunds + 2 to-infinitives + 1 *despite/because of*."
        ),
        "produce_sample": (
            "*Young workers should consider hybrid roles, but not "
            "for the obvious reasons. They should choose to look at "
            "hybrid because it forces a small discipline: the need "
            "to plan working from home so it doesn't become "
            "lonely, and the need to plan office days so they aren't "
            "purely social. Despite the loud debate online, hybrid "
            "is rarely either heaven or hell. Most workers admit "
            "missing certain things on both sides. I enjoy working "
            "alone for long blocks; I also like to overhear ideas "
            "I wouldn't have asked about. I plan to look for a "
            "hybrid junior role for my first year of work, then "
            "decide based on what I actually feel — not on what the "
            "internet thinks I should feel.*"
        ),
        "reflect": [
            "I can read a remote-work text and find the stance.",
            "I can choose gerund or to-infinitive after a verb.",
            "I can write a 150-word opinion piece on a workplace "
            "topic.",
        ],
        "pitfalls": [
            "*I enjoy to work* → ✗ / *I enjoy working* → ✓.",
            "*I want working* → ✗ / *I want to work* → ✓.",
            "*I miss to play football* → ✗ / *I miss playing "
            "football* → ✓.",
        ],
        "further": [
            "BBC Worklife — *The future of remote work*.",
            "The Atlantic — accessible essays on the workplace.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"Many workers enjoy working from home because of the "
            "quiet. Most also admit missing the bump-into "
            "conversations. Hybrid wins as a weak compromise — "
            "minimising the downsides rather than maximising the "
            "upsides.\"\n\n"
            "1. Pro of remote: ___ . 2. Con: ___ . 3. Hybrid as: "
            "___ . 4. Why: ___ ."
        ),
        "exam_reading": (
            "Read the *Hybrid, Honestly* extract above.\n\n"
            "1. Two reasons workers like remote: ___ . 2. What they "
            "miss: ___ . 3. Hybrid is defended: ___ . 4. Why most "
            "prefer it: ___ ."
        ),
        "exam_use": (
            "**Gerund or to-infinitive?**\n\n"
            "1. I enjoy __________ (work) from home.\n"
            "2. They plan __________ (apply) for a remote role.\n"
            "3. He admitted __________ (miss) his colleagues.\n"
            "4. We decided __________ (choose) the hybrid option."
        ),
        "exam_writing": (
            "Write 150 words: an opinion piece on remote vs. "
            "office work. Use 2 gerunds + 2 to-infinitives."
        ),
        "exam_keys": [
            "**T1.** quiet; bump-into conversations; weak compromise; minimises downsides.",
            "**T2.** no commute / quieter focus; bumping into colleagues; weakly; it minimises the downsides of both options.",
            "**T3.** working / to apply / missing / to choose.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 4, "slug": "australia-now",
        "title": "Australia Now",
        "skills": ["reading", "listening", "intercultural"],
        "bp": [
            "3.3.1 Soziokulturelles Orientierungswissen / Themen",
            "3.3.2 Interkulturelle kommunikative Kompetenz",
            "3.3.3.1 Hör-/Hörsehverstehen",
            "3.3.3.2 Leseverstehen",
            "3.3.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can read a short article on contemporary Australian society and identify two cultural anchors.",
            "I can recognise Australian English vocabulary differences.",
            "I can write a 150-word region portrait that goes past surface stereotypes.",
        ],
        "leadin": (
            "Maja's older cousin moved to Brisbane two years ago. "
            "Her postcards have stopped pretending. They no longer "
            "say *the weather is brilliant*. They now say things "
            "like *I have learned to wear sunscreen as a religion* "
            "and *the heat is not a season here, it is a relative*. "
            "Maja keeps the postcards in her desk drawer."
        ),
        "activate": (
            "**Three-fact scan.** With your partner, write three "
            "facts about contemporary Australia (not stereotypes). "
            "Pool with another pair."
        ),
        "input_blocks": [
            ("Reading — *Brisbane Postcards*",
             "*Australia is more urban than its myth. About 86 % of "
             "Australians live in cities. Multiculturalism is real "
             "and complicated — Brisbane is home to large Vietnamese "
             "and Lebanese communities, and First Nations languages "
             "are taught in some primary schools. The bushfire "
             "season has lengthened over the past two decades. "
             "Sunscreen is not a luxury; it is a habit closer to "
             "brushing teeth.*"),
            ("Vocabulary — Australian English",
             "*BrE / AmE → AusE often:* arvo (afternoon), brekkie "
             "(breakfast), barbie (BBQ), servo (petrol station), "
             "bushie (bush dweller), maccas (McDonald's), ute "
             "(pickup truck), arvo tea (afternoon snack).\n\n"
             "Common terms: *fair dinkum* (genuine), *no worries* "
             "(it's fine), *mate* (friend, but watch tone)."),
        ],
        "practise_g": [
            "1. Match AusE → standard: arvo, brekkie, barbie, servo "
            "→ ?",
            "2. T or F from the reading: 86 % live in cities, "
            "Vietnamese community in Brisbane, sunscreen optional.",
        ],
        "practise_m": [
            "3. Write 4 sentences about contemporary Australia "
            "using 2 AusE words and 2 facts from the text.",
        ],
        "answer_g": (
            "1. afternoon / breakfast / BBQ / petrol station.\n"
            "2. T, T, F (sunscreen is a habit, not optional)."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Region portrait, 150 words.** Write about "
            "contemporary Australia going past stereotypes. Use 1 "
            "AusE word + 2 specific facts."
        ),
        "produce_sample": (
            "*Australia is much more urban than its myth. About 86 "
            "% of Australians live in cities, and Brisbane — where "
            "my cousin lives — is home to large Vietnamese and "
            "Lebanese communities, plus a growing First Nations "
            "language presence in some primary schools. The bushfire "
            "season has lengthened over the past two decades. "
            "Sunscreen is not a holiday luxury but a daily habit, "
            "closer to brushing teeth than to skincare. People "
            "still call afternoon *arvo* and breakfast *brekkie* — "
            "those words are real, not tourist-brochure inventions. "
            "What surprised me most, when I read my cousin's "
            "postcards, was that the heat is described as a "
            "relative — annoying, present, sometimes funny, never "
            "going away.*"
        ),
        "reflect": [
            "I can identify two cultural anchors in a contemporary Australian article.",
            "I can recognise 5 AusE words.",
            "I can write a 150-word region portrait past stereotypes.",
        ],
        "pitfalls": [
            "Stereotype check: *koalas + kangaroos + outback* is "
            "thin.",
            "First Nations: capital N. Not *Aborigines* in writing "
            "(prefer *First Nations / Aboriginal and Torres Strait "
            "Islander peoples*).",
            "*Australia is dry* — true on average, but Brisbane is "
            "humid.",
        ],
        "further": [
            "ABC Australia — short news articles.",
            "Australian Bureau of Statistics — accessible "
            "factsheets.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"About 86 % of Australians live in cities. Brisbane "
            "is home to large Vietnamese and Lebanese communities. "
            "First Nations languages are taught in some primary "
            "schools. The bushfire season has lengthened.\"\n\n"
            "1. Urban %: ___ . 2. Two communities: ___ . 3. School "
            "languages: ___ . 4. Climate trend: ___ ."
        ),
        "exam_reading": (
            "Read the *Brisbane Postcards* extract.\n\n"
            "1. % urban: ___ . 2. Two cultural communities in "
            "Brisbane: ___ . 3. Trend: ___ . 4. Sunscreen role: "
            "___ ."
        ),
        "exam_use": (
            "**AusE → standard.**\n\n"
            "1. arvo → ___ ; 2. brekkie → ___ ; 3. barbie → ___ ; "
            "4. servo → ___ ."
        ),
        "exam_writing": (
            "Write 150 words on contemporary Australia past "
            "stereotypes. Use 1 AusE word + 2 specific facts."
        ),
        "exam_keys": [
            "**T1.** 86 %; Vietnamese and Lebanese; First Nations languages; bushfire season has lengthened.",
            "**T2.** 86 %; Vietnamese / Lebanese; bushfire season has lengthened over two decades; sunscreen is a daily habit (not a luxury).",
            "**T3.** afternoon / breakfast / BBQ / petrol station.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 5, "slug": "media-and-truth",
        "title": "Media and Truth",
        "skills": ["reading", "writing", "language_awareness"],
        "bp": [
            "3.3.1 Soziokulturelles Orientierungswissen / Themen",
            "3.3.3.2 Leseverstehen",
            "3.3.3.5 Schreiben",
            "3.3.3.7 Verfügen über sprachliche Mittel – Wortschatz",
            "3.3.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can read a short text and identify three signs of misinformation.",
            "I can use cautious-claim language (*it appears that, evidence suggests, critics argue that*).",
            "I can write a 180-word media-literacy review.",
        ],
        "leadin": (
            "Sam's class made a *Five-Minute Fact-Check* board on the "
            "wall. Each Friday, every student pinned one viral claim "
            "to the board, with three columns: *source / evidence / "
            "what would change my mind*. By March, the wall was full. "
            "Mr. Yilmaz did not say *I told you so*. He just looked at "
            "the wall sideways and smiled."
        ),
        "activate": (
            "**Headline scan.** Three real-looking headlines on the "
            "slide. Mark each: *check / probably true / probably "
            "wrong*."
        ),
        "input_blocks": [
            ("Reading — *Five-Minute Fact-Check*",
             "*Most viral claims feel true because they fit a "
             "pattern we already believe. The fact-checker's job is "
             "small but stubborn: ask three questions. Where is "
             "this from? What is the actual evidence? What would "
             "change my mind? If a claim cannot survive these "
             "questions, it does not belong in your shareable "
             "list.*"),
            ("Vocabulary — media literacy",
             "*verify, source, primary source, secondary source, "
             "fact-check, peer-reviewed, citation, anecdote, "
             "correlation vs. causation, statistical sample, bias, "
             "framing, context, viral, debunked, retracted.*"),
            ("Cautious-claim language",
             "*It appears that … / Evidence suggests that … / "
             "According to (named source) … / Critics argue that "
             "… / This is contested / Studies indicate that … / "
             "There is some evidence that …*"),
        ],
        "practise_g": [
            "1. Match: peer-reviewed → expert-checked; primary "
            "source → original; debunked → shown false.",
            "2. Choose cautious phrase: *(my own claim)* → ___ ; "
            "*(another expert's claim)* → ___ .",
        ],
        "practise_m": [
            "3. Build 4 cautious-claim sentences from a real or "
            "imagined news topic.",
        ],
        "answer_g": (
            "1. all true.\n"
            "2. *In my view / Studies indicate that.*"
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Media-literacy review, 180 words.** Pick a viral "
            "claim. Apply the three-question check. Use 4 "
            "cautious-claim phrases."
        ),
        "produce_sample": (
            "*A widely-shared post claims that one cup of green "
            "tea per day reduces the risk of dementia by 40 %. The "
            "post links to a science-sounding website. According "
            "to the linked website, the claim is based on a 2019 "
            "study. It appears, however, that the study sampled "
            "only 70 participants over six months — too small to "
            "support a 40 % claim. There is some evidence that "
            "green-tea polyphenols affect inflammation, but this "
            "is contested. Critics argue that the study has not "
            "been replicated. What would change my mind: a larger, "
            "peer-reviewed study with at least 1,000 participants "
            "over five years, ideally a meta-analysis. The original "
            "post itself shows two warning signs: the round number "
            "(40 %) and the absence of a named researcher. I would "
            "share it only after a serious follow-up.*"
        ),
        "reflect": [
            "I can identify 3 signs of misinformation.",
            "I can use cautious-claim language.",
            "I can write a 180-word media-literacy review.",
        ],
        "pitfalls": [
            "*Studies say* (vague) — better: *A 2019 study by … "
            "indicates that …*.",
            "*Most people think* without source — anecdote, not "
            "evidence.",
            "Round numbers (40 %, 90 %) → red flag for "
            "approximated or invented data.",
        ],
        "further": [
            "BBC Reality Check.",
            "FullFact.org (UK).",
            "Snopes.com — wide range of fact-checks.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"The post claims that one cup of green tea per day "
            "reduces dementia risk by 40 %. The study sampled only "
            "70 participants over six months. Critics argue the "
            "study has not been replicated. The post itself uses a "
            "round number and no named researcher.\"\n\n"
            "1. Claim: ___ . 2. Sample: ___ . 3. Critics' point: "
            "___ . 4. Two warning signs: ___ ."
        ),
        "exam_reading": (
            "Read the *Five-Minute Fact-Check* extract above.\n\n"
            "1. Three questions: ___ . 2. What viral claims "
            "exploit: ___ . 3. Fact-checker job: ___ . 4. "
            "Conclusion: ___ ."
        ),
        "exam_use": (
            "**Insert cautious-claim language.**\n\n"
            "1. ___ that 86 % of Australians live in cities.\n"
            "2. ___ that hybrid work reduces stress.\n"
            "3. ___ , the study has not been replicated.\n"
            "4. ___ argue that the data is incomplete."
        ),
        "exam_writing": (
            "Write 180 words: a media-literacy review of a viral "
            "claim. Use 4 cautious-claim phrases."
        ),
        "exam_keys": [
            "**T1.** green tea reduces dementia by 40 %; 70 participants over 6 months; not replicated; round number + no named researcher.",
            "**T2.** Where is this from? / What is the actual evidence? / What would change my mind?; pattern we already believe; small but stubborn — ask three questions; if a claim cannot survive these questions, it does not belong in your shareable list.",
            "**T3.** It appears / Evidence suggests / However / Critics.",
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
            "I can read a contemporary short story and identify protagonist, conflict, theme, and one stylistic move.",
            "I can use defining vs. non-defining relative clauses.",
            "I can write a 200-word literary response.",
        ],
        "leadin": (
            "The class read *The Note Under the Door* by an "
            "imagined contemporary author. Six pages. One narrator. "
            "One small noise that turns out not to be small. Maja "
            "wrote in the margin of her copy: *the house is a "
            "character*. Mr. Yilmaz read the margin note before he "
            "read the essay."
        ),
        "activate": (
            "**Story shape sketch.** With your partner, draw the "
            "shape of *The Note Under the Door* on a single line: "
            "*calm → noise → discovery → quiet again*. Add three "
            "specific words from the text."
        ),
        "input_blocks": [
            ("Reading — *The Note Under the Door* (extract)",
             "*The note, which someone had pushed under the door at "
             "3 a.m., was written in pencil on a small piece of card. "
             "The handwriting, which I did not recognise, looked "
             "tired. The card said: 'I'm sorry about the cat.' I "
             "read it three times. We do not have a cat. The cat, "
             "I realised, was someone else's idea of an apology — "
             "delivered by accident to my door, the kind of "
             "delivery that explains nothing but rearranges the "
             "room.*"),
            ("Grammar — defining vs. non-defining relative clauses",
             "**Defining** (no commas) — identifies which one:\n"
             "- *The note that someone pushed under the door at 3 "
             "a.m. was written in pencil.* (which note? — defines)\n\n"
             "**Non-defining** (with commas) — adds extra info:\n"
             "- *The note, which had been pushed under the door at "
             "3 a.m., was written in pencil.* (we already know "
             "which note)\n\n"
             "*That* is fine in defining clauses; in non-defining "
             "clauses use *which / who*."),
        ],
        "practise_g": [
            "1. Defining or non-defining? *The note (?) someone "
            "pushed under the door at 3 a.m. was written in "
            "pencil.* (which one?)",
            "2. Insert commas as needed: *The handwriting which I "
            "did not recognise looked tired.*",
        ],
        "practise_m": [
            "3. Build 3 sentences with defining + 2 with "
            "non-defining relative clauses.",
        ],
        "answer_g": (
            "1. *that someone pushed* (defining, no commas).\n"
            "2. *The handwriting, which I did not recognise, "
            "looked tired.* (non-defining, commas)."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Literary response, 200 words.** Read the extract. "
            "Answer: *Who is the narrator? What is the conflict? "
            "What is the theme? Which one detail is doing the most "
            "work?* Use 2 defining + 1 non-defining relative "
            "clause."
        ),
        "produce_sample": (
            "*The note, which someone had pushed under the door at "
            "3 a.m., does the most work in this short text — not "
            "because of what it says, but because of the small "
            "mismatch between sender and receiver. The narrator, "
            "whose voice is dry and careful, has no cat to apologise "
            "for. The misdelivered note becomes, in three readings, "
            "a different object each time: a scrap of paper, a "
            "stranger's regret, a domestic puzzle that won't "
            "rearrange itself. The conflict is not the noise at 3 "
            "a.m. — it is the impossibility of returning the "
            "apology to its real owner. The theme, I think, is "
            "the daily smallness of accidental contact in city "
            "life: we receive each other's lost messages all the "
            "time. The author's stylistic move is the line *the "
            "kind of delivery that explains nothing but rearranges "
            "the room.* That is the sentence that makes the "
            "whole story click into place. Without it, the note is "
            "a curiosity. With it, the note is a gentle invasion.*"
        ),
        "reflect": [
            "I can identify protagonist, conflict, theme, one stylistic move.",
            "I can use defining and non-defining relative clauses.",
            "I can write a 200-word literary response.",
        ],
        "pitfalls": [
            "Comma misuse in defining clauses: *The note, that he "
            "pushed under the door,* → ✗.",
            "*Who* for things or *which* for people → ✗.",
            "Don't summarise plot — analyse moves.",
        ],
        "further": [
            "The New Yorker — short fiction archive.",
            "BBC Radio 4 — *Short Story* podcasts.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"The note, which someone had pushed under the door "
            "at 3 a.m., was written in pencil on a small piece of "
            "card. The card said: 'I'm sorry about the cat.' We do "
            "not have a cat.\"\n\n"
            "1. When pushed: ___ . 2. Material: ___ . 3. Apology "
            "for: ___ . 4. Twist: ___ ."
        ),
        "exam_reading": (
            "Read the *Note Under the Door* extract above.\n\n"
            "1. The note's path: ___ . 2. Narrator's reaction "
            "(times read): ___ . 3. Realisation: ___ . 4. The "
            "story's key sentence: ___ ."
        ),
        "exam_use": (
            "**Insert correct relative pronoun + commas.**\n\n"
            "1. The note ___ someone pushed under the door at 3 "
            "a.m. was written in pencil. (defining)\n"
            "2. The note ___ had been pushed under the door at 3 "
            "a.m. was written in pencil. (non-defining)\n"
            "3. The handwriting ___ I did not recognise looked "
            "tired. (non-defining)\n"
            "4. The cat ___ apology this is meant for is not ours. "
            "(defining)"
        ),
        "exam_writing": (
            "Write 200 words: a literary response to the extract. "
            "Use 2 defining + 1 non-defining relative clause."
        ),
        "exam_keys": [
            "**T1.** 3 a.m.; pencil on small card; the cat; speaker has no cat.",
            "**T2.** pushed under the door at 3 a.m. by someone; three times; the apology was for someone else's cat, accidentally delivered; *the kind of delivery that explains nothing but rearranges the room*.",
            "**T3.** 1. that / which (defining, no commas); 2. , which (non-defining, commas); 3. , which (non-defining); 4. whose (defining).",
            "**T4.** Open.",
        ],
    },
    {
        "n": 7, "slug": "mediation-workplace-text",
        "title": "Mediation: A Workplace Text",
        "skills": ["mediation", "writing", "language_awareness"],
        "bp": [
            "3.3.1 Soziokulturelles Orientierungswissen / Themen",
            "3.3.3.5 Schreiben",
            "3.3.3.6 Sprachmittlung",
            "3.3.3.7 Verfügen über sprachliche Mittel – Wortschatz",
        ],
        "objectives": [
            "I can mediate a German workplace policy text into 6–8 English sentences for a colleague.",
            "I can preserve modal nuance (*sollten* → *should*; *müssen* → *must*) and adjust register.",
            "I can use 7 reporting verbs.",
        ],
        "leadin": (
            "Sam's mother forwarded a German policy update from her "
            "company. Sam's English-speaking cousin in Toronto, who "
            "is starting a similar job, asked for a quick gist. Sam "
            "rewrote it in seven sentences. He kept the modals. He "
            "dropped the company-letterhead language."
        ),
        "activate": (
            "**Drop or keep?** Slide shows a 100-word German policy. "
            "Mark each sentence as *essential / paraphrase / drop* "
            "for a colleague abroad."
        ),
        "input_blocks": [
            ("Source — *German workplace policy (excerpt)*",
             "*Sehr geehrte Mitarbeiterinnen und Mitarbeiter, ab "
             "dem 1. Juli gilt eine neue Regelung zum mobilen "
             "Arbeiten. Mitarbeitende dürfen bis zu drei Tage pro "
             "Woche im Homeoffice arbeiten, sofern dies vorher mit "
             "der Führungskraft abgestimmt wurde. Die Anwesenheit "
             "an einem festen Bürotag pro Woche wird vorausgesetzt. "
             "Bei Verstößen behält sich die Geschäftsleitung "
             "Maßnahmen vor.*"),
            ("Mediation — modal mapping",
             "German *dürfen* → English *may / are allowed to / "
             "can*.\n"
             "German *müssen* → English *must / have to*.\n"
             "German *sollen / sollten* → English *should*.\n"
             "Keep the modal nuance — *should* and *must* are not "
             "interchangeable in English."),
            ("Reporting verbs (workplace register)",
             "*to announce, to require, to permit, to expect, to "
             "warn, to advise, to clarify, to confirm, to "
             "stipulate, to reserve the right to.*"),
        ],
        "practise_g": [
            "1. Match German modal → English: dürfen → ?, müssen → "
            "?, sollten → ?",
            "2. Choose: *announce / warn / clarify / require* — "
            "Management __________ a new rule. The company "
            "__________ that breaches will be addressed.",
        ],
        "practise_m": [
            "3. Build a 6-sentence English mediation of the source "
            "above.",
        ],
        "answer_g": (
            "1. may / must / should.\n"
            "2. announces / warns."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Mediation, 7 sentences.** Read the German source "
            "above. Write 7 English sentences for a colleague "
            "abroad. Keep modal nuance + use 4 reporting verbs."
        ),
        "produce_sample": (
            "*Hi Jordan, here's the gist of the new policy. The "
            "company has announced a new home-office rule starting "
            "1 July. Employees may work from home up to three days "
            "a week, provided that this is agreed in advance with "
            "their line manager. Attendance at one fixed office "
            "day per week is required. Management warns that "
            "breaches may result in measures, though the policy "
            "doesn't say what those are. The tone is cautious — "
            "they confirm that the rule is conditional on prior "
            "approval. In short: hybrid is allowed, but not "
            "automatic.*"
        ),
        "reflect": [
            "I can mediate a German policy into 7 English sentences.",
            "I can preserve modal nuance.",
            "I can use 4 reporting verbs.",
        ],
        "pitfalls": [
            "*müssen* mistranslated as *should* (= weaker). "
            "*müssen* = *must / have to*.",
            "*dürfen* mistranslated as *should*. *dürfen* = *may "
            "/ are allowed to*.",
            "Carrying over German letterhead salutations (*Sehr "
            "geehrte …*) into a peer-message — drop them.",
        ],
        "further": [
            "Goethe-Institut — Sprachmittlungs-Beispielaufgaben.",
            "Cambridge Business English — accessible policy-text "
            "samples.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"Ab dem 1. Juli gilt eine neue Regelung. Mitarbeitende "
            "dürfen bis zu drei Tage pro Woche im Homeoffice arbeiten, "
            "sofern dies abgestimmt wurde. Ein fester Bürotag pro "
            "Woche wird vorausgesetzt.\"\n\n"
            "1. Date: ___ . 2. Permission: ___ . 3. Condition: ___ . "
            "4. Required: ___ ."
        ),
        "exam_reading": (
            "Read the German source above.\n\n"
            "1. New policy starts: ___ . 2. Maximum home-office "
            "days: ___ . 3. Pre-condition: ___ . 4. Sanctions: "
            "___ ."
        ),
        "exam_use": (
            "**Modal mapping.**\n\n"
            "1. Mitarbeitende dürfen … → Employees __________ …\n"
            "2. Ein Bürotag wird vorausgesetzt → One office day "
            "is __________ .\n"
            "3. Bei Verstößen … → In case of breaches, management "
            "__________ measures.\n"
            "4. Sollte abgestimmt werden → It __________ be "
            "agreed."
        ),
        "exam_writing": (
            "Mediate: write 7 English sentences from the source "
            "for a colleague abroad. Use 4 reporting verbs."
        ),
        "exam_keys": [
            "**T1.** 1 July; up to 3 days WFH; agreed with line manager; one office day per week.",
            "**T2.** 1 July; 3 days; prior agreement with line manager; possible measures (unspecified).",
            "**T3.** may / are allowed to; required / expected; reserves the right to take / warns about; should.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 8, "slug": "civic-english",
        "title": "Civic English: Rights and Voices",
        "skills": ["reading", "speaking", "language_awareness"],
        "bp": [
            "3.3.1 Soziokulturelles Orientierungswissen / Themen",
            "3.3.2 Interkulturelle kommunikative Kompetenz",
            "3.3.3.2 Leseverstehen",
            "3.3.3.3 Sprechen – an Gesprächen teilnehmen",
            "3.3.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can read a short civic text and identify a stated right and a stated duty.",
            "I can use *be entitled to*, *be required to*, *be expected to* in formal contexts.",
            "I can hold a 3-minute civic-question conversation in formal English.",
        ],
        "leadin": (
            "Maja's class read a one-page summary of the UN "
            "Convention on the Rights of the Child. They argued for "
            "twenty minutes about Article 12 — *every child has the "
            "right to be heard in matters affecting them.* Half the "
            "class said *that's already true*. The other half said "
            "*that's poorly enforced.* Mr. Yilmaz said: *both can "
            "be true*."
        ),
        "activate": (
            "**Right vs. duty scan.** With your partner, write 3 "
            "rights you have as a Klasse-10 student and 3 duties. "
            "Compare and discuss overlaps."
        ),
        "input_blocks": [
            ("Reading — *Article 12, paraphrased*",
             "*Every child has the right to express an opinion in "
             "matters affecting them, and that opinion is to be "
             "given due weight in accordance with the child's age "
             "and maturity. This right does not mean that children "
             "decide; it means that adults are required to listen "
             "and to consider. The article is one of the most "
             "frequently cited and one of the most unevenly "
             "enforced in the convention.*"),
            ("Vocabulary — civic English",
             "*right, duty, obligation, citizen, resident, "
             "constitution, convention, treaty, ratify, enforce, "
             "entitled to, required to, expected to, consult, "
             "represent, advocate, petition, due process.*"),
            ("Grammar — formal entitlement / duty phrases",
             "- *Children **are entitled to** express their views.*\n"
             "- *Adults **are required to** consider those views.*\n"
             "- *Schools **are expected to** consult students on "
             "rules that affect them.*\n"
             "- Negative: ***are not obliged to** decide based on "
             "those views.*"),
        ],
        "practise_g": [
            "1. Choose: *entitled / required / expected* — Children "
            "are __________ to express their views. Adults are "
            "__________ to listen.",
            "2. Match: right → entitlement; duty → obligation; "
            "ratify → formally accept.",
        ],
        "practise_m": [
            "3. Build 4 civic-English sentences using *entitled / "
            "required / expected* about a school or local civic "
            "topic.",
        ],
        "answer_g": (
            "1. entitled / required.\n"
            "2. all true."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Pair speaking — *Article 12 in our school*.** 3 min "
            "each direction. Question: *How is the right to be "
            "heard handled in our school?* Use 4 formal civic "
            "phrases + 1 cautious-claim phrase."
        ),
        "produce_sample": (
            "*— Students are entitled to express their views on "
            "rules that affect them. In our school, this is partly "
            "handled through the student representatives. According "
            "to the head pupil, however, only some rules are "
            "actually consulted on. It appears that the system "
            "works best for visible issues like break-time use, and "
            "less well for less visible ones like marking practice. "
            "Adults are required to consider student views, but "
            "they are not obliged to act on them.*"
        ),
        "reflect": [
            "I can identify a right and a duty in a civic text.",
            "I can use formal entitlement / duty phrases.",
            "I can hold a 3-minute civic-question conversation in "
            "formal English.",
        ],
        "pitfalls": [
            "*are entitled to express themselves* (formal) vs. *can "
            "say what they think* (everyday) — match the register.",
            "*ratify* ≠ *sign* — ratification is a separate "
            "domestic step.",
            "Civic note: *rights* can exist on paper without being "
            "*enforced* — keep that distinction.",
        ],
        "further": [
            "UNICEF — child-friendly version of the CRC.",
            "Council of Europe — accessible articles on Convention "
            "rights.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"Article 12 says that every child is entitled to "
            "express an opinion in matters affecting them. Adults "
            "are required to give that opinion due weight, "
            "considering age and maturity. The right does not mean "
            "children decide. The article is among the most "
            "frequently cited and the most unevenly enforced.\"\n\n"
            "1. Right: ___ . 2. Duty: ___ . 3. What it does NOT "
            "mean: ___ . 4. Status: ___ ."
        ),
        "exam_reading": (
            "Read the *Article 12, paraphrased* extract above.\n\n"
            "1. Right: ___ . 2. Adults' duty: ___ . 3. Limit on "
            "the right: ___ . 4. Reality of enforcement: ___ ."
        ),
        "exam_use": (
            "**Insert *entitled / required / expected*.**\n\n"
            "1. Children are ___ to express their views.\n"
            "2. Adults are ___ to consider those views.\n"
            "3. Schools are ___ to consult on rules.\n"
            "4. Adults are not ___ to follow the children's "
            "decision."
        ),
        "exam_writing": (
            "Write 180 words: a civic-English commentary on one "
            "right or one rule in your school. Use 4 formal "
            "phrases."
        ),
        "exam_keys": [
            "**T1.** every child entitled to express opinion; adults required to give due weight; not children deciding; most cited / most unevenly enforced.",
            "**T2.** express opinions in matters affecting them; consider those opinions with due weight; consideration based on age and maturity, children don't decide; one of the most cited and unevenly enforced.",
            "**T3.** entitled / required / expected / obliged.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 9, "slug": "youth-and-the-future",
        "title": "Youth and the Future",
        "skills": ["reading", "writing", "intercultural"],
        "bp": [
            "3.3.1 Soziokulturelles Orientierungswissen / Themen",
            "3.3.2 Interkulturelle kommunikative Kompetenz",
            "3.3.3.2 Leseverstehen",
            "3.3.3.5 Schreiben",
            "3.3.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can read a short text on a youth-led initiative and identify the main claim and one piece of evidence.",
            "I can use future perfect (*by 2030, I will have …*) and future continuous (*next year I will be …*).",
            "I can write a 200-word reflection on a youth-led future scenario.",
        ],
        "leadin": (
            "Sam read about a 17-year-old in Glasgow who has been "
            "running a community garden on a derelict industrial "
            "site for two years. By 2030, the project will have "
            "trained over 200 young volunteers. Sam's first "
            "reaction was *that's intimidating*. His second reaction "
            "was *that's encouraging*. His third reaction, on "
            "reflection, was *both, depending on the day*."
        ),
        "activate": (
            "**Future-self scan.** Write three lines: *By 2030 I "
            "will have …*; *In 2030 I will be …*; *I hope I will "
            "still be …*"
        ),
        "input_blocks": [
            ("Reading — *The Glasgow Garden Project*",
             "*The Glasgow Garden Project began in 2024 on a half-"
             "acre derelict industrial site. By 2030, the project "
             "will have trained over 200 young volunteers in "
             "small-scale urban food growing. Next year alone, the "
             "team will be running weekend workshops for primary-"
             "school groups. The founder, who started the project "
             "at 15, says the most useful skill she has gained is "
             "what she calls *small repeated public asking* — the "
             "willingness to keep asking adults for things they "
             "could easily say no to.*"),
            ("Grammar — future perfect + future continuous",
             "**Future perfect** (*will have* + past participle) — "
             "actions completed by a future time:\n"
             "- *By 2030, the project will have trained 200 "
             "volunteers.*\n"
             "- *I will have finished my apprenticeship by 2028.*\n\n"
             "**Future continuous** (*will be* + -ing) — actions "
             "in progress at a future time:\n"
             "- *Next year the team will be running workshops.*\n"
             "- *In 2030 I will be living in another city, "
             "probably.*"),
        ],
        "practise_g": [
            "1. Build the future perfect: *(by 2030 / I / finish / "
            "school)* → ___ .",
            "2. Future continuous: *(at 5 p.m. tomorrow / I / "
            "study)* → ___ .",
        ],
        "practise_m": [
            "3. Build 4 sentences mixing future perfect and future "
            "continuous about your decade ahead.",
        ],
        "answer_g": (
            "1. *By 2030 I will have finished school.*\n"
            "2. *At 5 p.m. tomorrow I will be studying.*"
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Reflection, 200 words.** Write about a youth-led "
            "initiative you find encouraging or intimidating. Use "
            "3 future perfect + 2 future continuous + 1 cautious-"
            "claim phrase."
        ),
        "produce_sample": (
            "*The Glasgow Garden Project, which began in 2024 on a "
            "derelict industrial site, will have trained over 200 "
            "young volunteers by 2030. Next year alone, the team "
            "will be running weekend workshops for primary-school "
            "groups. The most striking thing about the founder, who "
            "started at 15, is what she calls 'small repeated "
            "public asking'. According to her, the actual skill of "
            "youth leadership is not vision; it is patience with "
            "the awkwardness of asking adults for things they "
            "could easily refuse. By the time I am 23, I will have "
            "either started something small or watched the chance "
            "pass. By 2030, I hope I will be doing something — "
            "even on a half-acre, even badly at first. The project "
            "has shown me that the unit of change is not the grand "
            "speech but the small request, repeated until someone "
            "says yes.*"
        ),
        "reflect": [
            "I can identify the main claim and one piece of "
            "evidence in a youth-led text.",
            "I can use future perfect and future continuous.",
            "I can write a 200-word reflection on a future "
            "scenario.",
        ],
        "pitfalls": [
            "*By 2030 I will finish* (= future simple) does not "
            "stress completion-by; future perfect does.",
            "*Future continuous + state verb* (*I will be "
            "knowing*) → ✗.",
            "Don't romanticise youth-led work — name the small, "
            "boring steps.",
        ],
        "further": [
            "BBC News — Youth-led initiative profiles.",
            "The Conversation — opinion essays on youth and "
            "policy.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"By 2030, the Glasgow Garden Project will have "
            "trained over 200 young volunteers. Next year, the "
            "team will be running workshops for primary-school "
            "groups. The founder says the most useful skill is "
            "small repeated public asking.\"\n\n"
            "1. By 2030: ___ . 2. Next year: ___ . 3. Founder's "
            "key skill: ___ . 4. Definition: ___ ."
        ),
        "exam_reading": (
            "Read the *Glasgow Garden Project* extract above.\n\n"
            "1. Start year: ___ . 2. Site: ___ . 3. Founder's age "
            "at start: ___ . 4. Most useful skill: ___ ."
        ),
        "exam_use": (
            "**Future perfect or future continuous?**\n\n"
            "1. By 2030, I __________ (finish) my training.\n"
            "2. At 5 p.m. tomorrow, I __________ (study).\n"
            "3. By 2028, the project __________ (train) 200 "
            "volunteers.\n"
            "4. Next year, the team __________ (run) workshops."
        ),
        "exam_writing": (
            "Write 200 words on a youth-led initiative. Use 3 "
            "future perfect + 2 future continuous."
        ),
        "exam_keys": [
            "**T1.** 200+ trained volunteers; running workshops for primary-school groups; small repeated public asking; willingness to keep asking adults for things they could refuse.",
            "**T2.** 2024; half-acre derelict industrial site; 15; small repeated public asking.",
            "**T3.** will have finished / will be studying / will have trained / will be running.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 10, "slug": "project-and-presentation",
        "title": "Project and Presentation",
        "skills": ["speaking", "writing", "language_awareness"],
        "bp": [
            "3.3.1 Soziokulturelles Orientierungswissen / Themen",
            "3.3.3.4 Sprechen – zusammenhängendes monologisches Sprechen",
            "3.3.3.5 Schreiben",
            "3.3.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can plan a 4-week project with concrete milestones.",
            "I can deliver a 5-minute presentation with three movements (problem, evidence, ask).",
            "I can use signposting language for spoken and written project work.",
        ],
        "leadin": (
            "Mr. Yilmaz handed out a one-page brief: *Pick one small "
            "civic problem in your area. Spend four weeks "
            "investigating it. Present your findings to the class in "
            "five minutes.* Maja chose the bus stop where the bench "
            "had been broken since November. Sam chose the "
            "lost-property cupboard, which has its own ecosystem."
        ),
        "activate": (
            "**Problem-pick scan.** With your partner, list 5 "
            "small civic problems you would actually investigate. "
            "Pick one for the class brief."
        ),
        "input_blocks": [
            ("Project structure — 4 weeks",
             "Week 1: *Frame the question*. One sentence. Why now?\n"
             "Week 2: *Gather evidence*. Two sources minimum.\n"
             "Week 3: *Talk to one person* affected.\n"
             "Week 4: *Build the ask* — what specifically should "
             "change?"),
            ("Presentation — three movements",
             "1. **Problem (60 sec).** Concrete, specific, named.\n"
             "2. **Evidence (180 sec).** Two sources + one quote "
             "from a real person.\n"
             "3. **Ask (60 sec).** What you want the audience to "
             "do.\n\n"
             "Plus 30 sec buffer for questions."),
            ("Signposts (spoken)",
             "*Today I'd like to talk about … / Let me start with "
             "the problem … / The evidence falls into two parts … / "
             "I spoke to … / What I'm asking is this … / Thank you "
             "for listening.*"),
        ],
        "practise_g": [
            "1. Match: Week 1 → frame; Week 2 → evidence; Week 3 → "
            "interview; Week 4 → ask.",
            "2. Choose signpost: *(opening)* → ___ ; *(closing)* "
            "→ ___ .",
        ],
        "practise_m": [
            "3. Draft the bullets for your own 5-minute "
            "presentation.",
        ],
        "answer_g": (
            "1. all true.\n"
            "2. *Today / Thank you for listening.*"
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Class presentations.** Each student delivers a 5-"
            "minute presentation. Audience uses *I noticed / "
            "what worked / one thing you could try* feedback."
        ),
        "produce_sample": (
            "*Today I'd like to talk about the broken bench at the "
            "Mühlstraße bus stop. The bench has been broken since "
            "November. Let me start with the problem: at least 12 "
            "elderly residents wait for the 14 bus there at 9:14 "
            "every morning, and they have been standing for the "
            "past five months. The evidence falls into two parts: "
            "the city council's online maintenance ticket from "
            "December (still open) and my own count over five "
            "weekday mornings. I spoke to Mrs Schmidt, who lives "
            "two streets away. \"I have to balance against the "
            "pole,\" she said. \"That isn't a bus stop, that's a "
            "rehearsal for a fall.\" What I'm asking is this: "
            "could the class write a single, dated joint letter to "
            "the council? One letter, one date, one specific "
            "request. Thank you for listening.*"
        ),
        "reflect": [
            "I can plan a 4-week project with milestones.",
            "I can deliver a 5-minute three-movement presentation.",
            "I can use 5 signposting phrases.",
        ],
        "pitfalls": [
            "Reading word-for-word kills the talk.",
            "Vague problem (*the council does nothing*) — be "
            "specific.",
            "Skipping the *ask* — the talk loses its point.",
        ],
        "further": [
            "TED-Ed — short student presentations.",
            "BBC Sounds — *Short Cuts*.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"Today I'd like to talk about the broken bench at "
            "the Mühlstraße bus stop. It has been broken since "
            "November. At least 12 elderly residents wait there "
            "every morning. The evidence is the city's open "
            "maintenance ticket and my own count over five "
            "mornings. What I'm asking is one dated joint letter "
            "from the class.\"\n\n"
            "1. Place: ___ . 2. Time broken: ___ . 3. Affected: "
            "___ . 4. The ask: ___ ."
        ),
        "exam_reading": (
            "Read the sample presentation above.\n\n"
            "1. Three movements: ___ . 2. Two sources: ___ . 3. "
            "Quote: ___ . 4. Specific ask: ___ ."
        ),
        "exam_use": (
            "**Insert signposting phrase.**\n\n"
            "1. ___ I'd like to talk about the broken bench.\n"
            "2. ___ , the evidence is the open ticket.\n"
            "3. ___ to Mrs Schmidt, who lives nearby.\n"
            "4. ___ for listening."
        ),
        "exam_writing": (
            "Write a 5-minute presentation script (~250 words) on "
            "a small civic problem. Use the three-movement "
            "structure."
        ),
        "exam_keys": [
            "**T1.** Mühlstraße bus stop; since November; 12 elderly residents at 9:14; one dated joint letter from the class.",
            "**T2.** problem / evidence / ask; council's open maintenance ticket + own count over 5 mornings; *I have to balance against the pole — that isn't a bus stop, that's a rehearsal for a fall*; one dated joint letter.",
            "**T3.** Today / Let me start with / I spoke / Thank you.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 11, "slug": "a-short-novel",
        "title": "A Short Novel",
        "skills": ["reading", "writing", "language_awareness"],
        "bp": [
            "3.3.1 Soziokulturelles Orientierungswissen / Themen",
            "3.3.3.2 Leseverstehen",
            "3.3.3.5 Schreiben",
            "3.3.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can read three chapters of a short novel and identify protagonist arc, theme, and one stylistic move.",
            "I can write a 250-word literary essay with one quote.",
            "I can use *whereas* and *while* (contrast) and *moreover / furthermore* (addition).",
        ],
        "leadin": (
            "The class read three chapters of *The Slow Lane* by "
            "an imagined contemporary author — a short novel about "
            "a teenage long-distance runner. By chapter three, half "
            "the class had stopped seeing it as a sports book. Maja "
            "underlined the line *running, like reading, is a way "
            "of staying still while you move*. She showed the line "
            "to nobody for a week."
        ),
        "activate": (
            "**Three-line scan.** With your partner, write the one-"
            "line summary of each of the three chapters. Compare "
            "with another pair."
        ),
        "input_blocks": [
            ("Reading — *The Slow Lane*, ch. 3 extract",
             "*Running, like reading, is a way of staying still "
             "while you move. By the third week of training, I had "
             "discovered something I hadn't expected: the slow "
             "kilometres were the ones doing the work. Whereas the "
             "fast intervals felt like proof, the slow lanes felt "
             "like the actual training. Moreover, I learned that "
             "everyone faster than me said the same thing.*"),
            ("Grammar — contrast and addition connectives",
             "**Contrast:**\n"
             "- *whereas* — formal: *Whereas the fast intervals "
             "felt like proof, the slow lanes felt like training.*\n"
             "- *while* — slightly less formal.\n\n"
             "**Addition:**\n"
             "- *moreover* — formal addition of a stronger point.\n"
             "- *furthermore* — formal extension.\n"
             "- *in addition* — neutral.\n\n"
             "Use sparingly — they cost weight. One per "
             "paragraph, not three."),
        ],
        "practise_g": [
            "1. Choose: *whereas / while / moreover / furthermore* "
            "— ___ the fast intervals felt like proof, the slow "
            "lanes felt like training.",
            "2. Match: contrast → whereas/while; addition → "
            "moreover/furthermore. (T / F)",
        ],
        "practise_m": [
            "3. Build 4 sentences with one connective each.",
        ],
        "answer_g": (
            "1. Whereas (or While).\n"
            "2. all true."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Literary essay, 250 words.** Read the extract. "
            "Answer: *What is the protagonist's arc? What is the "
            "theme? Which stylistic move is doing the most work?* "
            "Use 1 *whereas* + 1 *moreover* + 1 direct quote."
        ),
        "produce_sample": (
            "*The narrator of *The Slow Lane* arrives at chapter "
            "three having completed two weeks of training and "
            "expecting that the fast work was where the change "
            "would happen. Whereas the fast intervals felt like "
            "evidence — sweat, pain, observable progress — the "
            "slow lanes felt unfinished, almost lazy. The "
            "discovery, in the third week, is that the slow work "
            "was the work. The protagonist's small arc, in this "
            "extract, is the inversion of expectation: not what is "
            "loud, but what is quiet, becomes the centre. The "
            "theme is patience as a method, and the stylistic move "
            "doing the most work is the line *'running, like "
            "reading, is a way of staying still while you move.'* "
            "Without that line, the chapter is competent. With "
            "that line, the chapter quietly insists that physical "
            "training and mental work share the same shape. "
            "Moreover, the line works because the narrator has "
            "earned it — three weeks of slow kilometres are sitting "
            "behind it. The author, who is unnamed in our text, "
            "is making a small but real argument: that the things "
            "we underestimate (slow reading, slow running, slow "
            "anything) are usually where the actual change "
            "happens.*"
        ),
        "reflect": [
            "I can identify protagonist arc, theme, one stylistic move.",
            "I can use formal contrast and addition connectives.",
            "I can write a 250-word literary essay.",
        ],
        "pitfalls": [
            "*Furthermore* + *also* in one sentence → ✗ (one "
            "addition is enough).",
            "*Whereas* with a single contrast (no second clause) → "
            "incomplete.",
            "Don't summarise the plot — analyse moves.",
        ],
        "further": [
            "Granta — accessible literary essays.",
            "London Review of Books — *Diary* short essays.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"Running, like reading, is a way of staying still "
            "while you move. By the third week, the narrator had "
            "discovered that the slow kilometres were doing the "
            "work. Whereas fast intervals felt like proof, the "
            "slow lanes felt like the actual training.\"\n\n"
            "1. Comparison: ___ . 2. Discovery: ___ . 3. Fast: "
            "___ . 4. Slow: ___ ."
        ),
        "exam_reading": (
            "Read the *Slow Lane* extract above.\n\n"
            "1. Three-week discovery: ___ . 2. Fast intervals "
            "described as: ___ . 3. Slow lanes described as: ___ . "
            "4. The pattern faster runners share: ___ ."
        ),
        "exam_use": (
            "**Insert *whereas / while / moreover / "
            "furthermore*.**\n\n"
            "1. ___ the fast intervals felt like proof, the slow "
            "lanes felt like training.\n"
            "2. ___ , I learned that faster runners say the same.\n"
            "3. ___ I expected progress, I discovered patience.\n"
            "4. ___ , the line works because the narrator earned "
            "it."
        ),
        "exam_writing": (
            "Write 250 words: a literary essay on the *Slow Lane* "
            "extract. Use 1 *whereas* + 1 *moreover* + 1 quote."
        ),
        "exam_keys": [
            "**T1.** running and reading share shape; slow kilometres do the work; like proof; like the actual training.",
            "**T2.** the slow kilometres were doing the work; like proof (sweat / pain / progress); like the actual training; the same: slow work was the work.",
            "**T3.** Whereas / Moreover / Whereas / Moreover.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 12, "slug": "year-review-graduation",
        "title": "Year Review: Graduation Exam Prep",
        "skills": ["writing", "speaking", "language_awareness"],
        "bp": [
            "3.3.1 Soziokulturelles Orientierungswissen / Themen",
            "3.3.3.4 Sprechen – zusammenhängendes monologisches Sprechen",
            "3.3.3.5 Schreiben",
            "3.3.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can compile a graduation portfolio with 5 representative pieces.",
            "I can write a 250-word year reflection demonstrating a wide grammar range.",
            "I can deliver a 3-minute graduation talk with one quote from my own writing.",
        ],
        "leadin": (
            "Mr. Yilmaz wrote on the board: *one folder, five "
            "pieces, three hundred days*. The class understood it "
            "without explanation — the year was nearly over, and "
            "the graduation portfolio was due. Maja had already "
            "started. Sam had a rough table of contents written on "
            "the back of an envelope from a forest ranger he had "
            "never met."
        ),
        "activate": (
            "**Pick-five scan.** Open your folder. Pick five "
            "pieces. Label each: *proudest / surprised me / didn't "
            "work / would rewrite / connects to my next step*."
        ),
        "input_blocks": [
            ("Portfolio structure (Klasse 10)",
             "1. **Cover sheet** (name, year, theme).\n"
             "2. **Five pieces** (one-line label each).\n"
             "3. **Reflection** (250 words: arc of the year, one "
             "moment of progress, one disappointment, one "
             "connection to the next step).\n"
             "4. **Talk** (3 minutes; one quote from your own "
             "writing).\n"
             "5. **Forward letter** (200 words to your future "
             "Klasse-11 / apprenticeship self)."),
            ("Reflection — useful frames",
             "*At the start of Klasse 10 I … / By Christmas I had "
             "started to … / The piece that surprised me was … / "
             "The piece that didn't work taught me that … / The "
             "thread I want to keep going is … / If I had known in "
             "September what I know now, I would have …*"),
        ],
        "practise_g": [
            "1. Build the five labels for your own folder.",
        ],
        "practise_m": [
            "2. Build a 6-line reflection draft using mixed "
            "tenses (past simple, past perfect, present perfect, "
            "future perfect).",
        ],
        "answer_g": "Open.",
        "answer_m": "Open.",
        "produce": (
            "**Portfolio + 250-word reflection + 3-minute talk + "
            "200-word forward letter.** Each student submits the "
            "portfolio and delivers a 3-minute graduation talk to "
            "the class. Audience gives one feedback sentence."
        ),
        "produce_sample": (
            "*At the start of Klasse 10 I wrote in three modes: "
            "translated, formal, and quietly imitating other "
            "people. By Christmas I had started to write in a "
            "fourth mode that I would call *paying attention*. The "
            "piece I am proudest of is my Mühlstraße bus-stop "
            "presentation: it taught me that small civic English "
            "is mostly about saying *what specifically should "
            "change.* The piece that didn't work was my first draft "
            "of the *Slow Lane* essay — I summarised the plot "
            "instead of analysing it. If I had known in September "
            "that the slow lanes were where the work happened, I "
            "would have spent more time on small editing rather "
            "than on first drafts. By 2027, I will have completed "
            "either an apprenticeship or a year of FOS. The thread "
            "I want to keep going is *small repeated public "
            "asking* — the thing I learned from the Glasgow "
            "Garden founder. Whichever path I take, it is "
            "honestly the most useful thing I have read this year. "
            "Moreover, it works in my own language too.*"
        ),
        "reflect": [
            "I can compile a 5-piece graduation portfolio.",
            "I can write a 250-word year reflection.",
            "I can deliver a 3-minute graduation talk.",
        ],
        "pitfalls": [
            "Reading the talk verbatim.",
            "Generic claims (*I learned a lot*) — give one "
            "specific example.",
            "Picking only your best five — the *didn't-work* slot "
            "matters.",
        ],
        "further": [
            "BBC Bitesize — *Reflective writing*.",
            "British Council — *Self-evaluation* tips for upper "
            "secondary.",
        ],
        "exam_listening": (
            "Listen twice to a graduation talk.\n\n"
            "> \"At the start of Klasse 10 I wrote in three modes: "
            "translated, formal, and imitating others. By Christmas "
            "I had started to write in a fourth mode I'd call "
            "*paying attention*. The piece I'm proudest of is the "
            "Mühlstraße bus-stop presentation. By 2027, I will "
            "have completed either an apprenticeship or a year "
            "of FOS.\"\n\n"
            "1. Three September modes: ___ . 2. Christmas change: "
            "___ . 3. Proudest piece: ___ . 4. By 2027: ___ ."
        ),
        "exam_reading": (
            "Read the reflection sample above.\n\n"
            "1. Four writing modes: ___ . 2. Proudest piece: "
            "___ . 3. Lesson learnt: ___ . 4. Future plan: ___ ."
        ),
        "exam_use": (
            "**Mixed grammar review.**\n\n"
            "1. By Christmas I __________ (start) to write "
            "differently. (past perfect)\n"
            "2. If I __________ (know) earlier, I __________ "
            "(spend) more time on editing. (third conditional)\n"
            "3. By 2027, I __________ (complete) my training. "
            "(future perfect)\n"
            "4. The piece __________ (write / passive) in March."
        ),
        "exam_writing": (
            "Write a 250-word year-review reflection. Use 5 "
            "grammar points from Klasse 9 + 10."
        ),
        "exam_keys": [
            "**T1.** translated / formal / imitating; *paying attention*; Mühlstraße bus-stop presentation; either apprenticeship or year of FOS.",
            "**T2.** translated, formal, imitating, paying attention; Mühlstraße bus-stop presentation; small civic English is mostly *what specifically should change*; complete apprenticeship or FOS year by 2027.",
            "**T3.** had started / had known-would have spent / will have completed / was written.",
            "**T4.** Open.",
        ],
    },
]


UNIT_TPL = """---
title: "Unit {n} — {title}"
subtitle: "Track G+M · Klasse 10 · Niveau G/M"
niveau: "G+M"
klassenstufe: 10
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
**Niveau:** G/M parallel. class test (Klassenarbeit) at Niveau M (45 BE).
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
structure. Above Niveau M: extension prompt linking to Klasse 11
(or post-Klasse-10 path).
:::

## Common pitfalls

{pitfalls}

## Further reading / listening

{further}
"""

EXAM_BODY_TPL = """::: {{.callout-warning icon=false title="class test (Klassenarbeit) — Niveau M (45 minutes)"}}
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
subtitle: "Track G+M · Klasse 10 · Niveau M · 45 Minuten"
author: "S. Le Boulanger"
niveau: "M"
klassenstufe: 10
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

# class test (Klassenarbeit) — Unit {n}: {title}

**Track G+M · Klasse 10 · Niveau M · 45 Minuten**

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

    print(f"Wrote {len(UNITS) * 3} files for Track G+M Klasse 10.")


if __name__ == "__main__":
    emit()
