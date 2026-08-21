#!/usr/bin/env python3
# Prose style: do not use em dash. Use periods, commas, colons, or "|" in titles.
"""Generate Wave 1 food x IBD SEO blogs (fruits + chicken, eggs, rice, turkey)."""
from __future__ import annotations

import json
import re
import shutil
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOGS = ROOT / "blogs"
DATA = ROOT / "data" / "wave1-food-nutrition-posts.json"
SITEMAP = ROOT / "sitemap.xml"
VERCEL = ROOT / "vercel.json"
SITE = "https://www.ibdpal.org"

sys.path.insert(0, str(ROOT / "scripts"))
from generate_blog_posts import render_post  # noqa: E402

FALLBACK_IMAGE = BLOGS / "assets" / "low-residue" / "low-residue_1.jpg"

IMAGE_URLS = {
    "banana-ibd": "https://images.unsplash.com/photo-1571771894821-ce9b6c11b08e?auto=format&w=1200&q=80",
    "apple-ibd": "https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6?auto=format&w=1200&q=80",
    "blueberries-ibd": "https://images.unsplash.com/photo-1498557850523-fd3d118b962e?auto=format&w=1200&q=80",
    "strawberries-ibd": "https://images.unsplash.com/photo-1464965911861-746a04b4bca6?auto=format&w=1200&q=80",
    "melon-ibd": "https://images.unsplash.com/photo-1587049352846-4a222e784d38?auto=format&w=1200&q=80",
    "avocado-ibd": "https://images.unsplash.com/photo-1523049673857-eb18f1d7b578?auto=format&w=1200&q=80",
    "oranges-ibd": "https://images.unsplash.com/photo-1547514701-42782101795e?auto=format&w=1200&q=80",
    "grapes-ibd": "https://images.unsplash.com/photo-1596363505729-4190a9506133?auto=format&w=1200&q=80",
    "chicken-ibd": "https://images.unsplash.com/photo-1598103442097-8b74394b95c6?auto=format&w=1200&q=80",
    "eggs-ibd": "https://images.unsplash.com/photo-1482049016688-2d3e1b311543?auto=format&w=1200&q=80",
    "white-rice-ibd": "https://images.unsplash.com/photo-1536304993881-ff6e9eefa2a6?auto=format&w=1200&q=80",
    "turkey-ibd": "https://images.unsplash.com/photo-1574781330855-d0db8cc6a79c?auto=format&w=1200&q=80",
}


def food_body(f: dict) -> str:
    """Shared SEO template for single-food IBD education posts."""
    name = f["name"]
    name_l = name.lower()
    macros = "".join(f"<li><strong>{k}:</strong> {v}</li>" for k, v in f["macros"])
    micros = "".join(f"<li><strong>{k}:</strong> {v}</li>" for k, v in f["micros"])
    flare = "".join(f"<li>{x}</li>" for x in f["flare_tips"])
    rem = "".join(f"<li>{x}</li>" for x in f["remission_tips"])
    myths = "".join(
        f"<li><strong>{m[0]}</strong> {m[1]}</li>" for m in f["myths"]
    )
    questions = "".join(f"<li>{q}</li>" for q in f["questions"])
    related = " · ".join(
        f'<a href="{href}">{label}</a>' for href, label in f["related"]
    )
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
<p>Log the form (raw, cooked, peeled), portion size, and symptoms for 24 to 48 hours. Patterns beat memory at clinic visits. Pair food logs with stool urgency, pain, and energy notes. See <a href="/blog/tracking-food-symptoms-ibdpal">tracking food and symptoms</a> for a simple workflow.</p>

<h2>Questions for your gastroenterologist or dietitian</h2>
<ul class="blog-list">{questions}</ul>
<p>Bring your food log and any recent labs (iron, B12, vitamin D, electrolytes) so advice can match your disease location and nutrition gaps.</p>

<h2>When food questions become urgent</h2>
<p>Contact your care team promptly for severe pain, vomiting, inability to keep fluids down, heavy bleeding, fever, or rapid weight loss. Food guides cannot replace evaluation for obstruction, severe flare, or dehydration. See <a href="/flare-help">flare help</a> and <a href="/blog/when-to-go-er-ibd">when to go to the ER</a>.</p>

<p>Related reading: {related}. Hub: <a href="/ibd-nutrition">IBD nutrition</a>.</p>
""".strip()


FOODS: list[dict] = [
    {
        "slug": "banana-ibd-crohns-colitis",
        "name": "Bananas",
        "title": "Bananas and IBD: Fiber, Potassium, and Flare-Friendly Tips",
        "description": "Bananas with Crohn's or colitis: potassium, soluble fiber, ripe vs green, flare tips, and dietitian questions. Patient education only.",
        "category": "Nutrition · August 2026",
        "date_display": "August 21, 2026",
        "date_iso": "2026-08-21T12:00:00Z",
        "asset_dir": "banana-ibd",
        "resource_category": "nutrition",
        "tags": [
            "banana", "bananas", "potassium", "fiber", "fruit", "Crohn's", "colitis",
            "flare food", "soluble fiber", "nutrition",
        ],
        "share": "Bananas and IBD: potassium, fiber, and flare tips. Education only.",
        "primary_kw": "banana Crohn's disease",
        "secondary_kw": "are bananas good for colitis",
        "nutrition_intro": (
            "A medium banana is often used as a soft fruit option during gentler eating phases. "
            "It supplies carbohydrates for energy, a modest amount of fiber that is mostly soluble when ripe, "
            "and notable potassium, which matters when diarrhea increases electrolyte losses."
        ),
        "macros": [
            ("Serving", "1 medium banana (~118 g)"),
            ("Calories", "~105"),
            ("Carbohydrate", "~27 g"),
            ("Fiber", "~3 g (more resistant starch when greener)"),
            ("Protein", "~1 g"),
            ("Fat", "~0.3 g"),
        ],
        "micros": [
            ("Potassium", "Helps replace losses from diarrhea; discuss labs if you take certain blood pressure meds"),
            ("Vitamin B6", "Supports energy metabolism in everyday diets"),
            ("Vitamin C", "Modest amount; still useful alongside other produce"),
            ("Magnesium", "Small contribution; not a full replacement for deficiency therapy"),
        ],
        "tolerance_intro": (
            "Many people tolerate ripe bananas better than firm green ones during flares because ripening "
            "shifts starch toward softer sugars and soluble fiber. Seeds and tough skins are not the issue here; "
            "ripeness and portion size usually matter more."
        ),
        "flare_tips": [
            "Choose yellow bananas with small brown spots; mash or slice into oatmeal or yogurt if approved",
            "Start with half a banana and note urgency or bloating",
            "Skip green bananas if they feel gassy or constipating for you",
            "Pair with a gentle protein (eggs, tender chicken) rather than a huge fruit-only meal",
        ],
        "remission_tips": [
            "Use as a portable snack with nut butter if nuts are tolerated",
            "Add to smoothies without large seed loads if seeds bother you",
            "Rotate with melon or cooked apple so one fruit does not dominate every day",
        ],
        "prep": (
            "Mashed ripe banana, banana with white toast, or blended into a lactose-free smoothie are common "
            "gentle formats. Avoid frying in heavy batters if fat worsens urgency. Frozen banana ice cream "
            "style treats are fine for some in remission; test small servings."
        ),
        "myths": [
            ("Bananas always calm Crohn's.", "Helpful for many, but not a treatment. Active disease still needs medical care."),
            ("You must avoid all fruit in IBD.", "Often false. Texture and portion matter more than a total ban."),
            ("Green bananas are always better.", "They are higher in resistant starch, which can increase gas for some people."),
        ],
        "questions": [
            "Given my stool pattern, should I favor ripe bananas or pause fruit briefly?",
            "Do my potassium or magnesium labs suggest I need more than food alone?",
            "If I have a stricture, are bananas still okay in my plan?",
        ],
        "related": [
            ("/blog/fiber-and-ibd-diet", "fiber and IBD"),
            ("/blog/low-residue-diet-flare", "low-residue flare eating"),
            ("/blog/electrolytes-flare-ibd", "electrolytes during flares"),
        ],
    },
    {
        "slug": "apple-ibd-cooked-vs-raw",
        "name": "Apples",
        "title": "Apples and IBD: Cooked vs Raw, Fiber, and Flare Tips",
        "description": "Apples with Crohn's or colitis: cooked vs raw, skins, pectin fiber, applesauce ideas, and clinic questions. Education only.",
        "category": "Nutrition · August 2026",
        "date_display": "August 21, 2026",
        "date_iso": "2026-08-21T14:00:00Z",
        "asset_dir": "apple-ibd",
        "resource_category": "nutrition",
        "tags": [
            "apple", "apples", "applesauce", "pectin", "fiber", "fruit", "cooked fruit",
            "Crohn's", "colitis", "nutrition",
        ],
        "share": "Apples and IBD: cooked vs raw tips. Education only.",
        "primary_kw": "apples Crohn's disease",
        "secondary_kw": "applesauce colitis flare",
        "nutrition_intro": (
            "Apples provide carbohydrate, fiber (including pectin), and vitamin C. The form matters: "
            "raw with skin is higher residue; peeled, cooked, or smooth applesauce is often discussed for gentler menus."
        ),
        "macros": [
            ("Serving", "1 medium apple (~182 g) or 1/2 cup applesauce"),
            ("Calories", "~95 (fresh) / ~50 (unsweetened applesauce, 1/2 cup)"),
            ("Carbohydrate", "~25 g fresh"),
            ("Fiber", "~4 g fresh with skin; less when peeled or strained"),
            ("Protein", "~0.5 g"),
            ("Fat", "negligible"),
        ],
        "micros": [
            ("Vitamin C", "Supports everyday immune and tissue roles; amount drops with long cooking"),
            ("Potassium", "Modest contribution"),
            ("Pectin (soluble fiber)", "Often easier than tough skins for some guts; still individual"),
        ],
        "tolerance_intro": (
            "Raw apple skins and firm flesh can feel abrasive during flares or with strictures. "
            "Cooked peeled apple and unsweetened applesauce are classic low-residue style options many clinics mention."
        ),
        "flare_tips": [
            "Prefer peeled, stewed apple or smooth unsweetened applesauce",
            "Avoid large raw salads of apple with skins if urgency is high",
            "Watch sweetened sauce: extra sugar alcohols or juice concentrates can worsen diarrhea for some",
            "Sip fluids with the snack; dry mouth plus fiber can feel uncomfortable",
        ],
        "remission_tips": [
            "Trial thin-skinned, well-chewed slices if raw fruit is a goal",
            "Pair with protein (cheese if tolerated, turkey, eggs) for steadier energy",
            "Bake apples with cinnamon as a softer dessert alternative",
        ],
        "prep": (
            "Simmer peeled chunks until soft, blend into sauce, or choose store unsweetened applesauce without "
            "added inulin if that fiber bothers you. Microwave softens texture quickly for a same-day gentle option."
        ),
        "myths": [
            ("An apple a day fixes IBD.", "Fruit supports nutrition; it does not replace biologics or other prescribed therapy."),
            ("All apples are high FODMAP forever.", "Serving size and variety matter in low-FODMAP frameworks; work with a dietitian."),
            ("Applesauce is only for kids.", "Adults use it during flares as a soft carbohydrate source when approved."),
        ],
        "questions": [
            "Should I peel and cook apples while calprotectin or symptoms are elevated?",
            "Is commercial applesauce okay with my FODMAP or low-residue plan?",
            "When can I reintroduce raw apple skin?",
        ],
        "related": [
            ("/blog/fodmap-diet-crohns-colitis", "FODMAP and IBD"),
            ("/blog/low-residue-diet-flare", "low-residue diet"),
            ("/blog/best-foods-crohns-flare", "foods during a Crohn's flare"),
        ],
    },
    {
        "slug": "blueberries-ibd",
        "name": "Blueberries",
        "title": "Blueberries and IBD: Antioxidants, Seeds, and Gut Tolerance",
        "description": "Blueberries with Crohn's or colitis: fiber, polyphenols, seed tips, cooked vs raw, and dietitian questions. Education only.",
        "category": "Nutrition · August 2026",
        "date_display": "August 21, 2026",
        "date_iso": "2026-08-21T16:00:00Z",
        "asset_dir": "blueberries-ibd",
        "resource_category": "nutrition",
        "tags": [
            "blueberries", "berries", "antioxidants", "polyphenols", "fruit", "fiber",
            "Crohn's", "colitis", "nutrition",
        ],
        "share": "Blueberries and IBD: tolerance and nutrition tips. Education only.",
        "primary_kw": "blueberries Crohn's disease",
        "secondary_kw": "blueberries ulcerative colitis",
        "nutrition_intro": (
            "Blueberries are popular for vitamin C, fiber, and polyphenol antioxidants. They are small, "
            "which helps portion control, but tiny seeds and skins still add residue that some people notice during flares."
        ),
        "macros": [
            ("Serving", "1/2 cup (~75 g)"),
            ("Calories", "~40"),
            ("Carbohydrate", "~11 g"),
            ("Fiber", "~2 g"),
            ("Protein", "~0.5 g"),
            ("Fat", "~0.2 g"),
        ],
        "micros": [
            ("Vitamin C and K", "Support everyday nutrition when intake is varied"),
            ("Manganese", "Trace mineral found in berries and grains"),
            ("Polyphenols", "Studied for general health; not an IBD cure"),
        ],
        "tolerance_intro": (
            "In remission, small servings of fresh or frozen blueberries are often well liked. "
            "During flares, cooked, mashed, or strained berry puree may feel easier than a full cup of raw berries."
        ),
        "flare_tips": [
            "Start with 2 to 4 tablespoons, not a large bowl",
            "Try warmed, lightly mashed berries over white rice or yogurt if dairy works",
            "Avoid dried blueberries if concentrated fiber and sugar spike symptoms",
            "Skip berry skins mixed into rough smoothies if seeds bother you",
        ],
        "remission_tips": [
            "Add to oatmeal or cottage cheese for protein plus produce",
            "Frozen berries work in cooked compotes year-round",
            "Rotate with melon or banana so berry fiber stays moderate",
        ],
        "prep": (
            "Simmer frozen blueberries briefly until soft, then mash. Strain if your team wants lower residue. "
            "Rinse fresh berries well. Do not assume organic status changes IBD tolerance."
        ),
        "myths": [
            ("Antioxidant berries heal Crohn's.", "Helpful foods support health; they do not replace medical therapy."),
            ("All seeds are forbidden forever.", "Many people reintroduce small seeded fruits in remission with guidance."),
            ("Blueberry supplements equal eating berries.", "Pills are not the same as food and may not be studied in IBD."),
        ],
        "questions": [
            "Are small-seeded berries okay with my stricture history?",
            "Should I cook berries while on a low-residue plan?",
            "How do blueberries fit my fiber goals in remission?",
        ],
        "related": [
            ("/blog/fiber-and-ibd-diet", "fiber and IBD"),
            ("/blog/anti-inflammatory-diet-ibd", "anti-inflammatory diet patterns"),
            ("/blog/complete-ibd-nutrition-guide", "complete IBD nutrition guide"),
        ],
    },
    {
        "slug": "strawberries-ibd",
        "name": "Strawberries",
        "title": "Strawberries and IBD: Vitamin C, Seeds, and Flare-Friendly Servings",
        "description": "Strawberries with Crohn's or colitis: vitamin C, fiber, seeds, portion tips, and clinic questions. Education only.",
        "category": "Nutrition · August 2026",
        "date_display": "August 21, 2026",
        "date_iso": "2026-08-21T18:00:00Z",
        "asset_dir": "strawberries-ibd",
        "resource_category": "nutrition",
        "tags": [
            "strawberries", "strawberry", "vitamin C", "berries", "fruit", "fiber",
            "Crohn's", "colitis", "nutrition",
        ],
        "share": "Strawberries and IBD: vitamin C and tolerance tips. Education only.",
        "primary_kw": "strawberries Crohn's",
        "secondary_kw": "strawberries colitis diet",
        "nutrition_intro": (
            "Strawberries deliver vitamin C, folate, and fiber with relatively few calories. "
            "Surface seeds and acidity bother some people more than the fruit's sugar content alone."
        ),
        "macros": [
            ("Serving", "1/2 cup sliced (~80 g)"),
            ("Calories", "~25 to 30"),
            ("Carbohydrate", "~6 g"),
            ("Fiber", "~1.5 g"),
            ("Protein", "~0.5 g"),
            ("Fat", "negligible"),
        ],
        "micros": [
            ("Vitamin C", "High for the calorie count; useful when produce intake is low"),
            ("Folate", "Supports blood cell health alongside other folate foods"),
            ("Manganese and potassium", "Small contributions to daily needs"),
        ],
        "tolerance_intro": (
            "Ripe strawberries that are soft and well rinsed may sit better than underripe, acidic berries. "
            "People with mouth sores sometimes prefer cooked or non-acidic fruits temporarily."
        ),
        "flare_tips": [
            "Try a few soft berries or cooked strawberry puree rather than a large raw serving",
            "Avoid strawberry seeds mixed into crunchy toppings if residue is restricted",
            "Watch syrupy desserts; added sugar alcohols can worsen diarrhea",
            "If acidity stings, switch to banana or melon until mouth and gut calm",
        ],
        "remission_tips": [
            "Pair with Greek yogurt or eggs for a more balanced snack",
            "Use in smoothies blended smooth if texture is the main issue",
            "Keep portions modest when stacking multiple high-fiber fruits the same day",
        ],
        "prep": (
            "Hull, rinse, and slice thinly. Lightly stew with a splash of water until soft. "
            "Strain for a seed-reduced sauce if your dietitian suggests lower residue."
        ),
        "myths": [
            ("Vitamin C foods cause flares.", "Evidence does not support blaming strawberries alone for Crohn's flares."),
            ("You must peel strawberries.", "There is no peel like an apple; seed and acidity tolerance matter more."),
            ("Frozen strawberries are worse.", "Frozen fruit is nutritionally similar; cooking still softens texture."),
        ],
        "questions": [
            "Do oral ulcers mean I should pause acidic fruits?",
            "Are strawberries allowed on my current low-residue instructions?",
            "How should I reintroduce berries after a flare?",
        ],
        "related": [
            ("/blog/oral-canker-sores-ibd", "oral sores and IBD"),
            ("/blog/micronutrients-ibd-deficiencies", "micronutrient deficiencies"),
            ("/blog/foods-that-may-trigger-uc-symptoms", "UC food trigger education"),
        ],
    },
    {
        "slug": "melon-ibd",
        "name": "Melon",
        "title": "Melon and IBD: Hydration, Potassium, and Gentle Fruit Options",
        "description": "Cantaloupe, honeydew, and watermelon with Crohn's or colitis: fluids, potassium, FODMAP notes, and flare tips. Education only.",
        "category": "Nutrition · August 2026",
        "date_display": "August 22, 2026",
        "date_iso": "2026-08-22T12:00:00Z",
        "asset_dir": "melon-ibd",
        "resource_category": "nutrition",
        "tags": [
            "melon", "watermelon", "cantaloupe", "honeydew", "hydration", "potassium",
            "fruit", "Crohn's", "colitis", "nutrition",
        ],
        "share": "Melon and IBD: hydration and gentle fruit tips. Education only.",
        "primary_kw": "watermelon Crohn's disease",
        "secondary_kw": "cantaloupe colitis",
        "nutrition_intro": (
            "Melons are mostly water, which supports hydration, with carbohydrate, potassium, and vitamin A or C "
            "depending on the type. They are often listed among softer fruits for people rebuilding a gentle menu."
        ),
        "macros": [
            ("Serving", "1 cup diced (~150 to 160 g)"),
            ("Calories", "~45 to 60 depending on type"),
            ("Carbohydrate", "~11 to 15 g"),
            ("Fiber", "~1 to 1.5 g"),
            ("Protein", "~1 g"),
            ("Fat", "negligible"),
        ],
        "micros": [
            ("Potassium", "Helpful when replacing stool losses; check labs if you have kidney disease"),
            ("Vitamin A (cantaloupe)", "Supports vision and epithelial health in overall diets"),
            ("Vitamin C (many melons)", "Adds to daily produce intake"),
            ("Lycopene (watermelon)", "A carotenoid studied in general nutrition, not an IBD drug"),
        ],
        "tolerance_intro": (
            "Seedless, ripe melon without rind is usually the form people try first. "
            "Large servings of watermelon can be high FODMAP for some; smaller portions may fit better during elimination phases."
        ),
        "flare_tips": [
            "Choose ripe, soft cubes without seeds or rind",
            "Start with 1/2 cup and watch bloating",
            "Use melon as a hydrating snack between broth and oral rehydration fluids",
            "Avoid overly firm underripe melon that feels fibrous",
        ],
        "remission_tips": [
            "Rotate cantaloupe, honeydew, and watermelon for variety",
            "Pair with turkey or cottage cheese for protein",
            "Keep chilled melon ready for low-appetite days",
        ],
        "prep": (
            "Cut away rind completely. Remove seeds. Chill for easier swallowing when nausea is present. "
            "Blend into a smooth slush with water if chewing feels tiring."
        ),
        "myths": [
            ("Watermelon is only sugar and bad for IBD.", "It also provides fluid and potassium; portion still matters."),
            ("Melon causes Crohn's.", "No fruit has been shown to cause IBD."),
            ("You must avoid melon on every IBD diet.", "Many remission and gentle menus include it."),
        ],
        "questions": [
            "What melon portion fits my FODMAP or low-residue plan?",
            "Should I use melon to help with fluid goals during diarrhea?",
            "Any potassium limits based on my labs or medications?",
        ],
        "related": [
            ("/blog/hydration-tips-ibd", "hydration tips"),
            ("/blog/electrolytes-flare-ibd", "electrolytes and flares"),
            ("/blog/fodmap-diet-crohns-colitis", "FODMAP diet overview"),
        ],
    },
    {
        "slug": "avocado-ibd",
        "name": "Avocado",
        "title": "Avocado and IBD: Healthy Fats, Fiber, and Portion Tips",
        "description": "Avocado with Crohn's or colitis: monounsaturated fat, fiber, FODMAP portions, mash tips, and clinic questions. Education only.",
        "category": "Nutrition · August 2026",
        "date_display": "August 22, 2026",
        "date_iso": "2026-08-22T14:00:00Z",
        "asset_dir": "avocado-ibd",
        "resource_category": "nutrition",
        "tags": [
            "avocado", "healthy fats", "fiber", "potassium", "FODMAP", "fruit",
            "Crohn's", "colitis", "nutrition",
        ],
        "share": "Avocado and IBD: fats, fiber, and portions. Education only.",
        "primary_kw": "avocado Crohn's disease",
        "secondary_kw": "avocado ulcerative colitis",
        "nutrition_intro": (
            "Avocado is a fruit rich in monounsaturated fat, fiber, potassium, and folate. "
            "Fat can slow digestion in helpful ways for some people, yet larger fatty meals can worsen urgency in others."
        ),
        "macros": [
            ("Serving", "1/3 medium avocado (~50 g edible)"),
            ("Calories", "~80"),
            ("Fat", "~7 to 8 g (mostly monounsaturated)"),
            ("Carbohydrate", "~4 g"),
            ("Fiber", "~3 g"),
            ("Protein", "~1 g"),
        ],
        "micros": [
            ("Potassium", "Notable for the serving size"),
            ("Folate", "Supports pregnancy planning and blood health in broader diets"),
            ("Vitamin E and K", "Fat-soluble nutrients that come with the fruit's oils"),
            ("Magnesium", "Small helpful amount"),
        ],
        "tolerance_intro": (
            "Many IBD diet patterns allow small avocado portions. Low-FODMAP guidance often uses limited serving sizes "
            "because larger amounts of avocado polyols can trigger IBS-like symptoms that overlap with IBD."
        ),
        "flare_tips": [
            "Mash 1 to 2 tablespoons into white toast or rice rather than a whole avocado",
            "Avoid large guacamole servings with onion and chips during flares",
            "If fat worsens urgency, pause and retry later with your dietitian",
            "Choose ripe, smooth mash over firm chunks",
        ],
        "remission_tips": [
            "Build toward 1/3 avocado with eggs or turkey for a balanced plate",
            "Use as a dairy-free creaminess swap in sauces if tolerated",
            "Track whether larger fatty meals change stool form",
        ],
        "prep": (
            "Mash thoroughly to reduce chunky residue. Squeeze lemon only if acidity is tolerated. "
            "Store leftovers cold with plastic against the surface to limit browning."
        ),
        "myths": [
            ("All fats are bad in IBD.", "Some fat supports calories and nutrient absorption; type and amount matter."),
            ("Avocado detoxes the gut.", "No food detoxes Crohn's or colitis."),
            ("You must eat a whole avocado daily.", "Smaller servings are often smarter while testing tolerance."),
        ],
        "questions": [
            "What avocado portion fits my FODMAP or calorie goals?",
            "Does fat malabsorption mean I should limit avocado?",
            "How can avocado help if I am underweight in remission?",
        ],
        "related": [
            ("/blog/fodmap-diet-crohns-colitis", "FODMAP and IBD"),
            ("/blog/protein-meal-plan-ibd-remission", "protein meal ideas"),
            ("/blog/mediterranean-diet-autoimmune", "Mediterranean-style patterns"),
        ],
    },
    {
        "slug": "oranges-citrus-ibd",
        "name": "Oranges and citrus",
        "title": "Oranges and Citrus With IBD: Vitamin C, Acidity, and Juice Tips",
        "description": "Oranges, citrus, and IBD: vitamin C, acidity, juice vs whole fruit, flare cautions, and dietitian questions. Education only.",
        "category": "Nutrition · August 2026",
        "date_display": "August 22, 2026",
        "date_iso": "2026-08-22T16:00:00Z",
        "asset_dir": "oranges-ibd",
        "resource_category": "nutrition",
        "tags": [
            "orange", "oranges", "citrus", "vitamin C", "juice", "fruit",
            "Crohn's", "colitis", "nutrition", "acidity",
        ],
        "share": "Oranges and citrus with IBD: vitamin C and acidity tips. Education only.",
        "primary_kw": "oranges Crohn's disease",
        "secondary_kw": "orange juice colitis",
        "nutrition_intro": (
            "Oranges are known for vitamin C and folate, with fiber in the whole fruit and membranes. "
            "Acidity and concentrated juice are the usual reasons some people with IBD limit citrus during flares."
        ),
        "macros": [
            ("Serving", "1 medium orange (~130 g) or 4 oz juice"),
            ("Calories", "~60 (fruit) / ~55 (4 oz juice)"),
            ("Carbohydrate", "~15 g fruit"),
            ("Fiber", "~3 g whole fruit; little in juice"),
            ("Protein", "~1 g"),
            ("Fat", "negligible"),
        ],
        "micros": [
            ("Vitamin C", "High; supports collagen and immune roles in general nutrition"),
            ("Folate", "Present in orange fruit and juice"),
            ("Potassium", "Helpful electrolyte contribution"),
            ("Calcium (fortified juice only)", "Check labels; not inherent to all orange juice"),
        ],
        "tolerance_intro": (
            "Whole peeled orange segments without tough membranes may feel different from acidic juice on an empty stomach. "
            "People with reflux, mouth sores, or raw rectal irritation sometimes pause citrus until symptoms settle."
        ),
        "flare_tips": [
            "Prefer small amounts of peeled fruit over large glasses of juice",
            "Dilute juice with water if your team still wants vitamin C from citrus",
            "Avoid peel zest and bitter pith if residue is restricted",
            "Switch to melon or banana if burning or urgency follows citrus",
        ],
        "remission_tips": [
            "Eat the fruit for fiber rather than juice-only habits",
            "Pair citrus with food, not on a completely empty stomach, if reflux is an issue",
            "Rotate vitamin C sources (strawberries, peppers if tolerated) so one acid source does not dominate",
        ],
        "prep": (
            "Peel fully, remove obvious pith, and separate soft segments. Mandarin cups without added syrup can be a "
            "soft option. Fresh squeeze is more acidic than some expect; sip slowly with meals."
        ),
        "myths": [
            ("Vitamin C causes IBD flares.", "Citrus acidity can irritate some people; vitamin C itself is not a proven flare trigger for everyone."),
            ("Juice is healthier than fruit.", "Juice drops fiber and raises how quickly sugar hits the gut."),
            ("All citrus is banned forever.", "Many patients return to small servings in remission."),
        ],
        "questions": [
            "Should I pause citrus while I have mouth sores or severe urgency?",
            "Is fortified orange juice a reasonable calcium source for me?",
            "How do we cover vitamin C if I avoid citrus?",
        ],
        "related": [
            ("/blog/oral-canker-sores-ibd", "mouth sores"),
            ("/blog/micronutrients-ibd-deficiencies", "micronutrients"),
            ("/blog/iron-b12-vitamin-d-ibd", "iron, B12, and vitamin D"),
        ],
    },
    {
        "slug": "grapes-ibd",
        "name": "Grapes",
        "title": "Grapes and IBD: Skins, Portions, and Gentle Fruit Swaps",
        "description": "Grapes with Crohn's or colitis: skins, sugar, portions, peeled or cooked options, and clinic questions. Education only.",
        "category": "Nutrition · August 2026",
        "date_display": "August 22, 2026",
        "date_iso": "2026-08-22T18:00:00Z",
        "asset_dir": "grapes-ibd",
        "resource_category": "nutrition",
        "tags": [
            "grapes", "grape", "fruit", "skins", "fiber", "Crohn's", "colitis", "nutrition",
        ],
        "share": "Grapes and IBD: skins, portions, and swaps. Education only.",
        "primary_kw": "grapes Crohn's disease",
        "secondary_kw": "grapes ulcerative colitis diet",
        "nutrition_intro": (
            "Grapes offer quick carbohydrate, water, and small amounts of vitamin K and copper. "
            "Skins and seeds (in seeded varieties) are the main texture concerns for flare or stricture plans."
        ),
        "macros": [
            ("Serving", "1/2 cup (~75 g)"),
            ("Calories", "~50"),
            ("Carbohydrate", "~14 g"),
            ("Fiber", "~0.5 to 1 g"),
            ("Protein", "~0.5 g"),
            ("Fat", "negligible"),
        ],
        "micros": [
            ("Vitamin K", "Small amount; relevant if you take warfarin (ask your clinician about consistency)"),
            ("Copper and potassium", "Modest contributions"),
            ("Polyphenols in skins", "General nutrition interest; not IBD therapy"),
        ],
        "tolerance_intro": (
            "Seedless grapes that are peeled or cooked appear more often on gentle menus than whole raw bunches. "
            "Raisins are concentrated and higher residue for some people despite being the same fruit."
        ),
        "flare_tips": [
            "Try a few peeled grapes or cooked grape compote instead of a large raw cluster",
            "Choose seedless varieties",
            "Avoid raisins and grape skins in trail mixes during low-residue phases",
            "Watch juice: low fiber, quick sugar, possible urgency",
        ],
        "remission_tips": [
            "Wash well and chew thoroughly",
            "Keep servings to a small handful when testing tolerance",
            "Pair with protein so the snack is not only sugar",
        ],
        "prep": (
            "Slice in half and peel if skins bother you. Simmer into a soft sauce over rice or yogurt. "
            "Frozen grapes as a snack work for some in remission; they are still skins-on."
        ),
        "myths": [
            ("Grape detox cleanses heal colitis.", "Detox claims are marketing, not IBD care."),
            ("Raisins are always safer than grapes.", "Dried fruit is denser and can be harder during flares."),
            ("Red grapes are inflammatory.", "Color alone does not dictate IBD flares."),
        ],
        "questions": [
            "Are grape skins restricted on my low-residue plan?",
            "How do grapes fit if I also have IBS overlap?",
            "Should I avoid raisins after surgery or with strictures?",
        ],
        "related": [
            ("/blog/low-residue-diet-flare", "low-residue diet"),
            ("/blog/fiber-and-ibd-diet", "fiber guide"),
            ("/blog/dining-out-ibd-restaurants", "dining out with IBD"),
        ],
    },
    {
        "slug": "chicken-protein-ibd",
        "name": "Chicken",
        "title": "Chicken and IBD: Lean Protein for Flares and Remission Plates",
        "description": "Chicken with Crohn's or colitis: protein for healing, tender cooking methods, skin and frying cautions, meal ideas. Education only.",
        "category": "Nutrition · August 2026",
        "date_display": "August 23, 2026",
        "date_iso": "2026-08-23T12:00:00Z",
        "asset_dir": "chicken-ibd",
        "resource_category": "nutrition",
        "tags": [
            "chicken", "poultry", "protein", "lean meat", "flare food", "Crohn's",
            "colitis", "nutrition", "macros",
        ],
        "share": "Chicken and IBD: lean protein tips for flares and remission. Education only.",
        "primary_kw": "chicken Crohn's disease diet",
        "secondary_kw": "chicken ulcerative colitis protein",
        "nutrition_intro": (
            "Chicken is a lean animal protein many IBD care teams suggest when appetite is low and healing needs are high. "
            "Protein supports tissue repair and helps preserve muscle when inflammation raises needs."
        ),
        "macros": [
            ("Serving", "3 oz cooked chicken breast (~85 g)"),
            ("Calories", "~120 to 140"),
            ("Protein", "~25 to 27 g"),
            ("Fat", "~2 to 3 g (skinless breast); higher with skin or thigh"),
            ("Carbohydrate", "0 g"),
            ("Fiber", "0 g"),
        ],
        "micros": [
            ("Niacin and B6", "Support energy metabolism"),
            ("Selenium and phosphorus", "Present in poultry"),
            ("Iron", "Less than red meat but still contributes"),
            ("Sodium", "Watch injected or heavily seasoned products if swelling or blood pressure is a concern"),
        ],
        "tolerance_intro": (
            "Tender, moist, skinless cuts are usually easier than fried, heavily spiced, or charred chicken. "
            "Tough, dry meat can feel hard to digest when the gut is raw."
        ),
        "flare_tips": [
            "Poach, bake, or slow-cook skinless breast or tender thigh; shred finely",
            "Serve with white rice or peeled potato rather than fried sides",
            "Skip crispy skin, spicy rubs, and deep frying during high urgency weeks",
            "Use broth-based soups with shredded chicken for easy calories",
        ],
        "remission_tips": [
            "Rotate breast and thigh based on calorie needs",
            "Batch-cook for weeknight protein when fatigue is high",
            "Add herbs your gut tolerates instead of heavy chili heat if spice is a trigger",
        ],
        "prep": (
            "Cook to a safe internal temperature, then rest and slice thin against the grain. "
            "Moisten leftovers with broth so reheated chicken does not dry out. Rotisserie chicken can work if you remove skin and heavy seasoning."
        ),
        "myths": [
            ("You must go vegetarian with IBD.", "Many patients do well with lean poultry; choose based on labs and values."),
            ("Chicken causes inflammation.", "Plain chicken is not a proven IBD trigger; sauces and frying often matter more."),
            ("Only protein shakes count during flares.", "Soft chicken and eggs are whole-food options when chewing and appetite allow."),
        ],
        "questions": [
            "What daily protein target fits my weight and flare status?",
            "Is deli chicken okay, or should I stick to fresh cooked?",
            "How do we combine food protein with oral nutrition supplements if needed?",
        ],
        "related": [
            ("/guides/protein-healing-ibd-flare", "protein during flares"),
            ("/blog/protein-meal-plan-ibd-remission", "high-protein meal ideas"),
            ("/blog/best-foods-crohns-flare", "flare food ideas"),
        ],
    },
    {
        "slug": "eggs-ibd-nutrition",
        "name": "Eggs",
        "title": "Eggs and IBD: Protein, Choline, and Easy Flare Meals",
        "description": "Eggs with Crohn's or colitis: protein, choline, scrambled vs fried, dairy-free prep, and dietitian questions. Education only.",
        "category": "Nutrition · August 2026",
        "date_display": "August 23, 2026",
        "date_iso": "2026-08-23T14:00:00Z",
        "asset_dir": "eggs-ibd",
        "resource_category": "nutrition",
        "tags": [
            "eggs", "egg", "protein", "choline", "breakfast", "flare food",
            "Crohn's", "colitis", "nutrition", "macros",
        ],
        "share": "Eggs and IBD: easy protein for flares and remission. Education only.",
        "primary_kw": "eggs Crohn's disease",
        "secondary_kw": "eggs ulcerative colitis diet",
        "nutrition_intro": (
            "Eggs are compact protein with choline, vitamin D (small amount), B12, and selenium. "
            "They cook quickly, which helps on low-energy days, and they fit many low-residue style patterns when prepared simply."
        ),
        "macros": [
            ("Serving", "2 large eggs"),
            ("Calories", "~140 to 160"),
            ("Protein", "~12 g"),
            ("Fat", "~10 g"),
            ("Carbohydrate", "~1 g"),
            ("Fiber", "0 g"),
        ],
        "micros": [
            ("Choline", "Important for cell membranes; eggs are a top food source"),
            ("Vitamin B12", "Helpful when animal foods are limited, though ileal disease still needs lab monitoring"),
            ("Selenium and iodine (varies)", "Depends on hen diet"),
            ("Vitamin D", "Modest; not a substitute for prescribed vitamin D therapy"),
        ],
        "tolerance_intro": (
            "Soft scrambled, poached, or baked eggs are common gentle choices. Greasy fried eggs with spicy sausage "
            "are more likely to bother people than the egg itself."
        ),
        "flare_tips": [
            "Scramble with a little oil or lactose-free milk if dairy is tolerated; keep texture soft",
            "Avoid chili sauces, large amounts of cheese, and fried sides during bad weeks",
            "Egg drop style broth can deliver protein when solid food is hard",
            "If fat is an issue, try more egg white with one yolk, then adjust with your dietitian",
        ],
        "remission_tips": [
            "Hard-boil a batch for snacks with white toast or fruit you tolerate",
            "Use eggs in fried rice made with white rice and tender vegetables",
            "Include eggs in higher-calorie plates if weight gain is a goal",
        ],
        "prep": (
            "Cook until whites are set for food safety. For softer digestion, avoid crispy browned edges. "
            "Store hard-boiled eggs peeled or unpeeled in the fridge for grab-and-go protein."
        ),
        "myths": [
            ("Eggs raise cholesterol so IBD patients must quit them.", "Dietary cholesterol advice is individualized; ask your clinician."),
            ("Eggs cause Crohn's.", "No evidence that eggs cause IBD."),
            ("Only egg whites are safe.", "Whole eggs are fine for many people; fat tolerance varies."),
        ],
        "questions": [
            "How many eggs fit my protein and heart-health goals?",
            "Are eggs okay with my bile acid or fat malabsorption issues?",
            "Should I prefer fortified eggs for vitamin D?",
        ],
        "related": [
            ("/guides/protein-healing-ibd-flare", "protein in flares"),
            ("/blog/teen-nutrition-ibd-growth", "teen nutrition"),
            ("/blog/how-ibdpal-nutrition-targets-work", "IBDPal nutrition targets"),
        ],
    },
    {
        "slug": "white-rice-ibd-flare",
        "name": "White rice",
        "title": "White Rice and IBD: Flare Staple, Carbs, and Remission Upgrades",
        "description": "White rice with Crohn's or colitis: low-residue carbs, hydration cooking tips, brown rice timing, and clinic questions. Education only.",
        "category": "Nutrition · August 2026",
        "date_display": "August 23, 2026",
        "date_iso": "2026-08-23T16:00:00Z",
        "asset_dir": "white-rice-ibd",
        "resource_category": "nutrition",
        "tags": [
            "white rice", "rice", "carbohydrate", "low residue", "flare food",
            "Crohn's", "colitis", "nutrition", "macros",
        ],
        "share": "White rice and IBD: a practical flare carbohydrate. Education only.",
        "primary_kw": "white rice Crohn's flare",
        "secondary_kw": "rice ulcerative colitis diet",
        "nutrition_intro": (
            "White rice is a refined grain that is lower in fiber than brown rice, which is why it appears on many "
            "low-residue and flare menus. It mainly supplies carbohydrate energy with little fat or protein."
        ),
        "macros": [
            ("Serving", "1 cup cooked (~160 g)"),
            ("Calories", "~200"),
            ("Carbohydrate", "~45 g"),
            ("Fiber", "~0.5 to 1 g"),
            ("Protein", "~4 g"),
            ("Fat", "~0.5 g"),
        ],
        "micros": [
            ("Manganese and selenium", "Present in small amounts"),
            ("B vitamins (enriched rice)", "Check enriched labels for folate and iron dusting"),
            ("Sodium", "Plain rice is low unless cooked in salty broth or boxed mixes"),
            ("Resistant starch", "Cooled rice forms more; some people notice more gas"),
        ],
        "tolerance_intro": (
            "Soft, well-cooked white rice is one of the most searched gentle carbs for IBD flares. "
            "Brown rice, wild rice, and rice bran are higher fiber and usually wait until remission or dietitian clearance."
        ),
        "flare_tips": [
            "Cook until very soft; add extra water or broth for a porridge-like texture if needed",
            "Pair with shredded chicken, eggs, or smooth peanut butter if approved",
            "Avoid fried rice loaded with oil, chili, and raw vegetables during flares",
            "Use plain rice water or thin rice porridge when appetite is poor (ask your team about fluids and electrolytes)",
        ],
        "remission_tips": [
            "Gradually trial brown rice if fiber goals increase",
            "Build bowls with tender proteins and peeled cooked vegetables",
            "Watch restaurant fried rice sodium and spice",
        ],
        "prep": (
            "Rinse if you prefer less surface starch. Simmer covered until grains mash easily between fingers. "
            "Reheat with a splash of water so leftovers stay moist. Instant white rice can work in a pinch; check sodium."
        ),
        "myths": [
            ("White rice is empty and useless.", "During flares it can be a practical energy source when fiber feels rough."),
            ("You must eat only rice forever.", "Long-term restriction without guidance risks nutrient gaps."),
            ("Brown rice is always better for IBD.", "Higher fiber is not always better during active inflammation or strictures."),
        ],
        "questions": [
            "How long should I stay on white rice before reintroducing whole grains?",
            "Does cooled rice (resistant starch) matter for my symptoms?",
            "How do we add protein so rice meals are more complete?",
        ],
        "related": [
            ("/blog/low-residue-diet-flare", "low-residue guide"),
            ("/blog/best-foods-crohns-flare", "flare foods"),
            ("/guides/low-residue-diet-ibd", "low-residue patient guide"),
        ],
    },
    {
        "slug": "turkey-protein-ibd",
        "name": "Turkey",
        "title": "Turkey and IBD: Lean Poultry Protein Beyond Chicken",
        "description": "Turkey with Crohn's or colitis: lean protein, deli vs fresh, flare cooking tips, and meal ideas. Education only.",
        "category": "Nutrition · August 2026",
        "date_display": "August 23, 2026",
        "date_iso": "2026-08-23T18:00:00Z",
        "asset_dir": "turkey-ibd",
        "resource_category": "nutrition",
        "tags": [
            "turkey", "poultry", "protein", "lean meat", "deli meat", "Crohn's",
            "colitis", "nutrition", "macros",
        ],
        "share": "Turkey and IBD: lean protein tips. Education only.",
        "primary_kw": "turkey Crohn's disease",
        "secondary_kw": "turkey ulcerative colitis protein",
        "nutrition_intro": (
            "Turkey is another lean poultry option that helps meet higher protein needs in IBD. "
            "Fresh roasted or ground turkey is usually gentler than spicy processed products, though low-sodium deli slices help some people on low-appetite days."
        ),
        "macros": [
            ("Serving", "3 oz cooked turkey breast (~85 g)"),
            ("Calories", "~120 to 135"),
            ("Protein", "~25 g"),
            ("Fat", "~1 to 3 g (skinless breast); higher in dark meat or processed products"),
            ("Carbohydrate", "0 g (plain)"),
            ("Sodium", "Low when fresh; can be high in deli meats"),
        ],
        "micros": [
            ("Selenium, B3, and B6", "Similar to other poultry"),
            ("Zinc", "Supports immune and repair roles in overall diets"),
            ("Iron", "Modest; still pair with iron strategy if anemic"),
            ("Phosphorus", "Present in muscle meats"),
        ],
        "tolerance_intro": (
            "Moist, simply seasoned turkey usually parallels chicken for tolerance. "
            "The bigger gaps are between fresh meat and highly processed, peppered, or fatty sausages labeled as turkey."
        ),
        "flare_tips": [
            "Roast or simmer ground turkey; drain excess fat; keep seasoning mild",
            "Shred into rice, broth, or mashed potato",
            "Choose low-sodium deli turkey without spicy pepper coating if using sandwich meat",
            "Skip turkey bacon and fried cutlets during high-symptom weeks if fat triggers urgency",
        ],
        "remission_tips": [
            "Alternate turkey and chicken so menus do not get boring",
            "Use lean ground turkey in soft meatballs or mild chili if beans are tolerated later",
            "Keep frozen turkey cutlets for easy protein on fatigue days",
        ],
        "prep": (
            "Cook ground turkey to a safe temperature and break into fine crumbles. "
            "For breast meat, slice thin and store with a little broth. Avoid drying out leftovers in the microwave without moisture."
        ),
        "myths": [
            ("Deli turkey is as clean as fresh roast.", "Sodium and additives differ widely; read labels."),
            ("Turkey is always low fat.", "Products vary; check packages and cooking methods."),
            ("Poultry must be avoided in autoimmune disease.", "Many IBD plans rely on poultry protein."),
        ],
        "questions": [
            "Is processed turkey okay for my blood pressure and sodium goals?",
            "What protein target should I hit on flare days?",
            "Can turkey help me meet needs if red meat worsens symptoms?",
        ],
        "related": [
            ("/blog/chicken-protein-ibd", "chicken and IBD"),
            ("/blog/protein-meal-plan-ibd-remission", "protein meal plans"),
            ("/guides/iron-deficiency-nutrition-ibd", "iron deficiency nutrition"),
        ],
    },
]


def build_posts() -> list[dict]:
    posts = []
    for f in FOODS:
        post = {
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
        posts.append(post)
    return posts


def download_image(url: str, dest: Path) -> bool:
    import ssl
    import urllib.request

    for ctx in (
        ssl.create_default_context(),
        ssl._create_unverified_context(),
    ):
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
        src = f'"/blog/{slug}"'
        if src in text:
            continue
        inserts.append(
            f'    {{\n      "source": "/blog/{slug}",\n'
            f'      "destination": "/blogs/{slug}.html"\n    }}'
        )
    if not inserts:
        return
    block = ",\n".join(inserts) + ",\n"
    text = text.replace('"rewrites": [\n', f'"rewrites": [\n{block}')
    VERCEL.write_text(text, encoding="utf-8")
    print("patched vercel.json (+", len(inserts), "rewrites)")


def patch_sitemap(slugs: list[str]) -> None:
    today = date.today().isoformat()
    text = SITEMAP.read_text(encoding="utf-8")
    marker = "<!-- wave1-food-nutrition-blogs -->"
    if marker in text:
        text = re.sub(
            rf"\n  {re.escape(marker)}.*?(?=\n  <!-- |\n</urlset>)",
            "",
            text,
            flags=re.DOTALL,
        )
    entries = []
    for slug in slugs:
        entries.append(
            f"  <url>\n    <loc>{SITE}/blog/{slug}</loc>\n    <lastmod>{today}</lastmod>\n"
            f"    <changefreq>monthly</changefreq>\n    <priority>0.85</priority>\n  </url>"
        )
    block = f"  {marker}\n" + "\n".join(entries)
    for anchor in ("  <!-- seo-wellness-blogs -->", "  <!-- ibd-topic-blogs -->", "  <!-- tier3-seo -->"):
        if anchor in text:
            text = text.replace(anchor, block + "\n" + anchor)
            break
    else:
        text = text.replace("</urlset>", block + "\n</urlset>")
    SITEMAP.write_text(text, encoding="utf-8")
    print("patched sitemap.xml (+", len(slugs), "urls)")


def write_data(posts: list[dict]) -> None:
    DATA.parent.mkdir(parents=True, exist_ok=True)
    payload = {"wave": 1, "theme": "food-nutrition", "posts": posts}
    DATA.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("wrote", DATA.relative_to(ROOT))


def main() -> None:
    posts = build_posts()
    write_data(posts)
    slugs = write_blogs(posts)
    patch_vercel(slugs)
    patch_sitemap(slugs)
    print("Done.", len(slugs), "Wave 1 food posts.")
    print("Next: amp + sync_resources + sync_llms")


if __name__ == "__main__":
    main()
