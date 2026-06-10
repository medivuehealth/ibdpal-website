#!/usr/bin/env python3
"""Tier 3 SEO blog posts: pregnancy, college, J-pouch, and ER guidance."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOGS = ROOT / "blogs"
sys.path.insert(0, str(ROOT / "scripts"))
from generate_blog_posts import render_post  # noqa: E402

POSTS = [
    {
        "slug": "ibd-pregnancy-planning",
        "title": "IBD and Pregnancy: Planning With Your Gastroenterologist",
        "description": "Crohn's and colitis pregnancy questions: medication planning, flares, nutrition, and when to involve maternal-fetal medicine, education only.",
        "category": "Clinical · June 2026",
        "date_display": "June 20, 2026",
        "date_iso": "2026-06-20T12:00:00Z",
        "asset_dir": "pregnancy-ibd",
        "images": ["pregnancy_1.jpg"],
        "alts": ["Person holding a notebook in a calm home setting"],
        "share": "IBD and pregnancy planning basics, always work with your care team.",
        "body": """
<p>Many people with <strong>Crohn's disease or ulcerative colitis</strong> have healthy pregnancies, but planning matters. Searchers often ask whether IBD affects fertility, which medications are safe, and how to time conception around remission.</p>
<h2>Start With a Preconception Visit</h2>
<p>Meet your gastroenterologist and, when recommended, obstetrics or maternal-fetal medicine <strong>before</strong> trying to conceive. Bring a medication list, recent labs, and flare history. Active inflammation can affect nutrition and pregnancy outcomes, so teams often aim for stable disease first.</p>
<h2>Medications and Shared Decision-Making</h2>
<p>Stopping IBD medication without guidance is a common mistake that can trigger flares. Many biologics and other therapies are continued in pregnancy under specialist oversight. Never change doses on your own.</p>
<h2>Nutrition and Supplements</h2>
<p>Folate, iron, vitamin D, and protein needs may rise. An IBD dietitian can help you meet goals if appetite is low. Log meals and symptoms in IBDPal to spot patterns to discuss at visits.</p>
<h2>Flares During Pregnancy</h2>
<p>Call your clinic promptly for worsening pain, bleeding, fever, or dehydration. Emergency care is appropriate for severe symptoms. Your team balances maternal and fetal safety.</p>
<h2>After Delivery</h2>
<p>Breastfeeding questions, postpartum flares, and sleep loss are common topics. Schedule GI follow-up early in the postpartum period if symptoms shift.</p>
""",
    },
    {
        "slug": "college-with-ibd",
        "title": "College With Crohn's or Colitis: Dorms, Dining Halls, and Disability Services",
        "description": "Starting college with IBD: disability accommodations, dining strategies, infusions away from home, and when to use campus health, education only.",
        "category": "Teen life · June 2026",
        "date_display": "June 21, 2026",
        "date_iso": "2026-06-21T12:00:00Z",
        "asset_dir": "college-ibd",
        "images": ["college_1.jpg"],
        "alts": ["University campus walkway with students"],
        "share": "College with IBD: accommodations, dining, and self-advocacy basics.",
        "body": """
<p>Leaving home with <strong>Crohn's disease or ulcerative colitis</strong> means new bathrooms, dining halls, and stress patterns. Disability services and campus health can help when you register accommodations early.</p>
<h2>Register With Disability Services</h2>
<p>Colleges provide accommodations similar to 504 plans: extended test time, flexible attendance, private restroom access, and note-taking support during flares. You choose how much detail to share with professors.</p>
<h2>Dining Halls and Shared Kitchens</h2>
<p>Scan menus online when possible. Plain rice, eggs, yogurt, and lean protein are frequent go-tos during symptoms, but needs vary. Dietitians at student health can help if weight drops or labs change.</p>
<h2>Medication and Infusions Away From Home</h2>
<p>Transfer prescriptions before move-in. Know the nearest infusion center and urgent care. Keep insurance cards and a clinician letter describing IBD and emergency needs.</p>
<h2>Roommates and Privacy</h2>
<p>You do not owe a full diagnosis story. Scripts like "I have a chronic stomach condition" are enough for bathroom courtesy. Trusted friends can learn more if you want support.</p>
<h2>Academic Pressure and Flares</h2>
<p>Track sleep, stress, and symptoms in IBDPal. Exports help disability coordinators document flare weeks. Severe pain, heavy bleeding, or dehydration need urgent evaluation, not waiting for midterms to end.</p>
""",
    },
    {
        "slug": "j-pouch-basics-ibd",
        "title": "J-Pouch Surgery for Ulcerative Colitis: Patient-Level Basics",
        "description": "What a J-pouch is, who may consider colectomy, recovery themes, and questions for your colorectal surgeon, education only.",
        "category": "Clinical · June 2026",
        "date_display": "June 22, 2026",
        "date_iso": "2026-06-22T12:00:00Z",
        "asset_dir": "jpouch-ibd",
        "images": ["jpouch_1.jpg"],
        "alts": ["Hospital corridor with soft natural light"],
        "share": "J-pouch basics for ulcerative colitis, not surgical advice.",
        "body": """
<p>Some people with <strong>ulcerative colitis</strong> consider colectomy when medications no longer control disease or when complications arise. A <strong>J-pouch</strong> (ileal pouch-anal anastomosis) is one reconstruction option after the colon is removed.</p>
<h2>What the Procedure Involves (High Level)</h2>
<p>Surgeons remove the colon and form a pouch from the end of the small intestine, attaching it to the anus so stool can pass without a permanent ileostomy in many cases. Care often happens in stages with temporary ostomy, depending on health and center protocol.</p>
<h2>Who Discusses J-Pouch?</h2>
<p>Colorectal surgeons and IBD gastroenterologists evaluate anatomy, prior surgeries, obesity, smoking, and personal goals. Crohn's disease generally follows different surgical paths than colitis.</p>
<h2>Recovery and Life After</h2>
<p>Patients learn about pouch function, hydration, possible pouchitis, and fertility questions. Support groups and WOC nurses help with practical adjustments. Recovery timelines vary widely.</p>
<h2>Questions for Your Surgical Team</h2>
<ul class="blog-list">
<li>Am I a candidate for a staged or one-stage approach?</li>
<li>What are realistic expectations for bowel frequency?</li>
<li>How do we monitor pouchitis or cuff inflammation?</li>
<li>Who handles long-term follow-up with my GI program?</li>
</ul>
<p>See also our <a href="/blog/ostomy-basics-ibd">ostomy basics article</a> for general stoma education.</p>
""",
    },
    {
        "slug": "when-to-go-er-ibd",
        "title": "When to Go to the ER With Crohn's or Colitis",
        "description": "Urgent IBD symptoms: severe pain, bleeding, fever, dehydration, and rigid abdomen. Education only, not a substitute for your clinic's on-call instructions.",
        "category": "Flares · June 2026",
        "date_display": "June 23, 2026",
        "date_iso": "2026-06-23T12:00:00Z",
        "asset_dir": "er-ibd",
        "images": ["er_1.jpg"],
        "alts": ["Emergency department entrance at a hospital"],
        "share": "When IBD symptoms need emergency care vs. clinic follow-up.",
        "body": """
<p>Flares are common, but some symptoms need <strong>emergency evaluation</strong>. This article summarizes red flags many clinics mention. Always follow your gastroenterologist's on-call instructions first.</p>
<h2>Call 911 or Go to the ER</h2>
<ul class="blog-list">
<li>Severe abdominal pain, especially with a rigid or board-like abdomen</li>
<li>Heavy rectal bleeding or dizziness with bleeding</li>
<li>High fever with worsening pain</li>
<li>Signs of severe dehydration: very low urine, confusion, rapid heartbeat</li>
<li>Persistent vomiting and inability to keep fluids down</li>
</ul>
<h2>Same-Day Clinic or Urgent Care</h2>
<p>Worsening urgency, moderate blood, new pain patterns, or flare symptoms that match your action plan may fit same-day nurse lines or urgent care if your GI team agrees. Bring a medication list and recent symptom log.</p>
<h2>What Helps in the ER</h2>
<p>State that you have Crohn's disease or ulcerative colitis, list biologics and steroids, and mention prior surgeries or ostomies. IBDPal exports can show recent stool counts and fever notes.</p>
<h2>After an ER Visit</h2>
<p>Schedule GI follow-up even if symptoms improve. Update your action plan if triggers changed.</p>
<h2>Prevention Planning</h2>
<p>Know the nearest hospitals covered by your insurance. Keep a clinician letter for travel and school. See our <a href="/blog/flare-first-48-hours">first 48 hours of a flare</a> article for early steps.</p>
""",
    },
]

POST_IMAGE_URLS = {
    "pregnancy-ibd": "https://images.pexels.com/photos/7176069/pexels-photo-7176069.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "college-ibd": "https://images.unsplash.com/photo-1523050854058-8df90110c9f1?auto=format&w=1200&q=80",
    "jpouch-ibd": "https://images.pexels.com/photos/263402/pexels-photo-263402.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "er-ibd": "https://images.pexels.com/photos/263950/pexels-photo-263950.jpeg?auto=compress&cs=tinysrgb&w=1200",
}


def download_image(url: str, dest: Path) -> bool:
    import urllib.request

    try:
        urllib.request.urlretrieve(url, dest)
        data = dest.read_bytes()
        if len(data) > 5000 and data[:2] == b"\xff\xd8":
            return True
    except OSError:
        pass
    return False


def generate_tier3_blogs() -> list[str]:
    slugs = []
    for p in POSTS:
        asset = BLOGS / "assets" / p["asset_dir"]
        asset.mkdir(parents=True, exist_ok=True)
        url = POST_IMAGE_URLS.get(p["asset_dir"])
        for img in p["images"]:
            dest = asset / img
            if url and (not dest.exists() or dest.stat().st_size < 5000):
                if not download_image(url, dest):
                    print("WARN: download failed for", dest)
        out = BLOGS / f"{p['slug']}.html"
        out.write_text(render_post(p), encoding="utf-8")
        slugs.append(p["slug"])
        print("wrote", out.name)
    return slugs


if __name__ == "__main__":
    generate_tier3_blogs()
