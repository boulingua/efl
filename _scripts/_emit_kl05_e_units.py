"""Batch-emit Track E Klasse 5 — all 12 Units.

Niveau E version of Klasse 5: same theme arc as G+M (the BW Sek I
Bildungsplan groups Kl. 5/6 into one Klassenstufenband, so the
codes are shared), but the texts are slightly longer and the
grammar carries one extra nuance per Unit. Cast unchanged: Mia,
Theo, Frida the fox, Mr. Flint.
"""
from __future__ import annotations
import pathlib

REPO = pathlib.Path(__file__).resolve().parent.parent
COURSE = REPO / "track_e_kl05" / "units"

UNITS = [
    {
        "n": 1,
        "slug": "hello-world",
        "title": "Hello World",
        "skills": ["speaking", "listening", "language_awareness"],
        "bp": [
            "3.1.1 Soziokulturelles Orientierungswissen / Themen",
            "3.1.3.3 Sprechen – an Gesprächen teilnehmen",
            "3.1.3.5 Schreiben",
            "3.1.3.8 Verfügen über sprachliche Mittel – Grammatik",
        ],
        "objectives": [
            "I can introduce myself with name, age, town, and one detail.",
            "I can ask a partner four questions and report what they said.",
            "I can use *to be* and *to have* in short sentences.",
        ],
        "leadin": (
            "Mia stands at the door of Klasse 5e. The room is "
            "freshly painted. Theo sits in the back row, swinging "
            "his feet. A small red fox is sitting on the windowsill "
            "— which is unusual. The fox waves. Mia hesitates, "
            "then waves back. \"Hello,\" the fox says. \"My name "
            "is Frida. I'm here to learn English with you. Foxes "
            "need second languages too.\""
        ),
        "activate": (
            "**Mingle and report.** Walk around for two minutes. "
            "Find three new classmates. Ask name, age, and one "
            "thing they like. Be ready to report one classmate to "
            "the class."
        ),
        "input_blocks": [
            ("Vocabulary — meeting people",
             "*Hello, hi, good morning, good afternoon, good "
             "evening, goodbye, see you later, please, thank you, "
             "you're welcome, nice to meet you, how do you do, "
             "what's your name, where are you from.*"),
            ("Grammar — *to be* + *to have*",
             "**to be** (am / is / are):\n"
             "- *I am Mia. She is my friend. We are in Klasse 5.*\n\n"
             "**to have**: in BrE often *have got*; in AmE *have*:\n"
             "- *I have a brother.* / *I've got a brother.*\n"
             "- *Mia has a cat.* / *Mia's got a cat.*\n\n"
             "Questions and short answers:\n"
             "- *Are you from Stuttgart?* — *Yes, I am. / No, I'm not.*\n"
             "- *Do you have a brother?* — *Yes, I do. / No, I don't.*"),
            ("Reporting frame",
             "- *His name is …, He is …, He has …*\n"
             "- Use the third-person -s on regular verbs."),
        ],
        "practise_g": [
            "1. Fill in: I __________ ten years old. We __________ "
            "in Klasse 5e. Theo __________ a brother.",
            "2. Build the question: (your age?) → ___ ; (your town?) "
            "→ ___ .",
        ],
        "practise_m": [
            "3. Report sentence. *Lina: 'I am ten. I live in "
            "Stuttgart. I have one cat.'* → ___ ",
            "4. Build a 4-line dialogue between two new classmates.",
        ],
        "answer_g": (
            "1. am, are, has.\n"
            "2. *How old are you?* / *Where do you live?*"
        ),
        "answer_m": (
            "3. *Lina is ten. She lives in Stuttgart. She has one "
            "cat.*\n"
            "4. Open."
        ),
        "produce": (
            "**Class wall.** On a strip of paper, write 4 sentences "
            "about yourself: name, age, town, one true thing. "
            "Stick the strips on the class wall in a long line."
        ),
        "produce_sample": (
            "*Hello, I'm Mia. I am ten years old. I live in "
            "Stuttgart. I have a cat called Pepper.*"
        ),
        "reflect": [
            "I can introduce myself with four facts.",
            "I can use *to be* and *to have*.",
            "I can report what a partner said using the third "
            "person.",
        ],
        "pitfalls": [
            "*I has a brother* → ✗ / *I have* → ✓.",
            "*She have a cat* → ✗ / *She has* → ✓.",
            "L1 trap: *Wie heißt du?* → *What is your name?* (not "
            "*how*).",
        ],
        "further": [
            "BBC Learning English — *Beginners*. <https://www.bbc.co.uk/learningenglish>",
            "British Council — *LearnEnglish Kids: Hello*. <https://learnenglishkids.britishcouncil.org>",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"Hi, my name is Lina. I am ten years old. I live in "
            "Stuttgart. I have one brother and a small dog. I love "
            "books and bike rides.\"\n\n"
            "1. Name: ___ . 2. Age: ___ . 3. Town: ___ . "
            "4. One thing she has: ___ ."
        ),
        "exam_reading": (
            "Read.\n\n"
            "> \"Hi, I'm Theo. I am eleven. My favourite colour is "
            "blue. My best friend is Mia. We have a cat called "
            "Pepper. I play football on Saturdays.\"\n\n"
            "T or F: 1. Theo is twelve. 2. His best friend is Mia. "
            "3. He has a dog. 4. He plays football."
        ),
        "exam_use": (
            "**Fill in *am, is, are, have, has*.**\n\n"
            "1. I __________ ten. 2. Mia __________ a cat. "
            "3. We __________ in Klasse 5. 4. Theo __________ a "
            "football."
        ),
        "exam_writing": (
            "Write 5 sentences about yourself: name, age, town, "
            "one thing you have, one thing you like."
        ),
        "exam_keys": [
            "**T1.** Lina, 10, Stuttgart, brother / small dog.",
            "**T2.** F, T, F, T.",
            "**T3.** 1. am, 2. has, 3. are, 4. has.",
            "**T4.** Open. 1 BE per correct sentence + 1 BE language.",
        ],
    },
    {
        "n": 2,
        "slug": "my-family",
        "title": "My Family",
        "skills": ["speaking", "writing", "language_awareness"],
        "bp": [
            "3.1.1 Soziokulturelles Orientierungswissen / Themen",
            "3.1.3.5 Schreiben",
            "3.1.3.7 Verfügen über sprachliche Mittel – Wortschatz",
            "3.1.3.8 Verfügen über sprachliche Mittel – Grammatik",
        ],
        "objectives": [
            "I can name 12 family words including grandparents and cousins.",
            "I can use the possessive 's and the genitive of plural nouns.",
            "I can write a short text (5–7 sentences) about my family.",
        ],
        "leadin": (
            "Mia draws her family on paper. Mother — doctor. Father "
            "— works at home. Brother Theo — football. Pepper the "
            "cat. Then her two grandmothers, both alive, both "
            "stubborn. \"Don't forget your aunt in Hamburg,\" Theo "
            "says. Mia adds the aunt. Frida the fox watches from "
            "the window. \"My family,\" she says, \"is a lot of "
            "foxes in one den. None of us draw.\""
        ),
        "activate": (
            "**Family quick-tree.** Draw three boxes: parents, "
            "siblings, grandparents. Add names. Tell a partner who "
            "is the youngest, who is the oldest, and who lives "
            "closest."
        ),
        "input_blocks": [
            ("Vocabulary — extended family",
             "*mother, father, parents, sister, brother, "
             "siblings, grandmother, grandfather, grandparents, "
             "aunt, uncle, cousin, niece, nephew, stepmother, "
             "stepfather, half-brother, half-sister.*"),
            ("Grammar — possessive 's and plural genitive",
             "- *Mia's brother* — singular owner: *'s*.\n"
             "- *my parents' car* — plural ending in -s: just *'*.\n"
             "- *the children's room* — irregular plural: *'s*.\n"
             "- *the cat's name* (singular) vs. *the cats' names* "
             "(two cats)."),
        ],
        "practise_g": [
            "1. Match: parents — Eltern, sibling — Geschwister, "
            "cousin — Cousin, niece — Nichte. (T / F)",
            "2. Build the possessive: (Mia / brother) → ___ ; (the "
            "cats / food) → ___ .",
        ],
        "practise_m": [
            "3. Family description. Use 5 sentences with at least "
            "two possessives.",
            "4. *(my grandmother / house)*, *(the children / "
            "playground)*, *(my friends / parents)* — write each "
            "as a possessive phrase.",
        ],
        "answer_g": "1. all true. 2. *Mia's brother*, *the cats' food*.",
        "answer_m": (
            "3. Open.\n"
            "4. *my grandmother's house*, *the children's "
            "playground*, *my friends' parents*."
        ),
        "produce": (
            "**Family poster.** A4 paper. Draw five family "
            "members. Underneath, write five sentences using two "
            "possessives and one *to be* sentence."
        ),
        "produce_sample": (
            "*This is my family. My mother's name is Petra. She is "
            "a doctor. My grandparents' house is in Heidelberg. My "
            "brother Theo is eleven. We have a cat. The cat's name "
            "is Pepper.*"
        ),
        "reflect": [
            "I can name 12 family words.",
            "I can use possessive 's and plural -s'.",
            "I can write a 5-sentence family text.",
        ],
        "pitfalls": [
            "*the brother of Mia* — grammatical, but *Mia's "
            "brother* is more natural in English.",
            "*my parents's car* → ✗ / *my parents' car* → ✓.",
            "L1 trap: German *Geschwister* = English *siblings* (or "
            "*brothers and sisters*).",
        ],
        "further": [
            "BBC Learning English — *Family vocabulary*.",
            "LearnEnglish Kids — *Family Tree*.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"In my family there are five people. My parents, my "
            "brother, my grandmother, and me. My grandmother lives "
            "with us. My favourite cousin lives in Hamburg.\"\n\n"
            "1. How many people: ___ . 2. Who lives with the "
            "family: ___ . 3. Cousin's town: ___ . 4. Who: ___ ."
        ),
        "exam_reading": (
            "Read.\n\n"
            "> \"This is Mia's family. Her parents' names are Petra "
            "and Markus. Mia's brother is Theo. Their grandparents' "
            "house is in Heidelberg. The cat's name is Pepper.\"\n\n"
            "1. Mia's parents: ___ . 2. Brother: ___ . "
            "3. Grandparents' town: ___ . 4. Cat: ___ ."
        ),
        "exam_use": (
            "**Build the possessive.**\n\n"
            "1. (Theo / book) → ___\n"
            "2. (the cat / bed) → ___\n"
            "3. (my parents / friends) → ___\n"
            "4. (the children / room) → ___"
        ),
        "exam_writing": (
            "Write 5–6 sentences about your family. Use at least "
            "two possessives."
        ),
        "exam_keys": [
            "**T1.** 5, grandmother, Hamburg, cousin.",
            "**T2.** Petra and Markus, Theo, Heidelberg, Pepper.",
            "**T3.** *Theo's book; the cat's bed; my parents' "
            "friends; the children's room.*",
            "**T4.** Open.",
        ],
    },
    {
        "n": 3,
        "slug": "home-and-room",
        "title": "Home and My Room",
        "skills": ["reading", "writing", "language_awareness"],
        "bp": [
            "3.1.1 Soziokulturelles Orientierungswissen / Themen",
            "3.1.3.2 Leseverstehen",
            "3.1.3.5 Schreiben",
            "3.1.3.7 Verfügen über sprachliche Mittel – Wortschatz",
        ],
        "objectives": [
            "I can name 14 things in a room and four rooms in a house.",
            "I can use *there is / there are* in positive, negative, and questions.",
            "I can write 6 sentences describing my home or my room.",
        ],
        "leadin": (
            "Theo opens the front door. The hallway smells of bread "
            "and rain. To the right is the kitchen, with its loud "
            "fridge and quiet kettle. The living room has a large "
            "window onto the courtyard. Down the hall is Mia's "
            "bedroom — door always almost shut, never quite open. "
            "Frida the fox arrives at the back door, wet and "
            "polite. \"I won't go in,\" she says. \"I just like to "
            "be invited.\""
        ),
        "activate": (
            "**Room sketch.** Quick-draw your bedroom in 60 "
            "seconds. Mark four items: bed, desk, window, one "
            "personal thing. Show your partner."
        ),
        "input_blocks": [
            ("Vocabulary — house and room",
             "*Rooms:* bedroom, kitchen, living room, bathroom, "
             "hallway, dining room, basement, attic.\n"
             "*Furniture:* bed, desk, chair, sofa, armchair, table, "
             "wardrobe, bookshelf, lamp, mirror, rug, curtain.\n"
             "*Other:* window, door, ceiling, floor, wall, drawer, "
             "shelf."),
            ("Grammar — there is / there are (full toolkit)",
             "Positive:\n"
             "- *There is a bed.* / *There are two windows.*\n\n"
             "Negative:\n"
             "- *There isn't a TV.* / *There aren't any chairs.*\n\n"
             "Questions:\n"
             "- *Is there a desk?* / *Are there any plants?*\n"
             "- Short answers: *Yes, there is. / No, there isn't.*\n\n"
             "Quantifier note: *some* in positives; *any* in "
             "negatives and questions."),
            ("Prepositions of place",
             "*on, under, in, in front of, behind, between, next "
             "to, above, below, opposite.* Quick examples: *The "
             "lamp is on the desk. The shoes are under the bed. "
             "There is a poster opposite the window.*"),
        ],
        "practise_g": [
            "1. Fill in *is / are / isn't / aren't*: There __________ "
            "a bed. There __________ no chairs. __________ there a "
            "lamp?",
            "2. Choose *some / any*: There are __________ books on "
            "the shelf. There aren't __________ chairs.",
        ],
        "practise_m": [
            "3. Describe your kitchen in 4 sentences using *there "
            "is/are* + 2 prepositions.",
            "4. Write 3 questions a guest might ask: *Is there a …? "
            "Where is …? Are there …?*",
        ],
        "answer_g": (
            "1. is / are / Is.\n"
            "2. some / any."
        ),
        "answer_m": "3-4. Open; check structures.",
        "produce": (
            "**Pen-pal letter — *My Home*.** Write 6 sentences "
            "describing your home or your room to an English "
            "pen-pal. Use at least 3 *there is/are* sentences and "
            "2 prepositions."
        ),
        "produce_sample": (
            "*Hi James, this is my home. There is a small kitchen "
            "with a loud fridge. There are two bedrooms. My room is "
            "next to the bathroom. There is a desk under the window "
            "and a poster of a fox above the bed. There aren't any "
            "TVs in the house, but there is a piano in the living "
            "room.*"
        ),
        "reflect": [
            "I can name 14 room/home words.",
            "I can use *there is/are* in positive, negative, and questions.",
            "I can write a 6-sentence pen-pal letter about my home.",
        ],
        "pitfalls": [
            "*There is two beds* → ✗ / *There are two beds* → ✓.",
            "*some* in negatives sounds wrong: *There isn't some "
            "lamp* → *There isn't any lamp*.",
            "L1 trap: German *Es gibt* always → *there is/are*.",
        ],
        "further": [
            "BBC Learning English — *Around the house*.",
            "British Council — *My House* worksheets.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"In Mia's flat there are four rooms: a kitchen, a "
            "living room, and two bedrooms. Mia's room is small but "
            "bright. There is a desk under the window. There aren't "
            "any TVs.\"\n\n"
            "1. How many rooms: ___ . 2. Mia's room is ___ . "
            "3. The desk is ___ . 4. TV? ___ ."
        ),
        "exam_reading": (
            "Read about a small flat.\n\n"
            "> \"There are two bedrooms, one bathroom, and a "
            "kitchen with a window. There is no living room — the "
            "kitchen is also the dining room. There is a sofa in "
            "the bigger bedroom.\"\n\n"
            "T or F: 1. Two bedrooms. 2. One bathroom. 3. There is "
            "a living room. 4. The sofa is in the kitchen."
        ),
        "exam_use": (
            "**Fill in *there is/are*, positive or negative.**\n\n"
            "1. ___ a desk in my room. (positive)\n"
            "2. ___ any chairs in the bedroom. (negative)\n"
            "3. ___ two windows in the kitchen?\n"
            "4. ___ a lamp on the desk."
        ),
        "exam_writing": (
            "Write 6 sentences about your room or home to a "
            "pen-pal. Use *there is/are* and prepositions."
        ),
        "exam_keys": [
            "**T1.** 4, small / bright, under the window, no.",
            "**T2.** T, T, F, F.",
            "**T3.** 1. There is, 2. There aren't, 3. Are there, "
            "4. There is.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 4,
        "slug": "school-day",
        "title": "A School Day",
        "skills": ["listening", "speaking", "language_awareness"],
        "bp": [
            "3.1.1 Soziokulturelles Orientierungswissen / Themen",
            "3.1.3.1 Hör-/Hörsehverstehen",
            "3.1.3.3 Sprechen – an Gesprächen teilnehmen",
            "3.1.3.8 Verfügen über sprachliche Mittel – Grammatik",
        ],
        "objectives": [
            "I can name 10 school subjects.",
            "I can tell the time in 5-minute steps (quarter past, twenty to, etc.).",
            "I can hold a 90-second conversation about my school day using present simple.",
        ],
        "leadin": (
            "Mia's timetable is taped to the inside of her locker "
            "door. Monday: maths, German, English, biology, sport, "
            "music. The lockers are new this year. They click when "
            "they shut. Theo says the click is the best sound in "
            "the school. Frida the fox watches the lockers from "
            "the corridor. \"I would like a locker,\" she says. "
            "\"Foxes also need a private space.\""
        ),
        "activate": (
            "**Timetable cross-talk.** Pair up. Take 90 seconds. A "
            "asks B about Monday and Tuesday. B asks A about "
            "Wednesday and Thursday. Use *What do you have at … "
            "o'clock?*"
        ),
        "input_blocks": [
            ("Vocabulary — school subjects",
             "*English, German, French, Spanish, Maths, Biology, "
             "Physics, Chemistry, History, Geography, Religion, "
             "Ethics, Music, Art, PE / Sport, IT.*"),
            ("Telling the time — five-minute steps",
             "- *It's eight o'clock.* (8:00)\n"
             "- *It's five past eight.* (8:05)\n"
             "- *It's ten past eight.* (8:10)\n"
             "- *It's quarter past eight.* (8:15)\n"
             "- *It's twenty past eight.* (8:20)\n"
             "- *It's twenty-five past eight.* (8:25)\n"
             "- *It's half past eight.* (8:30)\n"
             "- *It's twenty-five to nine.* (8:35)\n"
             "- *It's twenty to nine.* (8:40)\n"
             "- *It's quarter to nine.* (8:45)\n"
             "- *It's ten to nine.* (8:50)\n"
             "- *It's five to nine.* (8:55)"),
            ("Grammar — present simple, all persons",
             "- I/you/we/they: base form. *I start at eight.*\n"
             "- he/she/it: base + *-s*. *Mia starts at eight.*\n"
             "- Negatives: *I don't / She doesn't + base verb.*\n"
             "- Questions: *Do you …? / Does she …?*"),
        ],
        "practise_g": [
            "1. Time: 9:15 → ___ ; 11:20 → ___ ; 14:45 → ___ .",
            "2. Verb form: I __________ (start), Mia __________ "
            "(start), We __________ (have), He __________ (do).",
        ],
        "practise_m": [
            "3. Build the question: (Tuesday / first lesson?) → ___ ; "
            "(your favourite subject — why?) → ___ .",
            "4. *Negative*: I don't / She doesn't — write three "
            "true negative sentences about your week.",
        ],
        "answer_g": (
            "1. *quarter past nine, twenty past eleven, quarter to "
            "three.*\n"
            "2. start, starts, have, does."
        ),
        "answer_m": "3-4. Open.",
        "produce": (
            "**Pair speaking — *My Week*.** 90 seconds each "
            "direction. Cover: start time, three subjects, one "
            "favourite, one you don't like, lunch time, end time."
        ),
        "produce_sample": (
            "*— What time do you start on Monday?*\n"
            "*— I start at quarter past eight. We have maths first, "
            "and I don't really like maths. After the break we "
            "have biology, which is my favourite.*"
        ),
        "reflect": [
            "I can name 10 school subjects.",
            "I can tell the time in 5-minute steps.",
            "I can hold a 90-second conversation about my school day.",
        ],
        "pitfalls": [
            "Forgetting the third-person -s with negatives and "
            "questions: *Does she has* → ✗ / *Does she have* → ✓.",
            "*half eight* (BrE colloquial = 8:30) sometimes confuses "
            "German learners; stick with *half past eight* in writing.",
            "L1 trap: *Wir haben Mathe* → *We have maths* (no "
            "preposition).",
        ],
        "further": [
            "BBC Learning English — *Telling the time*.",
            "LearnEnglish Kids — *School subjects* games.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"On Monday I start at quarter past eight. First "
            "I have German, then maths. After the long break we "
            "have English and music. I finish at twenty past one.\"\n\n"
            "1. Start: ___ . 2. First lesson: ___ . 3. Two lessons "
            "after the break: ___ . 4. Finish: ___ ."
        ),
        "exam_reading": (
            "Read.\n\n"
            "> \"Theo's favourite subject is biology because the "
            "teacher tells stories about animals. He doesn't like "
            "maths, but he is good at it. He has six lessons every "
            "day.\"\n\n"
            "1. Favourite: ___ . 2. Why: ___ . 3. Doesn't like: "
            "___ . 4. Lessons per day: ___ ."
        ),
        "exam_use": (
            "**Fill in present simple, positive or negative.**\n\n"
            "1. I __________ (have) maths on Monday.\n"
            "2. Mia __________ (not / like) PE.\n"
            "3. ___ they ___ (start) at eight?\n"
            "4. Mr Flint __________ (teach) English."
        ),
        "exam_writing": (
            "Write 5–6 sentences about your school day: start, "
            "two subjects, one favourite, one you don't like, end."
        ),
        "exam_keys": [
            "**T1.** 8:15, German, English / music, 13:20.",
            "**T2.** biology, animal stories, maths, six.",
            "**T3.** 1. have, 2. doesn't like, 3. Do … start, "
            "4. teaches.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 5,
        "slug": "food-and-drinks",
        "title": "Food and Drinks",
        "skills": ["reading", "speaking", "language_awareness"],
        "bp": [
            "3.1.1 Soziokulturelles Orientierungswissen / Themen",
            "3.1.3.2 Leseverstehen",
            "3.1.3.3 Sprechen – an Gesprächen teilnehmen",
            "3.1.3.7 Verfügen über sprachliche Mittel – Wortschatz",
        ],
        "objectives": [
            "I can name 15 foods and 8 drinks.",
            "I can hold a 1-minute cafe conversation politely.",
            "I can use countable vs. uncountable nouns with *a, some, any*.",
        ],
        "leadin": (
            "Frida the fox sits at a cafe table that is too tall "
            "for her. The waiter is professional. He does not "
            "comment on the fox. \"Good afternoon. What can I get "
            "you?\" Frida considers. \"A cup of tea, please. And a "
            "small piece of cake — preferably the kind with apple "
            "in it.\" Mia, at the next table, mouths *thank you* "
            "to the waiter for not laughing."
        ),
        "activate": (
            "**Food memory.** Close eyes; teacher names 8 foods "
            "(apple, bread, cheese, egg, fish, rice, tomato, "
            "chocolate). Open eyes. Write down as many as you "
            "remember in 30 seconds."
        ),
        "input_blocks": [
            ("Vocabulary — food and drink",
             "*Foods:* apple, banana, bread, butter, cheese, "
             "chicken, egg, fish, fruit, meat, pasta, potato, rice, "
             "salad, sausage, soup, tomato, chocolate, cake.\n"
             "*Drinks:* water, milk, tea, coffee, juice, lemonade, "
             "hot chocolate, smoothie."),
            ("Grammar — countable vs. uncountable",
             "**Countable** nouns can be plural and take *a/an*: "
             "*an apple, two apples, three sandwiches.*\n"
             "**Uncountable** nouns are singular and take no *a/an*: "
             "*water, milk, bread, cheese, rice.*\n\n"
             "With **uncountable** use *some* (positive), *any* "
             "(negative/question), or units (*a glass of, a piece of, "
             "a slice of, a cup of*):\n"
             "- *I'd like some milk, please.*\n"
             "- *Is there any bread?*\n"
             "- *A cup of tea, please. A slice of cheese.*"),
            ("Cafe phrases",
             "- *What can I get you?* / *I'd like …, please.*\n"
             "- *Anything else?* / *No, that's all, thanks.*\n"
             "- *That's £4.50.* / *Here you are.* / *Thank you, "
             "have a nice day.*"),
        ],
        "practise_g": [
            "1. *a / an / some / any?* ___ apple, ___ milk, ___ "
            "tomatoes, ___ rice, ___ bread.",
            "2. Match unit to noun: a slice of — ?, a cup of — ?, "
            "a glass of — ?",
        ],
        "practise_m": [
            "3. Build the cafe order: 1 hot chocolate, 1 piece of "
            "cake. → 4 polite lines.",
            "4. Negative + question forms: *Is there any …? Are "
            "there any …?* — write three.",
        ],
        "answer_g": (
            "1. *an apple, some milk, some tomatoes, some rice, "
            "some bread.*\n"
            "2. *slice — bread/cheese/cake; cup — tea/coffee/hot "
            "chocolate; glass — water/juice/milk.*"
        ),
        "answer_m": "3-4. Open; check polite forms.",
        "produce": (
            "**Cafe role-play (Niveau E).** In pairs, run a 1-minute "
            "cafe scene. Customer orders two items, one with a "
            "unit (*a glass of, a piece of, a cup of*). Waiter asks "
            "follow-up question. Use *please / thank you* in every "
            "turn."
        ),
        "produce_sample": (
            "*— Good afternoon, what can I get you?*\n"
            "*— I'd like a cup of tea and a slice of apple cake, "
            "please.*\n"
            "*— Anything else? A glass of water?*\n"
            "*— No, that's all. Thank you.*"
        ),
        "reflect": [
            "I can name 15 foods and 8 drinks.",
            "I can use *a/an, some, any* correctly.",
            "I can run a 1-minute cafe role-play.",
        ],
        "pitfalls": [
            "*a milk* → ✗ — milk is uncountable. *Some milk* or *a "
            "glass of milk*.",
            "*two breads* → unusual; prefer *two slices of bread*.",
            "L1 trap: German *Ich nehme einen Tee* → English *I'll "
            "have a tea / a cup of tea*.",
        ],
        "further": [
            "BBC Good Food — short recipe articles.",
            "British Council — *Food vocabulary* games.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"At the cafe Mia orders a hot chocolate and a slice "
            "of carrot cake. Theo orders a glass of water and a "
            "sandwich. The total is £6.\"\n\n"
            "1. Mia drink: ___ . 2. Mia food: ___ . 3. Theo "
            "drink: ___ . 4. Total: ___ ."
        ),
        "exam_reading": (
            "Read the menu and the order.\n\n"
            "> Menu: *Tea £1.50, Hot chocolate £2.50, Sandwich £3, "
            "Cake £2.50.* Order: *one tea, one hot chocolate, two "
            "sandwiches.*\n\n"
            "1. Number of items: ___ . 2. Total cost: ___ . 3. "
            "Cheapest item: ___ . 4. Drinks total: ___ ."
        ),
        "exam_use": (
            "**Fill in *a, an, some, any*.**\n\n"
            "1. ___ apple, 2. ___ rice, 3. Is there ___ milk? "
            "4. There aren't ___ tomatoes."
        ),
        "exam_writing": (
            "Write a 6-line cafe dialogue with two items ordered "
            "and polite phrases."
        ),
        "exam_keys": [
            "**T1.** hot chocolate, slice of carrot cake, glass of "
            "water, £6.",
            "**T2.** 4, £10, tea, £4.",
            "**T3.** an, some, any, any.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 6,
        "slug": "animals-and-pets",
        "title": "Animals and Pets",
        "skills": ["reading", "writing", "language_awareness"],
        "bp": [
            "3.1.1 Soziokulturelles Orientierungswissen / Themen",
            "3.1.3.2 Leseverstehen",
            "3.1.3.5 Schreiben",
            "3.1.3.7 Verfügen über sprachliche Mittel – Wortschatz",
            "3.1.3.8 Verfügen über sprachliche Mittel – Grammatik",
        ],
        "objectives": [
            "I can name 14 animals (pets, farm, wild).",
            "I can use *have got* and the present simple together to describe a pet.",
            "I can write 6 sentences about a real or imagined pet.",
        ],
        "leadin": (
            "Pepper the cat does three things: sleep, eat, ignore. "
            "He is excellent at all three. Mia has known him for "
            "six years. He has known her since the day she carried "
            "him home from the shelter in a small cardboard box. "
            "Frida the fox once tried to make friends with Pepper. "
            "Pepper looked at her for thirty seconds, then walked "
            "away. Friendship: not yet."
        ),
        "activate": (
            "**Animal sounds and habitats.** Teacher names an "
            "animal; class shouts the sound; one volunteer names a "
            "habitat (forest, farm, ocean, house)."
        ),
        "input_blocks": [
            ("Vocabulary — animals",
             "*Pets:* cat, dog, hamster, rabbit, fish, bird, snake, "
             "turtle, parrot.\n"
             "*Farm:* cow, horse, sheep, pig, chicken, duck, goat.\n"
             "*Wild:* fox, wolf, bear, deer, owl, frog, lizard, "
             "spider."),
            ("Grammar — *have got* + present simple together",
             "Use *have got* for possession; present simple for "
             "habits.\n\n"
             "- *Mia has got a cat. The cat sleeps a lot.*\n"
             "- *Theo has got a fish. The fish swims in circles.*\n\n"
             "Question patterns:\n"
             "- *Have you got a pet? — Yes, I have. / No, I haven't.*\n"
             "- *Does it bark? — Yes, it does. / No, it doesn't.*"),
        ],
        "practise_g": [
            "1. *Have got* — fill in: I __________ a hamster. Mia "
            "__________ a cat. Theo __________ a fish.",
            "2. Present simple: *the cat / sleep / a lot* → ___ ; "
            "*the dog / bark / at the door* → ___ .",
        ],
        "practise_m": [
            "3. *Pet portrait.* Write 4 sentences about your pet "
            "or an imagined pet (have got + present simple).",
            "4. Question forms: build *(you / a pet?)*, *(your "
            "rabbit / eat carrots?)*.",
        ],
        "answer_g": (
            "1. have got / has got / has got.\n"
            "2. *The cat sleeps a lot. The dog barks at the door.*"
        ),
        "answer_m": "3-4. Open; check structures.",
        "produce": (
            "**Pet portrait poster.** Draw on A4. Underneath, "
            "write 6 sentences using *have got* + present simple. "
            "Include name, age, colour, food, one habit, one "
            "feeling."
        ),
        "produce_sample": (
            "*This is Pepper. He is a grey cat. He has got soft "
            "fur and green eyes. He is six years old. He eats fish "
            "and dry food. He sleeps on my bed every afternoon. He "
            "doesn't like dogs.*"
        ),
        "reflect": [
            "I can name 14 animals.",
            "I can use *have got* + present simple in one text.",
            "I can write a 6-sentence pet portrait.",
        ],
        "pitfalls": [
            "*The cat have got* → ✗ / *The cat has got* → ✓.",
            "*Does the cat has* → ✗ / *Does the cat have* → ✓.",
            "L1 trap: German *Mein Hund hat …* → English *My dog "
            "has (got) …*, with a *to be* checked option (*My dog "
            "is …*).",
        ],
        "further": [
            "BBC Earth Kids — short animal videos.",
            "RSPB — UK bird identifier (visual). <https://www.rspb.org.uk>",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"My grandmother has got two cats and a small dog. "
            "The cats are grey and white. The dog is black with a "
            "white spot on his chest. He is six years old.\"\n\n"
            "1. How many cats: ___ . 2. Cat colours: ___ . "
            "3. Dog colour: ___ . 4. Dog age: ___ ."
        ),
        "exam_reading": (
            "Read.\n\n"
            "> \"Mia has got a cat called Pepper. He is six years "
            "old. He has soft grey fur. He eats fish and dry food. "
            "He sleeps on Mia's bed every afternoon and ignores "
            "everyone he doesn't like.\"\n\n"
            "1. Pet: ___ . 2. Age: ___ . 3. Eats: ___ . 4. One habit: "
            "___ ."
        ),
        "exam_use": (
            "**Fill in *have got / has got* (pos / neg / Q).**\n\n"
            "1. I __________ a hamster.\n"
            "2. Theo __________ a fish? (question)\n"
            "3. We __________ no pets. (negative)\n"
            "4. Mia __________ two cats."
        ),
        "exam_writing": (
            "Write 6 sentences about a real or imagined pet "
            "(name, age, colour, food, habit, feeling)."
        ),
        "exam_keys": [
            "**T1.** 2, grey and white, black with white spot, 6.",
            "**T2.** cat / Pepper, 6, fish and dry food, sleeps on "
            "Mia's bed.",
            "**T3.** 1. have got, 2. Has Theo got, 3. have got, "
            "4. has got.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 7,
        "slug": "weather-and-seasons",
        "title": "Weather and Seasons",
        "skills": ["listening", "writing", "language_awareness"],
        "bp": [
            "3.1.1 Soziokulturelles Orientierungswissen / Themen",
            "3.1.3.1 Hör-/Hörsehverstehen",
            "3.1.3.5 Schreiben",
            "3.1.3.7 Verfügen über sprachliche Mittel – Wortschatz",
        ],
        "objectives": [
            "I can describe today's weather in 3 sentences.",
            "I can name the four seasons and 8 weather words.",
            "I can use the present continuous for *right now* and the "
            "present simple for general patterns.",
        ],
        "leadin": (
            "It is November. The sky is the colour of cold tea. "
            "Mia is wearing two jumpers. Theo is wearing his "
            "beloved green raincoat. Frida the fox is sitting in a "
            "puddle, looking comfortable. \"For you,\" she "
            "explains, \"this is bad weather. For me, this is a "
            "spa.\""
        ),
        "activate": (
            "**Window report.** Look outside for 30 seconds. "
            "Write three sentences: *Today it is …, the sky is …, I "
            "am wearing …*"
        ),
        "input_blocks": [
            ("Vocabulary — weather and seasons",
             "*Seasons:* spring, summer, autumn (US: fall), winter.\n"
             "*Weather adjectives:* sunny, cloudy, rainy, snowy, "
             "foggy, windy, hot, warm, cool, cold, mild, frosty, "
             "stormy.\n"
             "*Phrases:* it's pouring, it's freezing, it's boiling, "
             "it's drizzling."),
            ("Grammar — present simple vs. present continuous",
             "**Present simple** for general truths and habits:\n"
             "- *It rains a lot in November.*\n"
             "- *We have snow every January.*\n\n"
             "**Present continuous** (*am/is/are* + -ing) for what "
             "is happening right now:\n"
             "- *It is raining right now.*\n"
             "- *Mia is wearing two jumpers because she is cold.*\n\n"
             "Spelling for -ing: *sit → sitting, run → running, "
             "make → making, fly → flying.*"),
        ],
        "practise_g": [
            "1. *Right now*: It __________ (rain). The wind "
            "__________ (blow) hard.",
            "2. *General*: In Stuttgart it often __________ (snow) "
            "in January.",
        ],
        "practise_m": [
            "3. Build a 3-sentence weather report for today: "
            "general (this season) + right now + your clothes.",
            "4. Negative right-now: *It isn't snowing*. Build three "
            "true negative sentences about the weather right now.",
        ],
        "answer_g": (
            "1. is raining / is blowing.\n"
            "2. snows."
        ),
        "answer_m": "3-4. Open.",
        "produce": (
            "**Weather diary — one school week.** For five days, "
            "write two sentences in English: *Today it is …* + "
            "what you are wearing or doing because of it."
        ),
        "produce_sample": (
            "*Monday: Today it is foggy and cool. I am wearing my "
            "scarf and walking slowly because the path is "
            "slippery.*"
        ),
        "reflect": [
            "I can describe today's weather.",
            "I can use present simple for habits and present "
            "continuous for now.",
            "I can keep a 5-day weather diary.",
        ],
        "pitfalls": [
            "*It is rain* → ✗ / *It is raining* → ✓.",
            "*It always is snowing in January* → ✗ — habit takes "
            "present simple: *It always snows in January*.",
            "L1 trap: German has no -ing form; the English "
            "*am/is/are + -ing* must be added.",
        ],
        "further": [
            "BBC Weather — child-friendly forecast.",
            "Met Office Kids — *Weather words*.",
        ],
        "exam_listening": (
            "Listen twice to the forecast.\n\n"
            "> \"Tomorrow morning will be foggy. By midday the fog "
            "will lift and we will have sun. Late afternoon, "
            "thunderstorms in the south. Friday: heavy rain all day, "
            "with strong wind from the west.\"\n\n"
            "1. Tomorrow morning: ___ . 2. Midday: ___ . "
            "3. Friday: ___ . 4. Wind direction: ___ ."
        ),
        "exam_reading": (
            "Read.\n\n"
            "> \"In Stuttgart it usually rains a lot in November. "
            "December is colder and we sometimes have snow. The "
            "best month for a long walk is May.\"\n\n"
            "T or F: 1. November is dry. 2. December is colder than "
            "November. 3. Snow in December. 4. May is good for a "
            "long walk."
        ),
        "exam_use": (
            "**Present simple or present continuous?**\n\n"
            "1. Right now it __________ (snow).\n"
            "2. In Sweden it often __________ (be) cold.\n"
            "3. Look! The trees __________ (lose) their leaves.\n"
            "4. We always __________ (go) skiing in January."
        ),
        "exam_writing": (
            "Write 5–6 sentences: today's weather, your favourite "
            "season, two things you do in that season."
        ),
        "exam_keys": [
            "**T1.** foggy, sun, heavy rain all day, west.",
            "**T2.** F, T, T, T.",
            "**T3.** 1. is snowing, 2. is, 3. are losing, 4. go.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 8,
        "slug": "hobbies-and-sports",
        "title": "Hobbies and Sports",
        "skills": ["speaking", "listening", "language_awareness"],
        "bp": [
            "3.1.1 Soziokulturelles Orientierungswissen / Themen",
            "3.1.3.1 Hör-/Hörsehverstehen",
            "3.1.3.3 Sprechen – an Gesprächen teilnehmen",
            "3.1.3.7 Verfügen über sprachliche Mittel – Wortschatz",
        ],
        "objectives": [
            "I can name 10 hobbies and 8 sports.",
            "I can use *can / can't* and *to be good at + -ing*.",
            "I can run a 90-second *Find Someone Who* mingling task.",
        ],
        "leadin": (
            "Theo can do a perfect cartwheel on the school field. "
            "He cannot, however, fold a T-shirt. Mia can fold a "
            "T-shirt with surgical precision. She cannot do a "
            "cartwheel without falling onto her dignity. Frida the "
            "fox watches both attempts and writes nothing down. "
            "Foxes do not need cartwheels."
        ),
        "activate": (
            "**Mime corner.** Teacher mimes 8 hobbies; class shouts "
            "the English."
        ),
        "input_blocks": [
            ("Vocabulary — hobbies and sports",
             "*Hobbies:* reading, drawing, painting, dancing, "
             "playing the guitar, singing, baking, gardening, "
             "video games, photography.\n"
             "*Sports:* football, basketball, tennis, swimming, "
             "running, cycling, skateboarding, climbing, judo, "
             "yoga."),
            ("Grammar — *can / can't* + *be good at + -ing*",
             "*can / can't* + base verb:\n"
             "- *I can swim.* / *I can't ride a unicycle.*\n\n"
             "*be good at* + noun or *-ing* verb:\n"
             "- *Mia is good at maths.*\n"
             "- *Theo is good at swimming.*\n"
             "- *Are you good at drawing?*"),
        ],
        "practise_g": [
            "1. Build: I __________ swim, but I __________ swim 100 "
            "metres. (can / can't)",
            "2. *good at*: *Theo / football* → ___ ; *Mia / drawing* "
            "→ ___ .",
        ],
        "practise_m": [
            "3. Mini-survey: write three *Find someone who* "
            "questions for a partner.",
            "4. *Negative + question*: *He can't / Can he?* — three "
            "sentences each.",
        ],
        "answer_g": (
            "1. can / can't.\n"
            "2. *Theo is good at football. Mia is good at drawing.*"
        ),
        "answer_m": "3-4. Open.",
        "produce": (
            "**Find Someone Who.** Walk around with a list of 8 "
            "things (*can play chess / can ride a unicycle / is "
            "good at baking / can swim 50 metres / …*). Get "
            "signatures. 90 seconds."
        ),
        "produce_sample": (
            "*— Can you play chess?* — *Yes, I can.* — *Sign here, "
            "please!*"
        ),
        "reflect": [
            "I can name 10 hobbies and 8 sports.",
            "I can use *can/can't* and *be good at + -ing*.",
            "I can mingle for 90 seconds in English.",
        ],
        "pitfalls": [
            "*can to swim* → ✗ — *can* + base verb.",
            "*She cans dance* → ✗ — *can* never takes -s.",
            "*good in* → ✗ / *good at* → ✓.",
        ],
        "further": [
            "BBC Sport — short kids' articles.",
            "British Council — *Hobbies* topic.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"Lina can play the piano very well. She can also "
            "swim 100 metres. She can't ride a horse, but she "
            "wants to learn. She is very good at drawing.\"\n\n"
            "1. Two things she can: ___ . 2. Distance she can "
            "swim: ___ . 3. Cannot: ___ . 4. Good at: ___ ."
        ),
        "exam_reading": (
            "Read.\n\n"
            "> \"Theo plays football twice a week. He is good at "
            "passing but bad at heading. He can ride a bike, ride "
            "a skateboard, and bake bread. He can't yet bake a "
            "cake.\"\n\n"
            "1. How often football: ___ . 2. Good at: ___ . "
            "3. Three other things he can do: ___ . 4. One thing "
            "he can't yet do: ___ ."
        ),
        "exam_use": (
            "**Fill in *can/can't* or *be good at + -ing*.**\n\n"
            "1. I __________ ride a bike.\n"
            "2. ___ you ___ a unicycle? (ride)\n"
            "3. Mia __________ (good / draw) horses.\n"
            "4. We __________ (good / cook) pasta."
        ),
        "exam_writing": (
            "Write 5–6 sentences about your hobbies. Use *can/can't* "
            "twice and *be good at + -ing* once."
        ),
        "exam_keys": [
            "**T1.** play piano / swim 100 m, 100 m, ride a horse, "
            "drawing.",
            "**T2.** twice a week, passing, ride a bike / "
            "skateboard / bake bread, bake a cake.",
            "**T3.** 1. can, 2. Can ride, 3. is good at drawing, "
            "4. are good at cooking.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 9,
        "slug": "birthday-and-friends",
        "title": "Birthday and Friends",
        "skills": ["speaking", "writing", "language_awareness"],
        "bp": [
            "3.1.1 Soziokulturelles Orientierungswissen / Themen",
            "3.1.3.3 Sprechen – an Gesprächen teilnehmen",
            "3.1.3.5 Schreiben",
            "3.1.3.8 Verfügen über sprachliche Mittel – Grammatik",
        ],
        "objectives": [
            "I can give and accept an invitation politely.",
            "I can use ordinal numbers and dates in writing.",
            "I can write a 6-line birthday-invitation card.",
        ],
        "leadin": (
            "Mia's birthday is on the 17th of March. She is making "
            "invitations on bright pink paper. Theo, who claims "
            "pink is embarrassing, is also making invitations — on "
            "bright pink paper, because the green ran out. Frida "
            "steals one for the foxes. \"It is the principle,\" "
            "she says, \"of being included.\""
        ),
        "activate": (
            "**Date chant.** Class repeats the months together, "
            "then says the date of three classmates' birthdays."
        ),
        "input_blocks": [
            ("Vocabulary — months and ordinals",
             "*Months:* January–December.\n"
             "*Ordinals:* 1st first, 2nd second, 3rd third, 4th "
             "fourth, 5th fifth, 9th ninth, 12th twelfth, 21st "
             "twenty-first, 30th thirtieth.\n"
             "Spelling: *fifth* (not fiveth), *ninth* (no e), "
             "*twelfth* (drop ve)."),
            ("Grammar — dates and prepositions",
             "- *My birthday is on March 17.* / *on the 17th of "
             "March.*\n"
             "- *I'm 11 in March.*\n"
             "- *The party starts at 3 p.m.*\n"
             "- *We meet on Saturday at 3 p.m. at my house.*"),
            ("Invitation phrases",
             "- *I'd like to invite you to my party.*\n"
             "- *Would you like to come?*\n"
             "- *I'd love to, thank you!*\n"
             "- *Sorry, I can't make it, but thank you for asking.*\n"
             "- *Please RSVP by Tuesday.*"),
        ],
        "practise_g": [
            "1. Fill in *in/on/at*: My birthday is __________ March. "
            "The party is __________ Saturday __________ 3 p.m.",
            "2. Build the ordinal: 17 → ___ , 21 → ___ , 30 → ___ .",
        ],
        "practise_m": [
            "3. Build a polite invitation (date, time, place, "
            "RSVP).",
            "4. Build a polite refusal (one reason, thanks).",
        ],
        "answer_g": (
            "1. in / on / at.\n"
            "2. seventeenth, twenty-first, thirtieth."
        ),
        "answer_m": "3-4. Open; check polite forms.",
        "produce": (
            "**Birthday card swap.** A6 paper. Front: drawing. "
            "Inside: a 6-line invitation (greeting, reason, date, "
            "time, place, RSVP, sign-off). Swap with a partner — "
            "they reply in writing (accept or polite refusal)."
        ),
        "produce_sample": (
            "*Dear Theo, I would like to invite you to my birthday "
            "party. It is on Saturday, 17 March, at 3 p.m. at my "
            "house. There will be cake and games. Please RSVP by "
            "Tuesday. Best wishes, Mia.*"
        ),
        "reflect": [
            "I can write the 12 months and ordinals 1–31.",
            "I can use *in/on/at* with dates and times.",
            "I can write a polite invitation card.",
        ],
        "pitfalls": [
            "*on March* → ✗ / *in March* → ✓.",
            "*at Saturday* → ✗ / *on Saturday* → ✓.",
            "L1 trap: German *am 17. März* → English *on 17 March / "
            "on the seventeenth of March*.",
        ],
        "further": [
            "BBC Learning English — *Months and dates*.",
            "British Council — invitation card templates.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"Hi Lina, I would like to invite you to my birthday "
            "party on Saturday, 17 March. It starts at 3 p.m. at "
            "my house. Please let me know by Tuesday if you can "
            "come.\"\n\n"
            "1. Day: ___ . 2. Date: ___ . 3. Time: ___ . 4. RSVP "
            "deadline: ___ ."
        ),
        "exam_reading": (
            "Read the reply.\n\n"
            "> \"Dear Mia, thank you for the invitation. I would "
            "love to come on Saturday. I will bring a small gift. "
            "See you at 3! Love, Lina.\"\n\n"
            "1. Yes/no: ___ . 2. Day: ___ . 3. Bringing: ___ . "
            "4. Sign-off: ___ ."
        ),
        "exam_use": (
            "**Fill in *in/on/at*.**\n\n"
            "1. ___ April, 2. ___ 5 May, 3. ___ 4 p.m., "
            "4. ___ September."
        ),
        "exam_writing": (
            "Write a 6-line birthday invitation: greeting, "
            "reason, date, time, place, RSVP, sign-off."
        ),
        "exam_keys": [
            "**T1.** Saturday, 17 March, 3 p.m., Tuesday.",
            "**T2.** yes, Saturday, a small gift, Love.",
            "**T3.** in / on / at / in.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 10,
        "slug": "a-day-in-london",
        "title": "A Day in London",
        "skills": ["reading", "listening", "intercultural"],
        "bp": [
            "3.1.1 Soziokulturelles Orientierungswissen / Themen",
            "3.1.2 Interkulturelle kommunikative Kompetenz",
            "3.1.3.1 Hör-/Hörsehverstehen",
            "3.1.3.2 Leseverstehen",
            "3.1.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can name 8 famous London places and identify them on a map.",
            "I can ask for and give simple directions in 4–6 sentences.",
            "I can read a short tourist text and pick out 5 facts.",
        ],
        "leadin": (
            "Mia's class is in London on a school trip. The double-"
            "decker buses are bright red. Big Ben is louder than "
            "expected. The pigeons in Trafalgar Square are bigger "
            "than the pigeons at home. Theo wants to ride on the "
            "top of every bus. Mr. Flint says: \"We have a list. "
            "We follow the list.\""
        ),
        "activate": (
            "**London five.** With your partner, name: a river, a "
            "tower, a palace, a museum, a famous square. Compare "
            "with another pair."
        ),
        "input_blocks": [
            ("Vocabulary — London landmarks",
             "*Big Ben (Elizabeth Tower), the Tower of London, Tower "
             "Bridge, Buckingham Palace, Trafalgar Square, the "
             "British Museum, the National Gallery, the London Eye, "
             "the Thames.*"),
            ("Phrases — directions",
             "- *Excuse me, where is …?* / *How do I get to …?*\n"
             "- *Go straight on for two minutes.*\n"
             "- *Turn left / right at the lights.*\n"
             "- *Take the second street on the right.*\n"
             "- *It's on your left, opposite the bank.*"),
            ("Reading — *A class trip to London*",
             "We arrived at King's Cross at 10 a.m. The first stop "
             "was the British Museum. Theo wanted to see the "
             "mummies. Mia wanted to see the clocks. We had lunch "
             "in St James's Park, on a bench under a tree. After "
             "lunch we walked across Tower Bridge. The river was "
             "grey, but the bridge was bright blue. At 5 p.m. we "
             "took the train back from St Pancras."),
        ],
        "practise_g": [
            "1. Match: Big Ben — clock tower, Buckingham Palace — "
            "royal residence, Tower Bridge — opens for ships. "
            "(T / F)",
            "2. Direction fill-in: Go __________ on. Turn __________ "
            "at the corner. It's __________ your left.",
        ],
        "practise_m": [
            "3. Build a 4-line direction set from the school to a "
            "nearby place (the supermarket, the park).",
            "4. Reading question: from the text, who wanted what at "
            "the British Museum?",
        ],
        "answer_g": (
            "1. all true.\n"
            "2. straight / right / on."
        ),
        "answer_m": "3-4. Open; from text: Theo — mummies, Mia — clocks.",
        "produce": (
            "**London-trip plan.** In groups of 3, plan a 6-hour "
            "London day. Choose 4 places. Write a small itinerary "
            "(time + place + activity + transport)."
        ),
        "produce_sample": (
            "*10:00 — British Museum (mummies). 11:30 — walk to "
            "Trafalgar Square. 12:30 — lunch at St James's Park. "
            "14:00 — London Eye (book online). 16:00 — train back "
            "from St Pancras.*"
        ),
        "reflect": [
            "I can name 8 London landmarks.",
            "I can ask for and give simple directions.",
            "I can read a tourist text and find 5 facts.",
        ],
        "pitfalls": [
            "*Big Ben* — strictly the bell, not the tower. The tower "
            "is the *Elizabeth Tower*. Both are accepted in everyday "
            "English.",
            "Stereotype check: *all British people drink tea* — "
            "avoid.",
            "Britain ≠ England ≠ UK; Scotland and Wales are not "
            "England.",
        ],
        "further": [
            "VisitLondon — accessible city overview.",
            "British Museum — free entry, online floor plans.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"Excuse me, where is the National Gallery? Walk "
            "straight on for two minutes. At the lights, turn "
            "right. The gallery is on your left, opposite a small "
            "cafe.\"\n\n"
            "1. Place asked about: ___ . 2. First, walk ___ . "
            "3. At the lights, turn ___ . 4. The gallery is "
            "opposite ___ ."
        ),
        "exam_reading": (
            "Read.\n\n"
            "> \"On her London trip Mia saw Big Ben, the London "
            "Eye, Tower Bridge, and the British Museum. Her "
            "favourite was the London Eye, because the view was "
            "amazing. Theo's favourite was the museum.\"\n\n"
            "1. Four places: ___ . 2. Mia's favourite + reason: ___ . "
            "3. Theo's favourite: ___ . 4. Number of pupils: not in "
            "text — write *not given*."
        ),
        "exam_use": (
            "**Fill in *in/on/at*.**\n\n"
            "1. ___ London, 2. ___ Tower Bridge, 3. ___ 5 p.m., "
            "4. ___ the museum (= inside)."
        ),
        "exam_writing": (
            "Write 6 sentences about a city trip you would like to "
            "take. Include 3 places + 1 transport + 1 reason."
        ),
        "exam_keys": [
            "**T1.** National Gallery, straight on (2 min), right, "
            "a small cafe.",
            "**T2.** Big Ben / London Eye / Tower Bridge / British "
            "Museum; London Eye — view was amazing; the British "
            "Museum; not given.",
            "**T3.** in / on / at / in.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 11,
        "slug": "clothes-and-colours",
        "title": "Clothes and Colours",
        "skills": ["speaking", "writing", "language_awareness"],
        "bp": [
            "3.1.1 Soziokulturelles Orientierungswissen / Themen",
            "3.1.3.3 Sprechen – an Gesprächen teilnehmen",
            "3.1.3.5 Schreiben",
            "3.1.3.7 Verfügen über sprachliche Mittel – Wortschatz",
            "3.1.3.8 Verfügen über sprachliche Mittel – Grammatik",
        ],
        "objectives": [
            "I can name 12 items of clothing and 10 colours.",
            "I can describe what someone is wearing using present continuous.",
            "I can use comparative *the same … as / different from*.",
        ],
        "leadin": (
            "Theo's blue jumper has gone missing. He looks under "
            "the bed, in the wardrobe, behind the door. Frida the "
            "fox steps quietly out of the wardrobe wearing a small "
            "blue jumper that fits her remarkably well. \"Foxes,\" "
            "she says, \"appreciate clean wool.\" Theo opens his "
            "mouth to protest, then closes it. He has been raised "
            "well."
        ),
        "activate": (
            "**Colour shout.** Teacher points; class shouts the "
            "colour. 30 seconds, fast pace."
        ),
        "input_blocks": [
            ("Vocabulary — clothes and colours",
             "*Clothes:* T-shirt, shirt, jumper, jacket, coat, "
             "trousers, jeans, shorts, skirt, dress, shoes, "
             "trainers, boots, socks, hat, scarf, gloves.\n"
             "*Colours:* red, blue, green, yellow, black, white, "
             "grey, brown, orange, pink, purple, navy, beige."),
            ("Grammar — present continuous for outfits",
             "- *Mia is wearing a yellow jumper and blue jeans.*\n"
             "- *I am wearing a black T-shirt today.*\n"
             "- *Theo is not wearing a coat.*\n"
             "- *Are you wearing your new shoes?*"),
            ("Comparative phrases",
             "- *the same colour as*: *My T-shirt is the same "
             "colour as your scarf.*\n"
             "- *different from*: *My shoes are different from "
             "yours.*\n"
             "- *bigger / smaller than*: *His shoes are bigger than "
             "mine.*"),
        ],
        "practise_g": [
            "1. Build present continuous: I __________ (wear) blue "
            "jeans. Mia __________ (wear) a green jacket.",
            "2. Compare: my hat / your scarf — same colour → ___ ; "
            "his shoes / mine — bigger → ___ .",
        ],
        "practise_m": [
            "3. Describe a partner in 4 sentences. Add one comparison.",
            "4. Negative + question: *I'm not wearing …*; *Are you "
            "wearing …?* — three each.",
        ],
        "answer_g": (
            "1. am wearing / is wearing.\n"
            "2. *My hat is the same colour as your scarf. His shoes "
            "are bigger than mine.*"
        ),
        "answer_m": "3-4. Open.",
        "produce": (
            "**Description game.** In pairs, A closes their eyes; "
            "B describes a third classmate's outfit (4 sentences "
            "minimum, one comparison). A guesses who."
        ),
        "produce_sample": (
            "*— She is wearing a red T-shirt and black jeans. Her "
            "shoes are white. Her scarf is the same colour as her "
            "T-shirt.*\n*— Lina!*"
        ),
        "reflect": [
            "I can name 12 clothes and 10 colours.",
            "I can use present continuous for outfits.",
            "I can compare two items with *same … as*, *different "
            "from*.",
        ],
        "pitfalls": [
            "*She wear a red dress* → ✗ / *She is wearing* → ✓.",
            "*pant* (US, underwear) vs. *trousers* (BrE, "
            "outerwear).",
            "L1 trap: German *Hose* (singular) is English *trousers* "
            "(plural).",
        ],
        "further": [
            "BBC Learning English — *Clothes vocabulary*.",
            "British Council Kids — *Clothes* games and songs.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"Mia is wearing a yellow jumper, blue jeans, and "
            "white trainers. Theo is wearing a green T-shirt, black "
            "shorts, and brown sandals. Lina is wearing the same "
            "colour scarf as Mia's jumper.\"\n\n"
            "1. Mia jumper: ___ . 2. Mia shoes: ___ . 3. Theo "
            "T-shirt: ___ . 4. Lina's scarf colour: ___ ."
        ),
        "exam_reading": (
            "Read.\n\n"
            "> \"On the school trip we must wear comfortable shoes, "
            "a warm jumper, and a rain jacket. No skirts, no "
            "flip-flops. Pack one extra pair of socks in your "
            "rucksack.\"\n\n"
            "1. Shoes: ___ . 2. Jumper: ___ . 3. Bring: ___ . "
            "4. Don't wear: ___ ."
        ),
        "exam_use": (
            "**Build the present continuous.**\n\n"
            "1. (I / wear / blue / jeans) → ___\n"
            "2. (Mia / wear / red / dress) → ___\n"
            "3. (we / wear / school / uniform) → ___\n"
            "4. (Theo / not / wear / hat) → ___"
        ),
        "exam_writing": (
            "Describe what three classmates are wearing today. "
            "Use present continuous and one comparison."
        ),
        "exam_keys": [
            "**T1.** yellow, white trainers, green, yellow.",
            "**T2.** comfortable, warm, rain jacket / extra socks, "
            "skirts / flip-flops.",
            "**T3.** 1. *I am wearing blue jeans.* 2. *Mia is "
            "wearing a red dress.* 3. *We are wearing school "
            "uniform.* 4. *Theo isn't wearing a hat.*",
            "**T4.** Open.",
        ],
    },
    {
        "n": 12,
        "slug": "review-and-show",
        "title": "Review and Show",
        "skills": ["speaking", "writing", "language_awareness"],
        "bp": [
            "3.1.1 Soziokulturelles Orientierungswissen / Themen",
            "3.1.3.4 Sprechen – zusammenhängendes monologisches Sprechen",
            "3.1.3.5 Schreiben",
            "3.1.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can speak for 60–90 seconds about myself in English.",
            "I can use grammar from the year (am/is/are, have got, "
            "can, present simple, present continuous, possessive 's).",
            "I can listen to a peer's talk and give one constructive "
            "feedback sentence.",
        ],
        "leadin": (
            "Mr. Flint sets up two small microphones in the corner "
            "of the classroom. \"At the end of Klasse 5,\" he "
            "says, \"each of you stands here for a minute and says "
            "something true in English. Bullets, not full text.\" "
            "Frida the fox sits at the back, taking imaginary "
            "notes. \"Will you speak too?\" Mia asks. Frida says, "
            "\"Foxes don't talk\" — in perfect English."
        ),
        "activate": (
            "**Three-line warm-up.** In your notebook, write:\n"
            "- *In September I …*\n"
            "- *Now I …*\n"
            "- *Next year I want to …*"
        ),
        "input_blocks": [
            ("The 60–90 second talk — structure",
             "1. **Then.** Where I started in September. (1–2 "
             "sentences)\n"
             "2. **Now.** What I can do now. (3–4 sentences using "
             "the year's grammar)\n"
             "3. **Forward.** One thing I want to learn next year. "
             "(1 sentence)"),
            ("Sample (~60 seconds)",
             "*Hello, my name is Mia. In September I couldn't say "
             "much in English. Now I can introduce myself, talk "
             "about my family, and order a hot chocolate in a "
             "cafe. I have got a cat called Pepper and a brother "
             "called Theo. My favourite season is autumn because "
             "I like rainy walks. Next year I want to read my "
             "first English short story. Thank you.*"),
            ("Feedback frames",
             "- *I noticed that …*\n"
             "- *One thing that worked was …*\n"
             "- *One thing you could try is …*"),
        ],
        "practise_g": [
            "1. Build a 5-line talk using the three frames.",
        ],
        "practise_m": [
            "2. Build an 8-line talk: introduction, three Then/Now "
            "facts (one with possessive, one with *can*, one with "
            "present continuous), one Forward, one polite ending.",
        ],
        "answer_g": "Open. Check sentence variety.",
        "answer_m": "Open.",
        "produce": (
            "**Class show.** Each student stands at the front for "
            "60–90 seconds. Bullets only. After every talk, one "
            "classmate gives feedback in one English sentence. "
            "The teacher records the talks for a class playlist."
        ),
        "produce_sample": "(see Input above)",
        "reflect": [
            "I can speak for 60–90 seconds with a clear three-"
            "movement structure.",
            "I can use 4 grammar points from the year in one talk.",
            "I can give one specific piece of feedback in English.",
        ],
        "pitfalls": [
            "Reading aloud word-for-word makes the talk flat. "
            "Bullets only.",
            "*I am eleven years* → ✗ — *I am eleven* OR *I am "
            "eleven years old*.",
            "Avoid generic claims (*I have learned a lot*) — give "
            "one concrete example instead.",
        ],
        "further": [
            "BBC Sounds — *Short Cuts* (short personal monologues).",
            "LearnEnglish Kids — sample student videos at A1 level.",
        ],
        "exam_listening": (
            "Listen twice to Theo's talk.\n\n"
            "> \"My name is Theo. I am eleven. I have got one "
            "sister, Mia. I can play football very well. I can't "
            "swim 100 metres yet, but I can do 50. Next year I "
            "want to learn to play the guitar.\"\n\n"
            "1. Age: ___ . 2. Sister's name: ___ . 3. Two things "
            "he can do: ___ . 4. One plan: ___ ."
        ),
        "exam_reading": (
            "Read Lina's text.\n\n"
            "> \"Hi, I'm Lina. In September I couldn't speak much "
            "English. Now I can write a short text about my family "
            "and order in a cafe. I have got two cats. My favourite "
            "subject is art. Next year I want to read a book in "
            "English.\"\n\n"
            "1. September: ___ . 2. Now (two things): ___ . "
            "3. Pets: ___ . 4. Plan: ___ ."
        ),
        "exam_use": (
            "**Mixed grammar review.**\n\n"
            "1. I __________ (be) eleven.\n"
            "2. Mia __________ (have got) a cat.\n"
            "3. Right now I __________ (write) my exam.\n"
            "4. Next year I __________ (learn) the guitar."
        ),
        "exam_writing": (
            "Write your own 60-second talk text (10–14 sentences). "
            "Use *Then / Now / Forward* and at least four grammar "
            "points from the year."
        ),
        "exam_keys": [
            "**T1.** 11, Mia, play football / swim 50m, learn the "
            "guitar.",
            "**T2.** couldn't speak much; can write short text & "
            "order in a cafe; two cats; read a book in English.",
            "**T3.** 1. am, 2. has got, 3. am writing, "
            "4. will learn / am going to learn.",
            "**T4.** Open.",
        ],
    },
]

UNIT_TPL = """---
title: "Unit {n} — {title}"
subtitle: "Track E · Klasse 5 · Niveau E"
niveau: "E"
klassenstufe: 5
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
**Niveau:** E. Klassenarbeit at Niveau E (30 BE).
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

**One thing in your notebook:** *Write one sentence that uses
something you learned in this Unit.*

## Exam example

{{{{< include _unit{nn}_{slug}_exam_body.qmd >}}}}

## Downloads

{{{{< downloads >}}}}

::: {{.notes}}
**Slide deck timing.** 45 minutes total. Lead-in 3 min · Activate
4 min · Input 12 min · Practise 8 min · Produce 13 min · Reflect
5 min.

**Differentiation.** Below Niveau E (mixed group): provide a
support card with the key structure. Above Niveau E: extension
question linking to the next Unit's grammar.
:::

## Common pitfalls

{pitfalls}

## Further reading / listening

{further}
"""

EXAM_BODY_TPL = """::: {{.callout-warning icon=false title="Klassenarbeit — Niveau E (45 minutes)"}}
**Time.** 45 minutes. **Total.** 30 points.
:::

### Task 1 — Listening (8 BE)

{exam_listening}

### Task 2 — Reading (8 BE)

{exam_reading}

### Task 3 — Use of English (8 BE)

{exam_use}

### Task 4 — Writing (6 BE)

{exam_writing}

::: {{.callout-tip collapse="true" title="Answer key"}}
{exam_keys}
:::

::: {{.callout-tip collapse="true" title="Notenschlüssel (von 30)"}}
| 28–30 | 1 | 24–27 | 2 | 20–23 | 3 |
| 15–19 | 4 |  9–14 | 5 |  0–8  | 6 |
:::
"""

EXAM_WRAP_TPL = """---
title: "Klassenarbeit — Unit {n}: {title}"
subtitle: "Track E · Klasse 5 · Niveau E · 45 Minuten"
author: "S. Le Boulanger"
niveau: "E"
klassenstufe: 5
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

# Klassenarbeit — Unit {n}: {title}

**Track E · Klasse 5 · Niveau E · 45 Minuten**

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

    print(f"Wrote {len(UNITS) * 3} files for Track E Klasse 5.")


if __name__ == "__main__":
    emit()
