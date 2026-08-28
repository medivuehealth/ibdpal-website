#!/usr/bin/env python3
"""Topic definitions for all 58 guide expansions."""
from __future__ import annotations

# Each topic: intro OR body (foundation), sections[(heading,(p1,p2,p3))], tips, faq, related

TOPICS: dict = {}

def T(intro, sections, tips, faq, related, body=None):
    d = {"sections": sections, "tips": tips, "faq": faq, "related": related}
    if body:
        d["body"] = body
    else:
        d["intro"] = intro
    return d

# Shared paragraph helpers for consistent depth (~50 words each)
P = lambda *s: s  # paragraph tuple packer

TOPICS["what-should-i-eat-crohns-colitis"] = T(
    "There is no single best diet for Crohn's disease or ulcerative colitis. Triggers, tolerance, and nutrient needs differ by person and by whether inflammation is active or quiet. This guide summarizes patterns many patients discuss with their gastroenterologist or IBD dietitian. Education only, not medical advice.",
    [
        ("How disease activity changes food choices", P(
            "During remission, many people aim for a varied pattern with fruits, vegetables, lean protein, and grains when their clinician agrees it is safe. The goal is adequate calories, protein, and micronutrients without unnecessary restriction.",
            "During active symptoms, softer and lower-fiber foods are often easier to tolerate for a short time. Bananas, applesauce, white rice, plain pasta, eggs, broth-based soups, and lean poultry or fish appear frequently in patient education.",
            "Your GI team may suggest temporary changes while inflammation is treated. Return to a broader diet when symptoms improve, rather than staying on a minimal list indefinitely without guidance.",
        )),
        ("Building meals that support energy and healing", P(
            "Spread protein across the day if appetite is low. Eggs, yogurt, tofu, fish, and tender meats are common choices when tolerated. Pair protein with gentle starches if fiber feels harsh.",
            "Healthy fats from olive oil, avocado, or nut butters may help calories when weight is a concern. Introduce one new food at a time so you can notice patterns without guessing.",
            "Ask whether you need labs for iron, vitamin D, vitamin B12, folate, zinc, or magnesium. Malabsorption and chronic inflammation can affect stores even when you eat well.",
        )),
        ("Fiber, FODMAPs, and special diets", P(
            "Fiber is not always harmful in IBD. Some people reduce insoluble fiber during flares and reintroduce cooked vegetables and whole grains in remission with their team's support.",
            "Low FODMAP or other structured approaches are sometimes used under dietitian supervision for symptom relief. They are tools, not universal cures, and should fit your medical plan.",
            "Avoid copying social media elimination lists without clinician input. Over-restriction can cause weight loss, fatigue, and social stress without improving inflammation.",
        )),
        ("Hydration and eating rhythm", P(
            "Diarrhea, sweating, vomiting, or poor intake increase fluid needs. Water, oral rehydration solutions, broth, and decaffeinated teas are frequent suggestions when losses are higher.",
            "Smaller, more frequent meals may feel better than large portions when nausea or early fullness is present. Keep simple snacks available for low-energy days.",
            "Alcohol and high-caffeine drinks may worsen symptoms for some people. Ask your team what limits make sense for you.",
        )),
        ("Working with your IBD nutrition team", P(
            "Bring a one- to two-week food and symptom log to appointments. Note stool pattern, pain, blood, urgency, and energy alongside meals.",
            "Registered dietitians with IBD experience can help with enteral nutrition questions, repletion of deficiencies, and safe reintroduction plans.",
            "If you lose weight unintentionally, skip meals often, or fear most foods, tell your clinician promptly. Nutrition support is part of comprehensive IBD care.",
        )),
    ],
    ["Log meals and symptoms for at least one week before diet visits.", "Reintroduce one new food every few days when expanding your diet.", "Ask your GI team about iron, B12, and vitamin D labs at least yearly.", "Keep gentle backup meals frozen for flare weeks.", "Pair online diet tips with your clinic's written plan, not instead of it."],
    [("Is there one best diet for all people with IBD?", "No. Disease location, surgery history, activity level, and personal triggers vary. Your gastroenterologist or IBD dietitian should personalize guidance."),
     ("Should I cut out all fiber forever?", "Not usually. Many patients temporarily lower fiber during active symptoms and expand variety in remission with clinician guidance."),
     ("Can diet alone put IBD in remission?", "Nutrition matters and some supervised therapies are used clinically, but most people need medical monitoring and treatment tailored by their IBD team."),
     ("When should I see a dietitian?", "Consider a referral for weight change, strictures, short bowel, repeated flares, anemia, or if you feel afraid to eat.")],
    [("Foods during a Crohn's flare", "/guides/foods-to-eat-crohns-flare"), ("Anti-inflammatory diet and IBD", "/blog/anti-inflammatory-diet-ibd"),
     ("FODMAP diet for Crohn's and colitis", "/blog/fodmap-diet-crohns-colitis"), ("Track food and symptoms", "/guides/track-ibd-symptoms-food"),
     ("Foundation diet and nutrition bridge", "/guides/foundation-diet-nutrition-ibd"), ("Complete IBD nutrition article", "/blog/complete-ibd-nutrition-guide")],
)

TOPICS["foods-to-eat-crohns-flare"] = T(
    "When Crohn's inflammation is active, many people shift toward easy-to-digest meals and steady fluids. Food choices do not replace medical treatment, but they may reduce bowel irritation while your GI team adjusts therapy. These are common patterns from patient education, not rules that fit everyone.",
    [
        ("Gentle foods many patients tolerate", P(
            "Soft fruits such as bananas and applesauce, refined grains like white rice and plain pasta, and well-cooked potatoes are frequent short-term choices. Broth-based soups provide fluid and sodium when appetite is low.",
            "Lean protein from eggs, tofu, fish, or tender poultry can help maintain muscle when intake drops. Smooth nut butters or yogurt may add calories if dairy is tolerated.",
            "Avoid assuming a food is safe because it is on a list. Personal triggers still matter, and strictures or prior surgery can change what feels comfortable.",
        )),
        ("Hydration during active diarrhea", P(
            "Water alone may not replace electrolytes lost in stool. Oral rehydration solutions, diluted sports drinks, or broth can help when your team approves them.",
            "Sip steadily through the day rather than chugging large volumes if nausea is present. Ice chips or popsicles may be easier when solids are hard to manage.",
            "Limit alcohol and excess caffeine if they worsen urgency or dehydration. Herbal teas without strong laxative herbs are often better tolerated.",
        )),
        ("Foods to approach carefully", P(
            "Raw vegetables, tough skins, popcorn, nuts, seeds, and high-fat fried foods bother many people during flares. Spicy sauces and sugar alcohols in sugar-free products can increase gas or urgency.",
            "Large salads, cruciferous vegetables, and heavy cream sauces are common short-term avoids, not lifetime bans. Reintroduce them when symptoms calm with guidance.",
            "If you have a known stricture, follow texture advice from your GI team. Fiber and bulk may need special modification.",
        )),
        ("Meal timing and portion size", P(
            "Smaller meals four to six times daily may feel better than three large plates. Stop eating when comfortably full rather than pushing through pain.",
            "Keep a few ready options at home: rice, eggs, canned fruit, and low-fiber crackers. Planning reduces stress on bad days.",
            "If you cannot maintain intake for more than a day or two, contact your clinic. Early nutrition support can prevent worsening weakness.",
        )),
        ("Pairing diet with medical flare care", P(
            "Medication changes, stool testing, imaging, or labs may be needed even if food adjustments help symptoms slightly. Do not delay outreach hoping diet alone will fix inflammation.",
            "Track stool count, blood, fever, and weight at home. Share trends with your GI team at scheduled check-ins or sooner if red flags appear.",
            "Mental health support matters during flares. Anxiety about food is common and worth discussing with your care team.",
        )),
    ],
    ["Stock oral rehydration packets before symptoms worsen.", "Cook vegetables until very soft before trying raw salads again.", "Eat the highest-protein foods when appetite is best, often mornings.", "Avoid comparing your flare menu to remission social media posts.", "Call your GI team if you cannot drink enough fluids for 24 hours."],
    [("Can the right foods stop a Crohn's flare?", "Diet may ease irritation but does not treat underlying inflammation. Medical care from your IBD team is essential."),
     ("Is the BRAT diet enough long term?", "BRAT-style foods are short-term comfort choices. Long restriction without clinician input can cause nutrient gaps."),
     ("Should I fast during a flare?", "Do not fast without medical advice. Prolonged fasting can worsen fatigue and electrolyte problems.")],
    [("Crohn's flare: what to do", "/guides/crohns-flare-what-to-do"), ("Flare first 48 hours article", "/blog/flare-first-48-hours"),
     ("IBD hydration guide", "/guides/ibd-hydration-fluids"), ("Low-residue diet basics", "/guides/low-residue-diet-ibd"),
     ("Flare help hub", "/flare-help"), ("Best foods during a flare article", "/blog/best-foods-crohns-flare")],
)

# Remaining topics loaded from part 2
from _guide_topics_part2 import add_part2  # noqa: E402
add_part2(TOPICS)
