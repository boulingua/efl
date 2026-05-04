"""Batch-emit Track E Klasse 11 — all 12 Units (gymnasiale Oberstufe).

Klasse 11 voice: cultural entry, literary voice, exam-prep tagging
between basic course (Basisfach, E-BF) and advanced course
(Leistungsfach, E-LF). Cast: *narrators and author voices* — the
Klasse-11 cast is the texts themselves. curriculum framework
(Bildungsplan) prefix 3.4 (Leistungsfach) and 3.5 (Basisfach).

Klausur replaces class test (Klassenarbeit). Format scales: 90 BE
(Comprehension ≈ 24 + Analysis ≈ 18 + Composition ≈ 18 + Mediation
≈ 30). Inhalt / Sprache split: 50 / 50 (BF) or 40 / 60 (LF).
"""
from __future__ import annotations
import pathlib

REPO = pathlib.Path(__file__).resolve().parent.parent
COURSE = REPO / "track_e_kl11" / "units"

UNITS = [
    {
        "n": 1, "slug": "british-cultural-anchors",
        "title": "British Cultural Anchors",
        "skills": ["reading", "writing", "intercultural"],
        "bp": [
            "3.4.1 / 3.5.1 Soziokulturelles Orientierungswissen / Themen",
            "3.4.2 / 3.5.2 Interkulturelle kommunikative Kompetenz",
            "3.4.3.2 / 3.5.3.2 Leseverstehen",
            "3.4.3.5 / 3.5.3.5 Schreiben",
            "3.4.4 / 3.5.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can read a short cultural-history essay on a British anchor (the welfare state, the BBC, or the National Trust) and identify the writer's argumentative move.",
            "I can use formal academic discourse markers (*by contrast, accordingly, in this regard, more specifically*).",
            "I can write a 250-word cultural-essay paragraph that goes past tourist-image cliché.",
        ],
        "leadin": (
            "Klasse 11 opens with three short cultural-history "
            "essays: one on the BBC, one on the post-1945 welfare "
            "state, one on the National Trust. The class read all "
            "three, then argued for forty minutes about which one "
            "was the *most British*. The teacher said: *correct "
            "answer — none of them on its own*."
        ),
        "activate": (
            "**Anchor scan.** With your partner, list 5 British "
            "cultural anchors that are *not* tourist images. Mark "
            "each: *deeply British / partly British / British by "
            "global accident*."
        ),
        "input_blocks": [
            ("Reading — *The BBC, in Three Sentences*",
             "*The BBC was founded in 1922 as a private company and "
             "incorporated by Royal Charter in 1927. Its public-"
             "service mandate, often summarised as *inform, "
             "educate, entertain*, has been the source of constant "
             "argument and constant funding fights. By contrast "
             "with most national broadcasters, it is funded by a "
             "household licence fee — a model that is, accordingly, "
             "both unusual and politically vulnerable.*"),
            ("Discourse markers (formal academic)",
             "*by contrast / accordingly / in this regard / more "
             "specifically / it is worth noting that / it follows "
             "that / on this account / to put it differently.*"),
            ("Vocabulary — cultural-history register",
             "*charter, mandate, public-service, broadcaster, "
             "licence fee, devolved, post-war, founding moment, "
             "settlement, institutional resilience, soft power.*"),
        ],
        "practise_g": [
            "1. Choose discourse marker: *(contrast)* → ___ ; "
            "*(consequence)* → ___ ; *(specification)* → ___ .",
            "2. Match: charter → founding document; licence fee → "
            "funding model; soft power → cultural influence.",
        ],
        "practise_m": [
            "3. Build 4 sentences about a British anchor using "
            "4 different discourse markers.",
        ],
        "answer_g": (
            "1. by contrast / accordingly / more specifically.\n"
            "2. all true."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Cultural-essay paragraph, 250 words.** Pick one "
            "British anchor (BBC / NHS / National Trust / "
            "Parliament). Write a single argumentative paragraph "
            "with one claim, two pieces of evidence, and one "
            "concession. Use 4 academic discourse markers."
        ),
        "produce_sample": (
            "*The BBC is often described, accurately and lazily, as "
            "*the most British institution*. The accurate part is "
            "that the household licence fee places the BBC, by "
            "contrast with most national broadcasters, in a "
            "structural relationship to the public that is unusual: "
            "every household pays directly for an institution none "
            "of them owns. Accordingly, the BBC's editorial "
            "pressures are unusual too — it is criticised "
            "simultaneously by all major political camps, which is "
            "either a sign of balance or of a particular kind of "
            "blandness, depending on whom you ask. More "
            "specifically, the *inform-educate-entertain* mandate "
            "from 1927 survives because it is vague enough to be "
            "useful and old enough to be defensible. In this "
            "regard, the BBC's resilience is the resilience of an "
            "institution that has been continuously slightly "
            "embarrassing to power. The lazy part of calling the "
            "BBC the most British institution is that it ignores "
            "the post-1945 NHS, which has done at least as much to "
            "shape what *British* means in the second half of the "
            "twentieth century. Both are needed.*"
        ),
        "reflect": [
            "I can identify the writer's argumentative move in a cultural-history essay.",
            "I can use 4 formal academic discourse markers.",
            "I can write a 250-word cultural-essay paragraph past tourist cliché.",
        ],
        "pitfalls": [
            "Don't reduce 'British' to England. Scotland, Wales, "
            "Northern Ireland — devolved.",
            "*Most British* claims need an argument, not a flag.",
            "Don't romanticise institutions; name a specific "
            "concession.",
        ],
        "further": [
            "BBC History — accessible long-form articles.",
            "The Guardian — *Long reads* on British institutions.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"The BBC was founded in 1922 as a private company "
            "and incorporated by Royal Charter in 1927. Its "
            "*inform-educate-entertain* mandate is the source of "
            "constant funding fights. By contrast with most "
            "national broadcasters, it is funded by a household "
            "licence fee. Accordingly, it is both unusual and "
            "politically vulnerable.\"\n\n"
            "1. Founded: ___ . 2. Charter: ___ . 3. Mandate: ___ . "
            "4. Funding: ___ ."
        ),
        "exam_reading": (
            "Read the *BBC* extract above.\n\n"
            "1. Year founded: ___ . 2. Year of charter: ___ . 3. "
            "Three-word mandate: ___ . 4. Funding model: ___ ."
        ),
        "exam_use": (
            "**Insert academic discourse marker.**\n\n"
            "1. ___ , the BBC is funded by a household licence "
            "fee.\n"
            "2. ___ , the BBC has been politically vulnerable.\n"
            "3. ___ , the *inform-educate-entertain* mandate is "
            "vague enough to survive.\n"
            "4. ___ , the lazy part is the comparison with the NHS."
        ),
        "exam_writing": (
            "Write 250 words: a cultural-essay paragraph on a "
            "British anchor. Use 4 academic discourse markers."
        ),
        "exam_keys": [
            "**T1.** 1922; 1927; *inform, educate, entertain*; household licence fee.",
            "**T2.** 1922; 1927; *inform, educate, entertain*; household licence fee.",
            "**T3.** By contrast / Accordingly / More specifically / In this regard.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 2, "slug": "the-american-dream",
        "title": "The American Dream",
        "skills": ["reading", "writing", "intercultural"],
        "bp": [
            "3.4.1 / 3.5.1 Soziokulturelles Orientierungswissen / Themen",
            "3.4.2 / 3.5.2 Interkulturelle kommunikative Kompetenz",
            "3.4.3.2 / 3.5.3.2 Leseverstehen",
            "3.4.3.5 / 3.5.3.5 Schreiben",
            "3.4.4 / 3.5.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can read short extracts from American Dream sources (Declaration of Independence, James Truslow Adams 1931, contemporary critique) and trace one continuity and one rupture.",
            "I can use sentence-level emphasis (cleft + inversion) for argumentative writing.",
            "I can write a 280-word essay paragraph that holds two readings of the Dream in tension.",
        ],
        "leadin": (
            "The class read three short extracts: the *pursuit of "
            "happiness* line from 1776; James Truslow Adams's "
            "1931 phrase *American Dream* in *The Epic of "
            "America*; and a 2024 critique by an economist who "
            "argued that the phrase has *outlived its statistical "
            "basis*. The class spent the lesson asking: *which of "
            "these is the real one?*"
        ),
        "activate": (
            "**Three-source scan.** Match each line to a "
            "decade: 1776, 1931, 2024. Justify each match in 10 "
            "words."
        ),
        "input_blocks": [
            ("Reading — three extracts",
             "*1776 (Declaration of Independence):* *We hold these "
             "truths to be self-evident, that all men are created "
             "equal, that they are endowed by their Creator with "
             "certain unalienable Rights, that among these are "
             "Life, Liberty and the pursuit of Happiness.*\n\n"
             "*1931 (Adams, *The Epic of America*):* *The American "
             "Dream is that dream of a land in which life should be "
             "better and richer and fuller for everyone.*\n\n"
             "*2024 (economist, popular essay):* *Whatever else the "
             "American Dream is, it has, since the 1980s, "
             "outlived its statistical basis. Intergenerational "
             "income mobility in the United States is now lower "
             "than in most of comparable Western Europe.*"),
            ("Grammar — sentence emphasis (cleft + inversion)",
             "**Cleft:** *It is the 1931 phrase, not the 1776 line, "
             "that we usually mean by 'the Dream'.*\n\n"
             "**Negative inversion (formal):** *Not until the 1930s "
             "was the phrase coined.* / *Only after 1945 did the "
             "Dream become a mass image.*\n\n"
             "**Cleft (what):** *What the 2024 critique argues is "
             "that the Dream has outlived its statistical "
             "basis.*"),
        ],
        "practise_g": [
            "1. Build a cleft emphasising *the 1931 phrase*: ___ "
            "what we usually mean by 'the Dream'.",
            "2. Inversion: *Not until 1931 ___ (the phrase coin / "
            "passive)*.",
        ],
        "practise_m": [
            "3. Build 4 emphasis sentences (2 cleft + 2 "
            "inversion).",
        ],
        "answer_g": (
            "1. *It is the 1931 phrase that is what we usually "
            "mean by 'the Dream'.*\n"
            "2. *was the phrase coined.*"
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Essay paragraph, 280 words.** Hold two readings of "
            "the American Dream in tension. Use 1 cleft + 1 "
            "negative inversion + 3 academic discourse markers."
        ),
        "produce_sample": (
            "*It is the 1931 phrase, more than the 1776 line, that "
            "we usually mean when we speak of *the American "
            "Dream*. James Truslow Adams's claim — *that life "
            "should be better and richer and fuller for everyone* "
            "— is structurally different from the 1776 *pursuit of "
            "Happiness* in one important way: it is a claim about "
            "*outcomes* rather than rights. Not until the 1930s "
            "was the phrase coined; only after 1945 did the Dream "
            "harden into a mass image of single-family homes, "
            "rising wages, and a stable career. By contrast, the "
            "2024 critique argues that the Dream has, since the "
            "1980s, outlived its statistical basis: "
            "intergenerational income mobility in the United States "
            "is now lower than in most of comparable Western "
            "Europe. Accordingly, the Dream survives as a "
            "rhetorical resource even as the pattern it once "
            "described has weakened. More specifically, what the "
            "1931 phrase does well is mobilise hope; what it has "
            "stopped doing is describing reality. Both readings "
            "matter. Without the rhetorical Dream, "
            "American politics loses a shared vocabulary; without "
            "the statistical critique, that vocabulary becomes "
            "ornamental. In this regard, the most useful thing "
            "Klasse 11 readers can do is hold both — Adams's "
            "ambition and the 2024 economist's caution — without "
            "asking which is *really* the Dream.*"
        ),
        "reflect": [
            "I can trace one continuity and one rupture across three sources.",
            "I can use cleft and negative inversion for emphasis.",
            "I can write a 280-word essay holding two readings in tension.",
        ],
        "pitfalls": [
            "*The American Dream* read as one fixed object — it "
            "isn't.",
            "Negative inversion is formal — don't overuse.",
            "Don't reduce the Dream to either celebration or "
            "debunking.",
        ],
        "further": [
            "James Truslow Adams, *The Epic of America* (1931).",
            "The Atlantic — *American Dream* essay archive.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"The 1776 line speaks of the *pursuit of "
            "Happiness*. The 1931 phrase, by contrast, speaks of "
            "outcomes — *that life should be better and richer "
            "and fuller for everyone*. The 2024 critique points "
            "out that intergenerational income mobility in the US "
            "is now lower than in most of comparable Western "
            "Europe.\"\n\n"
            "1. 1776 phrase: ___ . 2. 1931 phrase: ___ . 3. 2024 "
            "claim: ___ . 4. Comparison region: ___ ."
        ),
        "exam_reading": (
            "Read the three extracts above.\n\n"
            "1. 1776 source: ___ . 2. 1931 author + book: ___ . "
            "3. 2024 critique: ___ . 4. Continuity / rupture: ___ ."
        ),
        "exam_use": (
            "**Build emphasis structures.**\n\n"
            "1. Cleft on *the 1931 phrase*: → ___\n"
            "2. Negative inversion: *Not until 1931 ___ (coin / "
            "passive)*.\n"
            "3. Cleft on *the 2024 critique*: → ___\n"
            "4. Negative inversion: *Only after 1945 ___ (the "
            "Dream / become / a mass image)*."
        ),
        "exam_writing": (
            "Write 280 words: an essay paragraph holding two "
            "readings of the Dream in tension. Use 1 cleft + 1 "
            "inversion + 3 markers."
        ),
        "exam_keys": [
            "**T1.** *pursuit of Happiness*; *life should be better and richer and fuller for everyone*; outlived its statistical basis (since 1980s); comparable Western Europe.",
            "**T2.** Declaration of Independence; James Truslow Adams, *The Epic of America*; intergenerational mobility lower than W. Europe; *pursuit of Happiness* (rights) → outcomes-language (1931) → statistical critique (2024).",
            "**T3.** *It is the 1931 phrase that we usually mean. Not until 1931 was the phrase coined. It is the 2024 critique that questions the statistical basis. Only after 1945 did the Dream become a mass image.*",
            "**T4.** Open.",
        ],
    },
    {
        "n": 3, "slug": "post-colonial-voices-intro",
        "title": "Post-Colonial Voices: An Introduction",
        "skills": ["reading", "writing", "intercultural"],
        "bp": [
            "3.4.1 / 3.5.1 Soziokulturelles Orientierungswissen / Themen",
            "3.4.2 / 3.5.2 Interkulturelle kommunikative Kompetenz",
            "3.4.3.2 / 3.5.3.2 Leseverstehen",
            "3.4.3.5 / 3.5.3.5 Schreiben",
            "3.4.4 / 3.5.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can read a short post-colonial extract (Achebe, Adichie, or Naipaul) and identify the writer's stance toward the imperial archive.",
            "I can use voice-marking phrases (*the speaker recalls, the narrator distances herself from, the text positions the reader*).",
            "I can write a 280-word literary essay that engages a post-colonial source on its own terms.",
        ],
        "leadin": (
            "The class opened a short anthology of post-colonial "
            "writing with three openings: Chinua Achebe (1958), "
            "Chimamanda Ngozi Adichie (2003), and V. S. Naipaul "
            "(1979). Three voices, three decades, one shared "
            "problem: how to write *in* English without writing "
            "*as* the English. The class did not finish the "
            "argument that day, which Mr. Yilmaz said was a sign "
            "the books were working."
        ),
        "activate": (
            "**Three-voice scan.** Match each opening to a likely "
            "decade and continent of setting. Justify in 10 words "
            "each."
        ),
        "input_blocks": [
            ("Reading — three openings (extracts)",
             "*Achebe (1958, *Things Fall Apart*):* *Okonkwo was "
             "well known throughout the nine villages and even "
             "beyond. His fame rested on solid personal "
             "achievements.*\n\n"
             "*Adichie (2003, *Purple Hibiscus*):* *Things "
             "started to fall apart at home when my brother, Jaja, "
             "did not go to communion and Papa flung his heavy "
             "missal across the room and broke the figurines on "
             "the étagère.*\n\n"
             "*Naipaul (1979, *A Bend in the River*):* *The world "
             "is what it is; men who are nothing, who allow "
             "themselves to become nothing, have no place in "
             "it.*"),
            ("Voice-marking phrases",
             "*the speaker recalls / the narrator distances "
             "herself from / the text positions the reader as / "
             "the opening lays claim to / the voice carries the "
             "weight of / the prose refuses the colonial "
             "register.*"),
        ],
        "practise_g": [
            "1. Match opening → likely setting (West Africa / "
            "post-colonial Africa with European parents / a "
            "Central African town).",
            "2. T or F: Achebe's opening foregrounds personal "
            "achievement. Adichie's opening alludes directly to "
            "Achebe's title.",
        ],
        "practise_m": [
            "3. Build 4 voice-marking sentences for the three "
            "extracts.",
        ],
        "answer_g": (
            "1. open (Achebe → 19th-c. Igbo village; Adichie → "
            "1990s Nigeria with educated middle-class parents; "
            "Naipaul → an unnamed African town).\n"
            "2. T, T."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Literary essay, 280 words.** Read all three "
            "openings. Argue that one of them does the most work "
            "with the fewest sentences. Use 4 voice-marking "
            "phrases + 1 cleft + 1 quote per source."
        ),
        "produce_sample": (
            "*Of the three openings, it is Adichie's that does the "
            "most work with the fewest sentences. The line — "
            "*Things started to fall apart at home when my brother, "
            "Jaja, did not go to communion and Papa flung his "
            "heavy missal across the room and broke the figurines "
            "on the étagère* — is a direct allusion to Achebe's "
            "1958 title, which the narrator places quietly inside "
            "her domestic frame. The opening positions the reader "
            "inside an educated middle-class Nigerian Catholic "
            "household where the *fall apart* of post-colonial "
            "fiction has migrated from village politics to the "
            "broken figurines of a domestic shelf. By contrast, "
            "Achebe's opening lays claim, with the calm of a "
            "history book, to *Okonkwo was well known throughout "
            "the nine villages and even beyond*; the prose refuses "
            "the colonial register simply by treating the village "
            "world as the centre. Naipaul's narrator, more "
            "abrasively, distances himself from sentimentality: "
            "*The world is what it is.* Each opening engages the "
            "imperial archive differently. Adichie's wins, in my "
            "reading, because the allusion is buried inside an "
            "object — the étagère — that domesticates the entire "
            "post-colonial argument into one piece of furniture. "
            "The text positions the reader as a guest in a room "
            "where something has just shattered, and the shattering "
            "is, somehow, the inheritance.*"
        ),
        "reflect": [
            "I can identify the writer's stance toward the imperial archive.",
            "I can use voice-marking phrases.",
            "I can write a 280-word literary essay engaging a post-colonial source.",
        ],
        "pitfalls": [
            "*Post-colonial* is not a synonym for *African* — it "
            "covers Caribbean, South-Asian, and other contexts.",
            "Don't celebrate or condemn — track the moves.",
            "Quote sparingly; integrate quotes inside your "
            "sentence.",
        ],
        "further": [
            "Chinua Achebe, *Things Fall Apart* (1958).",
            "Chimamanda Ngozi Adichie, *Purple Hibiscus* (2003).",
            "V. S. Naipaul, *A Bend in the River* (1979).",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"Achebe's 1958 opening lays claim, with the calm "
            "of a history book, to a village world. Adichie's "
            "2003 opening alludes to Achebe's title from inside a "
            "domestic frame. Naipaul's 1979 narrator distances "
            "himself with the line *the world is what it is*.\"\n\n"
            "1. Achebe year: ___ . 2. Achebe move: ___ . 3. "
            "Adichie move: ___ . 4. Naipaul stance: ___ ."
        ),
        "exam_reading": (
            "Read the three openings above.\n\n"
            "1. Achebe — what is foregrounded: ___ . 2. Adichie — "
            "what does the opening allude to: ___ . 3. Naipaul — "
            "describe the tone in 5 words: ___ . 4. The étagère "
            "image — its argumentative role: ___ ."
        ),
        "exam_use": (
            "**Insert voice-marking phrase.**\n\n"
            "1. ___ the calm of a history book.\n"
            "2. ___ Achebe's 1958 title.\n"
            "3. ___ from sentimentality.\n"
            "4. ___ as a guest in a room where something has "
            "shattered."
        ),
        "exam_writing": (
            "Write 280 words: a literary essay engaging the three "
            "post-colonial openings. Use 4 voice-marking phrases."
        ),
        "exam_keys": [
            "**T1.** 1958; lays claim with the calm of a history book; alludes to Achebe's title from inside a domestic frame; distances himself with *the world is what it is*.",
            "**T2.** Okonkwo's personal achievement / the village as world-centre; Achebe's 1958 title *Things Fall Apart*; cold / unsentimental / abrasive / refusing pity / blunt; domesticates the post-colonial argument into one piece of furniture.",
            "**T3.** The opening lays claim with / The opening alludes to / The narrator distances himself / The text positions the reader.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 4, "slug": "short-stories-and-style",
        "title": "Short Stories and Style",
        "skills": ["reading", "writing", "language_awareness"],
        "bp": [
            "3.4.1 / 3.5.1 Soziokulturelles Orientierungswissen / Themen",
            "3.4.3.2 / 3.5.3.2 Leseverstehen",
            "3.4.3.5 / 3.5.3.5 Schreiben",
            "3.4.3.8 / 3.5.3.8 Verfügen über sprachliche Mittel – Grammatik",
            "3.4.4 / 3.5.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can read a contemporary short story and identify three stylistic moves (image cluster, sentence rhythm, narrator distance).",
            "I can use a wider relative-clause toolkit (*whose, of whom, in which*) accurately.",
            "I can write a 300-word stylistic-analysis essay.",
        ],
        "leadin": (
            "The class read a contemporary short story called "
            "*The Hour Before*. Six pages. One narrator who is "
            "kept very tightly on the hour before something "
            "bigger happens off-stage. The class spent the lesson "
            "noticing what the author did *not* show. By the end, "
            "Maja had counted seven sentences in which a thing "
            "was named only by the way someone reacted to it."
        ),
        "activate": (
            "**Stylistic-move scan.** With your partner, list 3 "
            "stylistic moves you would notice in a short story "
            "(e.g. image cluster, sentence rhythm, narrator "
            "distance). Apply each to one famous opening you "
            "remember."
        ),
        "input_blocks": [
            ("Reading — *The Hour Before* (extract)",
             "*The hour before is the only one I remember. The "
             "kettle was on, whose whistle had not yet started; "
             "the cat was asleep, of whom I was, in the worst "
             "way, jealous; the corridor in which my mother stood "
             "was lit by the standing lamp, which she had bought "
             "in the year I learned to read. None of this is "
             "important. All of it is the only material I have.*"),
            ("Grammar — wider relative-clause toolkit",
             "**whose** — possession (people / things / animals): "
             "*the kettle, whose whistle had not yet started.*\n"
             "**of whom / of which** — formal: *the cat, of whom "
             "I was jealous.*\n"
             "**in which** — formal: *the corridor in which my "
             "mother stood.*\n\n"
             "Defining vs. non-defining still applies. Use the "
             "wider toolkit deliberately — it lifts register."),
        ],
        "practise_g": [
            "1. Choose: *whose / of whom / in which*: the corridor "
            "___ my mother stood; the cat ___ I was jealous; the "
            "kettle ___ whistle had not yet started.",
            "2. T or F: *of which* is informal; *whose* can refer "
            "to things; *in which* is more formal than *where*.",
        ],
        "practise_m": [
            "3. Build 4 sentences using each of *whose / of whom / "
            "of which / in which*.",
        ],
        "answer_g": (
            "1. in which / of whom / whose.\n"
            "2. F (formal), T, T."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Stylistic-analysis essay, 300 words.** Read the "
            "extract. Identify three stylistic moves. Use 3 "
            "wider-toolkit relative clauses + 1 cleft + 2 "
            "academic discourse markers."
        ),
        "produce_sample": (
            "*Three stylistic moves do most of the work in *The "
            "Hour Before*. The first is the deliberate weight of "
            "the relative clauses — *the kettle, whose whistle had "
            "not yet started; the cat, of whom I was jealous; the "
            "corridor in which my mother stood*. The cumulative "
            "effect is incantatory: each domestic object earns a "
            "subordinate clause, as if the narrator were unable to "
            "let any of them go. Accordingly, what the prose "
            "refuses to do is move forward; the hour stretches by "
            "way of relative clauses rather than action. The "
            "second move is the narrator's flat self-correction — "
            "*None of this is important. All of it is the only "
            "material I have.* It is the contradiction, more than "
            "either statement, that does the work. By contrast "
            "with a more transparent narrator, this voice insists "
            "on simultaneously dismissing and elevating the "
            "domestic detail. The third move is the absence of "
            "the larger event. Whatever happens after the hour "
            "before is kept entirely off-stage; the prose gives "
            "us no help. In this regard, the story is doing "
            "something quite specific to short fiction: pressing "
            "on a narrow window of attention until the window "
            "becomes the subject. The reader's task is to feel "
            "the weight of the cat, the kettle, the corridor, and "
            "to register, slowly, that the absent event is not the "
            "point. The point is the pressure that absence "
            "exerts on what remains.*"
        ),
        "reflect": [
            "I can identify three stylistic moves in a contemporary short story.",
            "I can use *whose / of whom / of which / in which*.",
            "I can write a 300-word stylistic-analysis essay.",
        ],
        "pitfalls": [
            "*of which* sounds formal — don't over-deploy.",
            "*whose* with things is correct, despite some old "
            "style guides.",
            "Don't summarise plot — analyse.",
        ],
        "further": [
            "Granta, The New Yorker, The Paris Review — short "
            "fiction archives.",
            "James Wood, *How Fiction Works* — accessible chapter "
            "samples.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"The hour before is the only one I remember. The "
            "kettle was on, whose whistle had not yet started; "
            "the cat was asleep, of whom I was jealous; the "
            "corridor in which my mother stood was lit by the "
            "standing lamp.\"\n\n"
            "1. The remembered period: ___ . 2. Kettle relative "
            "clause: ___ . 3. Cat relative clause: ___ . 4. "
            "Corridor relative clause: ___ ."
        ),
        "exam_reading": (
            "Read the *Hour Before* extract above.\n\n"
            "1. Three objects given relative clauses: ___ . 2. "
            "The narrator's contradiction: ___ . 3. What is "
            "deliberately absent: ___ . 4. The implied subject of "
            "the story: ___ ."
        ),
        "exam_use": (
            "**Insert *whose / of whom / of which / in which*.**\n\n"
            "1. The corridor ___ my mother stood was lit by the "
            "lamp.\n"
            "2. The cat ___ I was jealous slept on the chair.\n"
            "3. The kettle ___ whistle had not yet started was on "
            "the hob.\n"
            "4. The standing lamp ___ light filled the corridor "
            "had been bought in 2011."
        ),
        "exam_writing": (
            "Write 300 words: a stylistic-analysis essay on the "
            "*Hour Before* extract. Use 3 wider-toolkit relative "
            "clauses + 1 cleft + 2 markers."
        ),
        "exam_keys": [
            "**T1.** the hour before; *whose whistle had not yet started*; *of whom I was jealous*; *in which my mother stood*.",
            "**T2.** kettle / cat / corridor; *None of this is important. All of it is the only material I have.*; the larger event off-stage; the pressure that absence exerts on what remains.",
            "**T3.** in which / of whom / whose / whose.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 5, "slug": "poetry-from-the-anthology",
        "title": "Poetry from the Anthology",
        "skills": ["reading", "writing", "language_awareness"],
        "bp": [
            "3.4.1 / 3.5.1 Soziokulturelles Orientierungswissen / Themen",
            "3.4.3.2 / 3.5.3.2 Leseverstehen",
            "3.4.3.5 / 3.5.3.5 Schreiben",
            "3.4.4 / 3.5.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can read a short poem and identify form, voice, and one figurative move.",
            "I can use vocabulary of poetic analysis (*line break, enjambment, stanza, image, persona, meter, half-rhyme*).",
            "I can write a 280-word poetic-analysis essay.",
        ],
        "leadin": (
            "Mr. Yilmaz handed out a single poem of fourteen "
            "lines, no title given. The class spent twenty "
            "minutes reading it silently, then ten minutes "
            "arguing about whether the line-breaks were doing "
            "any actual work. They agreed they were. They "
            "disagreed about which one was doing the most."
        ),
        "activate": (
            "**Form scan.** Without the title, what do you notice "
            "first about a fourteen-line poem? Stanza count? "
            "Rhyme? Meter? Line-break choices?"
        ),
        "input_blocks": [
            ("Reading — sample poem (anonymous, contemporary)",
             "*Fourteen lines, two stanzas. The first is the "
             "outside; the second is what is overheard. The "
             "line-breaks fall, mostly, before strong stresses, "
             "so that each line ends on a small held breath. "
             "There are no full rhymes. There are three half-"
             "rhymes — *light / late*, *door / floor*, *gone / "
             "alone* — that sit at the close of the second stanza, "
             "where the speaker turns inward. The persona is not "
             "named. The pronoun shifts from *they* to *we* in "
             "the final couplet, which is the moment the poem "
             "decides what it has been doing all along.*"),
            ("Vocabulary — poetic analysis",
             "*line, line-break, enjambment, stanza, couplet, "
             "image, image cluster, simile, metaphor, "
             "personification, persona, voice, tone, meter, "
             "iambic, half-rhyme / slant rhyme, full rhyme, "
             "alliteration, assonance, caesura.*"),
        ],
        "practise_g": [
            "1. Match: enjambment → line continues without pause; "
            "couplet → two-line unit; persona → speaker / "
            "speaker-voice; assonance → vowel echo.",
            "2. T or F: half-rhymes are looser than full rhymes; "
            "a caesura is a pause within a line; iambic = "
            "stressed-unstressed.",
        ],
        "practise_m": [
            "3. Build 3 sentences using *enjambment, half-rhyme, "
            "persona*.",
        ],
        "answer_g": (
            "1. all true.\n"
            "2. T, T, F (iambic = unstressed-stressed)."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Poetic-analysis essay, 280 words.** Pick a poem "
            "from the class anthology (or use the sample above). "
            "Identify form, voice, one figurative move. Use 6 "
            "poetic-analysis terms + 1 quote + 1 cleft."
        ),
        "produce_sample": (
            "*The poem is a fourteen-liner with no title and no "
            "named persona. Its fourteen lines fall into two "
            "stanzas — the first the outside, the second the "
            "overheard — and the form is closer to a "
            "modified-sonnet shape than to anything regular. "
            "What does the most work in this poem is the rhythm "
            "of the line-breaks: enjambment falls, almost "
            "consistently, before a strong stress, so that each "
            "line ends on a small held breath. The effect is "
            "incantatory and slightly suspenseful. There are no "
            "full rhymes; there are three half-rhymes — *light / "
            "late, door / floor, gone / alone* — clustered at "
            "the close of the second stanza, where the persona "
            "turns inward and the *we* of the final couplet "
            "appears for the first time. Accordingly, the poem's "
            "most important move is the small grammatical shift "
            "from *they* to *we*, which the line-break-rhythm and "
            "the half-rhymes have prepared us for. It is precisely "
            "the shift, and not any single image, that does the "
            "argumentative work. The voice is restrained; the "
            "tone, almost archival; the persona, deliberately "
            "ungendered. By contrast with louder contemporary "
            "lyric, this poem's confidence is in its willingness "
            "to under-explain. The reader's job is to do the "
            "small final addition that the *we* at the end "
            "demands.*"
        ),
        "reflect": [
            "I can identify form, voice, and one figurative move in a short poem.",
            "I can use 6 poetic-analysis terms.",
            "I can write a 280-word poetic-analysis essay.",
        ],
        "pitfalls": [
            "Don't paraphrase the poem — analyse what the form is "
            "doing.",
            "*Persona* ≠ author. Keep them separate.",
            "Half-rhyme is a specific term; don't call any imperfect "
            "rhyme that.",
        ],
        "further": [
            "Poetry Foundation — *Poems & Poets* archive.",
            "Don Paterson, *The Poem* (essays on form).",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"The poem is fourteen lines in two stanzas. "
            "Line-breaks fall before strong stresses. There are "
            "three half-rhymes — *light / late, door / floor, "
            "gone / alone* — at the close of the second stanza. "
            "The pronoun shifts from *they* to *we* in the final "
            "couplet.\"\n\n"
            "1. Length / stanzas: ___ . 2. Line-break rule: ___ . "
            "3. Half-rhymes: ___ . 4. Pronoun shift: ___ ."
        ),
        "exam_reading": (
            "Read the *sample poem* description above.\n\n"
            "1. Form: ___ . 2. Persona: ___ . 3. Three half-"
            "rhymes: ___ . 4. The decisive shift: ___ ."
        ),
        "exam_use": (
            "**Insert poetic-analysis term.**\n\n"
            "1. The poem uses ___ : line continues without pause.\n"
            "2. The ___ is the speaker-voice, not the author.\n"
            "3. The three ___ cluster at the close.\n"
            "4. The two-line unit at the end is a ___ ."
        ),
        "exam_writing": (
            "Write 280 words: a poetic-analysis essay on a poem "
            "of your choice. Use 6 terms + 1 quote + 1 cleft."
        ),
        "exam_keys": [
            "**T1.** 14 lines / 2 stanzas; before strong stresses; *light / late, door / floor, gone / alone*; *they → we* in final couplet.",
            "**T2.** 14 lines, 2 stanzas, modified-sonnet shape; ungendered; *light / late, door / floor, gone / alone*; pronoun shift *they → we*.",
            "**T3.** enjambment / persona / half-rhymes / couplet.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 6, "slug": "media-literacy-advanced",
        "title": "Media Literacy, Advanced",
        "skills": ["reading", "writing", "language_awareness"],
        "bp": [
            "3.4.1 / 3.5.1 Soziokulturelles Orientierungswissen / Themen",
            "3.4.3.2 / 3.5.3.2 Leseverstehen",
            "3.4.3.5 / 3.5.3.5 Schreiben",
            "3.4.4 / 3.5.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can read a long-form journalistic piece and identify the writer's framing, sourcing pattern, and one disclosed limitation.",
            "I can use academic critique vocabulary (*frame, framing effect, sourcing, attribution, anonymisation, conflict of interest*).",
            "I can write a 300-word media-criticism essay.",
        ],
        "leadin": (
            "Maja read a 1,200-word piece by an English-language "
            "outlet on a contested local protest. She underlined "
            "the verbs of attribution. By the end she had "
            "counted: *said* 11 times, *insisted* 3, *claimed* 4, "
            "*denied* 1, *added* 2. She wrote in the margin: "
            "*verbs of attribution are votes*."
        ),
        "activate": (
            "**Attribution scan.** On the slide are three "
            "sentences with three different attribution verbs "
            "(*said*, *claimed*, *insisted*). With your partner, "
            "rank by neutrality."
        ),
        "input_blocks": [
            ("Reading — *Verbs of Attribution*",
             "*Long-form journalism is, mostly, a question of "
             "framing and verbs. The frame is what the article "
             "treats as the question; everything before the "
             "subhead is doing frame work. The verbs of "
             "attribution carry, accordingly, more weight than "
             "their dictionary definitions suggest. *Said* is "
             "neutral; *claimed* signals doubt; *insisted* signals "
             "stubbornness; *added* signals subordination. A "
             "reader who counts the verbs already knows half the "
             "writer's argument before they reach the conclusion.*"),
            ("Vocabulary — media critique (advanced)",
             "*frame, framing effect, agenda-setting, sourcing, "
             "anonymous source, on-the-record, off-the-record, "
             "attribution verb, lede, nut graf, disclosure, "
             "conflict of interest, false balance, both-sidesing, "
             "structural balance.*"),
        ],
        "practise_g": [
            "1. Rank attribution verbs by neutrality (most neutral "
            "first): *insisted, said, claimed, added, denied*.",
            "2. Match: lede → article opening; nut graf → core-"
            "argument paragraph; both-sidesing → false balance.",
        ],
        "practise_m": [
            "3. Build 4 sentences using 4 advanced media-critique "
            "terms about a long-form article.",
        ],
        "answer_g": (
            "1. *said* > *added* > *insisted* > *denied* > "
            "*claimed* (rough ranking; *added* and *denied* "
            "depend on context).\n"
            "2. all true."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Media-criticism essay, 300 words.** Pick a long-"
            "form article. Identify framing, sourcing, attribution "
            "pattern, and one disclosed limitation. Use 5 "
            "advanced media-critique terms + 2 hedges."
        ),
        "produce_sample": (
            "*The article frames the protest as a question of "
            "*public order versus expression*. This is itself a "
            "framing choice; an alternative frame — *housing-"
            "rights protest* — would have produced a different "
            "piece. Accordingly, the lede privileges police "
            "concerns, and the nut graf does not appear until "
            "paragraph four. The sourcing pattern is asymmetric: "
            "the police source is on-the-record and named; the "
            "two protester sources are anonymous, citing fear of "
            "professional consequences. This asymmetry is "
            "disclosed in a half-sentence late in the piece, "
            "which is a transparent if minimal acknowledgement. "
            "The attribution verbs do, however, do most of the "
            "covert work. The police source *says* and *adds*; "
            "the anonymous protesters *insist* and *claim*. By "
            "the end of the article, the careful reader has been "
            "voted at — without a single fact having to bend. "
            "However, the piece is not, in my view, dishonest. "
            "It is conventionally framed in a way that a "
            "neighbouring outlet would frame differently. The "
            "more useful critique is structural: the routine choice "
            "of *public order* as the default frame is not "
            "decided by individual writers but by the desk above "
            "them. Caution is warranted; readers who count "
            "attribution verbs will, in this regard, get more out "
            "of long-form than readers who don't. The framing "
            "habit, like the verbs, is teachable.*"
        ),
        "reflect": [
            "I can identify framing, sourcing pattern, and one disclosed limitation.",
            "I can use 5 advanced media-critique terms.",
            "I can write a 300-word media-criticism essay.",
        ],
        "pitfalls": [
            "Don't conflate *biased* and *dishonest*.",
            "Anonymous sources can be legitimate — flag the "
            "*reason* given.",
            "Attribution verbs are signals, not proofs.",
        ],
        "further": [
            "Reuters Institute Digital News Report.",
            "Columbia Journalism Review — accessible essays.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"Long-form journalism is mostly framing and "
            "verbs. *Said* is neutral; *claimed* signals doubt; "
            "*insisted* signals stubbornness. The reader who "
            "counts the attribution verbs already knows half the "
            "writer's argument.\"\n\n"
            "1. Two key elements: ___ . 2. *Claimed* signals: "
            "___ . 3. *Insisted* signals: ___ . 4. The reader's "
            "advantage: ___ ."
        ),
        "exam_reading": (
            "Read the *Verbs of Attribution* extract above.\n\n"
            "1. Where the frame work happens: ___ . 2. Said: ___ . "
            "3. Claimed: ___ . 4. Added: ___ ."
        ),
        "exam_use": (
            "**Insert advanced media-critique term.**\n\n"
            "1. The ___ is what the article treats as the "
            "question.\n"
            "2. The ___ is the article's opening.\n"
            "3. The ___ is the core-argument paragraph.\n"
            "4. The ___ pattern reveals which sources are named "
            "and which are not."
        ),
        "exam_writing": (
            "Write 300 words: a media-criticism essay on a long-"
            "form article. Use 5 advanced terms + 2 hedges."
        ),
        "exam_keys": [
            "**T1.** framing and verbs; doubt; stubbornness; already knows half the argument.",
            "**T2.** before the subhead; neutral; doubt; subordination.",
            "**T3.** frame / lede / nut graf / sourcing.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 7, "slug": "mediation-as-a-skill",
        "title": "Mediation as a Skill",
        "skills": ["mediation", "writing", "language_awareness"],
        "bp": [
            "3.4.1 / 3.5.1 Soziokulturelles Orientierungswissen / Themen",
            "3.4.3.5 / 3.5.3.5 Schreiben",
            "3.4.3.6 / 3.5.3.6 Sprachmittlung",
            "3.4.3.7 / 3.5.3.7 Verfügen über sprachliche Mittel – Wortschatz",
        ],
        "objectives": [
            "I can mediate a 350-word German feature into 12 English sentences for a named addressee.",
            "I can preserve register, hedge structure, and modal nuance simultaneously.",
            "I can use the full reporting-verb toolkit (12+ verbs) and explicit cultural notes where needed.",
        ],
        "leadin": (
            "The class has been working on mediation for years. "
            "In Klasse 11, mediation becomes a formal Abitur-task "
            "category. The shift is from *useful explaining* to "
            "*useful explaining with audited register*: who is "
            "reading, what register do they speak, what do I "
            "translate, what do I keep in German with a brief "
            "explanation, and what do I drop entirely?"
        ),
        "activate": (
            "**Audit scan.** Slide shows a German source + a "
            "named addressee profile (a Canadian housing "
            "researcher). Mark each line: *keep / explain in "
            "brackets / drop*."
        ),
        "input_blocks": [
            ("Source — *German feature on Mietpreisbremse*",
             "*Die sogenannte Mietpreisbremse, die 2015 als "
             "Reaktion auf den Druck auf den Wohnungsmarkt "
             "eingeführt wurde, gilt heute als Beispiel für eine "
             "regulatorische Maßnahme, deren Wirkung umstritten "
             "ist. Befürworter führen an, dass die Mieten in "
             "Ballungsgebieten weniger schnell steigen als ohne "
             "die Regelung. Kritikerinnen entgegnen, dass die "
             "Bremse Investitionen in Neubau bremst und das "
             "Angebot dadurch langfristig verknappt. Die "
             "Bundesregierung hat im Mai 2027 die Verlängerung "
             "der Regelung um sechs Jahre beschlossen.*"),
            ("Cultural-note conventions",
             "When a German term has no clean English equivalent, "
             "use:\n"
             "- *the term + a 5-7 word explanation in brackets*: "
             "*Mietpreisbremse* (a federal cap on rent increases "
             "in tight housing markets).\n"
             "- *the German label, italicised, on first mention "
             "only*; English on subsequent mentions.\n"
             "- *brief contextual sentence after the term* if a "
             "structural feature needs framing."),
            ("Reporting-verb toolkit (12+)",
             "*to say, to explain, to claim, to argue, to assert, "
             "to maintain, to concede, to admit, to deny, to "
             "stress, to add, to point out, to note, to dismiss, "
             "to caution, to warn, to remark.*"),
        ],
        "practise_g": [
            "1. Match: behaupten → ?, einräumen → ?, betonen → ?, "
            "bestreiten → ?, anmerken → ?",
            "2. Cultural-note: build a 5-7 word English bracketed "
            "explanation for *Mietpreisbremse* and for "
            "*Bundesregierung*.",
        ],
        "practise_m": [
            "3. Build 6 reporting-verb sentences for the source "
            "above using 6 different verbs.",
        ],
        "answer_g": (
            "1. claim / concede / stress / deny / note.\n"
            "2. *Mietpreisbremse (a federal cap on rent increases "
            "in tight markets); Bundesregierung (Germany's federal "
            "government).*"
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Full mediation, 12 sentences.** Read the source "
            "above. Write 12 English sentences for a Canadian "
            "housing researcher. Preserve register + use 7 "
            "reporting verbs + 2 cultural-note brackets."
        ),
        "produce_sample": (
            "*The German federal *Mietpreisbremse* (a federal cap "
            "on rent increases in tight housing markets) was "
            "introduced in 2015 in response to pressure on the "
            "rental market. The article points out that the policy "
            "is now widely cited as a contested regulatory "
            "intervention. Supporters argue that rents in "
            "high-pressure metropolitan areas rise more slowly "
            "with the cap than they would without it. Critics "
            "counter that the cap dampens investment in new-build "
            "construction, which in their view tightens the "
            "long-term supply problem rather than easing it. The "
            "article notes the asymmetry: the rent-increase data "
            "is robust, while the new-build data is harder to "
            "isolate. The *Bundesregierung* (Germany's federal "
            "government) decided in May 2027 to extend the cap "
            "for six further years. The piece does not claim that "
            "the extension settles the argument. It maintains, "
            "however, that the cap is now politically embedded — "
            "any future government would face significant "
            "domestic costs in repealing it. The author cautions "
            "that international comparisons (e.g. Vienna's social-"
            "housing-heavy model) are not directly transferable. "
            "In short: a contested but durable policy, useful for "
            "comparative housing research without being a clean "
            "model.*"
        ),
        "reflect": [
            "I can mediate a 350-word German feature into 12 English sentences.",
            "I can preserve register and modal nuance.",
            "I can use 7 reporting verbs and cultural-note brackets.",
        ],
        "pitfalls": [
            "Don't translate German policy-jargon literally — use "
            "an English-(German bracketed) form.",
            "Reporting-verb monotony (*said* only) flattens the "
            "source.",
            "Don't *both-side* a 70/30 source as if it were "
            "50/50.",
        ],
        "further": [
            "Goethe-Institut — Sprachmittlungs-Beispielaufgaben "
            "Oberstufe.",
            "Cambridge — *Translation and Mediation* "
            "guidelines.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"Die Mietpreisbremse wurde 2015 eingeführt. "
            "Befürworter sagen, dass die Mieten weniger schnell "
            "steigen. Kritikerinnen entgegnen, dass die Bremse "
            "Investitionen bremst. Die Bundesregierung hat im "
            "Mai 2027 die Verlängerung um sechs Jahre "
            "beschlossen.\"\n\n"
            "1. Year introduced: ___ . 2. Supporters' claim: ___ . "
            "3. Critics' counter: ___ . 4. May-2027 decision: ___ ."
        ),
        "exam_reading": (
            "Read the German source above.\n\n"
            "1. Year introduced: ___ . 2. Supporters' claim: ___ . "
            "3. Critics' counter: ___ . 4. Federal decision date "
            "and length: ___ ."
        ),
        "exam_use": (
            "**Match German verb → English reporting verb.**\n\n"
            "1. behaupten → ___ ; 2. entgegnen → ___ ; 3. "
            "betonen → ___ ; 4. bestreiten → ___ ."
        ),
        "exam_writing": (
            "Mediate: 12 English sentences from the source for a "
            "Canadian housing researcher. Use 7 reporting verbs "
            "+ 2 cultural-note brackets."
        ),
        "exam_keys": [
            "**T1.** 2015; rents rise more slowly with the cap; the cap dampens investment in new construction; extension by 6 years (May 2027).",
            "**T2.** 2015; rents in high-pressure metropolitan areas rise more slowly with the cap; the cap dampens new-build investment, tightening long-term supply; extended for 6 further years in May 2027.",
            "**T3.** claim / counter (or argue) / stress / deny.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 8, "slug": "opinion-essay-writing",
        "title": "Opinion Essay Writing",
        "skills": ["reading", "writing", "language_awareness"],
        "bp": [
            "3.4.1 / 3.5.1 Soziokulturelles Orientierungswissen / Themen",
            "3.4.3.2 / 3.5.3.2 Leseverstehen",
            "3.4.3.5 / 3.5.3.5 Schreiben",
            "3.4.3.8 / 3.5.3.8 Verfügen über sprachliche Mittel – Grammatik",
            "3.4.4 / 3.5.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can read three opinion pieces and identify their thesis-evidence-counter-conclusion structure.",
            "I can use cohesion devices (*lexical chain, anaphoric reference, conjunctive adverb*) deliberately.",
            "I can write a 350-word opinion essay with a five-paragraph structure (intro / 2 body / counter / conclusion).",
        ],
        "leadin": (
            "The class read three contemporary opinion pieces "
            "from English-language outlets, each on a different "
            "topic: a 700-word column, a 1,400-word essay, a "
            "300-word op-ed. Mr. Yilmaz framed the question: "
            "*how does length change the argument?* The class "
            "noticed that the 300-word op-ed had to land on its "
            "single best sentence; the 1,400-word essay could "
            "afford to lose two."
        ),
        "activate": (
            "**Length scan.** With your partner, predict what each "
            "length permits and forbids: 300, 700, 1,400 words."
        ),
        "input_blocks": [
            ("Reading — *Opinion at three lengths*",
             "*The 300-word op-ed forces the writer to choose a "
             "single best sentence and arrange the rest as a "
             "ramp toward and away from it. The 700-word column "
             "permits one well-developed counter, but only one. "
             "The 1,400-word essay can afford to lose two "
             "sentences and still land its argument; it can also "
             "support a fully-articulated counter, a partial "
             "concession, and a more subtle conclusion. Length, "
             "in this regard, is not merely cosmetic. It "
             "determines what kinds of arguments the form can "
             "carry.*"),
            ("Cohesion devices",
             "**Lexical chain:** repeating the topic with "
             "varied vocabulary (*the policy, the cap, the "
             "regulation, the measure*).\n\n"
             "**Anaphoric reference:** *this argument, that "
             "concession, such a structure*.\n\n"
             "**Conjunctive adverbs:** *however, nevertheless, "
             "moreover, accordingly, in this regard, by "
             "contrast*."),
        ],
        "practise_g": [
            "1. Build a 4-link lexical chain for *the four-day "
            "school week*: ___ → ___ → ___ → ___ .",
            "2. Match: *however / accordingly / by contrast / "
            "moreover* → contrast / consequence / contrast / "
            "addition.",
        ],
        "practise_m": [
            "3. Build 4 sentences using 4 different cohesion "
            "devices on a single topic.",
        ],
        "answer_g": (
            "1. *the four-day school week / the trial / the "
            "policy / the schedule.*\n"
            "2. all true."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Opinion essay, 350 words.** Five paragraphs: "
            "intro / 2 body / counter / conclusion. Use lexical "
            "chain (3+ links) + 4 conjunctive adverbs + 1 "
            "anaphoric reference + 2 hedges."
        ),
        "produce_sample": (
            "*The four-day school week is a tempting "
            "policy import. The Belgian trial of 2025-2027 "
            "reported unchanged test scores, higher pupil "
            "well-being, and modest cost savings — a finding the "
            "policy was always likely to produce. However, the "
            "trial also reported one limitation that the "
            "discussion has tended to underplay: many lower-"
            "income families struggled to arrange childcare for "
            "the extra Friday. This is the argument I want to "
            "develop. **The trial** is encouraging on its own "
            "terms. **The policy**, transferred to a different "
            "national context, is a different object. By "
            "contrast with Belgium, my home district has neither "
            "publicly-funded Friday childcare nor a tradition of "
            "Wednesday-afternoon-style half-days. **The schedule** "
            "we would actually face on import day is therefore "
            "not the schedule the trial measured. **Such a "
            "structure** would shift the burden of the well-"
            "being gain onto the families least able to absorb "
            "it. Accordingly, my position is conditional rather "
            "than oppositional: I would support a four-day school "
            "week here only if a publicly-funded Friday "
            "childcare option were funded first. Critics will "
            "argue, fairly, that this conditions the reform out "
            "of existence. In response, I would say that the "
            "well-being gain in Belgium is partly a product of "
            "the conditions Belgium already had; transplanting "
            "the policy without those conditions risks "
            "reproducing the headline without the result. "
            "Moreover, the public-administration literature is "
            "consistent on this point: well-being interventions "
            "fail when their structural pre-conditions are not "
            "in place. In this regard, the right question is not "
            "*should we adopt the policy?* but *what would have "
            "to be true for it to deliver here?*. That is, in my "
            "view, the more useful conversation.*"
        ),
        "reflect": [
            "I can identify thesis-evidence-counter-conclusion in three opinion pieces.",
            "I can use cohesion devices deliberately.",
            "I can write a 350-word opinion essay with a clear five-paragraph structure.",
        ],
        "pitfalls": [
            "Lexical-chain laziness — repetition of the same noun "
            "phrase reads flat.",
            "Conjunctive-adverb overload — three per paragraph is "
            "padding.",
            "Counter-paragraph that doesn't actually concede "
            "anything.",
        ],
        "further": [
            "The Atlantic, The Guardian Long Reads, The New "
            "Yorker — opinion archives.",
            "George Orwell, *Politics and the English Language* "
            "(1946) — short, accessible.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"The 300-word op-ed forces the writer to choose "
            "a single best sentence. The 700-word column permits "
            "one well-developed counter, but only one. The "
            "1,400-word essay can support a fully-articulated "
            "counter, a partial concession, and a more subtle "
            "conclusion. Length is not merely cosmetic.\"\n\n"
            "1. 300-word demand: ___ . 2. 700-word permission: "
            "___ . 3. 1,400-word capacity: ___ . 4. Length is: "
            "___ ."
        ),
        "exam_reading": (
            "Read the *Opinion at three lengths* extract.\n\n"
            "1. 300-word constraint: ___ . 2. 700-word allowance: "
            "___ . 3. 1,400-word affordance: ___ . 4. Length "
            "determines: ___ ."
        ),
        "exam_use": (
            "**Cohesion device.**\n\n"
            "1. Build a 4-link lexical chain for *the cap on "
            "rent increases*: ___ → ___ → ___ → ___\n"
            "2. Insert *however / accordingly / in this regard*: "
            "(contrast / consequence / specification).\n"
            "3. Anaphoric reference for *the four-day school "
            "week*: ___ .\n"
            "4. Conjunctive adverb for *addition* in formal "
            "register: ___ ."
        ),
        "exam_writing": (
            "Write 350 words: a five-paragraph opinion essay. "
            "Use lexical chain + 4 conjunctive adverbs + 1 "
            "anaphoric reference + 2 hedges."
        ),
        "exam_keys": [
            "**T1.** choose a single best sentence; one well-developed counter; fully-articulated counter + concession + subtle conclusion; not merely cosmetic.",
            "**T2.** single best sentence; one counter; counter + concession + subtle conclusion; what kinds of arguments the form can carry.",
            "**T3.** *the cap / the regulation / the measure / the policy*; however / accordingly / in this regard; *this policy*; moreover.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 9, "slug": "a-modern-novel-bf",
        "title": "A Modern Novel (Basisfach focus)",
        "skills": ["reading", "writing", "language_awareness"],
        "bp": [
            "3.5.1 Soziokulturelles Orientierungswissen / Themen",
            "3.5.3.2 Leseverstehen",
            "3.5.3.5 Schreiben",
            "3.5.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can read four chapters of a modern novel (BF set text) and write a 350-word literary essay with a clear thesis.",
            "I can integrate two short quotations into my own sentences without breaking syntax.",
            "I can use a Basisfach (basic course) writing register: clear, well-organised, less ornate than Leistungsfach (advanced course).",
        ],
        "leadin": (
            "The Basisfach (basic course) Englisch class has been "
            "reading Kazuo Ishiguro's *Klara and the Sun* (2021) "
            "across two chapters per week. Today is the four-"
            "chapter checkpoint. Students have been keeping a "
            "single-page reading log per chapter — not a summary, "
            "but one quote, one question, one stylistic move. "
            "Mr. Yilmaz called the logs *the slow lane of "
            "Oberstufe reading*."
        ),
        "activate": (
            "**Log scan.** With your partner, share two quotes "
            "from your reading logs. Mark each as *image / "
            "voice / structural*."
        ),
        "input_blocks": [
            ("Reading — *Klara and the Sun*, ch. 4 (extract)",
             "*The Sun would always come into the store, no "
             "matter the weather, and so would the dust on the "
             "windows of the Slow Lane. The girl who looked at me "
             "longest was the one who did not buy. I learned, in "
             "that first month, that my best customers were the "
             "ones who walked away.*"),
            ("Quote-integration patterns (Basisfach register)",
             "**Drop-in quote (avoid):** *Ishiguro writes: \"The "
             "Sun would always come into the store.\"*\n\n"
             "**Integrated quote (preferred):** *Ishiguro lets "
             "Klara observe that *\"the Sun would always come "
             "into the store, no matter the weather\"*, a line "
             "whose deceptive plainness is the novel's signature "
             "register.*\n\n"
             "**Embedded fragment:** *the *\"slow lane\"* of the "
             "novel's title becomes, by chapter four, a literal "
             "shop fixture.*"),
        ],
        "practise_g": [
            "1. Rewrite as integrated quote: *Ishiguro writes: "
            "'I learned, in that first month, that my best "
            "customers were the ones who walked away.'*",
            "2. T or F: a drop-in quote breaks the writer's "
            "syntax; an integrated quote keeps the writer's "
            "syntax intact; an embedded fragment uses two or "
            "three words inside the writer's sentence.",
        ],
        "practise_m": [
            "3. Build 3 integrated-quote sentences using the "
            "*Klara* extract.",
        ],
        "answer_g": (
            "1. *Ishiguro has Klara reflect that her best "
            "customers were *\"the ones who walked away\"*, a "
            "line whose mournful symmetry is the novel's "
            "signature.*\n"
            "2. all true."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Literary essay, 350 words (Basisfach register).** "
            "Read chapters 1-4. Argue one thesis about Klara as a "
            "narrator. Use 2 integrated quotes + 1 embedded "
            "fragment + 3 academic discourse markers."
        ),
        "produce_sample": (
            "*By chapter four of *Klara and the Sun*, Kazuo "
            "Ishiguro has established Klara as a narrator whose "
            "central limitation is also her central reliability. "
            "Klara is an Artificial Friend, observing her "
            "customers from the *\"slow lane\"* of a high-street "
            "store, and her observations are, by turns, "
            "literal-minded and quietly devastating. The "
            "deceptive plainness of her reports is the novel's "
            "signature: when she records that *\"the Sun would "
            "always come into the store, no matter the weather\"*, "
            "she is reporting both an observable fact and a "
            "framework of meaning we are not yet supposed to "
            "share. Accordingly, the reader does the work the "
            "narrator cannot. Klara herself does not yet know that "
            "the Sun is, for her, a deity-like figure; we are "
            "permitted to see this *because* she does not. By "
            "contrast with a more knowing narrator, Klara's voice "
            "earns its weight from what it cannot frame. The most "
            "precise example, in my reading, is the chapter-four "
            "summary: *\"my best customers were the ones who "
            "walked away.\"* This is, on the surface, a slightly "
            "sad observation about retail traffic. Beneath the "
            "surface, it is a thesis about how Klara experiences "
            "attention itself — concentrated, unrequited, and "
            "carefully accepted. In this regard, the novel is "
            "doing something specific to first-person narration: "
            "it is using a voice with limited frames to expose "
            "frames we have not noticed in ourselves. Klara's "
            "limitation is her instrument. The reader's task in "
            "the early chapters is not to feel sorry for her, but "
            "to recalibrate.*"
        ),
        "reflect": [
            "I can argue a clear thesis about a modern novel.",
            "I can integrate two short quotes without breaking syntax.",
            "I can hold the Basisfach register: clear, well-organised, less ornate than Leistungsfach.",
        ],
        "pitfalls": [
            "Drop-in quotes break the writer's voice — integrate.",
            "Don't paraphrase the plot — argue a thesis.",
            "Basisfach (basic course) ≠ less argument; it = "
            "tighter argument with cleaner moves.",
        ],
        "further": [
            "Kazuo Ishiguro, *Klara and the Sun* (2021).",
            "James Wood, *How Fiction Works*.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"By chapter four, Klara has been established as a "
            "narrator whose limitation is also her reliability. "
            "Her reports are literal-minded and quietly "
            "devastating. The deceptive plainness — *the Sun "
            "would always come into the store, no matter the "
            "weather* — is the novel's signature register.\"\n\n"
            "1. Klara's central pair: ___ . 2. Tone of reports: "
            "___ . 3. Plainness — what kind: ___ . 4. Register: "
            "___ ."
        ),
        "exam_reading": (
            "Read the *Klara* ch. 4 extract above.\n\n"
            "1. The shop's defining detail: ___ . 2. Klara's "
            "best customers: ___ . 3. Lesson she draws: ___ . 4. "
            "Implied thesis: ___ ."
        ),
        "exam_use": (
            "**Quote integration.**\n\n"
            "1. Drop-in → integrated: *Ishiguro writes: 'the Sun "
            "would always come into the store.'* → ___\n"
            "2. Drop-in → integrated: *Klara says: 'my best "
            "customers were the ones who walked away.'* → ___\n"
            "3. Embedded fragment using *\"slow lane\"*: → ___\n"
            "4. Embedded fragment using *\"no matter the "
            "weather\"*: → ___"
        ),
        "exam_writing": (
            "Write 350 words: a Basisfach literary essay on "
            "*Klara and the Sun* ch. 1-4. Use 2 integrated "
            "quotes + 1 embedded fragment + 3 markers."
        ),
        "exam_keys": [
            "**T1.** her limitation is also her reliability; literal-minded / quietly devastating; deceptive plainness; the novel's signature register.",
            "**T2.** the Sun and the dust on the windows of the slow lane; the ones who walked away (= longer-looking, non-buying); concentrated, unrequited attention is what Klara experiences; first-person narration uses limited frames to expose frames we don't notice.",
            "**T3.** *Ishiguro lets Klara observe that 'the Sun would always come into the store.' / Klara reflects that her best customers were 'the ones who walked away.' / The 'slow lane' of the novel's title becomes, by ch. 4, a literal shop fixture. / Klara reports the Sun coming 'no matter the weather' as if it were observable fact.*",
            "**T4.** Open.",
        ],
    },
    {
        "n": 10, "slug": "a-classic-text-lf",
        "title": "A Classic Text (Leistungsfach focus)",
        "skills": ["reading", "writing", "language_awareness"],
        "bp": [
            "3.4.1 Soziokulturelles Orientierungswissen / Themen",
            "3.4.3.2 Leseverstehen",
            "3.4.3.5 Schreiben",
            "3.4.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can read three soliloquies from Shakespeare's *Macbeth* (LF set text) and write a 450-word literary essay with a complex thesis.",
            "I can engage Early Modern English vocabulary and rhythm with confidence.",
            "I can hold the Leistungsfach (advanced course) register: complex argument, integrated close reading, sustained voice.",
        ],
        "leadin": (
            "The Leistungsfach (advanced course) Englisch class "
            "is reading Shakespeare's *Macbeth* (1606) over six "
            "weeks. Today's checkpoint covers three soliloquies: "
            "1.7 (*If it were done*), 2.1 (*Is this a dagger*), "
            "and 5.5 (*Tomorrow, and tomorrow, and tomorrow*). "
            "The class has been keeping a soliloquy log: one "
            "image, one rhythm-break, one moral move per "
            "soliloquy."
        ),
        "activate": (
            "**Soliloquy scan.** With your partner, list one "
            "image, one rhythm-break, and one moral move per "
            "soliloquy."
        ),
        "input_blocks": [
            ("Reading — three Macbeth soliloquies (extracts)",
             "*1.7 (Macbeth):* *If it were done when 'tis done, "
             "then 'twere well / It were done quickly: …*\n\n"
             "*2.1 (Macbeth):* *Is this a dagger which I see "
             "before me, / The handle toward my hand?*\n\n"
             "*5.5 (Macbeth):* *Tomorrow, and tomorrow, and "
             "tomorrow, / Creeps in this petty pace from day to "
             "day, …*"),
            ("Leistungsfach (advanced course) register",
             "**Marks of LF register:**\n"
             "- Sustained close reading of language and rhythm.\n"
             "- Integrated quotation rather than block-quotes.\n"
             "- Tracking of one argument over 4-6 paragraphs.\n"
             "- Confident use of literary vocabulary (*soliloquy, "
             "blank verse, iambic pentameter, caesura, "
             "syntactic inversion, dramatic irony*).\n"
             "- Engagement with at least one piece of critical "
             "commentary or contextual frame."),
        ],
        "practise_g": [
            "1. Match: soliloquy → speech alone on stage; "
            "blank verse → unrhymed iambic pentameter; "
            "caesura → mid-line pause.",
            "2. T or F: 1.7 explores moral hesitation; 2.1 "
            "stages hallucinated commitment; 5.5 collapses "
            "future-tense confidence.",
        ],
        "practise_m": [
            "3. Build 3 close-reading sentences using "
            "Leistungsfach register on the three soliloquies.",
        ],
        "answer_g": (
            "1. all true.\n"
            "2. all true."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Literary essay, 450 words (Leistungsfach "
            "register).** Argue a single complex thesis "
            "tracing how Macbeth's relationship to time changes "
            "across the three soliloquies. Use 4 integrated "
            "quotes + 6 academic discourse markers + 1 cleft."
        ),
        "produce_sample": (
            "*Macbeth's three central soliloquies — 1.7, 2.1, and "
            "5.5 — track a deterioration in his relationship to "
            "time, and that deterioration is, I shall argue, the "
            "most precise way to read his moral collapse. In 1.7, "
            "Macbeth approaches the prospective murder as a "
            "problem of completion: *\"If it were done when 'tis "
            "done, then 'twere well / It were done quickly\"*. The "
            "structure of the argument is conditional, and the "
            "tense is hypothetical; Macbeth is still inside a "
            "world in which an act could be sealed off from its "
            "consequences. The repetition of *done* signals, "
            "however, an over-confidence the verse itself "
            "destabilises by the end of the speech. By contrast, "
            "in 2.1 Macbeth has stepped into the present "
            "imperative: *\"Is this a dagger which I see before "
            "me, / The handle toward my hand?\"*. The hallucinated "
            "dagger is, accordingly, a present-tense object that "
            "compels rather than waits. It is precisely the "
            "shift from the conditional of 1.7 to the perceptual "
            "present of 2.1 that marks Macbeth's loss of "
            "deliberative space. Whatever moral hesitation "
            "remained in 1.7 is, here, hijacked by an image he "
            "neither chose nor can refuse. In 5.5, the "
            "deterioration completes itself in the famous "
            "*\"tomorrow, and tomorrow, and tomorrow\"* — three "
            "futures emptied of force by their own repetition. "
            "What had been hypothetical in 1.7 and present-"
            "compelling in 2.1 becomes, in 5.5, a *\"petty pace "
            "from day to day\"*: a future that will only ever "
            "shuffle into more of itself. More specifically, the "
            "verse-rhythm collapses with the meaning: the iambic "
            "pentameter loses its drive; the line *\"creeps in "
            "this petty pace\"* enacts the very tedium it "
            "describes. Critics have read 5.5 as nihilist; in my "
            "reading, it is the structural completion of the arc "
            "begun in 1.7. Macbeth's collapse is the collapse of "
            "his ability to imagine time as anything other than a "
            "ledger of repetition. In this regard, the play "
            "stages moral failure not as a single act but as the "
            "drying up of the tense-system itself — and the "
            "soliloquies do most of that work without the help "
            "of any other character.*"
        ),
        "reflect": [
            "I can read three soliloquies and trace a complex thesis across them.",
            "I can hold the Leistungsfach register over 450 words.",
            "I can integrate four quotes without breaking voice.",
        ],
        "pitfalls": [
            "Drop-in quotes break the LF register.",
            "Don't paraphrase Shakespeare — analyse his moves.",
            "Critical commentary is a flavour, not the meal.",
        ],
        "further": [
            "Stephen Greenblatt, *Will in the World* — accessible "
            "Shakespeare biography.",
            "Frank Kermode, *Shakespeare's Language*.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"In 1.7, Macbeth approaches the murder as "
            "completion: *if it were done when 'tis done, then "
            "'twere well / it were done quickly*. In 2.1, he "
            "steps into the perceptual present: *is this a "
            "dagger?* In 5.5, the future collapses: *tomorrow, "
            "and tomorrow, and tomorrow*.\"\n\n"
            "1. 1.7 mode: ___ . 2. 2.1 mode: ___ . 3. 5.5 "
            "mode: ___ . 4. Verb-system arc: ___ ."
        ),
        "exam_reading": (
            "Read the three soliloquy extracts above.\n\n"
            "1. 1.7 — Macbeth's tense / mood: ___ . 2. 2.1 — "
            "what compels: ___ . 3. 5.5 — the future as: ___ . "
            "4. The arc, in one sentence: ___ ."
        ),
        "exam_use": (
            "**Quote integration (Leistungsfach).**\n\n"
            "1. Integrated: *Macbeth speaks of … 'done quickly'.* "
            "→ ___\n"
            "2. Integrated: *In 2.1, the dagger is …* → ___\n"
            "3. Embedded fragment using *'petty pace'*: ___\n"
            "4. Cleft on *the verse-rhythm*: ___"
        ),
        "exam_writing": (
            "Write 450 words: a Leistungsfach literary essay "
            "tracing Macbeth's relationship to time across the "
            "three soliloquies. Use 4 integrated quotes + 6 "
            "markers + 1 cleft."
        ),
        "exam_keys": [
            "**T1.** completion (conditional / hypothetical); perceptual present; future emptied of force; from conditional → perceptual present → emptied future.",
            "**T2.** conditional / hypothetical; the hallucinated dagger compels rather than waits; *a petty pace from day to day* — empty repetition; tense-system collapses from conditional through compelling-present to ledger-future.",
            "**T3.** *Macbeth approaches the act as something to be 'done quickly', a phrase whose repetition the verse itself destabilises. / In 2.1, the dagger 'before me' compels rather than waits. / The 'petty pace' the speaker names is the verse rhythm enacting itself. / It is precisely the verse-rhythm that completes the meaning.*",
            "**T4.** Open.",
        ],
    },
    {
        "n": 11, "slug": "public-speaking-prep",
        "title": "Public Speaking: Toward the Komm-Prüfung",
        "skills": ["speaking", "listening", "language_awareness"],
        "bp": [
            "3.4.1 / 3.5.1 Soziokulturelles Orientierungswissen / Themen",
            "3.4.3.1 / 3.5.3.1 Hör-/Hörsehverstehen",
            "3.4.3.3 / 3.5.3.3 Sprechen – an Gesprächen teilnehmen",
            "3.4.3.4 / 3.5.3.4 Sprechen – zusammenhängendes monologisches Sprechen",
        ],
        "objectives": [
            "I can deliver a 4-minute monologue on a stimulus and respond to a 4-minute follow-up dialogue (Kommunikationsprüfung-style).",
            "I can use academic-spoken register without sounding stilted.",
            "I can rebut and concede with specifics in real time.",
        ],
        "leadin": (
            "Klasse 11 begins formal preparation for the oral exam "
            "(Kommunikationsprüfung). Mr. Yilmaz set the format: "
            "4-minute monologue from a stimulus + 4-minute "
            "examiner dialogue + 2-minute closing. The class is "
            "rehearsing in pairs. Maja drew a stimulus card on "
            "*the future of work*; the dialogue partner is to "
            "ask one supportive and one sharp follow-up."
        ),
        "activate": (
            "**Stimulus scan.** On the slide are three stimulus "
            "cards (one image, one quote, one statistic). Pick "
            "one. Build a 90-second outline."
        ),
        "input_blocks": [
            ("Kommunikationsprüfung format (~10 min)",
             "1. **Monologue (4 min).** Frame stimulus → 2 "
             "arguments → counter + concession → close.\n"
             "2. **Dialogue (4 min).** Examiner asks 4-6 follow-"
             "ups. Candidate must rebut, concede, and elaborate.\n"
             "3. **Close (2 min).** One synthesis + one final "
             "stance."),
            ("Spoken academic register",
             "*I would argue that … / The picture, however, is "
             "more complex … / Let me concede one point first … / "
             "The available evidence suggests … / What I'm not "
             "saying is X — what I am saying is Y. / On reflection, "
             "I think … / If I had to commit, I would say …*"),
        ],
        "practise_g": [
            "1. Match phrase to function: *Let me concede one "
            "point* → concession; *On reflection* → re-framing; "
            "*If I had to commit* → committing.",
            "2. Build a 4-line monologue opening from a stimulus "
            "*'The future of work is hybrid by 2030.'*",
        ],
        "practise_m": [
            "3. Build a 4-minute monologue outline (bullets) on a "
            "stimulus of your choice.",
        ],
        "answer_g": "1. all true. 2. Open.",
        "answer_m": "3. Open.",
        "produce": (
            "**Pair Komm-Prüfung rehearsal.** 10 minutes per "
            "pair (4 + 4 + 2). Audience scores: clarity of "
            "frame, specificity of evidence, quality of "
            "concession, fluency of rebuttal, quality of close."
        ),
        "produce_sample": (
            "*Let me start with the stimulus quote — *the future "
            "of work is hybrid by 2030*. I would argue that this "
            "claim is half-right and half-marketing. The available "
            "evidence suggests that hybrid arrangements are "
            "spreading in white-collar sectors, but the picture "
            "is more complex once we look beyond office work. "
            "Frontline jobs — care, retail, manufacturing — have "
            "been substantially less affected, and these are "
            "more than half of the workforce in most OECD "
            "countries. Accordingly, the *2030 will be hybrid* "
            "claim is, in this regard, a claim about a specific "
            "sector that has been generalised. Let me concede one "
            "point first: white-collar hybrid work is here to "
            "stay, and the cultural effect of that — including on "
            "city planning, commute patterns, and small-business "
            "lunch traffic — is real. What I'm not saying is that "
            "hybrid is a fad. What I am saying is that *the "
            "future of work* is plural, not singular. On "
            "reflection, the more honest stimulus would be: *the "
            "future of office work is hybrid by 2030*. If I had "
            "to commit, I would say that the policy debate "
            "should focus on flexibility for those whose jobs "
            "cannot be hybrid — paid sick leave, predictable "
            "scheduling, training rights — because that is the "
            "fairness gap the hybrid framing tends to obscure.*"
        ),
        "reflect": [
            "I can deliver a 4-minute monologue from a stimulus.",
            "I can hold a 4-minute dialogue with an examiner.",
            "I can rebut and concede in real time.",
        ],
        "pitfalls": [
            "Reading off a card kills the dialogue.",
            "Generic concessions (*you have a point*) → name the "
            "specific point.",
            "Don't memorise — internalise the structure.",
        ],
        "further": [
            "TED Talks — short examples of stimulus-led talks.",
            "BBC Sounds — *Question Time* extracts.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"I would argue that the *future of work is "
            "hybrid* claim is half-right. The available evidence "
            "suggests hybrid is real for white-collar sectors but "
            "frontline jobs — care, retail, manufacturing — have "
            "been substantially less affected. The honest "
            "stimulus is: the future of *office work* is hybrid "
            "by 2030.\"\n\n"
            "1. Stance: ___ . 2. Generalisation problem: ___ . "
            "3. Frontline examples: ___ . 4. The corrected "
            "stimulus: ___ ."
        ),
        "exam_reading": (
            "Read the sample monologue above.\n\n"
            "1. Two main arguments: ___ . 2. Concession + "
            "specifics: ___ . 3. *What I am not saying / what I "
            "am saying* contrast: ___ . 4. Final commit: ___ ."
        ),
        "exam_use": (
            "**Insert spoken-academic phrase.**\n\n"
            "1. ___ that hybrid is half-right.\n"
            "2. ___ , the picture is more complex.\n"
            "3. ___ one point first: cultural effects are real.\n"
            "4. ___ , I would say the policy debate should "
            "centre on flexibility."
        ),
        "exam_writing": (
            "Write a 4-minute Komm-Prüfung-style monologue "
            "script (~300 words) on a stimulus of your choice. "
            "Use 5 spoken-academic phrases."
        ),
        "exam_keys": [
            "**T1.** half-right; the claim is generalised from white-collar to all sectors; care / retail / manufacturing; *the future of office work is hybrid by 2030*.",
            "**T2.** white-collar hybrid is real and spreading + the *2030 hybrid* claim is over-generalised; cultural effects on city planning / commute / lunch traffic; *not saying it's a fad — saying the future is plural*; policy should focus on frontline-job flexibility (sick leave, predictable scheduling, training).",
            "**T3.** I would argue / The picture, however / Let me concede / If I had to commit.",
            "**T4.** Open.",
        ],
    },
    {
        "n": 12, "slug": "klausur-prep-exam-rehearsal",
        "title": "Klausur Prep: Exam Rehearsal",
        "skills": ["reading", "writing", "language_awareness"],
        "bp": [
            "3.4.1 / 3.5.1 Soziokulturelles Orientierungswissen / Themen",
            "3.4.3.2 / 3.5.3.2 Leseverstehen",
            "3.4.3.5 / 3.5.3.5 Schreiben",
            "3.4.3.6 / 3.5.3.6 Sprachmittlung",
            "3.4.4 / 3.5.4 Text- und Medienkompetenz",
        ],
        "objectives": [
            "I can complete a 90-BE Klausur (assessment) covering Comprehension + Analysis + Composition + Mediation under timed conditions.",
            "I can manage time across the four parts and produce a sustained answer in each.",
            "I can use Inhalt / Sprache awareness — knowing which parts are weighted to content and which to language.",
        ],
        "leadin": (
            "Klasse 11 ends with a full Klausur-rehearsal Unit. "
            "Mr. Yilmaz set the format: a 1,000-word source text "
            "(half journalistic, half literary), four tasks, 90 "
            "BE total, four hours including breaks. The Unit is "
            "less about new material than about timing and "
            "endurance — *which is, mostly, what Klausuren are*."
        ),
        "activate": (
            "**Time-budget scan.** With your partner, allocate "
            "minutes across: Comprehension (24 BE) / Analysis "
            "(18 BE) / Composition (18 BE) / Mediation (30 BE). "
            "What is *exam-realistic*?"
        ),
        "input_blocks": [
            ("Klausur structure (90 BE)",
             "**Part A — Comprehension** (~24 BE). Question-and-"
             "answer on a journalistic / literary source. Inhalt-"
             "weighted.\n\n"
             "**Part B — Analysis** (~18 BE). Stylistic analysis "
             "of the source. Sprache-weighted.\n\n"
             "**Part C — Composition / Comment** (~18 BE). 250-"
             "word original argument or creative response. Both "
             "Inhalt and Sprache.\n\n"
             "**Mediation** (~30 BE). Mediation of a German "
             "source for a named English-speaking addressee. "
             "Inhalt-weighted but Sprache-checked.\n\n"
             "**Inhalt / Sprache split.** BF: 50/50. LF: 40/60."),
            ("Time-management heuristic",
             "Total: 4 hours (240 min) incl. 20 min breaks → 220 "
             "active min.\n"
             "- Reading source carefully: 25 min.\n"
             "- Comprehension: 40 min.\n"
             "- Analysis: 40 min.\n"
             "- Composition: 50 min.\n"
             "- Mediation: 50 min.\n"
             "- Final review: 15 min.\n\n"
             "If you are over by 10 min on any part, move on. "
             "Half a finished answer beats a perfect unfinished "
             "one."),
        ],
        "practise_g": [
            "1. Match BE → part: 24 → ?, 18 → ?, 18 → ?, 30 → ?",
            "2. T or F: Mediation is mostly Inhalt-weighted; "
            "Analysis is mostly Sprache-weighted; Composition is "
            "both.",
        ],
        "practise_m": [
            "3. Build a 30-second answer to a Comprehension "
            "question + a 60-second answer to a Composition "
            "prompt.",
        ],
        "answer_g": (
            "1. Comprehension / Analysis / Composition / "
            "Mediation.\n"
            "2. all true."
        ),
        "answer_m": "3. Open.",
        "produce": (
            "**Klausur rehearsal (4 hours).** Full timed paper. "
            "1,000-word source (half journalistic + half "
            "literary). Four tasks. Inhalt / Sprache split as "
            "stated. Submit. Class debriefs collectively, with "
            "a focus on time management and unfinished sections."
        ),
        "produce_sample": (
            "(See *Reflection on the rehearsal* section below — "
            "the production task is the Klausur itself.)"
        ),
        "reflect": [
            "I can complete a 90-BE Klausur under timed conditions.",
            "I can manage time across four parts.",
            "I can use Inhalt / Sprache awareness.",
        ],
        "pitfalls": [
            "Spending too long on Comprehension because it feels "
            "safest — half-points cost.",
            "Mediation under-finished — it's the highest BE, "
            "protect its time.",
            "Sprache loss in Composition because content-energy "
            "ran out — leave 15 min review.",
        ],
        "further": [
            "Bildungsplan-aligned commercial Klausur-collections "
            "(e.g. Stark, Klett) for additional rehearsal "
            "papers.",
            "Past Abitur papers (BW), with caution: not for "
            "scaling, only for format familiarity.",
        ],
        "exam_listening": (
            "Listen twice.\n\n"
            "> \"The Klausur is 90 BE. Comprehension is 24, "
            "Analysis 18, Composition 18, Mediation 30. The "
            "total is 4 hours including 20 min of breaks. The "
            "Inhalt / Sprache split is 50/50 in Basisfach and "
            "40/60 in Leistungsfach.\"\n\n"
            "1. Total BE: ___ . 2. Highest-BE part: ___ . 3. "
            "Total time: ___ . 4. LF Sprache weighting: ___ ."
        ),
        "exam_reading": (
            "Read the *Klausur structure* and *Time-management* "
            "blocks above.\n\n"
            "1. Comprehension BE: ___ . 2. Mediation BE: ___ . "
            "3. Mediation suggested time: ___ . 4. The half-"
            "finished-vs.-perfect rule: ___ ."
        ),
        "exam_use": (
            "**Time-budget calculation.**\n\n"
            "1. With 220 active min, % allocated to Mediation: "
            "___ .\n"
            "2. % to Comprehension: ___ .\n"
            "3. Final review: ___ min.\n"
            "4. If you are 15 min over on Analysis, what should "
            "you do? ___ ."
        ),
        "exam_writing": (
            "Complete a full 90-BE Klausur rehearsal under timed "
            "conditions. Submit with a 200-word self-reflection "
            "on time management."
        ),
        "exam_keys": [
            "**T1.** 90; Mediation (30); 4 hours (incl. 20 min breaks); 60 %.",
            "**T2.** 24; 30; 50 min; *half a finished answer beats a perfect unfinished one*.",
            "**T3.** ~23 % (50 / 220); ~18 % (40 / 220); 15 min; move on / cut losses.",
            "**T4.** Open.",
        ],
    },
]


UNIT_TPL = """---
title: "Unit {n} — {title}"
subtitle: "Track E · Klasse 11 · Niveau E (Basisfach / Leistungsfach)"
niveau: "E"
klassenstufe: 11
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
**Niveau:** E. Klausur (assessment) at Niveau E (90 BE,
Comprehension + Analysis + Composition + Mediation).\\
**Course tagging:** basic course (Basisfach, E-BF) and advanced
course (Leistungsfach, E-LF) — Units in Klasse 11–13 carry both
where applicable; some Units are tagged BF or LF specifically.
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
subtitle: "Track E · Klasse 11 · Niveau E · 4 Stunden"
author: "S. Le Boulanger"
niveau: "E"
klassenstufe: 11
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

**Track E · Klasse 11 · Niveau E · 4 Stunden (incl. breaks) · 90 BE**

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

    print(f"Wrote {len(UNITS) * 3} files for Track E Klasse 11.")


if __name__ == "__main__":
    emit()
