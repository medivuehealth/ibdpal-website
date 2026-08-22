#!/usr/bin/env python3
# Prose style: do not use em dash.
"""Add Foundation Wave 2 guides: trials, surgery/ostomy, workplace/school rights."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "seo-landing-pages.json"

LICENSE_INTRO = (
    "Selected Crohn's & Colitis Foundation educational content and Marks are used on IBDPal under license. "
    "This page summarizes how to use Foundation patient education and links to the original Foundation sources. "
    "The Foundation does not endorse IBDPal or MediVue. Education only, not medical advice."
)

WAVE2 = [
    {
        "slug": "foundation-ibd-clinical-trials",
        "category": "clinical",
        "keywords": [
            "IBD clinical trials",
            "Crohn's research studies",
            "ulcerative colitis clinical trial",
            "Foundation clinical trial education",
        ],
        "title": "IBD Clinical Trials | Foundation Research Guide | IBDPal",
        "description": "How to use Crohn's & Colitis Foundation research and clinical trial education with your IBD team. Attribution to the Foundation. Not recruitment or medical advice.",
        "h1": "IBD clinical trials and Foundation research education",
        "intro": LICENSE_INTRO,
        "sections": [
            {
                "heading": "Why trials matter in IBD",
                "paragraphs": [
                    "Clinical trials help test new medicines, dosing strategies, devices, and care approaches for Crohn's disease and ulcerative colitis.",
                    "Foundation research education explains why participation is voluntary, how informed consent works at a high level, and why eligibility is study-specific.",
                    "Joining a trial is a clinical decision made with investigators and your gastroenterologist, not with a website.",
                ],
            },
            {
                "heading": "Questions to bring to your care team",
                "paragraphs": [
                    "Ask what phase the study is in, what is experimental versus standard care, visit burden, travel, and whether you can continue current therapy.",
                    "Clarify monitoring labs, rescue options if symptoms worsen, and how long follow-up lasts after the study drug ends.",
                    "Request plain-language summaries of risks, possible benefits, and alternatives if you decline.",
                ],
            },
            {
                "heading": "How IBDPal fits beside Foundation research education",
                "paragraphs": [
                    "Use Foundation research and patients-and-caregivers pages as original educational sources.",
                    "Track symptoms, stools, medications, and side effects in IBDPal so you and the study team can see baselines before screening.",
                    "IBDPal does not enroll patients in trials, screen for eligibility, or speak for the Foundation.",
                ],
            },
        ],
        "tips": [
            "Bring your full medication and surgery history to any screening visit",
            "Ask who pays for study visits, parking, and non-study care",
            "Never stop prescribed therapy to chase a trial without clinician guidance",
        ],
        "related": [
            {"label": "Foundation home (research education)", "url": "https://www.crohnscolitisfoundation.org/"},
            {"label": "Foundation patients and caregivers", "url": "https://www.crohnscolitisfoundation.org/patientsandcaregivers"},
            {"label": "IBDPal research sources", "url": "/research"},
            {"label": "Free government IBD research sources", "url": "/blog/free-government-ibd-research-sources"},
            {"label": "Foundation resources hub", "url": "/crohns-colitis-foundation-resources"},
            {"label": "Newly diagnosed Foundation pathway", "url": "/guides/newly-diagnosed-foundation-first-week"},
        ],
        "faq": [
            {
                "q": "Does reading Foundation pages enroll me in a trial?",
                "a": "No. Education pages explain concepts. Enrollment happens only through a study team after screening and consent.",
            },
            {
                "q": "Can IBDPal refer me into a specific study?",
                "a": "No. Ask your IBD clinician or Foundation research education pathways about how to find studies that fit your disease type and location.",
            },
        ],
    },
    {
        "slug": "foundation-ibd-surgery-ostomy",
        "category": "treatment",
        "keywords": [
            "IBD surgery",
            "Crohn's resection",
            "ulcerative colitis colectomy",
            "ostomy IBD Foundation",
            "J-pouch education",
        ],
        "title": "IBD Surgery & Ostomy | Foundation Education Bridge | IBDPal",
        "description": "Bridge guide to Crohn's & Colitis Foundation patient education on IBD surgery and ostomy living. Attribution to the Foundation. Not surgical advice.",
        "h1": "IBD surgery and ostomy: Foundation education bridge",
        "intro": LICENSE_INTRO,
        "sections": [
            {
                "heading": "When surgery enters the conversation",
                "paragraphs": [
                    "Some people with Crohn's or ulcerative colitis need surgery for strictures, fistulas, dysplasia, toxic colitis, medication failure, or other complications.",
                    "Foundation patient education helps families learn vocabulary such as resection, ostomy, and pouch procedures before surgical consults.",
                    "Whether surgery is recommended, and which operation, depends on imaging, endoscopy, nutrition status, and surgeon expertise.",
                ],
            },
            {
                "heading": "Ostomy and pouch living topics to review",
                "paragraphs": [
                    "If an ostomy is planned or already present, Foundation caregiver and patient materials often cover appliance basics, skin care themes, and returning to daily activities.",
                    "Ask your stoma nurse about pouching systems, output monitoring, dehydration risk, and when to call after hours.",
                    "Emotional adjustment is common. Pair Foundation education with clinic psychosocial support when needed.",
                ],
            },
            {
                "heading": "Using IBDPal around surgery",
                "paragraphs": [
                    "Before surgery, track pain, output, diet tolerance, and medications to share with GI and surgery teams.",
                    "After surgery, log hydration, stool or ostomy output, wound concerns, and new symptoms for follow-up visits.",
                    "IBDPal does not provide perioperative orders and does not replace wound-ostomy-continence nursing.",
                ],
            },
        ],
        "tips": [
            "Request a pre-op education visit with surgery and ostomy nursing when available",
            "Ask how medicines and biologics will be managed around the operation",
            "Save Foundation patient pages and your hospital's written discharge instructions together",
        ],
        "related": [
            {"label": "Foundation patients and caregivers (original source)", "url": "https://www.crohnscolitisfoundation.org/patientsandcaregivers"},
            {"label": "J-pouch basics article", "url": "/blog/j-pouch-basics-ibd"},
            {"label": "Ostomy basics article", "url": "/blog/ostomy-basics-ibd"},
            {"label": "Swimming with IBD or an ostomy", "url": "/blog/swimming-pool-beach-ibd-ostomy"},
            {"label": "Foundation resources hub", "url": "/crohns-colitis-foundation-resources"},
            {"label": "What is Crohn's disease Foundation basics", "url": "/guides/what-is-crohns-disease-foundation"},
        ],
        "faq": [
            {
                "q": "Does an ostomy mean IBD is cured?",
                "a": "Not always. Ulcerative colitis surgery can remove the diseased colon, but Crohn's can recur elsewhere. Your surgical and GI teams explain goals for your case.",
            },
            {
                "q": "Is this page a substitute for surgical consent?",
                "a": "No. Only your surgical team can explain risks, benefits, and alternatives for your operation.",
            },
        ],
    },
    {
        "slug": "foundation-workplace-school-rights-ibd",
        "category": "family",
        "keywords": [
            "IBD workplace rights",
            "IBD 504 plan",
            "Crohn's school accommodations",
            "ADA bathroom access IBD",
            "Foundation school workplace IBD",
        ],
        "title": "IBD Workplace & School Rights | Foundation Deep Dive | IBDPal",
        "description": "Deep dive on school and workplace accommodations for IBD using Crohn's & Colitis Foundation patient education themes. Attribution to the Foundation. Not legal advice.",
        "h1": "IBD workplace and school rights: Foundation deep dive",
        "intro": LICENSE_INTRO,
        "sections": [
            {
                "heading": "School: bathroom access, absences, and plans",
                "paragraphs": [
                    "Students with IBD often need unrestricted bathroom access, medication storage, make-up work flexibility, and nurse coordination during flares.",
                    "Foundation youth and parent education helps families prepare for 504 or similar accommodation conversations with schools.",
                    "A clinician letter describing functional needs is usually stronger than a generic printout. Your pediatric GI or school nurse can guide local process.",
                ],
            },
            {
                "heading": "Work: talking to managers and requesting adjustments",
                "paragraphs": [
                    "Adults may need predictable bathroom access, remote or hybrid options during flares, infusion-day flexibility, or temporary schedule changes.",
                    "Foundation patient education and advocacy materials help people frame access issues without oversharing private medical detail.",
                    "Employment laws and disability processes vary by country, state, and employer size. Use Foundation education as orientation, then consult HR or qualified counsel for your situation.",
                ],
            },
            {
                "heading": "How to use IBDPal in accommodation talks",
                "paragraphs": [
                    "Log flare days, urgency, night waking, and infusion schedules so patterns are clear when you meet school or workplace teams.",
                    "Export summaries for clinician letters rather than sending raw personal notes to employers.",
                    "Pair this deep dive with IBDPal's broader workplace and school rights guide and Foundation youth resources.",
                ],
            },
        ],
        "tips": [
            "Request accommodations in writing and keep copies",
            "Separate emergency medical plans from peer support chats",
            "Do not stop prescribed therapy to meet attendance rules without clinician advice",
        ],
        "related": [
            {"label": "Foundation youth and parent resources (original source)", "url": "https://www.crohnscolitisfoundation.org/patientandcaregivers/youth-parent-resources"},
            {"label": "Foundation patients and caregivers", "url": "https://www.crohnscolitisfoundation.org/patientsandcaregivers"},
            {"label": "IBDPal workplace and school rights guide", "url": "/guides/ibd-workplace-school-rights"},
            {"label": "Youth and school Foundation resources", "url": "/guides/youth-school-foundation-resources"},
            {"label": "Talking to your manager about IBD", "url": "/blog/ibd-at-work-talking-to-manager"},
            {"label": "High school IBD survival guide", "url": "/blog/high-school-ibd-survival-guide"},
            {"label": "Foundation resources hub", "url": "/crohns-colitis-foundation-resources"},
        ],
        "faq": [
            {
                "q": "Is this legal advice?",
                "a": "No. It is patient education that points to Foundation materials and practical planning steps. For disputes, use qualified legal or disability-rights help.",
            },
            {
                "q": "Do I have to disclose my full diagnosis at work?",
                "a": "Often you can request accommodations with limited medical detail. Ask HR what documentation is required and what your clinician should write.",
            },
        ],
    },
]


def main() -> None:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    pages: list[dict] = data["pages"]
    existing = {p["slug"] for p in pages}
    added = []
    for guide in WAVE2:
        if guide["slug"] in existing:
            for i, p in enumerate(pages):
                if p["slug"] == guide["slug"]:
                    pages[i] = guide
                    added.append(guide["slug"] + " (updated)")
                    break
        else:
            pages.append(guide)
            added.append(guide["slug"])
    data["pages"] = pages
    DATA.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"pages total={len(pages)}; wrote={len(added)}")
    for s in added:
        print(" -", s)


if __name__ == "__main__":
    main()
