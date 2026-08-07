#!/usr/bin/env python3
"""Append wave-1 nutrition SEO guides to seo-landing-pages.json."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "data" / "seo-landing-pages.json"

NEW_PAGES = [
    {
        "slug": "anti-inflammatory-diet-ibd",
        "category": "nutrition",
        "keywords": [
            "anti-inflammatory diet IBD",
            "Mediterranean diet Crohn's",
            "anti-inflammatory foods colitis",
            "IBD inflammation diet",
        ],
        "title": "Anti-Inflammatory Diet for IBD | Realistic Guide | IBDPal",
        "description": "What anti-inflammatory eating means for Crohn's and colitis: Mediterranean-style patterns, marketing claims vs evidence, and when to see a dietitian. Education only.",
        "h1": "Anti-inflammatory diet for IBD: a realistic guide",
        "intro": "Anti-inflammatory diet is a popular search phrase. For IBD, the useful idea is usually a Mediterranean-style pattern rich in plants, olive oil, fish, and fiber when tolerated, not a miracle cleanse. Diet supports care; it does not replace medication for inflammation.",
        "sections": [
            {
                "heading": "What the phrase usually means",
                "paragraphs": [
                    "Many clinicians discuss Mediterranean-style eating: vegetables, fruits, legumes when tolerated, whole grains in remission, olive oil, nuts if tolerated, and fish.",
                    "Marketing detox teas and extreme elimination kits are not the same as evidence-informed nutrition therapy.",
                ],
            },
            {
                "heading": "Flare vs remission",
                "paragraphs": [
                    "During active symptoms, softer textures and temporary fiber reductions may be easier. In quieter weeks, variety and nutrient density matter more.",
                    "Track personal triggers instead of copying someone else's forever-ban list.",
                ],
            },
            {
                "heading": "How to use IBDPal beside diet advice",
                "paragraphs": [
                    "Log meals and symptoms for two to four weeks before major changes.",
                    "Bring the log to your gastroenterologist or IBD dietitian.",
                ],
            },
        ],
        "tips": [
            "Prefer food patterns over supplement stacks sold as anti-inflammatory cures",
            "Ask about vitamin D, iron, and protein needs",
            "Reintroduce foods with a plan, not fear alone",
        ],
        "related": [
            {"label": "Anti-inflammatory diet article", "url": "/blog/anti-inflammatory-diet-ibd"},
            {"label": "What should I eat with Crohn's or colitis?", "url": "/guides/what-should-i-eat-crohns-colitis"},
            {"label": "Elimination diet timing", "url": "/guides/elimination-diet-when-to-stop-ibd"},
            {"label": "Nutrition hub", "url": "/ibd-nutrition"},
            {"label": "Research sources", "url": "/research"},
        ],
        "faq": [
            {
                "q": "Can an anti-inflammatory diet put Crohn's in remission alone?",
                "a": "No. Nutrition can support comfort and nutrient status. Inflammatory control usually requires medical therapy guided by your IBD team.",
            },
            {
                "q": "Is Mediterranean eating safe in a flare?",
                "a": "Parts of it may need texture changes during active symptoms. Ask your clinician or dietitian how to adapt the pattern for you.",
            },
        ],
    },
    {
        "slug": "iron-deficiency-nutrition-ibd",
        "category": "nutrition",
        "keywords": [
            "iron deficiency IBD diet",
            "anemia Crohn's food",
            "iron-rich foods colitis",
            "IBD iron absorption",
        ],
        "title": "Iron Deficiency Nutrition in IBD | Food and Clinic Guide",
        "description": "Iron-rich eating with Crohn's or colitis, why oral iron may fail during inflammation, and questions for IV vs oral therapy. Education only.",
        "h1": "Iron deficiency nutrition in IBD",
        "intro": "Iron deficiency and anemia are common in IBD because of blood loss, inflammation, and absorption limits. Food helps, but labs and therapy decisions belong with your care team.",
        "sections": [
            {
                "heading": "Food patterns that support iron",
                "paragraphs": [
                    "Lean meats, poultry, fish, eggs, legumes if tolerated, and iron-fortified foods are common building blocks.",
                    "Vitamin C-containing foods with plant iron sources may help absorption for some people.",
                ],
            },
            {
                "heading": "Why food is not always enough",
                "paragraphs": [
                    "Active inflammation can lock iron away. Small-bowel disease or surgery can limit absorption. Oral iron may worsen stools for some patients.",
                    "IV iron is sometimes appropriate; that is a clinical decision.",
                ],
            },
            {
                "heading": "Track and report",
                "paragraphs": [
                    "Note fatigue, shortness of breath, dizziness, and stool blood.",
                    "Bring hemoglobin and ferritin questions to clinic rather than guessing supplement doses.",
                ],
            },
        ],
        "tips": [
            "Do not start high-dose iron without clinician advice",
            "Pair reading with anemia article and visit prep",
            "Ask whether oral or IV iron fits your disease activity",
        ],
        "related": [
            {"label": "Anemia and iron deficiency article", "url": "/blog/anemia-iron-deficiency-ibd"},
            {"label": "Micronutrient deficiencies", "url": "/blog/micronutrients-ibd-deficiencies"},
            {"label": "Protein during flares", "url": "/guides/protein-healing-ibd-flare"},
            {"label": "Nutrition hub", "url": "/ibd-nutrition"},
        ],
        "faq": [
            {
                "q": "Which iron-rich foods are gentlest in a flare?",
                "a": "Tolerance varies. Soft proteins and fortified foods are often easier than high-fiber plant sources during active symptoms. Ask your dietitian.",
            },
            {
                "q": "Can I fix IBD anemia with spinach alone?",
                "a": "Usually not when bleeding or inflammation is ongoing. Food supports recovery; treating IBD activity and using prescribed iron therapy matter more.",
            },
        ],
    },
    {
        "slug": "vitamin-d-bone-nutrition-ibd",
        "category": "nutrition",
        "keywords": [
            "vitamin D IBD",
            "bone health Crohn's",
            "calcium colitis diet",
            "osteoporosis nutrition IBD",
        ],
        "title": "Vitamin D and Bone Nutrition in IBD | Patient Guide",
        "description": "Vitamin D, calcium, and bone-friendly nutrition for Crohn's and colitis, plus screening questions after steroids. Education only.",
        "h1": "Vitamin D and bone nutrition in IBD",
        "intro": "Low vitamin D is common in IBD. Bone health also depends on calcium intake, weight-bearing activity when safe, inflammation control, and steroid history.",
        "sections": [
            {
                "heading": "Why vitamin D matters",
                "paragraphs": [
                    "Vitamin D supports bone mineralization and is often repleted when labs are low.",
                    "Sunlight, fortified foods, and supplements may all play roles; dosing should follow labs and clinician advice.",
                ],
            },
            {
                "heading": "Calcium food sources",
                "paragraphs": [
                    "Dairy if tolerated, fortified alternatives, canned fish with bones, and tofu set with calcium are frequent options.",
                    "If dairy triggers symptoms, plan alternatives with a dietitian rather than dropping calcium entirely.",
                ],
            },
            {
                "heading": "Steroids and screening",
                "paragraphs": [
                    "Repeated systemic steroids raise bone-loss risk.",
                    "Ask about DEXA timing and steroid-sparing plans.",
                ],
            },
        ],
        "tips": [
            "Recheck vitamin D rather than guessing high doses",
            "Pair with bone health article",
            "Mention fracture history and menopause status at visits",
        ],
        "related": [
            {"label": "Osteoporosis and bone health article", "url": "/blog/osteoporosis-bone-health-ibd"},
            {"label": "Micronutrients article", "url": "/blog/micronutrients-ibd-deficiencies"},
            {"label": "Steroid taper expectations", "url": "/blog/steroid-taper-what-to-expect-ibd"},
            {"label": "Nutrition hub", "url": "/ibd-nutrition"},
            {"label": "Research sources", "url": "/research"},
        ],
        "faq": [
            {
                "q": "What vitamin D level should I target?",
                "a": "Targets vary by lab and clinician. Ask for your number and the plan to recheck after repletion.",
            },
            {
                "q": "Do I need calcium pills if I eat dairy?",
                "a": "Not always. Total intake from food and supplements matters. Your team personalizes this, especially with kidney stone history.",
            },
        ],
    },
    {
        "slug": "protein-healing-ibd-flare",
        "category": "nutrition",
        "keywords": [
            "protein IBD flare",
            "protein foods Crohn's flare",
            "healing protein colitis",
            "IBD muscle loss nutrition",
        ],
        "title": "Protein Intake During an IBD Flare | Healing Guide",
        "description": "Why protein matters during Crohn's or colitis flares, gentler protein ideas, and when to ask about oral nutrition supplements. Education only.",
        "h1": "Protein for healing during an IBD flare",
        "intro": "Inflammation and poor intake can speed muscle and nutrient loss. Soft, tolerated proteins help many people meet needs while medications calm disease. This is supportive nutrition, not a cure.",
        "sections": [
            {
                "heading": "Why protein rises in importance",
                "paragraphs": [
                    "Tissue repair, immune function, and preventing excess muscle loss all need adequate protein.",
                    "Needs may be higher during active disease; your clinician or dietitian sets targets.",
                ],
            },
            {
                "heading": "Often easier options",
                "paragraphs": [
                    "Eggs, yogurt if tolerated, tofu, fish, ground poultry, smoothies with protein powder approved by your team, and oral nutrition drinks when food volume is low.",
                    "Large steaks and high-fiber beans may be harder mid-flare.",
                ],
            },
            {
                "heading": "When to escalate",
                "paragraphs": [
                    "Rapid weight loss, inability to keep food down, or known strictures need prompt clinical contact.",
                    "Exclusive enteral nutrition is a supervised therapy, not a DIY protocol.",
                ],
            },
        ],
        "tips": [
            "Spread protein across smaller meals",
            "Log intake for clinic",
            "Ask before starting unfamiliar supplements",
        ],
        "related": [
            {"label": "High-protein meal ideas in remission", "url": "/blog/protein-meal-plan-ibd-remission"},
            {"label": "Foods during a Crohn's flare", "url": "/guides/foods-to-eat-crohns-flare"},
            {"label": "Enteral nutrition article", "url": "/blog/enteral-nutrition-ibd"},
            {"label": "Iron nutrition guide", "url": "/guides/iron-deficiency-nutrition-ibd"},
            {"label": "Nutrition hub", "url": "/ibd-nutrition"},
        ],
        "faq": [
            {
                "q": "How many grams of protein do I need in a flare?",
                "a": "It depends on weight, disease activity, and kidney function. Ask your IBD dietitian for a personal range.",
            },
            {
                "q": "Are protein shakes safe with IBD?",
                "a": "Some are well tolerated; others contain sugar alcohols or fibers that worsen symptoms. Check labels with your clinician.",
            },
        ],
    },
    {
        "slug": "elimination-diet-when-to-stop-ibd",
        "category": "nutrition",
        "keywords": [
            "elimination diet IBD",
            "when to stop elimination diet",
            "IBD food reintroduction",
            "Crohn's elimination diet risks",
        ],
        "title": "Elimination Diets in IBD: When to Stop and Reintroduce",
        "description": "How long IBD elimination trials should last, malnutrition risks, reintroduction steps, and dietitian roles. Education only, not a protocol.",
        "h1": "Elimination diets in IBD: when to stop",
        "intro": "Short, supervised elimination trials can identify triggers. Open-ended restriction without reintroduction raises malnutrition and fear-of-food risk. Know when to stop narrowing and start rebuilding.",
        "sections": [
            {
                "heading": "A safer mental model",
                "paragraphs": [
                    "Define the question (for example, dairy or a FODMAP group), the time box, and the reintroduction plan before you start.",
                    "Celiac screening should happen before long gluten-free trials.",
                ],
            },
            {
                "heading": "Red flags to stop the trial early",
                "paragraphs": [
                    "Unintentional weight loss, fear of almost all foods, nutrient gaps, or worsening pain and obstruction symptoms.",
                    "Call your team rather than cutting more food groups alone.",
                ],
            },
            {
                "heading": "Reintroduction",
                "paragraphs": [
                    "Add one item at a time, log symptoms for a few days, and keep foods that stay quiet.",
                    "Work with an IBD dietitian for structured plans such as guided FODMAP work.",
                ],
            },
        ],
        "tips": [
            "Time-box trials in weeks, not forever",
            "Protect protein and calorie intake while testing",
            "Use IBDPal logs so reintroduction has data",
        ],
        "related": [
            {"label": "Celiac screening with IBD", "url": "/blog/celiac-ibd-screening"},
            {"label": "Gluten and wheat article", "url": "/blog/gluten-wheat-ibd"},
            {"label": "FODMAP article", "url": "/blog/fodmap-diet-crohns-colitis"},
            {"label": "Anti-inflammatory diet guide", "url": "/guides/anti-inflammatory-diet-ibd"},
            {"label": "Nutrition hub", "url": "/ibd-nutrition"},
        ],
        "faq": [
            {
                "q": "How long should an IBD elimination diet last?",
                "a": "Many supervised trials are measured in weeks with a planned end. Forever diets without review increase nutrition risk.",
            },
            {
                "q": "Should I eliminate five food groups at once?",
                "a": "Usually no. Broad cuts make it harder to learn what mattered and easier to lose weight. Ask for a structured plan.",
            },
        ],
    },
]


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    existing = {x["slug"] for x in data["pages"]}
    added = 0
    for page in NEW_PAGES:
        if page["slug"] not in existing:
            data["pages"].append(page)
            added += 1
    PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"pages={len(data['pages'])} added={added}")


if __name__ == "__main__":
    main()
