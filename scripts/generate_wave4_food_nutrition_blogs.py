#!/usr/bin/env python3
# Prose style: do not use em dash. Use periods, commas, colons, or "|" in titles.
"""Generate Wave 4 food x IBD SEO blogs (lifestyle staples + remaining proteins)."""
from __future__ import annotations

import json
import re
import shutil
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOGS = ROOT / "blogs"
DATA = ROOT / "data" / "wave4-food-nutrition-posts.json"
SITEMAP = ROOT / "sitemap.xml"
VERCEL = ROOT / "vercel.json"
SITE = "https://www.ibdpal.org"

sys.path.insert(0, str(ROOT / "scripts"))
from generate_blog_posts import render_post  # noqa: E402

FALLBACK_IMAGE = BLOGS / "assets" / "low-residue" / "low-residue_1.jpg"

IMAGE_URLS = {
    "oatmeal-ibd": "https://images.unsplash.com/photo-1517673400267-0251440c45dc?auto=format&w=1200&q=80",
    "peanut-butter-ibd": "https://images.unsplash.com/photo-1508747703725-719777637510?auto=format&w=1200&q=80",
    "coffee-ibd": "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?auto=format&w=1200&q=80",
    "salmon-ibd": "https://images.unsplash.com/photo-1519708227418-c8fd9a32b7a2?auto=format&w=1200&q=80",
    "tofu-ibd": "https://images.unsplash.com/photo-1512058564366-18510be2db19?auto=format&w=1200&q=80",
    "lean-beef-ibd": "https://images.unsplash.com/photo-1588168333986-5078d3ae3976?auto=format&w=1200&q=80",
    "greek-yogurt-ibd": "https://images.unsplash.com/photo-1488477181946-6428a0291777?auto=format&w=1200&q=80",
    "tuna-ibd": "https://images.unsplash.com/photo-1467003909585-2f8a72700288?auto=format&w=1200&q=80",
    "tea-ibd": "https://images.unsplash.com/photo-1556679343-c7306c1976bc?auto=format&w=1200&q=80",
    "white-bread-ibd": "https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&w=1200&q=80",
    "chocolate-ibd": "https://images.unsplash.com/photo-1511381939415-e44015466834?auto=format&w=1200&q=80",
    "protein-shakes-ibd": "https://images.unsplash.com/photo-1579722820308-d74e571900a9?auto=format&w=1200&q=80",
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
<h3>Micronutrients and extras people ask about</h3>
<ul class="blog-list">{micros}</ul>

<h2>Flare versus remission: how many people approach {name_l}</h2>
<p>{f['tolerance_intro']}</p>
<h3>During a flare (when your team wants gentler textures)</h3>
<ul class="blog-list">{flare}</ul>
<h3>In remission (when variety is usually easier)</h3>
<ul class="blog-list">{rem}</ul>
<p>If you have strictures, recent surgery, or a short bowel history, fiber, skins, and chunky textures may need a different plan. Follow your clinician, not a generic list.</p>

<h2>Prep ideas that often feel kinder</h2>
<p>{f['prep']}</p>

<h2>Common myths about {name_l} and IBD</h2>
<ul class="blog-list">{myths}</ul>

<h2>How to track {name_l} with IBDPal</h2>
<p>Log the form (brand, brew strength, smooth vs crunchy, cooked texture), portion size, and symptoms for 24 to 48 hours. Patterns beat memory at clinic visits. See <a href="/blog/tracking-food-symptoms-ibdpal">tracking food and symptoms</a>.</p>

<h2>Questions for your gastroenterologist or dietitian</h2>
<ul class="blog-list">{questions}</ul>
<p>Bring your food log and recent labs so advice matches disease location, medicines, and nutrition gaps.</p>

<h2>When food questions become urgent</h2>
<p>Contact your care team promptly for severe pain, vomiting, inability to keep fluids down, heavy bleeding, fever, or rapid weight loss. See <a href="/flare-help">flare help</a> and <a href="/blog/when-to-go-er-ibd">when to go to the ER</a>.</p>

<p>Related reading: {related}. Hub: <a href="/ibd-nutrition">IBD nutrition</a>.</p>
""".strip()


FOODS: list[dict] = [
    {
        "slug": "oatmeal-ibd",
        "name": "Oatmeal",
        "title": "Oatmeal and IBD: Soluble Fiber, Flare Texture, and Prep Tips",
        "description": "Oatmeal with Crohn's or colitis: soluble fiber, instant vs steel-cut, flare porridge tips, and dietitian questions. Education only.",
        "category": "Nutrition · August 2026",
        "date_display": "August 28, 2026",
        "date_iso": "2026-08-28T16:00:00Z",
        "asset_dir": "oatmeal-ibd",
        "resource_category": "nutrition",
        "tags": ["oatmeal", "oats", "soluble fiber", "breakfast", "porridge", "Crohn's", "colitis", "nutrition"],
        "share": "Oatmeal and IBD: soluble fiber and flare tips. Education only.",
        "primary_kw": "oatmeal Crohn's disease",
        "secondary_kw": "oats ulcerative colitis",
        "nutrition_intro": (
            "Oatmeal is a breakfast staple that provides carbohydrate, soluble fiber (beta-glucan), and some protein and iron when enriched. "
            "Texture matters: smooth, well-cooked porridge is different from chunky steel-cut oats with skins and seeds mixed in."
        ),
        "macros": [
            ("Serving", "1/2 cup dry oats cooked (~40 g dry)"),
            ("Calories", "~150"),
            ("Carbohydrate", "~27 g"),
            ("Fiber", "~4 g (mostly soluble when cooked soft)"),
            ("Protein", "~5 g"),
            ("Fat", "~3 g"),
        ],
        "micros": [
            ("Iron and B vitamins", "Higher when oats are fortified"),
            ("Magnesium and zinc", "Modest contributions"),
            ("Beta-glucan", "Soluble fiber studied for cholesterol and gut comfort in general nutrition"),
        ],
        "tolerance_intro": (
            "Many people tolerate smooth oatmeal better than bran cereals during recovery phases. "
            "During strict low-residue flares, some teams prefer refined grains temporarily; oatmeal reintroduction is individualized."
        ),
        "flare_tips": [
            "Cook longer with extra fluid until silky; blend if lumps bother you",
            "Start with a small bowl; skip granola toppings, nuts, and raw fruit skins",
            "Instant plain oats can be smoother than undercooked steel-cut",
            "If fiber is fully restricted, use white toast or rice first, then ask when oats return",
        ],
        "remission_tips": [
            "Add ripe banana, smooth peanut butter, or lactose-free yogurt if tolerated",
            "Trial steel-cut oats once smooth oats sit well",
            "Watch flavored packets with sugar alcohols or inulin if those trigger you",
        ],
        "prep": (
            "Simmer with water or lactose-free milk, stirring until gluey-smooth. "
            "Overnight oats are colder and chewier; some guts prefer hot cooked porridge instead."
        ),
        "myths": [
            ("All fiber foods are banned in IBD.", "Soluble fiber foods are often reintroduced thoughtfully."),
            ("Gluten-free oats are required for every Crohn's patient.", "Only needed with celiac disease or confirmed oat sensitivity."),
            ("Oatmeal cures inflammation.", "It supports nutrition; it is not biologic therapy."),
        ],
        "questions": [
            "Where do oats fit on my current residue or FODMAP plan?",
            "Should I prefer instant, rolled, or steel-cut while symptoms settle?",
            "How do we use oatmeal toward fiber goals in remission?",
        ],
        "related": [
            ("/blog/fiber-and-ibd-diet", "fiber and IBD"),
            ("/blog/white-rice-ibd-flare", "white rice"),
            ("/blog/banana-ibd-crohns-colitis", "bananas"),
        ],
    },
    {
        "slug": "peanut-butter-ibd",
        "name": "Peanut butter",
        "title": "Peanut Butter and IBD: Calories, Smooth Texture, and Portion Tips",
        "description": "Peanut butter with Crohn's or colitis: smooth vs crunchy, calories for underweight patients, FODMAP notes, and clinic questions. Education only.",
        "category": "Nutrition · August 2026",
        "date_display": "August 28, 2026",
        "date_iso": "2026-08-28T18:00:00Z",
        "asset_dir": "peanut-butter-ibd",
        "resource_category": "nutrition",
        "tags": ["peanut butter", "peanuts", "protein", "calories", "smooth", "Crohn's", "colitis", "nutrition"],
        "share": "Peanut butter and IBD: smooth portions and calories. Education only.",
        "primary_kw": "peanut butter Crohn's",
        "secondary_kw": "peanut butter ulcerative colitis",
        "nutrition_intro": (
            "Peanut butter packs calories, plant protein, and fat into a small spoon. "
            "That helps underweight patients, while large sticky servings or crunchy bits can feel heavy during flares."
        ),
        "macros": [
            ("Serving", "2 tablespoons (~32 g)"),
            ("Calories", "~190"),
            ("Fat", "~16 g"),
            ("Protein", "~7 to 8 g"),
            ("Carbohydrate", "~6 to 8 g"),
            ("Fiber", "~2 g"),
        ],
        "micros": [
            ("Niacin, vitamin E, magnesium", "Useful everyday micronutrients"),
            ("Sodium", "Varies widely by brand"),
            ("Added sugar", "Check labels on sweetened jars"),
        ],
        "tolerance_intro": (
            "Smooth peanut butter on soft white toast is a classic gentle calorie booster. "
            "Crunchy styles, whole peanuts, and large spoonfuls of natural oil-separated butter are harder for some guts."
        ),
        "flare_tips": [
            "Choose smooth, well-stirred butter; start with 1 tablespoon",
            "Spread thin on white toast or swirl into oatmeal if oats are allowed",
            "Avoid crunchy PB and whole peanuts during strictures or high urgency",
            "If fat worsens diarrhea, pause and retry later with your dietitian",
        ],
        "remission_tips": [
            "Use as a snack with banana or apple if fruit is tolerated",
            "Natural vs conventional is preference; watch oil separation and sodium",
            "Powdered peanut butter is lower fat if that helps your stool pattern",
        ],
        "prep": (
            "Stir natural jars fully so oil is mixed. Warm a spoonful briefly for easier spreading. "
            "Keep portions measured; it is easy to overshoot calories or fat in a few scoops."
        ),
        "myths": [
            ("All nuts are forbidden forever in Crohn's.", "Smooth butters are different from whole nuts for many people."),
            ("Peanut butter causes IBD.", "No evidence that PB causes Crohn's or colitis."),
            ("Only protein powder beats peanut butter.", "PB is a practical whole-food calorie tool when tolerated."),
        ],
        "questions": [
            "Is smooth peanut butter okay on my stricture-aware plan?",
            "How much PB fits my weight-gain goals without worsening urgency?",
            "Should I prefer powdered or regular for fat tolerance?",
        ],
        "related": [
            ("/guides/protein-healing-ibd-flare", "protein during flares"),
            ("/blog/oatmeal-ibd", "oatmeal"),
            ("/blog/avocado-ibd", "avocado fats"),
        ],
    },
    {
        "slug": "coffee-ibd",
        "name": "Coffee",
        "title": "Coffee and IBD: Caffeine, Urgency, and When to Cut Back",
        "description": "Coffee with Crohn's or colitis: caffeine, acidity, decaf options, flare timing, and clinic questions. Education only.",
        "category": "Nutrition · August 2026",
        "date_display": "August 29, 2026",
        "date_iso": "2026-08-29T12:00:00Z",
        "asset_dir": "coffee-ibd",
        "resource_category": "nutrition",
        "tags": ["coffee", "caffeine", "urgency", "breakfast", "decaf", "Crohn's", "colitis", "nutrition"],
        "share": "Coffee and IBD: caffeine, urgency, and cutback tips. Education only.",
        "primary_kw": "coffee Crohn's disease",
        "secondary_kw": "coffee ulcerative colitis caffeine",
        "nutrition_intro": (
            "Coffee itself has almost no macros, but caffeine and organic acids can stimulate the gut and increase urgency for some people. "
            "It is one of the most searched lifestyle questions in IBD, alongside bathroom timing for work and school."
        ),
        "macros": [
            ("Serving", "8 oz black coffee"),
            ("Calories", "~2"),
            ("Carbohydrate / Protein / Fat", "negligible black"),
            ("Caffeine", "~80 to 100 mg typical cup (varies)"),
            ("Add-ins", "cream, sugar, and syrups change macros a lot"),
        ],
        "micros": [
            ("Polyphenols", "Present in coffee; not an IBD therapy"),
            ("Potassium", "Small amount"),
            ("Milk add-ins", "Can add calcium if dairy is tolerated"),
        ],
        "tolerance_intro": (
            "Some patients drink coffee daily in remission with no issue. Others notice looser stools within an hour of a strong cup. "
            "Empty-stomach espresso hits differently than coffee with breakfast."
        ),
        "flare_tips": [
            "Consider pausing or switching to half-caf / decaf during high urgency weeks",
            "Never use coffee as a substitute for fluids when dehydrated",
            "Skip large cold-brew concentrates if caffeine spikes symptoms",
            "If you continue, pair with food and sip smaller amounts",
        ],
        "remission_tips": [
            "Find your threshold: one small cup may be fine when three are not",
            "Trial lower-acid or cold brew styles if acidity bothers you",
            "Watch sugar-alcohol syrups in coffee shop drinks",
        ],
        "prep": (
            "Brew milder and shorter if you are testing tolerance. Decaf still has some caffeine. "
            "Keep a bathroom plan for commute days if coffee is non-negotiable for alertness."
        ),
        "myths": [
            ("Coffee causes Crohn's disease.", "Coffee does not cause IBD; it may affect symptoms for some."),
            ("Decaf is identical to water for the gut.", "Decaf can still have acids and small caffeine amounts."),
            ("Everyone with colitis must quit coffee forever.", "Many people return to modest amounts in remission."),
        ],
        "questions": [
            "Should I pause caffeine while calprotectin or symptoms are elevated?",
            "How does coffee interact with my dehydration risk?",
            "Is tea or decaf a better bridge for me?",
        ],
        "related": [
            ("/blog/alcohol-caffeine-ibd", "alcohol and caffeine overview"),
            ("/blog/tea-ibd", "tea and IBD"),
            ("/blog/hydration-tips-ibd", "hydration tips"),
        ],
    },
    {
        "slug": "salmon-fish-ibd",
        "name": "Salmon and fatty fish",
        "title": "Salmon and Fatty Fish With IBD: Protein, Omega-3, and Cooking Tips",
        "description": "Salmon with Crohn's or colitis: protein, omega-3 fats, tender cooking, flare portions, and dietitian questions. Education only.",
        "category": "Nutrition · August 2026",
        "date_display": "August 29, 2026",
        "date_iso": "2026-08-29T14:00:00Z",
        "asset_dir": "salmon-ibd",
        "resource_category": "nutrition",
        "tags": ["salmon", "fish", "omega-3", "protein", "seafood", "Crohn's", "colitis", "nutrition"],
        "share": "Salmon and IBD: protein and omega-3 tips. Education only.",
        "primary_kw": "salmon Crohn's disease",
        "secondary_kw": "fish ulcerative colitis diet",
        "nutrition_intro": (
            "Salmon is a soft, high-protein fish rich in EPA and DHA omega-3 fats. "
            "It fits many Mediterranean-style IBD education plates when fat tolerance allows."
        ),
        "macros": [
            ("Serving", "3 oz cooked salmon (~85 g)"),
            ("Calories", "~150 to 180"),
            ("Protein", "~22 g"),
            ("Fat", "~7 to 11 g (higher in fattier cuts)"),
            ("Carbohydrate", "0 g"),
            ("Omega-3", "notable EPA/DHA versus many other proteins"),
        ],
        "micros": [
            ("Vitamin D and B12", "Helpful in IBD diets when fish is eaten regularly"),
            ("Selenium", "Present in seafood"),
            ("Sodium", "Watch smoked salmon and packaged products"),
        ],
        "tolerance_intro": (
            "Moist baked or poached salmon is usually easier than fried fish sandwiches. "
            "During fat-sensitive flares, smaller portions of leaner white fish may feel better first."
        ),
        "flare_tips": [
            "Bake or poach until flaky; remove skin if it bothers you",
            "Start with 2 to 3 ounces alongside white rice",
            "Avoid deep-fried batter and spicy blackened rubs during bad weeks",
            "Skip heavy cream sauces if fat worsens urgency",
        ],
        "remission_tips": [
            "Include fatty fish a few times weekly if desired and tolerated",
            "Canned salmon mashed finely can be a convenient protein",
            "Pair with soft vegetables you already tolerate",
        ],
        "prep": (
            "Cook to a safe internal temperature and rest briefly so juices redistribute. "
            "Flake finely for easier chewing. Leftovers reheat gently with a splash of broth to stay moist."
        ),
        "myths": [
            ("Fish oil capsules replace eating fish and IBD medicines.", "Food helps; medicines still matter."),
            ("All seafood triggers colitis.", "Tolerance is individual; plain fish is often well liked."),
            ("Raw fish is required for omega-3.", "Cooked salmon still provides EPA/DHA."),
        ],
        "questions": [
            "How much fatty fish fits my fat tolerance and calorie goals?",
            "Is smoked salmon okay with my sodium limits?",
            "Should I use food omega-3 before supplements?",
        ],
        "related": [
            ("/blog/omega-3-ibd", "omega-3 deep dive"),
            ("/blog/mediterranean-diet-autoimmune", "Mediterranean-style eating"),
            ("/blog/chicken-protein-ibd", "chicken protein"),
        ],
    },
    {
        "slug": "tofu-soy-ibd",
        "name": "Tofu",
        "title": "Tofu and Soy With IBD: Soft Protein, Calcium-Set Options, and Prep Tips",
        "description": "Tofu with Crohn's or colitis: soft vs firm, calcium-set tofu, soy tolerance, and dietitian questions. Education only.",
        "category": "Nutrition · August 2026",
        "date_display": "August 29, 2026",
        "date_iso": "2026-08-29T16:00:00Z",
        "asset_dir": "tofu-ibd",
        "resource_category": "nutrition",
        "tags": ["tofu", "soy", "plant protein", "calcium", "vegan", "Crohn's", "colitis", "nutrition"],
        "share": "Tofu and IBD: soft plant protein tips. Education only.",
        "primary_kw": "tofu Crohn's disease",
        "secondary_kw": "soy ulcerative colitis protein",
        "nutrition_intro": (
            "Tofu is coagulated soy milk that provides plant protein with a soft texture when silken or soft styles are chosen. "
            "Calcium-set tofu can also support bone-friendly eating when dairy is limited."
        ),
        "macros": [
            ("Serving", "3 oz soft or firm tofu (~85 g)"),
            ("Calories", "~60 to 90 depending on firmness"),
            ("Protein", "~6 to 10 g"),
            ("Fat", "~3 to 5 g"),
            ("Carbohydrate", "~2 g"),
            ("Fiber", "low to modest"),
        ],
        "micros": [
            ("Calcium", "Higher when set with calcium sulfate; check labels"),
            ("Iron", "Non-heme iron; pair with vitamin C foods when tolerated"),
            ("Isoflavones", "Plant compounds in soy; not an IBD drug"),
        ],
        "tolerance_intro": (
            "Silken or soft tofu in smooth soups is often easier than fried firm cubes with chewy crusts. "
            "Whole soybeans and high-fiber soy foods differ from smooth tofu."
        ),
        "flare_tips": [
            "Use silken tofu blended into broth-based soups",
            "Avoid deep-fried tofu and heavy chili sauces during flares",
            "Start with small portions if soy is new to you",
            "Skip edamame and soy nuts if residue is restricted",
        ],
        "remission_tips": [
            "Bake or gently pan-cook soft cubes with mild seasoning",
            "Choose calcium-set tofu if dairy-free calcium is a goal",
            "Rotate with eggs, fish, or poultry for protein variety",
        ],
        "prep": (
            "Press firm tofu lightly if you need less water, or skip pressing for softer texture. "
            "Cube small and cook until warm through. Blend silken tofu into smooth savory porridge-style bowls."
        ),
        "myths": [
            ("Soy is always hormonal and unsafe.", "Moderate whole soy foods are accepted in many nutrition guidelines; ask your clinician for personal concerns."),
            ("Vegan diets cure IBD.", "Plant patterns can be healthy with planning; they do not replace medical therapy."),
            ("All soy is high FODMAP the same way.", "Servings and products differ; work with a dietitian."),
        ],
        "questions": [
            "Is soft tofu a good dairy-free protein for me?",
            "Which tofu labels give the most calcium?",
            "How do we build a vegetarian IBD plate without underdoing protein?",
        ],
        "related": [
            ("/blog/calcium-ibd", "calcium and IBD"),
            ("/blog/protein-meal-plan-ibd-remission", "protein meal ideas"),
            ("/guides/protein-healing-ibd-flare", "protein in flares"),
        ],
    },
    {
        "slug": "lean-beef-ibd",
        "name": "Lean beef",
        "title": "Lean Beef and IBD: Iron-Rich Protein Without Tough Cuts",
        "description": "Lean beef with Crohn's or colitis: heme iron, tender cuts, flare cooking tips, and clinic questions. Education only.",
        "category": "Nutrition · August 2026",
        "date_display": "August 29, 2026",
        "date_iso": "2026-08-29T18:00:00Z",
        "asset_dir": "lean-beef-ibd",
        "resource_category": "nutrition",
        "tags": ["beef", "lean beef", "iron", "protein", "red meat", "Crohn's", "colitis", "nutrition"],
        "share": "Lean beef and IBD: iron and tender cooking tips. Education only.",
        "primary_kw": "beef Crohn's disease diet",
        "secondary_kw": "red meat ulcerative colitis",
        "nutrition_intro": (
            "Lean beef is a dense source of protein and heme iron, which is often better absorbed than plant iron. "
            "That makes it relevant for IBD anemia discussions, while tough, fatty, or processed meats are a different story."
        ),
        "macros": [
            ("Serving", "3 oz cooked lean beef (~85 g)"),
            ("Calories", "~150 to 180"),
            ("Protein", "~22 to 26 g"),
            ("Fat", "~5 to 9 g for lean cuts"),
            ("Carbohydrate", "0 g"),
            ("Iron", "notable heme iron versus many poultry servings"),
        ],
        "micros": [
            ("Heme iron and zinc", "Support anemia and repair nutrition goals"),
            ("B12 and B vitamins", "Helpful when appetite is low"),
            ("Sodium", "High in many processed beef products"),
        ],
        "tolerance_intro": (
            "Ground lean beef cooked soft, or tenderloin sliced thin, is usually easier than steaks with gristle, sausages, or charred barbecue. "
            "Processed meats bring sodium and additives that deserve a separate look."
        ),
        "flare_tips": [
            "Choose 90%+ lean ground beef; cook thoroughly and drain fat; crumble finely",
            "Serve with white rice or peeled potato",
            "Avoid sausages, jerky, and tough steaks during flares or strictures",
            "Keep spices mild if heat worsens urgency",
        ],
        "remission_tips": [
            "Rotate beef with fish and poultry for variety",
            "Use beef strategically when iron food sources are a goal",
            "Limit ultra-processed meats even in remission for overall health",
        ],
        "prep": (
            "Slow-cook or simmer ground beef in broth-based dishes until soft. "
            "Slice whole-muscle cuts thin against the grain. Food safety: cook ground beef to a safe temperature."
        ),
        "myths": [
            ("Red meat causes Crohn's.", "IBD causes are complex; plain lean beef is not a proven universal trigger."),
            ("You must go fully vegetarian for colitis.", "Many patients include lean meats under dietitian guidance."),
            ("Any burger is the same as lean beef.", "Fat level, bun toppings, and processing change the meal a lot."),
        ],
        "questions": [
            "Can lean beef help my iron-deficiency plan alongside therapy?",
            "Which cuts are safest with my stricture history?",
            "How often should red meat appear in my weekly menu?",
        ],
        "related": [
            ("/guides/iron-deficiency-nutrition-ibd", "iron deficiency nutrition"),
            ("/blog/anemia-iron-deficiency-ibd", "anemia overview"),
            ("/blog/zinc-ibd", "zinc"),
        ],
    },
    {
        "slug": "greek-yogurt-ibd",
        "name": "Greek yogurt",
        "title": "Greek Yogurt and IBD: Protein, Lactose, and Probiotic Notes",
        "description": "Greek yogurt with Crohn's or colitis: protein, lactose tolerance, smooth textures, probiotics, and clinic questions. Education only.",
        "category": "Nutrition · August 2026",
        "date_display": "August 30, 2026",
        "date_iso": "2026-08-30T12:00:00Z",
        "asset_dir": "greek-yogurt-ibd",
        "resource_category": "nutrition",
        "tags": ["greek yogurt", "yogurt", "lactose", "protein", "probiotics", "dairy", "Crohn's", "colitis", "nutrition"],
        "share": "Greek yogurt and IBD: protein and lactose tips. Education only.",
        "primary_kw": "greek yogurt Crohn's",
        "secondary_kw": "yogurt ulcerative colitis",
        "nutrition_intro": (
            "Greek yogurt is strained yogurt with more protein per spoon than many regular yogurts. "
            "It can supply calcium and live cultures, but lactose tolerance and add-ins (granola, sugar alcohols) still matter."
        ),
        "macros": [
            ("Serving", "3/4 cup plain nonfat Greek yogurt (~170 g)"),
            ("Calories", "~100"),
            ("Protein", "~15 to 18 g"),
            ("Carbohydrate", "~6 g (plain)"),
            ("Fat", "~0 to 5 g depending on milkfat"),
            ("Calcium", "notable; check label"),
        ],
        "micros": [
            ("Calcium and phosphorus", "Support bone-friendly eating"),
            ("B12 and riboflavin", "Present in dairy yogurts"),
            ("Live cultures", "Strain-dependent; not a guaranteed IBD therapy"),
        ],
        "tolerance_intro": (
            "Many people with lactose intolerance tolerate yogurt better than milk because cultures help digest lactose, but not everyone. "
            "Lactose-free Greek-style options exist. During flares, plain smooth yogurt beats crunchy mix-ins."
        ),
        "flare_tips": [
            "Choose plain, smooth yogurt; start with a few spoonfuls",
            "Skip granola, seeds, and candy toppings",
            "If dairy worsens symptoms, trial lactose-free or pause and use alternatives",
            "Avoid sugar-alcohol sweetened yogurts if they loosen stools",
        ],
        "remission_tips": [
            "Use as a high-protein snack or breakfast base",
            "Pair with soft fruit you tolerate",
            "Full-fat versus nonfat is preference and calorie need",
        ],
        "prep": (
            "Keep cold and stir until smooth. Use as a sour-cream style topping on mild savory dishes if tolerated. "
            "Do not assume every yogurt's probiotic strain matches research products."
        ),
        "myths": [
            ("All dairy is forbidden in IBD.", "Many patients use yogurt successfully; see lactose guidance."),
            ("Greek yogurt probiotics heal Crohn's.", "Helpful for some comfort; not a substitute for prescribed therapy."),
            ("More live cultures always means better.", "Dose, strain, and your disease type matter."),
        ],
        "questions": [
            "Is lactose-free Greek yogurt better for me than regular?",
            "How can yogurt help me hit protein targets?",
            "Should I use yogurt cultures instead of a probiotic pill?",
        ],
        "related": [
            ("/blog/dairy-lactose-ibd", "dairy and lactose"),
            ("/blog/probiotics-ibd-gut-health", "probiotics overview"),
            ("/blog/calcium-ibd", "calcium"),
        ],
    },
    {
        "slug": "tuna-ibd",
        "name": "Tuna",
        "title": "Tuna and IBD: Convenient Protein, Mercury Notes, and Prep Tips",
        "description": "Tuna with Crohn's or colitis: canned vs fresh, protein convenience, mercury guidance, and dietitian questions. Education only.",
        "category": "Nutrition · August 2026",
        "date_display": "August 30, 2026",
        "date_iso": "2026-08-30T14:00:00Z",
        "asset_dir": "tuna-ibd",
        "resource_category": "nutrition",
        "tags": ["tuna", "canned tuna", "fish", "protein", "mercury", "Crohn's", "colitis", "nutrition"],
        "share": "Tuna and IBD: convenient protein tips. Education only.",
        "primary_kw": "tuna Crohn's disease",
        "secondary_kw": "canned tuna colitis",
        "nutrition_intro": (
            "Tuna is a lean fish protein that is easy to keep on the shelf. "
            "Canned tuna in water is a common flare-friendly protein when mixed soft, while fried tuna sandwiches and spicy salads are less gentle."
        ),
        "macros": [
            ("Serving", "3 oz canned tuna in water, drained (~85 g)"),
            ("Calories", "~90 to 110"),
            ("Protein", "~20 g"),
            ("Fat", "~1 g (oil-packed is higher)"),
            ("Carbohydrate", "0 g"),
            ("Sodium", "can be high; check labels"),
        ],
        "micros": [
            ("Selenium and B12", "Helpful seafood micronutrients"),
            ("Omega-3", "Present but usually less than fatty salmon per typical can"),
            ("Mercury", "Varies by tuna type; follow FDA fish advice for pregnancy and children"),
        ],
        "tolerance_intro": (
            "Mashed canned tuna with a little mayo or broth on soft bread is a practical low-cook meal. "
            "Chunky salads with raw onion and celery seed can worsen symptoms even if tuna itself is fine."
        ),
        "flare_tips": [
            "Choose tuna in water; drain well; mash finely",
            "Keep mix-ins simple: soft bread, white rice, mild mayo if fat is okay",
            "Avoid spicy tuna rolls with raw vegetables during flares",
            "Watch sodium if bloating or blood pressure is a concern",
        ],
        "remission_tips": [
            "Rotate tuna with salmon and poultry for variety",
            "Follow pregnancy fish frequency guidance if applicable",
            "Try baked fresh tuna steaks cooked moist if desired",
        ],
        "prep": (
            "Flake thoroughly so no dry chunks remain. Mix with a moist binder. "
            "Refrigerate leftovers promptly. For lower sodium, rinse briefly or choose low-salt cans."
        ),
        "myths": [
            ("Canned tuna is junk food with no place in IBD.", "It can be a useful lean protein when prepared simply."),
            ("All tuna is identical for mercury.", "Albacore and light tuna differ; check current FDA guidance."),
            ("Tuna causes flares by itself.", "Add-ins and sauces are frequent culprits."),
        ],
        "questions": [
            "How often can I eat tuna given my age and pregnancy status?",
            "Is oil-packed or water-packed better for my fat tolerance?",
            "How do we use tuna on low-energy flare days?",
        ],
        "related": [
            ("/blog/salmon-fish-ibd", "salmon and fatty fish"),
            ("/blog/protein-meal-plan-ibd-remission", "protein meals"),
            ("/blog/omega-3-ibd", "omega-3"),
        ],
    },
    {
        "slug": "tea-ibd",
        "name": "Tea",
        "title": "Tea and IBD: Caffeine, Herbal Options, and Hydration Tips",
        "description": "Tea with Crohn's or colitis: black vs green vs herbal, caffeine, tannins, flare sipping tips, and clinic questions. Education only.",
        "category": "Nutrition · August 2026",
        "date_display": "August 30, 2026",
        "date_iso": "2026-08-30T16:00:00Z",
        "asset_dir": "tea-ibd",
        "resource_category": "nutrition",
        "tags": ["tea", "green tea", "herbal tea", "caffeine", "hydration", "Crohn's", "colitis", "nutrition"],
        "share": "Tea and IBD: caffeine and herbal options. Education only.",
        "primary_kw": "tea Crohn's disease",
        "secondary_kw": "green tea ulcerative colitis",
        "nutrition_intro": (
            "Tea ranges from caffeinated black and green teas to caffeine-free herbal infusions. "
            "It can support fluid intake, but strong tannins and caffeine still affect urgency for some people."
        ),
        "macros": [
            ("Serving", "8 oz brewed tea, unsweetened"),
            ("Calories", "~0 to 2"),
            ("Caffeine", "varies: black > green > many herbals (often ~0)"),
            ("Add-ins", "milk, sugar, and syrups change the drink"),
            ("Oxalates", "Higher in some black teas; relevant for some stone histories"),
        ],
        "micros": [
            ("Polyphenols / catechins", "Studied in general nutrition; not IBD cures"),
            ("Fluoride", "Present in tea leaves in small amounts"),
            ("Herbal actives", "Peppermint, ginger, and others differ; quality varies"),
        ],
        "tolerance_intro": (
            "Weak tea with food may sit better than strong coffee-like brews on an empty stomach. "
            "Herbal does not automatically mean safe: senna teas are laxatives, and some herbs interact with medicines."
        ),
        "flare_tips": [
            "Prefer weak black/green tea or caffeine-free herbal options your clinician is okay with",
            "Avoid senna or strong laxative teas",
            "Sip warm, not scalding, if mouth sores are present",
            "Count tea toward fluids but still use oral rehydration when diarrhea is significant",
        ],
        "remission_tips": [
            "Trial green tea if you want less caffeine than coffee",
            "Iced tea: watch sugar and sugar alcohols",
            "Keep a simple ingredient list; fancy detox blends are marketing",
        ],
        "prep": (
            "Steep shorter for milder tannins. Dilute with hot water. "
            "If using milk, choose lactose-free if needed. Read herbal labels for medicine interactions."
        ),
        "myths": [
            ("Herbal tea cannot affect IBD.", "Some herbs loosen stools or interact with drugs."),
            ("Green tea heals colitis.", "Interesting research exists in labs; it is not a replacement for prescribed care."),
            ("Tea dehydrates you always.", "Moderate tea still contributes fluid for most people; caffeine response varies."),
        ],
        "questions": [
            "Which teas are safe with my medications?",
            "Should I switch from coffee to tea during flares?",
            "Do tannins or oxalates matter with my stone or anemia history?",
        ],
        "related": [
            ("/blog/coffee-ibd", "coffee and IBD"),
            ("/blog/alcohol-caffeine-ibd", "alcohol and caffeine"),
            ("/blog/hydration-tips-ibd", "hydration"),
        ],
    },
    {
        "slug": "white-bread-ibd",
        "name": "White bread",
        "title": "White Bread and IBD: Low-Residue Carbs and Sandwich Tips",
        "description": "White bread with Crohn's or colitis: refined carbs, flare sandwiches, enrichment nutrients, and dietitian questions. Education only.",
        "category": "Nutrition · August 2026",
        "date_display": "August 30, 2026",
        "date_iso": "2026-08-30T18:00:00Z",
        "asset_dir": "white-bread-ibd",
        "resource_category": "nutrition",
        "tags": ["white bread", "bread", "refined grains", "low residue", "sandwich", "Crohn's", "colitis", "nutrition"],
        "share": "White bread and IBD: low-residue carb tips. Education only.",
        "primary_kw": "white bread Crohn's flare",
        "secondary_kw": "white bread ulcerative colitis",
        "nutrition_intro": (
            "White bread is a refined grain staple on many low-residue menus because it is lower in insoluble fiber than whole-grain loaves. "
            "Enriched breads add back some B vitamins and iron."
        ),
        "macros": [
            ("Serving", "1 slice (~25 to 30 g)"),
            ("Calories", "~70 to 80"),
            ("Carbohydrate", "~13 to 15 g"),
            ("Fiber", "~0.5 to 1 g"),
            ("Protein", "~2 g"),
            ("Fat", "~1 g"),
        ],
        "micros": [
            ("Enriched B vitamins and iron", "Check the label"),
            ("Sodium", "Varies by brand"),
            ("Folic acid", "Often added in enriched flour products"),
        ],
        "tolerance_intro": (
            "Soft white bread without seeds is a common flare carbohydrate with eggs, turkey, or tuna. "
            "Seeded, sprouted, and heavy whole-grain breads are usually later reintroductions."
        ),
        "flare_tips": [
            "Choose soft sandwich bread without seeds or nuts",
            "Toast lightly if you prefer; avoid rock-hard crusts if they feel abrasive",
            "Keep fillings tender: egg, turkey, smooth PB",
            "Skip raw onion, big salads, and crunchy slaws in the sandwich during flares",
        ],
        "remission_tips": [
            "Gradually trial higher-fiber breads if desired",
            "Use bread as a vehicle for protein, not only jam",
            "Watch gluten-free breads: some are gum-heavy and change stool form",
        ],
        "prep": (
            "Store properly so bread stays soft. Slightly stale bread can be warmed. "
            "French toast made soft can be another gentle option when eggs are tolerated."
        ),
        "myths": [
            ("White bread is poison and has no role in IBD.", "It can be a practical flare carb when fiber is limited."),
            ("You must stay on white bread forever.", "Long-term goals usually re-expand grains with guidance."),
            ("Gluten-free bread is automatically easier for every IBD patient.", "Only required with celiac or confirmed sensitivity."),
        ],
        "questions": [
            "How long should I stay on refined grains during this flare?",
            "When can I reintroduce whole-grain bread?",
            "Do enriched breads help my folate or iron intake?",
        ],
        "related": [
            ("/blog/white-rice-ibd-flare", "white rice"),
            ("/blog/low-residue-diet-flare", "low-residue diet"),
            ("/blog/gluten-wheat-ibd", "gluten and wheat"),
        ],
    },
    {
        "slug": "chocolate-ibd",
        "name": "Chocolate",
        "title": "Chocolate and IBD: Cocoa, Fat, Sugar Alcohols, and Portion Tips",
        "description": "Chocolate with Crohn's or colitis: cocoa, milk vs dark, sugar alcohols in sugar-free candy, and clinic questions. Education only.",
        "category": "Nutrition · August 2026",
        "date_display": "August 31, 2026",
        "date_iso": "2026-08-31T12:00:00Z",
        "asset_dir": "chocolate-ibd",
        "resource_category": "nutrition",
        "tags": ["chocolate", "cocoa", "dessert", "sugar alcohols", "caffeine", "Crohn's", "colitis", "nutrition"],
        "share": "Chocolate and IBD: portions and sugar-alcohol cautions. Education only.",
        "primary_kw": "chocolate Crohn's disease",
        "secondary_kw": "chocolate ulcerative colitis",
        "nutrition_intro": (
            "Chocolate is a comfort food with fat, sugar, and small amounts of caffeine and theobromine from cocoa. "
            "Quality and portion matter more than guilt: sugar-free chocolates with sugar alcohols are a frequent hidden trigger."
        ),
        "macros": [
            ("Serving", "1 oz (~28 g) milk or dark chocolate"),
            ("Calories", "~140 to 170"),
            ("Fat", "~8 to 12 g"),
            ("Carbohydrate", "~15 to 20 g"),
            ("Protein", "~2 g"),
            ("Fiber", "higher in very dark bars with cocoa solids"),
        ],
        "micros": [
            ("Magnesium and iron", "Small amounts in darker chocolate"),
            ("Caffeine / theobromine", "Can stimulate some guts"),
            ("Added dairy", "Milk chocolate may bother lactose-intolerant patients"),
        ],
        "tolerance_intro": (
            "A small square after a meal may sit better than a large bag of candy on an empty stomach. "
            "Very high-cocoa bars are more bitter and fibrous; milk chocolate is softer but may include lactose."
        ),
        "flare_tips": [
            "Consider pausing chocolate during high urgency weeks if it worsens symptoms",
            "Avoid sugar-free chocolates sweetened with sugar alcohols (sorbitol, maltitol)",
            "If trialing, one small square of smooth milk chocolate may be gentler than seed-filled dark bark",
            "Skip cocoa powder drinks with sugar alcohols or heavy cream if fat is an issue",
        ],
        "remission_tips": [
            "Keep portions intentional; log how you feel",
            "Choose simple ingredient bars over candy with nuts and dried fruit if residue is a concern",
            "Hot cocoa made mild can be a comfort fluid with calories",
        ],
        "prep": (
            "Melt into a smooth sauce over tolerated fruit or rice pudding if that is your style. "
            "Read labels for inulin, chicory root, and sugar alcohols in 'high fiber' chocolate marketing."
        ),
        "myths": [
            ("Dark chocolate is always healthier for IBD.", "Higher cocoa can mean more fiber and bitterness; tolerance varies."),
            ("Sugar-free chocolate is safer for colitis.", "Sugar alcohols often worsen diarrhea."),
            ("Chocolate causes Crohn's.", "No evidence it causes IBD."),
        ],
        "questions": [
            "Do sugar alcohols explain my symptoms after 'diet' candy?",
            "Is a small chocolate allowance okay in remission?",
            "Could caffeine in chocolate affect my sleep or urgency?",
        ],
        "related": [
            ("/blog/coffee-ibd", "coffee"),
            ("/blog/magnesium-ibd", "magnesium"),
            ("/blog/fodmap-diet-crohns-colitis", "FODMAP overview"),
        ],
    },
    {
        "slug": "protein-shakes-ons-ibd",
        "name": "Protein shakes and oral nutrition supplements",
        "title": "Protein Shakes and ONS With IBD: When Liquids Help",
        "description": "Protein shakes and oral nutrition supplements with Crohn's or colitis: ONS basics, lactose-free options, flare calories, and clinic questions. Education only.",
        "category": "Nutrition · August 2026",
        "date_display": "August 31, 2026",
        "date_iso": "2026-08-31T14:00:00Z",
        "asset_dir": "protein-shakes-ibd",
        "resource_category": "nutrition",
        "tags": ["protein shake", "ONS", "oral nutrition supplement", "Ensure", "Boost", "calories", "Crohn's", "colitis", "nutrition"],
        "share": "Protein shakes and ONS with IBD: when liquids help. Education only.",
        "primary_kw": "protein shake Crohn's",
        "secondary_kw": "oral nutrition supplement colitis",
        "nutrition_intro": (
            "Protein shakes and oral nutrition supplements (ONS) are liquid or semi-liquid products used when solid food intake is too low. "
            "They are tools for calories, protein, and sometimes micronutrients, not magic cures."
        ),
        "macros": [
            ("Serving", "varies widely by product (often 8 to 12 oz)"),
            ("Calories", "commonly ~200 to 400+ per bottle"),
            ("Protein", "commonly ~10 to 30 g"),
            ("Fat and carbohydrate", "formula-dependent"),
            ("Fiber", "some versions add fiber; others are low residue style"),
        ],
        "micros": [
            ("Vitamins and minerals", "Many ONS are fortified; check labels versus your labs"),
            ("Lactose", "Lactose-free medical formulas are common"),
            ("Sugar and sweeteners", "Can affect taste and stool for some people"),
        ],
        "tolerance_intro": (
            "Ready-to-drink ONS and homemade smooth blends help when chewing hurts or appetite is tiny. "
            "High-fiber 'gut health' powders and sugar-alcohol protein bars are not the same as clinician-recommended ONS."
        ),
        "flare_tips": [
            "Ask your team which ONS fits your flare (calorie density, lactose-free, low fiber)",
            "Sip slowly chilled; stop if bloating spikes",
            "Use shakes between meals, not only as a reason to skip all solids forever without guidance",
            "Avoid unregulated detox shakes marketed for IBD",
        ],
        "remission_tips": [
            "Transition toward food-first protein when appetite returns",
            "Keep ONS as a backup for travel, infusion days, or low-appetite weeks",
            "Homemade shakes with tolerated ingredients can work if macros are planned",
        ],
        "prep": (
            "Shake bottles well. Homemade versions: blend smooth without seeds if residue is limited. "
            "Store opened products per label. Track which brands your gut prefers in IBDPal."
        ),
        "myths": [
            ("Any grocery protein powder is a medical ONS.", "Formulas differ; medical ONS are designed for incomplete intake."),
            ("Shakes replace the need to treat inflammation.", "Nutrition support helps; IBD therapy still matters."),
            ("More protein powder is always better.", "Kidneys, taste fatigue, and GI tolerance set limits."),
        ],
        "questions": [
            "Which ONS brand and schedule fit my weight and labs?",
            "Should I use shakes with partial enteral nutrition plans?",
            "How do we move from shakes back to solid meals?",
        ],
        "related": [
            ("/blog/enteral-nutrition-ibd", "enteral nutrition"),
            ("/guides/protein-healing-ibd-flare", "protein in flares"),
            ("/blog/exclusive-vs-partial-enteral-nutrition-crohns", "EEN vs PEN"),
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
    marker = "<!-- wave4-food-nutrition-blogs -->"
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
        "  <!-- wave3-food-nutrition-blogs -->",
        "  <!-- wave2-food-nutrition-blogs -->",
        "  <!-- wave1-food-nutrition-blogs -->",
        "  <!-- seo-wellness-blogs -->",
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
        json.dumps({"wave": 4, "theme": "lifestyle-protein", "posts": posts}, ensure_ascii=False, indent=2)
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
    print("Done.", len(slugs), "Wave 4 lifestyle/protein posts.")


if __name__ == "__main__":
    main()
