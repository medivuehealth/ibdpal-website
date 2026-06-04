#!/usr/bin/env python3
"""Generate five patient-education blog posts (June 2026)."""
from __future__ import annotations
import html
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from generate_blog_posts import render_post  # noqa: E402

BLOGS = ROOT / "blogs"
MEDICAL_REVIEW = (
    '                        <p class="blog-medical-review"><strong>Content note:</strong> '
    "Based on publicly available guidance from the Crohn's &amp; Colitis Foundation and "
    "general IBD patient-education sources. Last reviewed June 2026. Not individual medical advice.</p>\n"
)

POSTS = [
    {
        "slug": "workplace-school-ibd-rights",
        "title": "Workplace and School Rights When You Have IBD",
        "description": "High-level overview of ADA workplace accommodations and 504 school plans for Crohn's and colitis—not legal advice.",
        "category": "Wellness · June 2026",
        "date_display": "June 10, 2026",
        "date_iso": "2026-06-10T12:00:00Z",
        "asset_dir": "workplace-school",
        "images": ["workplace_1.jpg"],
        "alts": ["Person working at a laptop in a comfortable setting"],
        "share": "Workplace and school rights basics for IBD—education only.",
        "body": """
<p>IBD can affect attendance, bathroom access, energy, and concentration. Many students and employees are entitled to <strong>reasonable accommodations</strong> that help them participate fully—without disclosing more than you choose.</p>
<h2>At Work (United States)</h2>
<p>The Americans with Disabilities Act (ADA) may protect qualified employees with Crohn's disease or ulcerative colitis. Examples of accommodations: flexible start times, remote work days, nearby restroom access, breaks, or a modified schedule during flares.</p>
<p>Start with HR or your manager using a simple letter from your clinician describing functional needs—not your entire chart. An employee assistance program (EAP) can help with paperwork.</p>
<h2>At School</h2>
<p>Section 504 plans and IEPs (when applicable) can document bathroom passes, extra time, hydration, medication storage, and absence policies. Meet with the school nurse and counselor early in the year.</p>
<h2>Documentation Tips</h2>
<ul class="blog-list"><li>Keep a brief symptom log (IBDPal exports can help)</li><li>List accommodations that worked before</li><li>Plan for flare backup (online assignments, deadline extensions)</li></ul>
<p><strong>Not legal advice.</strong> Consult a disability rights organization or attorney for complex disputes.</p>
""",
    },
    {
        "slug": "insurance-biologics-ibd",
        "title": "Insurance and Biologics for IBD: What Patients Often Ask",
        "description": "Prior authorization, appeals, and questions to ask your team—educational overview, not insurance or legal advice.",
        "category": "Treatment · June 2026",
        "date_display": "June 11, 2026",
        "date_iso": "2026-06-11T12:00:00Z",
        "asset_dir": "insurance-basics",
        "images": ["insurance_1.jpg"],
        "alts": ["Organized desk with paperwork and planner"],
        "share": "Insurance basics for IBD biologics—education only.",
        "body": """
<p>Biologics and advanced therapies can be life-changing—and administratively heavy. Understanding the process reduces panic when a pharmacy says "prior authorization required."</p>
<h2>Common Steps</h2>
<ul class="blog-list"><li>Your clinician submits clinical documentation</li><li>The insurer reviews medical necessity</li><li>You may need step therapy documentation or appeals</li><li>Specialty pharmacies coordinate delivery or infusion</li></ul>
<h2>Questions for Your Team</h2>
<p>Who handles prior auth in the clinic? Is there a patient financial counselor? Are copay assistance programs available? What is the timeline if denied?</p>
<h2>Keep Records</h2>
<p>Save denial letters, call reference numbers, and dates. Many denials are overturned on first appeal with stronger notes from your gastroenterologist.</p>
""",
    },
    {
        "slug": "ostomy-basics-ibd",
        "title": "Living With an Ostomy: Gentle Basics for IBD Patients",
        "description": "What an ostomy is, emotional adjustment, and peer support resources—education only.",
        "category": "Wellness · June 2026",
        "date_display": "June 12, 2026",
        "date_iso": "2026-06-12T12:00:00Z",
        "asset_dir": "ostomy-basics",
        "images": ["ostomy_1.jpg"],
        "alts": ["Supportive conversation between two people"],
        "share": "Ostomy basics for people with IBD—peer support links included.",
        "body": """
<p>Some people with Crohn's disease or ulcerative colitis need a temporary or permanent ostomy. It can sound frightening at first; many people return to work, sports, travel, and intimacy with the right support and supplies.</p>
<h2>Types</h2>
<p><strong>Ileostomy</strong> (small intestine) and <strong>colostomy</strong> (colon) routes waste to an external pouch. Surgery teams and ostomy nurses teach pouching, skin care, and emptying routines.</p>
<h2>Emotional Health</h2>
<p>Grief, body image worries, and anxiety are normal. Peer groups—including United Ostomy Associations of America—connect you with people who have been there.</p>
<h2>Practical Tips</h2>
<ul class="blog-list"><li>Pre-cut supplies for travel</li><li>Notification cards for restroom access</li><li>Clothing options that feel secure</li></ul>
""",
    },
    {
        "slug": "flare-first-48-hours",
        "title": "The First 48 Hours of an IBD Flare: A Calm Checklist",
        "description": "Hydration, rest, what to log, and when to call your clinician—general education, not emergency guidance.",
        "category": "Wellness · June 2026",
        "date_display": "June 13, 2026",
        "date_iso": "2026-06-13T12:00:00Z",
        "asset_dir": "flare-48h",
        "images": ["flare_1.jpg"],
        "alts": ["Restful bedroom scene emphasizing rest and recovery"],
        "share": "First 48 hours of an IBD flare—calm checklist; not medical advice.",
        "body": """
<p>Flares feel urgent even when they are not emergencies. A short plan lowers chaos.</p>
<h2>Hour 0–12</h2>
<ul class="blog-list"><li>Contact your IBD team per their after-hours instructions if fever, heavy bleeding, or severe pain</li><li>Sip electrolyte fluids; avoid alcohol</li><li>Eat gentle foods your clinician has previously OK'd</li><li>Log symptoms in IBDPal</li></ul>
<h2>Hour 12–48</h2>
<p>Rest, cancel nonessential obligations, refill medications if low, and gather data for a triage call: stool frequency, pain level, temperature, weight change.</p>
<h2>Call Promptly If</h2>
<p>Significant blood, dehydration signs, rigid abdomen, or fever over clinician thresholds. When in doubt, use your clinic's on-call line.</p>
""",
    },
    {
        "slug": "partner-caregiver-ibd",
        "title": "Partners and Caregivers: Supporting Someone With IBD",
        "description": "Communication, boundaries, and practical help without taking over medical decisions.",
        "category": "Family · June 2026",
        "date_display": "June 14, 2026",
        "date_iso": "2026-06-14T12:00:00Z",
        "asset_dir": "caregiver-partner",
        "images": ["caregiver_1.jpg"],
        "alts": ["Two people sharing tea in a supportive moment"],
        "share": "Guide for partners and caregivers of people with IBD.",
        "body": """
<p>Supporting someone with Crohn's or colitis means balancing empathy with respect for their autonomy.</p>
<h2>Listen First</h2>
<p>Ask what help they want today—rides, meals, quiet, or space. Avoid comparing to others or pushing fad diets.</p>
<h2>Practical Support</h2>
<ul class="blog-list"><li>Learn bathroom maps for outings</li><li>Share meal prep during fatigue</li><li>Help track appointments without managing meds unless asked</li></ul>
<h2>Care for Yourself</h2>
<p>Caregiver burnout is real. Schedule your own rest and use peer resources (CCF caregivers, ICN parents).</p>
""",
    },
]


def render_with_review(p):
    return render_post(p)


def main():
    import urllib.request
    for p in POSTS:
        asset = BLOGS / "assets" / p["asset_dir"]
        asset.mkdir(parents=True, exist_ok=True)
        for img in p["images"]:
            dest = asset / img
            if not dest.exists():
                url = "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?auto=format&w=1200"
                try:
                    urllib.request.urlretrieve(url, dest)
                except Exception:
                    dest.write_bytes(b"\xff\xd8\xff")
        out = BLOGS / f"{p['slug']}.html"
        out.write_text(render_with_review(p), encoding="utf-8")
        print("wrote", out.name)


if __name__ == "__main__":
    main()
