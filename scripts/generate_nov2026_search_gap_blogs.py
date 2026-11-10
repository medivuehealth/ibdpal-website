#!/usr/bin/env python3
# Prose style: do not use em dash.
"""Generate Nov 2026 search-gap content for seasoning/herbs/spices + strengthen Crohn diet aliases."""
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
VERCEL = ROOT / "vercel.json"
SITEMAP = ROOT / "sitemap.xml"
FALLBACK = BLOGS / "assets" / "low-residue" / "low-residue_1.jpg"
SITE = "https://www.ibdpal.org"

sys.path.insert(0, str(ROOT / "scripts"))
from generate_blog_posts import render_post  # noqa: E402

DATE_ISO = "2026-11-10T04:00:00Z"
DATE_DISPLAY = "November 9, 2026"
MIN_WORDS = 850

IMAGE_URLS = {
    "seasonings-herbs-spices-ibd": (
        "https://images.unsplash.com/photo-1596040033229-a9821ebd058d?auto=format&w=1200&q=80"
    ),
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


POSTS: list[dict] = [
    {
        "slug": "seasonings-herbs-spices-ibd",
        "title": "Seasonings, Herbs, and Spices with IBD: Flavor Without the Flare Guesswork",
        "description": (
            "Seasoning, herbs, and spices with Crohn's or colitis: milder options, "
            "capsaicin caution, onion/garlic powders, and flare tips. Education only."
        ),
        "category": "Nutrition · November 2026",
        "date_display": DATE_DISPLAY,
        "date_iso": DATE_ISO,
        "asset_dir": "seasonings-herbs-spices-ibd",
        "images": ["seasonings-herbs-spices-ibd_1.jpg"],
        "alts": ["Assorted dried herbs and spices for IBD seasoning education"],
        "share": "Seasonings, herbs, and spices with IBD: practical flavor tips. Education only.",
        "resource_category": "nutrition",
        "match_terms": [
            "seasoning",
            "seasonings",
            "spice",
            "spices",
            "herbal",
            "herbs",
            "herb",
            "herbs and spices",
            "seasoning ibd",
            "spices crohn",
            "herbs colitis",
            "can i use seasoning with crohn's",
        ],
        "tags": [
            "seasoning",
            "seasonings",
            "spice",
            "spices",
            "herbal",
            "herbs",
            "nutrition",
            "flavor",
            "Crohn's",
            "colitis",
            "flare",
        ],
        "body": """
<p>People searching <strong>seasoning</strong>, <strong>spice</strong>, or <strong>herbal</strong> with IBD usually want the same thing: food that still tastes like food without guessing which shaker will bring urgency. Tolerance is individual. This page is patient education for Crohn's disease and ulcerative colitis. It is not a diet prescription or herbal treatment advice.</p>
<p>Pair this with <a href="/blog/spicy-foods-nuts-seeds-ibd">spicy foods, nuts, and seeds</a>, <a href="/blog/onion-garlic-ibd-fodmap">onion and garlic / FODMAP notes</a>, <a href="/blog/flare-foods-ibd">flare foods</a>, and the <a href="/ibd-nutrition">IBD nutrition hub</a>.</p>

<h2>Why seasoning searches show up</h2>
<p>During flares, many meal plans get bland: rice, eggs, plain chicken, peeled potato. People then search for seasoning ideas that add flavor without chili heat, heavy pepper, or large amounts of onion and garlic powder. In quieter remission, the question shifts to which herbs and spices fit everyday cooking again.</p>

<h2>Seasoning is not one ingredient</h2>
<p>Store bottles labeled "seasoning" can mean very different blends. Some are mostly salt. Others pack chili, black pepper, onion, garlic, citrus peel, or sugar. Always read the ingredient list. A "mild" taco or steak blend can still be spicy enough to bother an inflamed gut.</p>
<ul class="blog-list">
<li><strong>Single herbs:</strong> oregano, basil, parsley, thyme, dill, rosemary (often gentler when used lightly)</li>
<li><strong>Warm spices:</strong> cinnamon, mild paprika, turmeric, cumin (start tiny if you are sensitive)</li>
<li><strong>Heat spices:</strong> cayenne, chili flakes, hot paprika, many "cajun" blends</li>
<li><strong>Allium powders:</strong> onion powder and garlic powder are concentrated FODMAP sources for some people</li>
<li><strong>Salt and acid:</strong> salt, a squeeze of lemon, or mild vinegar can season without plant heat</li>
</ul>

<h2>Flare versus remission</h2>
<h3>During a louder flare</h3>
<ul class="blog-list">
<li>Prefer one mild herb at a time rather than complex blends</li>
<li>Skip chili heat, large black pepper loads, and mystery "seasoning salt" mixes</li>
<li>Watch onion powder and garlic powder if those usually cause gas or urgency</li>
<li>Use salt, lemon, and soft herbs on low-residue bases you already tolerate</li>
</ul>
<h3>In quieter remission</h3>
<ul class="blog-list">
<li>Reintroduce spices one at a time and log symptoms for a day or two</li>
<li>Fresh herbs often feel different from dried; portion still matters</li>
<li>Restaurant "well seasoned" food may hide chili oil or garlic paste</li>
<li>Ask about strictures before large amounts of whole spices or seed toppings</li>
</ul>

<h2>Herbal teas and "herbal" supplements are different topics</h2>
<p>A search for <strong>herbal</strong> may mean cooking herbs, herbal tea, or supplement capsules. Cooking with parsley is not the same as taking high-dose herbal products marketed for inflammation. Supplements can interact with medicines and are not IBD disease-modifying therapy unless your clinician says otherwise. See also <a href="/guides/foundation-complementary-medicine-ibd">complementary medicine notes</a> and ask your GI or pharmacist before new capsules, tinctures, or "gut detox" blends.</p>

<h2>Practical flavor swaps many people trial</h2>
<ul class="blog-list">
<li><strong>Instead of hot sauce:</strong> lemon, mild paprika, or a pinch of cumin</li>
<li><strong>Instead of garlic-heavy blends:</strong> chives tips if tolerated, or herb-only mixes without allium powders</li>
<li><strong>Instead of chili flakes on eggs or rice:</strong> dill, basil, or a soft scramble with salt only during flares</li>
<li><strong>Instead of mystery seasoning packets:</strong> buy single-ingredient jars so you can control the stack</li>
</ul>

<h2>Common myths</h2>
<ul class="blog-list">
<li><strong>"All spices are inflammatory."</strong> Not for everyone. Capsaicin heat bothers many people in flares, but mild herbs are often fine.</li>
<li><strong>"Turmeric cures Crohn's or colitis."</strong> Food amounts are not medicine. Do not replace prescribed therapy with spice claims.</li>
<li><strong>"If one blend caused urgency, never season again."</strong> Identify the trigger ingredient, then rebuild a short safe list with your dietitian.</li>
<li><strong>"Salt-free always means gut-safe."</strong> Salt-free blends can still be chili-heavy.</li>
</ul>

<h2>How to track seasoning with IBDPal</h2>
<p>Log the exact bottle or herbs used, roughly how much, the meal base, and symptoms for 24 to 48 hours. "Seasoned chicken" is too vague for clinic visits. See <a href="/blog/tracking-food-symptoms-ibdpal">tracking food and symptoms</a>.</p>

<h2>Questions for your gastroenterologist or dietitian</h2>
<ul class="blog-list">
<li>Which seasonings fit my current residue or FODMAP guidance?</li>
<li>Should I avoid onion and garlic powders while symptoms are loud?</li>
<li>Are any herbal supplements unsafe with my biologic or small-molecule therapy?</li>
<li>How do I reintroduce spices after a flare without wiping out my whole diet?</li>
</ul>

<h2>When food questions become urgent</h2>
<p>Contact your care team promptly for severe pain, vomiting, inability to keep fluids down, heavy bleeding, fever, or rapid weight loss. Seasoning guides cannot replace evaluation for obstruction, severe flare, or dehydration. See <a href="/flare-help">flare help</a> and <a href="/blog/when-to-go-er-ibd">when to go to the ER</a>.</p>

<p>Related reading: <a href="/blog/spicy-foods-nuts-seeds-ibd">spicy foods</a> · <a href="/blog/dining-out-ibd-restaurants">dining out</a> · <a href="/blog/crohns-diet-overview-ibd">Crohn's diet overview</a> · <a href="/blog/anti-inflammatory-diet-ibd">anti-inflammatory diet notes</a>.</p>
<p>Education supports shared decisions. It does not replace your gastroenterologist or registered dietitian. Bring your seasoning log to visits so advice can match your disease location and current plan.</p>
<p>If a restaurant meal repeatedly triggers symptoms after the same "house seasoning," ask what is in the rub before assuming every spice is the problem.</p>
<p>Kids and teens may refuse bland food. Offer one mild herb they choose, keep portions small, and avoid turning every meal into a negotiation about chili heat.</p>
<p>Travel packets of single herbs travel better than mystery blends when you need predictable flavor on the road.</p>

<h2>Reading a spice-aisle label quickly</h2>
<ul class="blog-list">
<li>Scan for chili, cayenne, red pepper, or "heat" words first</li>
<li>Next scan for onion, garlic, shallot, or chives powder</li>
<li>Note whether sugar or maltodextrin is near the top if sweets bother you</li>
<li>Prefer short ingredient lists when you are rebuilding tolerance</li>
</ul>

<h2>Clinic script you can copy</h2>
<p>"I have been searching seasoning and spice options for Crohn's/colitis. Heat and garlic powder seem to bother me most. Which mild herbs fit my current plan, and which blends should I avoid until calprotectin settles?"</p>
<p>Bring photos of the bottles you already own. That is faster than describing "the green one" over the portal.</p>
""".strip(),
    },
]


def download_image(url: str, dest: Path) -> bool:
    for ctx in (ssl.create_default_context(), ssl._create_unverified_context()):
        try:
            with urllib.request.urlopen(url, context=ctx, timeout=45) as resp:
                data = resp.read()
            if len(data) > 5000:
                dest.write_bytes(data)
                return True
        except Exception:
            continue
    return False


def ensure_image(post: dict) -> None:
    asset = BLOGS / "assets" / post["asset_dir"]
    asset.mkdir(parents=True, exist_ok=True)
    dest = asset / post["images"][0]
    if dest.exists() and dest.stat().st_size >= 1000:
        return
    url = IMAGE_URLS.get(post["asset_dir"])
    if url and download_image(url, dest):
        print("downloaded", dest.name)
        return
    if FALLBACK.exists():
        shutil.copy(FALLBACK, dest)
        print("fallback", dest.name)


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
    print("patched vercel.json")


def patch_sitemap(slugs: list[str]) -> None:
    today = date.today().isoformat()
    text = SITEMAP.read_text(encoding="utf-8")
    for slug in slugs:
        if f"/blog/{slug}" in text:
            continue
        entry = (
            f"  <url>\n    <loc>{SITE}/blog/{slug}</loc>\n"
            f"    <lastmod>{today}</lastmod>\n"
            f"    <changefreq>monthly</changefreq>\n"
            f"    <priority>0.85</priority>\n  </url>\n"
        )
        text = text.replace("</urlset>", entry + "</urlset>")
    SITEMAP.write_text(text, encoding="utf-8")
    print("patched sitemap.xml")


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


def update_aliases() -> None:
    data = json.loads(ALIASES.read_text(encoding="utf-8"))
    extras = {
        # True hard gap: seasoning / herbs / spices
        "seasoning": "seasoning",
        "seasonings": "seasoning",
        "seasoning ibd": "seasoning",
        "ibd seasoning": "seasoning",
        "spice": "seasoning",
        "spices": "seasoning",
        "spices ibd": "seasoning",
        "herbal": "seasoning",
        "herb": "seasoning",
        "herbs": "seasoning",
        "herbs and spices": "seasoning",
        "herbs ibd": "seasoning",
        "can i use seasoning with crohn's": "seasoning",
        "spices crohn": "seasoning",
        "herbs colitis": "seasoning",
        # Strengthen Crohn diet discovery for existing overview
        "crohn diet": "crohn diet",
        "crohns diet": "crohn diet",
        "crohn's diet": "crohn diet",
        "diet for crohn": "crohn diet",
        "diet for crohns": "crohn diet",
        "diet for crohn's": "crohn diet",
        "crohn disease diet": "crohn diet",
        "crohns disease diet": "crohn diet",
        "what to eat with crohn": "crohn diet",
        "what to eat with crohn's": "crohn diet",
        "what to eat with crohns": "crohn diet",
        "best diet for crohn": "crohn diet",
        "best diet for crohn's": "crohn diet",
    }
    data.update(extras)
    ALIASES.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("updated search-aliases.json")


def main() -> None:
    slugs = []
    for post in POSTS:
        ensure_image(post)
        wc = word_count(post["body"])
        if wc < MIN_WORDS:
            raise SystemExit(f"too short: {post['slug']} ({wc})")
        out = BLOGS / f"{post['slug']}.html"
        out.write_text(render_post(post), encoding="utf-8")
        slugs.append(post["slug"])
        print(f"wrote {out.name} (~{wc} words)")
    patch_vercel(slugs)
    patch_sitemap(slugs)
    update_search_gap(POSTS)
    update_aliases()
    print("Done.", len(slugs), "posts")


if __name__ == "__main__":
    main()
