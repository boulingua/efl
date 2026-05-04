"""Batch-emit Track G+M Klasse 5 Units 03-12.

Each Unit gets three files: the Unit .qmd, the standalone exam
wrapper .qmd, and the underscore-prefixed exam-body partial.
Klasse 5 voice: short sentences, present tense dominant, animal +
kid cast (Mia, Theo, Frida the fox, Mr. Flint).
"""
from __future__ import annotations
import pathlib
import textwrap

REPO = pathlib.Path(__file__).resolve().parent.parent
COURSE = REPO / "track_gm_kl05" / "units"

UNITS = [
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
            "3.1.3.8 Verfügen über sprachliche Mittel – Grammatik",
        ],
        "objectives": [
            "I can name 12 things in a room.",
            "I can use *there is / there are* to describe a place.",
            "I can write a short text about my own room (4–6 sentences).",
        ],
        "leadin": (
            "Mia opens the door of her room. The bed is on the right. "
            "The desk is on the left. There is a poster of a fox over "
            "the bed. There is a small green plant on the desk. "
            "Frida the fox jumps onto the windowsill. \"Tidy room,\" "
            "she says. \"For now,\" Mia says."
        ),
        "activate": (
            "**Quick-draw.** Draw your room in 30 seconds. Mark four "
            "things: bed, desk, window, door. Show your partner."
        ),
        "input_blocks": [
            ("Vocabulary — rooms and furniture",
             "| English | Deutsch |\n|---------|---------|\n"
             "| bedroom | Schlafzimmer |\n| kitchen | Küche |\n"
             "| living room | Wohnzimmer |\n| bathroom | Bad |\n"
             "| bed | Bett |\n| desk | Schreibtisch |\n| chair | Stuhl |\n"
             "| window | Fenster |\n| door | Tür |\n| poster | Poster |\n"
             "| shelf | Regal |\n| lamp | Lampe |"),
            ("Grammar — there is / there are",
             "Use **there is** with a singular noun, **there are** with "
             "plural.\n\n- *There is a bed in my room.*\n"
             "- *There are two windows in my room.*\n"
             "- *Is there a desk?* — *Yes, there is.*\n"
             "- *Are there chairs?* — *Yes, there are.*\n"
             "- *There is no lamp.* / *There aren't any chairs.*"),
            ("Prepositions of place",
             "*on, under, in, next to, between, behind, in front of, "
             "above*. Quick map: *The cat is on the bed. The shoes are "
             "under the bed. The lamp is next to the desk.*"),
        ],
        "practise_g": [
            "1. There __________ a desk in my room. (is / are)",
            "2. There __________ two windows. (is / are)",
            "3. There __________ no chairs in the kitchen. (is / are)",
            "4. The cat is __________ the bed. (on / between)",
        ],
        "practise_m": [
            "5. (your room: a bed, two posters) → ___",
            "6. (the kitchen: no chairs) → ___",
            "7. (the desk: under the window) → ___",
        ],
        "answer_g": "1. is, 2. are, 3. are, 4. on.",
        "answer_m": (
            "5. *In my room there is a bed and there are two posters.*\n"
            "6. *There aren't any chairs in the kitchen.*\n"
            "7. *The desk is under the window.*"
        ),
        "produce": (
            "**My-room poster.** Draw your room on A4 paper. Label six "
            "things in English. Write four sentences underneath using "
            "*there is / there are* and one preposition."
        ),
        "produce_sample": (
            "*This is my room. There is a bed in the corner. There are "
            "two posters on the wall. The desk is next to the window. "
            "My books are on the shelf above the desk.*"
        ),
        "reflect": [
            "I can name 12 room words.",
            "I can use *there is / there are* correctly.",
            "I can write four sentences about my room.",
        ],
        "pitfalls": [
            "*It has a bed* → unusual for *room has* — prefer *there is*.",
            "*There is two beds* → ✗ / *There are two beds* → ✓.",
            "L1 trap: German *Es gibt* always maps to *there is/are*, "
            "never to *it gives*.",
        ],
        "further": [
            "BBC Learning English — *Around the house*. <https://www.bbc.co.uk/learningenglish>",
            "LearnEnglish Kids — *My House* song. <https://learnenglishkids.britishcouncil.org>",
        ],
        "exam_listening": (
            "The teacher reads about Mia's room twice. Tick the "
            "right answers.\n\n"
            "> \"In my room there is a bed and a desk. There are two "
            "windows. The cat is under the bed. There is a green "
            "plant on the desk.\"\n\n"
            "1. There is a __________ . (bed / sofa)\n"
            "2. There are __________ windows. (one / two)\n"
            "3. The cat is __________ the bed. (on / under)\n"
            "4. The plant is __________ . (red / green)"
        ),
        "exam_reading": (
            "Read about Theo's room. Write **true** or **false**.\n\n"
            "> \"In my room there is a desk under the window. There are "
            "three football posters on the wall. There is no TV in my "
            "room.\"\n\n"
            "1. The desk is under the window. (T / F)\n"
            "2. There are two posters. (T / F)\n"
            "3. There is no TV. (T / F)\n"
            "4. The posters show football. (T / F)"
        ),
        "exam_use": (
            "**Fill in *there is / there are*.**\n\n"
            "1. __________ a chair next to the desk.\n"
            "2. __________ four books on the shelf.\n"
            "3. __________ no lamp in this room.\n"
            "4. __________ two windows in the kitchen."
        ),
        "exam_writing": (
            "Draw your room and write 4 sentences. Use *there is / "
            "there are* and one preposition (*on, under, next to*)."
        ),
        "exam_keys": [
            "**T1.** bed, two, under, green.",
            "**T2.** T, F, T, T.",
            "**T3.** 1. There is, 2. There are, 3. There is, 4. There are.",
            "**T4.** Open. 1 BE per correct sentence + 2 BE language.",
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
            "I can name 8 school subjects in English.",
            "I can tell the time on the clock (full hours and half hours).",
            "I can describe my school day using the present simple.",
        ],
        "leadin": (
            "Mia's timetable is on the fridge. Monday: maths, German, "
            "English, sport, music. Theo's timetable is the same, but "
            "with Latin instead of music. Frida the fox cannot read "
            "the timetable. \"Foxes don't go to school,\" she says. "
            "\"We just go.\""
        ),
        "activate": (
            "**Two-minute timetable.** Write your Monday in 5 lines. "
            "Lesson 1, Lesson 2, Lesson 3, Lesson 4, break."
        ),
        "input_blocks": [
            ("Vocabulary — school subjects",
             "*English, German, French, Maths, Biology, Physics, "
             "Chemistry, History, Geography, Music, Art, PE / Sport, "
             "Religion, Ethics.*"),
            ("Telling the time",
             "- *It's eight o'clock.*\n"
             "- *It's half past eight.* (= 8:30)\n"
             "- *It's quarter past eight.* (= 8:15)\n"
             "- *It's quarter to nine.* (= 8:45)\n"
             "- *At what time …?* — *At half past nine.*"),
            ("Grammar — present simple, third person -s",
             "Add **-s** to verbs in he/she/it.\n\n"
             "- *I start school at eight.*\n"
             "- *Mia **starts** school at eight.*\n"
             "- *Theo **plays** football.*\n\n"
             "Spelling traps: *go → goes*, *do → does*, *teach → "
             "teaches*, *study → studies*."),
        ],
        "practise_g": [
            "1. I __________ (start) school at eight.",
            "2. Mia __________ (start) school at eight.",
            "3. We __________ (have) maths on Monday.",
            "4. Theo __________ (do) sport on Tuesday.",
        ],
        "practise_m": [
            "5. (8:30) → ___",
            "6. (9:15) → ___",
            "7. (10:45) → ___",
            "8. *(my brother / English / Tuesday)* → ___",
        ],
        "answer_g": "1. start, 2. starts, 3. have, 4. does.",
        "answer_m": (
            "5. *It's half past eight.* 6. *It's quarter past nine.* "
            "7. *It's quarter to eleven.* "
            "8. *My brother has English on Tuesday.*"
        ),
        "produce": (
            "**Pair speaking — *My Day*.** With your partner, take "
            "turns. One asks *What time do you have …?*; the other "
            "answers. Cover four subjects."
        ),
        "produce_sample": (
            "*— What time do you have maths on Monday?*\n"
            "*— I have maths at quarter past eight.*"
        ),
        "reflect": [
            "I can name 8 school subjects.",
            "I can tell the time at the half hour.",
            "I can use the present simple with -s.",
        ],
        "pitfalls": [
            "Forgetting the third-person -s: *Mia start* → ✗ / "
            "*Mia starts* → ✓.",
            "*goes / does / teaches* — irregular -s spellings.",
            "L1 trap: German *Wir haben Mathe* maps to *We have maths* "
            "(no preposition).",
        ],
        "further": [
            "BBC Learning English — *Telling the time*. <https://www.bbc.co.uk/learningenglish>",
            "LearnEnglish Kids — *School subjects vocabulary*. <https://learnenglishkids.britishcouncil.org>",
        ],
        "exam_listening": (
            "The teacher reads aloud Mia's Monday twice.\n\n"
            "> \"On Monday I start at eight. First I have maths. Then "
            "I have English. At ten o'clock we have a break. After "
            "the break we have sport.\"\n\n"
            "1. School starts at __________ . (eight / nine)\n"
            "2. The first lesson is __________ . (maths / German)\n"
            "3. The break is at __________ . (10:00 / 10:30)\n"
            "4. After the break: __________ ."
        ),
        "exam_reading": (
            "Read Theo's Tuesday and complete the table.\n\n"
            "> \"On Tuesday I start at 8:15. I have music, German, "
            "English, and history.\"\n\n"
            "| Day | Start | Subjects |\n|-----|-------|----------|\n"
            "| Tuesday | ? | ? |"
        ),
        "exam_use": (
            "**Add -s where needed.**\n\n"
            "1. Mia __________ (start) at eight.\n"
            "2. We __________ (have) German.\n"
            "3. Theo __________ (do) Latin.\n"
            "4. They __________ (play) football."
        ),
        "exam_writing": (
            "Write 4 sentences about your Monday: subjects, times, "
            "one thing you like."
        ),
        "exam_keys": [
            "**T1.** eight, maths, 10:00, sport.",
            "**T2.** Tuesday / 8:15 / music, German, English, history.",
            "**T3.** 1. starts, 2. have, 3. does, 4. play.",
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
            "I can name 12 foods and 6 drinks.",
            "I can order a snack in a cafe in English.",
            "I can use *like / don't like* and the indefinite article.",
        ],
        "leadin": (
            "Frida the fox sits in the school canteen. She has never "
            "tried apple juice before. Mia hands her a cup. Frida "
            "tastes it. \"This,\" she says, \"is the second best "
            "thing I have ever tried.\" \"What's the first?\" Theo "
            "asks. Frida grins. \"Chicken.\""
        ),
        "activate": (
            "**Hands up.** Stand up if it is true: *I like apples. I "
            "don't like cheese. I drink water at school. I have "
            "breakfast every day.*"
        ),
        "input_blocks": [
            ("Vocabulary — food and drink",
             "*Food:* apple, banana, bread, cheese, egg, fish, chicken, "
             "potato, rice, salad, soup, sausage.\n"
             "*Drinks:* water, milk, tea, coffee, juice, lemonade.\n"
             "*Meals:* breakfast, lunch, dinner."),
            ("Grammar — *like / don't like* + indefinite article",
             "- *I like apples.* (general — no article needed for "
             "plurals)\n"
             "- *I don't like cheese.* (uncountable — no article)\n"
             "- *I want **an** apple.* (specific singular — *a/an*)\n"
             "- *Can I have **a** glass of water?*\n"
             "- *Use **an** before vowel sounds: an apple, an "
             "orange, an egg, an hour.*"),
            ("Cafe phrases",
             "- *Can I have …, please?*\n- *I'd like …, please.*\n"
             "- *That's £2.50.*\n- *Anything else?*\n"
             "- *Here you are.* / *Thank you.*"),
        ],
        "practise_g": [
            "1. *a* or *an*? __________ apple, __________ banana, "
            "__________ egg, __________ orange.",
            "2. I __________ (like) cheese.  My brother __________ "
            "(not / like) fish.",
            "3. Match: lemonade — drink, salad — food, juice — drink, "
            "soup — food. (T / F)",
        ],
        "practise_m": [
            "4. (you / cafe / asking for tea) → ___",
            "5. (you / cafe / asking for water) → ___",
            "6. *Build the dialogue.* Customer / waiter / 4 lines.",
        ],
        "answer_g": (
            "1. an apple, a banana, an egg, an orange.\n"
            "2. like / doesn't like.\n"
            "3. all true."
        ),
        "answer_m": (
            "4. *Can I have a tea, please?*\n"
            "5. *I'd like a glass of water, please.*\n"
            "6. Open. Check polite forms + *please / thank you*."
        ),
        "produce": (
            "**Cafe role-play.** In pairs, take turns being customer "
            "and waiter. Order one drink and one food. Use *please* "
            "and *thank you*."
        ),
        "produce_sample": (
            "*— Hello, what can I get you?*\n"
            "*— Can I have a tea and an apple, please?*\n"
            "*— That's two pounds. Anything else?*\n"
            "*— No, thank you. Here you are.*"
        ),
        "reflect": [
            "I can name 12 foods and 6 drinks.",
            "I can use *a* or *an* correctly.",
            "I can order a snack in a cafe.",
        ],
        "pitfalls": [
            "*a apple* → ✗ / *an apple* → ✓.",
            "*I like an apples* → ✗ — for general likes, no article "
            "with plurals.",
            "L1 trap: German *Ich möchte einen Tee* — English *I'd "
            "like a tea* (no *einen*).",
        ],
        "further": [
            "BBC Learning English — *In the cafe*. <https://www.bbc.co.uk/learningenglish>",
            "LearnEnglish Kids — *Food and drink* games. <https://learnenglishkids.britishcouncil.org>",
        ],
        "exam_listening": (
            "The teacher reads twice.\n\n"
            "> \"At the cafe, Mia orders an apple juice and a "
            "sandwich. Theo has a glass of milk and a banana. The "
            "fox just sips water from a small cup.\"\n\n"
            "1. Mia drinks __________ . 2. Theo eats __________ .\n"
            "3. The fox drinks __________ . 4. Mia eats __________ ."
        ),
        "exam_reading": (
            "Read the menu. Write the price.\n\n"
            "> \"Apple juice 1.50; Tea 1.20; Sandwich 3.00; Cake 2.50; "
            "Banana 0.50.\"\n\n"
            "How much is: 1. tea? 2. a sandwich? 3. cake? 4. a banana?"
        ),
        "exam_use": (
            "**Insert *a* or *an*.**\n\n"
            "1. ___ apple, 2. ___ banana, 3. ___ orange juice, "
            "4. ___ sandwich."
        ),
        "exam_writing": (
            "Write a short cafe dialogue (4 lines). One customer, "
            "one waiter, two items ordered."
        ),
        "exam_keys": [
            "**T1.** apple juice, a banana, water, a sandwich.",
            "**T2.** £1.20, £3.00, £2.50, £0.50.",
            "**T3.** an, a, an, a.",
            "**T4.** Open. Check polite forms.",
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
            "I can name 12 animals.",
            "I can use *have got / has got* to talk about pets.",
            "I can write a short text about a real or imagined pet.",
        ],
        "leadin": (
            "Frida the fox sits on Mia's bed. \"Am I a pet?\" she "
            "asks. Mia thinks. Pepper the cat opens one eye. "
            "\"Definitely not,\" Pepper says. \"Pets are quiet, kind, "
            "and full of fur.\" Frida is quiet, kind, and full of "
            "fur. Mia smiles. \"Pet enough for me.\""
        ),
        "activate": (
            "**Animal sounds.** The teacher makes an animal sound; "
            "the class shouts the English word. Cat, dog, cow, "
            "horse, sheep, duck, pig, owl."
        ),
        "input_blocks": [
            ("Vocabulary — animals",
             "*cat, dog, mouse, hamster, rabbit, fish, bird, fox, "
             "wolf, bear, cow, horse, sheep, pig, duck, chicken, "
             "owl, snake, frog, lizard.*"),
            ("Grammar — *have got / has got*",
             "British English uses *have got / has got* a lot for "
             "possession.\n\n"
             "- *I have got a cat.* / *I've got a cat.*\n"
             "- *Mia has got a brother.* / *Mia's got a brother.*\n"
             "- *Have you got a pet?* — *Yes, I have. / No, I haven't.*\n"
             "- *Has Theo got a fish?* — *No, he hasn't.*\n\n"
             "American English prefers *have / has* alone."),
        ],
        "practise_g": [
            "1. I __________ (have got) a cat.",
            "2. Mia __________ (have got) a brother.",
            "3. Theo __________ (not / have got) a dog.",
            "4. ___ you got a pet?",
        ],
        "practise_m": [
            "5. (Lina / hamster — yes) → ___",
            "6. (parents / fish — no) → ___",
            "7. (you / brother or sister?) → ___",
        ],
        "answer_g": "1. have got, 2. has got, 3. hasn't got, 4. Have.",
        "answer_m": (
            "5. *Lina has got a hamster.*\n"
            "6. *My parents haven't got fish.*\n"
            "7. *Have you got a brother or a sister?*"
        ),
        "produce": (
            "**Pet portrait.** Draw a real or imagined pet on paper. "
            "Underneath, write 4–6 sentences: name, age, colour, "
            "what it eats, one thing it does."
        ),
        "produce_sample": (
            "*This is Pepper. He has got grey fur. He is six years "
            "old. He eats fish and dry food. He sleeps on my bed "
            "every afternoon.*"
        ),
        "reflect": [
            "I can name 12 animals.",
            "I can use *have got / has got*.",
            "I can write 4 sentences about a pet.",
        ],
        "pitfalls": [
            "*I am have got* → ✗ / *I have got* → ✓.",
            "*Has she got* (no extra *do*).",
            "L1 trap: German *Ich habe einen Hund* maps to *I have "
            "(got) a dog* — not *I am having a dog*.",
        ],
        "further": [
            "BBC Earth — *Animals*. <https://www.bbc.co.uk/programmes/genres/factual/natureandenvironment>",
            "LearnEnglish Kids — *Pets vocabulary*. <https://learnenglishkids.britishcouncil.org>",
        ],
        "exam_listening": (
            "Listen.\n\n"
            "> \"Mia has got a cat. The cat is grey. Theo has got a "
            "fish. The fish is orange. Lina has got a rabbit. The "
            "rabbit is white.\"\n\n"
            "1. Mia: ___ , 2. Theo: ___ , 3. Lina: ___ , "
            "4. Colour of the cat: ___ ."
        ),
        "exam_reading": (
            "Read about Pepper.\n\n"
            "> \"Pepper is a grey cat. He is six years old. He likes "
            "fish and warm beds. He doesn't like dogs.\"\n\n"
            "T or F: 1. Pepper is white. 2. He is six. 3. He likes "
            "fish. 4. He likes dogs."
        ),
        "exam_use": (
            "**Fill in *have got / has got* (positive, negative, "
            "question).**\n\n"
            "1. I __________ a hamster.\n"
            "2. Theo __________ a dog. (negative)\n"
            "3. ___ you ___ a pet? (question)\n"
            "4. We __________ two cats."
        ),
        "exam_writing": (
            "Draw a real or imagined pet. Write 4 sentences: name, "
            "age, colour, one thing it likes."
        ),
        "exam_keys": [
            "**T1.** cat, fish, rabbit, grey.",
            "**T2.** F, T, T, F.",
            "**T3.** 1. have got, 2. hasn't got, 3. Have / got, "
            "4. have got.",
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
            "I can describe today's weather.",
            "I can name the four seasons and 6 weather words.",
            "I can use the present continuous (*it is raining*).",
        ],
        "leadin": (
            "It is raining. Mia is wearing her yellow boots. Theo is "
            "wearing his green raincoat. Frida the fox is sitting "
            "under a plastic umbrella that she found near the bins. "
            "\"This is fine weather,\" Frida says. \"Foxes love "
            "puddles.\" \"We don't,\" Theo says, sneezing."
        ),
        "activate": (
            "**Weather window.** Look outside for 30 seconds. Write "
            "two adjectives in your notebook (sunny? cloudy? cold?)."
        ),
        "input_blocks": [
            ("Vocabulary — weather and seasons",
             "*Seasons:* spring, summer, autumn (US: fall), winter.\n"
             "*Weather:* sunny, cloudy, rainy, windy, snowy, foggy, "
             "hot, warm, cool, cold."),
            ("Grammar — present simple vs. present continuous",
             "- **Present simple** for facts and routines:\n"
             "  *It rains a lot in November.*\n"
             "- **Present continuous** (*am/is/are* + -ing) for "
             "right-now actions:\n"
             "  *It is raining.* / *Mia is wearing her boots.*\n\n"
             "Spelling for -ing:\n"
             "*sit → sitting*, *make → making*, *run → running*, "
             "*play → playing*."),
        ],
        "practise_g": [
            "1. It __________ (rain) right now.",
            "2. The wind __________ (be) cold today.",
            "3. We __________ (wear) coats.",
            "4. In summer it __________ (be) hot.",
        ],
        "practise_m": [
            "5. (look outside) → ___",
            "6. (today: cloudy and cool) → ___",
            "7. (autumn: leaves / fall) → ___",
        ],
        "answer_g": "1. is raining, 2. is, 3. are wearing, 4. is.",
        "answer_m": (
            "5. *Look outside — it is raining.* (any present cont.)\n"
            "6. *Today is cloudy and cool.*\n"
            "7. *In autumn the leaves fall.*"
        ),
        "produce": (
            "**Weather diary — one week.** For seven days at home, "
            "write one sentence per day in English: *Today it is …*"
        ),
        "produce_sample": (
            "*Monday: Today it is sunny and warm.*\n"
            "*Tuesday: Today it is raining.*\n"
            "*Wednesday: Today it is windy and cold.*"
        ),
        "reflect": [
            "I can describe today's weather.",
            "I can name four seasons and six weather words.",
            "I can use the present continuous for *right now*.",
        ],
        "pitfalls": [
            "*It is rain* → ✗ / *It is raining* → ✓.",
            "*It rains today* (general fact) vs. *It is raining "
            "today* (right now) — context matters.",
            "L1 trap: German has no real -ing form; you must add "
            "*am/is/are* + -ing in English.",
        ],
        "further": [
            "BBC Learning English — *Weather*. <https://www.bbc.co.uk/learningenglish>",
            "Met Office Kids — *Weather words*. <https://www.metoffice.gov.uk>",
        ],
        "exam_listening": (
            "Listen twice to the weather forecast for the week.\n\n"
            "> \"Monday will be sunny. Tuesday: rain in the morning. "
            "Wednesday: windy and cool. Thursday: snow possible. "
            "Friday: cloudy.\"\n\n"
            "1. Monday: ___ , 2. Tuesday: ___ , 3. Wednesday: ___ , "
            "4. Friday: ___ ."
        ),
        "exam_reading": (
            "Read.\n\n"
            "> \"Today is November 15. It is cold and grey. There is "
            "no sun. The trees have lost their leaves.\"\n\n"
            "T or F: 1. It is summer. 2. It is cold. 3. The sun is "
            "shining. 4. The trees have leaves."
        ),
        "exam_use": (
            "**Present simple or present continuous?**\n\n"
            "1. Right now: it __________ (snow).\n"
            "2. In Stuttgart it often __________ (rain) in November.\n"
            "3. Today the children __________ (wear) coats.\n"
            "4. In summer we __________ (go) to the lake."
        ),
        "exam_writing": (
            "Write 4 sentences: today's weather + your favourite "
            "season + one thing you do in that season."
        ),
        "exam_keys": [
            "**T1.** sunny, rain, windy/cool, cloudy.",
            "**T2.** F, T, F, F.",
            "**T3.** 1. is snowing, 2. rains, 3. are wearing, 4. go.",
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
            "I can name 8 hobbies and 6 sports.",
            "I can ask and answer about hobbies (*Do you …?*).",
            "I can use *can / can't* to say what I am able to do.",
        ],
        "leadin": (
            "Theo plays football on Saturdays. Mia reads books in "
            "her room. Frida the fox does nothing in particular. "
            "\"Doing nothing is a hobby,\" Frida explains. \"For "
            "foxes it's a serious skill.\""
        ),
        "activate": (
            "**Mime corner.** The teacher mimes a hobby (reading, "
            "swimming, painting, cycling, dancing). Class shouts the "
            "English word."
        ),
        "input_blocks": [
            ("Vocabulary — hobbies and sports",
             "*Hobbies:* reading, drawing, painting, dancing, "
             "playing the guitar, playing video games, cooking, "
             "gardening.\n"
             "*Sports:* football, basketball, tennis, swimming, "
             "running, cycling, skateboarding."),
            ("Grammar — *can / can't*",
             "*Can* + base verb expresses ability or permission.\n\n"
             "- *I can swim.* / *I can't swim.*\n"
             "- *Can you ride a bike?* — *Yes, I can. / No, I can't.*\n"
             "- *He can play the guitar.* (no -s on can; no -s on "
             "play)"),
        ],
        "practise_g": [
            "1. I __________ swim. (can) 2. He __________ play "
            "tennis. (negative)",
            "3. ___ you ride a bike?",
            "4. Mia __________ play the guitar.",
        ],
        "practise_m": [
            "5. (write three sentences about what you can / can't do)",
        ],
        "answer_g": "1. can, 2. can't / cannot, 3. Can, 4. can.",
        "answer_m": "5. Open.",
        "produce": (
            "**Pair speaking — *Find someone who*.** Walk around "
            "with a list: *Find someone who can ride a unicycle / "
            "play chess / dance / swim 50 metres / draw a horse*. "
            "Write the names."
        ),
        "produce_sample": (
            "*— Can you ride a unicycle?* / *— No, I can't. Can you "
            "draw a horse?* / *— Yes, a small one.*"
        ),
        "reflect": [
            "I can name 8 hobbies and 6 sports.",
            "I can use *can / can't* correctly.",
            "I can ask 5 *Can you…?* questions.",
        ],
        "pitfalls": [
            "*He cans swim* → ✗ — *can* never takes -s.",
            "*I can to swim* → ✗ — *can* + base verb only.",
            "Pronunciation: *can* and *can't* are easy to mix up; "
            "*can't* is longer and stronger.",
        ],
        "further": [
            "BBC Learning English — *Hobbies*. <https://www.bbc.co.uk/learningenglish>",
            "LearnEnglish Kids — *Sports* games and songs.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"I can swim and I can ride a bike, but I can't play "
            "the guitar. My brother can play the guitar very well, "
            "but he can't swim.\"\n\n"
            "T or F: 1. I can swim. 2. I can play the guitar. "
            "3. My brother can swim. 4. My brother plays the "
            "guitar well."
        ),
        "exam_reading": (
            "Read.\n\n"
            "> \"Mia loves reading and drawing. She can paint very "
            "well. She can't play any instrument. On Saturdays she "
            "goes cycling with her brother.\"\n\n"
            "1. Two hobbies of Mia: ___ . 2. One thing she can do "
            "well: ___ . 3. One thing she cannot do: ___ . "
            "4. Saturday: ___ ."
        ),
        "exam_use": (
            "**Fill in *can / can't*.**\n\n"
            "1. I __________ swim, but I __________ swim 100 metres.\n"
            "2. ___ you ride a bike?\n"
            "3. Theo __________ play the guitar very well."
        ),
        "exam_writing": (
            "Write 4 sentences about your hobbies: two things you "
            "can do, one you can't, one you would like to learn."
        ),
        "exam_keys": [
            "**T1.** T, F, F, T.",
            "**T2.** reading and drawing; paint; play any "
            "instrument; she goes cycling.",
            "**T3.** 1. can / can't, 2. Can, 3. can.",
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
            "I can give and accept an invitation in English.",
            "I can name dates (months and ordinal numbers).",
            "I can write a short birthday invitation card.",
        ],
        "leadin": (
            "Mia's birthday is on the 17th of March. She is making "
            "invitations on bright pink paper. Theo says pink is "
            "embarrassing. Mia hands him a stack to deliver. "
            "\"Embarrassing is part of being a brother,\" she says. "
            "Frida steals one for the foxes."
        ),
        "activate": (
            "**Date chant.** Class repeats together:\n"
            "*January, February, March, April, May, June, July, "
            "August, September, October, November, December.*"
        ),
        "input_blocks": [
            ("Vocabulary — months and ordinals",
             "*Months:* January … December.\n"
             "*Ordinals:* first (1st), second (2nd), third (3rd), "
             "fourth (4th), fifth (5th), … twelfth (12th), thirteenth "
             "(13th), … twentieth (20th), twenty-first (21st), …, "
             "thirtieth (30th), thirty-first (31st)."),
            ("Grammar — dates and prepositions of time",
             "- *My birthday is **on** the 17th of March.* / *on "
             "March 17.*\n"
             "- *I am 11 **in** March.*\n"
             "- *We have school **at** 8 a.m.*\n"
             "- *The party is **on Saturday at** 3 p.m.*"),
            ("Invitation phrases",
             "- *Would you like to come to my party?*\n"
             "- *I'd love to. Thanks!*\n"
             "- *Sorry, I can't. I'm busy.*\n"
             "- *See you on Saturday!*"),
        ],
        "practise_g": [
            "1. My birthday is __________ March. (in / on)",
            "2. The party is __________ Saturday. (in / on)",
            "3. We start __________ 3 p.m. (at / on)",
            "4. Match: 17 → ___ , 21 → ___ , 30 → ___ .",
        ],
        "practise_m": [
            "5. *Build the question:* (your birthday — when?) → ___",
            "6. *Build the invitation:* (party / Saturday / 3 p.m.) → ___",
        ],
        "answer_g": (
            "1. in, 2. on, 3. at.\n"
            "4. 17 → seventeenth, 21 → twenty-first, "
            "30 → thirtieth."
        ),
        "answer_m": (
            "5. *When is your birthday?*\n"
            "6. *Would you like to come to my party on Saturday at "
            "3 p.m.?*"
        ),
        "produce": (
            "**Make a birthday card.** A6 paper. Front: a drawing. "
            "Inside: a 4-line invitation (date, time, place, RSVP). "
            "Swap with a partner — they accept or politely decline."
        ),
        "produce_sample": (
            "*Hi Theo, I would like to invite you to my birthday "
            "party. It's on Saturday, 17 March, at 3 p.m. at my "
            "house. Please let me know if you can come. Mia.*"
        ),
        "reflect": [
            "I can name the 12 months.",
            "I can use *in / on / at* with dates and times.",
            "I can write a short invitation.",
        ],
        "pitfalls": [
            "*at March* → ✗ / *in March* → ✓.",
            "*on 5 o'clock* → ✗ / *at 5 o'clock* → ✓.",
            "L1 trap: German *am 17. März* → English *on 17 March* "
            "or *on the seventeenth of March*.",
        ],
        "further": [
            "BBC Learning English — *Months and dates*.",
            "British Council — *Birthday party invitation* template.",
        ],
        "exam_listening": (
            "Listen twice to Mia's invitation.\n\n"
            "> \"Hi Lina, my party is on Saturday, 17 March, at 3 "
            "p.m. at my house. Can you come?\"\n\n"
            "1. Day: ___ , 2. Date: ___ , 3. Time: ___ , 4. Place: "
            "___ ."
        ),
        "exam_reading": (
            "Read the card and answer.\n\n"
            "> \"Dear Mia, thank you for the invitation. I would "
            "love to come on Saturday. See you at 3! Love, Lina.\"\n\n"
            "1. Lina says yes / no? 2. Day? 3. Time? 4. Closing "
            "word: ___ ."
        ),
        "exam_use": (
            "**Fill in *in, on, at*.**\n\n"
            "1. My birthday is __________ April.\n"
            "2. The party is __________ 5 May.\n"
            "3. We meet __________ 4 p.m.\n"
            "4. School starts __________ September."
        ),
        "exam_writing": (
            "Write a 5-line birthday invitation: greeting, date, "
            "time, place, sign-off."
        ),
        "exam_keys": [
            "**T1.** Saturday, 17 March, 3 p.m., her house.",
            "**T2.** yes, Saturday, 3 p.m., Love.",
            "**T3.** 1. in, 2. on, 3. at, 4. in.",
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
            "I can name 6 famous London places.",
            "I can ask for and give simple directions.",
            "I can read a short tourist leaflet and pick out 3 facts.",
        ],
        "leadin": (
            "Mia's class is in London on a school trip. Big Ben is "
            "louder than she expected. The pigeons are bigger. The "
            "buses are red and have two floors. Theo wants to ride "
            "on the top of every bus they see. Mr. Flint says: \"We "
            "have a list. We follow the list.\""
        ),
        "activate": (
            "**London quiz — five guesses.** With your partner, "
            "name: a river, a tower, a famous palace, a museum, a "
            "famous square."
        ),
        "input_blocks": [
            ("Vocabulary — London landmarks",
             "*Big Ben, the Tower of London, Tower Bridge, "
             "Buckingham Palace, Trafalgar Square, the British "
             "Museum, the London Eye, the Thames.*"),
            ("Useful phrases — directions",
             "- *Excuse me, where is …?*\n"
             "- *Go straight on.*\n"
             "- *Turn left / right.*\n"
             "- *It's on your left / right.*\n"
             "- *Take the second street on the right.*"),
            ("Reading — A class trip",
             "We arrived at King's Cross at 10 a.m. The first stop "
             "was the British Museum. Theo wanted to see the "
             "mummies. Mia wanted to see the clocks. We had lunch "
             "in a small park. After lunch we walked across Tower "
             "Bridge. The river was grey, but the bridge was bright "
             "blue. At 5 p.m. we took the train back."),
        ],
        "practise_g": [
            "1. Match: Big Ben — clock, Buckingham Palace — queen, "
            "Tower Bridge — river. (T / F)",
            "2. Excuse me, where __________ the museum? (be)",
            "3. Go __________ on. (right / straight)",
            "4. Turn __________ at the corner. (right / on)",
        ],
        "practise_m": [
            "5. (you / give / direction to bus stop / two streets / "
            "right) → ___",
            "6. (you / ask / the way to Big Ben) → ___",
        ],
        "answer_g": (
            "1. all true.\n"
            "2. is.\n"
            "3. straight.\n"
            "4. right."
        ),
        "answer_m": (
            "5. *Go straight on. Take the second street on the "
            "right. The bus stop is on your left.*\n"
            "6. *Excuse me, how do I get to Big Ben?*"
        ),
        "produce": (
            "**London-trip plan.** In groups of 3, plan a 6-hour "
            "London day. Choose 4 places. Write a small itinerary "
            "(time, place, activity)."
        ),
        "produce_sample": (
            "*10:00 — British Museum (mummies). 11:30 — walk to "
            "Trafalgar Square. 12:30 — lunch. 14:00 — London Eye. "
            "16:00 — train back.*"
        ),
        "reflect": [
            "I can name 6 London landmarks.",
            "I can ask for and give a simple direction.",
            "I can read a short tourist text and find 3 facts.",
        ],
        "pitfalls": [
            "*Big Ben is a tower / clock* — actually a bell; the "
            "tower is the *Elizabeth Tower*.",
            "Stereotype check: avoid *all British people drink tea*.",
            "L1 trap: German *Wo ist der Bahnhof?* maps to *Where "
            "is the station?* — no extra *do*.",
        ],
        "further": [
            "VisitLondon — accessible city overview. <https://www.visitlondon.com>",
            "British Museum (free) — <https://www.britishmuseum.org>",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"Excuse me, where is Trafalgar Square? Go straight "
            "on for two minutes. Then turn left. The square is on "
            "your right.\"\n\n"
            "1. The visitor asks about ___ .\n"
            "2. First, go ___ .\n"
            "3. Then turn ___ .\n"
            "4. The square is on the ___ ."
        ),
        "exam_reading": (
            "Read about Mia's trip.\n\n"
            "> \"In London I saw Big Ben, the London Eye, and Tower "
            "Bridge. My favourite was the London Eye, because the "
            "view was amazing.\"\n\n"
            "1. Three places: ___ . 2. Favourite: ___ . 3. Why: ___ ."
        ),
        "exam_use": (
            "**Choose: *in / on / at*.**\n\n"
            "1. ___ London, 2. ___ the bridge, 3. ___ 5 p.m., "
            "4. ___ the museum (= inside)."
        ),
        "exam_writing": (
            "Write 4–6 sentences about a city trip you would like "
            "to take. Include 3 places."
        ),
        "exam_keys": [
            "**T1.** Trafalgar Square, straight on, left, right.",
            "**T2.** Big Ben / London Eye / Tower Bridge; London "
            "Eye; the view was amazing.",
            "**T3.** 1. in, 2. on, 3. at, 4. in.",
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
        ],
        "objectives": [
            "I can name 10 clothes and 8 colours.",
            "I can describe what someone is wearing using present "
            "continuous.",
            "I can use simple comparisons (*bigger, smaller, same "
            "colour as*).",
        ],
        "leadin": (
            "Theo cannot find his blue jumper. \"It was here this "
            "morning,\" he says. \"It is not here now.\" Frida steps "
            "out of the wardrobe wearing a small blue jumper that "
            "fits her surprisingly well. \"Foxes get cold,\" she "
            "says. \"This is excellent fox fashion.\""
        ),
        "activate": (
            "**Colour shout.** The teacher points at items in the "
            "room; class shouts the colour."
        ),
        "input_blocks": [
            ("Vocabulary — clothes and colours",
             "*Clothes:* T-shirt, shirt, jumper, jacket, coat, "
             "trousers, jeans, skirt, dress, shoes, socks, boots, "
             "hat, scarf.\n"
             "*Colours:* red, blue, green, yellow, black, white, "
             "grey, brown, orange, pink, purple."),
            ("Grammar — present continuous for what someone is wearing",
             "- *Mia is wearing a red jumper.*\n"
             "- *Theo is wearing blue jeans and white trainers.*\n"
             "- *I am wearing a black T-shirt.*"),
            ("Comparing colours and sizes",
             "- *the same colour as*: *My T-shirt is the same colour "
             "as your hat.*\n"
             "- *bigger / smaller than*: *His shoes are bigger than "
             "mine.*"),
        ],
        "practise_g": [
            "1. Mia __________ (wear) a green jacket.",
            "2. Theo __________ (wear) blue jeans.",
            "3. Today I __________ (wear) ___ . (your real outfit)",
        ],
        "practise_m": [
            "4. Compare: my hat / your scarf — same colour. → ___",
            "5. Compare: his shoes / mine — bigger. → ___",
            "6. Describe a partner: 3 sentences with present "
            "continuous.",
        ],
        "answer_g": (
            "1. is wearing, 2. is wearing, 3. open."
        ),
        "answer_m": (
            "4. *My hat is the same colour as your scarf.*\n"
            "5. *His shoes are bigger than mine.*\n"
            "6. Open."
        ),
        "produce": (
            "**Description game.** In pairs, A closes their eyes; B "
            "describes a third classmate's outfit. A guesses who."
        ),
        "produce_sample": (
            "*— She is wearing a red T-shirt and black jeans. Her "
            "shoes are white.*\n*— Lina!*"
        ),
        "reflect": [
            "I can name 10 clothes and 8 colours.",
            "I can use present continuous for outfits.",
            "I can compare two items using *the same colour as* or "
            "*bigger than*.",
        ],
        "pitfalls": [
            "*She wear a red dress* → ✗ / *She is wearing* → ✓.",
            "*pant* (singular, US underwear) vs. *trousers* (BrE "
            "outerwear).",
            "L1 trap: German *Hose* (singular) is English *trousers* "
            "(always plural).",
        ],
        "further": [
            "BBC Learning English — *Clothes vocabulary*.",
            "British Council Kids — *Clothes* games and songs.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"Mia is wearing a yellow jumper, blue jeans, and "
            "white trainers. Theo is wearing a green T-shirt, black "
            "shorts, and brown sandals.\"\n\n"
            "1. Mia: jumper colour ___ , 2. Mia: shoes ___ , 3. Theo: "
            "T-shirt colour ___ , 4. Theo: shoes ___ ."
        ),
        "exam_reading": (
            "Read.\n\n"
            "> \"Today is a school trip day. We must wear "
            "comfortable shoes, a warm jumper, and a rain jacket. No "
            "skirts, no flip-flops.\"\n\n"
            "1. Wear ___ shoes. 2. Wear a warm ___ . 3. Bring a ___ "
            ". 4. Don't wear ___ ."
        ),
        "exam_use": (
            "**Build the present continuous.**\n\n"
            "1. (I / wear / blue / jeans) → ___\n"
            "2. (Mia / wear / red / dress) → ___\n"
            "3. (we / wear / school / uniform) → ___"
        ),
        "exam_writing": (
            "Describe what three classmates are wearing today (3–4 "
            "sentences each — total 9–12 sentences). Use present "
            "continuous."
        ),
        "exam_keys": [
            "**T1.** yellow, white trainers, green, brown sandals.",
            "**T2.** comfortable, jumper, rain jacket, skirts / "
            "flip-flops.",
            "**T3.** 1. *I am wearing blue jeans.* 2. *Mia is "
            "wearing a red dress.* 3. *We are wearing school "
            "uniform.*",
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
            "I can speak for ~60 seconds about myself in English.",
            "I can use grammar from the year (am/is/are, have got, "
            "can, present simple, present continuous) in one short "
            "talk.",
            "I can listen to a peer's talk and give one piece of "
            "feedback.",
        ],
        "leadin": (
            "Mr. Flint sets up a small stage in the classroom. \"At "
            "the end of the year,\" he says, \"each of you stands "
            "here for one minute and says something true in "
            "English.\" Frida the fox sits at the back. \"Will you "
            "speak too?\" Mia asks. Frida says, \"Foxes don't talk\" "
            "— in perfect English."
        ),
        "activate": (
            "**Three-line warm-up.** In your notebook, write:\n"
            "- *In September I …*\n"
            "- *Now I …*\n"
            "- *Next year I want to …*"
        ),
        "input_blocks": [
            ("The 60-second talk — structure",
             "1. **Then.** Where I started in September.\n"
             "2. **Now.** What I can do now.\n"
             "3. **Forward.** One thing I want to learn next year."),
            ("Sample (Niveau M, ~50 seconds)",
             "*Hello, my name is Mia. In September I couldn't say a "
             "long English sentence. Now I can talk about my family, "
             "my room, my hobbies, and my favourite season. I have "
             "got a cat called Pepper. He is six. Next year I want "
             "to read my first English short story. Thank you.*"),
            ("Useful sentence frames",
             "- *In September I …*\n- *Now I can …*\n"
             "- *I have got …*\n- *I like …*\n- *Next year I want "
             "to …*"),
        ],
        "practise_g": [
            "1. Build a 5-line talk using the frames above.",
        ],
        "practise_m": [
            "2. Build an 8-line talk: introduction, three Then/Now "
            "facts, one Forward, one polite ending.",
        ],
        "answer_g": "Open. Check sentence variety.",
        "answer_m": "Open.",
        "produce": (
            "**Class show.** Each student stands at the front for "
            "60 seconds. Bullets only — no full text. After every "
            "talk, one classmate gives feedback in one English "
            "sentence: *I noticed that …*"
        ),
        "produce_sample": "(see Input above)",
        "reflect": [
            "I can speak for 60 seconds about myself.",
            "I can use 4 grammar points from the year.",
            "I can give one English-sentence piece of feedback.",
        ],
        "pitfalls": [
            "Reading a full text aloud → flat performance. Bullets "
            "only.",
            "Mixing up *I am eleven years.* (omit *years*) — *I am "
            "eleven* OR *I am eleven years old*.",
            "Last-line nerves: practise the closing aloud at home.",
        ],
        "further": [
            "BBC Sounds — *Short Cuts*. Listen for short personal "
            "monologue models.",
            "LearnEnglish Kids — sample student videos at A1 level.",
        ],
        "exam_listening": (
            "Listen twice to Theo's 60-second talk.\n\n"
            "> \"My name is Theo. I am eleven. I have got one "
            "sister, Mia. I can play football very well. I can't "
            "swim 100 metres yet. Next year I want to learn the "
            "guitar.\"\n\n"
            "1. Age: ___ . 2. Sister's name: ___ . 3. One thing he "
            "can do: ___ . 4. One plan: ___ ."
        ),
        "exam_reading": (
            "Read Lina's text and answer.\n\n"
            "> \"Hi, I'm Lina. In September I couldn't speak much "
            "English. Now I can write a short text about my family. "
            "I have got two cats. My favourite subject is art. Next "
            "year I want to read a book in English.\"\n\n"
            "1. September: ___ . 2. Now: ___ . 3. Pets: ___ . "
            "4. Plan: ___ ."
        ),
        "exam_use": (
            "**Mixed grammar review.**\n\n"
            "1. I __________ (be) eleven.\n"
            "2. Mia __________ (have got) a cat.\n"
            "3. Right now I __________ (write) my exam.\n"
            "4. Next year I __________ (learn) the guitar."
        ),
        "exam_writing": (
            "Write your own 60-second talk text (8–12 sentences). "
            "Use *Then / Now / Forward*."
        ),
        "exam_keys": [
            "**T1.** 11, Mia, play football, learn the guitar.",
            "**T2.** couldn't speak much; can write a short text; "
            "two cats; read a book in English.",
            "**T3.** 1. am, 2. has got, 3. am writing, "
            "4. will learn / am going to learn.",
            "**T4.** Open.",
        ],
    },
]


UNIT_TPL = """---
title: "Unit {n} — {title}"
subtitle: "Track G+M · Klasse 5 · Niveau G/M"
niveau: "G+M"
klassenstufe: 5
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
**Niveau:** G/M parallel. Klassenarbeit at Niveau M (30 BE).
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

**Differentiation.** Niveau G: extra picture support and a printed
reference card. Above Niveau M: ask one extension question that
links to the next Unit.
:::

## Common pitfalls

{pitfalls}

## Further reading / listening

{further}
"""


EXAM_BODY_TPL = """::: {{.callout-warning icon=false title="Klassenarbeit — Niveau M (45 minutes)"}}
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
subtitle: "Track G+M · Klasse 5 · Niveau M · 45 Minuten"
author: "S. Le Boulanger"
niveau: "M"
klassenstufe: 5
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

**Track G+M · Klasse 5 · Niveau M · 45 Minuten**

{{{{< include _unit{nn}_{slug}_exam_body.qmd >}}}}
"""


def emit() -> None:
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

        (COURSE / f"unit{nn}_{u['slug']}.qmd").write_text(
            unit_md, encoding="utf-8")
        (COURSE / f"_unit{nn}_{u['slug']}_exam_body.qmd").write_text(
            exam_body_md, encoding="utf-8")
        (COURSE / f"unit{nn}_{u['slug']}_exam.qmd").write_text(
            exam_wrap_md, encoding="utf-8")

    print(f"Wrote {len(UNITS) * 3} files for Klasse 5 G+M Units 03-12.")


if __name__ == "__main__":
    emit()
