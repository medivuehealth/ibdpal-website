#!/usr/bin/env python3
# Prose style: do not use em dash. Use periods, commas, colons, or "|" in titles.
"""Generate Wave 2 food x IBD SEO blogs (vegetables + potato staples)."""
from __future__ import annotations

import json
import re
import shutil
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOGS = ROOT / "blogs"
DATA = ROOT / "data" / "wave2-food-nutrition-posts.json"
SITEMAP = ROOT / "sitemap.xml"
VERCEL = ROOT / "vercel.json"
SITE = "https://www.ibdpal.org"

sys.path.insert(0, str(ROOT / "scripts"))
from generate_blog_posts import render_post  # noqa: E402

FALLBACK_IMAGE = BLOGS / "assets" / "low-residue" / "low-residue_1.jpg"

IMAGE_URLS = {
    "carrots-ibd": "https://images.unsplash.com/photo-1598170845058-32b9d6a5da37?auto=format&w=1200&q=80",
    "potato-ibd": "https://images.unsplash.com/photo-1518977676601-b53f82aba655?auto=format&w=1200&q=80",
    "sweet-potato-ibd": "https://images.unsplash.com/photo-1589939705384-5185137a7f0f?auto=format&w=1200&q=80",
    "spinach-ibd": "https://images.unsplash.com/photo-1576045057995-568f588f82fb?auto=format&w=1200&q=80",
    "broccoli-ibd": "https://images.unsplash.com/photo-1628773822503-930a7eaecf80?auto=format&w=1200&q=80",
    "zucchini-ibd": "https://images.unsplash.com/photo-1592419044706-39796d40f98c?auto=format&w=1200&q=80",
    "cucumber-ibd": "https://images.unsplash.com/photo-1449300079323-02e209d9d3a6?auto=format&w=1200&q=80",
    "tomato-ibd": "https://images.unsplash.com/photo-1592924357228-91a4daadcfea?auto=format&w=1200&q=80",
    "onion-garlic-ibd": "https://images.unsplash.com/photo-1518977956812-cd3dbadaaf31?auto=format&w=1200&q=80",
    "corn-ibd": "https://images.unsplash.com/photo-1551754655-cd27e38d2076?auto=format&w=1200&q=80",
}


def food_body(f: dict) -> str:
    name = f["name"]
    name_l = name.lower()
    macros = "".join(f"<li><strong>{k}:</strong> {v}</li>" for k, v in f["macros"])
    micros = "".join(f"<li><strong>{k}:</strong> {v}</li>" for k, v in f["micros"])
    flare = "".join(f"<li>{x}</li>" for x in f["flare_tips"])
    rem = "".join(f"<li>{x}</li>" for x in f["remission_tips"])
    myths = "".join(f"<li><strong>{m[0]}</strong> {m[1]}</li>" for m in f["myths"])
    questions = "".join(f"<li>{q}</li>" for q in f["questions"])
    related = " · ".join(f'<a href="{href}">{label}</a>' for href, label in f["related"])
    return f"""
<p>Searches like <strong>{f['primary_kw']}</strong>, <strong>{f['secondary_kw']}</strong>, and <strong>{name_l} ulcerative colitis</strong> are common because patients want clear, practical answers. Tolerance with Crohn's disease or ulcerative colitis is individual. This page covers typical nutrition facts, flare versus remission ideas, and questions for your GI or dietitian. It is education only, not a prescription to eat or avoid {name_l}.</p>

<h2>Nutrition snapshot: {name}</h2>
<p>{f['nutrition_intro']}</p>
<h3>Approximate macros (typical serving)</h3>
<ul class="blog-list">{macros}</ul>
<p>Amounts vary by brand, cooking method, and portion. Use a label or USDA FoodData Central for exact numbers, and IBDPal food logs to compare your portion to how you felt afterward.</p>
<h3>Micronutrients people ask about</h3>
<ul class="blog-list">{micros}</ul>

<h2>Flare versus remission: how many people approach {name_l}</h2>
<p>{f['tolerance_intro']}</p>
<h3>During a flare (when your team wants gentler textures)</h3>
<ul class="blog-list">{flare}</ul>
<h3>In remission (when variety is usually easier)</h3>
<ul class="blog-list">{rem}</ul>
<p>If you have strictures, recent surgery, or a short bowel history, fiber and skins may need a different plan. Follow your clinician, not a generic list.</p>

<h2>Prep ideas that often feel kinder</h2>
<p>{f['prep']}</p>

<h2>Common myths about {name_l} and IBD</h2>
<ul class="blog-list">{myths}</ul>

<h2>How to track {name_l} with IBDPal</h2>
<p>Log the form (raw, cooked, peeled, pureed), portion size, and symptoms for 24 to 48 hours. Patterns beat memory at clinic visits. Pair food logs with stool urgency, pain, and energy notes. See <a href="/blog/tracking-food-symptoms-ibdpal">tracking food and symptoms</a> for a simple workflow.</p>

<h2>Questions for your gastroenterologist or dietitian</h2>
<ul class="blog-list">{questions}</ul>
<p>Bring your food log and any recent labs (iron, B12, vitamin D, electrolytes) so advice can match your disease location and nutrition gaps.</p>

<h2>When food questions become urgent</h2>
<p>Contact your care team promptly for severe pain, vomiting, inability to keep fluids down, heavy bleeding, fever, or rapid weight loss. Food guides cannot replace evaluation for obstruction, severe flare, or dehydration. See <a href="/flare-help">flare help</a> and <a href="/blog/when-to-go-er-ibd">when to go to the ER</a>.</p>

<p>Related reading: {related}. Hub: <a href="/ibd-nutrition">IBD nutrition</a>.</p>
""".strip()


FOODS: list[dict] = [
    {
        "slug": "carrots-ibd",
        "name": "Carrots",
        "title": "Carrots and IBD: Cooked vs Raw, Vitamin A, and Flare Tips",
        "description": "Carrots with Crohn's or colitis: beta-carotene, cooked vs raw, puree ideas, and dietitian questions. Education only.",
        "category": "Nutrition · August 2026",
        "date_display": "August 24, 2026",
        "date_iso": "2026-08-24T12:00:00Z",
        "asset_dir": "carrots-ibd",
        "resource_category": "nutrition",
        "tags": ["carrot", "carrots", "vitamin A", "vegetable", "cooked vegetables", "Crohn's", "colitis", "nutrition"],
        "share": "Carrots and IBD: cooked vs raw tips. Education only.",
        "primary_kw": "carrots Crohn's disease",
        "secondary_kw": "cooked carrots colitis",
        "nutrition_intro": (
            "Carrots supply carbohydrate, fiber, and beta-carotene (vitamin A precursor). "
            "Cooking softens the crunchy fibers that often feel harder during flares than the vegetable's nutrition value itself."
        ),
        "macros": [
            ("Serving", "1/2 cup cooked slices (~80 g)"),
            ("Calories", "~35"),
            ("Carbohydrate", "~8 g"),
            ("Fiber", "~2.5 g"),
            ("Protein", "~1 g"),
            ("Fat", "negligible"),
        ],
        "micros": [
            ("Vitamin A (from beta-carotene)", "Supports vision and epithelial health in overall diets"),
            ("Vitamin K and biotin", "Small contributions"),
            ("Potassium", "Modest electrolyte support"),
        ],
        "tolerance_intro": (
            "Well-cooked, peeled carrots and smooth carrot puree appear on many gentle menus. "
            "Raw sticks and large salad shreds are higher residue and more often paused during flares or with strictures."
        ),
        "flare_tips": [
            "Peel, boil or steam until soft, then mash or puree",
            "Start with a few tablespoons of puree in soup or with white rice",
            "Avoid raw carrot sticks and thick raw shreds if urgency is high",
            "Skip heavily spiced carrot fries if fat and spice worsen symptoms",
        ],
        "remission_tips": [
            "Trial soft steamed coins before returning to raw snacks",
            "Roast until tender with a small amount of oil if fat is tolerated",
            "Pair with chicken or eggs for a more complete plate",
        ],
        "prep": (
            "Peel thoroughly, cut thin, and cook until a fork slides through with no crunch. "
            "Blend with broth into a smooth soup. Baby carrots still need thorough cooking for flare textures."
        ),
        "myths": [
            ("Carrots are always safe in Crohn's.", "Tolerance depends on form; raw crunch differs from puree."),
            ("You must avoid all orange vegetables.", "Often false; texture and portion matter more."),
            ("Carrot juice equals eating carrots.", "Juice drops fiber and concentrates sugars."),
        ],
        "questions": [
            "Should carrots be peeled and pureed on my low-residue plan?",
            "When can I reintroduce raw carrots after a flare?",
            "Do my vitamin A labs or supplements change how much carrot I need from food?",
        ],
        "related": [
            ("/blog/low-residue-diet-flare", "low-residue diet"),
            ("/blog/fiber-and-ibd-diet", "fiber and IBD"),
            ("/blog/best-foods-crohns-flare", "flare food ideas"),
        ],
    },
    {
        "slug": "potato-ibd-white",
        "name": "White potatoes",
        "title": "White Potatoes and IBD: Flare Carbs, Skins, and Prep Tips",
        "description": "White potatoes with Crohn's or colitis: peeled vs skin-on, mash ideas, resistant starch notes, and clinic questions. Education only.",
        "category": "Nutrition · August 2026",
        "date_display": "August 24, 2026",
        "date_iso": "2026-08-24T14:00:00Z",
        "asset_dir": "potato-ibd",
        "resource_category": "nutrition",
        "tags": ["potato", "potatoes", "white potato", "carbohydrate", "low residue", "flare food", "Crohn's", "colitis", "nutrition"],
        "share": "White potatoes and IBD: skins, mash, and flare tips. Education only.",
        "primary_kw": "potato Crohn's disease",
        "secondary_kw": "mashed potatoes colitis flare",
        "nutrition_intro": (
            "White potatoes are a starchy vegetable that mainly provide carbohydrate energy, potassium, and vitamin C when not overcooked into oblivion. "
            "Peeled, well-cooked potato is a classic low-residue style option alongside white rice."
        ),
        "macros": [
            ("Serving", "1 medium peeled boiled potato (~150 g)"),
            ("Calories", "~130"),
            ("Carbohydrate", "~30 g"),
            ("Fiber", "~2 g peeled; higher with skin"),
            ("Protein", "~3 g"),
            ("Fat", "negligible before butter or oil"),
        ],
        "micros": [
            ("Potassium", "Helpful when replacing losses from diarrhea"),
            ("Vitamin C", "Present especially in freshly cooked potato"),
            ("Vitamin B6", "Supports everyday metabolism"),
            ("Resistant starch", "Increases when cooked potatoes cool; some people notice more gas"),
        ],
        "tolerance_intro": (
            "Peeled mashed or boiled potatoes are often better tolerated than skins, fries, or cold potato salad with skins and raw onion. "
            "Fat toppings (butter, gravy, cheese) can change tolerance more than the potato flesh."
        ),
        "flare_tips": [
            "Peel, boil until soft, mash smooth with a little broth or lactose-free milk if approved",
            "Avoid skins, chips, and deep-fried fries during high urgency weeks",
            "Keep seasoning mild; skip chili and raw onion toppings",
            "Pair with shredded chicken or eggs for protein",
        ],
        "remission_tips": [
            "Trial thin skins if fiber goals increase and no stricture limits apply",
            "Bake and fluff with yogurt or olive oil if tolerated",
            "Use leftover cooled potato carefully if gas increases",
        ],
        "prep": (
            "Cut evenly so pieces cook soft at the same time. Mash thoroughly to reduce lumps. "
            "Instant mashed potato can work in a pinch; check sodium and fiber additives."
        ),
        "myths": [
            ("Potatoes are junk food with no place in IBD.", "Plain potato can be a practical flare carbohydrate."),
            ("Sweet potatoes are always better.", "Both can fit; fiber and preparation differ."),
            ("You must never eat potato skin.", "Many people in remission tolerate thin skins; ask about strictures."),
        ],
        "questions": [
            "Should potato skin stay off my plate while symptoms are active?",
            "How do potatoes fit next to white rice in my flare plan?",
            "Does resistant starch from cooled potato matter for my gas or bloating?",
        ],
        "related": [
            ("/blog/white-rice-ibd-flare", "white rice and IBD"),
            ("/blog/low-residue-diet-flare", "low-residue guide"),
            ("/guides/low-residue-diet-ibd", "low-residue patient guide"),
        ],
    },
    {
        "slug": "sweet-potato-ibd",
        "name": "Sweet potatoes",
        "title": "Sweet Potatoes and IBD: Fiber, Vitamin A, and Texture Tips",
        "description": "Sweet potatoes with Crohn's or colitis: beta-carotene, peeled mash, fiber notes, and dietitian questions. Education only.",
        "category": "Nutrition · August 2026",
        "date_display": "August 24, 2026",
        "date_iso": "2026-08-24T16:00:00Z",
        "asset_dir": "sweet-potato-ibd",
        "resource_category": "nutrition",
        "tags": ["sweet potato", "sweet potatoes", "vitamin A", "fiber", "vegetable", "Crohn's", "colitis", "nutrition"],
        "share": "Sweet potatoes and IBD: mash and fiber tips. Education only.",
        "primary_kw": "sweet potato Crohn's",
        "secondary_kw": "sweet potato ulcerative colitis",
        "nutrition_intro": (
            "Sweet potatoes offer carbohydrate, fiber, potassium, and a large amount of beta-carotene. "
            "They are slightly higher in fiber than peeled white potato, so texture and peeling still matter during flares."
        ),
        "macros": [
            ("Serving", "1/2 cup mashed peeled (~120 g)"),
            ("Calories", "~90 to 110"),
            ("Carbohydrate", "~20 to 25 g"),
            ("Fiber", "~3 g"),
            ("Protein", "~2 g"),
            ("Fat", "negligible before toppings"),
        ],
        "micros": [
            ("Vitamin A (beta-carotene)", "Very high relative to many vegetables"),
            ("Vitamin C and manganese", "Support everyday nutrition"),
            ("Potassium", "Useful electrolyte contribution"),
        ],
        "tolerance_intro": (
            "Peeled, well-mashed sweet potato is the form many people trial first. "
            "Skins, large roasted wedges, and sweet potato fries with heavy oil are more demanding."
        ),
        "flare_tips": [
            "Peel, boil or steam until soft, mash smooth",
            "Start with a few spoonfuls rather than a large baked potato",
            "Avoid skins and crispy fries during flares",
            "Limit sugary marshmallow toppings that add little nutrition",
        ],
        "remission_tips": [
            "Roast soft cubes if fiber is better tolerated",
            "Pair with turkey or chicken for balance",
            "Use as a colorful side instead of only white starches",
        ],
        "prep": (
            "Pierce and microwave then peel for a fast soft mash, or simmer cubes in water until collapse-ready. "
            "Blend with a splash of broth for a soup base."
        ),
        "myths": [
            ("Sweet potatoes cure inflammation.", "They support nutrition; they are not IBD medication."),
            ("White potato is always safer.", "Both can work; peel and cook soft for flares."),
            ("Orange vegetables cause flares.", "No strong evidence that color alone triggers Crohn's or colitis."),
        ],
        "questions": [
            "Is mashed sweet potato okay on my current residue plan?",
            "Should I prefer white potato while calprotectin is high?",
            "How does sweet potato fit my vitamin A or supplement plan?",
        ],
        "related": [
            ("/blog/potato-ibd-white", "white potatoes and IBD"),
            ("/blog/carrots-ibd", "carrots and IBD"),
            ("/blog/complete-ibd-nutrition-guide", "complete nutrition guide"),
        ],
    },
    {
        "slug": "spinach-leafy-greens-ibd",
        "name": "Spinach and leafy greens",
        "title": "Spinach and Leafy Greens With IBD: Iron, Oxalates, and Cooking Tips",
        "description": "Spinach and leafy greens with Crohn's or colitis: iron, folate, cooked vs raw, oxalate notes, and clinic questions. Education only.",
        "category": "Nutrition · August 2026",
        "date_display": "August 24, 2026",
        "date_iso": "2026-08-24T18:00:00Z",
        "asset_dir": "spinach-ibd",
        "resource_category": "nutrition",
        "tags": ["spinach", "leafy greens", "iron", "folate", "salad", "vegetable", "Crohn's", "colitis", "nutrition"],
        "share": "Spinach and leafy greens with IBD: cooked vs raw tips. Education only.",
        "primary_kw": "spinach Crohn's disease",
        "secondary_kw": "leafy greens ulcerative colitis",
        "nutrition_intro": (
            "Spinach and similar leafy greens provide folate, vitamin K, vitamin A, and some non-heme iron. "
            "Raw salads are high residue; cooking shrinks volume and softens leaves, which many IBD patients prefer during flares."
        ),
        "macros": [
            ("Serving", "1/2 cup cooked spinach (~90 g) or 2 cups raw"),
            ("Calories", "~20 to 40"),
            ("Carbohydrate", "~3 to 7 g"),
            ("Fiber", "~2 to 4 g"),
            ("Protein", "~3 g cooked"),
            ("Fat", "negligible"),
        ],
        "micros": [
            ("Folate", "Important for blood health and pregnancy planning"),
            ("Vitamin K", "Relevant if you take warfarin; keep intake consistent and ask your clinician"),
            ("Iron", "Non-heme iron; absorption improves with vitamin C foods when tolerated"),
            ("Oxalates", "Higher in spinach; discuss if you have a history of oxalate kidney stones"),
        ],
        "tolerance_intro": (
            "Well-cooked, finely chopped spinach in soups or omelets is usually easier than large raw salads. "
            "People with strictures are often advised to be careful with fibrous raw greens."
        ),
        "flare_tips": [
            "Cook spinach until soft and chop finely; stir into eggs or broth",
            "Avoid big raw kale or spinach salads during high urgency weeks",
            "If residue is restricted, pause leafy greens briefly per your team",
            "Do not rely on spinach alone to fix iron-deficiency anemia",
        ],
        "remission_tips": [
            "Reintroduce cooked greens before large raw salads",
            "Pair with lemon or strawberries if vitamin C helps iron goals and acidity is tolerated",
            "Rotate spinach with softer greens your dietitian suggests",
        ],
        "prep": (
            "Saute or steam until wilted and soft. Squeeze out excess water for omelets. "
            "Blend cooked spinach into smooth soups if leaf pieces bother you."
        ),
        "myths": [
            ("Spinach iron will cure IBD anemia.", "IBD anemia often needs labs and sometimes IV or oral iron therapy."),
            ("All salads are forbidden forever.", "Many people return to tender greens in remission."),
            ("Raw is always healthier.", "Cooked greens can be the smarter texture choice with active IBD."),
        ],
        "questions": [
            "Are cooked leafy greens allowed on my low-residue instructions?",
            "Do oxalates matter with my kidney stone history?",
            "How should greens fit with my iron therapy plan?",
        ],
        "related": [
            ("/blog/anemia-iron-deficiency-ibd", "anemia and iron deficiency"),
            ("/guides/iron-deficiency-nutrition-ibd", "iron deficiency nutrition"),
            ("/blog/fiber-and-ibd-diet", "fiber guide"),
        ],
    },
    {
        "slug": "broccoli-ibd",
        "name": "Broccoli",
        "title": "Broccoli and IBD: Gas, Stems, and Softer Prep Ideas",
        "description": "Broccoli with Crohn's or colitis: fiber, gas tips, florets vs stems, cooked texture, and dietitian questions. Education only.",
        "category": "Nutrition · August 2026",
        "date_display": "August 25, 2026",
        "date_iso": "2026-08-25T12:00:00Z",
        "asset_dir": "broccoli-ibd",
        "resource_category": "nutrition",
        "tags": ["broccoli", "cruciferous", "gas", "fiber", "vegetable", "Crohn's", "colitis", "nutrition"],
        "share": "Broccoli and IBD: softer prep and gas tips. Education only.",
        "primary_kw": "broccoli Crohn's disease",
        "secondary_kw": "broccoli ulcerative colitis gas",
        "nutrition_intro": (
            "Broccoli provides vitamin C, vitamin K, folate, and fiber. It is a cruciferous vegetable that can increase gas "
            "for many people, with or without IBD, especially when eaten raw or undercooked."
        ),
        "macros": [
            ("Serving", "1/2 cup cooked florets (~80 g)"),
            ("Calories", "~25"),
            ("Carbohydrate", "~5 g"),
            ("Fiber", "~2.5 g"),
            ("Protein", "~2 g"),
            ("Fat", "negligible"),
        ],
        "micros": [
            ("Vitamin C", "High for the calorie count"),
            ("Vitamin K and folate", "Support everyday micronutrient intake"),
            ("Sulforaphane precursors", "Studied in general nutrition research; not an IBD drug"),
        ],
        "tolerance_intro": (
            "Soft-cooked florets with peeled stems removed are the usual starting point. "
            "Raw broccoli, large stems, and huge servings are common triggers for bloating even in remission."
        ),
        "flare_tips": [
            "Many people pause broccoli during flares; ask before forcing it",
            "If trialing, use tiny portions of well-steamed soft florets only",
            "Avoid raw crudites and fibrous stems",
            "Skip broccoli salads with raw onion and seeds",
        ],
        "remission_tips": [
            "Steam until very soft; chew thoroughly",
            "Start with a few florets, not a full bowl",
            "Pair with rice and chicken rather than a broccoli-only meal",
        ],
        "prep": (
            "Cut small florets, peel tough stem skin if using stems, and steam or boil until mashable. "
            "Puree into soup if pieces still feel rough."
        ),
        "myths": [
            ("Broccoli detoxes the gut.", "No vegetable detoxes Crohn's or colitis."),
            ("Gas from broccoli means a dangerous flare.", "Gas is common; track patterns and call for red-flag symptoms."),
            ("You must eat crucifers daily for IBD.", "Variety matters more than one hero vegetable."),
        ],
        "questions": [
            "Should I avoid cruciferous vegetables while symptomatic?",
            "Is pureed broccoli okay on a low-residue plan?",
            "How do we reintroduce broccoli after surgery or strictures?",
        ],
        "related": [
            ("/blog/gas-bloating-ibd", "gas and bloating"),
            ("/blog/fodmap-diet-crohns-colitis", "FODMAP overview"),
            ("/blog/fiber-and-ibd-diet", "fiber and IBD"),
        ],
    },
    {
        "slug": "zucchini-ibd",
        "name": "Zucchini",
        "title": "Zucchini and IBD: Soft Squash for Gentler Vegetable Intake",
        "description": "Zucchini with Crohn's or colitis: peeled cooked squash, low-residue style tips, and clinic questions. Education only.",
        "category": "Nutrition · August 2026",
        "date_display": "August 25, 2026",
        "date_iso": "2026-08-25T14:00:00Z",
        "asset_dir": "zucchini-ibd",
        "resource_category": "nutrition",
        "tags": ["zucchini", "summer squash", "vegetable", "cooked vegetables", "Crohn's", "colitis", "nutrition"],
        "share": "Zucchini and IBD: soft cooked squash tips. Education only.",
        "primary_kw": "zucchini Crohn's disease",
        "secondary_kw": "zucchini colitis diet",
        "nutrition_intro": (
            "Zucchini (summer squash) is mostly water with modest carbohydrate, fiber, vitamin C, and potassium. "
            "Peeled, seeded, and well-cooked zucchini is often easier than raw spiral noodles or large grilled planks with skin."
        ),
        "macros": [
            ("Serving", "1/2 cup cooked peeled (~90 g)"),
            ("Calories", "~15 to 20"),
            ("Carbohydrate", "~3 to 4 g"),
            ("Fiber", "~1 g"),
            ("Protein", "~1 g"),
            ("Fat", "negligible"),
        ],
        "micros": [
            ("Vitamin C and manganese", "Small helpful amounts"),
            ("Potassium", "Supports electrolyte intake with fluids"),
            ("Carotenoids in yellow varieties", "General nutrition interest"),
        ],
        "tolerance_intro": (
            "Soft sauteed or steamed zucchini without tough skin or large seeds is a common \"starter vegetable\" after flares. "
            "Raw zoodles behave more like salad residue for some guts."
        ),
        "flare_tips": [
            "Peel, scoop seeds if large, cook until translucent and soft",
            "Dice small or puree into soups",
            "Avoid raw spiralized zucchini during flares",
            "Limit oily fried zucchini sticks",
        ],
        "remission_tips": [
            "Add soft cubes to rice bowls with chicken or turkey",
            "Trial thin skins if tolerated",
            "Use as a volume food when appetite is low but you want vegetables",
        ],
        "prep": (
            "Peel with a vegetable peeler, slice thin, and simmer in broth until soft. "
            "Mash lightly into soft scramble eggs or fold into mashed potato."
        ),
        "myths": [
            ("Zucchini noodles are always IBD-safe.", "Raw zoodles can still be high residue for some people."),
            ("All squash is too fibrous.", "Peeled cooked summer squash is often gentler than tough winter squash skins."),
            ("Vegetables must be raw to count.", "Cooked vegetables still provide nutrients."),
        ],
        "questions": [
            "Is peeled zucchini allowed on my gentle diet phase?",
            "When can I try zucchini with skin?",
            "How should I use squash if I also follow low FODMAP portions?",
        ],
        "related": [
            ("/blog/low-residue-diet-flare", "low-residue diet"),
            ("/blog/carrots-ibd", "carrots"),
            ("/blog/best-foods-crohns-flare", "flare foods"),
        ],
    },
    {
        "slug": "cucumber-ibd",
        "name": "Cucumber",
        "title": "Cucumber and IBD: Hydration, Peels, and Seed Tips",
        "description": "Cucumber with Crohn's or colitis: water content, peeled vs skin-on, seeds, and dietitian questions. Education only.",
        "category": "Nutrition · August 2026",
        "date_display": "August 25, 2026",
        "date_iso": "2026-08-25T16:00:00Z",
        "asset_dir": "cucumber-ibd",
        "resource_category": "nutrition",
        "tags": ["cucumber", "hydration", "vegetable", "peel", "seeds", "Crohn's", "colitis", "nutrition"],
        "share": "Cucumber and IBD: peel and seed tips. Education only.",
        "primary_kw": "cucumber Crohn's disease",
        "secondary_kw": "cucumber ulcerative colitis",
        "nutrition_intro": (
            "Cucumber is mostly water with small amounts of vitamin K and potassium. "
            "It can support hydration snacks, but peels and seeds are the usual tolerance variables."
        ),
        "macros": [
            ("Serving", "1/2 cup peeled sliced (~60 g)"),
            ("Calories", "~8"),
            ("Carbohydrate", "~2 g"),
            ("Fiber", "~0.5 g"),
            ("Protein", "~0.3 g"),
            ("Fat", "negligible"),
        ],
        "micros": [
            ("Vitamin K", "Small amount; consistency matters on warfarin"),
            ("Potassium", "Modest"),
            ("Water", "Helpful snack fluid alongside oral rehydration plans"),
        ],
        "tolerance_intro": (
            "Peeled, seedless or deseeded cucumber is usually tried before skin-on spears. "
            "Large raw salads with peels may feel abrasive during flares."
        ),
        "flare_tips": [
            "Peel fully and scoop seeds; slice thin",
            "Start with a few slices, not a whole cucumber salad",
            "Avoid pickled cucumbers with garlic and spice if those trigger you",
            "If raw produce is restricted, pause cucumber and use melon for hydrating foods",
        ],
        "remission_tips": [
            "Add peeled cucumber to sandwiches with turkey",
            "Trial thin skins if no stricture concerns",
            "Use as a crunchy snack alternative to chips when tolerated",
        ],
        "prep": (
            "English cucumbers often have thinner skins and fewer seeds. Still peel if residue is a concern. "
            "Chill slices for nausea-friendly snacks."
        ),
        "myths": [
            ("Cucumber water detoxes IBD.", "Hydration helps; it does not treat inflammation."),
            ("All raw vegetables are identical.", "Peel, seed, and portion change the experience a lot."),
            ("Pickles are the same as fresh cucumber.", "Vinegar, garlic, and spice change tolerance."),
        ],
        "questions": [
            "Are peeled cucumbers okay while I am on a low-residue plan?",
            "Should I avoid cucumber peels with my stricture history?",
            "How can cucumber fit my fluid goals during diarrhea?",
        ],
        "related": [
            ("/blog/hydration-tips-ibd", "hydration tips"),
            ("/blog/melon-ibd", "melon and IBD"),
            ("/blog/low-residue-diet-flare", "low-residue eating"),
        ],
    },
    {
        "slug": "tomatoes-ibd",
        "name": "Tomatoes",
        "title": "Tomatoes and IBD: Acidity, Sauces, and Seed Tips",
        "description": "Tomatoes with Crohn's or colitis: acidity, cooked sauces, seeds and skins, and clinic questions. Education only.",
        "category": "Nutrition · August 2026",
        "date_display": "August 25, 2026",
        "date_iso": "2026-08-25T18:00:00Z",
        "asset_dir": "tomato-ibd",
        "resource_category": "nutrition",
        "tags": ["tomato", "tomatoes", "acidity", "lycopene", "sauce", "vegetable", "Crohn's", "colitis", "nutrition"],
        "share": "Tomatoes and IBD: acidity and sauce tips. Education only.",
        "primary_kw": "tomatoes Crohn's disease",
        "secondary_kw": "tomato sauce ulcerative colitis",
        "nutrition_intro": (
            "Tomatoes provide vitamin C, potassium, and lycopene (especially in cooked forms). "
            "Acidity, skins, and seeds are why some people with IBD limit raw tomatoes or spicy tomato sauces during flares."
        ),
        "macros": [
            ("Serving", "1/2 cup cooked tomato or sauce (~120 g)"),
            ("Calories", "~30 to 50 depending on added oil"),
            ("Carbohydrate", "~6 to 8 g"),
            ("Fiber", "~1 to 2 g"),
            ("Protein", "~1 g"),
            ("Fat", "low unless oil is added"),
        ],
        "micros": [
            ("Lycopene", "More available in cooked tomato products; not an IBD therapy"),
            ("Vitamin C", "Higher in fresh tomatoes; reduced with long cooking"),
            ("Potassium", "Present in tomato foods"),
            ("Sodium", "Watch canned sauces and ketchup"),
        ],
        "tolerance_intro": (
            "Smooth, mild tomato products without skins and seeds may sit better than raw wedges or chunky salsa. "
            "Acid reflux, mouth sores, or raw rectal irritation lead some patients to pause tomato temporarily."
        ),
        "flare_tips": [
            "Prefer strained, mild sauce in small amounts over raw tomato salads",
            "Avoid spicy arrabbiata-style heat during flares",
            "Skip sun-dried tomato pieces and thick skins if residue is limited",
            "If acidity burns, switch to broth-based sauces for a while",
        ],
        "remission_tips": [
            "Reintroduce peeled seeded tomatoes before large raw salads",
            "Use tomato with protein and starch, not only acidic snacks",
            "Compare fresh versus canned tolerance in your food log",
        ],
        "prep": (
            "Blanch, peel, and seed tomatoes for a softer sauce base, or choose strained passata. "
            "Cook briefly with mild herbs. Limit added chili flake."
        ),
        "myths": [
            ("Nightshade vegetables cause Crohn's.", "Evidence does not support a universal nightshade ban for IBD."),
            ("Tomato is always inflammatory.", "Some people are sensitive to acid or spice; that is not the same as proven causation."),
            ("Ketchup is a vegetable serving.", "It is mostly a condiment; watch sugar and sodium."),
        ],
        "questions": [
            "Should I pause tomatoes while I have mouth sores or severe urgency?",
            "Is strained tomato sauce okay on my current plan?",
            "Do canned tomatoes' sodium matter for me?",
        ],
        "related": [
            ("/blog/oranges-citrus-ibd", "citrus acidity tips"),
            ("/blog/oral-canker-sores-ibd", "mouth sores"),
            ("/blog/foods-that-may-trigger-uc-symptoms", "UC food trigger education"),
        ],
    },
    {
        "slug": "onion-garlic-ibd-fodmap",
        "name": "Onion and garlic",
        "title": "Onion and Garlic With IBD: FODMAPs, Flavor Swaps, and Flare Tips",
        "description": "Onion and garlic with Crohn's or colitis: FODMAP fructans, cooking oils, flavor alternatives, and dietitian questions. Education only.",
        "category": "Nutrition · August 2026",
        "date_display": "August 26, 2026",
        "date_iso": "2026-08-26T12:00:00Z",
        "asset_dir": "onion-garlic-ibd",
        "resource_category": "nutrition",
        "tags": ["onion", "garlic", "FODMAP", "fructans", "bloating", "flavor", "Crohn's", "colitis", "nutrition"],
        "share": "Onion and garlic with IBD: FODMAP and flavor tips. Education only.",
        "primary_kw": "onion garlic Crohn's",
        "secondary_kw": "garlic FODMAP colitis",
        "nutrition_intro": (
            "Onion and garlic are flavor staples with little calorie load, but they are high in fructan FODMAPs. "
            "That can drive gas and bloating in people with IBS overlap, which is common alongside IBD."
        ),
        "macros": [
            ("Serving", "varies; often small culinary amounts"),
            ("Calories", "low per clove or slice"),
            ("Carbohydrate", "mainly fructans in the FODMAP sense"),
            ("Fiber", "present in whole pieces"),
            ("Protein / Fat", "negligible"),
        ],
        "micros": [
            ("Sulfur compounds", "Give flavor and aroma; not a proven IBD cure"),
            ("Small amounts of vitamin C and B6", "Not the main reason people eat them"),
            ("Sodium in garlic salt", "Watch processed seasoning blends"),
        ],
        "tolerance_intro": (
            "Many low-FODMAP style plans limit onion and garlic pieces, especially during elimination phases. "
            "Garlic-infused oil (without garlic pieces) is sometimes used for flavor because fructans are water-soluble, not oil-soluble. Confirm with a dietitian."
        ),
        "flare_tips": [
            "Pause large amounts of onion and garlic if bloating and urgency spike",
            "Avoid raw onion on salads and heavy garlic sauces",
            "Ask about green onion tops or chives as milder options in some FODMAP frameworks",
            "Read labels: onion and garlic powders hide in broths and spice mixes",
        ],
        "remission_tips": [
            "Reintroduce with a dietitian using measured portions",
            "Cook thoroughly; start tiny",
            "Use infused oils for aroma when pieces are not tolerated",
        ],
        "prep": (
            "Saute aromatics separately so you can remove pieces if needed. "
            "Build flavor with herbs, ginger (if tolerated), citrus zest (if acidity is okay), or infused oils per professional guidance."
        ),
        "myths": [
            ("Garlic cures infections in IBD.", "Food is not a substitute for prescribed antibiotics or IBD therapy."),
            ("If FODMAPs help IBS symptoms, they treat Crohn's inflammation.", "Symptom relief is not the same as healing intestinal inflammation."),
            ("You must avoid all flavor forever.", "Many people find workarounds and later reintroductions."),
        ],
        "questions": [
            "Do I have IBS overlap that makes fructans worth limiting?",
            "Is garlic-infused oil appropriate for me?",
            "How should we reintroduce onion after a flare?",
        ],
        "related": [
            ("/blog/fodmap-diet-crohns-colitis", "FODMAP diet for IBD"),
            ("/blog/gas-bloating-ibd", "gas and bloating"),
            ("/blog/dining-out-ibd-restaurants", "dining out tips"),
        ],
    },
    {
        "slug": "corn-ibd",
        "name": "Corn",
        "title": "Corn and IBD: Kernels, Skins, and When to Be Careful",
        "description": "Corn with Crohn's or colitis: insoluble hulls, creamed corn vs kernels, stricture cautions, and clinic questions. Education only.",
        "category": "Nutrition · August 2026",
        "date_display": "August 26, 2026",
        "date_iso": "2026-08-26T14:00:00Z",
        "asset_dir": "corn-ibd",
        "resource_category": "nutrition",
        "tags": ["corn", "maize", "kernels", "fiber", "stricture", "vegetable", "Crohn's", "colitis", "nutrition"],
        "share": "Corn and IBD: kernels, hulls, and cautions. Education only.",
        "primary_kw": "corn Crohn's disease",
        "secondary_kw": "corn ulcerative colitis diet",
        "nutrition_intro": (
            "Corn provides carbohydrate, some fiber, and lutein/zeaxanthin carotenoids. "
            "The tough outer hull of whole kernels is classic insoluble residue that can be problematic with strictures."
        ),
        "macros": [
            ("Serving", "1/2 cup cooked kernels (~80 g)"),
            ("Calories", "~70"),
            ("Carbohydrate", "~15 g"),
            ("Fiber", "~2 g"),
            ("Protein", "~2 g"),
            ("Fat", "~1 g"),
        ],
        "micros": [
            ("Folate and thiamin", "Present in modest amounts"),
            ("Magnesium and phosphorus", "Small contributions"),
            ("Lutein / zeaxanthin", "Eye-health related carotenoids in general nutrition"),
        ],
        "tolerance_intro": (
            "Whole kernels, popcorn, and corn skins are frequently limited on low-residue or stricture-aware plans. "
            "Smooth creamed corn or finely processed corn products may be discussed case by case, but many teams still prefer pausing whole kernels during flares."
        ),
        "flare_tips": [
            "Many clinicians suggest avoiding whole corn kernels and popcorn during flares or known strictures",
            "Do not assume tortillas or corn chips are identical to whole kernels; still trial carefully",
            "Skip corn salads with raw peppers and skins",
            "Choose potato or rice as safer starch sides when residue is restricted",
        ],
        "remission_tips": [
            "Only reintroduce kernels with clinician clearance if you have stricturing Crohn's",
            "Chew thoroughly; start with a spoonful",
            "Prefer tender canned or fresh kernels over popcorn at first",
        ],
        "prep": (
            "If cleared to trial, cook until tender and chew well. "
            "Creamed styles reduce intact hulls but still contain corn fiber. Popcorn remains high residue for many people."
        ),
        "myths": [
            ("Seeing corn in stool always means poor digestion of everything.", "Hulls often pass visibly; ask your team what it means for you."),
            ("Corn is forbidden for all IBD forever.", "Some people without strictures tolerate small amounts in remission."),
            ("Corn syrup is the same discussion as corn kernels.", "Different products, different issues."),
        ],
        "questions": [
            "Do I have strictures that mean I should avoid whole corn and popcorn?",
            "Is creamed corn acceptable on my plan?",
            "When is it safe to reintroduce kernels after surgery?",
        ],
        "related": [
            ("/blog/low-residue-diet-flare", "low-residue diet"),
            ("/blog/vomiting-obstruction-ibd-warning-signs", "obstruction warning signs"),
            ("/blog/fiber-and-ibd-diet", "fiber guide"),
        ],
    },
]


def build_posts() -> list[dict]:
    posts = []
    for f in FOODS:
        posts.append(
            {
                "slug": f["slug"],
                "title": f["title"],
                "description": f["description"],
                "category": f["category"],
                "date_display": f["date_display"],
                "date_iso": f["date_iso"],
                "asset_dir": f["asset_dir"],
                "resource_category": f["resource_category"],
                "tags": f["tags"],
                "share": f["share"],
                "images": [f'{f["asset_dir"]}_1.jpg'],
                "alts": [f'{f["name"]} for IBD nutrition education'],
                "body": food_body(f),
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
        out = BLOGS / f"{post['slug']}.html"
        out.write_text(render_post(post), encoding="utf-8")
        slugs.append(post["slug"])
        print("wrote", out.name)
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
    marker = "<!-- wave2-food-nutrition-blogs -->"
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
        "  <!-- wave1-food-nutrition-blogs -->",
        "  <!-- seo-wellness-blogs -->",
        "  <!-- ibd-topic-blogs -->",
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
    DATA.parent.mkdir(parents=True, exist_ok=True)
    DATA.write_text(
        json.dumps({"wave": 2, "theme": "vegetables-nutrition", "posts": posts}, ensure_ascii=False, indent=2)
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
    print("Done.", len(slugs), "Wave 2 vegetable posts.")


if __name__ == "__main__":
    main()
