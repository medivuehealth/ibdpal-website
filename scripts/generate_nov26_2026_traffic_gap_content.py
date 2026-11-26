#!/usr/bin/env python3
# Prose style: do not use em dash.
"""Nov 26 2026 traffic-gap content: food micros, turmeric, OTC symptom helpers,
CBD/cannabis, autism+IBD, plus /foods-ibd Can I eat X hub."""
from __future__ import annotations

import json
import re
import shutil
import ssl
import sys
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOGS = ROOT / "blogs"
SEARCH_GAP = ROOT / "data" / "search-gap-posts.json"
ALIASES = ROOT / "data" / "search-aliases.json"
SEO = ROOT / "data" / "seo-expansion.json"
VERCEL = ROOT / "vercel.json"
SITEMAP = ROOT / "sitemap.xml"
FALLBACK = BLOGS / "assets" / "low-residue" / "low-residue_1.jpg"
SITE = "https://www.ibdpal.org"

sys.path.insert(0, str(ROOT / "scripts"))
from generate_blog_posts import render_post  # noqa: E402

DATE_ISO = "2026-11-26T18:30:00Z"
DATE_DISPLAY = "November 26, 2026"
MIN_WORDS_TOPIC = 850

IMAGE_URLS = {
    "pineapple-ibd": "https://images.unsplash.com/photo-1550258987-190a2d41a8ba?auto=format&w=1200&q=80",
    "quinoa-ibd": "https://images.unsplash.com/photo-1586201375761-83865001e31c?auto=format&w=1200&q=80",
    "honey-sweeteners-ibd": "https://images.unsplash.com/photo-1558642452-9d2a7deb7f62?auto=format&w=1200&q=80",
    "plant-milks-ibd": "https://images.unsplash.com/photo-1563636619-e9143da7973b?auto=format&w=1200&q=80",
    "popcorn-ibd": "https://images.unsplash.com/photo-1578849278619-e73505e9610f?auto=format&w=1200&q=80",
    "chickpeas-hummus-ibd": "https://images.unsplash.com/photo-1599599810694-b5b37304c041?auto=format&w=1200&q=80",
    "turmeric-curcumin-ibd": "https://images.unsplash.com/photo-1615485290382-441e4d049cb5?auto=format&w=1200&q=80",
    "loperamide-antispasmodics-ibd": "https://images.unsplash.com/photo-1584308666744-24d5c474f2ae?auto=format&w=1200&q=80",
    "cbd-cannabis-ibd": "https://images.unsplash.com/photo-1536663815808-595e952ba54f?auto=format&w=1200&q=80",
    "autism-ibd-connection": "https://images.unsplash.com/photo-1503454537195-1dcabb73ffb9?auto=format&w=1200&q=80",
    "adalimumab-vs-ustekinumab-ibd": "https://images.unsplash.com/photo-1587854692152-cbe660dbde88?auto=format&w=1200&q=80",
}


def word_count(html_body: str) -> int:
    text = html_body
    for tag in ("</p>", "</li>", "</h2>", "</h3>"):
        text = text.replace(tag, " ")
    out = []
    in_tag = False
    for ch in text:
        if ch == "<":
            in_tag = True
            continue
        if ch == ">":
            in_tag = False
            continue
        if not in_tag:
            out.append(ch)
    return len("".join(out).split())


def download_image(url: str, dest: Path) -> bool:
    for ctx in (ssl.create_default_context(), ssl._create_unverified_context()):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "IBDPalBot/1.0"})
            with urllib.request.urlopen(req, context=ctx, timeout=45) as resp:
                data = resp.read()
            if len(data) < 2000:
                return False
            dest.write_bytes(data)
            return True
        except Exception:
            continue
    return False


def ensure_image(post: dict) -> None:
    asset = BLOGS / "assets" / post["asset_dir"]
    asset.mkdir(parents=True, exist_ok=True)
    dest = asset / post["images"][0]
    if dest.exists() and dest.stat().st_size >= 2000:
        return
    url = IMAGE_URLS.get(post["asset_dir"])
    if url and download_image(url, dest):
        print("downloaded", dest.name)
        return
    if FALLBACK.exists():
        shutil.copy(FALLBACK, dest)
        print("fallback", dest.name)


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
<p>Browse more single-food guides in the <a href="/foods-ibd">Can I eat X? food hub</a>.</p>

<h2>Nutrition snapshot: {name}</h2>
<p>{f['nutrition_intro']}</p>
<h3>Approximate macros (typical serving)</h3>
<ul class="blog-list">{macros}</ul>
<p>Amounts vary by brand, ripeness, cooking method, and portion. Use a label or USDA FoodData Central for exact numbers, and IBDPal food logs to compare your portion to how you felt afterward.</p>
<h3>Micronutrients and extras people ask about</h3>
<ul class="blog-list">{micros}</ul>

<h2>Flare versus remission: how many people approach {name_l}</h2>
<p>{f['tolerance_intro']}</p>
<h3>During a flare (when your team wants gentler textures)</h3>
<ul class="blog-list">{flare}</ul>
<h3>In remission (when variety is usually easier)</h3>
<ul class="blog-list">{rem}</ul>
<p>If you have strictures, recent surgery, or a short bowel history, fiber, skins, seeds, and chunky textures may need a different plan. Follow your clinician, not a generic list.</p>

<h2>Prep ideas that often feel kinder</h2>
<p>{f['prep']}</p>

<h2>Common myths about {name_l} and IBD</h2>
<ul class="blog-list">{myths}</ul>

<h2>How to track {name_l} with IBDPal</h2>
<p>Log the form (fresh vs canned, cooked texture, sweetener type, brand), portion size, and symptoms for 24 to 48 hours. Patterns beat memory at clinic visits. See <a href="/blog/tracking-food-symptoms-ibdpal">tracking food and symptoms</a>.</p>

<h2>Questions for your gastroenterologist or dietitian</h2>
<ul class="blog-list">{questions}</ul>
<p>Bring your food log and recent labs so advice matches disease location, medicines, and nutrition gaps.</p>

<h2>When food questions become urgent</h2>
<p>Contact your care team promptly for severe pain, vomiting, inability to keep fluids down, heavy bleeding, fever, or rapid weight loss. See <a href="/flare-help">flare help</a> and <a href="/blog/when-to-go-er-ibd">when to go to the ER</a>.</p>

<p>Related reading: {related}. Hub: <a href="/foods-ibd">Can I eat X?</a> · <a href="/ibd-nutrition">IBD nutrition</a>.</p>
""".strip()


FOODS: list[dict] = [
    {
        "slug": "pineapple-ibd",
        "name": "Pineapple",
        "title": "Pineapple and IBD: Acid, Bromelain, and Flare Texture Tips",
        "description": "Pineapple with Crohn's or colitis: acidity, bromelain, canned vs fresh, flare tips, and dietitian questions. Education only.",
        "category": "Nutrition · November 2026",
        "resource_category": "nutrition",
        "tags": ["pineapple", "fruit", "bromelain", "acid", "Crohn's", "colitis", "nutrition"],
        "share": "Pineapple and IBD: acid and texture tips. Education only.",
        "primary_kw": "pineapple Crohn's disease",
        "secondary_kw": "pineapple ulcerative colitis",
        "nutrition_intro": (
            "Pineapple provides carbohydrate, vitamin C, manganese, and the enzyme mix often called bromelain. "
            "Fresh pineapple is acidic and fibrous. Canned pineapple in juice or light syrup is softer and sometimes better tolerated."
        ),
        "macros": [
            ("Serving", "1 cup chunks (~165 g)"),
            ("Calories", "~80"),
            ("Carbohydrate", "~22 g"),
            ("Fiber", "~2.3 g"),
            ("Protein", "~1 g"),
            ("Fat", "~0 g"),
        ],
        "micros": [
            ("Vitamin C", "High; supports general nutrition, not a flare cure"),
            ("Manganese", "Notable for a fruit serving"),
            ("Bromelain", "Enzyme activity people ask about; food amounts are not medicine doses"),
            ("Acidity", "Can bother reflux or rectal urgency in some people"),
        ],
        "tolerance_intro": (
            "Many people tolerate small portions of ripe or canned pineapple better than large acidic servings on an empty stomach. "
            "During strict low-residue flares, fruit may be limited; reintroduction is individualized."
        ),
        "flare_tips": [
            "Prefer canned pineapple in juice, drained, in a small portion",
            "Blend into a smoothie with banana if chunks feel sharp",
            "Avoid pineapple on an empty stomach if acid triggers urgency",
            "Skip dried pineapple with tough fibers and concentrated sugar if those bother you",
        ],
        "remission_tips": [
            "Trial fresh ripe pineapple in 1/2 cup servings",
            "Pair with a protein or carb buffer (yogurt alternative, rice)",
            "Watch juice concentrates; fiber-free juice can spike stools for some",
        ],
        "prep": (
            "Choose ripe fruit, remove the tough core, and cut small pieces. "
            "Cooking pineapple briefly in a stew softens fibers. Avoid grilling charred edges if smoke or spice toppings bother you."
        ),
        "myths": [
            ("Pineapple enzymes heal Crohn's.", "Food bromelain is not disease-modifying therapy."),
            ("All tropical fruit is banned.", "Tolerance is individual; portion and texture matter."),
            ("Canned fruit is always worse.", "Softer canned fruit is sometimes easier during recovery."),
        ],
        "questions": [
            "Where does pineapple fit on my current residue or FODMAP plan?",
            "Should I prefer canned or fresh while urgency is high?",
            "How do acid foods interact with my reflux or rectal symptoms?",
        ],
        "related": [
            ("/blog/mango-ibd-crohns-colitis", "mango"),
            ("/blog/banana-ibd-crohns-colitis", "bananas"),
            ("/blog/strawberries-ibd", "strawberries"),
            ("/blog/blueberries-ibd", "blueberries"),
        ],
        "match_terms": [
            "pineapple",
            "pineapple ibd",
            "pineapple crohn",
            "pineapple colitis",
            "bromelain ibd",
        ],
    },
    {
        "slug": "quinoa-ibd",
        "name": "Quinoa",
        "title": "Quinoa and IBD: Protein, Fiber, and Flare-Friendly Cooking",
        "description": "Quinoa with Crohn's or colitis: protein, fiber, rinsing, flare texture tips, and dietitian questions. Education only.",
        "category": "Nutrition · November 2026",
        "resource_category": "nutrition",
        "tags": ["quinoa", "grain", "protein", "fiber", "Crohn's", "colitis", "nutrition"],
        "share": "Quinoa and IBD: protein and fiber tips. Education only.",
        "primary_kw": "quinoa Crohn's disease",
        "secondary_kw": "quinoa ulcerative colitis",
        "nutrition_intro": (
            "Quinoa is a seed used like a grain. It offers complete plant protein, fiber, magnesium, and iron. "
            "Rinsing removes saponins that taste bitter. Well-cooked soft quinoa differs from undercooked crunchy grains."
        ),
        "macros": [
            ("Serving", "1 cup cooked (~185 g)"),
            ("Calories", "~220"),
            ("Carbohydrate", "~39 g"),
            ("Fiber", "~5 g"),
            ("Protein", "~8 g"),
            ("Fat", "~4 g"),
        ],
        "micros": [
            ("Iron and magnesium", "Useful plant sources when portions are adequate"),
            ("Complete protein", "Contains all essential amino acids in typical discussions"),
            ("Saponins", "Rinse before cooking to improve taste and comfort for some"),
        ],
        "tolerance_intro": (
            "During active flares with a low-residue plan, many teams prefer white rice or refined grains first. "
            "Quinoa often returns later when fiber goals expand. Soft, well-cooked portions beat dry, crunchy bowls."
        ),
        "flare_tips": [
            "Wait until your clinician clears higher-fiber grains",
            "If trialing, cook soft with extra water and start with 1/4 to 1/2 cup",
            "Blend into soups if whole grains feel scratchy",
            "Skip raw sprouted quinoa salads during strict residue limits",
        ],
        "remission_tips": [
            "Use as a rice swap for protein variety",
            "Pair with peeled cooked vegetables and tender proteins",
            "Watch large cold grain salads with raw onion, seeds, and skins",
        ],
        "prep": (
            "Rinse thoroughly. Simmer until grains look translucent and soft. "
            "Leftover quinoa reheated with broth is often gentler than dry refrigerated scoops."
        ),
        "myths": [
            ("Quinoa is always safe because it is gluten free.", "Gluten free does not equal low residue or low FODMAP for everyone."),
            ("All whole grains trigger flares.", "Many people reintroduce soft grains successfully under guidance."),
            ("Quinoa replaces biologic therapy.", "It is a food, not a medicine."),
        ],
        "questions": [
            "When can I reintroduce quinoa on my residue plan?",
            "Should I prefer white rice, oats, or quinoa first?",
            "How do we use quinoa toward protein goals without overdoing fiber?",
        ],
        "related": [
            ("/blog/oatmeal-ibd", "oatmeal"),
            ("/blog/white-rice-ibd-flare", "white rice"),
            ("/blog/couscous-ibd", "couscous"),
            ("/blog/fiber-and-ibd-diet", "fiber and IBD"),
        ],
        "match_terms": [
            "quinoa",
            "quinoa ibd",
            "quinoa crohn",
            "quinoa colitis",
        ],
    },
    {
        "slug": "honey-sweeteners-ibd",
        "name": "Honey and sweeteners",
        "title": "Honey, Stevia, and Sweeteners with IBD: What Patients Ask",
        "description": "Honey, stevia, and other sweeteners with Crohn's or colitis: FODMAP notes, sugar alcohols, portion tips, and clinic questions. Education only.",
        "category": "Nutrition · November 2026",
        "resource_category": "nutrition",
        "tags": ["honey", "stevia", "sweeteners", "sugar alcohols", "FODMAP", "Crohn's", "colitis"],
        "share": "Honey and sweeteners with IBD: practical tips. Education only.",
        "primary_kw": "honey Crohn's disease",
        "secondary_kw": "stevia ulcerative colitis",
        "nutrition_intro": (
            "Honey is mostly fructose and glucose. Stevia and monk fruit are non-nutritive sweeteners. "
            "Sugar alcohols (sorbitol, mannitol, xylitol, maltitol) in sugar-free products commonly cause gas, bloating, or diarrhea."
        ),
        "macros": [
            ("Honey serving", "1 tablespoon (~21 g)"),
            ("Calories (honey)", "~60"),
            ("Carbohydrate (honey)", "~17 g"),
            ("Stevia / monk fruit", "Negligible calories in pure forms"),
            ("Sugar-free candy", "Often high in sugar alcohols; GI effects vary"),
        ],
        "micros": [
            ("Fructose load", "Large honey servings can be high FODMAP for some"),
            ("Trace minerals in honey", "Not a meaningful micronutrient strategy"),
            ("Additive blends", "Stevia packets may include erythritol or fillers"),
        ],
        "tolerance_intro": (
            "Small amounts of honey in tea or cooking are different from large spoonfuls or sugar-free candy binges. "
            "If you follow a low-FODMAP trial, honey is often limited. Stevia is frequently better tolerated than polyols, but blends matter."
        ),
        "flare_tips": [
            "Skip sugar-free gums and candies with sorbitol or mannitol if diarrhea is active",
            "Use tiny honey amounts only if your team allows simple sugars",
            "Prefer plain stevia or monk fruit without polyol blends when testing",
            "Watch 'natural' syrups stacked on already sweet drinks",
        ],
        "remission_tips": [
            "Reintroduce honey in teaspoon amounts and log symptoms",
            "Read labels on protein bars and 'keto' desserts for sugar alcohols",
            "Keep total added sugar aligned with your dietitian's plan",
        ],
        "prep": (
            "Stir a teaspoon of honey into warm tea rather than eating it by the spoon. "
            "For baking, test recipes with half the usual sweetener and note stool changes for a day."
        ),
        "myths": [
            ("Honey heals the gut lining.", "It is a sugar source, not disease-modifying therapy."),
            ("All artificial sweeteners are identical.", "Polyols often differ from stevia or aspartame in GI effects."),
            ("Stevia is unsafe for every IBD patient.", "Many people use it; individual tolerance and product blends still matter."),
        ],
        "questions": [
            "Are honey or polyols restricted on my current diet plan?",
            "Which sweetener blends fit my FODMAP or diarrhea pattern?",
            "How should I read labels on sugar-free snacks?",
        ],
        "related": [
            ("/blog/chocolate-ibd", "chocolate"),
            ("/blog/fodmap-diet-crohns-colitis", "FODMAP"),
            ("/blog/tea-ibd", "tea"),
            ("/blog/seasonings-herbs-spices-ibd", "seasonings"),
        ],
        "match_terms": [
            "honey",
            "honey ibd",
            "stevia",
            "stevia ibd",
            "sweeteners ibd",
            "sugar alcohols ibd",
            "monk fruit ibd",
        ],
    },
    {
        "slug": "plant-milks-ibd",
        "name": "Plant milks",
        "title": "Oat Milk, Almond Milk, and Plant Milks with IBD",
        "description": "Oat milk, almond milk, and other plant milks with Crohn's or colitis: fiber, FODMAP, additives, and dietitian questions. Education only.",
        "category": "Nutrition · November 2026",
        "resource_category": "nutrition",
        "tags": ["oat milk", "almond milk", "plant milk", "dairy alternative", "Crohn's", "colitis"],
        "share": "Plant milks and IBD: oat vs almond tips. Education only.",
        "primary_kw": "oat milk Crohn's",
        "secondary_kw": "almond milk ulcerative colitis",
        "nutrition_intro": (
            "Plant milks vary widely. Almond milk is often lower calorie and lower protein. Oat milk is creamier with more carbohydrate and sometimes more fiber. "
            "Soy milk usually offers more protein. Fortified calcium and vitamin D matter if you avoid dairy."
        ),
        "macros": [
            ("Almond milk (unsweetened, 1 cup)", "~30 to 40 kcal, ~1 g protein"),
            ("Oat milk (original, 1 cup)", "~120 kcal, ~3 g protein, more carbs"),
            ("Soy milk (unsweetened, 1 cup)", "~80 kcal, ~7 g protein"),
            ("Added sugars", "Flavored cartons can add 10+ g sugar per cup"),
        ],
        "micros": [
            ("Calcium and vitamin D", "Choose fortified cartons if dairy-free"),
            ("Carrageenan / gums", "Some people feel better on simpler ingredient lists"),
            ("Oat fiber", "Can be gentle or gassy depending on the person and serving"),
        ],
        "tolerance_intro": (
            "Lactose-free dairy and plant milks are both options when lactose bothers you. "
            "Oat milk is not automatically low FODMAP in large servings. Almond milk may be easier in small amounts but is a poor protein source alone."
        ),
        "flare_tips": [
            "Choose unsweetened, simple-ingredient cartons",
            "Start with 1/2 cup in tea, coffee, or smooth cereals",
            "If gums bother you, trial brands without carrageenan",
            "Do not rely on almond milk alone for protein during weight loss",
        ],
        "remission_tips": [
            "Compare oat, soy, and lactose-free dairy for satiety and stools",
            "Use fortified soy or pea milks when protein goals are high",
            "Watch barista oat milks with extra oils if fatty meals trigger you",
        ],
        "prep": (
            "Shake cartons well. Warm gently rather than boiling if separation bothers you. "
            "In smoothies, pair plant milk with banana or protein powder your dietitian approves."
        ),
        "myths": [
            ("Plant milk is always healthier than dairy.", "Depends on protein, fortification, additives, and your tolerance."),
            ("Oat milk is low residue for everyone.", "Serving size and brand fiber differ."),
            ("Almond milk fixes inflammation.", "It is a beverage choice, not a biologic."),
        ],
        "questions": [
            "Which fortified milk alternative fits my calcium and protein targets?",
            "Should I avoid gums or carrageenan based on my symptoms?",
            "How do oat milk portions fit my FODMAP plan?",
        ],
        "related": [
            ("/blog/dairy-lactose-ibd", "dairy and lactose"),
            ("/blog/greek-yogurt-ibd", "Greek yogurt"),
            ("/blog/oatmeal-ibd", "oatmeal"),
            ("/blog/coffee-ibd", "coffee"),
        ],
        "match_terms": [
            "oat milk",
            "almond milk",
            "plant milk",
            "plant milks",
            "oat milk ibd",
            "almond milk ibd",
            "dairy alternative ibd",
        ],
    },
    {
        "slug": "popcorn-ibd",
        "name": "Popcorn",
        "title": "Popcorn and IBD: Hulls, Fiber, and Movie-Snack Reality",
        "description": "Popcorn with Crohn's or colitis: hulls, insoluble fiber, oil and salt loads, flare caution, and dietitian questions. Education only.",
        "category": "Nutrition · November 2026",
        "resource_category": "nutrition",
        "tags": ["popcorn", "snack", "fiber", "hulls", "Crohn's", "colitis"],
        "share": "Popcorn and IBD: hull and fiber caution. Education only.",
        "primary_kw": "popcorn Crohn's disease",
        "secondary_kw": "popcorn ulcerative colitis",
        "nutrition_intro": (
            "Air-popped popcorn is a whole-grain snack with insoluble fiber and corn hulls that can be sharp. "
            "Movie-theater popcorn adds fat, salt, and volume that change tolerance completely."
        ),
        "macros": [
            ("Serving", "3 cups air-popped (~24 g)"),
            ("Calories", "~90"),
            ("Carbohydrate", "~19 g"),
            ("Fiber", "~4 g (mostly insoluble)"),
            ("Protein", "~3 g"),
            ("Fat", "~1 g air-popped; much higher if oil-popped"),
        ],
        "micros": [
            ("Hulls", "Can irritate strictures or sensitive guts"),
            ("Salt load", "Large bags can worsen bloating perception and thirst"),
            ("Flavor coatings", "Cheese powders, chili, and artificial butter vary widely"),
        ],
        "tolerance_intro": (
            "Many IBD diet plans limit popcorn during flares or when strictures are a concern because of hulls and insoluble fiber. "
            "Remission trials should stay small and plain."
        ),
        "flare_tips": [
            "Usually skip popcorn during active flares or low-residue instructions",
            "Avoid kernels and unpopped bits entirely",
            "Do not use popcorn as a 'healthy' binge snack while urgent",
            "Choose softer snacks your team already cleared (crackers, ripe banana)",
        ],
        "remission_tips": [
            "Trial a small plain air-popped bowl if your clinician agrees",
            "Chew thoroughly; stop if pain or incomplete emptying sensations appear",
            "Skip heavy oil, caramel corn, and spicy coatings on first trials",
        ],
        "prep": (
            "Air-pop and sift out unpopped kernels. Season lightly. "
            "Microwave bags vary; check oil and artificial flavor lists."
        ),
        "myths": [
            ("Popcorn is always a safe whole grain.", "Hulls make it a special case in IBD."),
            ("If I tolerate corn tortillas I tolerate popcorn.", "Texture and hulls differ."),
            ("Air-popped means unlimited.", "Portion and fiber load still matter."),
        ],
        "questions": [
            "Do my imaging or stricture history make popcorn risky?",
            "When can I trial a small plain serving?",
            "What snacks are better while fiber is limited?",
        ],
        "related": [
            ("/blog/corn-ibd", "corn"),
            ("/blog/tortillas-ibd", "tortillas"),
            ("/blog/fiber-and-ibd-diet", "fiber"),
            ("/blog/low-residue-diet-flare", "low-residue flare diet"),
        ],
        "match_terms": [
            "popcorn",
            "popcorn ibd",
            "popcorn crohn",
            "popcorn colitis",
        ],
    },
    {
        "slug": "chickpeas-hummus-ibd",
        "name": "Chickpeas and hummus",
        "title": "Chickpeas and Hummus with IBD: Fiber, FODMAPs, and Prep Tips",
        "description": "Chickpeas and hummus with Crohn's or colitis: fiber, FODMAP notes, smooth hummus tips, and dietitian questions. Education only.",
        "category": "Nutrition · November 2026",
        "resource_category": "nutrition",
        "tags": ["chickpeas", "hummus", "legumes", "fiber", "FODMAP", "Crohn's", "colitis"],
        "share": "Chickpeas and hummus with IBD: practical tips. Education only.",
        "primary_kw": "hummus Crohn's disease",
        "secondary_kw": "chickpeas ulcerative colitis",
        "nutrition_intro": (
            "Chickpeas (garbanzo beans) provide plant protein, fiber, folate, and iron. Hummus blends chickpeas with tahini, oil, lemon, and garlic. "
            "Skins, portion size, and garlic/onion content drive many tolerance differences."
        ),
        "macros": [
            ("Chickpeas, 1/2 cup cooked", "~140 kcal, ~6 g fiber, ~7 g protein"),
            ("Hummus, 2 tablespoons", "~70 kcal; fiber and fat vary by brand"),
            ("Fat", "Higher in tahini-rich or oil-heavy dips"),
        ],
        "micros": [
            ("Folate and iron", "Helpful plant sources when portions are tolerated"),
            ("FODMAPs", "GOS in legumes; garlic/onion in classic hummus add load"),
            ("Skins", "Blending or peeling can change comfort"),
        ],
        "tolerance_intro": (
            "Whole chickpeas are often limited on low-residue or low-FODMAP plans. "
            "Small amounts of smooth hummus are sometimes tolerated earlier than a bean salad, especially if garlic is reduced."
        ),
        "flare_tips": [
            "Skip whole chickpeas during strict low-residue flares",
            "If allowed, try 1 tablespoon smooth hummus without raw veggie dippers",
            "Choose garlic-light or homemade versions when testing",
            "Avoid falafel and crunchy roasted chickpeas while urgent",
        ],
        "remission_tips": [
            "Increase bean portions slowly while logging gas and pain",
            "Rinse canned chickpeas; cook until very soft",
            "Pair hummus with soft bread or cucumber if raw crudites bother you",
        ],
        "prep": (
            "Blend hummus until silky. Some people peel chickpeas for a smoother dip. "
            "Lemon and spice levels can be lowered without losing the idea of the dish."
        ),
        "myths": [
            ("All legumes are forbidden forever in IBD.", "Many people reintroduce soft legumes under guidance."),
            ("Hummus is low fiber because it is a dip.", "It still contains chickpea fiber and often garlic."),
            ("Canned beans are always worse.", "Well-rinsed soft canned beans can be practical when tolerated."),
        ],
        "questions": [
            "Where do legumes sit on my current diet plan?",
            "Is smooth hummus allowed before whole chickpeas?",
            "How do we meet protein goals if beans are limited?",
        ],
        "related": [
            ("/blog/dal-lentils-ibd", "dal and lentils"),
            ("/blog/fodmap-diet-crohns-colitis", "FODMAP"),
            ("/blog/fiber-and-ibd-diet", "fiber"),
            ("/blog/tofu-soy-ibd", "tofu"),
        ],
        "match_terms": [
            "chickpeas",
            "hummus",
            "hummus ibd",
            "chickpeas ibd",
            "garbanzo ibd",
        ],
    },
]


TOPIC_POSTS: list[dict] = [
    {
        "slug": "turmeric-curcumin-ibd",
        "title": "Turmeric and Curcumin for IBD: Evidence, Doses, and Safety Questions",
        "description": "Turmeric and curcumin with Crohn's or colitis: food vs supplements, evidence limits, interactions, and clinic questions. Education only.",
        "category": "Nutrition · November 2026",
        "date_display": DATE_DISPLAY,
        "date_iso": DATE_ISO,
        "asset_dir": "turmeric-curcumin-ibd",
        "images": ["turmeric-curcumin-ibd_1.jpg"],
        "alts": ["Turmeric root and powder representing IBD nutrition education"],
        "share": "Turmeric and curcumin for IBD: evidence and safety questions. Education only.",
        "resource_category": "nutrition",
        "match_terms": [
            "turmeric",
            "curcumin",
            "turmeric ibd",
            "curcumin ibd",
            "turmeric crohn",
            "curcumin colitis",
            "turmeric supplement",
        ],
        "tags": ["turmeric", "curcumin", "supplements", "nutrition", "Crohn's", "colitis"],
        "body": """
<p>People searching <strong>turmeric for Crohn's</strong>, <strong>curcumin ulcerative colitis</strong>, or <strong>turmeric IBD supplement</strong> usually want to know whether a spice or capsule can calm inflammation. This page separates cooking amounts from concentrated supplements, notes evidence limits, and lists safety questions for your gastroenterologist or pharmacist. It is education only, not a dosing plan.</p>
<p>Pair this with <a href="/blog/seasonings-herbs-spices-ibd">seasonings and spices</a>, <a href="/blog/probiotics-ibd-practical-guide">probiotics</a>, and the <a href="/foods-ibd">Can I eat X? hub</a>.</p>

<h2>Food turmeric versus curcumin supplements</h2>
<p><strong>Turmeric</strong> is the culinary rhizome. <strong>Curcumin</strong> is one group of compounds inside turmeric that researchers study in higher doses. A pinch of turmeric in soup is not the same as a standardized curcumin capsule with piperine (black pepper extract) to raise absorption. Online "anti-inflammatory spice" claims often blur that difference.</p>
<ul class="blog-list">
<li><strong>Culinary turmeric:</strong> flavor and color; tiny curcumin amounts</li>
<li><strong>Supplements:</strong> concentrated extracts; product quality varies</li>
<li><strong>Enhanced absorption formulas:</strong> may raise blood levels and interaction risk</li>
</ul>

<h2>What the evidence can and cannot say</h2>
<p>Some clinical studies have explored curcumin as an add-on in ulcerative colitis under supervised protocols. Results are mixed, sample sizes are often modest, and products differ. Curcumin is not a substitute for mesalamine, immunomodulators, biologics, or surgery when those are indicated. Crohn's data are less clear than marketing posts suggest.</p>
<p>Treat any supplement discussion as an add-on conversation with your IBD team, not a DIY remission plan from social media.</p>

<h2>Safety topics to raise before you buy</h2>
<ul class="blog-list">
<li><strong>Bleeding risk:</strong> high-dose curcumin may affect clotting; ask before procedures or if you bruise easily</li>
<li><strong>Gallbladder disease:</strong> caution may apply for some biliary conditions</li>
<li><strong>Drug interactions:</strong> discuss with your pharmacist if you take anticoagulants, diabetes medicines, or chemotherapy</li>
<li><strong>Liver enzymes:</strong> rare reports of liver injury with some herbal products; report jaundice or dark urine promptly</li>
<li><strong>Pregnancy and breastfeeding:</strong> do not self-dose concentrated curcumin without specialist guidance</li>
</ul>

<h2>Practical kitchen use</h2>
<p>Many people enjoy mild turmeric in dals, rice, or golden milk. If spicy blends bother you, start with tiny amounts without chili. Food use is usually a comfort and culture question more than a pharmacologic one. See also <a href="/blog/dal-lentils-ibd">dal and lentils</a>.</p>

<h2>Supplement shopping red flags</h2>
<ul class="blog-list">
<li>Claims that turmeric "cures Crohn's" or replaces biologics</li>
<li>No lot number, no curcuminoid percentage, no third-party testing talk</li>
<li>Mega-doses far above studied ranges without clinician oversight</li>
<li>Stacked "gut repair" powders with many stimulants or laxative herbs</li>
</ul>

<h2>Questions for your gastroenterologist or dietitian</h2>
<ul class="blog-list">
<li>Is a curcumin trial reasonable with my disease activity and medicines?</li>
<li>Which product features matter if we trial an adjunct?</li>
<li>What labs or symptoms should stop a trial early?</li>
<li>How should I log stools and pain if we test a capsule?</li>
</ul>

<h2>How IBDPal can help</h2>
<p>If you trial a clinician-approved supplement, log the brand, dose, timing, and symptoms for two weeks. Bring that printout to clinic. Patterns beat memory when deciding whether something helped or only coincided with a steroid taper.</p>

<h2>When to seek prompt care</h2>
<p>Severe abdominal pain, heavy bleeding, fever, yellowing skin, or signs of allergic reaction need urgent evaluation. Supplement education cannot triage emergencies. See <a href="/flare-help">flare help</a> and <a href="/blog/when-to-go-er-ibd">when to go to the ER</a>.</p>

<p>Related reading: <a href="/blog/omega-3-ibd">omega-3</a> · <a href="/blog/iron-b12-vitamin-d-ibd">iron, B12, vitamin D</a> · <a href="/guides/foundation-complementary-medicine-ibd">complementary medicine bridge</a>.</p>
<p>Education supports shared decisions. It does not replace your gastroenterologist. Do not stop prescribed therapy because a spice aisle label sounded confident.</p>
<p>Kids and teens need pediatric dosing guidance. Culinary turmeric in family meals is different from adult capsules.</p>
<p>If cost is pushing you toward unregulated imports, ask your pharmacist about quality signals before ordering from unfamiliar sites.</p>

<h2>How curcumin studies are usually designed</h2>
<p>When researchers study curcumin in ulcerative colitis, they often use standardized extracts as an add-on to mesalamine in people with mild to moderate activity. Endpoints may include clinical scores, endoscopy, or calprotectin. Even positive signals rarely mean curcumin alone induces deep remission the way advanced therapies can. Product formulation (with or without piperine, phospholipid complexes, or nanoparticles) changes absorption, so copying a milligram number from a forum is unsafe.</p>
<p>Crohn's disease involves different locations and mechanisms. Extrapolating UC adjunct data to stricturing ileal Crohn's is not automatic. Ask your team which phenotype you have before assuming a spice capsule is relevant.</p>

<h2>Label literacy for patients</h2>
<ul class="blog-list">
<li>Look for curcuminoid percentage or milligrams of curcuminoids, not only "turmeric root powder"</li>
<li>Note whether black pepper extract is included</li>
<li>Check for multi-herb blends that hide stimulant laxatives</li>
<li>Prefer brands that discuss third-party testing for identity and contaminants</li>
</ul>
<p>Dietary supplements are regulated differently from prescription drugs in the United States. Quality varies. Bring the bottle photo to clinic rather than a vague brand nickname.</p>

<h2>Interactions and procedure timing</h2>
<p>Tell your surgeon, endoscopist, and pharmacist about curcumin before elective procedures. Some teams ask patients to pause certain supplements around operations because of bleeding or anesthesia considerations. Never assume "natural" means "no pause needed."</p>
<p>If you take anticoagulants, antiplatelets, or medicines with narrow therapeutic windows, get an explicit yes or no before starting high-dose curcumin. A cooking pinch is not the same risk conversation as a concentrated capsule.</p>

<h2>Tracking plan if your clinician agrees to a time-limited trial</h2>
<p>Agree on a start date, dose, duration (often a few weeks), and stop rules. Log stool frequency, urgency, pain, bleeding, and any new nausea. Keep other variables as steady as possible. If you start curcumin the same week you change biologics or begin a steroid taper, you will not know what helped.</p>
<p>At the follow-up, bring objective markers your team already uses: calprotectin, CRP, or scheduled scopes. Subjective "I feel less inflamed" without a plan is how money gets spent without learning.</p>

<h2>Bottom line</h2>
<p>Turmeric as food is a flavor choice. Curcumin as a supplement is a medical conversation with uncertain benefit, real interaction questions, and no license to replace IBD therapy. Use this page to prepare better questions, not to self-prescribe a cure.</p>
<p>Clinic script: "I am considering a curcumin supplement. Can we review evidence for my disease type, interactions with my medicines, and whether a time-limited tracked trial makes sense?"</p>
""",
    },
    {
        "slug": "loperamide-antispasmodics-ibd",
        "title": "Loperamide (Imodium) and Antispasmodics with IBD: Safety Questions",
        "description": "Loperamide (Imodium), dicyclomine, and antispasmodics with Crohn's or colitis: when people ask, risks, and clinic questions. Education only, not dosing advice.",
        "category": "Treatment · November 2026",
        "date_display": DATE_DISPLAY,
        "date_iso": DATE_ISO,
        "asset_dir": "loperamide-antispasmodics-ibd",
        "images": ["loperamide-antispasmodics-ibd_1.jpg"],
        "alts": ["Pharmacy shelf representing OTC IBD symptom education"],
        "share": "Loperamide and antispasmodics with IBD: questions to ask. Education only.",
        "resource_category": "treatment",
        "match_terms": [
            "loperamide",
            "imodium",
            "imodium ibd",
            "loperamide ibd",
            "antispasmodic",
            "bentyl",
            "dicyclomine",
            "dicyclomine ibd",
            "can i take imodium with crohn",
        ],
        "tags": ["loperamide", "Imodium", "antispasmodics", "dicyclomine", "symptoms", "Crohn's", "colitis"],
        "body": """
<p>Searches like <strong>can I take Imodium with Crohn's</strong>, <strong>loperamide ulcerative colitis</strong>, or <strong>Bentyl for IBD pain</strong> are common when diarrhea or cramping disrupts work and sleep. This page explains what these medicines are for in plain language, where the caution flags are, and what to ask your IBD team. It is education only. It is not a dose, a green light, or a substitute for urgent evaluation of obstruction, infection, or flare.</p>
<p>Pair with <a href="/blog/chronic-diarrhea-ibd-causes">chronic diarrhea causes</a>, <a href="/blog/abdominal-pain-stomach-pain-ibd">abdominal pain</a>, and <a href="/blog/when-to-call-gi-vs-er-ibd">when to call GI vs ER</a>.</p>

<h2>Loperamide (Imodium) in everyday words</h2>
<p>Loperamide slows intestinal motility and can reduce stool frequency for some people. In IBD it is sometimes used short-term for non-inflammatory diarrhea after a clinician rules out red flags. It is not a treatment for uncontrolled inflammation, C. difficile, or bowel obstruction.</p>
<ul class="blog-list">
<li><strong>Possible use cases people discuss with clinics:</strong> short trips, radiation of urgency after inflammation is quieter, bile-acid diarrhea pathways under guidance</li>
<li><strong>Not a DIY plan for:</strong> severe flare pain, fever, bloody stools without advice, suspected obstruction</li>
</ul>

<h2>Why IBD teams sometimes say "ask first"</h2>
<p>Slowing the gut when inflammation, infection, or a narrowing is present can worsen dilation risk or mask important symptoms. Toxic megacolon and obstruction are rare but serious contexts where antimotility medicines are unsafe without clinician direction. If you have fever, severe tenderness, persistent vomiting, or a known stricture, do not self-escalate OTC antimotility medicine.</p>

<h2>Antispasmodics (including dicyclomine / Bentyl)</h2>
<p>Antispasmodics reduce smooth-muscle cramping for some people with IBS-like pain. They do not heal ulcers or replace biologics. Side effects can include dry mouth, constipation, blurry vision, or urinary retention. People with certain glaucoma, severe colitis flares, or obstruction risk need individualized advice.</p>

<h2>Questions before you take an OTC antidiarrheal</h2>
<ul class="blog-list">
<li>Could this diarrhea be infection, including C. difficile after antibiotics?</li>
<li>Do I have fever, severe pain, or vomiting that needs same-day care?</li>
<li>Has my team ever said antimotility medicines are unsafe for my anatomy?</li>
<li>Am I already on opioids or other constipating medicines?</li>
<li>What maximum daily dose and duration does my clinician allow if approved?</li>
</ul>

<h2>Cardiac and high-dose warnings patients hear about</h2>
<p>High doses of loperamide misused for opioid effects have caused serious heart rhythm problems. Stick to labeled OTC directions unless your clinician gives a different plan, and never chase escalating doses when stools do not slow. If you feel faint, have palpitations, or syncope after dosing, seek urgent care.</p>

<h2>Tracking so clinic advice is better</h2>
<p>Log stool form (Bristol), frequency, blood, nocturnal stools, meals, and any OTC doses. Bring that log. Your team may be distinguishing inflammatory diarrhea from bile acid diarrhea, IBS overlap, or diet triggers. See <a href="/blog/bristol-stool-chart-ibd">Bristol stool chart</a> and <a href="/tools/bristol-flare-checker">flare checker tool</a>.</p>

<h2>When to seek prompt care instead of another pill</h2>
<p>Heavy bleeding, black stools, high fever, severe abdominal distension, repeated vomiting, dizziness from dehydration, or inability to pass gas or stool with pain need urgent pathways. See <a href="/flare-help">flare help</a> and <a href="/blog/vomiting-obstruction-ibd-warning-signs">vomiting and obstruction warning signs</a>.</p>

<p>Related reading: <a href="/blog/dehydration-ibd-warning-signs">dehydration</a> · <a href="/blog/electrolytes-flare-ibd">electrolytes</a> · <a href="/treatment-decisions">treatment decisions hub</a>.</p>
<p>Education supports shared decisions. It does not replace your gastroenterologist or pharmacist. Brand names are examples patients search; your formulary and diagnosis drive what is appropriate.</p>
<p>Pediatric dosing is different. Do not give adult OTC antidiarrheals to children with IBD without pediatric guidance.</p>
<p>If insurance or clinic access delays answers, use the nurse line rather than stacking multiple antimotility products.</p>

<h2>How clinics think about "safe enough for a flight"</h2>
<p>Patients often ask for a situational plan before travel. Some teams provide written instructions for short-term loperamide use when disease is quiet, infection is unlikely, and red-flag symptoms are absent. Others prefer prescription alternatives or bile-acid binders for specific mechanisms. The key is a written plan, not a screenshot of a forum dose.</p>
<p>Ask what to do if you develop fever mid-trip, how to hydrate, and when to go to urgent care abroad. Pair medicine questions with <a href="/blog/travel-with-ibd">travel with IBD</a>.</p>

<h2>Constipation rebound and overlapping IBS</h2>
<p>Overuse of antimotility medicines can swing some people into hard stools, overflow, or more cramping. Antispasmodics can also constipate. If your pattern is mixed diarrhea and constipation, say so clearly. Mixed patterns change the risk calculus.</p>

<h2>Infection check before you suppress diarrhea</h2>
<p>After antibiotics, hospitalization, or community outbreaks, infectious diarrhea needs a different pathway. Suppressing infectious diarrhea without evaluation can be harmful. Ask whether stool testing is needed before OTC escalation.</p>

<h2>Medication list hygiene</h2>
<p>Tell every clinician about loperamide, pepto-type products, cannabidiol oils, magnesium, and herbal "gut calm" teas. Duplicate antimotility stacks happen when people mix brands. Bring bottles or photos to visits.</p>

<h2>Hydration still comes first</h2>
<p>Slowing stools does not replace fluids and electrolytes when diarrhea has been heavy. Ask your team about oral rehydration options that fit your sodium and potassium needs. If you cannot keep fluids down, that is an urgent pathway, not another OTC dose. See <a href="/blog/dehydration-ibd-warning-signs">dehydration warning signs</a>.</p>
<p>People sometimes combine loperamide with fiber supplements, probiotics, or magnesium products without telling anyone. Bring the full list. Duplicate gut-slowing stacks raise constipation and bloating risk.</p>

<h2>Bottom line</h2>
<p>Loperamide and antispasmodics can be part of a clinician-guided symptom plan for some people with IBD, and unsafe self-medication for others, especially with infection, severe flare, or obstruction risk. Use this page to ask better questions, not to invent a standing home protocol.</p>
<p>Clinic script: "I am considering loperamide or an antispasmodic for urgency. Can we review whether that is safe for my disease location, infection risk, and what dose and stop rules you recommend?"</p>
""",
    },
    {
        "slug": "cbd-cannabis-ibd",
        "title": "CBD and Cannabis with IBD: Evidence, Risks, and Clinic Questions",
        "description": "CBD and cannabis with Crohn's or colitis: symptom claims, evidence limits, safety, drug interactions, and questions for your IBD team. Education only.",
        "category": "Wellness · November 2026",
        "date_display": DATE_DISPLAY,
        "date_iso": DATE_ISO,
        "asset_dir": "cbd-cannabis-ibd",
        "images": ["cbd-cannabis-ibd_1.jpg"],
        "alts": ["Calm wellness setting representing CBD and IBD education"],
        "share": "CBD and cannabis with IBD: evidence and safety questions. Education only.",
        "resource_category": "wellness",
        "match_terms": [
            "cbd",
            "cbd ibd",
            "cannabis ibd",
            "marijuana crohn",
            "cbd ulcerative colitis",
            "medical marijuana ibd",
            "cannabidiol crohn",
        ],
        "tags": ["CBD", "cannabis", "marijuana", "wellness", "symptoms", "Crohn's", "colitis"],
        "body": """
<p>People searching <strong>CBD for Crohn's</strong>, <strong>cannabis ulcerative colitis</strong>, or <strong>medical marijuana IBD</strong> often hope for pain relief, appetite help, or inflammation control. This page summarizes how patients and clinicians usually frame the topic, what evidence does not yet support, and safety questions to ask. It is education only. It is not a recommendation to start cannabis, a legal guide for your state, or a substitute for IBD therapy.</p>
<p>Pair with <a href="/blog/ibd-fatigue-brain-fog">fatigue and brain fog</a>, <a href="/blog/stress-coping-strategies-ibd">stress coping</a>, and <a href="/guides/foundation-complementary-medicine-ibd">complementary medicine</a>.</p>

<h2>CBD versus THC in plain language</h2>
<ul class="blog-list">
<li><strong>CBD (cannabidiol):</strong> non-intoxicating for many people at typical retail doses; product purity varies widely</li>
<li><strong>THC:</strong> intoxicating component; may increase appetite or reduce nausea for some, with cognitive and psychiatric risks</li>
<li><strong>Whole-plant / "full spectrum" products:</strong> mixtures that may include both plus terpenes</li>
</ul>
<p>Labels can be inaccurate. Contaminants and wrong THC amounts show up in testing studies of commercial CBD.</p>

<h2>Symptoms versus inflammation</h2>
<p>Some people report better pain coping, sleep, or nausea with cannabis-related products. Feeling better is not the same as healing ulcers or lowering calprotectin. Do not stop biologics or skip scopes because a vape or gummy reduced discomfort. Objective monitoring still matters. See <a href="/blog/what-remission-means-ibd">what remission means</a>.</p>

<h2>Evidence limits patients should know</h2>
<p>High-quality randomized data for cannabis as disease-modifying IBD therapy remain limited. Guidelines and specialty reviews generally treat cannabis as an unproven anti-inflammatory strategy while acknowledging possible symptom roles under medical supervision where legal. Expect more marketing certainty than clinical certainty.</p>

<h2>Safety and interaction topics</h2>
<ul class="blog-list">
<li><strong>Drug interactions:</strong> CBD can affect liver enzymes that metabolize other medicines; ask your pharmacist</li>
<li><strong>Smoking and vaping:</strong> lung irritation and infection risk discussions matter, especially on immunosuppression</li>
<li><strong>Mental health:</strong> THC can worsen anxiety or psychosis risk in vulnerable people</li>
<li><strong>Adolescents:</strong> brain development concerns; pediatric IBD teams need to lead this talk</li>
<li><strong>Pregnancy:</strong> avoid cannabis products unless your obstetric and IBD teams explicitly counsel otherwise</li>
<li><strong>Perioperative care:</strong> tell anesthesiology; abrupt changes can affect dosing of other drugs</li>
</ul>

<h2>Legal and workplace realities</h2>
<p>State medical programs, employer drug testing, travel across state lines, and federal rules do not always align. Educational articles cannot certify legality where you live. Ask a clinician familiar with your jurisdiction and read program rules yourself.</p>

<h2>Questions for your gastroenterologist</h2>
<ul class="blog-list">
<li>Are my symptoms more likely inflammation, IBS overlap, or medication side effects?</li>
<li>Could CBD interact with my IBD medicines or other prescriptions?</li>
<li>If we discuss cannabis for symptoms, how will we still monitor objective disease?</li>
<li>What product red flags should I avoid?</li>
</ul>

<h2>Safer symptom alternatives to discuss first</h2>
<p>Depending on your pattern, teams may prioritize treat-to-target IBD therapy, dietitian support, pelvic floor therapy, mental health care, sleep plans, or short-term symptom medicines. Cannabis should not be the first and only strategy for uncontrolled inflammation.</p>

<h2>When to seek prompt care</h2>
<p>Severe pain, heavy bleeding, high fever, dehydration, suicidal thoughts, or acute psychiatric changes need urgent pathways. Do not wait on a CBD experiment. See <a href="/flare-help">flare help</a> and <a href="/blog/depression-anxiety-ibd">depression and anxiety with IBD</a>.</p>

<p>Related reading: <a href="/blog/nsaids-ibd-risk">NSAIDs and IBD</a> · <a href="/blog/sleep-rest-ibd-flares">sleep during flares</a> · <a href="/ask">reader Q&amp;A</a>.</p>
<p>Education supports shared decisions. It does not replace your gastroenterologist, pharmacist, or local legal counsel. Brand names and dispensary menus change quickly; bring product labels to clinic.</p>
<p>If cost or stigma keeps you from telling your doctor, say that out loud. Honest med lists prevent dangerous interactions.</p>
<p>Driving, childcare, and school policies may prohibit impairment even when a product is legal. Plan accordingly.</p>

<h2>How to talk about "it helps my appetite"</h2>
<p>Appetite and nausea support can be meaningful during flares or after surgery. Tell your team what is working so they can weigh benefits against risks and still treat the inflammation driving weight loss. Nutrition support, antiemetics, and disease control often outperform cannabis alone for malnutrition.</p>
<p>Log weight, oral intake, and product timing. If you only eat when intoxicated, ask about safer appetite strategies and whether enteral support is needed. See <a href="/blog/enteral-nutrition-ibd">enteral nutrition</a>.</p>

<h2>Product quality checklist</h2>
<ul class="blog-list">
<li>Certificate of analysis for cannabinoid content and contaminants when available</li>
<li>Clear CBD versus THC amounts per serving</li>
<li>No extravagant "cures IBD" claims on the label</li>
<li>Avoid unknown oils sold only through social media DMs</li>
</ul>

<h2>Immunosuppression and lung products</h2>
<p>People on biologics or other immunosuppressants should be especially cautious with smoked or vaped products because of lung injury and infection concerns. Oral or pharmacist-reviewed options (where legal and clinician-approved) are a different risk conversation than combustion.</p>

<h2>Sleep, pain, and the "it is the only thing that works" trap</h2>
<p>Chronic pain and insomnia push people toward cannabis when other tools feel slow. That distress is real. Still ask whether disease activity is undertreated, whether pelvic floor dysfunction or joint EIMs need their own plans, and whether mental health care is under-resourced. Cannabis may blunt awareness of worsening bloody stools or fevers. Keep a simple red-flag checklist on the fridge.</p>
<p>If you already use cannabis daily, tell your IBD team the approximate THC and CBD amounts, route, and timing. Abrupt cessation before surgery or hospitalization can complicate symptom interpretation. Plan changes with clinicians rather than quitting cold turkey the night before a scope without telling anyone.</p>
<p>Workplace impairment, parenting safety, and school or college policies matter even when a product is legal for adults. Write down your personal rules before you are tired and tempted to drive after a dose.</p>

<h2>Bottom line</h2>
<p>CBD and cannabis are common patient questions. Symptom relief stories exist. Disease-modifying proof is limited. Safety, legality, interactions, and honest monitoring plans belong in clinic, not in a solo experiment that replaces treat-to-target care.</p>
<p>Clinic script: "I am considering CBD or cannabis for IBD symptoms. Can we review interactions, legality constraints, and how we will still track objective inflammation if I try a product?"</p>
""",
    },
    {
        "slug": "autism-ibd-connection",
        "title": "Autism and IBD: Overlap Questions Patients and Families Ask",
        "description": "Autism and IBD overlap: GI symptoms, sensory feeding, care coordination, and clinic questions for families and adults. Education only, not diagnostic advice.",
        "category": "Family · November 2026",
        "date_display": DATE_DISPLAY,
        "date_iso": DATE_ISO,
        "asset_dir": "autism-ibd-connection",
        "images": ["autism-ibd-connection_1.jpg"],
        "alts": ["Supportive family care setting representing autism and IBD education"],
        "share": "Autism and IBD: overlap questions for families. Education only.",
        "resource_category": "family",
        "match_terms": [
            "autism",
            "autism ibd",
            "autism crohn",
            "autism colitis",
            "asd ibd",
            "autism gut",
            "autistic ibd",
        ],
        "tags": ["autism", "ASD", "family", "pediatrics", "Crohn's", "colitis", "neurodiversity"],
        "body": """
<p>People searching <strong>autism and IBD</strong>, <strong>autism Crohn's</strong>, or <strong>ASD colitis</strong> usually want to know whether the conditions are linked, how to manage GI symptoms when communication or sensory needs differ, and how to coordinate care. This page offers patient- and family-oriented education. It does not diagnose autism or IBD, and it does not claim that one causes the other in a simple way.</p>
<p>Pair with <a href="/blog/living-with-ibd-kids">living with IBD kids</a>, <a href="/pediatric-caregivers">pediatric caregivers</a>, and <a href="/blog/icn-health-literacy-toolkit-ibd">health literacy toolkit</a>.</p>

<h2>What "overlap" can mean</h2>
<ul class="blog-list">
<li><strong>Co-occurrence:</strong> some people live with both an autism diagnosis and Crohn's or ulcerative colitis</li>
<li><strong>Shared clinic challenges:</strong> sensory aversions to prep drinks, difficulty describing pain, procedure anxiety</li>
<li><strong>Research interest:</strong> scientists study immune, microbiome, and genetic themes; headlines often outrun settled clinical rules</li>
</ul>
<p>GI symptoms are also common in autistic people without IBD (constipation, reflux, feeding selectivity). Alarm features still need proper evaluation rather than assuming "just sensory."</p>

<h2>Do not skip IBD workups because of autism stereotypes</h2>
<p>Weight loss, blood in stool, nocturnal diarrhea, growth failure, severe anemia, or escalating pain deserve gastroenterology evaluation. Communication differences can delay recognition. Caregivers and clinicians should use concrete observation tools: stool photos, food refusal logs, sleep disruption, and school nurse notes.</p>

<h2>Care coordination that helps</h2>
<ul class="blog-list">
<li>Share autism accommodations with the GI team (visual schedules, low-stimulation rooms, preferred communication)</li>
<li>Ask about quieter infusion chairs or longer visit slots</li>
<li>Practice medical play for kids before scopes when developmentally appropriate</li>
<li>Involve occupational therapy and dietitians who understand selective eating plus IBD diets</li>
<li>Keep one shared medication list across neurology, psychiatry, GI, and primary care</li>
</ul>

<h2>Feeding and sensory diets meet IBD diet advice</h2>
<p>Selective eating can collide with low-residue or high-protein instructions. The goal is workable nutrition, not perfection. Dietitians may prioritize calories, hydration, and safe textures first, then expand variety. Avoid forcing large sensory leaps during active flares. See <a href="/blog/teen-nutrition-ibd-growth">teen nutrition and growth</a> and <a href="/ibd-nutrition">IBD nutrition</a>.</p>

<h2>Procedures, colonoscopy prep, and hospital stays</h2>
<p>Prep volume, taste, and bathroom urgency are hard for many patients and can be especially hard with sensory sensitivities. Ask about prep flavor options, timing schedules that match routines, and anesthesia plans. Bring comfort items allowed by the unit. Write a one-page "how I communicate pain" sheet for nurses.</p>

<h2>Questions for your gastroenterologist</h2>
<ul class="blog-list">
<li>Which symptoms worry you for IBD versus functional GI issues?</li>
<li>How can we adapt prep and clinic visits for sensory needs?</li>
<li>Who coordinates growth, mental health, and IBD therapy?</li>
<li>What home observations should we track between visits?</li>
</ul>

<h2>Adults with autism and IBD</h2>
<p>Adults may need workplace accommodations, clearer visit summaries, and support deciding when to escalate care. Bring a trusted supporter if helpful. Ask for written after-visit instructions. See <a href="/blog/ibd-at-work-talking-to-manager">IBD at work</a> and <a href="/blog/disability-fmla-work-ibd">disability and FMLA</a>.</p>

<h2>When to seek prompt care</h2>
<p>Severe pain, heavy bleeding, dehydration, high fever, or sudden behavior changes with abdominal symptoms need urgent evaluation. Use visual pain scales if verbal description is hard. See <a href="/flare-help">flare help</a> and <a href="/blog/when-to-go-er-ibd">when to go to the ER</a>.</p>

<p>Related reading: <a href="/blog/siblings-when-child-has-ibd">siblings when a child has IBD</a> · <a href="/blog/partner-caregiver-ibd">partner and caregiver</a> · <a href="/ask">reader Q&amp;A</a>.</p>
<p>Education supports shared decisions. It does not replace your gastroenterologist, developmental pediatrician, or autism specialist.</p>
<p>Research headlines about autism and the gut change quickly. Ask your clinician how any new study applies to your child or yourself before changing therapy.</p>
<p>Respect neurodiversity in clinic scripts. Clear, concrete language helps more than metaphors.</p>

<h2>Research claims versus clinic decisions</h2>
<p>You may see articles about microbiome differences, immune signaling, or epidemiologic associations between neurodevelopmental conditions and IBD. Association is not destiny, and it is not a mandate to pursue unproven "autism gut protocols" that delay standard IBD care. Treat-to-target inflammation control, growth support, and mental health care remain the backbone when IBD is confirmed.</p>
<p>Be wary of clinics selling expensive unvalidated tests as the key to both autism and Crohn's. Bring marketing materials to a trusted clinician before paying.</p>

<h2>School and therapy team alignment</h2>
<p>Share relevant GI needs with IEP or 504 teams: bathroom access, hydration, fatigue after infusions, and sensory triggers around cafeteria smells. Occupational therapists and feeding therapists should know which textures are medically restricted during flares so goals stay aligned. See <a href="/teens-and-school">teens and school hub</a>.</p>

<h2>Pain communication toolkit</h2>
<ul class="blog-list">
<li>Number or color scales practiced at home before clinic</li>
<li>Photo logs of stools when words fail</li>
<li>Body maps to point to pain location</li>
<li>Scripts for nurses: "I need a break" or "too loud"</li>
</ul>

<h2>Caregiver burnout is clinical data</h2>
<p>Night bathroom trips, food battles, and procedure anxiety exhaust families. Tell the team when caregivers are depleted. Respite, counseling, and simplified regimens may be part of safe care. See <a href="/blog/icn-caregiver-coping-resource">caregiver coping</a>.</p>

<h2>Transitions from pediatric to adult care</h2>
<p>Young adults with both autism and IBD may need longer transfer planning than a single goodbye visit. Ask who will refill biologics, who manages prior authorizations, and how emergency contacts work after the pediatric team steps back. Written care maps reduce missed infusions during the handoff year. See <a href="/blog/icn-transfer-toolkit-adult-care">transfer to adult care</a>.</p>
<p>College housing, roommate bathroom access, and dining-hall sensory load should be part of the IBD plan, not an afterthought. Disability services offices can help with practical accommodations when medical documentation is clear.</p>

<h2>Bottom line</h2>
<p>Autism and IBD can co-occur and create unique care logistics. Take GI alarm symptoms seriously, adapt communication and procedures, coordinate feeding goals with IBD nutrition needs, and keep evidence-based IBD therapy at the center. Use this page to prepare questions, not to self-diagnose.</p>
<p>Clinic script: "We are navigating autism and possible or confirmed IBD. Can we build a visit and prep plan that fits sensory needs while still monitoring inflammation properly?"</p>
""",
    },
    {
        "slug": "adalimumab-vs-ustekinumab-ibd",
        "title": "Adalimumab vs Ustekinumab for IBD: Patient Comparison Questions",
        "description": "Adalimumab (Humira and biosimilars) vs ustekinumab (Stelara): how patients compare mechanisms, dosing, monitoring, and clinic questions. Education only.",
        "category": "Treatment · November 2026",
        "date_display": DATE_DISPLAY,
        "date_iso": DATE_ISO,
        "asset_dir": "adalimumab-vs-ustekinumab-ibd",
        "images": ["adalimumab-vs-ustekinumab-ibd_1.jpg"],
        "alts": ["Medication discussion representing IBD biologic comparison education"],
        "share": "Adalimumab vs ustekinumab for IBD: comparison questions. Education only.",
        "resource_category": "treatment",
        "match_terms": [
            "humira vs stelara",
            "adalimumab vs ustekinumab",
            "stelara vs humira",
            "humira or stelara",
            "adalimumab vs stelara",
            "ustekinumab vs adalimumab",
        ],
        "tags": ["adalimumab", "ustekinumab", "Humira", "Stelara", "biologics", "comparison", "treatment"],
        "body": """
<p>Searches like <strong>Humira vs Stelara</strong> or <strong>adalimumab vs ustekinumab</strong> usually mean you are choosing between biologics or preparing for a clinic visit. This page compares themes patients ask about: mechanism class, dosing style, monitoring, and insurance realities. It is education only. It does not rank a "best drug" for you.</p>
<p>Pair with <a href="/blog/ibd-treatment-comparison-guide">treatment comparison guide</a>, <a href="/blog/understanding-biologics-ibd">understanding biologics</a>, and <a href="/treatment-decisions">treatment decisions hub</a>.</p>

<h2>Quick class difference</h2>
<ul class="blog-list">
<li><strong>Adalimumab:</strong> anti-TNF biologic (Humira and many biosimilars). Often self-injected on a scheduled cadence after induction.</li>
<li><strong>Ustekinumab:</strong> interleukin-12/23 pathway biologic (Stelara and related products depending on market). Often IV induction then subcutaneous maintenance.</li>
</ul>
<p>Different immune targets mean prior drug history, antibodies, infection screening, and comorbidities steer the choice more than internet popularity contests.</p>

<h2>What usually drives the clinical choice</h2>
<ul class="blog-list">
<li>Disease type and location (Crohn's vs UC; fistulizing disease; extraintestinal issues)</li>
<li>Prior anti-TNF exposure and whether antibodies developed</li>
<li>Infection history, TB and hepatitis screening, heart failure considerations for anti-TNF class talks</li>
<li>Pregnancy planning, age, and other immune conditions</li>
<li>Infusion center access versus home injection preference</li>
<li>Formulary, step therapy, and copay programs</li>
</ul>

<h2>Dosing lifestyle differences patients notice</h2>
<p>Adalimumab maintenance is typically a regular home injection schedule. Ustekinumab often starts with an infusion, then spaced subcutaneous injections. Exact schedules depend on indication and response. Ask your nurse for the calendar that matches your prescription, not a generic chart from social media.</p>

<h2>Monitoring and loss of response</h2>
<p>Both require ongoing assessment of symptoms, labs, and sometimes drug levels or endoscopy. If a biologic stops working, teams consider mechanistic failure versus low drug exposure. See <a href="/blog/therapeutic-drug-monitoring-ibd">therapeutic drug monitoring</a> and <a href="/blog/when-ibd-biologic-stops-working">when a biologic stops working</a>.</p>

<h2>Biosimilars and brand names</h2>
<p>Adalimumab has multiple biosimilars. Switching conversations involve insurance design, shared decision-making, and sometimes device differences. Ustekinumab access also evolves with coverage policy. Ask which exact product your plan covers and how support programs work.</p>

<h2>Questions to bring to clinic</h2>
<ul class="blog-list">
<li>Why this mechanism for my disease history?</li>
<li>What does induction and maintenance look like week by week?</li>
<li>How will we judge success at 12 weeks and beyond?</li>
<li>What infection precautions and vaccines should I update first?</li>
<li>If this fails, what is the next class we are preserving?</li>
<li>What is the prior authorization timeline?</li>
</ul>

<h2>Insurance and access</h2>
<p>Step therapy may require trying one class before another. Document failures and intolerances carefully. See <a href="/blog/prior-authorization-biologics-timeline">prior authorization timeline</a> and <a href="/blog/ibd-insurance-denial-appeal-toolkit">appeal toolkit</a>.</p>

<h2>When to seek prompt care on either medicine</h2>
<p>High fever, severe abdominal pain, heavy bleeding, signs of serious infection, or allergic reactions after an injection or infusion need urgent pathways. See <a href="/blog/infusion-day-what-to-expect">infusion day tips</a> and <a href="/flare-help">flare help</a>.</p>

<p>Related reading: <a href="/blog/humira-fatigue-ibd">Humira and fatigue</a> · <a href="/blog/skyrizi-patient-questions-ibd">Skyrizi questions</a> · <a href="/guides/biologics-questions-for-your-doctor">biologic questions guide</a>.</p>
<p>Education supports shared decisions. It does not replace your gastroenterologist. Brand examples reflect common search terms; your prescription may be a biosimilar or updated product.</p>
<p>Never stop a biologic suddenly without a plan for flare risk and coverage timing.</p>
<p>Bring a caregiver to comparison visits when brain fog makes decision-making harder.</p>

<h2>Side-effect themes to compare in clinic (not online scare lists)</h2>
<p>Both drug classes suppress parts of the immune system and share infection vigilance. Anti-TNF counseling often includes TB reactivation screening and discussions about certain demyelinating or heart-failure histories when relevant. IL-12/23 pathway counseling has its own infection and monitoring themes. Your clinician should personalize warnings to your chart rather than a generic internet list.</p>
<p>Injection-site reactions, infusion reactions, and how to report delayed fever should be part of teach-back before your first dose.</p>

<h2>How to read "someone on Reddit did better on X"</h2>
<p>Anecdotes skip phenotype, prior antibodies, smoking status, steroid use, and therapeutic drug monitoring. Two patients with "Crohn's" can have completely different disease biology. Use peer stories for emotional support, not mechanism selection.</p>

<h2>Pregnancy and family planning</h2>
<p>If you are pregnant, planning pregnancy, or breastfeeding, ask for IBD and obstetric co-management before changing biologics. Do not assume one brand is universally safer based on a forum thread. Timing of third-trimester doses and live vaccines for newborns are specialist topics.</p>

<h2>Practical comparison worksheet</h2>
<ul class="blog-list">
<li>My prior biologics and why they stopped</li>
<li>My preferred care setting (home injection vs infusion center)</li>
<li>My insurance preferred product list</li>
<li>My top three treatment goals (fistula healing, steroid free, scope healing, work reliability)</li>
<li>My red-flag symptoms and on-call number</li>
</ul>

<h2>Infection vigilance on either path</h2>
<p>Fever, cough, wound drainage, or exposure to tuberculosis contacts should trigger a call before the next injection or infusion. Keep vaccine records updated with your team before intensifying immunosuppression when possible. See <a href="/blog/vaccines-biologics-immunosuppressants-ibd">vaccines and immunosuppressants</a>.</p>
<p>Travel with injectables needs cooler packs, letters, and a plan for delays. Ask whether a missed window requires clinic guidance before you self-adjust timing from a social media tip.</p>
<p>If fatigue worsens after starting therapy, do not assume the drug is "wrong" without labs. Anemia, sleep loss, and active inflammation can look like drug side effects. Log timing carefully for the next visit.</p>

<h2>Shared decision checklist you can print</h2>
<p>Write your top goal in one sentence. List prior drug failures. Circle home injection versus infusion preference. Note pregnancy plans for the next year. Bring insurance cards and denial letters. That packet turns a vague "Humira vs Stelara" search into a productive appointment.</p>

<h2>Bottom line</h2>
<p>Adalimumab and ustekinumab differ in immune target and dosing logistics. The right choice depends on your history, safety screen, monitoring plan, and access, not a universal ranking. Use this page to structure the visit.</p>
<p>Clinic script: "Can we compare adalimumab and ustekinumab for my disease history, dosing lifestyle, monitoring plan, and insurance path before I decide?"</p>
""",
    },
]


def build_food_posts() -> list[dict]:
    posts = []
    for f in FOODS:
        posts.append(
            {
                "slug": f["slug"],
                "title": f["title"],
                "description": f["description"],
                "category": f["category"],
                "date_display": DATE_DISPLAY,
                "date_iso": DATE_ISO,
                "asset_dir": f["slug"],
                "images": [f"{f['slug']}_1.jpg"],
                "alts": [f["title"]],
                "share": f["share"],
                "resource_category": f["resource_category"],
                "match_terms": f["match_terms"],
                "tags": f["tags"],
                "body": food_body(f),
            }
        )
    return posts


def discover_food_slugs() -> list[str]:
    """Heuristic: food micros already on disk plus new ones."""
    known_new = [f["slug"] for f in FOODS] + ["turmeric-curcumin-ibd"]
    extra = [
        "apple-ibd-cooked-vs-raw",
        "avocado-ibd",
        "banana-ibd-crohns-colitis",
        "blueberries-ibd",
        "broccoli-ibd",
        "carrots-ibd",
        "chapati-roti-ibd",
        "chicken-protein-ibd",
        "chocolate-ibd",
        "coffee-ibd",
        "congee-rice-porridge-ibd",
        "corn-ibd",
        "couscous-ibd",
        "cucumber-ibd",
        "dairy-lactose-ibd",
        "dal-lentils-ibd",
        "dates-ramadan-ibd",
        "eggs-ibd-nutrition",
        "greek-yogurt-ibd",
        "grapes-ibd",
        "kimchi-fermented-ibd",
        "lean-beef-ibd",
        "mango-ibd-crohns-colitis",
        "melon-ibd",
        "miso-soup-ibd",
        "oatmeal-ibd",
        "onion-garlic-ibd-fodmap",
        "oranges-citrus-ibd",
        "paneer-ibd",
        "peanut-butter-ibd",
        "plantain-ibd",
        "potato-ibd-white",
        "salmon-fish-ibd",
        "spinach-leafy-greens-ibd",
        "strawberries-ibd",
        "sweet-potato-ibd",
        "tea-ibd",
        "tofu-soy-ibd",
        "tomatoes-ibd",
        "tortillas-ibd",
        "tuna-ibd",
        "turkey-protein-ibd",
        "white-bread-ibd",
        "white-rice-ibd-flare",
        "zucchini-ibd",
        "alcohol-caffeine-ibd",
        "bone-broth-gut-healing-ibd",
        "seasonings-herbs-spices-ibd",
        "spicy-foods-nuts-seeds-ibd",
    ]
    slugs = []
    for slug in known_new + extra:
        if (BLOGS / f"{slug}.html").exists() or slug in known_new:
            if slug not in slugs:
                slugs.append(slug)
    return slugs


FOODS_HUB = {
    "slug": "foods-ibd",
    "h1": "Can I eat this with IBD?",
    "title": "Can I Eat X with IBD? Food A-Z for Crohn's & Colitis | IBDPal",
    "description": "Food-by-food IBD guides for Crohn's and ulcerative colitis: fruits, grains, dairy alternatives, snacks, sweeteners, and spices. Education only.",
    "intro": "Single-food questions drive much of IBDPal traffic. Use this hub to jump to practical Can I eat X? articles. Tolerance is individual. These pages prepare clinic questions; they do not prescribe a personal diet.",
    "keywords": [
        "can I eat with Crohn's",
        "IBD food list",
        "Crohn's safe foods",
        "ulcerative colitis foods",
        "pineapple IBD",
        "quinoa IBD",
        "honey IBD",
        "oat milk IBD",
        "popcorn Crohn's",
        "hummus colitis",
        "turmeric IBD",
    ],
    "featured_links": [
        {
            "url": "/guides/what-should-i-eat-crohns-colitis",
            "label": "What should I eat with Crohn's or colitis?",
            "blurb": "Start with a clinician-aligned overview before food-by-food experiments.",
        },
        {
            "url": "/blog/flare-foods-ibd",
            "label": "Flare foods overview",
            "blurb": "Gentler patterns many teams discuss during active symptoms.",
        },
        {
            "url": "/blog/tracking-food-symptoms-ibdpal",
            "label": "Track food and symptoms",
            "blurb": "Log portion, form, and timing so patterns show up in clinic.",
        },
    ],
    "sections": [
        {
            "heading": "How to use this hub",
            "paragraphs": [
                "Open the food article that matches your question. Read flare versus remission tips, then log your own trial if your clinician agrees.",
                "If you have strictures, recent surgery, or a prescribed elimination plan, follow your IBD team over any generic food page.",
                "New long-tail guides include pineapple, quinoa, honey and sweeteners, plant milks, popcorn, chickpeas and hummus, plus a dedicated turmeric and curcumin page.",
            ],
        },
        {
            "heading": "When food questions become urgent",
            "paragraphs": [
                "Severe pain, repeated vomiting, inability to keep fluids down, heavy bleeding, high fever, or rapid weight loss need prompt medical care, not another food trial.",
            ],
        },
    ],
    "guides": [
        {"url": "/ibd-nutrition", "label": "IBD nutrition hub"},
        {"url": "/guides/what-should-i-eat-crohns-colitis", "label": "What should I eat?"},
        {"url": "/guides/crohns-disease-diet-nutrition", "label": "Crohn's diet & nutrition"},
        {"url": "/guides/ulcerative-colitis-diet-foods", "label": "UC diet & foods"},
        {"url": "/guides/low-residue-diet-ibd", "label": "Low-residue diet overview"},
        {"url": "/guides/foods-to-eat-crohns-flare", "label": "Foods during a Crohn's flare"},
        {"url": "/eating-with-ibd", "label": "Eating With IBD book landing"},
        {"url": "/tools/food-pain-tracker", "label": "Food and pain tracker tool"},
    ],
    "blog_slugs": [],  # filled at publish time
}


def patch_vercel_blog(slugs: list[str]) -> None:
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
    print("patched vercel blog rewrites", len(inserts))


def patch_vercel_hub(path: str) -> None:
    text = VERCEL.read_text(encoding="utf-8")
    if f'"source": "{path}"' in text:
        return
    insert = f'    {{\n      "source": "{path}",\n      "destination": "{path}.html"\n    }},\n'
    text = text.replace('"rewrites": [\n', '"rewrites": [\n' + insert)
    VERCEL.write_text(text, encoding="utf-8")
    print("patched vercel hub", path)


def patch_sitemap_paths(paths: list[str], priority: str = "0.85") -> None:
    today = date.today().isoformat()
    text = SITEMAP.read_text(encoding="utf-8")
    for path in paths:
        if f"{SITE}{path}</loc>" in text:
            continue
        entry = (
            f"  <url>\n    <loc>{SITE}{path}</loc>\n"
            f"    <lastmod>{today}</lastmod>\n"
            f"    <changefreq>monthly</changefreq>\n"
            f"    <priority>{priority}</priority>\n  </url>\n"
        )
        text = text.replace("</urlset>", entry + "</urlset>")
    SITEMAP.write_text(text, encoding="utf-8")
    print("patched sitemap.xml", len(paths), "paths checked")


def update_search_gap(posts: list[dict]) -> None:
    data = {"posts": []}
    if SEARCH_GAP.exists():
        data = json.loads(SEARCH_GAP.read_text(encoding="utf-8"))
        if isinstance(data, list):
            data = {"posts": data}
    by_slug = {p["slug"]: p for p in data.get("posts", [])}
    for post in posts:
        by_slug[post["slug"]] = {
            "slug": post["slug"],
            "match_terms": post.get("match_terms", []),
            "title": post["title"],
            "description": post["description"],
            "category": post["category"],
            "date_display": post["date_display"],
            "date_iso": post["date_iso"],
            "asset_dir": post["asset_dir"],
            "resource_category": post.get("resource_category", "nutrition"),
            "tags": post.get("tags", []),
        }
    data["posts"] = list(by_slug.values())
    SEARCH_GAP.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("updated search-gap-posts.json")


def update_aliases(posts: list[dict]) -> None:
    data = json.loads(ALIASES.read_text(encoding="utf-8"))
    for post in posts:
        terms = post.get("match_terms") or []
        if not terms:
            continue
        canonical = terms[0]
        for term in terms:
            data[term.lower()] = canonical
    extras = {
        "can i eat": "can i eat",
        "can i eat this": "can i eat",
        "foods ibd": "can i eat",
        "ibd food list": "can i eat",
        "food a to z": "can i eat",
        "safe foods ibd": "can i eat",
    }
    data.update(extras)
    ALIASES.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("updated search-aliases.json")


def update_seo_hub(food_slugs: list[str]) -> dict:
    data = json.loads(SEO.read_text(encoding="utf-8"))
    hub = dict(FOODS_HUB)
    hub["blog_slugs"] = food_slugs
    hubs = data.get("hubs", [])
    hubs = [h for h in hubs if h.get("slug") != "foods-ibd"]
    hubs.append(hub)
    data["hubs"] = hubs
    SEO.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("updated seo-expansion.json foods-ibd hub")
    return hub


def patch_home_search_pins() -> None:
    path = ROOT / "home-search.js"
    text = path.read_text(encoding="utf-8")
    block = """
    pineapple: ['/blog/pineapple-ibd'],
    quinoa: ['/blog/quinoa-ibd'],
    honey: ['/blog/honey-sweeteners-ibd'],
    stevia: ['/blog/honey-sweeteners-ibd'],
    'oat milk': ['/blog/plant-milks-ibd'],
    'almond milk': ['/blog/plant-milks-ibd'],
    popcorn: ['/blog/popcorn-ibd'],
    hummus: ['/blog/chickpeas-hummus-ibd'],
    chickpeas: ['/blog/chickpeas-hummus-ibd'],
    turmeric: ['/blog/turmeric-curcumin-ibd'],
    curcumin: ['/blog/turmeric-curcumin-ibd'],
    loperamide: ['/blog/loperamide-antispasmodics-ibd'],
    imodium: ['/blog/loperamide-antispasmodics-ibd'],
    dicyclomine: ['/blog/loperamide-antispasmodics-ibd'],
    bentyl: ['/blog/loperamide-antispasmodics-ibd'],
    cbd: ['/blog/cbd-cannabis-ibd'],
    cannabis: ['/blog/cbd-cannabis-ibd'],
    autism: ['/blog/autism-ibd-connection'],
    'humira vs stelara': ['/blog/adalimumab-vs-ustekinumab-ibd'],
    'can i eat': ['/foods-ibd'],
    'foods ibd': ['/foods-ibd'],
"""
    if "pineapple: ['/blog/pineapple-ibd']" in text:
        print("home-search pins already present")
        return
    text = text.replace(
        "    'what it takes': ['/ibd-awareness-calendar']\n  };",
        "    'what it takes': ['/ibd-awareness-calendar'],"
        + block
        + "  };",
    )
    path.write_text(text, encoding="utf-8")
    print("patched home-search.js pins")


def patch_resource_library_pins() -> None:
    path = ROOT / "resource-library.js"
    text = path.read_text(encoding="utf-8")
    if "pineapple:" in text and "turmeric:" in text and "/foods-ibd" in text:
        print("resource-library pins already present")
        return
    # Mirror home-search style if a PINNED block exists
    marker = "var PINNED_TOPIC_URLS"
    if marker not in text:
        print("WARN: resource-library.js has no PINNED_TOPIC_URLS; skip")
        return
    # Find closing of PINNED object near seasoning pins or end
    if "pineapple: ['/blog/pineapple-ibd']" in text:
        return
    insert = """
    pineapple: ['/blog/pineapple-ibd'],
    quinoa: ['/blog/quinoa-ibd'],
    honey: ['/blog/honey-sweeteners-ibd'],
    stevia: ['/blog/honey-sweeteners-ibd'],
    turmeric: ['/blog/turmeric-curcumin-ibd'],
    curcumin: ['/blog/turmeric-curcumin-ibd'],
    loperamide: ['/blog/loperamide-antispasmodics-ibd'],
    imodium: ['/blog/loperamide-antispasmodics-ibd'],
    cbd: ['/blog/cbd-cannabis-ibd'],
    autism: ['/blog/autism-ibd-connection'],
    'can i eat': ['/foods-ibd'],
"""
    # Insert before the closing of the first PINNED_TOPIC_URLS object after herbs line if present
    if "herbs: ['/blog/seasonings-herbs-spices-ibd']," in text:
        text = text.replace(
            "herbs: ['/blog/seasonings-herbs-spices-ibd'],",
            "herbs: ['/blog/seasonings-herbs-spices-ibd']," + insert,
            1,
        )
        path.write_text(text, encoding="utf-8")
        print("patched resource-library.js pins")
        return
    print("WARN: could not find insertion point in resource-library.js")


def patch_changelog() -> None:
    path = ROOT / "scripts" / "ui_snippets.py"
    text = path.read_text(encoding="utf-8")
    bullet = (
        '                            <li><strong>Traffic-gap pack (Nov 26):</strong> '
        '<a href="/foods-ibd">Can I eat X? food hub</a>; new food micros for '
        '<a href="/blog/pineapple-ibd">pineapple</a>, '
        '<a href="/blog/quinoa-ibd">quinoa</a>, '
        '<a href="/blog/honey-sweeteners-ibd">honey/sweeteners</a>, '
        '<a href="/blog/plant-milks-ibd">plant milks</a>, '
        '<a href="/blog/popcorn-ibd">popcorn</a>, '
        '<a href="/blog/chickpeas-hummus-ibd">chickpeas/hummus</a>; '
        '<a href="/blog/turmeric-curcumin-ibd">turmeric/curcumin</a>, '
        '<a href="/blog/loperamide-antispasmodics-ibd">loperamide/antispasmodics</a>, '
        '<a href="/blog/cbd-cannabis-ibd">CBD/cannabis</a>, '
        '<a href="/blog/autism-ibd-connection">autism and IBD</a>, '
        '<a href="/blog/adalimumab-vs-ustekinumab-ibd">adalimumab vs ustekinumab</a></li>\n'
    )
    if "Traffic-gap pack (Nov 26)" in text:
        print("changelog already present")
        return
    anchor = '                        <h2>November 2026</h2>\n                        <ul class="seo-landing__list">\n'
    if anchor not in text:
        print("WARN: November 2026 changelog anchor missing")
        return
    text = text.replace(anchor, anchor + bullet, 1)
    path.write_text(text, encoding="utf-8")
    print("patched ui_snippets changelog")


def publish_hub(hub: dict) -> None:
    from amp_utils import discover_blogs  # noqa: E402
    from generate_seo_hubs import render_hub  # noqa: E402
    from blog_related import patch_blog_html  # noqa: E402

    posts = discover_blogs(BLOGS)
    out = ROOT / f"{hub['slug']}.html"
    out.write_text(render_hub(hub, posts), encoding="utf-8")
    print("wrote", out.name)
    data = json.loads(SEO.read_text(encoding="utf-8"))
    hubs = data["hubs"]
    patched = 0
    for slug in hub.get("blog_slugs", [])[:12]:
        path = BLOGS / f"{slug}.html"
        if path.exists() and patch_blog_html(path, slug, posts, hubs):
            patched += 1
    print(f"patched related reading on {patched} hub blogs")


def main() -> None:
    food_posts = build_food_posts()
    all_posts = food_posts + TOPIC_POSTS
    slugs = []
    for post in all_posts:
        ensure_image(post)
        if post in TOPIC_POSTS:
            wc = word_count(post["body"])
            if wc < MIN_WORDS_TOPIC:
                raise SystemExit(f"too short: {post['slug']} ({wc})")
            print(f"topic {post['slug']} ~{wc} words")
        out = BLOGS / f"{post['slug']}.html"
        out.write_text(render_post(post), encoding="utf-8")
        slugs.append(post["slug"])
        print("wrote", out.name)

    patch_vercel_blog(slugs)
    patch_sitemap_paths([f"/blog/{s}" for s in slugs])
    update_search_gap(all_posts)
    update_aliases(all_posts)

    # Ensure new food html exists before discovery
    food_slugs = discover_food_slugs()
    hub = update_seo_hub(food_slugs)
    patch_vercel_hub("/foods-ibd")
    patch_sitemap_paths(["/foods-ibd"], priority="0.9")
    publish_hub(hub)

    patch_home_search_pins()
    patch_resource_library_pins()
    patch_changelog()

    from sync_resources_library import main as sync_resources  # noqa: E402
    from generate_home_engagement_data import main as gen_engagement  # noqa: E402
    from refresh_content_counts import main as refresh_counts  # noqa: E402
    from sync_sitemap import main as sync_sitemap  # noqa: E402
    from sync_site_updates_sections import main as sync_updates  # noqa: E402
    from sync_llms_txt import sync_llms_txt  # noqa: E402
    from generate_amp_pages import (  # noqa: E402
        BLOGS_AMP,
        amp_url_for,
        parse_blog_html,
        patch_canonical_amphtml,
        render_amp_blog,
    )

    sync_resources()
    gen_engagement()
    refresh_counts()
    sync_updates()
    sync_llms_txt()

    BLOGS_AMP.mkdir(parents=True, exist_ok=True)
    for slug in slugs:
        path = BLOGS / f"{slug}.html"
        post = parse_blog_html(path)
        if not post:
            print("WARN: amp skip", slug)
            continue
        (BLOGS_AMP / f"{slug}.html").write_text(render_amp_blog(post), encoding="utf-8")
        patch_canonical_amphtml(
            path,
            f"https://www.ibdpal.org/blog/{slug}",
            amp_url_for(f"/blog/{slug}"),
        )
        print("AMP", slug)
    sync_sitemap()
    print("Done.", len(slugs), "posts + /foods-ibd hub")


if __name__ == "__main__":
    main()
