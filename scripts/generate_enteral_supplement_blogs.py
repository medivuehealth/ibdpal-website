#!/usr/bin/env python3
# Prose style: do not use em dash. Use periods, commas, colons, or "|" in titles.
"""Generate supplemental enteral nutrition blogs that deepen the EEN/PEN cluster."""
from __future__ import annotations

import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOGS = ROOT / "blogs"
VERCEL = ROOT / "vercel.json"
SRC_IMG = BLOGS / "assets" / "gut-nutrition" / "ulcerative-colitis-crohns-nutrition_1.jpg"
FALLBACK = BLOGS / "assets" / "low-residue" / "low-residue_1.jpg"

sys.path.insert(0, str(ROOT / "scripts"))
from generate_blog_posts import render_post  # noqa: E402

CLUSTER = (
    '<p>Related reading: <a href="/blog/enteral-nutrition-ibd">Enteral nutrition overview</a>, '
    '<a href="/blog/exclusive-vs-partial-enteral-nutrition-crohns">EEN vs PEN</a>, '
    '<a href="/blog/fiber-prebiotics-enteral-feeds-microbiome">Fiber and prebiotic formulas</a>, '
    '<a href="/blog/hospital-feeding-ibd-enteral-parenteral">Hospital feeding</a>, '
    '<a href="/ibd-nutrition">IBD nutrition hub</a>.</p>'
)

POSTS: list[dict] = [
    {
        "slug": "elemental-vs-polymeric-formula-ibd",
        "title": "Elemental vs Polymeric Formula for IBD: Questions to Ask",
        "description": "Elemental, semi-elemental, and polymeric enteral formulas in Crohn's and IBD: what the labels mean, taste and tolerance themes, and dietitian questions. Education only.",
        "category": "Nutrition · August 2026",
        "date_display": "August 21, 2026",
        "date_iso": "2026-08-21T19:00:00Z",
        "asset_dir": "elemental-vs-polymeric-formula-ibd",
        "images": ["elemental-vs-polymeric-formula-ibd_1.jpg"],
        "alts": ["Nutrition education image for IBD formula types"],
        "share": "Elemental vs polymeric IBD formulas explained for clinic visits. Education only.",
        "body": f"""
<p>Searches for <strong>elemental formula IBD</strong>, <strong>polymeric formula Crohn's</strong>, and <strong>semi-elemental Peptamen</strong> often mean the same practical question: which liquid nutrition style is my team recommending, and why. This page translates common labels into clinic questions. It is education only, not a product recommendation or a dosing guide.</p>

<h2>Three labels you will hear</h2>
<ul class="blog-list">
<li><strong>Polymeric:</strong> Proteins are more intact. Often used when digestion and absorption are expected to handle standard formula well.</li>
<li><strong>Semi-elemental (peptide-based):</strong> Proteins are partly broken down. Sometimes chosen when tolerance to intact protein is a concern.</li>
<li><strong>Elemental (amino acid-based):</strong> Proteins are fully broken into amino acids. Sometimes used when the team wants the least digestive work, or when other formulas were poorly tolerated.</li>
</ul>
<p>Brand names (Modulen, Peptamen, and others) sit inside these categories. Availability and insurance coverage vary by country and plan. Your dietitian picks from what your center can actually supply.</p>

<h2>What research and guidelines do (and do not) settle</h2>
<p>In pediatric Crohn's, exclusive enteral nutrition (EEN) as a therapy is better studied than the claim that one protein form always outperforms another for every patient. Adult practice is even more individualized. Do not assume elemental is "stronger" or polymeric is "weaker." Ask what problem the formula class is meant to solve for you: induction, growth, post-op recovery, or calorie rescue.</p>
<p>Fiber and prebiotic content can also differ across products. See <a href="/blog/fiber-prebiotics-enteral-feeds-microbiome">fiber and prebiotics in enteral feeds</a> before assuming more fiber is automatically better during a flare.</p>

<h2>Taste, volume, and real-life tradeoffs</h2>
<p>Elemental formulas are often described as less palatable. That matters if the plan is oral sip feeds for weeks. Tube feeds can bypass taste but add placement, pump, and sleep logistics. Polymeric formulas may be easier to drink for some people, which can improve adherence. Adherence is part of effectiveness.</p>
<ul class="blog-list">
<li>Ask whether chilling, flavor packets (if allowed), or straw pacing are approved for your product.</li>
<li>Ask how many cartons or milliliters equal your calorie and protein target.</li>
<li>Ask what to do if nausea or diarrhea starts after a formula switch.</li>
</ul>

<h2>Questions for your GI or dietitian</h2>
<ul class="blog-list">
<li>Is the goal EEN, partial enteral nutrition, or short-term supplementation?</li>
<li>Why this protein form for my disease location and history?</li>
<li>Does this product contain fiber or FOS, and why?</li>
<li>If I fail this formula, what is the backup class?</li>
<li>How will we judge success at week two: weight, CRP, stool frequency, energy?</li>
</ul>

<h2>How IBDPal can help</h2>
<p>Log formula brand, volume, timing, and symptoms so a switch is not based on memory alone. Visit prep notes can store the written calorie target next to your medication list. See <a href="/blog/tracking-food-symptoms-ibdpal">tracking food and symptoms</a>.</p>

<h2>When to call promptly</h2>
<p>Contact your team for vomiting that prevents formula intake, signs of dehydration, fever, severe pain, or sudden breathing trouble during a tube feed. Related: <a href="/blog/when-to-go-er-ibd">when to go to the ER</a>.</p>
{CLUSTER}
""",
    },
    {
        "slug": "food-reintroduction-after-een-ibd",
        "title": "Food Reintroduction After EEN: A Practical Clinic Checklist",
        "description": "How food reintroduction after exclusive enteral nutrition often works in IBD care: pacing, symptom logs, and questions for your dietitian. Education only.",
        "category": "Nutrition · August 2026",
        "date_display": "August 21, 2026",
        "date_iso": "2026-08-21T19:30:00Z",
        "asset_dir": "food-reintroduction-after-een-ibd",
        "images": ["food-reintroduction-after-een-ibd_1.jpg"],
        "alts": ["Meal planning notebook illustrating food reintroduction after EEN"],
        "share": "Food reintroduction after EEN: pacing checklist for IBD clinic visits.",
        "body": f"""
<p>Finishing exclusive enteral nutrition (EEN) can feel like crossing a finish line and starting a second race. Searches for <strong>food reintroduction after EEN</strong> and <strong>what to eat after Modulen</strong> usually mean: how do I add food without erasing progress. This checklist is educational. Your dietitian's written sequence overrides any blog order.</p>

<h2>Why reintroduction is planned, not improvised</h2>
<p>EEN works partly because the diet is controlled. Adding random restaurant meals, spicy foods, or large fiber loads in one weekend can cause symptoms that look like "EEN failed" when the real issue is pacing. A staged plan helps your team separate disease activity from food challenge responses.</p>

<h2>Common pacing themes (illustrative only)</h2>
<ul class="blog-list">
<li>Keep full formula calories while the first few low-risk foods appear.</li>
<li>Add one new food every one to three days, not five at once.</li>
<li>Start with simpler textures your center prefers for your disease pattern.</li>
<li>Watch stool, pain, nausea, and energy for 24 to 48 hours after each add.</li>
<li>Hold the next food if a clear reaction appears, then call the dietitian.</li>
</ul>
<p>Some centers use structured diets after EEN. Others return toward a Mediterranean-style or habitual pattern more quickly. Neither approach is "the only correct" path for every Crohn's patient.</p>

<h2>What to log</h2>
<ul class="blog-list">
<li>Food name, portion, and time</li>
<li>Whether formula volume stayed the same that day</li>
<li>Stool frequency and blood if present</li>
<li>Pain score and sleep disruption</li>
<li>Missed work or school</li>
</ul>
<p>IBDPal meal and symptom pairing is built for this phase. See <a href="/blog/tracking-food-symptoms-ibdpal">tracking food and symptoms</a> and the broader <a href="/blog/enteral-nutrition-ibd">enteral nutrition guide</a>.</p>

<h2>Social meals and pressure</h2>
<p>Family gatherings often collide with week one of reintroduction. Bring a short script: "I am still on a staged plan with my dietitian." Pack a backup carton if your team still wants formula support at events.</p>

<h2>Questions to ask before food returns</h2>
<ul class="blog-list">
<li>What is day-one food, and what waits until week two?</li>
<li>How much formula do I keep while food starts?</li>
<li>Which symptoms mean pause versus emergency?</li>
<li>When do we reassess inflammation labs or stool markers?</li>
<li>If food fails, do we restart EEN or change medicine?</li>
</ul>

<h2>When to seek urgent care</h2>
<p>Severe pain, persistent vomiting, high fever, heavy bleeding, or inability to keep fluids down need prompt clinical review, not another food trial. See <a href="/flare-help">flare help</a>.</p>
{CLUSTER}
""",
    },
    {
        "slug": "taste-fatigue-enteral-formula-ibd",
        "title": "Taste Fatigue on Enteral Formula: Practical Coping Ideas",
        "description": "Taste fatigue during EEN or sip feeds for IBD: pacing, temperature, flavor rules, and when to ask for a formula or route change. Education only.",
        "category": "Nutrition · August 2026",
        "date_display": "August 21, 2026",
        "date_iso": "2026-08-21T20:00:00Z",
        "asset_dir": "taste-fatigue-enteral-formula-ibd",
        "images": ["taste-fatigue-enteral-formula-ibd_1.jpg"],
        "alts": ["Person resting with a nutrition drink illustrating formula taste fatigue"],
        "share": "Taste fatigue on IBD formula feeds: coping ideas to discuss with your dietitian.",
        "body": f"""
<p><strong>Taste fatigue</strong> is one of the top reasons people struggle to finish exclusive or partial enteral nutrition. If every carton tastes the same by day five, adherence drops even when the medical plan is sound. This page collects practical ideas patients discuss with dietitians. Confirm every tip against your prescribed product rules.</p>

<h2>Why formula taste is hard</h2>
<p>Therapeutic formulas are built for complete nutrition, not dessert. Amino acid and peptide formulas can taste more medicinal. Volume targets are often large. Nausea from active disease or medicines amplifies aversion. None of that means you are "failing." It means the plan needs human engineering.</p>

<h2>Ideas teams sometimes approve</h2>
<ul class="blog-list">
<li>Serve cold; many formulas taste milder chilled.</li>
<li>Use a straw to reduce nose involvement in flavor.</li>
<li>Split volume across the day instead of three huge servings.</li>
<li>Rotate allowed flavors if your brand has more than one.</li>
<li>Ask whether a covered cup helps if smell triggers nausea.</li>
<li>Pair sip timing with a show, podcast, or calm routine (not with stressful meetings if you can help it).</li>
</ul>
<p>Do not add coffee syrups, fruit juice, or protein powders unless your dietitian explicitly allows them. Unapproved mix-ins can change osmolarity, sugar load, and whether the plan still counts as therapeutic EEN.</p>

<h2>When to ask for a route or product change</h2>
<ul class="blog-list">
<li>You are repeatedly missing calorie targets because of taste alone.</li>
<li>Gagging or vomiting starts at the smell of formula.</li>
<li>Weight is falling despite "trying hard."</li>
<li>School or work is impossible because daytime volume is intolerable.</li>
</ul>
<p>Options may include a different formula class, overnight nasogastric feeds, or a temporary partial plan. See <a href="/blog/nasogastric-tube-feeds-ibd-practical">NG tube feeds practical guide</a> and <a href="/blog/exclusive-vs-partial-enteral-nutrition-crohns">EEN vs PEN</a>.</p>

<h2>Caregiver and teen notes</h2>
<p>Pressure to "just drink it" often backfires. Agree on a daily minimum with the dietitian, celebrate partial wins, and schedule an early check-in instead of waiting until week six. Related: <a href="/blog/teen-nutrition-ibd-growth">teen nutrition and growth</a>.</p>

<h2>Track the pattern</h2>
<p>Log which flavor, temperature, and time of day worked. Bring that log to clinic so the next prescription is informed. IBDPal symptom notes can sit beside formula volume entries.</p>
{CLUSTER}
""",
    },
    {
        "slug": "nasogastric-tube-feeds-ibd-practical",
        "title": "Nasogastric Tube Feeds for IBD: A Practical Patient Guide",
        "description": "Nasogastric (NG) overnight feeds in IBD care: what to ask about placement, pumps, school logistics, and red flags. Education only, not a how-to for self-placement.",
        "category": "Nutrition · August 2026",
        "date_display": "August 22, 2026",
        "date_iso": "2026-08-22T15:00:00Z",
        "asset_dir": "nasogastric-tube-feeds-ibd-practical",
        "images": ["nasogastric-tube-feeds-ibd-practical_1.jpg"],
        "alts": ["Educational illustration context for NG tube feeding discussions in IBD"],
        "share": "NG tube feeds for IBD: practical questions for patients and caregivers.",
        "body": f"""
<p>When drinking enough formula is impossible, teams may discuss a <strong>nasogastric (NG) tube</strong> for overnight or continuous feeds. Searches for <strong>NG tube Crohn's</strong> and <strong>overnight feeds IBD</strong> spike around growth failure, severe taste fatigue, or hospital discharge. This guide prepares questions. It is not instructions for placing or adjusting a tube on your own.</p>

<h2>What an NG tube is doing in IBD care</h2>
<p>An NG tube delivers formula through the nose into the stomach. For many pediatric and some adult patients, overnight feeds protect calorie and protein goals while daytime life continues. The gut is still being used (enteral), which is different from intravenous parenteral nutrition.</p>

<h2>Questions before the first placement</h2>
<ul class="blog-list">
<li>Who places the tube, and how is position confirmed?</li>
<li>What formula rate and total overnight volume are prescribed?</li>
<li>How do I flush the tube, and with what?</li>
<li>What pump alarms mean stop versus call?</li>
<li>How do we manage skin care at the nose?</li>
<li>Who teaches school nursing or campus health?</li>
</ul>

<h2>Home logistics that matter</h2>
<p>You will need a clean workspace, a reliable outlet, backup formula, and a written after-hours number. Sleep position and tape technique affect comfort. Travel and sleepovers need a separate plan. Photograph the pump settings your nurse programmed so household members do not guess.</p>

<h2>Red flags</h2>
<ul class="blog-list">
<li>Breathing trouble, choking, or blue lips during a feed</li>
<li>Forceful vomiting with chest pain</li>
<li>Tube that will not flush, or formula leaking from the nose unexpectedly</li>
<li>Fever with new severe abdominal pain</li>
</ul>
<p>Stop the feed and follow the emergency instructions your team gave you. If those instructions are missing, seek urgent care. Related: <a href="/blog/hospital-feeding-ibd-enteral-parenteral">hospital feeding</a> and <a href="/blog/when-to-go-er-ibd">ER timing</a>.</p>

<h2>Emotional load</h2>
<p>Tubes can affect body image, dating, and sports. Peer mentoring and Foundation youth programs help some families. Ask your center about psychosocial support, not only pump training.</p>

<h2>How IBDPal fits</h2>
<p>Log overnight volumes, morning symptoms, and sleep quality. Bring trends to the dietitian when rates change. Pair with <a href="/blog/enteral-nutrition-ibd">enteral nutrition overview</a>.</p>
{CLUSTER}
""",
    },
    {
        "slug": "adult-een-crohns-what-to-expect",
        "title": "Adult EEN for Crohn's: What to Expect",
        "description": "Exclusive enteral nutrition in adults with Crohn's: how it differs from pediatric EEN, lifestyle logistics, and clinic questions. Education only.",
        "category": "Nutrition · August 2026",
        "date_display": "August 22, 2026",
        "date_iso": "2026-08-22T15:30:00Z",
        "asset_dir": "adult-een-crohns-what-to-expect",
        "images": ["adult-een-crohns-what-to-expect_1.jpg"],
        "alts": ["Adult reviewing a nutrition plan representing adult EEN education"],
        "share": "Adult EEN for Crohn's: expectations and clinic questions. Education only.",
        "body": f"""
<p>Most EEN headlines focus on children. Adults still ask: <strong>Can adults do exclusive enteral nutrition for Crohn's?</strong> Yes, in selected cases, though medicines are more often the first induction tool in adult clinics. This page sets expectations for work, family, and follow-up. It is not a prescription to start EEN without a clinician.</p>

<h2>How adult EEN differs in practice</h2>
<ul class="blog-list">
<li>Evidence and protocols are thicker in pediatrics; adult plans are often more customized.</li>
<li>Work meetings, caregiving, and social eating create adherence pressure kids do not face the same way.</li>
<li>Insurance coverage language may differ when no feeding tube is present.</li>
<li>Adults may combine short EEN bridges with steroid tapers or biologic starts.</li>
</ul>

<h2>When adults hear EEN offered</h2>
<p>Examples include preference to avoid or delay steroids, malnutrition before surgery, limited drug options, or a center experienced with adult formula induction. Ulcerative colitis uses exclusive formula less often than Crohn's. Ask why EEN fits your phenotype specifically.</p>

<h2>Work and home planning</h2>
<ul class="blog-list">
<li>Block fridge space and calendar sip windows.</li>
<li>Tell one trusted coworker you may need flexible breaks.</li>
<li>Pre-write a social script for dinners you cannot eat.</li>
<li>Schedule week-two check-in before motivation dips.</li>
</ul>
<p>Taste fatigue is common. See <a href="/blog/taste-fatigue-enteral-formula-ibd">taste fatigue coping ideas</a>.</p>

<h2>Success metrics to request in writing</h2>
<ul class="blog-list">
<li>Target weight or BMI trend</li>
<li>Symptom scores or stool frequency goals</li>
<li>Lab or calprotectin timing</li>
<li>Food reintroduction start window</li>
<li>Backup plan if EEN is not tolerated</li>
</ul>

<h2>Adult myths</h2>
<ul class="blog-list">
<li><strong>Myth:</strong> EEN is only for kids. <strong>Reality:</strong> Selected adults use it.</li>
<li><strong>Myth:</strong> Any meal replacement shake counts. <strong>Reality:</strong> Therapeutic formulas and duration matter.</li>
<li><strong>Myth:</strong> If EEN is hard, you failed. <strong>Reality:</strong> Route or medicine changes are normal clinical adjustments.</li>
</ul>

<p>Deepen the basics with <a href="/blog/enteral-nutrition-ibd">enteral nutrition for IBD</a> and <a href="/blog/exclusive-vs-partial-enteral-nutrition-crohns">EEN vs PEN</a>.</p>
{CLUSTER}
""",
    },
    {
        "slug": "enteral-nutrition-after-ibd-surgery",
        "title": "Enteral Nutrition After IBD Surgery: Recovery Questions",
        "description": "Enteral nutrition after Crohn's or colitis surgery: sip feeds, tubes, when TPN enters the conversation, and discharge questions. Education only.",
        "category": "Nutrition · August 2026",
        "date_display": "August 22, 2026",
        "date_iso": "2026-08-22T16:00:00Z",
        "asset_dir": "enteral-nutrition-after-ibd-surgery",
        "images": ["enteral-nutrition-after-ibd-surgery_1.jpg"],
        "alts": ["Hospital nutrition education context after IBD surgery"],
        "share": "Enteral nutrition after IBD surgery: recovery questions for your team.",
        "body": f"""
<p>After resection, stricturoplasty, colectomy, or ostomy surgery, nutrition often becomes as important as the incision. Searches for <strong>tube feeds after Crohn's surgery</strong> and <strong>formula after ileostomy</strong> reflect real discharge anxiety. This page lists questions for surgical and IBD dietitians. It does not set post-op diet stages.</p>

<h2>Why formula shows up after surgery</h2>
<ul class="blog-list">
<li>Appetite and nausea limit solid intake.</li>
<li>Healing tissues need reliable protein and calories.</li>
<li>Short bowel or high-output stomas may need specialized plans.</li>
<li>Teams prefer enteral routes when the gut can be used safely.</li>
</ul>
<p>If the bowel cannot be used yet, <strong>parenteral nutrition</strong> may appear temporarily. See <a href="/blog/hospital-feeding-ibd-enteral-parenteral">hospital feeding: enteral and parenteral</a>.</p>

<h2>Discharge checklist topics</h2>
<ul class="blog-list">
<li>Which formula, how much, and for how many weeks?</li>
<li>Oral diet stages and foods to delay (skins, nuts, tough fiber if advised).</li>
<li>Ostomy output targets and dehydration warning signs.</li>
<li>Who adjusts formula if weight falls at home?</li>
<li>When biologics or other IBD drugs restart.</li>
</ul>

<h2>Home monitoring</h2>
<p>Track weight, urine color, stoma or stool output, wound concerns, and formula volumes. Rising output with dizziness needs same-day clinical advice. Related: <a href="/blog/dehydration-ibd-warning-signs">dehydration warning signs</a> and <a href="/guides/foundation-ibd-surgery-ostomy">surgery and ostomy Foundation bridge</a>.</p>

<h2>Emotional recovery</h2>
<p>Food fear after surgery is common. Ask for a written re-expansion plan so every meal is not a negotiation. Peer ostomy nurses and Foundation education can help with vocabulary while your surgeons remain the authority on your operation.</p>

<h2>Questions for the joint surgical and IBD visit</h2>
<ul class="blog-list">
<li>Is formula bridging to food, or a longer PEN plan?</li>
<li>What labs mark nutrition recovery?</li>
<li>How do pain medicines and antibiotics interact with formula tolerance?</li>
<li>When is gym or lifting cleared relative to calorie targets?</li>
</ul>
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
        # last resort: any existing enteral asset
        for cand in (BLOGS / "assets").rglob("*enteral*.jpg"):
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


def main() -> None:
    slugs = []
    for post in POSTS:
        ensure_image(post)
        out = BLOGS / f"{post['slug']}.html"
        out.write_text(render_post(post), encoding="utf-8")
        slugs.append(post["slug"])
        print("wrote", out.name)
    patch_vercel(slugs)
    print("Done.", len(slugs), "supplemental enteral posts.")


if __name__ == "__main__":
    main()
