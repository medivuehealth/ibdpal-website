#!/usr/bin/env python3
# Prose style: do not use em dash. Use periods, commas, colons, or "|" in titles.
"""Generate Wave 3 micronutrient x IBD SEO blogs (extend beyond iron/B12/D)."""
from __future__ import annotations

import json
import re
import shutil
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOGS = ROOT / "blogs"
DATA = ROOT / "data" / "wave3-food-nutrition-posts.json"
SITEMAP = ROOT / "sitemap.xml"
VERCEL = ROOT / "vercel.json"
SITE = "https://www.ibdpal.org"

sys.path.insert(0, str(ROOT / "scripts"))
from generate_blog_posts import render_post  # noqa: E402

FALLBACK_IMAGE = BLOGS / "assets" / "micronutrients-ibd" / "micronutrients-ibd_1.jpg"
if not FALLBACK_IMAGE.exists():
    FALLBACK_IMAGE = BLOGS / "assets" / "low-residue" / "low-residue_1.jpg"

IMAGE_URLS = {
    "calcium-ibd": "https://images.unsplash.com/photo-1550583724-b2692b85b150?auto=format&w=1200&q=80",
    "zinc-ibd": "https://images.unsplash.com/photo-1604503468506-a8da13d82791?auto=format&w=1200&q=80",
    "magnesium-ibd": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?auto=format&w=1200&q=80",
    "potassium-ibd": "https://images.unsplash.com/photo-1571771894821-ce9b6c11b08e?auto=format&w=1200&q=80",
    "vitamin-c-ibd": "https://images.unsplash.com/photo-1547514701-42782101795e?auto=format&w=1200&q=80",
    "folate-ibd": "https://images.unsplash.com/photo-1576045057995-568f588f82fb?auto=format&w=1200&q=80",
    "vitamin-a-ibd": "https://images.unsplash.com/photo-1598170845058-32b9d6a5da37?auto=format&w=1200&q=80",
    "omega3-ibd": "https://images.unsplash.com/photo-1519708227418-c8fd9a32b7a2?auto=format&w=1200&q=80",
}


def nutrient_body(n: dict) -> str:
    name = n["name"]
    name_l = name.lower()
    roles = "".join(f"<li>{x}</li>" for x in n["roles"])
    why = "".join(f"<li>{x}</li>" for x in n["why_ibd"])
    foods_flare = "".join(f"<li>{x}</li>" for x in n["foods_flare"])
    foods_rem = "".join(f"<li>{x}</li>" for x in n["foods_remission"])
    labs = "".join(f"<li>{x}</li>" for x in n["labs"])
    myths = "".join(f"<li><strong>{m[0]}</strong> {m[1]}</li>" for m in n["myths"])
    questions = "".join(f"<li>{q}</li>" for q in n["questions"])
    related = " · ".join(f'<a href="{href}">{label}</a>' for href, label in n["related"])
    return f"""
<p>Searches like <strong>{n['primary_kw']}</strong>, <strong>{n['secondary_kw']}</strong>, and <strong>{name_l} ulcerative colitis</strong> spike when labs come back low or fatigue will not quit. This page explains what {name_l} does, why IBD raises risk, gentler food sources, and questions for your GI or dietitian. It is education only, not a dose or supplement prescription.</p>

<h2>What {name} does in the body</h2>
<p>{n['intro']}</p>
<ul class="blog-list">{roles}</ul>

<h2>Why {name_l} gaps are common in Crohn's and colitis</h2>
<ul class="blog-list">{why}</ul>
<p>{n['risk_note']}</p>

<h2>Food sources that often fit IBD eating</h2>
<p>{n['food_intro']}</p>
<h3>Gentler options many people use during flares</h3>
<ul class="blog-list">{foods_flare}</ul>
<h3>Wider options when remission allows more variety</h3>
<ul class="blog-list">{foods_rem}</ul>
<p>Food first is the usual starting point. Supplements belong under clinician guidance, especially if you have kidney disease, take interacting medicines, or already use a multivitamin.</p>

<h2>Supplements and safety notes</h2>
<p>{n['supplement_note']}</p>

<h2>Labs and monitoring people ask about</h2>
<ul class="blog-list">{labs}</ul>
<p>Log meals and symptoms in IBDPal so your team can connect intake patterns with labs. See <a href="/blog/how-ibdpal-nutrition-targets-work">how IBDPal sets nutrition targets</a> and <a href="/blog/tracking-food-symptoms-ibdpal">food symptom tracking</a>.</p>

<h2>Common myths about {name_l} and IBD</h2>
<ul class="blog-list">{myths}</ul>

<h2>Questions for your gastroenterologist or dietitian</h2>
<ul class="blog-list">{questions}</ul>

<h2>When to call sooner</h2>
<p>Seek prompt care for severe weakness, irregular heartbeat symptoms, fainting, inability to keep fluids down, heavy bleeding, or fever with rapid decline. Nutrient articles cannot diagnose emergencies. See <a href="/flare-help">flare help</a> and <a href="/blog/when-to-go-er-ibd">when to go to the ER</a>.</p>

<p>Related reading: {related}. Overview: <a href="/blog/micronutrients-ibd-deficiencies">micronutrient deficiencies in IBD</a>. Hub: <a href="/ibd-nutrition">IBD nutrition</a>.</p>
""".strip()


NUTRIENTS: list[dict] = [
    {
        "slug": "calcium-ibd",
        "name": "Calcium",
        "title": "Calcium and IBD: Bones, Dairy Alternatives, and Steroid Questions",
        "description": "Calcium with Crohn's or colitis: bone health, dairy and alternatives, steroid risk, labs, and dietitian questions. Education only.",
        "category": "Nutrition · August 2026",
        "date_display": "August 26, 2026",
        "date_iso": "2026-08-26T16:00:00Z",
        "asset_dir": "calcium-ibd",
        "resource_category": "nutrition",
        "tags": ["calcium", "bones", "dairy", "osteoporosis", "steroids", "micronutrients", "Crohn's", "colitis", "nutrition"],
        "share": "Calcium and IBD: bones, foods, and steroid questions. Education only.",
        "primary_kw": "calcium Crohn's disease",
        "secondary_kw": "calcium ulcerative colitis bones",
        "intro": (
            "Calcium is the main mineral stored in bone and teeth. It also supports muscle and nerve signaling. "
            "People with IBD often ask about calcium because steroids, low dairy intake, and vitamin D deficiency raise long-term fracture concerns."
        ),
        "roles": [
            "Builds and maintains bone mineral density over time",
            "Supports normal muscle contraction and nerve signaling",
            "Works closely with vitamin D for absorption and bone health",
        ],
        "why_ibd": [
            "Repeated corticosteroid courses increase bone loss risk",
            "Lactose intolerance or dairy avoidance reduces easy calcium sources",
            "Inflammation, surgery, and limited menus can shrink intake",
            "Low vitamin D common in IBD worsens calcium handling",
        ],
        "risk_note": (
            "Bone health is a long game. Short flare menus matter, but so do years of steroid exposure and underfueling. "
            "Pair this topic with vitamin D and DEXA discussions when your team recommends them."
        ),
        "food_intro": (
            "Aim for food sources your gut tolerates before high-dose supplements. Fortified options help when dairy is limited."
        ),
        "foods_flare": [
            "Lactose-free milk or fortified lactose-free yogurt if dairy protein sits well",
            "Fortified plant milks (check calcium on the label) in smooth textures",
            "Canned soft fish with soft bones mashed finely if tolerated (for example soft salmon)",
            "Tofu set with calcium sulfate when soy is tolerated, served soft",
        ],
        "foods_remission": [
            "Yogurt, cheese, or kefir if lactose is managed",
            "Fortified orange juice in small amounts if acidity is okay",
            "Leafy greens that you tolerate cooked (absorption varies; still useful in a varied plate)",
            "Sesame tahini or almonds if nuts/seeds are cleared",
        ],
        "supplement_note": (
            "Calcium carbonate and citrate differ in absorption with meals and acid-reducing medicines. "
            "Too much supplemental calcium is not automatically better and can cause constipation or interact with other minerals. "
            "Dosing belongs with your clinician, especially after steroid courses."
        ),
        "labs": [
            "Serum calcium is often normal even when bone risk is high; it is not a full bone status test",
            "Vitamin D (25-OH) commonly checked alongside bone planning",
            "DEXA bone density when steroids, fractures, or other risk factors apply",
        ],
        "myths": [
            ("If my blood calcium is normal, my bones are fine.", "Blood calcium is tightly regulated; bone density needs other assessment."),
            ("Dairy is banned in all IBD.", "Many people tolerate lactose-free dairy; alternatives can be fortified."),
            ("Calcium supplements replace medical IBD care.", "They support nutrition goals; they do not treat gut inflammation."),
        ],
        "questions": [
            "Do my steroid history and labs mean I need a DEXA scan?",
            "What daily calcium target fits my age, sex, and kidney status?",
            "Which form of calcium supplement, if any, fits my acid-reducing meds?",
        ],
        "related": [
            ("/guides/vitamin-d-bone-nutrition-ibd", "vitamin D and bone nutrition"),
            ("/blog/osteoporosis-bone-health-ibd", "osteoporosis and IBD"),
            ("/blog/dairy-lactose-ibd", "dairy and lactose"),
        ],
    },
    {
        "slug": "zinc-ibd",
        "name": "Zinc",
        "title": "Zinc and IBD: Immunity, Wound Healing, and Food Sources",
        "description": "Zinc with Crohn's or colitis: diarrhea losses, immunity, food sources, supplement cautions, and clinic questions. Education only.",
        "category": "Nutrition · August 2026",
        "date_display": "August 26, 2026",
        "date_iso": "2026-08-26T18:00:00Z",
        "asset_dir": "zinc-ibd",
        "resource_category": "nutrition",
        "tags": ["zinc", "immunity", "wound healing", "diarrhea", "micronutrients", "Crohn's", "colitis", "nutrition"],
        "share": "Zinc and IBD: deficiency risk and food sources. Education only.",
        "primary_kw": "zinc deficiency Crohn's",
        "secondary_kw": "zinc ulcerative colitis",
        "intro": (
            "Zinc is a trace mineral used in hundreds of enzymes. Patients search it after hair changes, poor wound healing, "
            "taste changes, or when diarrhea has been relentless."
        ),
        "roles": [
            "Supports immune function and skin/mucosal repair",
            "Helps with taste and smell in everyday nutrition",
            "Participates in protein synthesis and cell division",
        ],
        "why_ibd": [
            "Chronic diarrhea increases zinc losses in stool",
            "Small bowel Crohn's disease and resections can reduce absorption",
            "Low meat intake or strict plant-only patterns without planning can lower intake",
            "High-dose iron or calcium supplements can compete with zinc absorption when timed poorly",
        ],
        "risk_note": (
            "Zinc deficiency can look like ongoing fatigue, skin issues, or slow healing, but those symptoms have many causes. "
            "Labs and clinical context matter more than buying the largest zinc bottle online."
        ),
        "food_intro": "Animal proteins are efficient zinc sources. Plant sources help when portions and preparation are planned.",
        "foods_flare": [
            "Tender chicken, turkey, or eggs",
            "Soft fish if tolerated",
            "Smooth nut butters in small amounts if approved",
            "Fortified cereals that are low residue if your plan allows",
        ],
        "foods_remission": [
            "Beef or other meats if tolerated and desired",
            "Pumpkin seeds or legumes when fiber is okay",
            "Dairy foods if lactose is managed",
            "Shellfish for some people when food safety and tolerance allow",
        ],
        "supplement_note": (
            "High-dose zinc for weeks can lower copper and upset the stomach. "
            "Lozenge and mega-dose trends are not IBD treatment protocols. Use team-directed doses based on labs when deficiency is confirmed or strongly suspected."
        ),
        "labs": [
            "Plasma zinc can be influenced by inflammation and albumin; interpret with your clinician",
            "Watch copper if you take prolonged high-dose zinc",
            "Reassess after diarrhea improves or diet expands",
        ],
        "myths": [
            ("Zinc supplements stop Crohn's flares.", "Zinc supports nutrition; it does not replace anti-inflammatory therapy."),
            ("More zinc is always better.", "Excess can cause nausea and copper deficiency."),
            ("Plant foods never provide zinc.", "They can, but absorption is often lower than from meat."),
        ],
        "questions": [
            "Should we check zinc after prolonged diarrhea or resection?",
            "How should I time zinc apart from iron pills if both are prescribed?",
            "What food-first plan raises zinc without upsetting my gut?",
        ],
        "related": [
            ("/blog/micronutrients-ibd-deficiencies", "micronutrient overview"),
            ("/blog/chicken-protein-ibd", "chicken protein"),
            ("/blog/eggs-ibd-nutrition", "eggs and IBD"),
        ],
    },
    {
        "slug": "magnesium-ibd",
        "name": "Magnesium",
        "title": "Magnesium and IBD: Cramps, Diarrhea Losses, and Repletion Tips",
        "description": "Magnesium with Crohn's or colitis: stool losses, muscle cramps, food sources, laxative forms to avoid, and clinic questions. Education only.",
        "category": "Nutrition · August 2026",
        "date_display": "August 27, 2026",
        "date_iso": "2026-08-27T12:00:00Z",
        "asset_dir": "magnesium-ibd",
        "resource_category": "nutrition",
        "tags": ["magnesium", "cramps", "electrolytes", "diarrhea", "micronutrients", "Crohn's", "colitis", "nutrition"],
        "share": "Magnesium and IBD: losses, foods, and supplement cautions. Education only.",
        "primary_kw": "magnesium Crohn's disease",
        "secondary_kw": "magnesium deficiency colitis",
        "intro": (
            "Magnesium supports muscles, nerves, and energy metabolism. IBD patients often search it for cramps, "
            "fatigue, or after learning diarrhea wastes magnesium."
        ),
        "roles": [
            "Helps normal muscle and nerve function",
            "Supports enzyme reactions for energy production",
            "Contributes to bone mineral structure with calcium and vitamin D",
        ],
        "why_ibd": [
            "Diarrhea and high-output stomas increase magnesium losses",
            "Malabsorption after small bowel disease or surgery",
            "Some medications and low intake from restricted diets",
            "Refeeding or IV fluids contexts in hospital care may need monitored repletion",
        ],
        "risk_note": (
            "Low magnesium can be serious. Self-supplementing with strong laxative forms (oxide in large doses, citrate meant as prep) "
            "can worsen diarrhea. Kidney disease changes what is safe."
        ),
        "food_intro": "Food sources are often gentler than high-dose laxative magnesium salts when the gut is sensitive.",
        "foods_flare": [
            "Smooth peanut or almond butter in small amounts if tolerated",
            "Fortified cereals that fit your residue plan",
            "Banana and potato for combined potassium and some magnesium support",
            "Soft fish or poultry as part of balanced plates (not the richest sources, but easier textures)",
        ],
        "foods_remission": [
            "Nuts, seeds, and legumes if fiber is cleared",
            "Leafy greens cooked soft",
            "Whole grains when you have moved past low-residue phases",
            "Dark chocolate in modest amounts if tolerated",
        ],
        "supplement_note": (
            "Forms differ: some are more laxative, some better absorbed with fewer stools for certain patients. "
            "Never start high-dose magnesium for heart rhythm symptoms without urgent medical evaluation. "
            "People with reduced kidney function need clinician dosing only."
        ),
        "labs": [
            "Serum magnesium may be ordered with electrolytes during flares or cramps",
            "Low potassium and low magnesium often travel together",
            "Repeat after repletion and when diarrhea slows",
        ],
        "myths": [
            ("Any magnesium powder labeled calm is safe in IBD.", "Many are laxative and can worsen urgency."),
            ("Normal sodium means electrolytes are fine.", "Magnesium and potassium need their own checks when indicated."),
            ("Food cannot help magnesium.", "Food helps many people; severe losses still need medical repletion."),
        ],
        "questions": [
            "Should we check magnesium with my electrolyte panel?",
            "Which supplement form is least likely to worsen diarrhea for me?",
            "Do my kidney labs limit magnesium supplements?",
        ],
        "related": [
            ("/blog/electrolytes-flare-ibd", "electrolytes during flares"),
            ("/blog/potassium-ibd", "potassium and IBD"),
            ("/blog/dehydration-ibd-warning-signs", "dehydration warning signs"),
        ],
    },
    {
        "slug": "potassium-ibd",
        "name": "Potassium",
        "title": "Potassium and IBD: Diarrhea Losses, Foods, and Safety Limits",
        "description": "Potassium with Crohn's or colitis: stool and urine losses, banana and potato sources, medication cautions, and clinic questions. Education only.",
        "category": "Nutrition · August 2026",
        "date_display": "August 27, 2026",
        "date_iso": "2026-08-27T14:00:00Z",
        "asset_dir": "potassium-ibd",
        "resource_category": "nutrition",
        "tags": ["potassium", "electrolytes", "banana", "potato", "diarrhea", "micronutrients", "Crohn's", "colitis", "nutrition"],
        "share": "Potassium and IBD: losses, foods, and safety. Education only.",
        "primary_kw": "potassium Crohn's diarrhea",
        "secondary_kw": "low potassium ulcerative colitis",
        "intro": (
            "Potassium is a key electrolyte for heart rhythm and muscle function. "
            "Diarrhea, vomiting, and some medicines can drop levels, which is why flares and potassium searches overlap."
        ),
        "roles": [
            "Helps maintain normal heart rhythm and muscle contraction",
            "Supports fluid and electrolyte balance with sodium",
            "Participates in nerve signaling",
        ],
        "why_ibd": [
            "Diarrhea increases fecal potassium losses",
            "Poor intake during nausea or liquid diets",
            "Some diuretics or other medicines affect potassium (review your full list)",
            "Rehydration with water only, without electrolytes, may not restore losses",
        ],
        "risk_note": (
            "Both low and high potassium can be dangerous. Kidney disease, ACE inhibitors, ARBs, and potassium-sparing drugs "
            "change what is safe. Do not mega-dose potassium supplements without labs and a clinician."
        ),
        "food_intro": "Many gentle IBD foods are naturally helpful potassium sources.",
        "foods_flare": [
            "Ripe banana",
            "Peeled mashed white potato or sweet potato",
            "Melon if tolerated",
            "Oral rehydration solutions your clinic recommends (not random sports drinks only)",
        ],
        "foods_remission": [
            "Yogurt or milk alternatives if tolerated",
            "Cooked tomatoes or tomato products if acidity is okay",
            "Beans and avocado when fiber and fat allow",
            "Orange fruit or diluted juice if citrus sits well",
        ],
        "supplement_note": (
            "Over-the-counter potassium pills are not harmless candy. Prescription repletion and monitored IV therapy belong in clinical care "
            "when levels are significantly low. Salt substitutes labeled potassium chloride can be risky for some patients."
        ),
        "labs": [
            "Basic metabolic panel or electrolytes during flares, dehydration, or new weakness",
            "Recheck after vomiting, high-output stoma days, or medication changes",
            "Interpret with kidney function and full medication list",
        ],
        "myths": [
            ("Bananas alone fix any potassium problem.", "Helpful food, not a substitute for labs when symptoms are severe."),
            ("All sports drinks are ideal rehydration.", "Formulas differ; ask what your team prefers."),
            ("High potassium foods are banned if I have IBD.", "Many patients need potassium; restrictions are individualized."),
        ],
        "questions": [
            "Should we check potassium during this flare?",
            "Which fluids and foods best replace my losses?",
            "Do any of my medicines raise or lower potassium too much?",
        ],
        "related": [
            ("/blog/banana-ibd-crohns-colitis", "bananas and IBD"),
            ("/blog/potato-ibd-white", "white potatoes"),
            ("/blog/electrolytes-flare-ibd", "electrolytes and flares"),
        ],
    },
    {
        "slug": "vitamin-c-ibd",
        "name": "Vitamin C",
        "title": "Vitamin C and IBD: Immunity Myths, Food Sources, and Acidity Tips",
        "description": "Vitamin C with Crohn's or colitis: food sources, citrus acidity, iron absorption helper, mega-dose myths, and clinic questions. Education only.",
        "category": "Nutrition · August 2026",
        "date_display": "August 27, 2026",
        "date_iso": "2026-08-27T16:00:00Z",
        "asset_dir": "vitamin-c-ibd",
        "resource_category": "nutrition",
        "tags": ["vitamin C", "ascorbic acid", "citrus", "iron absorption", "micronutrients", "Crohn's", "colitis", "nutrition"],
        "share": "Vitamin C and IBD: foods, acidity, and myths. Education only.",
        "primary_kw": "vitamin C Crohn's disease",
        "secondary_kw": "vitamin C ulcerative colitis",
        "intro": (
            "Vitamin C (ascorbic acid) supports collagen, immune cell function, and non-heme iron absorption. "
            "People with IBD often worry about citrus burning symptoms while still needing vitamin C from somewhere."
        ),
        "roles": [
            "Helps collagen formation for tissues and wound healing support",
            "Acts as an antioxidant in normal physiology",
            "Improves absorption of plant (non-heme) iron when eaten together",
        ],
        "why_ibd": [
            "Avoiding acidic fruits and juices can lower intake",
            "Limited menus during flares reduce produce variety",
            "Smoking (if present) raises vitamin C needs",
            "Iron therapy plans sometimes intentionally pair vitamin C with iron under guidance",
        ],
        "risk_note": (
            "Mega-dose vitamin C is not an IBD flare treatment and can cause GI upset or kidney stone risk in susceptible people. "
            "Food-range intake is usually the goal unless your clinician recommends more."
        ),
        "food_intro": "You can meet vitamin C needs without forcing large glasses of orange juice.",
        "foods_flare": [
            "Soft strawberries or melon if tolerated",
            "Peeled cooked potato (surprising but real vitamin C source when not overcooked for hours)",
            "Fortified juices diluted with water if acidity is an issue",
            "Smoothies with tolerated fruit and no large seed loads",
        ],
        "foods_remission": [
            "Oranges, kiwi, peppers, broccoli if those textures sit well",
            "Tomato products if acidity is okay",
            "Berries with yogurt or eggs",
            "Fresh fruit over candy-like gummies marketed as immunity shields",
        ],
        "supplement_note": (
            "If citrus triggers symptoms, a clinician may suggest a non-acidic vitamin C source or a modest supplement. "
            "Chewables and fizzy high-dose packets can irritate some guts. Timing with iron pills should follow your iron protocol."
        ),
        "labs": [
            "Vitamin C blood tests are not routine for every IBD visit",
            "Focus on dietary history, wound healing, and iron therapy plans",
            "Discuss kidney stone history before high-dose ascorbic acid",
        ],
        "myths": [
            ("Vitamin C cures colds and Crohn's flares.", "It supports nutrition; it does not replace IBD medicines."),
            ("If citrus burns, I cannot get vitamin C.", "Other fruits, potato, and guided supplements exist."),
            ("IV vitamin C is required for colitis.", "Not a standard IBD therapy; beware clinics selling unproven infusions."),
        ],
        "questions": [
            "How should I get vitamin C if tomatoes and citrus bother me?",
            "Should I take vitamin C with my iron pills?",
            "Is a multivitamin enough for my needs?",
        ],
        "related": [
            ("/blog/oranges-citrus-ibd", "oranges and citrus"),
            ("/blog/strawberries-ibd", "strawberries"),
            ("/guides/iron-deficiency-nutrition-ibd", "iron deficiency nutrition"),
        ],
    },
    {
        "slug": "folate-ibd",
        "name": "Folate",
        "title": "Folate and IBD: Methotrexate, Pregnancy Planning, and Food Sources",
        "description": "Folate (folic acid) with Crohn's or colitis: methotrexate, pregnancy, food sources, labs, and dietitian questions. Education only.",
        "category": "Nutrition · August 2026",
        "date_display": "August 27, 2026",
        "date_iso": "2026-08-27T18:00:00Z",
        "asset_dir": "folate-ibd",
        "resource_category": "nutrition",
        "tags": ["folate", "folic acid", "methotrexate", "pregnancy", "B vitamins", "micronutrients", "Crohn's", "colitis", "nutrition"],
        "share": "Folate and IBD: methotrexate, pregnancy, and foods. Education only.",
        "primary_kw": "folate Crohn's methotrexate",
        "secondary_kw": "folic acid ulcerative colitis",
        "intro": (
            "Folate (vitamin B9) helps make DNA and blood cells. In IBD care it comes up with methotrexate, sulfasalazine, "
            "pregnancy planning, and limited green vegetable intake."
        ),
        "roles": [
            "Supports red blood cell production with B12 and iron",
            "Critical for early pregnancy neural tube development",
            "Participates in methylation pathways used throughout the body",
        ],
        "why_ibd": [
            "Methotrexate interferes with folate pathways; prescribed folic acid is common",
            "Sulfasalazine can affect folate handling",
            "Low intake of leafy greens and legumes during flares",
            "Increased needs with pregnancy or planning pregnancy",
        ],
        "risk_note": (
            "Do not stop methotrexate folic acid schedules on your own. "
            "Also do not assume folate fixes B12 deficiency; both can cause anemia and need proper labs."
        ),
        "food_intro": "Food folate plus fortified grains help; medicine-related needs often still require prescribed folic acid.",
        "foods_flare": [
            "Enriched white bread, pasta, or cereals if they fit your plan",
            "Cooked spinach pureed into eggs or soup if greens are allowed",
            "Orange fruit or diluted juice if tolerated",
            "Liver is rich but not a flare staple for most people; discuss if relevant",
        ],
        "foods_remission": [
            "Cooked leafy greens, asparagus, Brussels sprouts if tolerated",
            "Beans and lentils when fiber is okay",
            "Avocado in measured portions",
            "Fortified grains as easy daily contributors",
        ],
        "supplement_note": (
            "Folic acid dosing with methotrexate is prescription-directed (often weekly timing that avoids the methotrexate day). "
            "Pregnancy dosing may differ. High-dose folate without a plan can mask B12 deficiency on some blood tests, so teams check both."
        ),
        "labs": [
            "Folate level when anemia, methotrexate use, or poor intake is present",
            "Always interpret with B12, iron studies, and CBC",
            "Pregnancy planning labs and prenatal vitamin review",
        ],
        "myths": [
            ("I take methotrexate so I should avoid all folate foods.", "Usually false; prescribed folic acid and food are part of safe plans."),
            ("Folate and B12 are interchangeable.", "They are different vitamins with different absorption issues in IBD."),
            ("A green juice cleanses folate status.", "Food and prescribed supplements beat detox marketing."),
        ],
        "questions": [
            "What folic acid schedule should I use with methotrexate?",
            "Do I need extra folate before pregnancy?",
            "Should we recheck folate and B12 with my next CBC?",
        ],
        "related": [
            ("/blog/iron-b12-vitamin-d-ibd", "iron, B12, and vitamin D"),
            ("/blog/ibd-pregnancy-planning", "pregnancy planning"),
            ("/blog/spinach-leafy-greens-ibd", "spinach and greens"),
        ],
    },
    {
        "slug": "vitamin-a-ibd",
        "name": "Vitamin A",
        "title": "Vitamin A and IBD: Vision, Night Blindness Concerns, and Food Sources",
        "description": "Vitamin A with Crohn's or colitis: fat malabsorption, beta-carotene foods, supplement toxicity cautions, and clinic questions. Education only.",
        "category": "Nutrition · August 2026",
        "date_display": "August 28, 2026",
        "date_iso": "2026-08-28T12:00:00Z",
        "asset_dir": "vitamin-a-ibd",
        "resource_category": "nutrition",
        "tags": ["vitamin A", "beta-carotene", "vision", "fat malabsorption", "micronutrients", "Crohn's", "colitis", "nutrition"],
        "share": "Vitamin A and IBD: foods and toxicity cautions. Education only.",
        "primary_kw": "vitamin A Crohn's disease",
        "secondary_kw": "vitamin A deficiency colitis",
        "intro": (
            "Vitamin A supports vision, immune barriers, and epithelial health. "
            "It is fat-soluble, so fat malabsorption, short bowel, or very low-fat diets can raise deficiency risk, while mega-dose supplements raise toxicity risk."
        ),
        "roles": [
            "Supports night vision and corneal health",
            "Helps maintain mucosal barriers",
            "Participates in immune cell function",
        ],
        "why_ibd": [
            "Fat malabsorption after ileal disease, resection, or cholestyramine use",
            "Very restricted diets lacking orange vegetables and fortified foods",
            "Zinc deficiency can impair vitamin A use (they interact)",
            "Hospital or exclusive liquid diets without complete micronutrient coverage in rare cases",
        ],
        "risk_note": (
            "Preformed vitamin A (retinol) in high supplemental doses can be toxic and is especially concerning in pregnancy. "
            "Beta-carotene from food is a safer everyday route for many people, but still discuss prenatal needs with obstetrics and GI."
        ),
        "food_intro": "Beta-carotene foods (orange and dark green produce) convert to vitamin A as needed for many patients.",
        "foods_flare": [
            "Peeled cooked carrots or carrot puree",
            "Mashed sweet potato",
            "Fortified milk alternatives if used",
            "Eggs (contain preformed vitamin A) when tolerated",
        ],
        "foods_remission": [
            "Cooked spinach and other leafy greens",
            "Cantaloupe if tolerated",
            "Tomato products",
            "Fortified cereals",
        ],
        "supplement_note": (
            "Do not stack multiple high-vitamin-A supplements, cod liver oil mega-doses, and fortified products without adding up retinol activity equivalents. "
            "Deficiency treatment doses are medical, not DIY."
        ),
        "labs": [
            "Vitamin A testing is not routine for every patient; ordered when risk or symptoms suggest need",
            "Review fat-soluble vitamins (A, D, E, K) together after major resections when indicated",
            "Night vision changes deserve a clinic call, not only a supplement aisle visit",
        ],
        "myths": [
            ("I can take as much vitamin A as I want because it is natural.", "Retinol toxicity is real."),
            ("Carrots alone prove my vitamin A status is perfect.", "Intake helps; malabsorption still needs clinical judgment."),
            ("Vitamin A cures leaky gut in IBD.", "Marketing phrase, not a substitute for IBD therapy."),
        ],
        "questions": [
            "Do my surgery history and fat absorption suggest fat-soluble vitamin monitoring?",
            "Is my multivitamin already high in retinol?",
            "What food plan raises vitamin A safely in pregnancy planning?",
        ],
        "related": [
            ("/blog/carrots-ibd", "carrots"),
            ("/blog/sweet-potato-ibd", "sweet potatoes"),
            ("/blog/micronutrients-ibd-deficiencies", "micronutrient overview"),
        ],
    },
    {
        "slug": "omega-3-ibd",
        "name": "Omega-3 fats",
        "title": "Omega-3 and IBD: Fish, Supplements, and What Evidence Suggests",
        "description": "Omega-3 fats with Crohn's or colitis: fish sources, fish oil evidence limits, flare fat tolerance, and clinic questions. Education only.",
        "category": "Nutrition · August 2026",
        "date_display": "August 28, 2026",
        "date_iso": "2026-08-28T14:00:00Z",
        "asset_dir": "omega3-ibd",
        "resource_category": "nutrition",
        "tags": ["omega-3", "fish oil", "EPA", "DHA", "salmon", "heart", "micronutrients", "Crohn's", "colitis", "nutrition"],
        "share": "Omega-3 and IBD: fish, oils, and evidence limits. Education only.",
        "primary_kw": "omega-3 Crohn's disease",
        "secondary_kw": "fish oil ulcerative colitis",
        "intro": (
            "Omega-3 fatty acids (EPA and DHA from fish, ALA from some plants) are popular in anti-inflammatory diet searches. "
            "They support heart and general nutrition goals, but fish oil is not a proven stand-alone Crohn's or colitis therapy for everyone."
        ),
        "roles": [
            "Structural fats in cell membranes",
            "Precursors for signaling molecules involved in inflammation resolution pathways",
            "Support heart and triglyceride health in broader medical nutrition",
        ],
        "why_ibd": [
            "Patients seek anti-inflammatory eating patterns (Mediterranean-style plates often include fish)",
            "Low fish intake is common on limited menus",
            "Fat tolerance varies; oily fish or concentrated oils can worsen urgency for some during flares",
            "Supplement quality and dose vary widely on store shelves",
        ],
        "risk_note": (
            "Evidence that fish oil induces IBD remission is mixed and not a reason to skip prescribed medicines. "
            "High-dose oils can affect bleeding risk with some medicines and may cause burps or looser stools."
        ),
        "food_intro": "Food-first omega-3 from fish is usually preferred over mystery megadose capsules when fish is tolerated.",
        "foods_flare": [
            "Small portions of tender white fish if oily fish feels too heavy",
            "Smooth nut butters providing ALA if tolerated (conversion to EPA/DHA is limited)",
            "Hold concentrated fish oil during bad fat-intolerance weeks unless your clinician says otherwise",
            "Focus on overall calories and protein first when underweight in a flare",
        ],
        "foods_remission": [
            "Salmon, sardines, trout, or other fatty fish a few times per week if desired and tolerated",
            "Mediterranean-style plates with fish, olive oil, and produce you tolerate",
            "Walnuts or ground flax if seeds/nuts are cleared (ALA source)",
            "Discuss algae-based DHA if you avoid fish",
        ],
        "supplement_note": (
            "If a clinician recommends an omega-3 supplement, ask about EPA/DHA dose, brand quality, and timing with anticoagulants or surgery. "
            "More milligrams is not automatically more remission."
        ),
        "labs": [
            "Routine omega-3 blood indexes are not required for most IBD visits",
            "Triglycerides and heart risk panels may motivate fish intake for other reasons",
            "Bring supplement bottles to visits so doses are visible",
        ],
        "myths": [
            ("Fish oil replaces biologics.", "False. Stay on prescribed IBD therapy."),
            ("Plant omega-3 fully equals fish EPA/DHA for everyone.", "Conversion is limited; needs vary."),
            ("Any supermarket oil labeled omega-3 is proven for colitis.", "Marketing outruns evidence for many products."),
        ],
        "questions": [
            "Does fish oil make sense for me given my medicines and stool pattern?",
            "How can I add fish without triggering urgency?",
            "Should I follow a Mediterranean-style pattern with an IBD dietitian?",
        ],
        "related": [
            ("/blog/anti-inflammatory-diet-ibd", "anti-inflammatory diet"),
            ("/blog/mediterranean-diet-autoimmune", "Mediterranean-style eating"),
            ("/blog/chicken-protein-ibd", "poultry protein alternatives"),
        ],
    },
]


def build_posts() -> list[dict]:
    posts = []
    for n in NUTRIENTS:
        posts.append(
            {
                "slug": n["slug"],
                "title": n["title"],
                "description": n["description"],
                "category": n["category"],
                "date_display": n["date_display"],
                "date_iso": n["date_iso"],
                "asset_dir": n["asset_dir"],
                "resource_category": n["resource_category"],
                "tags": n["tags"],
                "share": n["share"],
                "images": [f'{n["asset_dir"]}_1.jpg'],
                "alts": [f'{n["name"]} nutrition education for IBD'],
                "body": nutrient_body(n),
            }
        )
    return posts


def download_image(url: str, dest: Path) -> bool:
    import ssl
    import urllib.request

    for ctx in (ssl.create_default_context(), ssl._create_unverified_context()):
        try:
            with urllib.request.urlopen(url, context=ctx, timeout=45) as resp:
                data = resp.read()
            if len(data) > 5000 and data[:2] == b"\xff\xd8":
                dest.write_bytes(data)
                return True
        except Exception:
            continue
    return False


def ensure_image(post: dict) -> None:
    asset = BLOGS / "assets" / post["asset_dir"]
    asset.mkdir(parents=True, exist_ok=True)
    dest = asset / post["images"][0]
    if dest.exists() and dest.stat().st_size >= 5000:
        return
    url = IMAGE_URLS.get(post["asset_dir"])
    if url and download_image(url, dest):
        print("downloaded", dest.name)
        return
    if FALLBACK_IMAGE.exists():
        shutil.copy(FALLBACK_IMAGE, dest)
        print("fallback image for", dest.name)
    else:
        print("WARN: no image for", dest)


def write_blogs(posts: list[dict]) -> list[str]:
    slugs = []
    for post in posts:
        ensure_image(post)
        (BLOGS / f"{post['slug']}.html").write_text(render_post(post), encoding="utf-8")
        slugs.append(post["slug"])
        print("wrote", post["slug"] + ".html")
    return slugs


def patch_vercel(slugs: list[str]) -> None:
    text = VERCEL.read_text(encoding="utf-8")
    inserts = []
    for slug in slugs:
        if f'"/blog/{slug}"' in text:
            continue
        inserts.append(
            f'    {{\n      "source": "/blog/{slug}",\n'
            f'      "destination": "/blogs/{slug}.html"\n    }}'
        )
    if not inserts:
        return
    text = text.replace('"rewrites": [\n', '"rewrites": [\n' + ",\n".join(inserts) + ",\n")
    VERCEL.write_text(text, encoding="utf-8")
    print("patched vercel.json (+", len(inserts), "rewrites)")


def patch_sitemap(slugs: list[str]) -> None:
    today = date.today().isoformat()
    text = SITEMAP.read_text(encoding="utf-8")
    marker = "<!-- wave3-food-nutrition-blogs -->"
    if marker in text:
        text = re.sub(
            rf"\n  {re.escape(marker)}.*?(?=\n  <!-- |\n</urlset>)",
            "",
            text,
            flags=re.DOTALL,
        )
    entries = [
        f"  <url>\n    <loc>{SITE}/blog/{slug}</loc>\n    <lastmod>{today}</lastmod>\n"
        f"    <changefreq>monthly</changefreq>\n    <priority>0.85</priority>\n  </url>"
        for slug in slugs
    ]
    block = f"  {marker}\n" + "\n".join(entries)
    for anchor in (
        "  <!-- wave2-food-nutrition-blogs -->",
        "  <!-- wave1-food-nutrition-blogs -->",
        "  <!-- seo-wellness-blogs -->",
        "  <!-- tier3-seo -->",
    ):
        if anchor in text:
            text = text.replace(anchor, block + "\n" + anchor)
            break
    else:
        text = text.replace("</urlset>", block + "\n</urlset>")
    SITEMAP.write_text(text, encoding="utf-8")
    print("patched sitemap.xml (+", len(slugs), "urls)")


def write_data(posts: list[dict]) -> None:
    DATA.write_text(
        json.dumps({"wave": 3, "theme": "micronutrients", "posts": posts}, ensure_ascii=False, indent=2)
        + "\n",
        encoding="utf-8",
    )
    print("wrote", DATA.relative_to(ROOT))


def main() -> None:
    posts = build_posts()
    write_data(posts)
    slugs = write_blogs(posts)
    patch_vercel(slugs)
    patch_sitemap(slugs)
    print("Done.", len(slugs), "Wave 3 micronutrient posts.")


if __name__ == "__main__":
    main()
