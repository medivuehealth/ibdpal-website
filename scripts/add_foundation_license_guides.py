#!/usr/bin/env python3
# Prose style: do not use em dash.
"""Append Crohn's & Colitis Foundation licensed-education guides to seo-landing-pages.json."""
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

FOUNDATION_GUIDES = [
    {
        "slug": "what-is-ibd-foundation",
        "category": "getting-started",
        "keywords": [
            "what is IBD",
            "inflammatory bowel disease basics",
            "Crohn's Colitis Foundation IBD",
            "IBD patient education",
        ],
        "title": "What Is IBD? Foundation Patient Basics | IBDPal",
        "description": "Plain-language IBD overview using Crohn's & Colitis Foundation patient education. Attribution to the Foundation. Not medical advice.",
        "h1": "What is IBD? Foundation patient basics",
        "intro": LICENSE_INTRO,
        "sections": [
            {
                "heading": "IBD in plain language",
                "paragraphs": [
                    "Inflammatory bowel disease (IBD) is a group of chronic conditions that cause inflammation in the digestive tract. The two main types are Crohn's disease and ulcerative colitis.",
                    "Foundation patient education explains symptoms, testing pathways, and why IBD is different from irritable bowel syndrome (IBS).",
                    "Your gastroenterologist confirms your diagnosis and disease location. Online education prepares questions; it does not replace an exam or labs.",
                ],
            },
            {
                "heading": "How to use Foundation education",
                "paragraphs": [
                    "Start with the Foundation What is IBD page as the original source, then read Crohn's and ulcerative colitis pages for type-specific detail.",
                    "Write down terms you do not understand and bring them to your next clinic visit.",
                    "Use IBDPal to log symptoms, stools, and medications so patterns are easier to share with your care team.",
                ],
            },
            {
                "heading": "Boundaries",
                "paragraphs": [
                    "Foundation materials are patient education. Treatment choices belong with your IBD clinician.",
                    "IBDPal does not diagnose IBD and is not a Foundation partner or endorsed product.",
                ],
            },
        ],
        "tips": [
            "Bookmark Foundation disease basics before your next GI visit",
            "Note symptom timing, blood in stool, night waking, and weight change",
            "Ask whether your disease is Crohn's, ulcerative colitis, or IBD-unclassified",
        ],
        "related": [
            {"label": "Foundation: What is IBD (original source)", "url": "https://www.crohnscolitisfoundation.org/what-is-ibd"},
            {"label": "Foundation: What is Crohn's disease", "url": "https://www.crohnscolitisfoundation.org/what-is-crohns-disease"},
            {"label": "Foundation: What is ulcerative colitis", "url": "https://www.crohnscolitisfoundation.org/what-is-ulcerative-colitis"},
            {"label": "Foundation resources hub on IBDPal", "url": "/crohns-colitis-foundation-resources"},
            {"label": "Newly diagnosed hub", "url": "/newly-diagnosed"},
        ],
        "faq": [
            {
                "q": "Is IBD the same as IBS?",
                "a": "No. IBD involves inflammation that can damage the bowel. IBS is a functional syndrome without the same inflammatory damage. Foundation education covers this distinction.",
            },
            {
                "q": "Can this page diagnose me?",
                "a": "No. Only your clinician can diagnose IBD after history, exam, and appropriate testing.",
            },
        ],
    },
    {
        "slug": "what-is-crohns-disease-foundation",
        "category": "getting-started",
        "keywords": [
            "what is Crohn's disease",
            "Crohn's disease basics",
            "Crohn's Colitis Foundation Crohn's",
            "Crohn's patient education",
        ],
        "title": "What Is Crohn's Disease? Foundation Basics | IBDPal",
        "description": "Crohn's disease basics with Crohn's & Colitis Foundation patient education links. Attribution to the Foundation. Education only.",
        "h1": "What is Crohn's disease? Foundation basics",
        "intro": LICENSE_INTRO,
        "sections": [
            {
                "heading": "What Crohn's can affect",
                "paragraphs": [
                    "Crohn's disease can involve any part of the digestive tract from mouth to anus, often in patches. Inflammation may be transmural, meaning deeper bowel layers can be involved.",
                    "Foundation education covers common symptoms such as diarrhea, abdominal pain, fatigue, weight change, and perianal issues, plus extraintestinal symptoms some people notice.",
                    "Disease location and behavior (inflammatory, stricturing, penetrating) shape monitoring and therapy. Your GI team maps that for you.",
                ],
            },
            {
                "heading": "Using Foundation Crohn's pages with IBDPal",
                "paragraphs": [
                    "Read the Foundation What is Crohn's disease page as the original source.",
                    "Track stools, pain, energy, and medications in IBDPal between visits so your team sees trends, not only a single day.",
                    "Call your clinic or urgent pathways for red-flag symptoms. Do not use education pages as triage.",
                ],
            },
        ],
        "tips": [
            "Ask where your Crohn's is located (ileum, colon, both, other)",
            "Bring a one-week symptom summary to appointments",
            "Pair Foundation reading with your clinic's written care plan",
        ],
        "related": [
            {"label": "Foundation: What is Crohn's disease (original source)", "url": "https://www.crohnscolitisfoundation.org/what-is-crohns-disease"},
            {"label": "What is IBD? Foundation basics", "url": "/guides/what-is-ibd-foundation"},
            {"label": "Crohn's disease hub on IBDPal", "url": "/crohns-disease"},
            {"label": "Foundation resources hub", "url": "/crohns-colitis-foundation-resources"},
        ],
        "faq": [
            {
                "q": "Can Crohn's be cured by diet alone?",
                "a": "No. Nutrition matters, and some supervised nutrition therapies are used clinically, but Crohn's care is individualized and usually includes medical monitoring. Follow your IBD team.",
            },
            {
                "q": "Does the Foundation endorse IBDPal?",
                "a": "No. Selected Foundation content and Marks are used under license. The Foundation does not endorse IBDPal or MediVue.",
            },
        ],
    },
    {
        "slug": "what-is-ulcerative-colitis-foundation",
        "category": "getting-started",
        "keywords": [
            "what is ulcerative colitis",
            "UC basics",
            "Crohn's Colitis Foundation UC",
            "ulcerative colitis patient education",
        ],
        "title": "What Is Ulcerative Colitis? Foundation Basics | IBDPal",
        "description": "Ulcerative colitis basics with Crohn's & Colitis Foundation patient education links. Attribution to the Foundation. Education only.",
        "h1": "What is ulcerative colitis? Foundation basics",
        "intro": LICENSE_INTRO,
        "sections": [
            {
                "heading": "What ulcerative colitis involves",
                "paragraphs": [
                    "Ulcerative colitis (UC) causes continuous inflammation of the colon lining. Extent can range from rectum-only disease to more of the colon.",
                    "Foundation patient pages describe typical symptoms such as bloody diarrhea, urgency, tenesmus, and fatigue, and why colonoscopy and biopsies matter.",
                    "Your clinician grades activity and extent. That guides medicines, monitoring, and cancer surveillance timing.",
                ],
            },
            {
                "heading": "How to pair Foundation UC education with daily tracking",
                "paragraphs": [
                    "Use the Foundation What is ulcerative colitis page as the original source.",
                    "Log stool frequency, blood, urgency, and night waking in IBDPal so flare patterns are clearer at visits.",
                    "Seek urgent care guidance for severe bleeding, dizziness, high fever, or inability to keep fluids down.",
                ],
            },
        ],
        "tips": [
            "Ask how much of your colon is involved",
            "Track urgency and nighttime stools during active weeks",
            "Keep Foundation UC pages bookmarked for family questions",
        ],
        "related": [
            {"label": "Foundation: What is ulcerative colitis (original source)", "url": "https://www.crohnscolitisfoundation.org/what-is-ulcerative-colitis"},
            {"label": "What is IBD? Foundation basics", "url": "/guides/what-is-ibd-foundation"},
            {"label": "Ulcerative colitis hub on IBDPal", "url": "/ulcerative-colitis"},
            {"label": "Foundation resources hub", "url": "/crohns-colitis-foundation-resources"},
        ],
        "faq": [
            {
                "q": "Is ulcerative colitis the same as Crohn's colitis?",
                "a": "They can look similar but are different diseases. Crohn's can involve any GI segment and deeper layers. UC is limited to the colon lining in a continuous pattern. Your pathologist and GI confirm the type.",
            },
            {
                "q": "Can I stop medication when I feel well?",
                "a": "Do not stop prescribed therapy without your clinician's plan. Remission often depends on continued treatment.",
            },
        ],
    },
    {
        "slug": "foundation-ibd-appeal-letters",
        "category": "treatment",
        "keywords": [
            "IBD appeal letter",
            "insurance denial Crohn's",
            "Foundation appeal letters",
            "biologic appeal template",
        ],
        "title": "IBD Insurance Appeal Letters | Foundation Resources | IBDPal",
        "description": "How to use Crohn's & Colitis Foundation appeal-letter education with your clinic after an insurance denial. Attribution to the Foundation. Not legal or insurance advice.",
        "h1": "IBD insurance appeal letters with Foundation resources",
        "intro": LICENSE_INTRO,
        "sections": [
            {
                "heading": "When appeals come up",
                "paragraphs": [
                    "Insurers may deny IBD medications, infusions, or procedures. Clinics often lead prior authorization and appeals with clinical documentation.",
                    "The Foundation publishes program materials and patient guidance that help families understand appeal steps and sample language.",
                    "Your case still depends on your medical records, plan rules, and state or federal protections.",
                ],
            },
            {
                "heading": "How to use Foundation appeal education safely",
                "paragraphs": [
                    "Open the Foundation appeal-letter and prior authorization pages as original sources.",
                    "Share useful templates with your GI office, specialty pharmacy, or infusion coordinator. Do not invent clinical claims on your own.",
                    "Keep denial letters, case numbers, and deadlines in one folder. IBDPal can store visit notes and medication timelines you later export for your team.",
                ],
            },
            {
                "heading": "What IBDPal does not do",
                "paragraphs": [
                    "We do not file appeals, practice insurance law, or guarantee coverage.",
                    "We are not a Foundation partner. Licensed Foundation education is attributed and linked to original pages.",
                ],
            },
        ],
        "tips": [
            "Ask who at the clinic owns the appeal clock",
            "Save PDFs of denials and peer-to-peer outcomes",
            "Pair this guide with Foundation prior authorization education",
        ],
        "related": [
            {"label": "Foundation appeal letters (original source)", "url": "https://www.crohnscolitisfoundation.org/science-and-professionals/program-materials/appeal-letters"},
            {"label": "Foundation prior authorization guide", "url": "https://www.crohnscolitisfoundation.org/your-guide-to-navigating-prior-authorization"},
            {"label": "IBDPal prior authorization guide", "url": "/guides/ibd-prior-authorization-foundation"},
            {"label": "Foundation Action Center", "url": "https://www.crohnscolitisfoundation.org/get-involved/be-an-advocate/action-center"},
            {"label": "Foundation resources hub", "url": "/crohns-colitis-foundation-resources"},
        ],
        "faq": [
            {
                "q": "Can I submit a Foundation template without my clinic?",
                "a": "Insurers usually need clinician documentation. Use Foundation education with your care team rather than as a solo filing strategy.",
            },
            {
                "q": "Is an appeal the same as prior authorization?",
                "a": "Prior authorization is often the first review. An appeal usually follows a denial. Foundation materials explain both pathways in patient language.",
            },
        ],
    },
    {
        "slug": "step-therapy-safe-step-act-ibd",
        "category": "treatment",
        "keywords": [
            "IBD step therapy",
            "Safe Step Act",
            "fail first insurance IBD",
            "Foundation advocacy step therapy",
        ],
        "title": "IBD Step Therapy & Safe Step Act | Foundation Advocacy | IBDPal",
        "description": "Patient explainer for IBD step therapy and Foundation advocacy resources including Safe Step Act materials. Attribution to the Foundation. Not legal advice.",
        "h1": "IBD step therapy and Safe Step Act resources",
        "intro": LICENSE_INTRO,
        "sections": [
            {
                "heading": "What step therapy means for patients",
                "paragraphs": [
                    "Step therapy (sometimes called fail first) can require trying insurer-preferred drugs before covering the medicine your clinician recommended.",
                    "That can delay effective therapy for Crohn's or ulcerative colitis when the preferred sequence does not match your history.",
                    "Foundation advocacy education explains why patients organize around step-therapy reform and how to contact lawmakers.",
                ],
            },
            {
                "heading": "Using Foundation Action Center materials",
                "paragraphs": [
                    "Visit the Foundation Action Center and step-therapy advocacy pages as original sources.",
                    "Advocacy is separate from your personal coverage appeal. Keep clinic prior auth work and civic advocacy in different tracks.",
                    "If treatment is delayed, ask your GI team about medical exceptions while you follow Foundation civic guidance if you choose to advocate.",
                ],
            },
        ],
        "tips": [
            "Document prior drug failures and side effects for your clinic",
            "Use Foundation Action Center links for current campaigns",
            "Do not stop medication because of an advocacy article",
        ],
        "related": [
            {"label": "Foundation Action Center (original source)", "url": "https://www.crohnscolitisfoundation.org/get-involved/be-an-advocate/action-center"},
            {"label": "Foundation Safe Step Act overview", "url": "https://www.crohnscolitisfoundation.org/get-involved/be-an-advocate/advocacy-priorities/step-therapy/federal-safe-step-act"},
            {"label": "Foundation state step-therapy legislation", "url": "https://www.crohnscolitisfoundation.org/get-involved/be-an-advocate/advocacy-priorities/step-therapy/state-legislation"},
            {"label": "Prior authorization with Foundation resources", "url": "/guides/ibd-prior-authorization-foundation"},
            {"label": "Foundation resources hub", "url": "/crohns-colitis-foundation-resources"},
        ],
        "faq": [
            {
                "q": "Does supporting the Safe Step Act change my insurance tomorrow?",
                "a": "Advocacy can change future rules. Your current denial still needs clinic-led prior auth or appeal steps.",
            },
            {
                "q": "Is IBDPal a Foundation advocacy partner?",
                "a": "No. We link Foundation advocacy education under license and clearly state the Foundation does not endorse IBDPal.",
            },
        ],
    },
    {
        "slug": "find-ccf-chapter-support-group",
        "category": "support",
        "keywords": [
            "Crohn's Colitis Foundation chapter",
            "IBD support group near me",
            "CCF chapter finder",
            "IBD peer support",
        ],
        "title": "Find a Foundation Chapter or IBD Support Group | IBDPal",
        "description": "How to use Crohn's & Colitis Foundation chapter and support-group finders with IBDPal's state map. Attribution to the Foundation. Education only.",
        "h1": "Find a Foundation chapter or IBD support group",
        "intro": LICENSE_INTRO,
        "sections": [
            {
                "heading": "Chapters vs support groups",
                "paragraphs": [
                    "Foundation chapters organize local education, fundraising, and community programs.",
                    "Support groups offer peer connection and may be virtual or in person. Formats and schedules change by region.",
                    "Peer support complements care. It does not replace your gastroenterologist or mental health clinician.",
                ],
            },
            {
                "heading": "How to search effectively",
                "paragraphs": [
                    "Use the Foundation chapter finder and support-group finder as original sources.",
                    "Then open IBDPal's community map for state-level helplines and additional listings.",
                    "Confirm meeting times, privacy expectations, and facilitator credentials directly with the organizers.",
                ],
            },
        ],
        "tips": [
            "Try one virtual group if travel is hard during flares",
            "Ask about caregiver-only or teen-focused options",
            "Keep emergency and clinic numbers separate from peer chats",
        ],
        "related": [
            {"label": "Foundation chapters (original source)", "url": "https://www.crohnscolitisfoundation.org/chapters"},
            {"label": "Foundation find a support group", "url": "https://www.crohnscolitisfoundation.org/find-a-support-group"},
            {"label": "IBDPal support near me guide", "url": "/guides/ibd-support-near-me"},
            {"label": "Support groups guide", "url": "/guides/crohns-colitis-support-groups"},
            {"label": "Foundation resources hub", "url": "/crohns-colitis-foundation-resources"},
            {"label": "Community map", "url": "/#community"},
        ],
        "faq": [
            {
                "q": "Are Foundation support groups medical appointments?",
                "a": "No. They are community and education spaces. Clinical decisions stay with your IBD care team.",
            },
            {
                "q": "Does IBDPal run Foundation chapters?",
                "a": "No. Chapters and official programs belong to the Foundation. IBDPal links to public finders under license.",
            },
        ],
    },
    {
        "slug": "foundation-emotional-wellness-ibd",
        "category": "wellness",
        "keywords": [
            "IBD mental health",
            "Crohn's anxiety depression",
            "Foundation emotional wellness",
            "IBD stress support",
        ],
        "title": "IBD Emotional Wellness | Foundation Resources | IBDPal",
        "description": "How to use Crohn's & Colitis Foundation patient education for stress, anxiety, and emotional wellness with IBD. Attribution to the Foundation. Not therapy.",
        "h1": "Foundation resources for IBD emotional wellness",
        "intro": LICENSE_INTRO,
        "sections": [
            {
                "heading": "Why emotional health is part of IBD care",
                "paragraphs": [
                    "Living with flares, bathrooms, and unpredictable energy can raise anxiety, depression, or burnout for patients and caregivers.",
                    "Foundation patient and caregiver education acknowledges these challenges and points people toward support and professional care when needed.",
                    "Peer stories help. Licensed mental health care treats clinical anxiety or depression.",
                ],
            },
            {
                "heading": "Practical next steps",
                "paragraphs": [
                    "Read Foundation patients and caregivers materials as the original source for wellness framing.",
                    "Tell your GI team about mood, sleep, and panic around symptoms. Ask for behavioral health referrals experienced with chronic illness.",
                    "Use IBDPal to note stress triggers beside symptom logs so patterns are visible at visits.",
                ],
            },
        ],
        "tips": [
            "Screen for sleep loss and isolation during long flares",
            "Caregivers deserve support too",
            "Crisis or suicidal thoughts need emergency or crisis-line help immediately",
        ],
        "related": [
            {"label": "Foundation patients and caregivers (original source)", "url": "https://www.crohnscolitisfoundation.org/patientsandcaregivers"},
            {"label": "IBDPal stress and anxiety guide", "url": "/guides/stress-anxiety-ibd"},
            {"label": "Depression and anxiety article", "url": "/blog/depression-anxiety-ibd"},
            {"label": "Help Center vs clinic", "url": "/blog/when-to-call-ibd-help-center"},
            {"label": "Foundation resources hub", "url": "/crohns-colitis-foundation-resources"},
        ],
        "faq": [
            {
                "q": "Can Foundation pages replace a therapist?",
                "a": "No. They provide education and connection ideas. Therapy and medication decisions need licensed clinicians.",
            },
            {
                "q": "Is stress the cause of IBD?",
                "a": "Stress can worsen how symptoms feel and coping capacity. IBD itself is an inflammatory disease managed with medical care.",
            },
        ],
    },
    {
        "slug": "newly-diagnosed-foundation-first-week",
        "category": "getting-started",
        "keywords": [
            "newly diagnosed Crohn's",
            "newly diagnosed ulcerative colitis",
            "first week IBD diagnosis",
            "Foundation newly diagnosed",
        ],
        "title": "Newly Diagnosed IBD: First Week with Foundation Resources | IBDPal",
        "description": "A first-week pathway after Crohn's or colitis diagnosis using Crohn's & Colitis Foundation education and IBDPal tools. Attribution to the Foundation.",
        "h1": "Newly diagnosed IBD: first-week Foundation pathway",
        "intro": LICENSE_INTRO,
        "sections": [
            {
                "heading": "Day 1 to 2: orient with trusted education",
                "paragraphs": [
                    "Read Foundation What is IBD and your disease-type page so vocabulary matches what your GI said.",
                    "Save the Foundation IBD Help Center number for education questions that are not emergencies.",
                    "Avoid drastic DIY diets or stopping medicines without clinician guidance.",
                ],
            },
            {
                "heading": "Day 3 to 5: build your visit kit",
                "paragraphs": [
                    "List medications, allergies, surgeries, and top three goals for the next appointment.",
                    "Start a simple IBDPal log for stools, pain, food, and energy.",
                    "Ask about labs, imaging follow-up, vaccines, and who to call after hours.",
                ],
            },
            {
                "heading": "Day 6 to 7: support and sustainability",
                "paragraphs": [
                    "Look up your Foundation chapter or a support group if peer connection would help.",
                    "Share one Foundation page with a caregiver so they learn from the same source.",
                    "Plan sleep, hydration, and work or school adjustments with your clinician's advice.",
                ],
            },
        ],
        "tips": [
            "Emergencies go to urgent care or ER pathways, not Help Center education lines",
            "Write questions before each specialist visit",
            "Return to Foundation basics when relatives send conflicting advice",
        ],
        "related": [
            {"label": "Foundation patients and caregivers", "url": "https://www.crohnscolitisfoundation.org/patientsandcaregivers"},
            {"label": "Foundation IBD Help Center", "url": "https://www.crohnscolitisfoundation.org/patientsandcaregivers/ibdhelpcenter"},
            {"label": "What is IBD? Foundation basics", "url": "/guides/what-is-ibd-foundation"},
            {"label": "Newly diagnosed hub", "url": "/newly-diagnosed"},
            {"label": "Visit prep", "url": "/visit-prep"},
            {"label": "Foundation resources hub", "url": "/crohns-colitis-foundation-resources"},
        ],
        "faq": [
            {
                "q": "Should I read everything online in week one?",
                "a": "No. Stick to Foundation basics and your clinic's handouts first. Too many unverified sources raises anxiety.",
            },
            {
                "q": "Can IBDPal replace my first GI visits?",
                "a": "No. Tracking supports visits. Diagnosis and therapy plans require your care team.",
            },
        ],
    },
    {
        "slug": "pregnancy-ibd-foundation-resources",
        "category": "family",
        "keywords": [
            "pregnancy IBD",
            "Crohn's pregnancy",
            "ulcerative colitis pregnancy",
            "Foundation pregnancy IBD",
        ],
        "title": "Pregnancy and IBD | Foundation Patient Resources | IBDPal",
        "description": "How to use Crohn's & Colitis Foundation patient education when planning pregnancy with Crohn's or colitis. Attribution to the Foundation. Not obstetric advice.",
        "h1": "Pregnancy and IBD with Foundation resources",
        "intro": LICENSE_INTRO,
        "sections": [
            {
                "heading": "Plan with your IBD and OB teams",
                "paragraphs": [
                    "Many people with IBD have healthy pregnancies with coordinated care. Medication plans often need preconception review.",
                    "Foundation patient education helps families prepare questions about flares, nutrition, delivery planning, and postpartum support.",
                    "Do not start or stop IBD drugs based on a webpage. Decisions belong with your gastroenterologist and obstetric clinicians.",
                ],
            },
            {
                "heading": "How IBDPal can help during planning",
                "paragraphs": [
                    "Use Foundation caregiver and patient hubs as original educational sources.",
                    "Track symptoms, nutrition, and medication timing in IBDPal to share at joint visits.",
                    "Ask early about folate, iron, vitamin D, and vaccine timing when relevant to your regimen.",
                ],
            },
        ],
        "tips": [
            "Schedule a preconception IBD visit when possible",
            "Bring a full medication list including biologics and steroids",
            "Identify who covers flares during pregnancy after hours",
        ],
        "related": [
            {"label": "Foundation patients and caregivers (original source)", "url": "https://www.crohnscolitisfoundation.org/patientsandcaregivers"},
            {"label": "IBD pregnancy planning article", "url": "/blog/ibd-pregnancy-planning"},
            {"label": "Foundation resources hub", "url": "/crohns-colitis-foundation-resources"},
            {"label": "Newly diagnosed pathway", "url": "/guides/newly-diagnosed-foundation-first-week"},
        ],
        "faq": [
            {
                "q": "Is remission required before pregnancy?",
                "a": "Many clinicians prefer conception during quieter disease, but individual advice varies. Ask your IBD team about your case.",
            },
            {
                "q": "Does IBDPal provide obstetric care?",
                "a": "No. We provide education links and tracking tools only.",
            },
        ],
    },
    {
        "slug": "youth-school-foundation-resources",
        "category": "family",
        "keywords": [
            "IBD school 504",
            "teen Crohn's school",
            "Foundation youth resources",
            "IBD classroom accommodations",
        ],
        "title": "Youth & School IBD Resources | Foundation Education | IBDPal",
        "description": "School and teen living-with-IBD guidance using Crohn's & Colitis Foundation youth and parent education. Attribution to the Foundation. Education only.",
        "h1": "Youth and school IBD resources from the Foundation",
        "intro": LICENSE_INTRO,
        "sections": [
            {
                "heading": "School life with IBD",
                "paragraphs": [
                    "Students may need bathroom access, medication storage, absence flexibility, and make-up work plans.",
                    "Foundation youth and parent resources explain advocacy topics families often discuss with schools.",
                    "Camp Oasis and teen programs can reduce isolation, but eligibility and dates live on Foundation pages.",
                ],
            },
            {
                "heading": "How families can use IBDPal beside Foundation education",
                "paragraphs": [
                    "Read Foundation youth-parent resources and Camp Oasis pages as original sources.",
                    "Track school-day symptoms and triggers in IBDPal to support 504 or IEP conversations with clinicians and counselors.",
                    "Keep medical letters from your pediatric GI as the authority for accommodations.",
                ],
            },
        ],
        "tips": [
            "Meet the school nurse early each year",
            "Document flares that cause absences",
            "Pair this guide with the Camp Oasis youth guide",
        ],
        "related": [
            {"label": "Foundation youth and parent resources (original source)", "url": "https://www.crohnscolitisfoundation.org/patientandcaregivers/youth-parent-resources"},
            {"label": "Camp Oasis guide on IBDPal", "url": "/guides/camp-oasis-kids-ibd"},
            {"label": "Foundation Camp Oasis", "url": "https://www.crohnscolitisfoundation.org/get-involved/camp-oasis"},
            {"label": "Teens and school hub", "url": "/teens-and-school"},
            {"label": "Foundation resources hub", "url": "/crohns-colitis-foundation-resources"},
        ],
        "faq": [
            {
                "q": "Does the Foundation write my child's 504 plan?",
                "a": "No. Schools and clinicians create accommodations. Foundation education helps families prepare informed requests.",
            },
            {
                "q": "Is Camp Oasis required for school support?",
                "a": "No. Camp is optional peer programming. School supports are separate.",
            },
        ],
    },
]


def main() -> None:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    pages: list[dict] = data["pages"]
    existing = {p["slug"] for p in pages}
    added = []
    for guide in FOUNDATION_GUIDES:
        if guide["slug"] in existing:
            # refresh in place
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
