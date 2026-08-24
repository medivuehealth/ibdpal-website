#!/usr/bin/env python3
# Prose style: do not use em dash. Use periods, commas, colons, or "|" in titles.
"""Generate microbiome lab + Visbiome/probiotic education blogs."""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOGS = ROOT / "blogs"
VERCEL = ROOT / "vercel.json"
SRC_IMG = BLOGS / "assets" / "probiotics-ibd" / "probiotics-ibd_1.jpg"
FALLBACK = BLOGS / "assets" / "gut-nutrition" / "ulcerative-colitis-crohns-nutrition_1.jpg"

sys.path.insert(0, str(ROOT / "scripts"))
from generate_blog_posts import render_post  # noqa: E402

CLUSTER = (
    '<p>Related reading: '
    '<a href="/blog/probiotics-ibd-gut-health">Probiotics research overview</a>, '
    '<a href="/blog/visbiome-probiotics-ibd">Visbiome and multi-strain products</a>, '
    '<a href="/blog/microbiome-lab-testing-ibd">Microbiome lab testing</a>, '
    '<a href="/blog/probiotics-ibd-practical-guide">Practical probiotics guide</a>, '
    '<a href="/blog/microbiome-research-labs-ibd">Microbiome research labs</a>, '
    '<a href="/blog/gut-barrier-dysbiosis-inflammation-ibd">Gut barrier and dysbiosis</a>, '
    '<a href="/ibd-nutrition">IBD nutrition hub</a>.</p>'
)

POSTS: list[dict] = [
    {
        "slug": "microbiome-lab-testing-ibd",
        "title": "Microbiome Lab Testing for IBD: What Stool Tests Can and Cannot Tell You",
        "description": "Stool microbiome sequencing, clinical GI labs, and direct-to-consumer gut tests for Crohn's and colitis: what results mean, limits, and questions for your team. Education only.",
        "category": "Nutrition · August 2026",
        "date_display": "August 23, 2026",
        "date_iso": "2026-08-23T22:00:00Z",
        "asset_dir": "microbiome-lab-testing-ibd",
        "images": ["microbiome-lab-testing-ibd_1.jpg"],
        "alts": ["Lab notebook illustrating microbiome stool testing education for IBD"],
        "share": "Microbiome lab tests for IBD explained: what they can and cannot show. Education only.",
        "body": f"""
<p>Searches for <strong>microbiome lab test IBD</strong>, <strong>stool sequencing Crohn's</strong>, and <strong>gut bacteria test colitis</strong> usually mean the same practical question: should I order a microbiome report, and will it change my care. This page separates clinical labs your GI already uses from research-style or consumer microbiome panels. It is education only, not a recommendation to buy a kit.</p>

<h2>Two different kinds of "lab work"</h2>
<ul class="blog-list">
<li><strong>Standard IBD labs and stool markers:</strong> Bloodwork (CBC, CRP, chemistry), fecal calprotectin, stool infection panels, and sometimes cultures. These help track inflammation and rule out infection. See <a href="/blog/reading-ibd-labs-calprotectin-crp">reading IBD labs</a>.</li>
<li><strong>Microbiome profiling:</strong> Tests that report bacterial names, diversity scores, or imbalance charts from stool DNA (often 16S or shotgun sequencing). These are common in research and in direct-to-consumer kits. They are not a stand-alone Crohn's or colitis diagnosis.</li>
</ul>
<p>Confusing the two leads to false hope or false alarm. A low diversity score on a consumer report is not the same as a high calprotectin that your GI acts on.</p>

<h2>What microbiome reports often show</h2>
<ul class="blog-list">
<li>Relative amounts of bacterial groups (not a full good vs bad scorecard)</li>
<li>Diversity metrics that change with diet, antibiotics, flares, and sampling method</li>
<li>Comparisons to a reference database that may not match your age, diet, or disease type</li>
</ul>
<p>Results can look dramatic while still being hard to translate into a medication or diet change. Many centers do not use commercial microbiome kits to choose biologics or probiotics.</p>

<h2>Limits patients should expect</h2>
<ul class="blog-list">
<li>One stool sample is a snapshot. Travel, antibiotics, colonoscopy prep, and formula feeds can shift results.</li>
<li>Strain-level detail is uneven across labs. Brand names of probiotics may not match what the report lists.</li>
<li>Personalized food lists from consumer apps are not validated as IBD treatment plans.</li>
<li>Insurance often does not cover research-style sequencing outside a study.</li>
</ul>

<h2>When microbiome testing may appear in real care</h2>
<p>You might see microbiome methods inside a clinical trial, an academic research visit, or a specialized program. That is different from ordering a kit online and bringing a PDF to clinic. If a study invites you, ask what decisions (if any) the result will drive, who owns the data, and whether findings return to your GI.</p>

<h2>Questions for your gastroenterologist or dietitian</h2>
<ul class="blog-list">
<li>Do we need any new stool or blood markers for my current question, or is calprotectin and exam enough?</li>
<li>Would a commercial microbiome kit change our plan this year?</li>
<li>If I already bought a kit, which parts are worth discussing and which can we ignore?</li>
<li>Are there research studies at this center that include microbiome sampling with clear consent?</li>
</ul>

<h2>How IBDPal can help</h2>
<p>Log antibiotics, probiotic starts, diet shifts, and symptom changes by date. That timeline is often more useful at visits than a single diversity chart. Pair with the <a href="/tools/food-pain-tracker">food and pain sheet</a> and <a href="/visit-prep">visit prep</a>.</p>

<h2>When to call promptly</h2>
<p>Fever, severe pain, dehydration, heavy bleeding, or signs of infection need clinical care, not a microbiome reorder. Related: <a href="/blog/when-to-go-er-ibd">when to go to the ER</a>.</p>
{CLUSTER}
""",
    },
    {
        "slug": "visbiome-probiotics-ibd",
        "title": "Visbiome and Multi-Strain Probiotics for IBD: Clinic Questions",
        "description": "Visbiome, De Simone Formulation, and multi-strain probiotics in ulcerative colitis and pouchitis discussions: labeling, history vs VSL#3 naming, safety, and GI questions. Education only, not a product endorsement.",
        "category": "Nutrition · August 2026",
        "date_display": "August 23, 2026",
        "date_iso": "2026-08-23T22:30:00Z",
        "asset_dir": "visbiome-probiotics-ibd",
        "images": ["visbiome-probiotics-ibd_1.jpg"],
        "alts": ["Capsule education image for multi-strain probiotic clinic questions"],
        "share": "Visbiome and multi-strain probiotics in IBD: questions for your GI. Not a product endorsement.",
        "body": f"""
<p>Patients often search <strong>Visbiome for ulcerative colitis</strong>, <strong>Visbiome pouchitis</strong>, or <strong>Visbiome vs VSL#3</strong> after a friend, forum, or older paper mentions a high-potency multi-strain probiotic. This page explains how those names show up in clinic conversations. It is education only. IBDPal does not sell or endorse Visbiome or any supplement brand.</p>

<h2>Why the names feel confusing</h2>
<p>For years, IBD education materials discussed a multi-strain probiotic often labeled VSL#3 in research summaries. Brand ownership and formulations available in different countries later diverged. In the United States, many clinicians and patients now talk about <strong>Visbiome</strong> when they mean a high-potency product described as the <strong>De Simone Formulation</strong> (eight bacterial strains at a high colony-forming unit count). Older articles may still say VSL#3. Always check the exact product, CFU count, and storage instructions on the label your pharmacist dispenses.</p>

<h2>Where multi-strain products appear in IBD talks</h2>
<ul class="blog-list">
<li><strong>Ulcerative colitis:</strong> Some studies and guidelines discussions have explored certain multi-strain probiotics as adjuncts in selected UC settings. Results are not universal, and they are not a substitute for mesalamine, biologics, or other prescribed therapy.</li>
<li><strong>Pouchitis:</strong> After J-pouch surgery, probiotic protocols sometimes appear in specialty pathways. Your colorectal and IBD team decide if that fits your pouch history.</li>
<li><strong>Crohn's disease:</strong> Evidence for probiotics as disease-modifying therapy is generally weaker and more mixed. Do not assume a UC-oriented product automatically helps Crohn's inflammation.</li>
</ul>
<p>For a broader evidence map, see <a href="/blog/probiotics-ibd-gut-health">probiotics for Crohn's and colitis</a>.</p>

<h2>Medical food vs "just a probiotic"</h2>
<p>Some high-potency products are marketed with medical-food style language for dietary management of specific GI conditions. That labeling is not the same as FDA approval of a drug to induce Crohn's or colitis remission. Your clinician still needs to place any product inside your full plan: disease location, immune medicines, infections, and surgery history.</p>

<h2>Practical safety themes to review in clinic</h2>
<ul class="blog-list">
<li>Immunosuppression, central lines, or severe illness can change probiotic risk discussions.</li>
<li>Refrigeration, shipping heat, and expired CFU claims matter for live products.</li>
<li>Starting a high-dose product during an unexplained fever or infection workup needs clinician input first.</li>
<li>Your pharmacist can flag conflicts with your full medication list.</li>
</ul>

<h2>Questions to bring to your GI or IBD pharmacist</h2>
<ul class="blog-list">
<li>Is a multi-strain probiotic reasonable for my diagnosis (UC, Crohn's, pouch), or should we skip it?</li>
<li>If yes, which exact product and dose range are you comfortable with, and for how long before we reassess?</li>
<li>How will we judge success: stool frequency, calprotectin, pouch symptoms, or something else?</li>
<li>What side effects should make me stop and call?</li>
<li>If cost or shortages force a switch, what label details must stay the same?</li>
</ul>

<h2>How IBDPal can help</h2>
<p>Log start date, brand, dose, storage notes, and symptoms for two to four weeks so the follow-up visit is concrete. Use <a href="/visit-prep">visit prep</a> for the full medication and supplement list. Optional notes also fit the <a href="/tools/food-pain-tracker">food and pain sheet</a>.</p>
{CLUSTER}
""",
    },
    {
        "slug": "probiotics-ibd-practical-guide",
        "title": "Probiotics for IBD: A Practical Guide Before You Buy",
        "description": "How to choose and discuss probiotics for Crohn's and ulcerative colitis: strain labels, CFU, yogurt vs capsules, timing with antibiotics, and clinic red flags. Education only.",
        "category": "Nutrition · August 2026",
        "date_display": "August 23, 2026",
        "date_iso": "2026-08-23T23:00:00Z",
        "asset_dir": "probiotics-ibd-practical-guide",
        "images": ["probiotics-ibd-practical-guide_1.jpg"],
        "alts": ["Yogurt and supplement education image for IBD probiotics"],
        "share": "Practical probiotic buying guide for Crohn's and colitis clinic visits. Education only.",
        "body": f"""
<p>Store shelves and online ads make probiotics look interchangeable. For IBD, they are not. Searches for <strong>best probiotic for Crohn's</strong>, <strong>probiotic for ulcerative colitis</strong>, and <strong>should I take probiotics with a biologic</strong> need a clinic-first answer, not a viral ranking. This practical guide helps you prepare that conversation. It does not rank brands as medical winners.</p>

<h2>Start with the goal, not the brand</h2>
<ul class="blog-list">
<li>Support during or after antibiotics?</li>
<li>Adjunct idea for mild UC symptoms already discussed with your GI?</li>
<li>Pouchitis pathway directed by your surgical IBD team?</li>
<li>General wellness curiosity with no clear IBD endpoint?</li>
</ul>
<p>If the goal is vague ("fix my gut"), the chance of disappointment is high. Tie any trial to a measurable check-in date.</p>

<h2>Read the label like a medication list</h2>
<ul class="blog-list">
<li><strong>Genus, species, and strain:</strong> <em>Lactobacillus rhamnosus GG</em> is more specific than "lactobacillus blend."</li>
<li><strong>CFU at end of shelf life:</strong> Prefer products that state viable count through expiration, not only at manufacture.</li>
<li><strong>Storage:</strong> Room temperature vs refrigerated. Heat during shipping can matter.</li>
<li><strong>Extra ingredients:</strong> Inulin, sugar alcohols, or herbal blends can trigger symptoms unrelated to the bacteria.</li>
</ul>
<p>Yogurt and kefir can offer food-based microbes plus protein, but CFU and strains vary widely. See also <a href="/blog/greek-yogurt-ibd">Greek yogurt and IBD</a>.</p>

<h2>Crohn's vs ulcerative colitis vs pouch</h2>
<p>Research interest is stronger in some ulcerative colitis and pouchitis settings than in many Crohn's scenarios. A product discussed for pouchitis is not automatically appropriate for small-bowel Crohn's. Your disease location and surgery history belong in the first sentence of the clinic ask. Deep dive: <a href="/blog/probiotics-ibd-gut-health">research overview</a> and <a href="/blog/visbiome-probiotics-ibd">Visbiome and multi-strain products</a>.</p>

<h2>Antibiotics, flares, and immune medicines</h2>
<ul class="blog-list">
<li>Ask whether to pause, continue, or time-separate probiotics while on antibiotics.</li>
<li>During a flare with fever or possible infection, clarify before starting something new.</li>
<li>Biologics and immunosuppressants do not automatically forbid all probiotics, but risk talk should be individualized.</li>
</ul>

<h2>Red flags when shopping</h2>
<ul class="blog-list">
<li>Claims to replace biologics, steroids, or colonoscopy surveillance</li>
<li>Claims to cure IBD or rebalance any microbiome test in seven days</li>
<li>Pressure to buy large subscriptions before a clinician review</li>
<li>Protocols that ignore your infection history or central line status</li>
</ul>

<h2>A simple two-week trial template (only if your clinician agrees)</h2>
<ul class="blog-list">
<li>Write the exact product name, lot, and CFU on your visit sheet.</li>
<li>Log stool frequency, pain, gas, and energy daily.</li>
<li>Do not change three diet variables on the same day you start the probiotic.</li>
<li>Stop and call for hives, breathing trouble, high fever, or severe new pain.</li>
</ul>
<p>IBDPal food and symptom pairing keeps the trial honest. Related: <a href="/blog/tracking-food-symptoms-ibdpal">tracking food and symptoms</a>.</p>
{CLUSTER}
""",
    },
    {
        "slug": "microbiome-research-labs-ibd",
        "title": "Microbiome Research Labs and IBD: How Science Reaches Patient Care",
        "description": "How microbiome research labs study Crohn's and colitis, what translational science means for patients, and how to read study headlines without over-trusting supplements. Education only.",
        "category": "Nutrition · August 2026",
        "date_display": "August 23, 2026",
        "date_iso": "2026-08-23T23:30:00Z",
        "asset_dir": "microbiome-research-labs-ibd",
        "images": ["microbiome-research-labs-ibd_1.jpg"],
        "alts": ["Research lab concept image for IBD microbiome education"],
        "share": "How microbiome research labs connect to IBD clinic decisions. Education only.",
        "body": f"""
<p>Headlines about <strong>microbiome research labs</strong>, fecal transplants, and next-generation probiotics move faster than clinic pathways. Patients then wonder whether their GI is behind, or whether a supplement aisle product already delivers the lab result. This explainer translates research-lab language into patient-sized expectations. Education only, not enrollment advice for any specific trial.</p>

<h2>What research labs actually measure</h2>
<ul class="blog-list">
<li>Community composition (who is present in stool or tissue-associated samples)</li>
<li>Metabolites such as short-chain fatty acids in research settings</li>
<li>Immune and barrier readouts alongside microbes</li>
<li>Responses to diet patterns, exclusive enteral nutrition, antibiotics, or investigational therapies</li>
</ul>
<p>Those measurements help scientists build hypotheses. They do not automatically create a retail probiotic that works for every Crohn's or colitis patient. Related nutrition science themes: <a href="/blog/fiber-prebiotics-enteral-feeds-microbiome">fiber and prebiotics in feeds</a> and <a href="/blog/gut-barrier-dysbiosis-inflammation-ibd">dysbiosis and barrier function</a>.</p>

<h2>Lab proven in marketing vs peer-reviewed care</h2>
<p>A strain studied in a dish or in a small open-label series is not the same as a therapy with replicated clinical endpoints (steroid-free remission, hospitalization, surgery). When a bottle says "supported by research," ask which disease, which dose, which outcome, and whether the studied product matches what you can buy.</p>

<h2>Paths from lab bench toward clinic</h2>
<ul class="blog-list">
<li><strong>Observational cohorts:</strong> Tracking microbes during flares or diet changes.</li>
<li><strong>Dietary interventions:</strong> Controlled feeding or EEN studies that watch microbiome shifts as one of several outcomes.</li>
<li><strong>Defined microbial consortia:</strong> Carefully manufactured multi-strain products tested in trials (the scientific context behind some clinic conversations about products such as Visbiome).</li>
<li><strong>Microbiome therapeutics and FMT research:</strong> Regulated research pathways, not casual home protocols.</li>
</ul>
<p>If a center invites you into a study, ask about risks, stool collection burden, whether results return to you, and how the study interacts with your current biologic or small molecule.</p>

<h2>How to read a microbiome headline in 60 seconds</h2>
<ul class="blog-list">
<li>Was this mice, a cell model, or people with IBD?</li>
<li>How many participants, and was there a control group?</li>
<li>Did symptoms or inflammation markers improve, or only bacterial charts?</li>
<li>Is the intervention available outside a trial, and under what regulation?</li>
</ul>

<h2>What to do this month without waiting on a breakthrough</h2>
<ul class="blog-list">
<li>Keep standard monitoring your team ordered (calprotectin, scopes, drug levels as advised).</li>
<li>Bring supplement questions to clinic instead of stacking new products after every paper.</li>
<li>Use reputable education hubs and your care team. Treat social media protocols as unverified.</li>
<li>Consider research participation only through legitimate institutional review channels.</li>
</ul>

<h2>Questions for a research-interested visit</h2>
<ul class="blog-list">
<li>Are any microbiome-related trials open here for my disease type?</li>
<li>Would a commercial stool sequencing kit change anything before those results exist?</li>
<li>Which probiotic or medical-food discussions are reasonable for me now, if any?</li>
</ul>
<p>Practical next reads: <a href="/blog/microbiome-lab-testing-ibd">microbiome lab testing</a>, <a href="/blog/visbiome-probiotics-ibd">Visbiome clinic questions</a>, and <a href="/blog/probiotics-ibd-practical-guide">probiotics buying guide</a>.</p>
{CLUSTER}
""",
    },
]


def ensure_image(post: dict) -> None:
    asset = BLOGS / "assets" / post["asset_dir"]
    asset.mkdir(parents=True, exist_ok=True)
    dest = asset / post["images"][0]
    if dest.exists() and dest.stat().st_size >= 1000:
        return
    src = SRC_IMG if SRC_IMG.exists() else FALLBACK
    if not src.exists():
        for cand in (BLOGS / "assets").rglob("*probiotic*.jpg"):
            src = cand
            break
    if src.exists():
        shutil.copy(src, dest)
        print("copied image", dest.relative_to(ROOT))
    else:
        print("WARN: no image source for", post["slug"])


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


def patch_keywords(slugs: list[str]) -> None:
    path = ROOT / "data" / "ibd-resource-keywords.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    mapping = {
        "microbiome-lab-testing-ibd": [
            "microbiome lab test",
            "stool microbiome test",
            "gut bacteria test",
            "16S sequencing IBD",
            "microbiome testing Crohn's",
            "consumer microbiome kit",
            "dysbiosis test",
            "stool sequencing",
            "microbiome",
            "labs",
        ],
        "visbiome-probiotics-ibd": [
            "Visbiome",
            "Visbiome IBD",
            "Visbiome ulcerative colitis",
            "Visbiome pouchitis",
            "De Simone Formulation",
            "VSL#3",
            "VSL3",
            "multi-strain probiotic",
            "probiotic medical food",
            "probiotics",
        ],
        "probiotics-ibd-practical-guide": [
            "best probiotic for Crohn's",
            "probiotic for ulcerative colitis",
            "probiotics CFU",
            "probiotic strains IBD",
            "yogurt probiotic IBD",
            "probiotics with biologics",
            "probiotics",
            "supplements",
        ],
        "microbiome-research-labs-ibd": [
            "microbiome research",
            "microbiome lab",
            "gut microbiome research IBD",
            "translational microbiome",
            "FMT research",
            "next generation probiotics",
            "microbiome",
            "research",
        ],
    }
    for slug in slugs:
        if slug in mapping:
            data[slug] = mapping[slug]
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("patched ibd-resource-keywords.json")


def patch_aliases() -> None:
    path = ROOT / "data" / "search-aliases.json"
    aliases = json.loads(path.read_text(encoding="utf-8"))
    extra = {
        "visbiome": "probiotics",
        "vsl": "probiotics",
        "vsl3": "probiotics",
        "vsl#3": "probiotics",
        "de simone": "probiotics",
        "microbiome test": "microbiome",
        "stool sequencing": "microbiome",
        "gut bacteria test": "microbiome",
        "16s": "microbiome",
        "probiotic supplement": "probiotics",
    }
    added = 0
    for k, v in extra.items():
        if k not in aliases:
            aliases[k] = v
            added += 1
    path.write_text(json.dumps(aliases, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"patched search-aliases.json (+{added})")


def patch_seo_hubs(slugs: list[str]) -> None:
    path = ROOT / "data" / "seo-expansion.json"
    seo = json.loads(path.read_text(encoding="utf-8"))
    for hub in seo.get("hubs", []):
        if hub.get("slug") not in ("ibd-nutrition", "ulcerative-colitis", "crohns-disease"):
            continue
        blogs = hub.setdefault("blog_slugs", [])
        for s in reversed(slugs):
            if s in blogs:
                blogs.remove(s)
            blogs.insert(0, s)
        hub["blog_slugs"] = blogs[:28]
        kws = hub.setdefault("keywords", [])
        for w in ("Visbiome", "probiotics", "microbiome testing", "gut microbiome"):
            if w not in kws:
                kws.insert(0, w)
    path.write_text(json.dumps(seo, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("patched seo-expansion.json hubs")


def main() -> None:
    slugs = []
    for post in POSTS:
        ensure_image(post)
        out = BLOGS / f"{post['slug']}.html"
        out.write_text(render_post(post), encoding="utf-8")
        slugs.append(post["slug"])
        print("wrote", out.name)
    patch_vercel(slugs)
    patch_keywords(slugs)
    patch_aliases()
    patch_seo_hubs(slugs)
    print("Done.", len(slugs), "microbiome/probiotic posts.")


if __name__ == "__main__":
    main()
