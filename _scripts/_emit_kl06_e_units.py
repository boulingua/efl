"""Batch-emit Track E Klasse 6 — all 12 Units.

Niveau E version of Klasse 6: shares the theme arc and cast with
G+M (Sam, Lina, Mr. Flint, Captain Cody) but with slightly richer
texts and one extra grammar nuance per Unit. Bildungsplan prefix
3.1 (Klassen 5/6 band).
"""
from __future__ import annotations
import pathlib

REPO = pathlib.Path(__file__).resolve().parent.parent
COURSE = REPO / "track_e_kl06" / "units"

UNITS = [
    {
        "n": 1, "slug": "a-new-year-at-school", "title": "A New Year at School",
        "skills": ["speaking", "writing", "language_awareness"],
        "bp": [
            "3.1.1 Soziokulturelles Orientierungswissen / Themen",
            "3.1.3.3 Sprechen – an Gesprächen teilnehmen",
            "3.1.3.5 Schreiben",
            "3.1.3.8 Verfügen über sprachliche Mittel – Grammatik",
        ],
        "objectives": [
            "I can describe my Klasse-6 timetable in 6 sentences with frequency adverbs.",
            "I can use *always / often / sometimes / rarely / never / hardly ever*.",
            "I can ask and answer about a typical school week in 90 seconds.",
        ],
        "leadin": (
            "Sam stands in the corridor of the new building. "
            "Klasse 6 has a different floor. The lockers click "
            "shut. The chemistry lab smells faintly of vinegar. "
            "Lina finds Sam staring at a noticeboard. \"Same class, "
            "different planet,\" she says. Mr. Flint walks past "
            "with a tray of test tubes, says, \"Welcome back,\" "
            "and disappears into the lab without slowing down. "
            "Klasse 6 has begun, and the building has agreed to it."
        ),
        "activate": (
            "**Two-truth check.** Tell your partner two true "
            "things and one slightly invented thing about your "
            "summer. Partner guesses which is invented. Then swap."
        ),
        "input_blocks": [
            ("Vocabulary — secondary school",
             "*lockers, the chemistry lab, the staff room, the "
             "headteacher's office, period (= Stunde), break time, "
             "free period (= Hohlstunde), homework diary, blazer "
             "(BrE), uniform, prefect, head pupil, the bell, "
             "first period, last period.*"),
            ("Grammar — frequency adverbs (full set)",
             "Adverbs of frequency by approximate %: *always 100%, "
             "usually 90%, often 70%, sometimes 50%, occasionally "
             "30%, rarely / hardly ever 5%, never 0%*.\n\n"
             "Position rule:\n"
             "- **Before** the main verb: *I always have maths on "
             "Monday.*\n"
             "- **After** *to be*: *She is sometimes late.*\n"
             "- **Between** modal/aux and main: *I have never been "
             "to Paris.*"),
        ],
        "practise_g": [
            "1. Place the adverb. *(always)* I __________ have "
            "English on Tuesday. *(rarely)* Lina __________ is "
            "late. *(never)* They __________ play chess.",
            "2. Sort by % (low → high): *occasionally, never, "
            "always, often, hardly ever, sometimes, usually*.",
        ],
        "practise_m": [
            "3. Build 5 true sentences about your week using 5 "
            "different frequency adverbs and one *to be* sentence.",
        ],
        "answer_g": (
            "1. always have / rarely is / never play.\n"
            "2. *never < hardly ever < occasionally < sometimes < "
            "often < usually < always.*"
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Pair speaking — *My Week (Niveau E)*.** 90 seconds "
            "each direction. Cover: a typical Monday, a Friday "
            "afternoon, *something I never do at school*, "
            "*something I always do at home before school*."
        ),
        "produce_sample": (
            "*— On Mondays I usually have biology first thing, "
            "which I love. I sometimes have a free period after "
            "lunch — those are the best minutes of the week.*"
        ),
        "reflect": [
            "I can place frequency adverbs correctly with main "
            "verbs and *to be*.",
            "I can sort 7 frequency adverbs by approximate %.",
            "I can hold a 90-second school-week conversation.",
        ],
        "pitfalls": [
            "*I have always maths* → ✗ / *I always have maths* → ✓.",
            "*She always is late* → ✗ / *She is always late* → ✓ "
            "(after *to be*).",
            "L1 trap: German *immer* often follows the verb; "
            "English keeps it before main verbs.",
        ],
        "further": [
            "BBC Learning English — *Adverbs of frequency*.",
            "British Council — *School routines* topic.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"In Klasse 6 we have biology twice a week, music "
            "once a week, and PE on Friday afternoon. We hardly "
            "ever have homework on Wednesday. Lunch is always at "
            "12:30.\"\n\n"
            "1. Biology: ___ . 2. PE: ___ . 3. Homework on Wed: "
            "___ . 4. Lunch: ___ ."
        ),
        "exam_reading": (
            "Read.\n\n"
            "> \"Sam usually walks to school. Sometimes he takes "
            "the bus when it rains heavily. He hardly ever gets a "
            "lift from his parents. He often arrives ten minutes "
            "early to talk to Lina at her locker.\"\n\n"
            "T or F: 1. Sam usually walks. 2. He always takes the "
            "bus. 3. He hardly ever gets a lift. 4. He often "
            "arrives early."
        ),
        "exam_use": (
            "**Place the adverb.**\n\n"
            "1. *(always)* I ___ have music on Monday.\n"
            "2. *(usually)* She ___ is on time.\n"
            "3. *(hardly ever)* They ___ play tennis.\n"
            "4. *(occasionally)* We ___ have a free period."
        ),
        "exam_writing": (
            "Write 6 sentences about your school week using 4 "
            "different frequency adverbs and at least one *to be* "
            "sentence."
        ),
        "exam_keys": [
            "**T1.** twice a week, Friday afternoon, hardly ever, 12:30.",
            "**T2.** T, F, T, T.",
            "**T3.** 1. always have, 2. is usually, 3. hardly "
            "ever play, 4. occasionally have.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 2, "slug": "on-holiday", "title": "On Holiday",
        "skills": ["listening", "speaking", "intercultural"],
        "bp": [
            "3.1.1 Soziokulturelles Orientierungswissen / Themen",
            "3.1.2 Interkulturelle kommunikative Kompetenz",
            "3.1.3.1 Hör-/Hörsehverstehen",
            "3.1.3.3 Sprechen – an Gesprächen teilnehmen",
            "3.1.3.8 Verfügen über sprachliche Mittel – Grammatik",
        ],
        "objectives": [
            "I can talk about a past holiday using past simple in 90 seconds.",
            "I can describe a place using 6+ adjectives.",
            "I can use past simple in positive, negative, and questions.",
        ],
        "leadin": (
            "Lina spent a week at the seaside in Cornwall. The sea "
            "was cold even in August. Her cousin caught one tiny "
            "crab and released it three minutes later, looking "
            "slightly betrayed. Sam stayed home and finally cleaned "
            "his desk. The desk was deeply impressed. Both of them "
            "claim to have had the better holiday, with no clear "
            "winner."
        ),
        "activate": (
            "**Map prompt.** Sticky notes on a blank world map: *one "
            "place I have been, one I want to visit, one I never "
            "want to visit.* Compare with another pair."
        ),
        "input_blocks": [
            ("Vocabulary — holidays",
             "*seaside, beach, cliffs, mountains, countryside, "
             "city break, campsite, hotel, hostel, suitcase, "
             "passport, souvenir, postcard, sunscreen, life jacket, "
             "lighthouse, harbour, ferry.*"),
            ("Grammar — past simple (positive / negative / Q)",
             "**Regular** + *-ed*: *worked, played, watched.*\n"
             "**Irregular** changes: *go → went, see → saw, eat → "
             "ate, swim → swam, take → took, have → had, find → "
             "found, fly → flew, leave → left, meet → met.*\n\n"
             "Negatives & questions: *did + base verb*.\n"
             "- *Did you go? / I didn't go.*\n"
             "- *Did she eat? / She didn't eat.*"),
        ],
        "practise_g": [
            "1. Past simple: I __________ (visit) my grandmother. "
            "We __________ (go) to the sea. We __________ (eat) "
            "fish. They __________ (find) a small crab.",
            "2. Make negative + question: *We saw a crab* → ___ ; "
            "*They went* → ___ .",
        ],
        "practise_m": [
            "3. Build 6 past-simple sentences about a real or "
            "imagined holiday: place, weather, transport, food, one "
            "fun thing, one feeling.",
        ],
        "answer_g": (
            "1. visited / went / ate / found.\n"
            "2. *We didn't see a crab. / Did we see a crab? They "
            "didn't go. / Did they go?*"
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Pair speaking — *Holiday Interview (Niveau E)*.** 90 "
            "seconds each direction. Six questions minimum: where, "
            "when, who with, weather, transport, best moment, one "
            "thing that didn't work."
        ),
        "produce_sample": (
            "*— Where did you go?* — *I went to Cornwall with my "
            "family.* — *Did anything not go to plan?* — *Yes — we "
            "missed the ferry on the second day.*"
        ),
        "reflect": [
            "I can use past simple in pos/neg/Q.",
            "I can describe a place with 6+ adjectives.",
            "I can hold a 90-second holiday interview.",
        ],
        "pitfalls": [
            "*I goed* → ✗ / *I went* → ✓ (irregular).",
            "*Did you went?* → ✗ / *Did you go?* → ✓ (after *did*, base form).",
            "Past time marker + present perfect = ✗.",
        ],
        "further": [
            "BBC Learning English — *Past simple* lessons.",
            "VisitBritain — short articles for young learners.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"Last summer Lina went to Cornwall with her family. "
            "They stayed in a small hotel near the harbour. The sea "
            "was cold but the sun was warm. They saw seals from the "
            "cliffs. They ate fish and chips on the beach.\"\n\n"
            "1. Where: ___ . 2. Stay: ___ . 3. Animal: ___ . 4. "
            "Food: ___ ."
        ),
        "exam_reading": (
            "Read.\n\n"
            "> \"Sam stayed at home last summer. He cleaned his "
            "desk, read three books, learned how to bake bread, "
            "and started a small notebook of recipes. He didn't "
            "travel, but he says it was the calmest summer of his "
            "life.\"\n\n"
            "1. Did Sam travel? ___ . 2. Three things he did: ___ . "
            "3. New skill: ___ . 4. Description: ___ ."
        ),
        "exam_use": (
            "**Past simple.**\n\n"
            "1. We __________ (visit) Cornwall.\n"
            "2. They __________ (not / go) to Spain.\n"
            "3. ___ you ___ (see) the sea?\n"
            "4. He __________ (eat) fish and chips.\n"
            "5. ___ she ___ (find) the right station?"
        ),
        "exam_writing": (
            "Write 6 sentences about a real or imagined holiday."
        ),
        "exam_keys": [
            "**T1.** Cornwall, small hotel near harbour, seals, fish and chips.",
            "**T2.** No, cleaned desk / read three books / learned to bake bread, baking bread, the calmest of his life.",
            "**T3.** 1. visited, 2. didn't go, 3. Did … see, 4. ate, 5. Did … find.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 3, "slug": "in-the-city", "title": "In the City",
        "skills": ["reading", "speaking", "language_awareness"],
        "bp": [
            "3.1.1 Soziokulturelles Orientierungswissen / Themen",
            "3.1.3.2 Leseverstehen",
            "3.1.3.3 Sprechen – an Gesprächen teilnehmen",
            "3.1.3.7 Verfügen über sprachliche Mittel – Wortschatz",
        ],
        "objectives": [
            "I can name 14 places in a city and 6 services they offer.",
            "I can give 4-step directions clearly.",
            "I can describe my favourite local place in 5 sentences.",
        ],
        "leadin": (
            "Sam and Lina meet at the fountain in the market square. "
            "The square smells of fresh bread and yesterday's rain. "
            "They have one hour before the bus and a list of three "
            "errands: the bookshop (a thank-you card), the post "
            "office (one stamp, one parcel), and a small bakery "
            "that supposedly sells the best apple pastry in town. "
            "They argue, briefly, about which to do first."
        ),
        "activate": (
            "**City map sketch.** Quick-draw your home street and "
            "four places nearby. Label them in English. Pair with a "
            "neighbour and quiz each other in *Where is …?*"
        ),
        "input_blocks": [
            ("Vocabulary — places + services",
             "*supermarket → groceries; bakery → bread + pastries; "
             "butcher → meat; post office → stamps + parcels; "
             "library → books + study spaces; pharmacy → medicine; "
             "town hall → official paperwork; cinema → films; "
             "museum → exhibitions; sports centre → swimming + "
             "football; bus stop → buses; train station → trains; "
             "playground → for younger children; bookshop → books "
             "to buy; cafe → tea + cake.*"),
            ("Phrases — multi-step directions",
             "- *Excuse me, where is …?*\n"
             "- *Go straight on for two minutes.*\n"
             "- *At the lights, turn left.*\n"
             "- *Take the second turning on the right.*\n"
             "- *It's on your left, opposite the post office.*\n"
             "- *Is it far?* — *About five minutes on foot.*"),
        ],
        "practise_g": [
            "1. Match place to service.",
            "2. Direction fill-in: Go __________ on. At the lights, "
            "turn __________ . Take the __________ turning on the "
            "right.",
        ],
        "practise_m": [
            "3. Give a 4-step direction from your school to your "
            "home.",
        ],
        "answer_g": (
            "1. open.\n"
            "2. straight / left or right / second."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Pair role-play — *Lost Tourist*.** Two minutes. One "
            "asks for three places; the other gives multi-step "
            "directions. Swap. At the end of each turn, the "
            "*tourist* repeats the directions back to verify "
            "(active listening)."
        ),
        "produce_sample": (
            "*— Excuse me, how do I get to the bookshop?* — *Go "
            "straight on for two minutes. At the lights, turn "
            "right. Take the second turning on the left. The "
            "bookshop is opposite the cafe.*"
        ),
        "reflect": [
            "I can name 14 places in town.",
            "I can give 4-step directions clearly.",
            "I can describe my favourite local place in 5 sentences.",
        ],
        "pitfalls": [
            "*Where is the post office is?* → ✗.",
            "Prefer *Turn right* over *Go right on*.",
            "*Apotheke* → *pharmacy / chemist's*.",
        ],
        "further": [
            "BBC Learning English — *Asking for directions*.",
            "British Council — *In town* topic.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"Excuse me, how do I get to the train station? Walk "
            "straight on for three minutes. Then turn left at the "
            "church. The station is on your right, opposite a "
            "small cafe.\"\n\n"
            "1. Place: ___ . 2. Walk for: ___ . 3. Turn at: ___ . "
            "4. Station is opposite: ___ ."
        ),
        "exam_reading": (
            "Read.\n\n"
            "> \"My favourite place in town is the small bakery "
            "next to the library. They open at 6 a.m. and the "
            "bread is still warm. The owner knows everyone's "
            "name and remembers everyone's favourite pastry.\"\n\n"
            "1. Where: ___ . 2. Open at: ___ . 3. Bread: ___ . "
            "4. Owner remembers: ___ ."
        ),
        "exam_use": (
            "**Fill in the right preposition.**\n\n"
            "1. The library is ___ the bookshop. (next to)\n"
            "2. The bank is ___ the church. (opposite)\n"
            "3. The cafe is ___ the corner. (on)\n"
            "4. Walk ___ on. (straight)"
        ),
        "exam_writing": (
            "Write 6 sentences describing a path from your school "
            "to your favourite local place. Use 4 direction phrases."
        ),
        "exam_keys": [
            "**T1.** train station, 3 minutes, the church, a small cafe.",
            "**T2.** next to library, 6 a.m., still warm, everyone's favourite pastry.",
            "**T3.** next to / opposite / on / straight.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 4, "slug": "food-around-the-world", "title": "Food Around the World",
        "skills": ["reading", "writing", "intercultural"],
        "bp": [
            "3.1.1 Soziokulturelles Orientierungswissen / Themen",
            "3.1.2 Interkulturelle kommunikative Kompetenz",
            "3.1.3.2 Leseverstehen",
            "3.1.3.5 Schreiben",
            "3.1.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can name 14 dishes from at least 8 countries.",
            "I can write a 6-line description of a meal with sensory detail.",
            "I can use *like / love / enjoy / hate + -ing* in 4 different sentences.",
        ],
        "leadin": (
            "Lina's class made an international food day. There "
            "were sushi rolls, samosas, falafel wraps, pierogi, "
            "tacos, jollof rice, a tray of perfect Spätzle, and "
            "two pies — one cherry, one a mystery savoury one with "
            "rosemary. Mr. Flint had two of everything, on what "
            "he called *strict research grounds*."
        ),
        "activate": (
            "**Food origin guess.** Teacher names a dish; class "
            "shouts the country. Then turn the game: a country, "
            "students name a dish."
        ),
        "input_blocks": [
            ("Vocabulary — dishes and countries",
             "*sushi (Japan), pizza (Italy), pasta (Italy), paella "
             "(Spain), curry (India), pierogi (Poland), falafel "
             "(Middle East), tacos (Mexico), jollof rice (West "
             "Africa), Spätzle (Germany), goulash (Hungary), "
             "noodles (China), pho (Vietnam), kimchi (Korea).*"),
            ("Grammar — *like + -ing / enjoy + -ing*",
             "After *like, love, enjoy, hate, prefer, mind, "
             "fancy*, use **-ing**:\n"
             "- *I enjoy cooking pasta.*\n"
             "- *She doesn't mind eating spicy food.*\n"
             "- *They prefer baking to frying.*"),
        ],
        "practise_g": [
            "1. Match country and dish (any 6 pairs).",
            "2. Fill in -ing: I enjoy __________ (cook). She doesn't "
            "mind __________ (eat) spicy. They prefer __________ "
            "(bake).",
        ],
        "practise_m": [
            "3. Build 5 sentences using *like, love, enjoy, hate, "
            "prefer* + -ing.",
        ],
        "answer_g": (
            "1. open.\n"
            "2. cooking / eating / baking."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Mini-poster — *A Dish I Love*.** A4 paper. Top: name "
            "+ country. Middle: drawing or sketch. Bottom: 6 "
            "sentences (ingredients, preparation, who eats it, "
            "occasion, sensory detail, why you love it)."
        ),
        "produce_sample": (
            "*Spätzle is a German pasta from Swabia. The dough is "
            "made of eggs, flour, and water. We press it through a "
            "small board into boiling water. We eat Spätzle with "
            "cheese and crispy onions. The smell of frying onions "
            "fills the kitchen for an hour. I love eating Spätzle "
            "on cold Sundays — it tastes like coming home.*"
        ),
        "reflect": [
            "I can name 14 dishes from 8 countries.",
            "I can use *like / enjoy / hate / prefer + -ing*.",
            "I can describe a meal in 6 sentences with sensory detail.",
        ],
        "pitfalls": [
            "*I'm enjoying cook* → ✗ / *I enjoy cooking* → ✓.",
            "*I prefer to bake* (also acceptable) vs. *I prefer baking*.",
            "L1 trap: German *gerne* maps differently to verbs.",
        ],
        "further": [
            "BBC Good Food — international recipes.",
            "British Council Kids — *Food from around the world*.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"At our food day we tried sushi from Japan, samosa "
            "from India, falafel from the Middle East, and pierogi "
            "from Poland. The most popular dish was the falafel "
            "wrap, partly because it was the warmest.\"\n\n"
            "1. Number of dishes: ___ . 2. From Japan: ___ . 3. "
            "From Poland: ___ . 4. Most popular + reason: ___ ."
        ),
        "exam_reading": (
            "Read.\n\n"
            "> \"My favourite dish is Spätzle with cheese. My "
            "grandmother makes it on cold Sundays. The dough is "
            "thick and yellow. We eat it with crispy onions on "
            "top, and the kitchen smells of fried onion for an "
            "hour.\"\n\n"
            "1. Dish: ___ . 2. Who: ___ . 3. When: ___ . 4. "
            "Sensory detail: ___ ."
        ),
        "exam_use": (
            "**Fill in the -ing form.**\n\n"
            "1. I love __________ (cook).\n"
            "2. She enjoys __________ (eat) sushi.\n"
            "3. They like __________ (bake) bread.\n"
            "4. We hate __________ (peel) onions."
        ),
        "exam_writing": (
            "Write 6 sentences about a dish you love (country, "
            "ingredients, occasion, one sensory detail, why)."
        ),
        "exam_keys": [
            "**T1.** 4, sushi, pierogi, falafel wrap / warmest.",
            "**T2.** Spätzle with cheese, grandmother, cold Sundays, smell of fried onion.",
            "**T3.** cooking / eating / baking / peeling.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 5, "slug": "daily-routines", "title": "Daily Routines",
        "skills": ["speaking", "writing", "language_awareness"],
        "bp": [
            "3.1.1 Soziokulturelles Orientierungswissen / Themen",
            "3.1.3.3 Sprechen – an Gesprächen teilnehmen",
            "3.1.3.5 Schreiben",
            "3.1.3.8 Verfügen über sprachliche Mittel – Grammatik",
        ],
        "objectives": [
            "I can describe my morning, afternoon, and evening "
            "in detail.",
            "I can use the present simple with time expressions "
            "and sequence words.",
            "I can use object pronouns (me, him, her, us, them).",
        ],
        "leadin": (
            "Sam wakes up at 6:30. Brushes teeth. Lets the cat out. "
            "Eats two pieces of toast and three slices of cheese, "
            "in that exact order. Walks to school in less than "
            "twelve minutes. Lina wakes up at 7:00, runs out the "
            "door at 7:25, and arrives at school out of breath but "
            "before the bell. Sam still doesn't understand how. "
            "Lina says: *the bell is on my side*."
        ),
        "activate": (
            "**Routine line-up.** Class lines up by *time of waking* "
            "without speaking — just signal numbers. Then by "
            "*length of breakfast*. Then by *minutes from door to "
            "school*. Three quick rounds."
        ),
        "input_blocks": [
            ("Vocabulary — daily routines (richer)",
             "*get up, wake up, brush my teeth, get dressed, have "
             "a shower, have breakfast, leave home, take the bus, "
             "start school, have a break, have lunch, finish "
             "school, do homework, have dinner, watch TV, read, "
             "go to bed.*"),
            ("Grammar — present simple + sequence words",
             "Sequence: *first, then, after that, before, "
             "afterwards, finally.*\n"
             "- *First I get up. Then I have breakfast.*\n"
             "- *After that I take the bus.*\n"
             "- *Before bed I read for ten minutes.*"),
            ("Grammar — object pronouns",
             "| Subject | Object |\n|---------|--------|\n"
             "| I | me |\n| you | you |\n| he | him |\n| she | her |\n"
             "| it | it |\n| we | us |\n| they | them |\n\n"
             "- *Sam helps me. I see her at the bus stop. Can you "
             "give him the book?*"),
        ],
        "practise_g": [
            "1. Subject → object: I → ___ ; he → ___ ; we → ___ ; "
            "they → ___ .",
            "2. Sequence fill-in: ___ I get up. ___ I have "
            "breakfast. ___ I leave home.",
        ],
        "practise_m": [
            "3. Build 6 sentences about your morning routine using "
            "5 different sequence words.",
        ],
        "answer_g": (
            "1. me / him / us / them.\n"
            "2. *First / Then / Finally* (or similar)."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Pair speaking — *Routine Swap (Niveau E)*.** 90 sec "
            "each direction. Cover morning, school, evening + one "
            "sequence-word phrase per turn. Report back to a "
            "different pair using object pronouns."
        ),
        "produce_sample": (
            "*— First I get up at 6:30. Then I have breakfast with "
            "my brother — I help him with his maths. After that we "
            "walk to school together.*"
        ),
        "reflect": [
            "I can describe my routine using 5 sequence words.",
            "I can use object pronouns correctly.",
            "I can report a partner's routine using *him/her*.",
        ],
        "pitfalls": [
            "*I get up to seven* → ✗ / *I get up at seven* → ✓.",
            "*Sam helps I* → ✗ / *Sam helps me* → ✓.",
            "Sequence words don't replace tense logic.",
        ],
        "further": [
            "BBC Learning English — *Daily routines vocabulary*.",
            "British Council Kids — *My day*.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"My name is Sam. First I get up at 6:30. Then I "
            "have breakfast at 7. Afterwards I leave home at 7:30. "
            "School starts at 8. I finish at 1:20.\"\n\n"
            "1. Get up: ___ . 2. Breakfast: ___ . 3. Leave home: "
            "___ . 4. Finish school: ___ ."
        ),
        "exam_reading": (
            "Read.\n\n"
            "> \"On Sundays Lina wakes up late. First she has a "
            "long breakfast with her family. After that she meets "
            "Sam in the park. They play chess for an hour. Finally, "
            "in the evening, she does her homework.\"\n\n"
            "1. Wake up: ___ . 2. Breakfast: ___ . 3. Park: ___ . "
            "4. Evening: ___ ."
        ),
        "exam_use": (
            "**Object pronoun.**\n\n"
            "1. I see ___ every day. (Lina = ?)\n"
            "2. He helps ___ with maths. (you and me = ?)\n"
            "3. They invite ___ to the party. (you and Lina = ?)\n"
            "4. We meet ___ at the bus stop. (Sam and Lina = ?)"
        ),
        "exam_writing": (
            "Write 6 sentences about your typical Saturday "
            "routine using 4 sequence words."
        ),
        "exam_keys": [
            "**T1.** 6:30, 7:00, 7:30, 1:20.",
            "**T2.** late, with her family, with Sam, homework.",
            "**T3.** her / us / you / them.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 6, "slug": "friends-and-feelings", "title": "Friends and Feelings",
        "skills": ["speaking", "writing", "language_awareness"],
        "bp": [
            "3.1.1 Soziokulturelles Orientierungswissen / Themen",
            "3.1.3.3 Sprechen – an Gesprächen teilnehmen",
            "3.1.3.5 Schreiben",
            "3.1.3.7 Verfügen über sprachliche Mittel – Wortschatz",
        ],
        "objectives": [
            "I can name 14 feelings (basic + nuanced).",
            "I can ask *How are you?* in 6 different ways.",
            "I can use *because*, *so*, and *although* in short reasons.",
        ],
        "leadin": (
            "Lina is in a strange mood. Sam asks why. \"I don't "
            "know,\" she says. \"I'm tired and slightly proud and "
            "a tiny bit jealous all at the same time.\" Sam nods. "
            "\"That's called Tuesday afternoon,\" he says. \"It "
            "happens to everyone.\""
        ),
        "activate": (
            "**Mood scan.** Stand on a line: *very happy* (left "
            "wall) → *very sad* (right wall). Find your spot. No "
            "talking. Teacher reads three short statements; "
            "students adjust position."
        ),
        "input_blocks": [
            ("Vocabulary — feelings (richer)",
             "*happy, sad, tired, excited, proud, nervous, scared, "
             "angry, jealous, calm, surprised, disappointed, "
             "embarrassed, grateful, frustrated, content, "
             "overwhelmed, focused.*"),
            ("Grammar — *because / so / although*",
             "**because** + reason:\n"
             "- *I'm tired **because** I went to bed late.*\n\n"
             "**so** + result:\n"
             "- *I went to bed late, **so** I'm tired.*\n\n"
             "**although** + contrast:\n"
             "- ***Although** I went to bed late, I am not tired.*"),
            ("Asking *How are you?*",
             "- *How are you?* / *How are you doing?* / *How's it "
             "going?* / *How was your day?* / *Are you OK?* / "
             "*How are things?*"),
        ],
        "practise_g": [
            "1. Match: happy — :), sad — :(, surprised — :O, "
            "tired — zzz.",
            "2. Fill in *because*, *so*, *although*: I'm hungry "
            "__________ I didn't eat. He's tired, __________ he "
            "is going to bed. ___ I am tired, I am happy.",
        ],
        "practise_m": [
            "3. Build 6 sentences with *because*, *so*, and "
            "*although* (two each) about your real day.",
        ],
        "answer_g": (
            "1. all true.\n"
            "2. because / so / Although."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Pair speaking — *Today's Mood (Niveau E)*.** 2 min "
            "each. Use 4 feelings + 1 *because* + 1 *so* + 1 "
            "*although*."
        ),
        "produce_sample": (
            "*— I'm a bit nervous because we have a maths test.*\n"
            "*— Although I'm tired, I am also proud — I worked "
            "hard last week, so today's test feels less scary.*"
        ),
        "reflect": [
            "I can name 14 feelings.",
            "I can ask *How are you?* in 6 ways.",
            "I can use *because*, *so*, *although* in reasons.",
        ],
        "pitfalls": [
            "*because + clause*; *because of + noun*: *because the "
            "rain* → ✗ / *because of the rain* / *because it was "
            "raining* → ✓.",
            "*although + clause*: *Although tired …* → "
            "informal, but in writing prefer *Although I am tired*.",
            "Pastoral note: keep prompts low-stakes.",
        ],
        "further": [
            "BBC Learning English — *Feelings and emotions*.",
            "ChildLine UK — accessible articles.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"Lina is excited because she has a school trip "
            "tomorrow. Sam is nervous because he forgot his "
            "homework. Although Mr. Flint is busy, he is calm. "
            "The cat is hungry, so it complains.\"\n\n"
            "1. Lina: ___ . 2. Sam: ___ . 3. Mr. Flint: ___ . "
            "4. The cat: ___ ."
        ),
        "exam_reading": (
            "Read.\n\n"
            "> \"Today is Friday and I am tired but happy. Tired "
            "because we had two tests. Happy because the weekend "
            "starts at 1 p.m. and my best friend is coming over. "
            "Although I have homework, I will do it tomorrow.\"\n\n"
            "1. Day: ___ . 2. Two feelings: ___ . 3. Reason for "
            "tiredness: ___ . 4. What about homework: ___ ."
        ),
        "exam_use": (
            "**Fill in *because*, *so*, *although*.**\n\n"
            "1. I'm hungry __________ I didn't eat.\n"
            "2. He's tired, __________ he is going to bed.\n"
            "3. We're excited __________ tomorrow is a trip.\n"
            "4. ___ it is raining, we are still going."
        ),
        "exam_writing": (
            "Write 6 sentences about today's mood. Use 3 feelings, "
            "*because*, *so*, and *although*."
        ),
        "exam_keys": [
            "**T1.** excited / school trip; nervous / forgot homework; calm; hungry / complains.",
            "**T2.** Friday; tired and happy; two tests; will do it tomorrow.",
            "**T3.** because / so / because / Although.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 7, "slug": "an-adventure-story", "title": "An Adventure Story",
        "skills": ["reading", "writing", "language_awareness"],
        "bp": [
            "3.1.1 Soziokulturelles Orientierungswissen / Themen",
            "3.1.3.2 Leseverstehen",
            "3.1.3.5 Schreiben",
            "3.1.3.8 Verfügen über sprachliche Mittel – Grammatik",
            "3.1.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can read a short adventure story and identify "
            "setting, characters, plot.",
            "I can use past simple and past continuous together with *while* and *when*.",
            "I can write a 100-word continuation in past tense.",
        ],
        "leadin": (
            "Sam found an old envelope behind the bookshelf. The "
            "paper was thick and yellow. Inside there was one "
            "page, half a map, and the signature *Captain Cody — "
            "1782*. The map showed an island that did not appear "
            "on any modern atlas. Sam decided not to mention it to "
            "anyone. Yet."
        ),
        "activate": (
            "**Story openers.** Three first lines from three "
            "stories on the slide. With your partner, predict what "
            "kind of story will follow each."
        ),
        "input_blocks": [
            ("Reading — *Captain Cody's Letter* (extract 1)",
             "*Dear traveller. If you are reading this, the envelope "
             "has waited a long time. The map is incomplete. The "
             "other half is hidden in a place where books and "
             "silence keep each other company. Bring courage. Bring "
             "biscuits. Don't bring a phone — it spoils the mood. "
             "Yours, Cody.*"),
            ("Grammar — *while / when* + past simple/continuous",
             "**While** + past continuous (longer action):\n"
             "- *I was reading **while** Sam was walking home.*\n\n"
             "**When** + past simple (event):\n"
             "- *I was reading **when** Sam arrived.*\n\n"
             "Form: *was/were + -ing*."),
        ],
        "practise_g": [
            "1. Past continuous: I __________ (read). Sam __________ "
            "(walk) home. They __________ (look) at the map.",
            "2. Choose *while* or *when*: ___ I was reading, the "
            "phone rang. ___ Sam was walking, it started to rain.",
        ],
        "practise_m": [
            "3. Build 4 sentences combining past continuous + past "
            "simple with *when* and *while*.",
        ],
        "answer_g": (
            "1. was reading / was walking / were looking.\n"
            "2. When / While."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Story continuation.** Write 100 words continuing "
            "*Captain Cody's Letter*. What happens next? Stay in "
            "past simple. Use one *while* and one *when*."
        ),
        "produce_sample": (
            "*Sam folded the half-map and put it under his pillow. "
            "While he was eating dinner, he kept thinking about the "
            "place 'where books and silence keep each other "
            "company'. The library, of course. When he arrived "
            "the next afternoon, the librarian was placing a stack "
            "of books on a low shelf. \"Are you looking for something "
            "old?\" she asked. Sam swallowed. \"Yes,\" he said. "
            "\"Very old.\" The librarian nodded slowly, as if she "
            "had been waiting for this exact question for years.*"
        ),
        "reflect": [
            "I can identify setting, characters, plot in a short story.",
            "I can use past simple and past continuous together.",
            "I can write a 100-word continuation.",
        ],
        "pitfalls": [
            "*When I was read* → ✗ / *was reading* → ✓.",
            "*while + past simple* feels off; prefer past continuous.",
            "Don't switch tense mid-clause without reason.",
        ],
        "further": [
            "Project Gutenberg — short adventure stories.",
            "BBC Learning English — *Past continuous*.",
        ],
        "exam_listening": (
            "Listen twice to the start of a story.\n\n"
            "> \"Sam was reading in the library when the lights "
            "suddenly went out. While he was waiting in the dark, "
            "he heard a quiet sound. Someone was opening the door "
            "very slowly.\"\n\n"
            "1. Where was Sam: ___ . 2. What happened: ___ . 3. "
            "While waiting: ___ . 4. Door: ___ ."
        ),
        "exam_reading": (
            "Read.\n\n"
            "> \"Lina found a small key in her grandmother's "
            "drawer. While she was studying it, the light caught "
            "the metal in a strange way. When she turned the key "
            "in her hand, she noticed letters carved on the side.\"\n\n"
            "1. Where: ___ . 2. While studying: ___ . 3. When she "
            "turned: ___ . 4. The key was: ___ ."
        ),
        "exam_use": (
            "**Past simple or past continuous?**\n\n"
            "1. While Lina __________ (study), the lights went out.\n"
            "2. When the lights __________ (go) out, she screamed.\n"
            "3. They __________ (read) when the bell rang.\n"
            "4. He __________ (find) a key while he __________ (clean) his desk."
        ),
        "exam_writing": (
            "Write 100 words continuing the story 'Lina's key'. "
            "Use *while* and *when* once each."
        ),
        "exam_keys": [
            "**T1.** library; lights went out; heard quiet sound; opening slowly.",
            "**T2.** grandmother's drawer; light caught metal; noticed letters; small / carved.",
            "**T3.** 1. was studying, 2. went, 3. were reading, 4. found / was cleaning.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 8, "slug": "school-around-the-world", "title": "School Around the World",
        "skills": ["reading", "writing", "intercultural"],
        "bp": [
            "3.1.1 Soziokulturelles Orientierungswissen / Themen",
            "3.1.2 Interkulturelle kommunikative Kompetenz",
            "3.1.3.2 Leseverstehen",
            "3.1.3.5 Schreiben",
            "3.1.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can compare two school days using 5 comparative forms.",
            "I can name 8 differences between schools in 3 countries.",
            "I can write a 120-word comparison letter.",
        ],
        "leadin": (
            "Lina has a pen-pal in Tokyo. Sam has a pen-pal in Cape "
            "Town. The three of them compare their school days by "
            "e-mail. Tokyo: 8:00 to 15:30, six lessons and a "
            "cleaning duty. Cape Town: 7:45 to 14:30, with a break "
            "that involves actual fruit. Stuttgart: 7:55 to 13:20, "
            "no fruit, no cleaning. \"We are very specialised,\" "
            "Lina jokes."
        ),
        "activate": (
            "**Three columns.** Board: *Stuttgart, Tokyo, Cape "
            "Town*. Class fills in 5 facts under each column."
        ),
        "input_blocks": [
            ("Reading — *Three school days*",
             "*In Tokyo, students clean their classroom every day "
             "after lessons. In Cape Town, the school year starts "
             "in January. In Stuttgart, students have free periods "
             "if a teacher is absent. In Tokyo, lunch is served at "
             "school. In Cape Town, many students bring fruit. In "
             "Stuttgart, lunch is at home or in the canteen.*"),
            ("Grammar — comparative + superlative",
             "Short adjectives: *+ -er, the + -est*: *long → "
             "longer → the longest.*\n"
             "Long adjectives: *more + adj, the most + adj*: "
             "*interesting → more interesting → the most "
             "interesting.*\n"
             "Irregular: *good → better → the best, bad → worse "
             "→ the worst.*"),
        ],
        "practise_g": [
            "1. Build comparative + superlative: long → ___ / ___ ; "
            "interesting → ___ / ___ ; good → ___ / ___ .",
            "2. Compare: Tokyo / Stuttgart / school day / longer "
            "→ ___ .",
        ],
        "practise_m": [
            "3. Build 4 comparison sentences about Stuttgart vs. "
            "Tokyo vs. Cape Town. Use one superlative.",
        ],
        "answer_g": (
            "1. longer / longest; more interesting / most "
            "interesting; better / best.\n"
            "2. *Tokyo's school day is longer than Stuttgart's.*"
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Pen-pal comparison letter.** Write 120 words to a "
            "pen-pal abroad. Use 5 comparatives and 1 superlative."
        ),
        "produce_sample": (
            "*Hi Hiro, my school day is shorter than yours, but I "
            "think yours is more interesting because you clean "
            "your classroom together every day. We don't do that, "
            "but I think it would be a better tradition than the "
            "one we have. Out of all my lessons, biology is the "
            "best — the teacher tells stories instead of lecturing. "
            "We finish at 1:20 and I am always hungrier than my "
            "brother by lunchtime, although he claims this is "
            "physically impossible.*"
        ),
        "reflect": [
            "I can build comparative + superlative forms.",
            "I can compare two school days in 4 sentences.",
            "I can write a 120-word pen-pal comparison letter.",
        ],
        "pitfalls": [
            "*more longer* → ✗ / *longer* → ✓.",
            "*more better* → ✗ / *better* → ✓.",
            "L1 trap: German *als* → English *than*.",
        ],
        "further": [
            "BBC Bitesize — *School around the world*.",
            "British Council Schools Online.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"In Tokyo, lessons start at 8:30. The day is longer "
            "than ours. Students clean their classrooms every day. "
            "The break is shorter, but lunch is served at school. "
            "The school year is also longer than ours.\"\n\n"
            "1. Tokyo start: ___ . 2. Day length: ___ . 3. Daily "
            "task: ___ . 4. Lunch: ___ ."
        ),
        "exam_reading": (
            "Read.\n\n"
            "> \"South African schools start their year in January. "
            "The summer holiday is in December. Many schools wear "
            "uniform. Lessons end earlier than in Germany, but "
            "afternoon clubs are common.\"\n\n"
            "1. Year start: ___ . 2. Summer: ___ . 3. Uniform: "
            "___ . 4. Lessons end: ___ ."
        ),
        "exam_use": (
            "**Build the comparative or superlative.**\n\n"
            "1. Tokyo's school day is __________ (long) than "
            "Stuttgart's.\n"
            "2. Cape Town's break is __________ (short) than ours.\n"
            "3. The Tokyo school year is __________ (interesting) "
            "year of all.\n"
            "4. Their cafeteria food is __________ (good) than "
            "ours."
        ),
        "exam_writing": (
            "Write 120 words to a pen-pal comparing your school "
            "day with theirs. Use 4 comparatives and 1 superlative."
        ),
        "exam_keys": [
            "**T1.** 8:30, longer than ours, clean classrooms, served at school.",
            "**T2.** January, December, common, earlier.",
            "**T3.** longer / shorter / most interesting / better.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 9, "slug": "body-and-health", "title": "Body and Health",
        "skills": ["listening", "speaking", "language_awareness"],
        "bp": [
            "3.1.1 Soziokulturelles Orientierungswissen / Themen",
            "3.1.3.1 Hör-/Hörsehverstehen",
            "3.1.3.3 Sprechen – an Gesprächen teilnehmen",
            "3.1.3.7 Verfügen über sprachliche Mittel – Wortschatz",
        ],
        "objectives": [
            "I can name 14 body parts and 8 common illnesses.",
            "I can describe symptoms in 4 sentences using *have got* + adjectives.",
            "I can hold an 8-line doctor-patient role-play.",
        ],
        "leadin": (
            "Sam wakes up with a sore throat. He drinks tea, eats "
            "honey, refuses to admit defeat, and goes to school. "
            "By the second period, he has a strong opinion about "
            "the value of staying home. By the fourth period, his "
            "classmates have made it clear that they share his "
            "opinion. Strongly."
        ),
        "activate": (
            "**Body parts mime.** Teacher says a body part; class "
            "touches it as fast as possible."
        ),
        "input_blocks": [
            ("Vocabulary — body and illness",
             "*Body:* head, hair, eye, ear, nose, mouth, tongue, "
             "neck, shoulder, arm, elbow, hand, finger, chest, "
             "stomach, back, leg, knee, ankle, foot, toe.\n"
             "*Illness:* cold, cough, flu, sore throat, headache, "
             "stomachache, earache, fever, runny nose, dizziness, "
             "rash, allergy."),
            ("Grammar — *have got* + *I'm + adjective*",
             "- *I have got a sore throat.* / *I've got a cold.*\n"
             "- *I'm tired. I'm hot. I'm dizzy. I'm exhausted.*\n"
             "- *Where does it hurt?* — *It hurts here.*"),
            ("Doctor-patient phrases",
             "- *What's the matter?* / *I don't feel well.*\n"
             "- *Let me have a look.*\n"
             "- *Take this medicine three times a day.*\n"
             "- *Stay in bed. Drink lots of water.*"),
        ],
        "practise_g": [
            "1. Match body part to image (slide).",
            "2. Build: *I / cold* → ___ ; *I / sore throat* → ___ ; "
            "*I / fever* → ___ .",
        ],
        "practise_m": [
            "3. Doctor-patient mini-dialogue: build 8 lines.",
        ],
        "answer_g": (
            "1. open.\n"
            "2. *I have a cold. I have a sore throat. I have a fever.*"
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Doctor-patient role-play (Niveau E).** In pairs, "
            "two minutes. Patient: 4+ symptoms with details. "
            "Doctor: 3 questions, 1 piece of advice. Swap."
        ),
        "produce_sample": (
            "*— What's the matter?*\n"
            "*— I have a sore throat and a slight fever. My head "
            "hurts and I feel a bit dizzy.*\n"
            "*— How long?*\n"
            "*— Since yesterday morning.*\n"
            "*— Take this medicine three times a day. Drink lots "
            "of water and stay home tomorrow.*"
        ),
        "reflect": [
            "I can name 14 body parts and 8 illnesses.",
            "I can describe symptoms in 4 sentences.",
            "I can run an 8-line doctor-patient dialogue.",
        ],
        "pitfalls": [
            "*I am cold* (= temperature) vs. *I have a cold* (= illness).",
            "*My head hurts me* → ✗ / *My head hurts* OR *I have a headache* → ✓.",
            "L1 trap: *Halsschmerzen* (plural) → *a sore throat* (singular).",
        ],
        "further": [
            "BBC Bitesize — *The body* topic.",
            "NHS Kids — accessible health information.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"Sam doesn't feel well. He has got a sore throat "
            "and a slight fever. The doctor tells him to drink warm "
            "tea, take some medicine, and stay in bed for two "
            "days.\"\n\n"
            "1. Symptom 1: ___ . 2. Symptom 2: ___ . 3. Drink: ___ . "
            "4. Days in bed: ___ ."
        ),
        "exam_reading": (
            "Read.\n\n"
            "> \"Lina has a headache and feels dizzy. She thinks "
            "it is because she didn't sleep enough. Her mother "
            "tells her to lie down for an hour and drink water.\"\n\n"
            "1. Two symptoms: ___ . 2. Reason: ___ . 3. Mother's "
            "advice: ___ . 4. Time: ___ ."
        ),
        "exam_use": (
            "**Fill in *have got* or *I'm + adjective*.**\n\n"
            "1. I __________ a sore throat.\n"
            "2. I __________ tired.\n"
            "3. He __________ a headache.\n"
            "4. We __________ exhausted."
        ),
        "exam_writing": (
            "Write an 8-line doctor-patient dialogue."
        ),
        "exam_keys": [
            "**T1.** sore throat, slight fever, warm tea, 2.",
            "**T2.** headache / dizzy, didn't sleep enough, lie down + water, one hour.",
            "**T3.** 1. have got, 2. am, 3. has got, 4. are.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 10, "slug": "travelling-by-train", "title": "Travelling by Train",
        "skills": ["listening", "reading", "language_awareness"],
        "bp": [
            "3.1.1 Soziokulturelles Orientierungswissen / Themen",
            "3.1.3.1 Hör-/Hörsehverstehen",
            "3.1.3.2 Leseverstehen",
            "3.1.3.7 Verfügen über sprachliche Mittel – Wortschatz",
        ],
        "objectives": [
            "I can understand a station announcement.",
            "I can read a train timetable and find a connection with one change.",
            "I can buy a ticket using polite phrases.",
        ],
        "leadin": (
            "Sam and Lina are at the station with three large "
            "rucksacks. The train is delayed by twelve minutes. "
            "They have read every poster on the platform twice. "
            "Mr. Flint has bought tea from a small kiosk and looks "
            "suspiciously content. \"This,\" he says, \"is the "
            "proper way to start a journey.\""
        ),
        "activate": (
            "**Station noticing.** Photo of a British station on "
            "the slide. With your partner, list 6 English words "
            "you can see."
        ),
        "input_blocks": [
            ("Vocabulary — train travel",
             "*platform, ticket office, single (BrE) / one-way "
             "(AmE), return (BrE) / round-trip (AmE), connection, "
             "departure, arrival, delay, cancelled, on time, lost "
             "property, the guard, the ticket inspector, the "
             "trolley, the waiting room, off-peak / peak.*"),
            ("Reading — a small timetable",
             "| From → To | Departure | Arrival | Platform |\n"
             "|-----------|-----------|---------|----------|\n"
             "| Stuttgart → Karlsruhe | 09:14 | 09:53 | 5 |\n"
             "| Karlsruhe → Strasbourg | 10:08 | 10:54 | 1 |\n"
             "| Strasbourg → Paris | 11:24 | 13:00 | 8 |"),
            ("Buying a ticket",
             "- *A return to Karlsruhe, please.*\n"
             "- *Single or return?*\n"
             "- *That's £18.50.*\n"
             "- *Which platform?* — *Platform 5.*\n"
             "- *When is the next train to …?*\n"
             "- *Is the train on time?*"),
        ],
        "practise_g": [
            "1. From the timetable: which platform for Karlsruhe? "
            "When does the train to Strasbourg leave?",
            "2. Match: single — one-way; return — round-trip; "
            "delayed — late; cancelled — not running.",
        ],
        "practise_m": [
            "3. Build a ticket-buying dialogue: 8 polite lines.",
        ],
        "answer_g": (
            "1. Platform 5; 10:08.\n"
            "2. all true."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Pair role-play — *At the Ticket Office (Niveau E)*.** "
            "Two minutes. Customer asks for a ticket, a platform, "
            "and the next train; clerk answers. Polite forms."
        ),
        "produce_sample": (
            "*— Hello, a return to Karlsruhe, please. Off-peak, if "
            "possible.*\n"
            "*— That's £18.50. Platform 5. The next train is in 12 "
            "minutes.*\n"
            "*— Thank you very much.*"
        ),
        "reflect": [
            "I can understand a station announcement.",
            "I can read a small timetable and find a connection.",
            "I can run an 8-line ticket-buying dialogue.",
        ],
        "pitfalls": [
            "*single ticket* (BrE) vs. *one-way ticket* (AmE).",
            "*the train is in delay* → ✗ / *the train is delayed* → ✓.",
            "L1 trap: *Gleis* → *platform*, not *track*.",
        ],
        "further": [
            "National Rail Enquiries (UK) — example timetables.",
            "BBC Learning English — *At the station*.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"This is the announcement for the 09:14 to "
            "Karlsruhe. The train will leave from Platform 5. "
            "Please mind the gap between the train and the "
            "platform. The next train to Frankfurt is delayed by "
            "ten minutes.\"\n\n"
            "1. To Karlsruhe — time: ___ . 2. Platform: ___ . 3. "
            "Watch out for: ___ . 4. Frankfurt: ___ ."
        ),
        "exam_reading": (
            "Read the timetable above. Answer.\n\n"
            "1. Platform for Karlsruhe: ___ .\n"
            "2. Departure to Strasbourg: ___ .\n"
            "3. Arrival in Paris: ___ .\n"
            "4. Total Stuttgart → Paris: ___ ."
        ),
        "exam_use": (
            "**Fill in train vocabulary.**\n\n"
            "1. A __________ to London, please. (one-way)\n"
            "2. The train from __________ 5.\n"
            "3. The train is __________ by ten minutes.\n"
            "4. The next train __________ at 09:14."
        ),
        "exam_writing": (
            "Write an 8-line ticket-office dialogue."
        ),
        "exam_keys": [
            "**T1.** 09:14, 5, the gap, delayed by 10 min.",
            "**T2.** 5, 10:08, 13:00, 3 hours 46 min.",
            "**T3.** single, platform, delayed, leaves.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 11, "slug": "captain-codys-map", "title": "Captain Cody's Map",
        "skills": ["reading", "writing", "language_awareness"],
        "bp": [
            "3.1.1 Soziokulturelles Orientierungswissen / Themen",
            "3.1.3.2 Leseverstehen",
            "3.1.3.5 Schreiben",
            "3.1.3.8 Verfügen über sprachliche Mittel – Grammatik",
            "3.1.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can understand a short narrative with embedded clues.",
            "I can use *will / going to* to plan a journey.",
            "I can write a 100-word continuation of an adventure story.",
        ],
        "leadin": (
            "Sam pieced the two halves of Captain Cody's map "
            "together on Lina's kitchen table. Half from his "
            "envelope. Half from a hollow book in the school "
            "library. The whole map showed a coastline, an X, and "
            "the words *Tomorrow's tide will tell*. Lina stared at "
            "the map. \"This is either the best or the worst week "
            "of our lives.\" Sam said, \"Both, maybe.\""
        ),
        "activate": (
            "**Map clue read.** Slide shows a small puzzle with "
            "three clues. With your partner, write down what you "
            "think the map points to."
        ),
        "input_blocks": [
            ("Reading — *Captain Cody's Map* (extract 2)",
             "*Tomorrow we are going to take the early train. We "
             "will meet at the station at 6 a.m. We will bring "
             "biscuits and a torch. We won't bring our phones — "
             "they spoil the mood. The plan: arrive, follow the "
             "coastline, count the steps from the lighthouse, and "
             "dig — but only with the lighthouse keeper's "
             "permission.*"),
            ("Grammar — *will / going to* (review)",
             "**will** for predictions and spontaneous decisions:\n"
             "- *I will help you with that.*\n\n"
             "**be going to** for plans and visible evidence:\n"
             "- *We are going to take the early train.*\n\n"
             "Time clauses: *when, as soon as, before* + present "
             "simple."),
        ],
        "practise_g": [
            "1. Choose: *will* or *going to*: We have already booked "
            "tickets — we __________ travel tomorrow. Look at the "
            "clouds — it __________ rain.",
            "2. Time clause: I will text you __________ I arrive.",
        ],
        "practise_m": [
            "3. Build 4 sentences: two with *going to* (plans) and "
            "two with *will* (predictions).",
        ],
        "answer_g": (
            "1. are going to / is going to.\n"
            "2. as soon as."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Story continuation.** Write 100 words continuing "
            "*Captain Cody's Map*. Use *going to* and *will*."
        ),
        "produce_sample": (
            "*Sam and Lina arrived at the lighthouse at 7:30. The "
            "keeper was already up. \"You're going to need a "
            "shovel,\" he said quietly, before they had asked "
            "anything. \"And probably more biscuits than that.\" "
            "He gave them a small, worn shovel and a paper bag of "
            "ginger biscuits. \"I'll be in the garden,\" he said. "
            "\"Shout when you find something. Or when you give up. "
            "Either way, I will be making tea by the time you come "
            "back.\"*"
        ),
        "reflect": [
            "I can read a story with embedded clues.",
            "I can use *will / going to* correctly.",
            "I can write a 100-word continuation.",
        ],
        "pitfalls": [
            "*I will to do* → ✗ / *I will do* → ✓.",
            "*I am going to will* → ✗.",
            "*when I will arrive* → ✗ / *when I arrive* → ✓.",
        ],
        "further": [
            "Project Gutenberg — children's adventure stories.",
            "Roald Dahl Stories Online — extracts.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"Tomorrow we are going to take the 6 a.m. train. "
            "We will meet at the station. We're not going to bring "
            "our phones. We will bring biscuits and a torch.\"\n\n"
            "1. Train time: ___ . 2. Meeting place: ___ . 3. Won't "
            "bring: ___ . 4. Will bring: ___ ."
        ),
        "exam_reading": (
            "Read.\n\n"
            "> \"Captain Cody's note ended with: 'When you find the "
            "X, dig only with permission. The keeper of the "
            "lighthouse will know what to do. Don't try at "
            "night.'\"\n\n"
            "1. Find: ___ . 2. Permission: ___ . 3. Knows: ___ . "
            "4. Not at: ___ ."
        ),
        "exam_use": (
            "**Fill in *will* or *going to*.**\n\n"
            "1. We __________ (travel) tomorrow. (planned)\n"
            "2. Look! It __________ (rain).\n"
            "3. I __________ (help) you carry that.\n"
            "4. They __________ (visit) Paris in July."
        ),
        "exam_writing": (
            "Write 100 words continuing the Cody story. Use one "
            "*going to* and one *will*."
        ),
        "exam_keys": [
            "**T1.** 6 a.m., the station, phones, biscuits and a torch.",
            "**T2.** the X, the lighthouse keeper's, the keeper of the lighthouse, at night.",
            "**T3.** are going to travel / is going to rain / will help / are going to visit.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 12, "slug": "year-end-festival", "title": "Year-End Festival",
        "skills": ["speaking", "writing", "intercultural"],
        "bp": [
            "3.1.1 Soziokulturelles Orientierungswissen / Themen",
            "3.1.3.4 Sprechen – zusammenhängendes monologisches Sprechen",
            "3.1.3.5 Schreiben",
            "3.1.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can speak for 90 seconds about my Klasse-6 year.",
            "I can use grammar from the year (past simple, "
            "comparatives, will/going to, frequency adverbs, "
            "because/so/although).",
            "I can host a small year-end festival event in English.",
        ],
        "leadin": (
            "The class is planning a year-end festival in the "
            "school courtyard. Lina is in charge of the snack "
            "table. Sam is in charge of the music. Mr. Flint is in "
            "charge of looking calmly worried, which he does "
            "professionally. Captain Cody is in charge of nothing, "
            "because he is fictional, but everyone agrees his "
            "treasure-map-themed games stand will be the most "
            "popular."
        ),
        "activate": (
            "**Year-end scan.** In your notebook write three lines: "
            "*In September I …, Now I …, At the festival I will …*"
        ),
        "input_blocks": [
            ("The 90-second talk — Klasse 6 version",
             "1. **Then.** Where I started in Klasse 6.\n"
             "2. **Now.** Three things I can do (with one concrete example).\n"
             "3. **Forward.** What I will do at the festival or next year."),
            ("Festival vocabulary",
             "*stall, stand, performance, snack table, raffle, "
             "decoration, banner, hosting, MC (master of "
             "ceremonies), volunteers, headphones, microphone, "
             "applause, crowd, queue, demonstration.*"),
        ],
        "practise_g": [
            "1. Build a 6-line festival talk using *Then / Now / Forward*.",
        ],
        "practise_m": [
            "2. Build a 90-second talk using past simple, one "
            "comparative, *going to*, and one frequency adverb.",
        ],
        "answer_g": "Open.",
        "answer_m": "Open.",
        "produce": (
            "**Festival rehearsal.** In groups of 4, rehearse your "
            "stall. Each person prepares one short statement (15 "
            "seconds) explaining what their stall is, plus one "
            "polite invitation to a visitor."
        ),
        "produce_sample": (
            "*Welcome to the snack table! We are going to have "
            "homemade pretzels and English scones today. Would you "
            "like to try one? They are warmer than they look.*"
        ),
        "reflect": [
            "I can speak for 90 seconds about my Klasse-6 year.",
            "I can use 5 grammar points in one talk.",
            "I can host a stall at a year-end festival.",
        ],
        "pitfalls": [
            "Reading aloud word-for-word; bullets only.",
            "Vague claims; give a concrete example instead.",
            "*Welcome at* → ✗ / *Welcome to* → ✓.",
        ],
        "further": [
            "BBC Sounds — *Short Cuts*.",
            "British Council Schools Online — festival ideas.",
        ],
        "exam_listening": (
            "Listen twice to Lina's festival speech.\n\n"
            "> \"Hello everyone, welcome to the snack table! In "
            "September I couldn't bake bread. Now I can bake "
            "scones. They are tastier than my first attempts. "
            "Tomorrow we are going to sell them for one euro each. "
            "Please come and try one!\"\n\n"
            "1. September: ___ . 2. Now: ___ . 3. Tastier than: "
            "___ . 4. Price: ___ ."
        ),
        "exam_reading": (
            "Read.\n\n"
            "> \"At the festival there will be six stalls: a "
            "bookshop, a snack table, a music corner, a games "
            "stand, a treasure-hunt stall, and a photography "
            "booth. The festival starts at 4 p.m. and ends at 7 "
            "p.m.\"\n\n"
            "1. Number of stalls: ___ . 2. Two stalls: ___ . 3. "
            "Start: ___ . 4. End: ___ ."
        ),
        "exam_use": (
            "**Mixed grammar review.**\n\n"
            "1. Last summer I __________ (visit) Cornwall.\n"
            "2. The festival is __________ (interesting) than last year's.\n"
            "3. Tomorrow we __________ (sell) scones. (planned)\n"
            "4. We __________ (always / start) at 4 p.m."
        ),
        "exam_writing": (
            "Write 100 words: your festival stall, one Klasse-6 "
            "achievement, and what you will do next year."
        ),
        "exam_keys": [
            "**T1.** couldn't bake, can bake scones, first attempts, one euro.",
            "**T2.** 6, any two, 4 p.m., 7 p.m.",
            "**T3.** visited / more interesting / are going to sell / always start.",
            "**T4.** Open.",
        ],
    },
]


UNIT_TPL = """---
title: "Unit {n} — {title}"
subtitle: "Track E · Klasse 6 · Niveau E"
niveau: "E"
klassenstufe: 6
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

**One thing in your notebook:** *Write one sentence using something you learned in this Unit.*

## Exam example

{{{{< include _unit{nn}_{slug}_exam_body.qmd >}}}}

## Downloads

{{{{< downloads >}}}}

::: {{.notes}}
**Slide deck timing.** 45 minutes total. Lead-in 3 min · Activate
4 min · Input 12 min · Practise 8 min · Produce 13 min · Reflect 5 min.

**Differentiation.** Below Niveau E (mixed group): provide a support
card. Above Niveau E: extension question linking to the next Unit.
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
subtitle: "Track E · Klasse 6 · Niveau E · 45 Minuten"
author: "S. Le Boulanger"
niveau: "E"
klassenstufe: 6
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

**Track E · Klasse 6 · Niveau E · 45 Minuten**

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

    print(f"Wrote {len(UNITS) * 3} files for Track E Klasse 6.")


if __name__ == "__main__":
    emit()
