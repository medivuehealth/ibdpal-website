"""Transform compiled site prose into standalone book voice."""

from __future__ import annotations

import re

from book_prose_cleanup import (
    apply_prose_replacements,
    remove_figure_references,
    should_drop_paragraph as prose_should_drop,
    strip_web_tails,
)

PUBLISHER_LINE = "MediVue Health Education · Patient-education publication"

BOILERPLATE_SENTENCES = [
    r"Discuss how this topic applies to your current disease activity with your gastroenterologist\.",
    r"Logging patterns in IBDPal or a notebook helps clinicians see trends beyond a single visit\.",
    r"Your GI team can adjust recommendations based on labs, imaging, and symptom trends\.",
    r"Second opinions are reasonable when plans feel unclear or symptoms persist despite treatment\.",
    r"If symptoms worsen while you try these steps, contact your clinic using your flare pathway\.",
    r"Bring these observations to your next IBD appointment so your team can personalize advice\.",
    r"Children, older adults, and post-surgical patients may need modified guidance from specialists\.",
    r"Patient education supports shared decision making; it does not replace individual medical assessment\.",
    r"Write down questions for your gastroenterologist before each visit so limited appointment time is used well\.",
    r"Symptom patterns tracked over several days are more useful to your clinician than a single snapshot\.",
    r"Medication adherence and follow-up labs are as important as diet changes for many IBD patients\.",
    r"Tell your team about travel, work stress, sleep changes, and menstrual cycle timing when symptoms shift\.",
    r"Bring prior colonoscopy, imaging, and pathology reports when seeing a new IBD specialist\.",
]

BOILERPLATE_RE = re.compile("|".join(BOILERPLATE_SENTENCES), re.IGNORECASE)

SKIP_HEADING_PATTERNS = [
    r"ibdpal",
    r"foundation.*ibdpal",
    r"using foundation",
    r"free tools on",
    r"explore ibdpal",
    r"how to track .+ with",
    r"how to track .+ with ibdpal",
    r"does foundation endorse",
    r"related reading",
    r"related resources",
    r"medical disclaimer",
    r"questions for your gastroenterologist or dietitian",
    r"when food questions become urgent",
    r"frequently asked",
    r"\bfaq\b",
    r"complete ibd nutrition guide",
    r"newly diagnosed with ibd",
    r"newly diagnosed with crohn",
    r".+\band IBD\b.*:",
]

SKIP_HEADING_RE = re.compile("|".join(SKIP_HEADING_PATTERNS), re.IGNORECASE)

DROP_PARAGRAPH_PATTERNS = [
    r"^related reading:",
    r"^related:",
    r"ibdpal\.org",
    r"download the ibdpal",
    r"explore ibdpal",
    r"free tools on ibdpal",
    r"hub:\s*/ibd-nutrition",
    r"selected crohn.*foundation.*license",
    r"foundation does not endorse ibdpal",
    r"content is used under license from the foundation",
    r"bookmark foundation disease basics",
    r"explore newly diagnosed foundation",
    r"community map",
    r"technology platforms like",
    r"share foundation and .* guides",
    r"foundation chapters.*improvecarenow",
    r"a symptom diary nutrition tracking",
    r"nutrition overview guide, foods during",
    r"notebook or\.?$",
    r"foundation newly diagnosed",
    r"first gi appointment guide",
    r"what is ibd\? foundation",
    r"^scientists are actively studying:?\s*$",
    r"^and how they may influence",
    r"for educational purposes only",
    r"this article is for educational",
    r"see /blog/",
    r"see /guides/",
    r"^this page cannot diagnose you",
    r"^patterns to monitor include:\s*$",
    r"^no\.\s+it may support overall health",
    r"readers who found humid weather",
    r"see when to go to the er",
    r"see flare go-bag",
    r"^see chapter 10\.?\s*$",
]

DROP_PARAGRAPH_RE = re.compile("|".join(DROP_PARAGRAPH_PATTERNS), re.IGNORECASE)

TEXT_REPLACEMENTS = [
    (re.compile(r"\bShare Foundation and IBDPal guides\b", re.I), "Share trusted patient-education guides"),
    (re.compile(r"\bIBDPal's community map\b", re.I), "local support groups"),
    (re.compile(r"\bFoundation chapters, ImproveCareNow families, and IBDPal's community map\b", re.I), "Patient organizations and local support groups"),
    (re.compile(r"\bTechnology platforms like IBDPal\b", re.I), "Health tracking tools"),
    (re.compile(r"\bIBDPal and similar tools\b", re.I), "Paper diaries and health apps"),
    (re.compile(r"\bLogging patterns in IBDPal or a notebook\b", re.I), "Keeping a notebook or diary"),
    (re.compile(r"\bLog (?:meals|symptoms|the form[^.]*) in IBDPal\b", re.I), "Keep a simple food and symptom log"),
    (re.compile(r"\b(?:Use |Pair with )IBDPal\b", re.I), "Use a notebook"),
    (re.compile(r"\bIBDPal food logs?\b", re.I), "food logs"),
    (re.compile(r"\bPair numbers with a short symptom log from IBDPal or paper notes\b", re.I), "Pair numbers with a short symptom log or paper notes"),
    (re.compile(r"\bPair numbers with a short symptom log from or paper notes\b", re.I), "Pair numbers with a short symptom log or paper notes"),
    (re.compile(r"\bHow IBDPal can support the non-formula parts of care\b", re.I), "Supporting the Non-Formula Parts of Care"),
    (re.compile(r"\bNutrition targets inside the app are educational companions, not a replacement for dietitian math\b", re.I), "Nutrition targets in the __IBDPAL__ app are educational tools, not replacements for individualized calculations from a dietitian"),
    (re.compile(r"\bTrack .+ in IBDPal\b", re.I), "Track meals, sleep, stools, symptoms, and energy"),
    (re.compile(r"\bwith IBDPal\b", re.I), "in a food log"),
    (re.compile(r"\bin IBDPal\b", re.I), "in a food log"),
    (re.compile(r"\bnotebook or IBDPal\b", re.I), "notebook or food log"),
    (re.compile(r"\bKeep a notebook or IBDPal log\b", re.I), "Keep a notebook or food log"),
    (re.compile(r"\b(?:Apps|Tools) like can make it easier to log[^.]*\.?", re.I), ""),
    (re.compile(r"\b(?:Apps|Tools) like can[^.]*\.?", re.I), ""),
    (re.compile(r"\b(?:Apps|Tools) like or[^.]*\.?", re.I), ""),
    (re.compile(r"\bTechnology platforms like\b", re.I), "Food and symptom logs"),
    (re.compile(r"\bIBDPal\b", re.I), ""),
    (re.compile(r"\bnotebook or\.\s*$", re.I), "notebook or food log."),
    (re.compile(r"\bnotebook or\.\s+", re.I), "notebook or food log. "),
    (re.compile(r"\bibdpal\.org\b", re.I), ""),
    (re.compile(r"\s*\|\s*IBDPal.*$", re.I), ""),
    (re.compile(r"\bFoundation patient basics\b", re.I), "Patient basics"),
    (re.compile(r"\bFoundation diet and nutrition resources\b", re.I), "Diet and nutrition in IBD"),
    (re.compile(r"\band a symptom diary guides\b", re.I), "and trusted guides"),
    (re.compile(r"\ba symptom diary's\b", re.I), "your"),
    (re.compile(r"\bEat a low-fiber diet during a flare\b", re.I), "Some people may tolerate lower-fiber foods more easily during periods of increased symptoms"),
    (re.compile(r"\bEveryone with IBD should\b", re.I), "People with IBD may"),
    (re.compile(r"\bat least yearly\b", re.I), "periodically, depending on individual risk factors"),
    (re.compile(r"\bYou should eat\b", re.I), "Some people find it helpful to eat"),
    (re.compile(r"\bYou must avoid\b", re.I), "Some people choose to avoid"),
    (re.compile(r"\bAlways eat\b", re.I), "Some people may eat"),
    (re.compile(r"\bNever eat\b", re.I), "Some people avoid"),
    (re.compile(r"\bStop eating\b", re.I), "Some people choose to stop eating"),
    (re.compile(r"\bYou need to take\b", re.I), "Your clinician may recommend"),
    (re.compile(r"\bYou must take\b", re.I), "Your clinician may recommend"),
    (re.compile(r"\bAlways avoid\b", re.I), "Some people avoid"),
    (re.compile(r"\bNever take\b", re.I), "Avoid taking without clinician guidance"),
    (re.compile(r"\bevery year\b", re.I), "periodically, based on individual risk"),
    (re.compile(r"\s+,"), ","),
    (re.compile(r"\s+\."), "."),
    (re.compile(r"\s{2,}"), " "),
]

STANDALONE_PREFACE = """Most people diagnosed with Crohn's disease or ulcerative colitis leave the clinic with more questions than answers about food. Social media offers conflicting elimination lists. Appointment time is short. Labs arrive without plain-language context.

I wrote this book to gather practical nutrition guidance in one place, grounded in major patient-education sources and clinical nutrition basics, not internet fear. It is not a meal plan, not a substitute for your gastroenterologist or IBD dietitian, and not a promise that one diet controls inflammation for everyone.

You will find flare-first eating ideas, remission variety, deficiency and lab literacy, named diet patterns explained honestly, enteral nutrition basics, a food reference library, and life situations from travel to pregnancy. Use what matches your season of disease; skip what does not apply with your team's approval."""

HOW_TO_USE = """Read Part I once for shared vocabulary about how IBD changes digestion and absorption. If you are in an active flare, start with Part II Chapters 6, 7 and the sample combinations in Chapter 39. If fatigue or anemia dominates, jump to Part III. Part VI works as a lookup index when you wonder about a specific food.

Each chapter opens with a short orientation and closes with key takeaways and references. Tables in Part III summarize NIH Dietary Reference Intakes and common food sources, starting points for clinic conversation, not self-prescription."""

AUTOIMMUNE_NOTE = """Inflammatory bowel disease is immune-mediated. That is different from adopting a generic "autoimmune diet" promoted online. Some people have overlapping autoimmune conditions; most viral cleanse or carnivore protocols lack IBD-specific evidence. Part I Chapter 4 separates real overlap from marketing."""

EDUCATIONAL_DISCLAIMER = """This book is a patient-education resource. It does not provide individualized medical advice, diagnosis, or treatment. It does not replace care from a gastroenterologist, registered dietitian, or other licensed clinicians.

Discuss decisions involving treatment, supplements, restrictive diets, suspected deficiencies, pregnancy, surgery, enteral nutrition, or significant or worsening symptoms with qualified clinicians before acting on general education.

Educational concepts draw on publicly available materials from major IBD education organizations where cited. Those organizations do not endorse this book or its publisher.

The author is not a physician or registered dietitian. This publication has not been formally clinically reviewed.

US-centric reference values (NIH DRI, USDA FoodData Central) appear throughout. International readers should confirm targets with local guidelines."""

CONCLUSION = """Nutrition with IBD is not one correct plate forever. It is a sequence of choices across flare, remission, labs, surgery, medication changes, and ordinary life. Use this book to prepare better questions, not to override your care team.

When inflammation is active, prioritize enough calories, protein, and fluids with textures you tolerate. When remission returns, widen variety with monitoring. When labs show gaps, treat repletion as medical care. Update your personal plan, the worksheet in Chapter 51, when disease activity or treatment changes."""

ABOUT_AUTHOR = """Aryan Shashi Kumar founded MediVue, a North Carolina 501(c)(3) nonprofit dedicated to clear patient education for people living with Crohn's disease and ulcerative colitis. He also created IBDPal, MediVue's educational platform for IBD nutrition and symptom literacy.

IBD information is everywhere, but useful answers are often scattered across research papers, clinic handouts, and social media. Aryan began this work with a simple standard: make tomorrow a little clearer than today.

That mission grew into a large library of nutrition education, now synthesized in Eating With IBD. Aryan asks of every resource: Will this help someone prepare a better question for their care team, understand a lab result, or eat more confidently during a flare or in remission?

Aryan is not a physician or registered dietitian. Medical and nutrition decisions belong with your gastroenterologist, IBD dietitian, and other licensed clinicians."""

ABOUT_BOOK = """Published by MediVue Health Education, an educational imprint of MediVue, a 501(c)(3) nonprofit organization.

Eating With IBD is a patient-education guide, not a medical textbook, treatment protocol, or clinically reviewed clinical handbook. Content draws on publicly available materials from the Crohn's & Colitis Foundation, NIH, USDA, and peer-reviewed sources where concepts are cited. Illustration licenses appear in the Illustration Credits appendix.

Related educational platform: IBDPal (ibdpal.org)."""

START_HERE = """If you are newly diagnosed → Chapters 1, 6, and 13
If you are currently flaring → Chapters 6, 7, 10, and 39
If you are in remission → Chapters 8, 12, and 26
If you are worried about deficiencies → Chapters 13–20
If you want to compare diets → Chapters 21–27
If you have a stricture → Chapters 12 and 35 (ask your team first)
If you have an ostomy → Chapter 48
If you want to look up a food → Part VI, Chapters 32–38"""

DRI_SOURCE_NOTE = (
    "Reference values from Dietary Reference Intakes (National Academies). "
    "NIH Office of Dietary Supplements fact sheets are a supporting reference. "
    "Higher targets during flares, malabsorption, or deficiency treatment require your "
    "gastroenterologist or IBD dietitian."
)

FOOD_INTRO = (
    "Amounts below are rounded from USDA FoodData Central standard portions. "
    "They help you compare foods, not prescribe a diet. Tolerance changes during "
    "Crohn's or colitis flares; reintroduce produce and fiber with your IBD dietitian."
)

IMAGE_LICENSE_NOTE = (
    "Photographs in this book are listed in the Illustration Credits appendix with "
    "source and license information. USDA FoodData Central tables contain no stock photography."
)


def heading_should_skip(text: str) -> bool:
    return bool(SKIP_HEADING_RE.search(text))


def paragraph_should_drop(text: str) -> bool:
    if not text or len(text.strip()) < 20:
        return True
    if prose_should_drop(text):
        return True
    if DROP_PARAGRAPH_RE.search(text):
        return True
    if text.lower().startswith("photos:"):
        return True
    if re.match(r"^and how they may influence", text.strip(), re.I):
        return True
    return False


def strip_boilerplate(text: str) -> str:
    text = BOILERPLATE_RE.sub("", text)
    text = re.sub(r"\s{2,}", " ", text)
    text = re.sub(r"\.\s*\.", ".", text)
    return text.strip()


def strip_trailing_web_refs(text: str) -> str:
    text = strip_web_tails(text)
    text = re.split(r"\.\s*Related:", text, maxsplit=1, flags=re.I)[0]
    text = re.split(r"\.\s*Hub:", text, maxsplit=1, flags=re.I)[0]
    return text.strip().rstrip(".")


def sanitize_book_text(text: str) -> str | None:
    if paragraph_should_drop(text):
        return None
    out = strip_boilerplate(text)
    for pattern, repl in TEXT_REPLACEMENTS:
        out = pattern.sub(repl, out)
    out = out.replace("__IBDPAL__", "IBDPal")
    out = strip_trailing_web_refs(out)
    out = apply_prose_replacements(out)
    out = remove_figure_references(out)
    out = strip_boilerplate(out)
    out = out.strip(" ·.")
    if re.search(r"\bor\.?$", out, re.I) and len(out.split()) < 20:
        return None
    if not out or len(out) < 25:
        return None
    try:
        from book_text_cleanup import is_nav_orphan, repair_text

        out = repair_text(out)
        if is_nav_orphan(out):
            return None
    except ImportError:
        pass
    return out


def sanitize_title(title: str) -> str:
    out = title
    for pattern, repl in TEXT_REPLACEMENTS:
        out = pattern.sub(repl, out)
    out = re.sub(r"\s*\|\s*.*$", "", out)
    return out.strip()
