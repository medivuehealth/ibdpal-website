#!/usr/bin/env python3
# Prose style: do not use em dash.
"""Add Foundation Wave 3 guides: meds, pain/fatigue, EIMs, CAM, travel, intimacy, vaccines, CRC surveillance."""
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

WAVE3 = [
    {
        "slug": "foundation-ibd-medication-guide",
        "category": "treatment",
        "keywords": [
            "IBD medication guide",
            "Crohn's biologics",
            "ulcerative colitis drugs",
            "Foundation IBD medications",
            "biosimilars IBD",
        ],
        "title": "IBD Medication Guide | Foundation Drug Classes | IBDPal",
        "description": "How to use the Crohn's & Colitis Foundation IBD Medication Guide with your care team. Attribution to the Foundation. Not prescribing advice.",
        "h1": "IBD medications: Foundation Medication Guide bridge",
        "intro": LICENSE_INTRO,
        "sections": [
            {
                "heading": "What the Foundation Medication Guide is for",
                "paragraphs": [
                    "The Foundation IBD Medication Guide helps patients browse drug classes such as aminosalicylates, corticosteroids, immunomodulators, biologics, and related options.",
                    "It is education for shared decision-making, not a substitute for your gastroenterologist's prescription plan.",
                    "Filters by condition, class, and how a medicine is taken can help you prepare questions before a visit or infusion.",
                ],
            },
            {
                "heading": "Questions to ask about any IBD drug",
                "paragraphs": [
                    "Ask why this class was chosen for your disease location and severity, what monitoring labs or scopes are needed, and how soon to expect response.",
                    "Clarify infection precautions, vaccine timing, pregnancy plans, and what to do if doses are missed or side effects appear.",
                    "If a biosimilar or formulary change is proposed, ask how switching is handled and what to report if symptoms change.",
                ],
            },
            {
                "heading": "How IBDPal fits",
                "paragraphs": [
                    "Log doses, infusion dates, flares, and side effects so trends are clear at appointments.",
                    "Use Foundation medication pages as the original educational source, then confirm details with your clinic and pharmacist.",
                    "IBDPal does not recommend starting, stopping, or switching therapies.",
                ],
            },
        ],
        "tips": [
            "Bring a written medication list including steroids and over-the-counter products",
            "Ask for the plan if prior authorization delays the preferred drug",
            "Never stop a biologic or immunomodulator without clinician guidance",
        ],
        "related": [
            {"label": "Foundation IBD Medication Guide (original source)", "url": "https://www.crohnscolitisfoundation.org/patientsandcaregivers/ibd-medication-guide"},
            {"label": "Foundation patients and caregivers", "url": "https://www.crohnscolitisfoundation.org/patientsandcaregivers"},
            {"label": "Prior authorization Foundation guide", "url": "/guides/ibd-prior-authorization-foundation"},
            {"label": "Understanding biologics article", "url": "/blog/understanding-biologics-ibd"},
            {"label": "Vaccines Foundation bridge", "url": "/guides/foundation-ibd-vaccines-infection"},
            {"label": "Foundation resources hub", "url": "/crohns-colitis-foundation-resources"},
        ],
        "faq": [
            {
                "q": "Does the Foundation decide which drug I should take?",
                "a": "No. The Guide explains options. Your gastroenterologist and you choose therapy based on your disease, history, and labs.",
            },
            {
                "q": "Are biosimilars the same as generics?",
                "a": "Biosimilars are highly similar to reference biologics under regulatory standards. Ask your team how a switch would work for you.",
            },
        ],
    },
    {
        "slug": "foundation-ibd-pain-fatigue",
        "category": "symptoms",
        "keywords": [
            "IBD pain management",
            "Crohn's fatigue",
            "ulcerative colitis energy",
            "Foundation pain and fatigue",
        ],
        "title": "IBD Pain & Fatigue | Foundation Education | IBDPal",
        "description": "Bridge to Crohn's & Colitis Foundation pain and fatigue patient education. Attribution to the Foundation. Not a treatment plan.",
        "h1": "IBD pain and fatigue: Foundation education bridge",
        "intro": LICENSE_INTRO,
        "sections": [
            {
                "heading": "Why pain and fatigue deserve their own visit agenda",
                "paragraphs": [
                    "Abdominal pain, joint pain, and deep fatigue are common with Crohn's and ulcerative colitis, even when people are working hard on gut therapy.",
                    "Foundation pain and fatigue education explains that causes can include active inflammation, anemia, vitamin gaps, sleep disruption, medications, or stress loops.",
                    "NSAIDs that help joint pain can irritate the gut for some people. Ask your clinician before using them for IBD-related pain.",
                ],
            },
            {
                "heading": "What to track and what to ask",
                "paragraphs": [
                    "Note pain location, timing with meals or stools, night waking, and energy crashes across the week.",
                    "Ask about iron, B12, vitamin D, thyroid checks, sleep evaluation, physical therapy, and mental health supports when fatigue persists.",
                    "Complementary approaches discussed in Foundation materials should be cleared with your care team and never replace prescribed IBD therapy.",
                ],
            },
            {
                "heading": "Using IBDPal",
                "paragraphs": [
                    "Log pain scores, fatigue, sleep, and stool patterns so patterns are visible between visits.",
                    "Read Foundation pain-management and managing-fatigue pages as original sources.",
                    "Seek urgent care for severe new pain, fever, or red-flag symptoms rather than relying on education pages.",
                ],
            },
        ],
        "tips": [
            "Bring a one-week energy and pain diary to GI visits",
            "Ask whether fatigue might reflect under-treated disease versus another cause",
            "Do not escalate opioids or cannabis based only on online reading",
        ],
        "related": [
            {"label": "Foundation pain management (original source)", "url": "https://www.crohnscolitisfoundation.org/patientsandcaregivers/pain-and-fatigue/pain-management"},
            {"label": "Foundation managing fatigue (original source)", "url": "https://www.crohnscolitisfoundation.org/patientsandcaregivers/pain-and-fatigue/managing-fatigue"},
            {"label": "Foundation emotional wellness guide", "url": "/guides/foundation-emotional-wellness-ibd"},
            {"label": "Iron deficiency nutrition guide", "url": "/guides/iron-deficiency-nutrition-ibd"},
            {"label": "Foundation complementary medicine bridge", "url": "/guides/foundation-complementary-medicine-ibd"},
            {"label": "Foundation resources hub", "url": "/crohns-colitis-foundation-resources"},
        ],
        "faq": [
            {
                "q": "If my colonoscopy looks better, why am I still exhausted?",
                "a": "Gut healing and energy recovery can diverge. Ask about anemia, sleep, mental health, and other causes using Foundation fatigue education as a conversation starter.",
            },
            {
                "q": "Is acetaminophen always safe for IBD pain?",
                "a": "Many teams prefer it over NSAIDs for gut reasons, but dosing and liver risk still need clinician guidance for your case.",
            },
        ],
    },
    {
        "slug": "foundation-ibd-extraintestinal-manifestations",
        "category": "symptoms",
        "keywords": [
            "extraintestinal manifestations IBD",
            "IBD joint pain",
            "IBD eye inflammation",
            "IBD skin manifestations",
            "Foundation EIM education",
        ],
        "title": "IBD Outside the Gut | Foundation EIM Guide | IBDPal",
        "description": "Foundation-attributed bridge on extraintestinal IBD issues affecting joints, skin, eyes, and more. Education only, not diagnosis.",
        "h1": "Extraintestinal manifestations: Foundation education bridge",
        "intro": LICENSE_INTRO,
        "sections": [
            {
                "heading": "IBD is not only a gut disease",
                "paragraphs": [
                    "Some people with Crohn's or ulcerative colitis develop problems in joints, skin, eyes, liver, mouth, or other systems, often called extraintestinal manifestations.",
                    "Foundation and GI society education notes that some issues track with gut flares while others can appear even when the intestine looks quieter.",
                    "New eye pain, vision change, severe joint swelling, or unexplained skin ulcers need prompt clinical evaluation.",
                ],
            },
            {
                "heading": "Building the right care team",
                "paragraphs": [
                    "Ask whether rheumatology, dermatology, ophthalmology, or hepatology should join your plan.",
                    "Share your full IBD medication list with every specialist so therapies do not conflict.",
                    "Use Foundation patient education to learn vocabulary, then confirm what applies to you with clinicians.",
                ],
            },
            {
                "heading": "How IBDPal helps",
                "paragraphs": [
                    "Track joint pain, eye symptoms, skin changes, and gut symptoms on the same timeline.",
                    "Pair this bridge with IBDPal autoimmune and EIM hubs for deeper reading.",
                    "IBDPal cannot diagnose EIMs or recommend specialist referrals.",
                ],
            },
        ],
        "tips": [
            "Photograph skin lesions with dates for clinic visits",
            "Treat sudden vision symptoms as urgent",
            "Ask if a therapy change might help both gut and joint disease",
        ],
        "related": [
            {"label": "Foundation patients and caregivers (original source)", "url": "https://www.crohnscolitisfoundation.org/patientsandcaregivers"},
            {"label": "IBD autoimmune associations hub", "url": "/ibd-autoimmune-associations"},
            {"label": "Extraintestinal manifestations article", "url": "/blog/ibd-extraintestinal-manifestations"},
            {"label": "Uveitis and eye inflammation article", "url": "/blog/uveitis-eye-inflammation-ibd"},
            {"label": "Foundation pain and fatigue bridge", "url": "/guides/foundation-ibd-pain-fatigue"},
            {"label": "Foundation resources hub", "url": "/crohns-colitis-foundation-resources"},
        ],
        "faq": [
            {
                "q": "Do EIMs mean my IBD treatment is failing?",
                "a": "Not always. Some manifestations need separate specialist care even when gut therapy is appropriate. Ask your GI team.",
            },
            {
                "q": "Can IBDPal tell me if my rash is pyoderma?",
                "a": "No. Skin diagnosis belongs with clinicians. Logging timing and photos can still help the visit.",
            },
        ],
    },
    {
        "slug": "foundation-complementary-medicine-ibd",
        "category": "treatment",
        "keywords": [
            "complementary medicine IBD",
            "integrative Crohn's",
            "ulcerative colitis CAM",
            "Foundation complementary medicine",
        ],
        "title": "Complementary Medicine & IBD | Foundation Bridge | IBDPal",
        "description": "How to use Crohn's & Colitis Foundation complementary medicine education safely alongside IBD care. Attribution to the Foundation.",
        "h1": "Complementary medicine and IBD: Foundation bridge",
        "intro": LICENSE_INTRO,
        "sections": [
            {
                "heading": "Alongside care, not instead of care",
                "paragraphs": [
                    "Foundation complementary medicine education discusses approaches some people use to support comfort, stress, or quality of life while staying on conventional IBD therapy.",
                    "Complementary options are not a cure and should not replace biologics, immunomodulators, or other prescribed treatments without clinician agreement.",
                    "Herbs, supplements, and unregulated products can interact with IBD drugs or delay needed care.",
                ],
            },
            {
                "heading": "Safer conversation starters",
                "paragraphs": [
                    "Ask your gastroenterologist and pharmacist before starting any supplement, cannabis product, or intensive mind-body program during a flare.",
                    "Bring ingredient lists and doses to visits. Track whether symptoms change after a new product.",
                    "Evidence quality varies widely. Foundation pages help frame questions; they do not personalize a regimen.",
                ],
            },
            {
                "heading": "IBDPal's role",
                "paragraphs": [
                    "Log complementary products next to prescribed medicines so side effects and flares are easier to interpret.",
                    "Use the Foundation complementary medicine page as the original educational source.",
                    "IBDPal does not endorse specific alternative products or clinics.",
                ],
            },
        ],
        "tips": [
            "Tell every clinician about supplements, not only prescription drugs",
            "Be wary of anyone who says you can stop IBD medicine if you buy their protocol",
            "Prioritize sleep, nutrition support, and mental health with your team",
        ],
        "related": [
            {"label": "Foundation complementary medicine (original source)", "url": "https://www.crohnscolitisfoundation.org/ibd/complementary-medicine"},
            {"label": "Foundation Medication Guide bridge", "url": "/guides/foundation-ibd-medication-guide"},
            {"label": "Foundation diet and nutrition resources", "url": "/guides/foundation-diet-nutrition-ibd"},
            {"label": "Foundation pain and fatigue bridge", "url": "/guides/foundation-ibd-pain-fatigue"},
            {"label": "Foundation resources hub", "url": "/crohns-colitis-foundation-resources"},
        ],
        "faq": [
            {
                "q": "Can complementary therapy put IBD in remission alone?",
                "a": "Do not assume that. Remission plans belong with your IBD clinician. Complementary care may support comfort for some people as an add-on.",
            },
            {
                "q": "Is medical cannabis proven to heal IBD inflammation?",
                "a": "Foundation education notes symptom interest in some studies, with limited evidence for controlling inflammation. Decisions require clinician guidance and local law.",
            },
        ],
    },
    {
        "slug": "foundation-ibd-travel-restroom-access",
        "category": "lifestyle",
        "keywords": [
            "travel with IBD",
            "We Can't Wait",
            "IBD bathroom access",
            "flying with biologics",
            "Foundation restroom access",
        ],
        "title": "Travel & Restroom Access | Foundation We Can't Wait | IBDPal",
        "description": "Foundation-attributed guide to IBD travel planning and restroom access education, including We Can't Wait themes. Not medical or legal advice.",
        "h1": "IBD travel and restroom access: Foundation bridge",
        "intro": LICENSE_INTRO,
        "sections": [
            {
                "heading": "Plan the trip around care, not around hope",
                "paragraphs": [
                    "Travel with Crohn's or ulcerative colitis is often doable with planning for bathrooms, medications, food, and after-hours contacts.",
                    "Foundation restroom access and patient education help families prepare for urgency in public places and while traveling.",
                    "Carry medicines in original labeled packaging when possible, plus a clinician letter for injectables or infusion schedules if your team recommends one.",
                ],
            },
            {
                "heading": "Restroom access and We Can't Wait themes",
                "paragraphs": [
                    "Foundation We Can't Wait resources focus on finding restrooms and advocating for bathroom access when urgency hits.",
                    "Know local laws and store policies vary. Education cards do not override private property rules everywhere.",
                    "Practice a short script for staff and keep hydration and spare supplies in your bag.",
                ],
            },
            {
                "heading": "Using IBDPal on the road",
                "paragraphs": [
                    "Log flares, food experiments, and medication timing across time zones to share after you return.",
                    "Save Foundation travel and restroom pages before you lose Wi-Fi.",
                    "Seek local urgent care for red-flag symptoms abroad rather than waiting for your home clinic.",
                ],
            },
        ],
        "tips": [
            "Pack extra doses and a written medication list in your carry-on",
            "Map bathrooms near lodging, transit hubs, and venues",
            "Ask about vaccine and infection planning before international trips",
        ],
        "related": [
            {"label": "Foundation We Can't Wait / restroom access (original source)", "url": "https://www.crohnscolitisfoundation.org/patientsandcaregivers/wecantwait"},
            {"label": "Foundation patients and caregivers", "url": "https://www.crohnscolitisfoundation.org/patientsandcaregivers"},
            {"label": "Travel with IBD article", "url": "/blog/travel-with-ibd"},
            {"label": "Vaccines Foundation bridge", "url": "/guides/foundation-ibd-vaccines-infection"},
            {"label": "Workplace and school rights deep dive", "url": "/guides/foundation-workplace-school-rights-ibd"},
            {"label": "Foundation resources hub", "url": "/crohns-colitis-foundation-resources"},
        ],
        "faq": [
            {
                "q": "Does a restroom card guarantee bathroom access everywhere?",
                "a": "No. It can help explain urgency. Laws and business policies differ by place.",
            },
            {
                "q": "Can I put biologics in checked luggage?",
                "a": "Many clinicians prefer carry-on with temperature guidance from the pharmacy. Confirm storage rules for your specific product.",
            },
        ],
    },
    {
        "slug": "foundation-ibd-intimacy-sexual-health",
        "category": "lifestyle",
        "keywords": [
            "IBD intimacy",
            "Crohn's sexual health",
            "ulcerative colitis dating",
            "IBD contraception",
            "Foundation intimacy education",
        ],
        "title": "IBD Intimacy & Sexual Health | Foundation Bridge | IBDPal",
        "description": "Bridge to Crohn's & Colitis Foundation education on intimacy, relationships, and sexual health with IBD. Attribution to the Foundation. Not clinical advice.",
        "h1": "IBD intimacy and sexual health: Foundation bridge",
        "intro": LICENSE_INTRO,
        "sections": [
            {
                "heading": "Relationships and IBD can coexist",
                "paragraphs": [
                    "Foundation education on intimacy and related women's health topics emphasizes that people with IBD can have fulfilling relationships with open communication.",
                    "Flares, fatigue, body image, ostomy or pouch status, and urgency can affect desire or comfort. That does not mean intimacy is off-limits.",
                    "Pain with intercourse, new pelvic symptoms, or perianal disease need clinical evaluation, not only lifestyle tips.",
                ],
            },
            {
                "heading": "Contraception and medication conversations",
                "paragraphs": [
                    "Some contraceptive methods interact with clot risk, bone health, or IBD medication plans. Foundation intimacy and contraception education is a starting point for questions.",
                    "Coordinate gastroenterology with gynecology or primary care before changing birth control.",
                    "Pregnancy planning is a separate conversation. See the Foundation pregnancy bridge on IBDPal for that pathway.",
                ],
            },
            {
                "heading": "How IBDPal fits",
                "paragraphs": [
                    "Track fatigue, pain, and flare timing if those patterns matter for relationship planning, without sharing private logs unless you choose to.",
                    "Use Foundation original pages for intimacy education themes.",
                    "IBDPal does not provide couples therapy or sexual medicine care.",
                ],
            },
        ],
        "tips": [
            "Write questions for GI and gynecology ahead of visits",
            "Discuss ostomy intimacy resources with your stoma nurse when relevant",
            "Seek urgent care for severe pelvic or infectious symptoms",
        ],
        "related": [
            {"label": "Foundation intimacy and contraception (original source)", "url": "https://www.crohnscolitisfoundation.org/effects-of-ibd-on-women/intimacy-and-contraception"},
            {"label": "Foundation patients and caregivers", "url": "https://www.crohnscolitisfoundation.org/patientsandcaregivers"},
            {"label": "Pregnancy IBD Foundation resources", "url": "/guides/pregnancy-ibd-foundation-resources"},
            {"label": "Dating and intimacy article", "url": "/blog/dating-intimacy-ibd-adults"},
            {"label": "Surgery and ostomy Foundation bridge", "url": "/guides/foundation-ibd-surgery-ostomy"},
            {"label": "Foundation resources hub", "url": "/crohns-colitis-foundation-resources"},
        ],
        "faq": [
            {
                "q": "Should I tell a new partner about IBD?",
                "a": "That is a personal choice. Many people share bathroom and energy needs early. Foundation education supports honest communication without requiring medical detail dumps.",
            },
            {
                "q": "Is this page only for women?",
                "a": "Foundation intimacy themes apply broadly. Some contraception content is written for people who can become pregnant. Ask your clinicians about your situation.",
            },
        ],
    },
    {
        "slug": "foundation-ibd-vaccines-infection",
        "category": "treatment",
        "keywords": [
            "IBD vaccines",
            "biologics live vaccines",
            "immunosuppressant infection risk",
            "Foundation vaccine education IBD",
        ],
        "title": "IBD Vaccines & Infection Risk | Foundation Bridge | IBDPal",
        "description": "Foundation-attributed education bridge on vaccines and infection awareness for people on IBD therapies. Not an immunization schedule.",
        "h1": "IBD vaccines and infection risk: Foundation bridge",
        "intro": LICENSE_INTRO,
        "sections": [
            {
                "heading": "Why vaccines are part of IBD safety",
                "paragraphs": [
                    "People with IBD, especially those on steroids, immunomodulators, or biologics, often need proactive vaccine planning and infection awareness.",
                    "Foundation medication and patient education repeatedly stresses asking about vaccines before escalating immunosuppression when timing allows.",
                    "Live vaccines may be restricted on certain regimens. Inactivated vaccines are commonly discussed for flu, COVID-19, pneumonia, and other age-based shots.",
                ],
            },
            {
                "heading": "Infection precautions to review with your team",
                "paragraphs": [
                    "Ask which fever or cough thresholds should trigger a call, whether TB or hepatitis screening is current, and how travel vaccines fit your drugs.",
                    "Household contacts staying up to date can add a layer of protection.",
                    "Do not skip prescribed IBD therapy because of vaccine anxiety without clinician guidance.",
                ],
            },
            {
                "heading": "Using IBDPal",
                "paragraphs": [
                    "Log vaccine dates, infections, and antibiotic courses next to IBD medications.",
                    "Pair Foundation medication education with IBDPal vaccine articles for clinic questions.",
                    "IBDPal does not issue vaccine orders or travel clearance.",
                ],
            },
        ],
        "tips": [
            "Bring an immunization record to GI and primary care",
            "Ask about live vaccine rules before travel or school requirements",
            "Report fever promptly when immunosuppressed",
        ],
        "related": [
            {"label": "Foundation IBD Medication Guide (original source)", "url": "https://www.crohnscolitisfoundation.org/patientsandcaregivers/ibd-medication-guide"},
            {"label": "Foundation patients and caregivers", "url": "https://www.crohnscolitisfoundation.org/patientsandcaregivers"},
            {"label": "Vaccines with biologics article", "url": "/blog/vaccines-biologics-immunosuppressants-ibd"},
            {"label": "Foundation Medication Guide bridge", "url": "/guides/foundation-ibd-medication-guide"},
            {"label": "Travel and restroom Foundation bridge", "url": "/guides/foundation-ibd-travel-restroom-access"},
            {"label": "Foundation resources hub", "url": "/crohns-colitis-foundation-resources"},
        ],
        "faq": [
            {
                "q": "Can I get a flu shot on a biologic?",
                "a": "Often yes for inactivated flu vaccine, but confirm with your IBD clinician and primary care for your regimen and timing.",
            },
            {
                "q": "Should I pause my biologic around vaccines?",
                "a": "Sometimes timing is adjusted; sometimes it is not. Only your care team should decide.",
            },
        ],
    },
    {
        "slug": "foundation-ibd-colonoscopy-cancer-surveillance",
        "category": "clinical",
        "keywords": [
            "IBD colonoscopy surveillance",
            "ulcerative colitis cancer risk",
            "dysplasia IBD",
            "Foundation colorectal cancer education",
        ],
        "title": "IBD Colonoscopy & Cancer Surveillance | Foundation Bridge | IBDPal",
        "description": "Bridge to Crohn's & Colitis Foundation patient education themes on colonoscopy and colorectal cancer surveillance in IBD. Not a screening schedule.",
        "h1": "IBD colonoscopy and cancer surveillance: Foundation bridge",
        "intro": LICENSE_INTRO,
        "sections": [
            {
                "heading": "Why surveillance comes up in long-standing colitis",
                "paragraphs": [
                    "Long-standing ulcerative colitis and some Crohn's colitis patterns raise conversations about colorectal cancer risk and timed colonoscopy surveillance.",
                    "Foundation patient education helps explain dysplasia monitoring vocabulary before procedures.",
                    "Your personal interval depends on disease extent, duration, prior findings, family history, and other risk factors decided by your gastroenterologist.",
                ],
            },
            {
                "heading": "How to prepare for the conversation",
                "paragraphs": [
                    "Ask when your next surveillance scope is due, what bowel prep to use, and how biopsy or chromoendoscopy findings would change follow-up.",
                    "Clarify who calls with pathology results and what symptoms between scopes still need urgent review.",
                    "Do not skip surveillance because symptoms feel quiet. Quiet guts can still need scheduled checks when your team recommends them.",
                ],
            },
            {
                "heading": "IBDPal's role",
                "paragraphs": [
                    "Log prep tolerance, post-procedure symptoms, and medication holds so the next cycle is easier.",
                    "Use Foundation patient education as original reading, then follow your clinic's written surveillance plan.",
                    "IBDPal does not set colonoscopy intervals or interpret pathology.",
                ],
            },
        ],
        "tips": [
            "Keep a dated list of past colonoscopies and findings",
            "Ask about primary sclerosing cholangitis if liver tests are abnormal, since that can change surveillance urgency",
            "Treat rectal bleeding or unexplained weight loss as a reason to call, even between scheduled scopes",
        ],
        "related": [
            {"label": "Foundation patients and caregivers (original source)", "url": "https://www.crohnscolitisfoundation.org/patientsandcaregivers"},
            {"label": "What is ulcerative colitis Foundation basics", "url": "/guides/what-is-ulcerative-colitis-foundation"},
            {"label": "Surgery and ostomy Foundation bridge", "url": "/guides/foundation-ibd-surgery-ostomy"},
            {"label": "Newly diagnosed Foundation pathway", "url": "/guides/newly-diagnosed-foundation-first-week"},
            {"label": "Foundation resources hub", "url": "/crohns-colitis-foundation-resources"},
        ],
        "faq": [
            {
                "q": "Does everyone with IBD need the same colonoscopy schedule?",
                "a": "No. Intervals are individualized. Foundation education explains why surveillance exists; your GI sets the calendar.",
            },
            {
                "q": "If dysplasia is found, is surgery automatic?",
                "a": "Not always. Management depends on findings and guidelines your team applies. Ask for a clear written plan.",
            },
        ],
    },
]


def main() -> None:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    pages: list[dict] = data["pages"]
    existing = {p["slug"] for p in pages}
    added = []
    for guide in WAVE3:
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
