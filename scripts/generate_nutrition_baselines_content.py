#!/usr/bin/env python3
"""Blog + sitemap/vercel wiring for NIH DRI nutrition baseline article."""
from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOGS = ROOT / "blogs"
SITEMAP = ROOT / "sitemap.xml"
VERCEL = ROOT / "vercel.json"
SITE = "https://www.ibdpal.org"
SLUG = "how-ibdpal-nutrition-targets-work"

sys.path.insert(0, str(ROOT / "scripts"))
from generate_blog_posts import render_post  # noqa: E402

POST = {
    "slug": SLUG,
    "title": "How IBDPal Sets Nutrition Targets (And When Your Care Team Should Adjust Them)",
    "description": "IBDPal uses NIH Dietary Reference Intakes for baseline calories, protein, fluids, and micronutrients by age and sex. Extra needs belong with your GI or dietitian, education only.",
    "category": "Nutrition · June 2026",
    "date_display": "June 3, 2026",
    "date_iso": "2026-06-03T14:00:00Z",
    "asset_dir": "nutrition-targets-ibd",
    "images": ["nutrition_targets_1.jpg"],
    "alts": ["Balanced meal with vegetables, grains, and protein on a table"],
    "share": "How IBDPal uses NIH DRI baselines for nutrition tracking. Personal targets still come from your care team.",
    "body": """
<p>IBDPal helps you log meals, fluids, and symptoms so clinic visits are clearer. Nutrition targets in the app are a <strong>starting reference</strong>, not a personal prescription. This article explains what goes into those baselines and when your gastroenterologist or IBD dietitian should set higher goals.</p>

<h2>Baseline needs come from NIH Dietary Reference Intakes</h2>
<p>The U.S. government publishes <strong>Dietary Reference Intakes (DRI)</strong> through the National Institutes of Health. These tables list reference amounts for energy (calories), protein, vitamins, and minerals. Values change by <strong>age and sex</strong>, and sometimes by life stage such as pregnancy or older adulthood.</p>
<p>IBDPal aligns daily tracking goals with these NIH reference values. That keeps the app grounded in the same standards clinicians and dietitians use when they talk about general nutrition needs. Read the official tables at the <a href="https://ods.od.nih.gov/HealthInformation/Dietary_Reference_Intakes.aspx" rel="noopener noreferrer">NIH Office of Dietary Supplements DRI hub</a> or browse our <a href="/research">research source library</a>.</p>
<p><strong>RDA</strong> and <strong>AI</strong> on DRI charts mean "reference intake for most healthy people in this age and sex group." They are not the same as a supplement prescription or a hospital nutrition order.</p>

<h2>Calories, protein, and fluids need more than one formula</h2>
<p>A simple weight-based rule such as 30 kilocalories per kilogram of body weight does not capture everything that matters for individualized goals. Clinicians also weigh:</p>
<ul class="blog-list">
<li>Age and whether you are still growing (teens)</li>
<li>Current weight and recent weight change</li>
<li>Sex and body composition</li>
<li>Activity level and job demands</li>
<li>Disease activity, fevers, and healing after surgery</li>
<li>Pregnancy or breastfeeding</li>
</ul>
<p>IBDPal uses profile inputs such as age, sex, and weight to estimate baseline calorie, protein, and fluid targets. Those estimates help you see patterns over time. They are not a substitute for a full nutrition assessment.</p>
<p>If you need <strong>additional calories or protein</strong> during a flare, after malabsorption, or while recovering from surgery, that plan should come from your healthcare team. The app is built to track against general baselines, not to auto-prescribe high-calorie or high-protein protocols.</p>

<h2>Vitamins and minerals vary by age and gender</h2>
<p>Micronutrient needs are not one-size-fits-all. Iron, calcium, vitamin D, folate, and B12 reference amounts differ across age and sex groups on NIH DRI tables. Teens, menstruating adults, and older adults each have distinct ranges.</p>
<p>People with <strong>Crohn's disease or ulcerative colitis</strong> may be at higher risk for deficiencies because of inflammation, diarrhea, surgery, or diet restriction. That makes labs important. It does not mean every patient should chase very high daily food goals for iron or B12 in the app.</p>
<p><strong>Replacement doses</strong> (for example injectable B12 or prescription iron) are treatment decisions based on labs and symptoms. They belong in your medical record, not in a food log alone. IBDPal tracks dietary intake against general DRI reference levels so you and your clinician can discuss gaps at visits.</p>
<p>For deficiency basics, see our article on <a href="/blog/iron-b12-vitamin-d-ibd">iron, B12, and vitamin D in IBD</a>.</p>

<h2>What IBDPal shows vs. what your clinician personalizes</h2>
<p><strong>Calories:</strong> The app shows a DRI-informed estimate from age, sex, and weight. Your team may add extra calories during hypermetabolism or weight regain.</p>
<p><strong>Protein:</strong> The app tracks general reference ranges for your profile. Higher targets after surgery, a steroid course, or malnutrition come from your clinician.</p>
<p><strong>Fluids:</strong> Baseline hydration goals live in the app. IV fluids, oral rehydration plans, and ostomy-related losses are medical decisions.</p>
<p><strong>Vitamins and minerals:</strong> Age and sex DRI reference levels guide food tracking. Supplements, injections, and lab-driven doses belong with your care team.</p>
<p>This split is intentional. <strong>Base nutrition needs</strong> stay in the app so tracking stays understandable. <strong>Additional needs</strong> stay with professionals who know your history, medications, and labs.</p>

<h2>How to use this in real life</h2>
<ul class="blog-list">
<li>Log meals and fluids for a typical week before a nutrition visit.</li>
<li>Export or review trends in IBDPal and note flare weeks separately.</li>
<li>Ask: "Should my calorie or protein targets change while I am in this flare?"</li>
<li>Request labs for iron, B12, vitamin D, and other nutrients your team monitors.</li>
<li>Pair food tracking with <a href="/visit-prep">visit prep</a> so questions are ready.</li>
</ul>
<p>AGA clinical guidance and Crohn's and colitis nutrition research (linked on our <a href="/research">research page</a>) explain why diet supports medical care but does not replace it.</p>

<h2>Bottom line</h2>
<p>IBDPal uses <strong>NIH DRI baselines</strong> adjusted for age, sex, and weight to help you track everyday nutrition. Individualized increases for calories, protein, vitamins, or minerals should come from your healthcare team. Use the app to build awareness and better conversations, not to self-prescribe treatment.</p>
""",
}

IMAGE_URL = (
    "https://images.unsplash.com/photo-1490645935967-10de6ba17061"
    "?auto=format&w=1200&q=80"
)


def download_image(url: str, dest: Path) -> bool:
    import ssl
    import urllib.request

    ctx = ssl.create_default_context()
    try:
        with urllib.request.urlopen(url, context=ctx, timeout=30) as resp:
            data = resp.read()
        if len(data) > 5000 and data[:2] == b"\xff\xd8":
            dest.write_bytes(data)
            return True
    except Exception:
        try:
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            with urllib.request.urlopen(url, context=ctx, timeout=30) as resp:
                data = resp.read()
            if len(data) > 5000 and data[:2] == b"\xff\xd8":
                dest.write_bytes(data)
                return True
        except Exception:
            pass
    return False


def write_blog() -> None:
    asset = BLOGS / "assets" / POST["asset_dir"]
    asset.mkdir(parents=True, exist_ok=True)
    dest = asset / POST["images"][0]
    if not dest.exists() or dest.stat().st_size < 5000:
        if not download_image(IMAGE_URL, dest):
            print("WARN: image download failed for", dest)
    out = BLOGS / f"{SLUG}.html"
    out.write_text(render_post(POST), encoding="utf-8")
    print("wrote", out.name)


def patch_vercel() -> None:
    text = VERCEL.read_text(encoding="utf-8")
    src = f'"/blog/{SLUG}"'
    if src in text:
        return
    insert = (
        f'    {{\n      "source": "/blog/{SLUG}",\n'
        f'      "destination": "/blogs/{SLUG}.html"\n    }},\n'
    )
    text = text.replace('"rewrites": [\n', f'"rewrites": [\n{insert}')
    VERCEL.write_text(text, encoding="utf-8")
    print("patched vercel.json")


def patch_sitemap() -> None:
    today = date.today().isoformat()
    text = SITEMAP.read_text(encoding="utf-8")
    entry = (
        f"  <!-- nutrition-baselines-blog -->\n"
        f"  <url>\n    <loc>{SITE}/blog/{SLUG}</loc>\n    <lastmod>{today}</lastmod>\n"
        f"    <changefreq>monthly</changefreq>\n    <priority>0.86</priority>\n  </url>"
    )
    if "<!-- nutrition-baselines-blog -->" in text:
        text = re.sub(
            r"  <!-- nutrition-baselines-blog -->.*?</url>",
            entry,
            text,
            flags=re.S,
        )
    else:
        anchor = "  <!-- tier3-seo -->"
        if anchor in text:
            text = text.replace(anchor, entry + "\n" + anchor)
        else:
            text = text.replace("  <!-- seo-expansion -->", entry + "\n  <!-- seo-expansion -->")
    SITEMAP.write_text(text, encoding="utf-8")
    print("patched sitemap.xml")


def main() -> None:
    write_blog()
    patch_vercel()
    patch_sitemap()
    print("Next: python scripts/generate_research_page.py")
    print("      python scripts/generate_seo_hubs.py")
    print("      python scripts/generate_amp_pages.py")
    print("      python scripts/sync_llms_txt.py")


if __name__ == "__main__":
    main()
