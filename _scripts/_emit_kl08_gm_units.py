"""Batch-emit Track G+M Klasse 8 — all 12 Units.

Klasse 8 voice: identity, fairness, belonging, dry / observational
humour. Cast: Jonas, Hawa, plus a global pen-pal class. Bildungsplan
prefix 3.2 (Klassen 7/8/9). Grammar arc moves toward middle-secondary:
passive, second conditional, relative clauses, modals of possibility,
present perfect (simple).
"""
from __future__ import annotations
import pathlib

REPO = pathlib.Path(__file__).resolve().parent.parent
COURSE = REPO / "track_gm_kl08" / "units"

UNITS = [
    {
        "n": 1, "slug": "identities", "title": "Identities",
        "skills": ["reading", "writing", "intercultural"],
        "bp": [
            "3.2.1 Soziokulturelles Orientierungswissen / Themen",
            "3.2.2 Interkulturelle kommunikative Kompetenz",
            "3.2.3.2 Leseverstehen",
            "3.2.3.5 Schreiben",
            "3.2.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can read a short identity-text and identify the writer's main claim.",
            "I can use *both / either / neither* to talk about belonging.",
            "I can write a 120-word self-portrait that goes beyond surface labels.",
        ],
        "leadin": (
            "Hawa's class made a wall called *Who Am I, Today?* Each "
            "student pinned three small cards to the wall: a country, "
            "a language, a thing they like. Hawa pinned *Nigeria, "
            "Yoruba, my grandmother's stew*. Jonas pinned *Germany, "
            "Polish, my brother's old skateboard*. The wall, by "
            "Friday, looked like an unusually honest atlas."
        ),
        "activate": (
            "**Three cards.** On three sticky notes, write: a place "
            "you feel from, a language you grew up hearing, a thing "
            "you do that says something about who you are. Stick "
            "them up. No labels — just things."
        ),
        "input_blocks": [
            ("Reading — *Hawa's wall*",
             "*The wall changed every week. People added new cards, "
             "moved old ones, sometimes took one down and never "
             "explained why. Mr. Ade said the wall was \"a working "
             "draft of the class\". I think identity is also a "
             "working draft. We are who we are right now, plus the "
             "things we are still trying out, plus the things we "
             "haven't told anyone yet.*"),
            ("Vocabulary — identity",
             "*roots, heritage, language, belonging, hometown, "
             "background, identity, multilingual, bilingual, "
             "first language, mother tongue, second language, "
             "tradition, custom, community.*"),
            ("Grammar — *both / either / neither*",
             "- *Both* + plural: *Both languages are part of who I am.*\n"
             "- *Either* + singular (in negatives/questions): *I "
             "don't speak either language perfectly.*\n"
             "- *Neither* + singular: *Neither parent grew up here.*\n"
             "- *Both … and …*: *I speak both Polish and German at home.*\n"
             "- *Neither … nor …*: *Neither my mum nor my dad "
             "celebrates that holiday.*"),
        ],
        "practise_g": [
            "1. Choose: *both / either / neither* — Hawa speaks "
            "__________ Yoruba and English. I don't speak "
            "__________ language perfectly. __________ of my "
            "parents was born here.",
            "2. Build: *(both / Polish / German)* → ___ ; *(neither "
            "/ mum / dad / celebrates)* → ___ .",
        ],
        "practise_m": [
            "3. Build 4 sentences about your own languages, places, "
            "or traditions using *both / either / neither / both … "
            "and …*",
        ],
        "answer_g": (
            "1. both / either / Neither.\n"
            "2. *I speak both Polish and German.* / *Neither my "
            "mum nor my dad celebrates that holiday.*"
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Self-portrait, 120 words.** Three paragraphs: *Where "
            "I come from* (1–2 sentences), *Languages and people in "
            "my life* (4–5 sentences), *What I am still figuring "
            "out* (2–3 sentences). Use at least two of: *both / "
            "either / neither / both … and …*"
        ),
        "produce_sample": (
            "*I come from Stuttgart, but my parents come from "
            "Krakow. I grew up hearing Polish at home and German "
            "at school. I speak both languages, although neither "
            "of them perfectly. My grandmother sends me long "
            "voice messages in a mix of both, and I love it. What "
            "I am still figuring out is whether I want to study in "
            "Germany or in Poland. Either way, I think I will end "
            "up with a strange accent.*"
        ),
        "reflect": [
            "I can read an identity text and find the main claim.",
            "I can use *both / either / neither / both … and …*.",
            "I can write a 120-word self-portrait beyond labels.",
        ],
        "pitfalls": [
            "*Both of my parents are not* → ✗ / *Neither of my "
            "parents is* → ✓.",
            "*Neither … or …* → ✗ / *Neither … nor …* → ✓.",
            "Don't reduce identity to a flag — push for one "
            "concrete object or moment.",
        ],
        "further": [
            "BBC Bitesize — *Identity* topic at KS3 level.",
            "British Council Voices — short student-identity essays.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"Both my parents grew up in different countries. "
            "Neither of them speaks the other's first language "
            "well. They communicate in English. I grew up with "
            "three languages, but only one of them — German — "
            "is the one I dream in.\"\n\n"
            "1. Parents: ___ . 2. Common language: ___ . 3. "
            "Speaker's languages: ___ . 4. Dream language: ___ ."
        ),
        "exam_reading": (
            "Read.\n\n"
            "> \"My identity is not a single label. It is a list "
            "that changes every year. When I was eleven, I was "
            "mainly *the football kid*. Now I am the kid who reads "
            "instead. I haven't told my old team yet.\"\n\n"
            "1. Single label? ___ . 2. List changes: ___ . 3. At "
            "11, the writer was: ___ . 4. Now: ___ ."
        ),
        "exam_use": (
            "**Fill in *both / either / neither*.**\n\n"
            "1. ___ my parents grew up here. (both)\n"
            "2. ___ of them speaks Yoruba. (neither)\n"
            "3. I don't celebrate ___ holiday strictly. (either)\n"
            "4. We speak ___ Polish ___ German at home. (both / and)"
        ),
        "exam_writing": (
            "Write 120 words: a self-portrait beyond surface labels."
        ),
        "exam_keys": [
            "**T1.** different countries, English, three, German.",
            "**T2.** No, every year, the football kid, reads instead.",
            "**T3.** 1. Both, 2. Neither, 3. either, 4. both / and.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 2, "slug": "school-life-elsewhere", "title": "School Life Elsewhere",
        "skills": ["reading", "speaking", "intercultural"],
        "bp": [
            "3.2.1 Soziokulturelles Orientierungswissen / Themen",
            "3.2.2 Interkulturelle kommunikative Kompetenz",
            "3.2.3.2 Leseverstehen",
            "3.2.3.3 Sprechen – an Gesprächen teilnehmen",
        ],
        "objectives": [
            "I can read short pen-pal texts from 3 countries and compare them.",
            "I can use the present passive to talk about how things are done elsewhere.",
            "I can hold a 2-minute conversation comparing schools.",
        ],
        "leadin": (
            "Mr. Ade pinned three printed e-mails to the noticeboard. "
            "One from a school in Lagos. One from a school in "
            "Helsinki. One from a school in São Paulo. Three "
            "students were assigned to read them and report back. "
            "Hawa read all three twice before lunch."
        ),
        "activate": (
            "**Predict.** Slide shows three flags. With your partner, "
            "predict three differences each school might have from "
            "yours."
        ),
        "input_blocks": [
            ("Reading — three short pen-pal extracts",
             "*Lagos.* In our school, lessons are taught in English, "
             "but we speak Yoruba and Igbo with friends. Uniform is "
             "compulsory. Lunch is brought from home.\n\n"
             "*Helsinki.* In Finland, school starts at age 7. "
             "Homework is given lightly. Lunch is provided free. We "
             "go outside for a break every hour, even in -10°C.\n\n"
             "*São Paulo.* Our school day is split: lessons in the "
             "morning, sports in the afternoon. Homework is set "
             "every day. Lunch is bought at a small canteen."),
            ("Grammar — present passive",
             "Form: *to be* (in tense) + past participle.\n"
             "- *Lessons are taught in English.*\n"
             "- *Homework is given lightly.*\n"
             "- *Lunch is provided free.*\n"
             "- *Sports are played in the afternoon.*\n\n"
             "Use the passive when *who* does the action is "
             "obvious or unimportant."),
        ],
        "practise_g": [
            "1. Active → passive: They teach lessons in English. → ___ "
            "; The school provides lunch. → ___ ; Teachers give "
            "homework. → ___ .",
            "2. Choose active or passive (more natural): *(somebody / "
            "set / homework / every day)* → ___ .",
        ],
        "practise_m": [
            "3. Build 4 sentences in present passive about how "
            "things are done at your school.",
        ],
        "answer_g": (
            "1. *Lessons are taught in English. Lunch is provided "
            "by the school. Homework is given by teachers.*\n"
            "2. *Homework is set every day.*"
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Pair speaking — *Compare three schools*.** 2 min each. "
            "Use 3 passive structures + one comparison. Report "
            "back to the class with one *I learned that …* sentence."
        ),
        "produce_sample": (
            "*— In Helsinki, lunch is provided free at school, "
            "while in São Paulo lunch is bought at a canteen.*\n"
            "*— Yes, and homework is given more in São Paulo than "
            "in Helsinki.*"
        ),
        "reflect": [
            "I can read three pen-pal texts and compare them.",
            "I can build present passive sentences.",
            "I can run a 2-minute compare-and-contrast conversation.",
        ],
        "pitfalls": [
            "*Lessons are teach* → ✗ / *Lessons are taught* → ✓.",
            "Using passive when active is clearer: *I do my "
            "homework* not *Homework is done by me* unless context "
            "demands it.",
            "L1 trap: German *man* often becomes English passive: "
            "*Man liest viel* → *A lot is read* / *We read a lot*.",
        ],
        "further": [
            "BBC News — *Education* short articles.",
            "British Council Schools Online — pen-pal projects.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"In Finland, lunch is provided free for every "
            "student. Homework is given lightly. Children go "
            "outside every hour, even in cold weather. Tests are "
            "fewer than in many other countries.\"\n\n"
            "1. Lunch: ___ . 2. Homework: ___ . 3. Outside: ___ . "
            "4. Tests: ___ ."
        ),
        "exam_reading": (
            "Read.\n\n"
            "> \"In our Lagos school, lessons are taught in "
            "English, but English is most students' second "
            "language. Uniform is compulsory and is checked "
            "every morning. Lunch is brought from home in metal "
            "containers.\"\n\n"
            "1. Lesson language: ___ . 2. First language? ___ . "
            "3. Uniform: ___ . 4. Lunch: ___ ."
        ),
        "exam_use": (
            "**Active → passive.**\n\n"
            "1. They teach English from age 5. → ___\n"
            "2. The school provides lunch. → ___\n"
            "3. Teachers set homework every day. → ___\n"
            "4. Students wear uniform. → ___"
        ),
        "exam_writing": (
            "Write 100 words comparing your school with one of "
            "the three pen-pal schools. Use 4 passive structures."
        ),
        "exam_keys": [
            "**T1.** provided free, given lightly, every hour, fewer.",
            "**T2.** English, no — second language for most, compulsory + checked, brought from home in metal containers.",
            "**T3.** *English is taught from age 5. Lunch is provided by the school. Homework is set every day. Uniform is worn.*",
            "**T4.** Open.",
        ],
    },
    {
        "n": 3, "slug": "fairness-at-school", "title": "Fairness at School",
        "skills": ["speaking", "writing", "language_awareness"],
        "bp": [
            "3.2.1 Soziokulturelles Orientierungswissen / Themen",
            "3.2.3.3 Sprechen – an Gesprächen teilnehmen",
            "3.2.3.5 Schreiben",
            "3.2.3.8 Verfügen über sprachliche Mittel – Grammatik",
        ],
        "objectives": [
            "I can argue a school-fairness point in 5 sentences.",
            "I can use the second conditional (*if I were … I would …*).",
            "I can use connectives of contrast (*although, however, on the other hand*).",
        ],
        "leadin": (
            "Jonas's class is voting on a new rule: *no phones at "
            "lunch*. Half the class is for it. The other half "
            "thinks it is mostly aimed at one group of students who "
            "happen to be loud anyway. Hawa says, \"If I were the "
            "headteacher, I would ask why we are voting on phones "
            "and not on actual fairness.\""
        ),
        "activate": (
            "**Two-minute scan.** On the slide are five school "
            "rules. With your partner, mark each one as *fair / "
            "unfair / depends*."
        ),
        "input_blocks": [
            ("Vocabulary — fairness",
             "*rule, rights, equal, equality, privilege, "
             "discrimination, exception, vote, debate, agree, "
             "disagree, valid, biased, neutral, inclusive.*"),
            ("Grammar — second conditional",
             "Structure: *If* + past simple, *would* + base verb.\n"
             "- *If I were the headteacher, I would change the "
             "rule.*\n"
             "- *If we voted, it would be close.*\n"
             "- *I wouldn't ban phones if I had to enforce the "
             "rule myself.*\n\n"
             "*Were* (not *was*) is preferred for *I/he/she/it* in "
             "formal writing: *If I **were** you …*"),
            ("Connectives of contrast",
             "*although, however, on the other hand, even though, "
             "still, but, yet.*\n"
             "- *Although the rule is meant to help, it doesn't.*\n"
             "- *However, I see the point of the original idea.*\n"
             "- *On the other hand, fairness has limits.*"),
        ],
        "practise_g": [
            "1. Fill in second conditional: If I __________ (be) "
            "the headteacher, I __________ (change) the rule.",
            "2. Connective fill-in: ___ I agree with the rule, "
            "I think it is unfair to one group. (although)",
        ],
        "practise_m": [
            "3. Build 3 second-conditional sentences and 2 contrast "
            "sentences about a school rule you would change.",
        ],
        "answer_g": (
            "1. were / would change.\n"
            "2. Although."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Mini-debate.** Two teams of 4. The motion: *This "
            "class would replace the no-phones rule with a "
            "no-loud-phones rule.* Each speaker uses one second "
            "conditional + one contrast connective. Two minutes "
            "per side."
        ),
        "produce_sample": (
            "*— If we replaced the rule, we would still have "
            "quiet lunch tables. However, some people just "
            "wouldn't follow it.*\n"
            "*— On the other hand, the current rule punishes "
            "everyone for the loudness of a few.*"
        ),
        "reflect": [
            "I can argue a school-fairness point in 5 sentences.",
            "I can use the second conditional in writing.",
            "I can use 3 connectives of contrast.",
        ],
        "pitfalls": [
            "*If I would be …* → ✗ / *If I were …* → ✓.",
            "*Although + but* in one sentence → ✗ — pick one.",
            "*on the another hand* → ✗ / *on the other hand* → ✓.",
        ],
        "further": [
            "BBC Newsround — short fairness debates for teens.",
            "Childline UK — *Your rights at school* page.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"If I were the headteacher, I would replace the "
            "no-phones rule with a no-loud-phones rule. I think "
            "it would be fairer. Although some students would "
            "still break it, most wouldn't. On the other hand, "
            "enforcing it would still be tricky.\"\n\n"
            "1. Speaker would replace: ___ . 2. With: ___ . 3. "
            "Most students would: ___ . 4. Tricky part: ___ ."
        ),
        "exam_reading": (
            "Read.\n\n"
            "> \"In an interview, the head pupil said: 'If we had "
            "more student representation on the rule committee, "
            "fewer rules would feel unfair. However, I understand "
            "that adults don't always want students to vote on "
            "everything.'\"\n\n"
            "1. What would help: ___ . 2. Result: ___ . 3. "
            "Adults: ___ . 4. *However* introduces: ___ ."
        ),
        "exam_use": (
            "**Build the second conditional.**\n\n"
            "1. If I __________ (be) headteacher, I __________ "
            "(change) the rule.\n"
            "2. If we __________ (vote), the result __________ "
            "(be) close.\n"
            "3. I __________ (not / ban) phones if I __________ "
            "(have) to enforce it.\n"
            "4. Although the rule __________ (be) clear, it "
            "__________ (not / be) fair."
        ),
        "exam_writing": (
            "Write 120 words: one school rule you would change. "
            "Use 2 second conditionals + 2 contrast connectives."
        ),
        "exam_keys": [
            "**T1.** no-phones rule, no-loud-phones rule, wouldn't break, enforcing.",
            "**T2.** more student representation, fewer rules feel unfair, don't always want students to vote, contrast.",
            "**T3.** were / would change; voted / would be; wouldn't ban / had; is / is not (or *isn't*).",
            "**T4.** Open.",
        ],
    },
    {
        "n": 4, "slug": "ireland-stories", "title": "Ireland: Stories from the Island",
        "skills": ["reading", "writing", "intercultural"],
        "bp": [
            "3.2.1 Soziokulturelles Orientierungswissen / Themen",
            "3.2.2 Interkulturelle kommunikative Kompetenz",
            "3.2.3.2 Leseverstehen",
            "3.2.3.5 Schreiben",
            "3.2.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can read a short narrative about Ireland and identify the speaker's perspective.",
            "I can use relative clauses (*who, which, that, where*).",
            "I can write a 120-word place-portrait of an English-speaking region.",
        ],
        "leadin": (
            "Hawa's pen-pal Niamh lives in Galway, on the west "
            "coast of Ireland. Her e-mails are mostly about wind, "
            "music, and people who walk faster than they talk. "
            "Hawa printed one and read it aloud at the breakfast "
            "table. Her father said: \"That's the kind of place "
            "where you'd lose three umbrellas in a week.\""
        ),
        "activate": (
            "**Map quick-think.** On the slide is a map of "
            "Ireland with five towns marked. With your partner, "
            "guess which one is on the west coast, which is the "
            "capital, which is in Northern Ireland."
        ),
        "input_blocks": [
            ("Reading — *Niamh's letter from Galway*",
             "*Hi Hawa, today the wind tried to take my school "
             "bag along Salthill prom. I won. Galway is the kind "
             "of city where you can walk into a pub at lunchtime "
             "and find three musicians playing for the joy of it. "
             "My grandmother, who learned Irish (Gaeilge) as a "
             "first language, says the language is louder than "
             "ever. The shops where the staff speak only Irish "
             "are still rare, but they exist. I'll write more on "
             "Tuesday, which is when I'm meant to be doing "
             "homework but I'll probably write to you instead.*"),
            ("Grammar — relative clauses",
             "*who* — for people: *My grandmother, who learned "
             "Irish, …*\n"
             "*which* — for things: *The wind, which is famous, …*\n"
             "*that* — people or things (informal): *The pub that "
             "has the best music …*\n"
             "*where* — places: *Galway is a city where …*\n\n"
             "Defining (no commas) vs. non-defining (with "
             "commas): *The pub that has music* (defines which "
             "pub). *Galway, which is on the west coast, is "
             "famous for music* (extra info)."),
        ],
        "practise_g": [
            "1. Choose: *who, which, that, where*. The musicians "
            "__________ play in the pub. The wind __________ took "
            "the bag. Galway is a place __________ the rain is "
            "constant.",
            "2. Combine: *Niamh has a grandmother. She learned "
            "Irish.* → ___ .",
        ],
        "practise_m": [
            "3. Build 4 sentences with one relative clause each "
            "(use *who, which, that, where*).",
        ],
        "answer_g": (
            "1. who / that — which / that — where.\n"
            "2. *Niamh has a grandmother who learned Irish.*"
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Place-portrait, 120 words.** Write a short letter "
            "describing a place you know (or want to know) in an "
            "English-speaking country. Use 4 relative clauses."
        ),
        "produce_sample": (
            "*Hi Niamh, I'd love to visit a place where the sea "
            "and the city sit next to each other — like your "
            "Galway. I want to find the pub that has music every "
            "lunchtime. My friend Jonas, who has been to Dublin "
            "twice, says the buses there are run by people who "
            "actually answer questions. I'd start with the "
            "Cliffs of Moher, which I have only seen on "
            "postcards. Then I'd ask your grandmother to teach me "
            "one Irish phrase, just one, that I could use every "
            "day.*"
        ),
        "reflect": [
            "I can read a short Irish letter and find the speaker's perspective.",
            "I can use relative clauses (who/which/that/where).",
            "I can write a 120-word place-portrait letter.",
        ],
        "pitfalls": [
            "*The man which* → ✗ / *The man who* → ✓.",
            "Comma misuse with defining clauses: *The pub, that "
            "has music,* → ✗ — no commas in defining clauses.",
            "Stereotype check: avoid *all Irish people drink "
            "Guinness*.",
        ],
        "further": [
            "RTÉ Learning English — Ireland-focused content.",
            "Tourism Ireland — accessible articles for young learners.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"Galway is a city on the west coast of Ireland "
            "that is famous for music. The pub which I love has "
            "live music every lunchtime. My pen-pal, who is "
            "called Niamh, sends letters about it.\"\n\n"
            "1. Galway location: ___ . 2. Famous for: ___ . 3. "
            "Pub has: ___ . 4. Pen-pal name: ___ ."
        ),
        "exam_reading": (
            "Read the *Niamh's letter* extract above. Answer.\n\n"
            "1. What did the wind do? ___ . 2. What does Galway "
            "have at lunchtime? ___ . 3. What does the "
            "grandmother think about Irish? ___ . 4. Where does "
            "the writer write instead of doing homework? ___ ."
        ),
        "exam_use": (
            "**Insert the correct relative pronoun.**\n\n"
            "1. The musicians __________ play in the pub.\n"
            "2. The shops __________ sell only Irish books.\n"
            "3. Galway is a city __________ the rain is "
            "constant.\n"
            "4. The wind, __________ is famous in Galway, is "
            "very strong."
        ),
        "exam_writing": (
            "Write 120 words: a place-portrait letter. Use 4 "
            "relative clauses."
        ),
        "exam_keys": [
            "**T1.** west coast of Ireland, music, live music every lunchtime, Niamh.",
            "**T2.** tried to take her school bag; live music; says it is louder than ever; on Tuesday — to her pen-pal.",
            "**T3.** who/that, which/that, where, which.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 5, "slug": "digital-friendships", "title": "Digital Friendships",
        "skills": ["listening", "writing", "language_awareness"],
        "bp": [
            "3.2.1 Soziokulturelles Orientierungswissen / Themen",
            "3.2.3.1 Hör-/Hörsehverstehen",
            "3.2.3.5 Schreiben",
            "3.2.3.7 Verfügen über sprachliche Mittel – Wortschatz",
            "3.2.3.8 Verfügen über sprachliche Mittel – Grammatik",
        ],
        "objectives": [
            "I can describe a digital friendship using present perfect (simple).",
            "I can use *for / since / ever / never / just / already / yet*.",
            "I can write a 120-word reflection on online friendship.",
        ],
        "leadin": (
            "Jonas has a friend in Iceland whom he has never met "
            "in person. They have been writing to each other on a "
            "shared map app for two years. They have already "
            "exchanged 287 photos of clouds. They have not yet "
            "spoken on the phone. Jonas says, \"It's a friendship. "
            "It just looks weird.\""
        ),
        "activate": (
            "**Quick poll.** Stand up if you have ever played a "
            "game online with someone you don't know in person. "
            "Sit if you have never. Notice. No comment yet."
        ),
        "input_blocks": [
            ("Listening — *The Cloud-Sender*",
             "*Jonas and his Icelandic friend Ari started writing "
             "to each other on a map app two years ago. Each one "
             "drops photos of the sky in their location. Jonas has "
             "sent 287 cloud photos. Ari has answered 287 times. "
             "They have never met. They have not yet spoken on the "
             "phone. Jonas says he just doesn't see the point of "
             "phones for this kind of friendship.*"),
            ("Grammar — present perfect simple",
             "Form: *have/has + past participle*.\n\n"
             "**for** + duration: *for two years.*\n"
             "**since** + start point: *since 2024.*\n"
             "**ever / never**: *Have you ever met him? — No, I "
             "have never met him.*\n"
             "**just** (recent): *I have just sent the photo.*\n"
             "**already** (sooner than expected): *We have already "
             "exchanged 287 photos.*\n"
             "**yet** (not yet completed, in negatives/Q): *We "
             "haven't spoken on the phone yet.*"),
        ],
        "practise_g": [
            "1. Insert *for* or *since*: I have known him "
            "__________ two years. I have lived here __________ "
            "2024.",
            "2. Place *just / already / yet*: I have ___ sent the "
            "message. They have ___ replied. We haven't met ___ .",
        ],
        "practise_m": [
            "3. Build 4 present-perfect sentences about a "
            "friendship: 1 with *for*, 1 with *since*, 1 with "
            "*never*, 1 with *yet*.",
        ],
        "answer_g": (
            "1. for / since.\n"
            "2. just / already / yet."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Reflection, 120 words.** Write about a "
            "friendship that exists mostly online (or one you "
            "imagine could exist). Use 4 present-perfect "
            "structures and one *because*-clause."
        ),
        "produce_sample": (
            "*I have been writing to Ari for almost two years. "
            "We started because of a school project, but we have "
            "kept writing because his cloud photos make my "
            "afternoons better. We have already exchanged 287 "
            "photos. We have never spoken on the phone. We just "
            "don't need to. Sometimes I worry that I haven't met "
            "him yet, and that the friendship will stay flat. "
            "Then he sends another photo of a strange-shaped "
            "cloud and I laugh, and the worry feels like the "
            "wrong size for the situation.*"
        ),
        "reflect": [
            "I can use present perfect with *for/since/ever/"
            "never/just/already/yet*.",
            "I can describe a digital friendship in 120 words.",
            "I can spot when present perfect is wrong (with past "
            "time markers).",
        ],
        "pitfalls": [
            "*I have seen him yesterday* → ✗ — past time marker → "
            "past simple.",
            "*I have met him since two years* → ✗ / *for two years* → ✓.",
            "*Already* in negatives sounds odd; prefer *yet*.",
        ],
        "further": [
            "BBC Learning English — *Present perfect* lessons.",
            "ChildLine UK — *Online friendships* topic.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"Jonas has been writing to Ari for almost two "
            "years. They have never met. They have already "
            "exchanged 287 photos of clouds. They haven't spoken "
            "on the phone yet. Jonas says they just don't need "
            "to.\"\n\n"
            "1. How long: ___ . 2. Met in person: ___ . 3. "
            "Photos: ___ . 4. Phone: ___ ."
        ),
        "exam_reading": (
            "Read.\n\n"
            "> \"I have known my best friend Lia for six years. "
            "We met in primary school. Last year she moved to "
            "Munich. Since then we have written every week and "
            "have already met up three times. We haven't decided "
            "yet which Christmas to spend together.\"\n\n"
            "1. How long: ___ . 2. Where met: ___ . 3. Move: "
            "___ . 4. Christmas: ___ ."
        ),
        "exam_use": (
            "**Present perfect.**\n\n"
            "1. I __________ (know) him for two years.\n"
            "2. We __________ (not / meet) yet.\n"
            "3. They __________ (already / send) 287 photos.\n"
            "4. ___ you ___ (ever / play) chess online?"
        ),
        "exam_writing": (
            "Write 120 words about an online friendship (real or "
            "imagined). Use 4 present-perfect structures."
        ),
        "exam_keys": [
            "**T1.** almost two years, never, 287 cloud photos, not yet — they don't need to.",
            "**T2.** six years, primary school, to Munich last year, not yet decided.",
            "**T3.** 1. have known, 2. haven't met, 3. have already sent, 4. Have … ever played.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 6, "slug": "opinion-writing", "title": "Writing an Opinion",
        "skills": ["reading", "writing", "language_awareness"],
        "bp": [
            "3.2.1 Soziokulturelles Orientierungswissen / Themen",
            "3.2.3.2 Leseverstehen",
            "3.2.3.5 Schreiben",
            "3.2.3.8 Verfügen über sprachliche Mittel – Grammatik",
            "3.2.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can read an opinion text and identify the main claim and one supporting reason.",
            "I can structure my own opinion in 4 paragraphs (claim, reason, counter, conclusion).",
            "I can use signposting phrases (*in my view, on the contrary, in contrast, finally*).",
        ],
        "leadin": (
            "Hawa's class is writing opinion pieces for a school "
            "blog. The topic: *Should pupils have a say in choosing "
            "school books?* Mr. Ade pinned a single-page guide on "
            "the wall: *Claim. One reason. One counter. "
            "Conclusion.* Hawa stared at it. \"Four moves,\" she "
            "said. \"That's almost a dance.\""
        ),
        "activate": (
            "**Claim spotting.** Slide shows three short paragraphs. "
            "With your partner, underline the one sentence in each "
            "that is the writer's main *claim*."
        ),
        "input_blocks": [
            ("Reading — model opinion text",
             "*In my view, pupils should help choose at least one "
             "of the books we read each year. Firstly, when "
             "students are part of the choice, they are more "
             "likely to actually read the book. Secondly, the "
             "school benefits because more voices are involved. "
             "On the other hand, teachers know the curriculum "
             "better than students do, and that knowledge matters. "
             "In conclusion, a small say — perhaps one book in "
             "three — would be a fair compromise.*"),
            ("Structure of the opinion paragraph",
             "1. **Claim** — what you think.\n"
             "2. **Reason** — why.\n"
             "3. **Counter** — what someone might say against you.\n"
             "4. **Conclusion** — your final position, slightly "
             "softer or sharper.\n\n"
             "Signposts: *In my view / I think / firstly / "
             "secondly / on the other hand / however / on the "
             "contrary / in contrast / in conclusion / overall.*"),
        ],
        "practise_g": [
            "1. Match: claim — c, reason — r, counter — co, "
            "conclusion — cn. Label each sentence in the model "
            "text.",
            "2. Choose the right signpost: *(disagreement)* → ___ ; "
            "*(adding a second reason)* → ___ ; *(closing)* → ___ .",
        ],
        "practise_m": [
            "3. Build a 4-sentence mini-opinion on: *Should we "
            "have a longer break?*",
        ],
        "answer_g": (
            "1. open (most students should help choose = c; "
            "*Firstly* / *Secondly* = r; *On the other hand* = co; "
            "*In conclusion* = cn).\n"
            "2. *On the contrary / However / Secondly / Finally / "
            "In conclusion.*"
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Opinion paragraph, 120 words.** Choose: *Should "
            "school start later? Should pupils choose one book a "
            "year? Should school clubs be free?* Use the four-move "
            "structure and three signposts."
        ),
        "produce_sample": (
            "*In my view, school clubs should be free for everyone. "
            "Firstly, paying makes some clubs feel like extra "
            "school, when they should feel like a release valve. "
            "Secondly, free clubs reach pupils whose families "
            "cannot pay, which is the whole point. On the other "
            "hand, equipment costs money, and someone has to pay "
            "for it. In conclusion, the school could ask for a "
            "small *contribution if you can*, but never block a "
            "pupil from joining because of cost.*"
        ),
        "reflect": [
            "I can identify claim, reason, counter, conclusion in a text.",
            "I can structure an opinion text with three signposts.",
            "I can write a 120-word opinion paragraph.",
        ],
        "pitfalls": [
            "Stating an opinion without a reason → reads as a "
            "claim only.",
            "Skipping the counter → makes the writing look like a "
            "rant.",
            "Mixing first person with passive: *In my view, the "
            "rule is changed* → unclear who changes it.",
        ],
        "further": [
            "The Guardian — short opinion pieces by teachers.",
            "BBC News — *Have your say* columns.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"In my view, school should start later. Firstly, "
            "teenagers' biological clocks are different from "
            "adults'. Secondly, students who sleep more do better "
            "in school. On the other hand, many parents leave for "
            "work early. In conclusion, a thirty-minute later "
            "start would help most.\"\n\n"
            "1. Claim: ___ . 2. First reason: ___ . 3. Counter: "
            "___ . 4. Conclusion: ___ ."
        ),
        "exam_reading": (
            "Read the model text above. Answer.\n\n"
            "1. Main claim: ___ . 2. Two reasons: ___ . 3. "
            "Counter: ___ . 4. Final position: ___ ."
        ),
        "exam_use": (
            "**Insert the right signpost.**\n\n"
            "1. ___ , I think the rule is unfair. (opening)\n"
            "2. ___ , the teachers know the curriculum. (counter)\n"
            "3. ___ , a small say would be fair. (conclusion)\n"
            "4. ___ , students would read the book. (additional reason)"
        ),
        "exam_writing": (
            "Write 120 words: an opinion paragraph on a school "
            "topic. Use the four-move structure."
        ),
        "exam_keys": [
            "**T1.** school should start later, biological clocks, parents leave for work, 30 min later start.",
            "**T2.** pupils should help choose at least one book, more likely to read + more voices involved, teachers know curriculum better, small say (1 in 3) would be fair.",
            "**T3.** In my view / However / In conclusion / Secondly.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 7, "slug": "teen-magazine-mediation", "title": "Mediation: A Teen Magazine",
        "skills": ["mediation", "writing", "language_awareness"],
        "bp": [
            "3.2.1 Soziokulturelles Orientierungswissen / Themen",
            "3.2.3.5 Schreiben",
            "3.2.3.6 Sprachmittlung",
            "3.2.3.7 Verfügen über sprachliche Mittel – Wortschatz",
        ],
        "objectives": [
            "I can mediate a German teen-magazine article into 5–6 English sentences for a peer.",
            "I can keep dates, advice, and key facts; drop ceremony and decorative phrasing.",
            "I can use 5 reporting verbs (says, explains, advises, warns, recommends).",
        ],
        "leadin": (
            "Jonas's German cousin sent him a teen-magazine article "
            "about phone use at night. Jonas's English-speaking "
            "pen-pal had asked: *what do German teen mags say about "
            "this?* Jonas read the article twice. Then he closed it "
            "and wrote five English sentences from memory."
        ),
        "activate": (
            "**Drop or keep?** Slide shows five lines from a "
            "German article. With your partner, mark each as "
            "*essential / paraphrase / drop* depending on the "
            "addressee."
        ),
        "input_blocks": [
            ("Source — *German teen-mag article (excerpt)*",
             "*Studien zeigen, dass Jugendliche, die ihr Handy "
             "nachts neben dem Bett liegen haben, im Schnitt 30 "
             "Minuten weniger schlafen als ihre Mitschüler. "
             "Experten empfehlen, das Gerät außerhalb des "
             "Schlafzimmers zu laden. Eltern sollten dabei mit "
             "gutem Beispiel vorangehen.*"),
            ("Mediation — three rules",
             "1. *Who is reading?* — adjust greeting and tone.\n"
             "2. *What do they need to know?* — keep facts, "
             "drop decoration.\n"
             "3. *What is the smallest version that gets them "
             "there?*"),
            ("Reporting verbs",
             "*to say, to explain, to advise (someone to), to "
             "recommend, to warn (someone about), to mention, to "
             "claim, to point out.*\n"
             "- *Studies show that …*\n"
             "- *Experts recommend that …*\n"
             "- *Parents are advised to …*"),
        ],
        "practise_g": [
            "1. Match German verb to English: *empfehlen — ?, "
            "warnen — ?, erklären — ?, behaupten — ?*.",
            "2. Choose: *say / explain / recommend* — Studies "
            "__________ that teens lose sleep. Experts __________ "
            "that the phone be charged outside the bedroom.",
        ],
        "practise_m": [
            "3. Build a 4-sentence English mediation of the "
            "source article above for an English-speaking friend.",
        ],
        "answer_g": (
            "1. recommend / warn / explain / claim.\n"
            "2. show or say / recommend."
        ),
        "answer_m": "3. Open. Sample: *A German teen magazine "
                    "reports that teens who keep their phones by "
                    "the bed sleep about 30 minutes less than "
                    "others. Experts recommend charging phones "
                    "outside the bedroom. Parents are advised to "
                    "set the example.*",
        "produce": (
            "**Mediation, 6 sentences.** Read the German source "
            "above. Write 6 English sentences for an English-"
            "speaking friend who has asked what the article says. "
            "Use 3 reporting verbs."
        ),
        "produce_sample": (
            "*Hi Jordan, here's the gist of that German article. "
            "It says that teenagers who keep their phones next to "
            "the bed sleep about 30 minutes less on average than "
            "those who don't. Experts recommend charging the phone "
            "outside the bedroom. Parents are advised to set the "
            "example. The article also points out that this is not "
            "about willpower — it's about how the brain reacts to "
            "screens at night.*"
        ),
        "reflect": [
            "I can mediate a German article into 6 English sentences.",
            "I can keep facts and drop decoration.",
            "I can use 3 reporting verbs.",
        ],
        "pitfalls": [
            "Literal translation kills mediation. Reward "
            "addressee-fit.",
            "Carrying over German salutations into a peer message.",
            "*recommend to do* (informal) is increasingly used; "
            "*recommend that someone do* is more formal.",
        ],
        "further": [
            "Goethe-Institut — Beispiel-Aufgaben Sprachmittlung "
            "Englisch (Sek I).",
            "Landesbildungsserver BW — Mediation-Beispielaufgaben.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"Studien zeigen, dass Jugendliche, die ihr Handy "
            "nachts neben dem Bett liegen haben, weniger schlafen. "
            "Experten empfehlen, das Gerät außerhalb des "
            "Schlafzimmers zu laden.\"\n\n"
            "1. Topic: ___ . 2. Effect: ___ . 3. Expert advice: "
            "___ . 4. Source-language: ___ ."
        ),
        "exam_reading": (
            "Read the German source above. Answer in English.\n\n"
            "1. The study finding (one sentence). 2. The expert "
            "recommendation. 3. The role of parents. 4. The "
            "addressee of the article."
        ),
        "exam_use": (
            "**Reporting-verb fill-in.**\n\n"
            "1. The article __________ that teens lose sleep. (says)\n"
            "2. Experts __________ charging the phone elsewhere. (recommend)\n"
            "3. Parents __________ to set the example. (are advised)\n"
            "4. The author __________ that this is not about "
            "willpower. (points out)"
        ),
        "exam_writing": (
            "Mediate: write 5 English sentences from the German "
            "source for a peer. Use 3 reporting verbs."
        ),
        "exam_keys": [
            "**T1.** phones at night, less sleep (about 30 min), charge phone outside bedroom, German.",
            "**T2.** Teens with phones by the bed sleep about 30 min less. Experts recommend charging phones outside the bedroom. Parents are advised to set the example. Addressed to teens (and parents).",
            "**T3.** says / recommend / are advised / points out.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 8, "slug": "music-and-belonging", "title": "Music and Belonging",
        "skills": ["listening", "speaking", "intercultural"],
        "bp": [
            "3.2.1 Soziokulturelles Orientierungswissen / Themen",
            "3.2.2 Interkulturelle kommunikative Kompetenz",
            "3.2.3.1 Hör-/Hörsehverstehen",
            "3.2.3.3 Sprechen – an Gesprächen teilnehmen",
        ],
        "objectives": [
            "I can describe a piece of music in 5 sentences (genre, mood, instruments, association).",
            "I can use modals of possibility (*might / could / may / must*).",
            "I can hold a 90-second conversation about a song.",
        ],
        "leadin": (
            "Hawa is preparing a class playlist. The rule: each "
            "song must mean *belonging* in some way. Jonas chose "
            "an Icelandic instrumental that sounds like wind. Hawa "
            "chose a Yoruba song her grandmother sings. Mr. Ade, "
            "uninvited, contributed a 1980s German pop song that "
            "no one had asked for. He smiled. \"Belonging,\" he "
            "said, \"is sometimes a guilty pleasure.\""
        ),
        "activate": (
            "**Mood scan.** Teacher plays 30 seconds of three "
            "tracks. For each one, write one mood word and one "
            "instrument."
        ),
        "input_blocks": [
            ("Vocabulary — music",
             "*genre, beat, rhythm, lyrics, melody, harmony, "
             "verse, chorus, bridge, solo, instrumental, "
             "acoustic, electric, bass, drums, percussion, "
             "vocals, hook, fade out.*"),
            ("Grammar — modals of possibility",
             "*might / may / could* — possible: *This might be a "
             "Bollywood film score.*\n"
             "*must* — strongly likely: *That **must** be your "
             "grandmother's voice.*\n"
             "*can't* — strongly unlikely: *That **can't** be live "
             "— it's too clean.*"),
        ],
        "practise_g": [
            "1. Choose: *might / must / can't*: That voice "
            "__________ be Mariah Carey. The track __________ be "
            "by Adele — it sounds different. The drum __________ "
            "be a real drum.",
            "2. Match: instrumental → no vocals; chorus → repeated "
            "section. (T / F)",
        ],
        "practise_m": [
            "3. Build 4 sentences about a track using each modal "
            "(might / could / must / can't).",
        ],
        "answer_g": (
            "1. might (or could) / can't / could.\n"
            "2. all true."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Pair speaking — *One Song That Means Home*.** 90 "
            "sec each. Cover: title (or theme), genre, instrument, "
            "association, why it means belonging. Use 1 modal of "
            "possibility."
        ),
        "produce_sample": (
            "*— My song is in Yoruba — my grandmother sings it. It "
            "must be at least fifty years old. There's a small "
            "drum and her voice. It might mean nothing to anyone "
            "else, but for me it is the sound of Sunday afternoons.*"
        ),
        "reflect": [
            "I can describe a piece of music in 5 sentences.",
            "I can use modals of possibility correctly.",
            "I can hold a 90-second song-conversation.",
        ],
        "pitfalls": [
            "*That can be Mariah* (= permission) vs. *That could "
            "be Mariah* (= possibility) — easy mix-up.",
            "*music* is uncountable: *a music* → ✗ / *some music* → ✓.",
            "Stereotype check: don't reduce a country to one genre.",
        ],
        "further": [
            "BBC Sounds — playlists by genre.",
            "NPR Music — *Tiny Desk* concerts (free).",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"This song could be by Adele — it has the same "
            "kind of voice. But the chorus is different, so it "
            "might be someone newer. The drum sounds programmed "
            "rather than live, which means it can't be a stripped-"
            "back acoustic version.\"\n\n"
            "1. Could be by: ___ . 2. Why uncertain: ___ . 3. "
            "Might be: ___ . 4. Drum: ___ ."
        ),
        "exam_reading": (
            "Read.\n\n"
            "> \"My favourite song must be the one my grandmother "
            "sings every Sunday. It might be 50 years old, or it "
            "could be older — no one in the family is sure. There "
            "is a small drum and her voice. It can't be heard on "
            "any streaming app.\"\n\n"
            "1. Favourite: ___ . 2. Age: ___ . 3. Sounds: ___ . "
            "4. Streaming: ___ ."
        ),
        "exam_use": (
            "**Modal of possibility.**\n\n"
            "1. That voice __________ be Mariah Carey. (might)\n"
            "2. That __________ be live — too clean. (can't)\n"
            "3. The drum __________ be a real drum. (could)\n"
            "4. That singer __________ be German. (must — listen to the language)"
        ),
        "exam_writing": (
            "Write 120 words about one song that means belonging "
            "to you. Use 3 modals of possibility."
        ),
        "exam_keys": [
            "**T1.** Adele, chorus is different, someone newer, programmed (not live).",
            "**T2.** the song her grandmother sings; might be 50 years old or older; small drum + her voice; not on streaming.",
            "**T3.** might / can't / could / must.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 9, "slug": "rural-and-urban", "title": "Rural and Urban Lives",
        "skills": ["reading", "writing", "intercultural"],
        "bp": [
            "3.2.1 Soziokulturelles Orientierungswissen / Themen",
            "3.2.2 Interkulturelle kommunikative Kompetenz",
            "3.2.3.2 Leseverstehen",
            "3.2.3.5 Schreiben",
            "3.2.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can compare rural and urban life using 5 paired terms.",
            "I can use *as … as / not as … as* and superlatives in comparisons.",
            "I can write a 120-word balanced comparison of two places.",
        ],
        "leadin": (
            "Jonas spent a week with his uncle on a farm outside "
            "Stuttgart. The cows were less interested in him than "
            "he was in them. The internet was unreliable. The "
            "stars at night were noisier in their silence than the "
            "city ever managed in its noise. By Friday, Jonas was "
            "writing in a notebook, which surprised everyone."
        ),
        "activate": (
            "**Two columns.** *Rural / Urban*. Class fills in 5 "
            "associations under each."
        ),
        "input_blocks": [
            ("Reading — *A week on a farm*",
             "*The cows were less interested in me than I was in "
             "them. The internet was as unreliable as the weather "
             "forecast. The night was the loudest silence I had "
             "ever heard. By the second day I had stopped checking "
             "my phone, partly because it didn't work and partly "
             "because the stars were doing better.*"),
            ("Grammar — *as … as / not as … as*",
             "- *The countryside is **as quiet as** I remembered.*\n"
             "- *The internet is **not as reliable as** in the "
             "city.*\n"
             "- *Cows are **not as friendly as** dogs.*"),
            ("Vocabulary — rural vs. urban",
             "*Rural:* farm, field, barn, livestock, dirt road, "
             "local shop, neighbour, tractor.\n"
             "*Urban:* skyscraper, traffic, public transport, "
             "anonymity, takeaway, signal, neon, pace."),
        ],
        "practise_g": [
            "1. Build *as … as*: *(the village / quiet / the "
            "library)* → ___ ; *(this internet / fast / yours)* → "
            "___ .",
            "2. Match rural ↔ urban: tractor ↔ ?, field ↔ ?, "
            "neighbour ↔ ?, livestock ↔ ?",
        ],
        "practise_m": [
            "3. Build 4 *as … as / not as … as* sentences "
            "comparing your home town with another place.",
        ],
        "answer_g": (
            "1. *The village is as quiet as the library. This "
            "internet is not as fast as yours.*\n"
            "2. tractor↔car/bus, field↔skyscraper, "
            "neighbour↔stranger, livestock↔people."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Comparison, 120 words.** Write a balanced "
            "comparison of a rural and an urban place. Use 4 "
            "*as … as / not as … as* and 1 superlative."
        ),
        "produce_sample": (
            "*The village where my uncle lives is not as fast as "
            "Stuttgart, but it is as alive — just on a different "
            "scale. The stars at night are the loudest silence I "
            "have ever experienced. The internet is not as "
            "reliable as in the city, which means people actually "
            "look at each other while they speak. The local shop "
            "is the smallest building I know, but it sells "
            "everything I need plus a few things I didn't know "
            "existed.*"
        ),
        "reflect": [
            "I can compare rural and urban life with 5 paired "
            "terms.",
            "I can use *as … as / not as … as*.",
            "I can write a balanced 120-word comparison.",
        ],
        "pitfalls": [
            "*as quiet than* → ✗ / *as quiet as* → ✓.",
            "*not so quiet as* (older form) → acceptable but less "
            "common; prefer *not as … as*.",
            "Stereotype check: rural ≠ boring; urban ≠ exciting.",
        ],
        "further": [
            "BBC Countryfile — accessible articles.",
            "The Guardian — *Cities* section.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"My grandmother lives in a small village. The "
            "internet is not as reliable as in the city. The local "
            "shop sells almost everything but is not as cheap as a "
            "big supermarket. The night is as quiet as a library.\"\n\n"
            "1. Internet: ___ . 2. Shop: ___ . 3. Night: ___ . 4. "
            "Compared with city / supermarket / library: ___ ."
        ),
        "exam_reading": (
            "Read the *A week on a farm* extract above.\n\n"
            "1. Cows: ___ . 2. Internet: ___ . 3. Night: ___ . 4. "
            "Phone: ___ ."
        ),
        "exam_use": (
            "**Build *as … as / not as … as*.**\n\n"
            "1. The village / quiet / the library → ___\n"
            "2. The internet / not / fast / yours → ___\n"
            "3. The stars / loud / city traffic → ___\n"
            "4. Cows / not / friendly / dogs → ___"
        ),
        "exam_writing": (
            "Write 120 words: a balanced comparison of one rural "
            "place and one urban place you know."
        ),
        "exam_keys": [
            "**T1.** not as reliable as city, sells almost everything but not as cheap as a supermarket, as quiet as a library.",
            "**T2.** less interested in me than I was in them; as unreliable as weather forecast; loudest silence ever; stopped checking it.",
            "**T3.** *The village is as quiet as the library. The internet is not as fast as yours. The stars are as loud as city traffic. Cows are not as friendly as dogs.*",
            "**T4.** Open.",
        ],
    },
    {
        "n": 10, "slug": "a-novella-in-class", "title": "A Novella in Class",
        "skills": ["reading", "writing", "language_awareness"],
        "bp": [
            "3.2.1 Soziokulturelles Orientierungswissen / Themen",
            "3.2.3.2 Leseverstehen",
            "3.2.3.5 Schreiben",
            "3.2.3.8 Verfügen über sprachliche Mittel – Grammatik",
            "3.2.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can read a chapter extract and identify protagonist, conflict, and theme.",
            "I can use direct → reported speech (statements and questions).",
            "I can write a 150-word reading-journal entry.",
        ],
        "leadin": (
            "Mr. Ade started the term with a thin novella: *The "
            "Library of Almost-Found Things* (an original — not a "
            "real-world title). Each chapter is six pages. The "
            "class is reading one chapter per week. The protagonist "
            "is a girl named June who keeps a notebook of *things "
            "she almost found*. Hawa says, \"This is suspiciously "
            "specific. I think Mr. Ade has lost something.\""
        ),
        "activate": (
            "**Predict.** First sentence on the slide: *On the "
            "Tuesday June found the umbrella, she had already lost "
            "two other things.* With your partner, predict three "
            "things the chapter will involve."
        ),
        "input_blocks": [
            ("Reading — *Chapter 1, opening*",
             "*On the Tuesday June found the umbrella, she had "
             "already lost two other things. The first was a "
             "library book she could no longer remember the title "
             "of. The second was the courage to ask Mr. Owen what "
             "had happened to her grandmother's letters. The "
             "umbrella, by comparison, was small. But it had her "
             "grandmother's initials on the handle, and June had "
             "looked for it for three years.*"),
            ("Grammar — direct → reported speech",
             "**Statements** — backshift the tense:\n"
             "- *\"I found it,\" she said.* → *She said (that) "
             "she had found it.*\n"
             "- *\"I'm tired.\"* → *She said she was tired.*\n\n"
             "**Questions** — change to statement order, use "
             "*if/whether* for yes/no:\n"
             "- *\"Where is it?\"* → *He asked where it was.*\n"
             "- *\"Did you see it?\"* → *He asked if I had seen "
             "it.*"),
        ],
        "practise_g": [
            "1. Direct → reported (statement): *\"I found the "
            "umbrella,\" she said.* → ___ .",
            "2. Direct → reported (Q): *\"Where is the "
            "library?\"* → ___ .",
        ],
        "practise_m": [
            "3. Build 4 reported sentences (2 statements + 2 "
            "questions) from a chapter scene.",
        ],
        "answer_g": (
            "1. *She said she had found the umbrella.*\n"
            "2. *He asked where the library was.*"
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Reading-journal entry, 150 words.** After reading "
            "Chapter 1, write a journal entry: *one quote*, *one "
            "question I have*, *one prediction*, *one personal "
            "connection*. Use one direct quote and one reported "
            "version of a character's question."
        ),
        "produce_sample": (
            "*One sentence in this chapter stays with me: \"The "
            "umbrella, by comparison, was small.\" June seems to "
            "compare every object to her bigger losses, which is "
            "both touching and a bit sad. I wonder why Mr. Owen "
            "kept her grandmother's letters in the first place. "
            "He asked June if she remembered the title of the "
            "lost library book; she didn't. I predict the title "
            "will return at the end of the book and explain "
            "everything. My personal connection: I once spent two "
            "weeks looking for a single sock and never found it.*"
        ),
        "reflect": [
            "I can identify protagonist, conflict, theme.",
            "I can convert direct ↔ reported speech.",
            "I can write a 150-word reading-journal entry.",
        ],
        "pitfalls": [
            "Forgetting backshift: *\"I am tired\" → He said he is "
            "tired* → ✗ / *was tired* → ✓.",
            "Question word order: *He asked where was it* → ✗ / "
            "*where it was* → ✓.",
            "Pronoun shift: *I → he/she/I* depending on speaker.",
        ],
        "further": [
            "Project Gutenberg — short novellas at A2/B1 level.",
            "BBC Bitesize — *Reported speech* practice.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"After Chapter 1, the teacher said that June had "
            "lost two things. He explained that the umbrella was "
            "the smallest of her losses. He asked the class if "
            "they could remember the last thing they had lost.\"\n\n"
            "1. Said: ___ . 2. Explained: ___ . 3. Asked: ___ . "
            "4. Form of reported question: ___ ."
        ),
        "exam_reading": (
            "Read the *Chapter 1, opening* extract above.\n\n"
            "1. Two losses: ___ . 2. Why is the umbrella small "
            "*by comparison*? ___ . 3. What is on the handle? "
            "___ . 4. How long has she looked? ___ ."
        ),
        "exam_use": (
            "**Direct → reported.**\n\n"
            "1. \"I found the umbrella,\" she said. → ___\n"
            "2. \"Where is the library?\" he asked. → ___\n"
            "3. \"Did you see it?\" she asked. → ___\n"
            "4. \"I am tired,\" June said. → ___"
        ),
        "exam_writing": (
            "Write 150 words: a reading-journal entry on Chapter "
            "1 (quote, question, prediction, personal connection)."
        ),
        "exam_keys": [
            "**T1.** June had lost two things, the umbrella was the smallest, if they could remember the last thing they had lost, *if* + statement order with backshift.",
            "**T2.** the library book and the courage to ask Mr. Owen; because the other two losses are bigger; her grandmother's initials; three years.",
            "**T3.** *She said (that) she had found the umbrella. He asked where the library was. She asked if I had seen it. June said (that) she was tired.*",
            "**T4.** Open.",
        ],
    },
    {
        "n": 11, "slug": "public-speaking", "title": "Public Speaking: A Short Talk",
        "skills": ["speaking", "listening", "language_awareness"],
        "bp": [
            "3.2.1 Soziokulturelles Orientierungswissen / Themen",
            "3.2.3.1 Hör-/Hörsehverstehen",
            "3.2.3.4 Sprechen – zusammenhängendes monologisches Sprechen",
            "3.2.3.7 Verfügen über sprachliche Mittel – Wortschatz",
        ],
        "objectives": [
            "I can deliver a 2-minute monologue with three movements (hook, body, close).",
            "I can use signposting phrases for spoken English.",
            "I can listen to a peer's talk and give one specific piece of feedback.",
        ],
        "leadin": (
            "Hawa is preparing a talk. The rule: two minutes, no "
            "slides, one object you bring with you. Hawa is "
            "bringing a small green spoon. Jonas is bringing a "
            "single cloud photo printed on paper. Mr. Ade is "
            "bringing a calmly worried face, which he has done "
            "before."
        ),
        "activate": (
            "**Hook scan.** Listen to three first lines from "
            "different talks. Which one would you keep listening "
            "to? Why?"
        ),
        "input_blocks": [
            ("Structure — three movements",
             "1. **Hook** (15 sec): a question, a small object, "
             "a strong sentence.\n"
             "2. **Body** (90 sec): three short points, each "
             "with one specific example.\n"
             "3. **Close** (15 sec): a sentence the audience can "
             "carry out of the room."),
            ("Signposts for spoken English",
             "*Today I'd like to talk about … / Let me start "
             "with … / Firstly … Secondly … Lastly … / What "
             "this means is … / In short … / So, that's why I … / "
             "Thank you for listening.*"),
        ],
        "practise_g": [
            "1. Match: hook → grab attention; body → make 3 "
            "points; close → leave one idea.",
            "2. Choose a hook for *the importance of break time*: "
            "a question / a single object / a strong sentence.",
        ],
        "practise_m": [
            "3. Draft the bullets for your own 2-minute talk on "
            "a topic of your choice.",
        ],
        "answer_g": "1. correct. 2. open.",
        "answer_m": "3. Open.",
        "produce": (
            "**Class talks.** Each student delivers a 2-minute "
            "monologue with the three movements + one object. "
            "After every talk, one classmate gives feedback in "
            "one English sentence using *I noticed that … / "
            "What worked was … / One thing you could try is …*"
        ),
        "produce_sample": (
            "*This small green spoon belongs to my grandmother. "
            "She has stirred more meals with it than I have eaten "
            "in my life. Today I want to talk about three things "
            "small objects can do that big speeches cannot. "
            "Firstly, they remember things we forget. Secondly, "
            "they fit in pockets — they travel with us. Lastly, "
            "they are honest — a worn handle is a kind of "
            "biography. Thank you for listening.*"
        ),
        "reflect": [
            "I can deliver a 2-minute monologue with three "
            "movements.",
            "I can use 5 spoken-English signposts.",
            "I can give one specific piece of feedback in English.",
        ],
        "pitfalls": [
            "Reading word-for-word from a page → flat. Bullets "
            "only.",
            "Vague hooks (*Today I want to talk about an "
            "interesting topic*) → boring.",
            "Skipping the close → audience does not know it ended.",
        ],
        "further": [
            "TED-Ed — short student talks.",
            "BBC Sounds — *Short Cuts*.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"Today I'd like to talk about break time. Firstly, "
            "break time is when most school friendships actually "
            "happen. Secondly, it is when teachers see what kind of "
            "class they really have. Lastly, it is the only time "
            "that doesn't have a goal. So in short, break time "
            "matters more than the timetable suggests. Thank you for "
            "listening.\"\n\n"
            "1. Topic: ___ . 2. Three points: ___ . 3. Closing: "
            "___ . 4. Sign-off: ___ ."
        ),
        "exam_reading": (
            "Read the sample monologue above. Answer.\n\n"
            "1. Hook: ___ . 2. Three points: ___ . 3. Object: "
            "___ . 4. Closing: ___ ."
        ),
        "exam_use": (
            "**Insert the right signpost.**\n\n"
            "1. ___ I'd like to talk about my favourite teacher.\n"
            "2. ___ , break time matters.\n"
            "3. ___ , let me say something obvious.\n"
            "4. ___ for listening."
        ),
        "exam_writing": (
            "Write a 2-minute talk script (~150 words) using the "
            "three movements + one object."
        ),
        "exam_keys": [
            "**T1.** break time, friendships happen / teachers see real class / no goal, *break time matters more than timetable suggests*, Thank you for listening.",
            "**T2.** the green spoon belongs to grandmother; small objects remember / fit in pockets / are honest; the spoon; *Thank you for listening*.",
            "**T3.** Today / In short / Firstly / Thank you.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 12, "slug": "school-magazine-issue", "title": "Class Magazine Issue",
        "skills": ["writing", "speaking", "language_awareness"],
        "bp": [
            "3.2.1 Soziokulturelles Orientierungswissen / Themen",
            "3.2.3.4 Sprechen – zusammenhängendes monologisches Sprechen",
            "3.2.3.5 Schreiben",
            "3.2.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can plan and write a 150-word article for a class magazine.",
            "I can use grammar from the year (passive, second conditional, relative clauses, present perfect).",
            "I can edit a peer's article using a simple checklist.",
        ],
        "leadin": (
            "The class is producing a one-issue magazine. Six "
            "pages. Six articles. Each student is responsible for "
            "one piece (~150 words) plus one piece of feedback on "
            "a peer's article. Hawa is writing about the canteen. "
            "Jonas is writing about the lost-property cupboard, "
            "which he claims has its own ecosystem."
        ),
        "activate": (
            "**Pitch in 30 seconds.** With your partner, pitch "
            "your article: title + one sentence. The partner says "
            "*yes / no / not yet*."
        ),
        "input_blocks": [
            ("Article structure",
             "1. **Headline** — short, sharp.\n"
             "2. **Lead** — one sentence that says *what / who / "
             "why now*.\n"
             "3. **Body** (3 short paragraphs): a fact, a "
             "story-detail, a quote.\n"
             "4. **Close** — one line that lands."),
            ("Editing checklist",
             "- Headline under 8 words?\n"
             "- One specific detail in the lead?\n"
             "- At least one quote?\n"
             "- Tense consistent within paragraphs?\n"
             "- One mistake-prone area checked (passive forms / "
             "past simple irregulars / relative pronouns)?"),
        ],
        "practise_g": [
            "1. Match headline → article: *Lost-Property Cupboard "
            "Has Its Own Ecosystem* — A. lost things B. canteen "
            "C. school trip.",
            "2. Build a 1-sentence lead for *the new canteen "
            "rules*.",
        ],
        "practise_m": [
            "3. Build a 3-paragraph body for an article of your "
            "choice. Include one quote.",
        ],
        "answer_g": (
            "1. A.\n"
            "2. *The canteen has new rules from Monday — and "
            "they are not what you expected.*"
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Article, 150 words.** Pick one topic from class "
            "life. Use 4 grammar points from the year (e.g. "
            "passive, relative clause, present perfect, contrast "
            "connective). Swap with a partner; edit using the "
            "checklist; rewrite."
        ),
        "produce_sample": (
            "**The Canteen That Almost Worked**\n\n"
            "*The new canteen rules, which were introduced on "
            "Monday, have already changed how lunch feels. Plates "
            "are now distributed in a single line. Drinks are "
            "served from a separate counter. Although the queue "
            "is shorter, several students have complained that "
            "the system removes the pause that used to be the "
            "lunch's best part. \"It's faster, but I miss the "
            "chat,\" said one Klasse-8 student. The headteacher "
            "has agreed to review the rules in two weeks. In the "
            "meantime, lunch is a slightly different experience. "
            "If anyone has missed the old slow line, the next two "
            "weeks are the time to say so.*"
        ),
        "reflect": [
            "I can write a 150-word article with a clear "
            "structure.",
            "I can use 4 grammar points in one piece.",
            "I can edit a peer's article using a checklist.",
        ],
        "pitfalls": [
            "Burying the lead under a long opening.",
            "No quotes → reads like an essay.",
            "Inconsistent tense within a paragraph.",
        ],
        "further": [
            "BBC News — student journalism collection.",
            "The Guardian — school-magazine writing tips.",
        ],
        "exam_listening": (
            "Listen twice to a short editorial meeting.\n\n"
            "> \"Hawa's article on the canteen is clear, but the "
            "lead is too long. If she shortened it, the piece "
            "would feel tighter. Jonas's piece on the lost-"
            "property cupboard, which is genuinely funny, needs "
            "one more quote. Both pieces should run on the same "
            "page.\"\n\n"
            "1. Hawa's issue: ___ . 2. Editor's advice: ___ . 3. "
            "Jonas's strength: ___ . 4. Layout: ___ ."
        ),
        "exam_reading": (
            "Read the *Canteen That Almost Worked* article above. "
            "Answer.\n\n"
            "1. When did the rules start? 2. Two changes. 3. The "
            "complaint. 4. The headteacher's response."
        ),
        "exam_use": (
            "**Mixed-grammar review.**\n\n"
            "1. The new rules __________ (introduce / passive) on "
            "Monday.\n"
            "2. The student __________ (complain) said it removed "
            "the pause.\n"
            "3. If the system __________ (be) different, lunch "
            "__________ (feel) better.\n"
            "4. The headteacher __________ (already / agree) to "
            "review the rules."
        ),
        "exam_writing": (
            "Write a 150-word class-magazine article on a topic "
            "of your choice. Use 4 grammar points from the year."
        ),
        "exam_keys": [
            "**T1.** lead is too long, shorten it (would feel tighter), genuinely funny, on the same page.",
            "**T2.** Monday; plates in single line, drinks from separate counter; the system removes the pause that was lunch's best part; agreed to review in two weeks.",
            "**T3.** were introduced / who complained / were / would feel / has already agreed.",
            "**T4.** Open.",
        ],
    },
]


UNIT_TPL = """---
title: "Unit {n} — {title}"
subtitle: "Track G+M · Klasse 8 · Niveau G/M"
niveau: "G+M"
klassenstufe: 8
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

**Differentiation.** Niveau G: extra scaffolding card with the
key structure. Above Niveau M: extension prompt linking to the
next Unit.
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
subtitle: "Track G+M · Klasse 8 · Niveau M · 45 Minuten"
author: "S. Le Boulanger"
niveau: "M"
klassenstufe: 8
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

**Track G+M · Klasse 8 · Niveau M · 45 Minuten**

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

    print(f"Wrote {len(UNITS) * 3} files for Track G+M Klasse 8.")


if __name__ == "__main__":
    emit()
