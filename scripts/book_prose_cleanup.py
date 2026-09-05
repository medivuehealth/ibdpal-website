"""Web-article residue removal and figure-reference cleanup for book prose."""

from __future__ import annotations

import re

# Entire sections pasted onto many IBDPal articles (blog-expansion footer blocks)
SKIP_SECTION_HEADINGS = frozenset(
    h.lower()
    for h in (
        "Building habits that last beyond a flare",
        "Coordinating care across your health team",
        "Planning ahead when life gets busy",
        "When symptoms shift despite good habits",
        "Recording what works for your next visit",
        "Medical Disclaimer",
        "Medical disclaimer",
        "Related reading",
        "Related resources",
        "Questions for your gastroenterologist or dietitian",
        "When food questions become urgent",
        "Partnering with your care team",
        "Common questions",
        "Frequently asked questions",
        "Balanced meals and ingredients relevant to gut health",
        "Whole foods and dietary variety",
        "The Gut Microbiome and Inflammation",
        "Looking Toward Personalized Nutrition",
        "When to Seek Prompt Medical Advice",
        "Practical tips",
        "Approximate macros",
        "During a flare",
        "In remission",
        "Prep ideas that often feel kinder",
        "More detail for careful readers",
        "Movement and posture",
        "Obstruction warning signs",
        "Recording what works for your next visit",
        "Building habits that last beyond a flare",
        "When symptoms shift despite good habits",
        "Planning ahead when life gets busy",
        "Coordinating care across your health team",
        "How IBDPal can support",
        "Sample week-one conversation agenda",
        "Keeping ICU research in context",
    )
)

SEO_HEADING_PREFIXES = (
    "nutrition snapshot",
    "common myths",
    "flare versus remission",
    "how to track",
    "my ibd nutrition snapshot",
    "approximate macros",
    "micronutrients and extras",
    "during a flare",
    "in remission",
    "during remission",
    "prep ideas",
    "movement and posture",
    "obstruction warning",
    "more detail for careful",
)

# Part VI food articles use these headings as the real entry structure.
FOOD_ARTICLE_STRUCTURE_PREFIXES = (
    "nutrition snapshot",
    "nutrition",
    "flare versus remission",
    "during a flare",
    "in remission",
    "during remission",
    "prep ideas",
    "preparation or modification",
    "common myths",
    "what to watch",
    "approximate macros",
    "micronutrients",
    "ask your care team",
)


def norm_heading(text: str) -> str:
    """Normalize heading text for skip/dedup matching."""
    return re.sub(r"\s+", " ", text.lower().strip()).rstrip(".")

# Drop standalone paragraphs (exact prefix match after normalize)
DROP_PARAGRAPH_PREFIXES = tuple(
    p.lower()
    for p in (
        "Bring one prioritized question from this article",
        "Choose one practical step from this guide",
        "Bring a written symptom and medication list to each gastroenterology visit",
        "Track patterns over one to two weeks before clinic visits because single-day snapshots",
        "Keep a brief symptom and lifestyle log for one to two weeks before appointments",
        "List medications, supplements, and missed doses honestly. Small adherence gaps",
        "Ask your gastroenterologist whether dietitian, mental health, physical therapy",
        "Share updates from other specialists at GI visits so drug interactions",
        "Use your patient portal to upload outside lab results",
        "Pair new habits with existing routines, such as taking evening meds",
        "Revisit your plan after travel, holidays, or medication changes",
        "Pack medications, snacks, and a small symptom kit before exams",
        "Identify backup clinicians or infusion centers near work",
        "Discuss preventive plans with your clinician before predictable stress seasons",
        "Return to your GI team if new bleeding, fever, weight loss, or pain appears even when you follow general lifestyle guidance",
        "Labs and stool markers sometimes change before you feel improvement",
        "Do not assume setbacks mean personal failure. Inflammatory bowel disease activity fluctuates",
        "This article is for educational purposes only",
        "This article does not replace",
        "Contact your clinician if you see significant weight loss",
        "Scientists are actively studying",
        "And how they may influence",
        "Patient education supports shared decision making",
        "Discuss how this topic applies to your current disease activity",
        "Second opinions are reasonable when plans feel unclear",
        "Medication adherence and follow-up labs are as important",
        "Tell your team about travel, work stress, sleep changes",
        "Write down questions for your gastroenterologist before each visit",
        "Symptom patterns tracked over several days are more useful",
        "Bring prior colonoscopy, imaging, and pathology reports",
        "Children, older adults, and post-surgical patients may need modified",
        "If symptoms worsen while you try these steps",
        "Bring these observations to your next IBD appointment",
        "Your GI team can adjust recommendations based on labs",
        "Logging patterns in",
        "Keeping a notebook or diary helps clinicians see trends",
        "Unplanned weight loss with diarrhea, blood, or fever suggests active inflammation or malabsorption",
        "Track weekly weights at the same time of day",
        "Muscle loss affects strength and bone health",
    )
)

# Always drop every occurrence (not just repeats)
ALWAYS_DROP_PREFIXES = DROP_PARAGRAPH_PREFIXES

# Drop after first manuscript occurrence only
GLOBAL_REPEAT_PREFIXES = (
    "bring a written symptom and medication list",
    "track patterns over one to two weeks before clinic",
    "keep a brief symptom and lifestyle log",
    "list medications, supplements, and missed doses honestly",
    "ask your gastroenterologist whether dietitian, mental health",
    "share updates from other specialists at gi visits",
    "use your patient portal to upload outside lab results",
    "nutrition as partner to medical therapy",
    "macronutrients that matter",
    "micronutrients and the microbiome",
    "working with professionals",
    "tolerance with crohn's disease or ulcerative colitis is individual",
    "amounts vary by brand, cooking method, and portion",
    "gentler options many people use during flares",
    "wider options when remission allows more variety",
)

FIGURE_REF_PATTERNS = [
    re.compile(r"\bas shown in Figure\s+[0-9.]+[^.]*\.?", re.I),
    re.compile(r"\bsee Figure\s+[0-9.]+[^.]*\.?", re.I),
    re.compile(r"\bFigure\s+[12]\.[12]\b[^.]*\.?", re.I),
    re.compile(r"\bshown (?:below|above|in the (?:figure|diagram))[^.]*\.?", re.I),
    re.compile(r"\billustrated below[^.]*\.?", re.I),
    re.compile(r"\bas (?:depicted|illustrated) (?:below|above)[^.]*\.?", re.I),
    re.compile(r"\[?\s*insert diagram[^\]]*\]?", re.I),
    re.compile(r"\bdiagram placeholder\b", re.I),
]

WEB_TAIL_PATTERNS = [
    re.compile(r"\.\s*Related reading:.*$", re.I),
    re.compile(r"\.\s*Related:.*$", re.I),
    re.compile(r"\s*Related reading:.*$", re.I),
    re.compile(r"\s*Related:.*$", re.I),
    re.compile(r"\s*Hub:\s*.*$", re.I),
    re.compile(r"\s*Overview:.*$", re.I),
    re.compile(r"\s*See\s+/[\w\-/]+.*$", re.I),
]

INTERNAL_REF_REPLACEMENTS = [
    (re.compile(r"See micronutrient deficiencies and fatigue and brain fog[^.]*\.?", re.I), "See Chapters 13 and 17 for deficiency and fatigue guidance."),
    (re.compile(r"See also our FODMAP diet article[^.]*\.?", re.I), "See Chapter 23 for FODMAP basics."),
    (re.compile(r"See also our ostomy basics article[^.]*\.?", re.I), "See Chapter 48."),
    (re.compile(r"Pair this reading with hydration tips[^.]*\.?", re.I), "See Chapter 10 for hydration guidance."),
    (re.compile(r"pair with hydration tips[^.]*\.?", re.I), "See Chapter 10."),
    (re.compile(r"See newly diagnosed hub[^.]*\.?", re.I), "See Chapter 6."),
    (re.compile(r"\bnutrition hub\.?", re.I), ""),
    (re.compile(r"\bflare help hub\.?", re.I), "See Chapter 7."),
    (re.compile(r"Complete IBD nutrition guide,\s*", re.I), ""),
    (re.compile(r"Nutrition hub\.?", re.I), ""),
    (re.compile(r"Explore college disability offices during junior year campus visits\.?", re.I), "Ask about disability office resources during junior-year campus visits."),
    (re.compile(r"See also Greek yogurt[^.]*\.?", re.I), "See fermented dairy guidance in Chapter 27."),
    (re.compile(r"Using a tracking app can help users recognize recurring trends over weeks or months\.\s*Tools like can make it easier to log meals and symptoms\.?", re.I), "Tracking meals and symptoms over several weeks helps you recognize recurring trends."),
    (re.compile(r"Tracking hydration alongside symptoms can help identify patterns between fluid intake and flare severity\.\s*Apps like can[^.]*\.?", re.I), "Tracking hydration alongside symptoms can help identify patterns between fluid intake and flare severity."),
    (re.compile(r"\b(?:Apps|Tools) like can make it easier to log[^.]*\.?", re.I), ""),
    (re.compile(r"\b(?:Apps|Tools) like can[^.]*\.?", re.I), ""),
    (re.compile(r"Explore protein meals for IBD and the pillar complete IBD nutrition guide\.?", re.I), "See Chapter 11 for protein guidance."),
    (re.compile(r"Hydration support: hydration tips\.?", re.I), "See Chapter 10."),
    (re.compile(r"Explore tracking food and symptoms and visit prep\.?", re.I), "See Chapters 49 and 50."),
    (re.compile(r"Map common sites with extraintestinal manifestations\.[^.]*\.?", re.I), ""),
    (re.compile(r"For joints, see joint pain and arthritis and ankylosing spondylitis and IBD\.?", re.I), ""),
    (re.compile(r"Readers who found humid weather symptoms or summer heat hydration often need this dehydration checklist next\.?", re.I), ""),
    (re.compile(r"\.\s*Use when to go to the ER and GI vs ER decision tree\.?", re.I), "."),
    (re.compile(r"\.\s*See when to go to the ER and GI vs ER decision tree\.?", re.I), "."),
    (re.compile(r"\.\s*See flare go-bag\.?", re.I), "."),
    (re.compile(r"See flare go-bag\.?", re.I), ""),
    (re.compile(r"See when to go to the ER and GI vs ER decision tree\.?", re.I), ""),
    (re.compile(r"Tracking meals and symptoms over several weeks helps you recognize recurring trends\.\s*consistently and share summaries[^.]*\.?", re.I), "Tracking meals and symptoms over several weeks helps you recognize recurring trends you can share with your care team."),
    (re.compile(r"Hydration and protein: Gentle fuel supports recovery;\s*See Chapter 10\.?", re.I), "Gentle fuel supports recovery; pair meals with adequate hydration (see Chapter 10)."),
    (re.compile(r"\.\s*See Chapter 10\.\s*$"), "."),
    (re.compile(r"^See Chapter 10\.\s*$"), ""),
    (re.compile(r"^Patterns to monitor include:\s*$"), ""),
    (re.compile(r"^No\.\s+It may support overall health but does not replace IBD medications when needed\.?\s*$", re.I), ""),
    (re.compile(r"This page cannot diagnose you\.[^.]*\.?", re.I), ""),
    (re.compile(r"Annual or symptom-based testing may be appropriate\.?", re.I), "Monitoring frequency depends on disease location, activity, medications, surgery history, previous deficiencies, and clinician judgment."),
    (re.compile(r"Annual or flare-based CBC, iron studies, B12, vitamin D\.?", re.I), "Monitoring frequency depends on disease location, activity, medications, surgery history, previous deficiencies, and clinician judgment."),
    (re.compile(r"\b(?:Apps|Tools) like or[^.]*\.?", re.I), ""),
    (re.compile(r"Read sugar alcohols and fiber additives[^.]*\.?", re.I), ""),
    (re.compile(r"Read fiber and IBD diet before making large changes[^.]*\.?", re.I), "See Chapter 12 before making large fiber changes, especially if you have known narrowing."),
    (re.compile(r"Guide:\s*dairy and lactose in IBD\.?", re.I), "See Chapter 27 for dairy and lactose."),
    (re.compile(r"See hydration tips for IBD and the hydration fluids guide\.?", re.I), "See Chapter 10 for hydration guidance."),
    (re.compile(r"Details and sample ideas:\s*low-residue diet for flares\.?", re.I), "See Chapter 22 for low-residue patterns during flares."),
    (
        re.compile(
            r"See\s+low-residue flare guide\s+and\s+low-residue patient guide\.?",
            re.I,
        ),
        "See Chapter 22 for a fuller discussion of low-residue eating and gentle textures.",
    ),
    (
        re.compile(
            r"Shift to softer proteins: eggs, tofu, fish, broth-based soups\. "
            r"Pair with low-residue flare guidance if your team recommends it\.?",
            re.I,
        ),
        (
            "If symptoms temporarily make meals difficult during remission, softer proteins such as "
            "eggs, tofu, fish, or broth-based soups may be easier to tolerate. Persistent or worsening "
            "symptoms should be discussed with your care team rather than managed through restriction alone."
        ),
    ),
    (re.compile(r"This page explains what [^.]+\.?\s*", re.I), ""),
    (re.compile(r"\bHigh protein diet Crohn'?s disease,\s*IBD meal plan,\s*and ulcerative colitis protein are among the most common nutrition searches\.\s*", re.I), ""),
    (re.compile(r"are among the most common nutrition searches\.\s*", re.I), ""),
    (re.compile(r"\bis one of the most searched[^.]+\.\s*", re.I), ""),
    (re.compile(r"\bare among the most searched[^.]+\.\s*", re.I), ""),
    (re.compile(r"This page explains what (?:vitamin [a-z]|\w+) does, why IBD raises risk, gentler food sources, and questions for your GI or dietitian\.?\s*", re.I), ""),
    (re.compile(r"It is education only, not a dose or supplement prescription\.?\s*", re.I), ""),
    (re.compile(
        r"Log meals and symptoms in a food log so your team can connect intake patterns with labs\.\s*"
        r"See how sets nutrition targets and food symptom tracking\.?\s*"
        r"This page explains what vitamin c does[^.]+\.?\s*",
        re.I,
    ), ""),
    (re.compile(r"Log meals and symptoms in a food log so your team can connect intake patterns with labs\.?\s*", re.I), ""),
    (re.compile(
        r"Vitamin A supports vision, immune barriers, and epithelial health\. It is fat-soluble, so fat malabsorption[^.]+\.",
        re.I,
    ), (
        "Vitamin A supports vision, immune barriers, and epithelial health. Because it is fat-soluble, "
        "malabsorption, bowel resection, and highly restrictive diets can affect vitamin A status, "
        "while excessive supplementation can cause toxicity."
    )),
    (re.compile(
        r"Vitamin C \(ascorbic acid\) supports collagen, immune cell function, and non-heme iron absorption\. "
        r"People with IBD often worry about citrus[^.]+\.",
        re.I,
    ), (
        "Vitamin C supports collagen formation, normal immune function, and absorption of non-heme iron. "
        "Limited produce intake during restrictive periods may reduce dietary vitamin C intake."
    )),
    (re.compile(r"\bIBD fatigue\b[^.]+\bamong the most frustrating[^.]+\.\s*", re.I), "Fatigue and brain fog are common IBD symptoms, even when bowel movements improve. "),
    (re.compile(r"See our iron, B12, and vitamin D article[^.]*\.?", re.I), "See Chapters 15–17"),
    (re.compile(r"and micronutrient deficiencies guide\.?", re.I), ""),
    (re.compile(r"For anemia context, see anemia and iron deficiency in IBD\.?", re.I), "For a fuller discussion of iron deficiency and anemia, see Chapter 15."),
    (re.compile(r"For anemia context, see[^.]*anemia[^.]*\.?", re.I), "For a fuller discussion of iron deficiency and anemia, see Chapter 15."),
    (re.compile(r"\bIron, B12, and vitamin D\b are so common we cover them in a dedicated article\.?", re.I), "Iron, vitamin B12, and vitamin D are covered in dedicated chapters."),
    (re.compile(r"\bIron, B12, and vitamin D\b are so common we cover them in dedicated chapters\. Beyond those:", re.I), "Iron, vitamin B12, and vitamin D are covered in dedicated chapters. Beyond those:"),
    (re.compile(r"See how sets nutrition targets and food symptom tracking\.?", re.I), ""),
    (re.compile(r"See how IBDPal sets nutrition targets[^.]*\.?", re.I), ""),
    (re.compile(r"Log meals and symptoms in IBDPal so your team can connect intake patterns with labs\.[^.]*\.?", re.I), ""),
    (re.compile(r"Log meals and symptoms in a food log so your team can connect intake patterns with labs\.[^.]*\.?", re.I), ""),
    (
        re.compile(r"IV repletion sometimes beats oral when inflammation is high\.?", re.I),
        (
            "Clinician-directed intravenous repletion may be appropriate when oral supplementation "
            "is ineffective, poorly tolerated, or insufficient in the setting of active disease."
        ),
    ),
    (re.compile(r"Prioritize sleep during flares \(see Part VII\)\.?", re.I), ""),
    (re.compile(r"Protein spreads across meals supports mucosal repair\.?", re.I), "Spreading protein intake across meals supports tissue repair and recovery."),
    (re.compile(r"\bFiber During flares,\s*many clinicians suggest lower-fiber textures temporarily\.?", re.I), "During flares, clinicians may suggest lower-fiber textures temporarily."),
    (re.compile(r"Bring a photo of the portal report to the visit\.?", re.I), "Bring or have access to recent laboratory results during the visit."),
    (re.compile(r"Smoking cessation is non-negotiable for bone and IBD outcomes\.?", re.I), "Smoking cessation is particularly important for both bone health and IBD outcomes."),
    (re.compile(r"Smoking cessation dramatically improves bone and IBD outcomes\.?", re.I), "Smoking cessation is particularly important for both bone health and IBD outcomes."),
    (re.compile(r"Minimize cumulative prednisone exposure through timely biologic or immunomodulator escalation when indicated\.?", re.I), "Because cumulative corticosteroid exposure can affect bone health, clinicians may consider steroid-sparing treatment strategies when appropriate."),
    (re.compile(r"Read sleep during flares\.?", re.I), ""),
    (re.compile(r"see depression and anxiety with IBD\.?", re.I), "discuss depression and anxiety screening with your team"),
    (re.compile(r"Repeat calprotectin in two weeks if symptoms conflict with a single high value\.?", re.I), "When symptoms and a single calprotectin result conflict, clinicians may consider repeat testing based on the broader clinical picture."),
    (re.compile(r"Rising markers with symptoms may prompt steroid bridge, dose increase, or scope\.?", re.I), "Rising markers alongside symptoms may prompt the care team to reassess treatment or consider additional evaluation."),
    (re.compile(r"Recheck labs four to eight weeks after starting therapy\.?", re.I), "Clinicians typically recheck labs after starting therapy, based on individual response."),
    (re.compile(r", consistency beats complexity\.", re.I), ". Consistency beats complexity."),
    (re.compile(r"\b(?:notebook or food log|food log), consistency beats complexity\b", re.I), "notebook or food log. Consistency beats complexity"),
    (re.compile(r"\bBring or paper logs\b", re.I), "Bring digital or paper logs"),
    (re.compile(r"\bHow Can Support the Non-Formula Parts of Care\b", re.I), "Supporting the Non-Formula Parts of Care"),
    (re.compile(r"\bHow IBDPal can support the non-formula parts of care\b", re.I), "Supporting the Non-Formula Parts of Care"),
    (re.compile(r"\bNutrition targets inside the app are educational companions[^.]*\.?", re.I), "Nutrition targets in the IBDPal app are educational tools, not replacements for individualized calculations from a dietitian."),
    (re.compile(r"If your prescribed carton count and the app's general targets disagree[^.]*\.?", re.I), "If your prescribed carton count and IBDPal's general targets disagree, follow the prescription and ask the clinic to reconcile."),
    (re.compile(r"\bSeparate calcium supplements from iron doses when possible\.?", re.I), "Calcium can affect iron absorption, so ask your clinician or pharmacist whether supplement timing should be separated."),
    (re.compile(r"\bAnnual or more frequent labs guide supplementation\.?", re.I), "Periodic laboratory monitoring, individualized by the care team, helps guide supplementation."),
    (re.compile(r"\bTrack meals and symptoms in a log next to sleep, stools, and meals for visit-ready trends\.?", re.I), "Track meals, sleep, stools, symptoms, and energy to create visit-ready trends."),
    (re.compile(r"\bTrack meals, sleep, stools, symptoms, and energy next to sleep, stools, and meals for visit-ready trends\.?", re.I), "Track meals, sleep, stools, symptoms, and energy to create visit-ready trends."),
    (re.compile(r"\bSee school and workplace rights\.?", re.I), "For school-related planning, see Chapter 45."),
    (re.compile(r"Screen with your team;\s*discuss depression and anxiety screening with your team\.?", re.I), "Discuss depression and anxiety screening with your care team when appropriate."),
    (re.compile(r"Screen with your team;\s*see depression and anxiety with IBD\.?", re.I), "Discuss depression and anxiety screening with your care team when appropriate."),
    (re.compile(r"\blonger than directed,\s*your gut still needs\b", re.I), "longer than directed. Your gut still needs"),
    (re.compile(r"\bSee Chapters 15,\s*17\b", re.I), "See Chapters 15–17"),
    (re.compile(r"\bSee Chapters 15–17 and\s*\.?", re.I), "See Chapters 15–17."),
    (
        re.compile(
            r"Crohn's disease can affect any part of the digestive tract, so nutrition needs vary "
            r"by disease location, prior surgery, and activity level\. This (?:chapter|guide) "
            r"outlines common diet and nutrition topics patients review with their GI team\. "
            r"It is educational only and does not replace personalized medical or nutrition advice\.",
            re.I,
        ),
        (
            "Crohn's disease can affect any part of the digestive tract, so nutrition needs vary "
            "by disease location, prior surgery, and activity level."
        ),
    ),
    (
        re.compile(r"Travel, exercise, and illness stacks burdens quickly\.?", re.I),
        "Travel, exercise, and illness can compound these losses quickly.",
    ),
    (
        re.compile(r"Small snacks every few hours beat forcing large plates\.?", re.I),
        "Small snacks every few hours may be easier to tolerate than forcing large meals.",
    ),
    (
        re.compile(
            r"Active symptoms: white rice, refined pasta, peeled potatoes, and smooth soups are common go-tos\.?",
            re.I,
        ),
        (
            "During active symptoms, white rice, refined pasta, peeled potatoes, and smooth soups "
            "are common short-term options."
        ),
    ),
    (re.compile(r"\bMany adults discuss roughly 1-1\.2 g per kg body weight with dietitians during recovery[^.]*\.", re.I), "Protein needs may increase during recovery from active inflammation, surgery, or malnutrition. Dietitians can individualize grams per kilogram based on body weight, disease activity, nutritional status, and recovery needs."),
    (re.compile(r"\bMany adults discuss roughly 1\.2 g per kg body weight with dietitians during recovery[^.]*\.", re.I), "Protein needs may increase during recovery from active inflammation, surgery, or malnutrition. Dietitians can individualize grams per kilogram based on body weight, disease activity, nutritional status, and recovery needs."),
    (
        re.compile(r"Magnesium supports muscles, nerves, and energy metabolism\. IBD\.?", re.I),
        "Magnesium supports muscle and nerve function as well as normal energy metabolism.",
    ),
    (
        re.compile(
            r"Magnesium supports muscles, nerves, and energy metabolism\. IBD patients often search[^.]+\.",
            re.I,
        ),
        "Magnesium supports muscle and nerve function as well as normal energy metabolism.",
    ),
    (
        re.compile(
            r"IV iron is common when oral forms fail, losses are high, or inflammation blocks absorption\.?",
            re.I,
        ),
        (
            "Clinicians may use IV iron when oral iron is ineffective, poorly tolerated, or "
            "insufficient in the setting of ongoing losses or active inflammation."
        ),
    ),
    (
        re.compile(
            r"Food first is the usual starting point\. Supplements belong under clinician guidance[^.]*\.?",
            re.I,
        ),
        (
            "Food can contribute to intake, while confirmed deficiency or medication-related needs "
            "may require clinician-directed supplementation."
        ),
    ),
    (
        re.compile(r"approach trigger discovery safely\. Education only\.?", re.I),
        "approach trigger discovery safely.",
    ),
    (
        re.compile(
            r"A jump from 80 to 300 mcg/g matters more than debating whether 45 is normal at one lab versus another\.?",
            re.I,
        ),
        (
            "Trends over time usually matter more than a single result compared with one lab's "
            "reference range. Rising values alongside symptoms may prompt your team to reassess "
            "treatment; falling values often track with healing, but symptoms and scopes still "
            "guide decisions together."
        ),
    ),
    (re.compile(r"\bPatients search it after [^.]+\.\s*", re.I), ""),
    (re.compile(r"^Patients often search [^.]+\.\s*", re.I | re.M), ""),
    (
        re.compile(
            r"Searches like [^.]+ spike when labs come back low or fatigue will not quit\.[^.]*\.\s*",
            re.I,
        ),
        "",
    ),
    (
        re.compile(
            r"which is why flares and potassium searches overlap\.?",
            re.I,
        ),
        "which is why potassium losses often rise during active flares with diarrhea or vomiting.",
    ),
    (
        re.compile(
            r"Zinc is a trace mineral used in hundreds of enzymes\. Patients search it after [^.]+\.\s*",
            re.I,
        ),
        (
            "Zinc is a trace mineral used in hundreds of enzymes. Hair thinning, poor wound healing, "
            "taste changes, and chronic diarrhea can signal low stores worth discussing with your team. "
        ),
    ),
    (
        re.compile(r"\bpopular in anti-inflammatory diet searches\b", re.I),
        "often highlighted in anti-inflammatory eating patterns",
    ),
    (
        re.compile(r"\bpeople (?:often )?search(?:ing)?\b[^.]+\.\s*", re.I),
        "",
    ),
    (
        re.compile(r"\bpatients (?:often )?search(?:ing)?\b[^.]+\.\s*", re.I),
        "",
    ),
    (re.compile(r"\bsearches like\b[^.]+\.\s*", re.I), ""),
    (re.compile(r"\bLabs and monitoring people ask about\b", re.I), "Labs and monitoring to discuss"),
    (re.compile(r"^patients ", re.M), "Patients "),
    (
        re.compile(
            r"Handgrip strength and energy are informal signs of recovery\.\s*",
            re.I,
        ),
        "",
    ),
    (
        re.compile(
            r"Repeat albumin and prealbumin only as your clinician orders; trends matter\.\s*",
            re.I,
        ),
        (
            "Albumin and prealbumin are strongly influenced by inflammation and are not standalone "
            "measures of nutritional status; repeat them only when your clinician orders them, "
            "and interpret trends with symptoms and other labs."
        ),
    ),
    (
        re.compile(
            r"Short-term low-residue diets may reduce mechanical irritation before colonoscopy prep or during severe colitis\.\s*",
            re.I,
        ),
        (
            "Short-term low-residue diets may reduce mechanical irritation during severe colitis. "
            "Before colonoscopy, follow only the prep instructions your endoscopy team provides."
        ),
    ),
    (
        re.compile(
            r"Children and teens need adequate fiber for growth when safe\.\s*Over-restriction affects bone and colon health long term\.\s*",
            re.I,
        ),
        (
            "Children and teens need nutritionally adequate diets that support growth, while fiber "
            "may need temporary modification when clinically appropriate."
        ),
    ),
    (
        re.compile(
            r"If you cannot maintain intake for more than a day or two, contact your clinic\.\s*",
            re.I,
        ),
        (
            "If you cannot maintain adequate food or fluid intake, contact your care team promptly."
        ),
    ),
    (
        re.compile(
            r"Reintroduce one food every three to seven days while logging stools, pain, and gas\.\s*",
            re.I,
        ),
        (
            "One approach is to reintroduce foods individually over several days while logging "
            "stools, pain, and gas."
        ),
    ),
    (
        re.compile(
            r"Very dark urine, dizziness on standing, rapid heartbeat, confusion, or inability to keep fluids down for 24 hours need prompt outreach\.\s*",
            re.I,
        ),
        (
            "Very dark urine, dizziness on standing, rapid heartbeat, confusion, or persistent "
            "inability to keep fluids down warrant prompt medical guidance."
        ),
    ),
    (
        re.compile(
            r"Request monitoring at routine visits\.\s*",
            re.I,
        ),
        "Ask your care team whether periodic monitoring is appropriate.",
    ),
    (
        re.compile(
            r"Introduce one new food every few days when expanding your diet\.\s*",
            re.I,
        ),
        (
            "One approach is to introduce foods individually over several days while watching "
            "for patterns."
        ),
    ),
    (
        re.compile(
            r"One new food every few days (?:clarifies triggers versus coincidence|isolates triggers)\.\s*",
            re.I,
        ),
        "Introduce foods individually while monitoring tolerance.",
    ),
    (
        re.compile(
            r"Reintroduce one new food every few days when expanding your diet\.\s*",
            re.I,
        ),
        "Introduce foods individually while monitoring tolerance.",
    ),
    (
        re.compile(
            r"Increase fiber gradually over weeks, not days\.\s*",
            re.I,
        ),
        "Increase fiber gradually as tolerated rather than making large changes at once.",
    ),
    (
        re.compile(
            r"Introduce one new fiber source weekly to identify personal thresholds\.\s*",
            re.I,
        ),
        "Introduce new fiber sources individually so tolerance is easier to interpret.",
    ),
    (
        re.compile(
            r"Fat malabsorption after ileal disease, resection, or cholestyramine use\s*",
            re.I,
        ),
        (
            "Fat malabsorption associated with extensive small-bowel disease, resection, or "
            "bile-acid disturbances may increase risk"
        ),
    ),
    (
        re.compile(
            r"Hospital or exclusive liquid diets without complete micronutrient coverage in rare cases\s*",
            re.I,
        ),
        "Prolonged nutritionally incomplete liquid diets (in rare cases)",
    ),
    (
        re.compile(
            r"Calprotectin should trend toward remission before attributing symptoms to FODMAPs alone\.\s*",
            re.I,
        ),
        (
            "Evidence of active inflammation should be considered before symptoms are attributed "
            "primarily to FODMAP intolerance."
        ),
    ),
    (
        re.compile(
            r"Weighing yourself at the same time daily can reveal fluid loss trends when stool counts are hard to measure\.\s*",
            re.I,
        ),
        (
            "Your care team may recommend monitoring weight at consistent times when stool counts "
            "are hard to measure."
        ),
    ),
    (
        re.compile(
            r"Inflammation, fever, and diarrhea increase protein breakdown\.\s*",
            re.I,
        ),
        (
            "Active inflammation, fever, significant losses, surgery, and inadequate intake can "
            "increase protein requirements or contribute to muscle loss."
        ),
    ),
    (
        re.compile(
            r"Some fiber supplements interact with timing of mesalamine or thyroid pills\. Separate doses by a few hours unless your pharmacist says otherwise\.\s*",
            re.I,
        ),
        (
            "Fiber supplements can affect the timing or absorption of some medications. Ask your "
            "pharmacist whether your medicines should be separated from fiber supplements."
        ),
    ),
    (
        re.compile(
            r"Improving symptoms: reintroduce fiber slowly with professional guidance\.?",
            re.I,
        ),
        "As symptoms improve, reintroduce fiber gradually with professional guidance.",
    ),
    (
        re.compile(
            r"High-dose iron or calcium supplements can compete with zinc absorption when timed poorly\.\s*",
            re.I,
        ),
        (
            "High-dose mineral supplements can affect the absorption of other minerals, another "
            "reason to review supplement combinations with your care team."
        ),
    ),
    (
        re.compile(
            r"Some diuretics or other medicines affect potassium \(review your full list\)\s*",
            re.I,
        ),
        (
            "Some diuretics and other medications can affect potassium levels. Review your full "
            "medication list with your clinician or pharmacist."
        ),
    ),
    (
        re.compile(
            r"Small bowel Crohn'?s may affect absorption of iron, B12, and fat-soluble vitamins\.\s*",
            re.I,
        ),
        (
            "Small-bowel Crohn's can affect nutrient absorption depending on disease location; "
            "terminal ileal disease or resection is particularly relevant to vitamin B12 and "
            "bile-acid absorption."
        ),
    ),
    (
        re.compile(
            r"Track stool count, blood, fever, and weight at home\.\s*",
            re.I,
        ),
        (
            "Keeping track of stool frequency, bleeding, fever, or meaningful weight changes can "
            "give your GI team useful context."
        ),
    ),
    (
        re.compile(
            r"Monitor weight weekly during flares\.\s*",
            re.I,
        ),
        (
            "When weight loss is a concern, your care team may recommend monitoring weight during "
            "flares."
        ),
    ),
    (
        re.compile(
            r"Spread calcium intake across meals if supplements are needed\.\s*",
            re.I,
        ),
        (
            "If calcium supplements are needed, ask your clinician or pharmacist about dose and "
            "timing."
        ),
    ),
    (
        re.compile(
            r"Repeat DEXA per clinic protocol after starting therapy\.\s*",
            re.I,
        ),
        "Follow your care team's recommendations for repeat bone-density testing.",
    ),
    (
        re.compile(
            r"Zinc deficiency can impair vitamin A use \(they interact\)\s*",
            re.I,
        ),
        "Zinc status can influence vitamin A metabolism",
    ),
    (
        re.compile(
            r"Iron, B12, vitamin D, zinc, and calcium need periodic labs\.\s*",
            re.I,
        ),
        (
            "Iron, vitamin B12, vitamin D, zinc, and other nutrients may require monitoring "
            "based on individual risk."
        ),
    ),
    (
        re.compile(
            r"Track weight weekly at the same time of day\s*",
            re.I,
        ),
        (
            "When weight loss is a concern, your care team may recommend monitoring weight at "
            "consistent times."
        ),
    ),
    (
        re.compile(
            r"Track weekly weights at the same time of day\.\s*",
            re.I,
        ),
        (
            "When weight loss is a concern, your care team may recommend monitoring weight at "
            "consistent times."
        ),
    ),
    (
        re.compile(
            r"Active inflammation can suppress appetite while increasing calorie needs\.\s*",
            re.I,
        ),
        (
            "Active inflammation can suppress appetite while illness, weight loss, poor intake, "
            "or recovery may increase nutritional needs."
        ),
    ),
    (
        re.compile(
            r"Surgery, resection, strictureplasty, ostomy, or pouch, can improve inflammation while permanently changing anatomy\.\s*",
            re.I,
        ),
        (
            "Surgery, including resection, strictureplasty, ostomy creation, or pouch surgery, "
            "can control disease or address complications while permanently changing anatomy."
        ),
    ),
    (
        re.compile(
            r"Thirst alone is a late signal\.\s*",
            re.I,
        ),
        (
            "Thirst may appear only after significant fluid losses, so do not rely on thirst alone "
            "during high-output days."
        ),
    ),
    (re.compile(r"\.\s*This page [^.]+\.", re.I), "."),
]

PROSE_REPLACEMENTS = [
    (re.compile(r"This pillar page maps[^.]+\.\s*", re.I), ""),
    (re.compile(r"points you to deeper[^.]+\.\s*", re.I), ""),
    (re.compile(r"\bfrom this article\b", re.I), "from this chapter"),
    (re.compile(r"\bthis guide\b", re.I), "this chapter"),
    (re.compile(r"\bthis article\b", re.I), "this chapter"),
    (re.compile(r"\bsearches like\b[^.]+\.\s*", re.I), ""),
    (re.compile(r"\s+"), " "),
]


class GlobalRepeatTracker:
    """Drop repeated web-footer sentences after the first manuscript occurrence."""

    def __init__(self) -> None:
        self.seen: set[str] = set()

    def should_drop(self, text: str) -> bool:
        if should_drop_paragraph(text):
            return True
        lower = text.lower().strip()
        if not any(lower.startswith(p) for p in GLOBAL_REPEAT_PREFIXES):
            return False
        key = re.sub(r"\s+", " ", lower)[:160]
        if key in self.seen:
            return True
        self.seen.add(key)
        return False


class ChapterSectionTracker:
    """Skip FAQ blocks and duplicate section headings within one chapter."""

    def __init__(self) -> None:
        self.headings_seen: set[str] = set()
        self.skip_until_heading = False

    def _heading_key(self, text: str) -> str:
        return norm_heading(text)

    def heading_level(self, kind: str) -> int:
        if kind.startswith("heading_h"):
            return int(kind[-1])
        return 99

    def should_skip_block(self, kind: str, content: str | list[str] | dict) -> bool:
        if not kind.startswith("heading_"):
            return self.skip_until_heading

        text = str(content)
        key = self._heading_key(text)
        level = self.heading_level(kind)

        if is_article_faq_heading(text):
            self.skip_until_heading = True
            return True

        if heading_starts_skip_section(text) or key in {
            h.lower() for h in (
                "partnering with your care team",
                "common questions",
                "frequently asked questions",
                "the gut microbiome and inflammation",
                "looking toward personalized nutrition",
                "balanced meals and ingredients relevant to gut health",
                "whole foods and dietary variety",
            )
        }:
            self.skip_until_heading = True
            return True

        if key in self.headings_seen and level >= 2:
            self.skip_until_heading = True
            return True

        self.headings_seen.add(key)
        self.skip_until_heading = False
        return False


def filter_chapter_sections(
    blocks: list[tuple[str, str | list[str] | dict]],
) -> list[tuple[str, str | list[str] | dict]]:
    tracker = ChapterSectionTracker()
    out: list[tuple[str, str | list[str] | dict]] = []
    for kind, content in blocks:
        if kind.startswith("heading_"):
            if tracker.should_skip_block(kind, content):
                continue
            out.append((kind, content))
        elif tracker.skip_until_heading:
            continue
        else:
            out.append((kind, content))
    return out


def strip_web_tails(text: str) -> str:
    out = text
    for pat in WEB_TAIL_PATTERNS:
        out = pat.sub("", out)
    return out.strip().rstrip(".")


def remove_figure_references(text: str) -> str:
    out = text
    for pat in FIGURE_REF_PATTERNS:
        out = pat.sub("", out)
    return re.sub(r"\s{2,}", " ", out).strip()


def apply_internal_refs(text: str) -> str:
    out = text
    for _ in range(3):
        for pat, repl in INTERNAL_REF_REPLACEMENTS:
            out = pat.sub(repl, out)
    out = re.sub(r"\s{2,}", " ", out).strip()
    return out


def apply_prose_replacements(text: str) -> str:
    out = text
    for pat, repl in PROSE_REPLACEMENTS:
        out = pat.sub(repl, out)
    out = apply_internal_refs(out)
    return out.strip()


def is_seo_residue_heading(text: str) -> bool:
    lower = text.lower().strip()
    return any(lower.startswith(prefix) for prefix in SEO_HEADING_PREFIXES)


def is_food_article_structure_heading(text: str) -> bool:
    lower = text.lower().strip()
    return any(lower.startswith(prefix) for prefix in FOOD_ARTICLE_STRUCTURE_PREFIXES)


def heading_starts_skip_section(text: str, *, food_mode: bool = False) -> bool:
    if food_mode and is_food_article_structure_heading(text):
        return False
    key = norm_heading(text)
    if key in SKIP_SECTION_HEADINGS:
        # Food entries intentionally use flare/remission/prep section labels.
        if food_mode and is_food_article_structure_heading(text):
            return False
        if food_mode and key in {
            "during a flare",
            "in remission",
            "during remission",
            "prep ideas that often feel kinder",
            "approximate macros",
        }:
            return False
        return True
    if food_mode:
        lower = text.lower().strip()
        if lower.startswith(("how to track", "questions for your", "when food questions")):
            return True
        if is_seo_residue_heading(text) and not is_food_article_structure_heading(text):
            return True
        return False
    return is_seo_residue_heading(text)


def should_drop_paragraph(text: str) -> bool:
    lower = text.lower().strip()
    if not lower:
        return True
    if any(lower.startswith(p) for p in ALWAYS_DROP_PREFIXES):
        return True
    if "this article is for educational purposes only" in lower:
        return True
    if lower.startswith("photos:"):
        return True
    if re.search(r"\b(?:apps|tools) like can\b", lower):
        return True
    if re.search(r"\b(?:apps|tools) like or\b", lower):
        return True
    if lower.startswith("complete ibd nutrition guide,"):
        return True
    if "nutrition hub" in lower and lower.count(",") >= 3:
        return True
    if re.search(r"see also our .+ article.*nutrition hub", lower):
        return True
    if lower.startswith("patterns to monitor include:"):
        return True
    if re.match(r"^no\.\s+it may support overall health", lower):
        return True
    if lower.startswith("this page cannot diagnose you"):
        return True
    if re.match(r"^see chapter 10\.?\s*$", lower):
        return True
    if lower.startswith("read sugar alcohols"):
        return True
    if "most common nutrition searches" in lower:
        return True
    if lower.startswith("this page explains what"):
        return True
    if "see how sets nutrition" in lower:
        return True
    if "log meals and symptoms in a food log so your team can connect intake patterns with labs" in lower:
        return True
    if "it is education only, not a dose or supplement prescription" in lower:
        return True
    if "nutrition education for ibd" in lower and len(lower) < 120:
        return True
    if "food symptom tracking" in lower and len(lower) < 100:
        return True
    if lower.startswith("this page "):
        return True
    if lower.startswith("searches like"):
        return True
    if "spike when labs come back low or fatigue" in lower:
        return True
    if re.match(r"^(protein meal ideas for ibd|micronutrient deficiencies|unintentional weight changes)\.?$", lower):
        return True
    return False


def should_drop_list_item(text: str) -> bool:
    lower = text.lower().strip()
    if should_drop_paragraph(text):
        return True
    if re.match(r"^(protein meal ideas for ibd|micronutrient deficiencies|unintentional weight changes)\.?$", lower):
        return True
    return False


def is_article_faq_heading(text: str) -> bool:
    from book_text_cleanup import is_faq_heading

    return is_faq_heading(text)


def strip_boilerplate_tail(
    blocks: list[tuple[str, str | list[str] | dict]],
) -> list[tuple[str, str | list[str] | dict]]:
    """Remove trailing blog-expansion headings (often orphaned before References)."""
    out = list(blocks)
    while out:
        kind, content = out[-1]
        if kind.startswith("heading_") and heading_starts_skip_section(str(content)):
            out.pop()
            continue
        break
    return out
