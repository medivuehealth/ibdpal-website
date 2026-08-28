#!/usr/bin/env python3
"""Generate static patient-resource HTML pages with full SEO heads."""
from __future__ import annotations
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from eeat_blocks import content_note_en, ccf_nonaffiliation_about_en, edu_disclaimer_en, hub_disclaimer_en, page_review_props # noqa: E402
from es_mirrors import es_url_for_en_path # noqa: E402
from seo_head import breadcrumb_json, howto_json, render_seo_head, web_page_json, THEME_COLOR_META, VIEWPORT_META # noqa: E402
from site_nav import PAGE_SCRIPTS, TAB_NAV_HTML, site_header_html # noqa: E402
from site_footer import SITE_FOOTER_STATIC # noqa: E402
from ui_snippets import ( # noqa: E402
    IBD_NEWS_TAB_HTML,
    RESOURCE_TOOLBAR_HTML,
    SITE_UPDATES_SUBTAB_HTML,
    UPDATES_MONTHLY_SECTIONS_HTML,
)

SITE = "https://www.ibdpal.org"
EEAT_PATHS = {
    "/start-here",
    "/newly-diagnosed",
    "/what-is-ibd",
    "/crohns-and-colitis",
    "/visit-prep",
    "/pediatric-caregivers",
    "/resources",
    "/crohns-colitis-foundation-resources",
    "/ibd-autoimmune-associations",
    "/trusted-ibd-resources",
    "/ibd-red-flags-urgent-care",
}

NAV = TAB_NAV_HTML

FOOTER = SITE_FOOTER_STATIC

SCRIPTS = PAGE_SCRIPTS

HEAD_ASSETS = """ <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="stylesheet" href="/styles.css">
    <link rel="stylesheet" href="/site-layout-icn.css">
    <link rel="stylesheet" href="/site-polish.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet">
    <link rel="icon" type="image/x-icon" href="/favicon.ico">
    <link rel="icon" type="image/png" href="/IBDPal_Logo.png">
    <link rel="apple-touch-icon" href="/IBDPal_Logo.png">
"""


VISIT_PREP_HOWTO = howto_json(
    name="Prepare for an IBD gastroenterology visit",
    description="Printable checklist: gather symptoms, medications, and questions before a Crohn's or colitis appointment.",
    path="/visit-prep",
    steps=[
        {"name": "Compile symptom summary", "text": "Note pain on a 0-10 scale, stools per day, blood, and fever."},
        {"name": "List medications", "text": "Bring medication names, doses, and last refill dates."},
        {"name": "Note weight and appetite changes", "text": "Record any recent weight loss or appetite shifts."},
        {"name": "Write your top three questions", "text": "Prioritize what you need answered at this visit."},
        {"name": "Bring insurance details", "text": "Carry your insurance card and prior authorization status if on biologics."},
        {"name": "Ask about disease activity", "text": "Discuss whether your IBD is active, in remission, or uncertain."},
        {"name": "Review nutrition labs", "text": "Ask about vitamin deficiencies or nutrition labs."},
        {"name": "Discuss treatment adjustments", "text": "Talk about changes to diet, medications, or scopes."},
        {"name": "Clarify urgent symptoms", "text": "Ask when to call or go to urgent care."},
        {"name": "Record follow-up plans", "text": "Note the next appointment date and portal messages."},
        {"name": "Update your health log", "text": "Log plan changes in IBDPal or your symptom tracker."},
    ],
)


def faq_json_ld(faq: list[dict], path: str) -> dict:
    return {
        "@type": "FAQPage",
        "@id": f"{SITE}{path}#faq",
        "mainEntity": [
            {
                "@type": "Question",
                "name": item["q"],
                "acceptedAnswer": {"@type": "Answer", "text": item["a"]},
            }
            for item in faq
        ],
    }


WHAT_IS_IBD_FAQ = faq_json_ld(
    [
        {
            "q": "What is inflammatory bowel disease (IBD)?",
            "a": "IBD is a group of chronic conditions that cause inflammation in the digestive tract. The two main types are Crohn's disease and ulcerative colitis. A gastroenterologist diagnoses IBD after history, exam, labs, imaging, and often endoscopy.",
        },
        {
            "q": "Is IBD the same as irritable bowel syndrome (IBS)?",
            "a": "No. IBD involves inflammation that can damage the bowel over time. IBS is a functional syndrome without the same inflammatory injury pattern. Only your clinician can tell which you have.",
        },
        {
            "q": "Can diet alone cure Crohn's or colitis?",
            "a": "No. Diet supports medical care but does not replace prescribed treatment. Many patients work with a GI doctor and sometimes a dietitian on nutrition plans alongside medication or other therapies.",
        },
    ],
    "/what-is-ibd",
)

CROHNS_COLITIS_FAQ = faq_json_ld(
    [
        {
            "q": "What is the difference between Crohn's disease and ulcerative colitis?",
            "a": "Crohn's can affect any part of the digestive tract from mouth to anus and often skips areas. Ulcerative colitis involves the colon and rectum in a continuous pattern. Your GI team names your type after testing.",
        },
        {
            "q": "Are Crohn's and colitis autoimmune diseases?",
            "a": "IBD involves immune dysregulation and inflammation in the gut. Patients often hear 'autoimmune' in education materials, but your clinician can explain how this applies to your case and treatment plan.",
        },
        {
            "q": "When should I call my clinic for Crohn's or colitis symptoms?",
            "a": "Follow your team's plan. Many clinics want a call for worsening pain, frequent bloody stools, fever, dehydration, or symptoms that feel like your usual flare pattern. See our red flags guide for urgent symptoms.",
        },
    ],
    "/crohns-and-colitis",
)


PILLAR_EXTRA_GRAPH: dict[str, list[dict]] = {
    "what-is-ibd.html": [WHAT_IS_IBD_FAQ],
    "crohns-and-colitis.html": [CROHNS_COLITIS_FAQ],
}


def shell(
    title: str,
    description: str,
    path: str,
    body: str,
    active_nav: str = "",
    extra_graph: list[dict] | None = None,
) -> str:
    nav = NAV
    if active_nav:
        nav = nav.replace(
            f'href="{active_nav}" class="tab-button"',
            f'href="{active_nav}" class="tab-button active"',
            1,
        )
    crumb_name = title.split("|")[0].strip()
    if path in EEAT_PATHS:
        body = content_note_en() + edu_disclaimer_en() + body + f"\n {hub_disclaimer_en()}"
    graph = [
        breadcrumb_json(path, crumb_name),
        {**web_page_json(path, crumb_name, description, medical=True), **(page_review_props() if path in EEAT_PATHS else {})},
    ]
    if extra_graph:
        graph.extend(extra_graph)
    json_ld = {"@context": "https://schema.org", "@graph": graph}
    hreflang_es = es_url_for_en_path(path) or f"{SITE}/es/recursos"
    seo = render_seo_head(
        title=title,
        description=description,
        path=path,
        json_ld=json_ld,
        hreflang_es=hreflang_es,
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
{VIEWPORT_META}
{THEME_COLOR_META}
{seo}{HEAD_ASSETS}</head>
<body>
    <div class="container">
{site_header_html()}
{nav}
        <main class="main-content" id="main-content">
{body}
        </main>
{FOOTER}
    </div>
{SCRIPTS}
</body>
</html>
"""


PAGES = {
    "start-here.html": (
        "Start Here with IBD | Newly Diagnosed Roadmap | IBDPal",
        "A calm first path through IBDPal for Crohn's and colitis: diagnosis basics, first GI visit, flare planning, tracking, and trusted support.",
        "/start-here",
        """
            <article class="support-section seo-landing">
                <h1>Start Here with IBD</h1>
                <p class="support-intro">If Crohn's disease or ulcerative colitis is new to you, start with a simple path. Learn the basics, prepare for your first appointments, make a flare plan, and connect with trusted support.</p>
                <section class="seo-landing__block">
                    <h2>1. Understand the diagnosis</h2>
                    <p>IBD is a chronic inflammatory condition. Crohn's disease can affect any part of the digestive tract; ulcerative colitis affects the colon. Your GI team will explain your disease location, severity, and treatment goals.</p>
                    <p><a href="/newly-diagnosed">Newly diagnosed hub</a> · <a href="/what-is-ibd">What is IBD?</a> · <a href="/crohns-and-colitis">Crohn's and colitis guide</a> · <a href="/crohns-disease">Crohn's hub</a> · <a href="/ulcerative-colitis">Ulcerative colitis hub</a></p>
                </section>
                <section class="seo-landing__block">
                    <h2>2. Prepare for the first GI visit</h2>
                    <ul class="seo-landing__list">
                        <li>Bring prior scopes, labs, imaging reports, and medication lists.</li>
                        <li>Write your top three questions before the visit.</li>
                        <li>Ask who to call after hours and what symptoms need urgent attention.</li>
                    </ul>
                    <p><a href="/guides/first-gastroenterology-appointment-ibd">First GI appointment guide</a> · <a href="/visit-prep">Printable visit prep checklist</a></p>
                </section>
                <section class="seo-landing__block">
                    <h2>3. Make a flare plan before you need it</h2>
                    <p>A flare plan should come from your care team. Keep clinic contact details, medication instructions, and red-flag symptoms in one place.</p>
                    <p><a href="/flare-help">Flare help hub</a> · <a href="/ibd-red-flags-urgent-care">Red flags and urgent care guide</a> · <a href="/guides/ibd-flare-emergency-supplies">Flare supplies guide</a></p>
                </section>
                <section class="seo-landing__block">
                    <h2>4. Track what matters</h2>
                    <p>Short daily notes help appointments go better: stools, pain, blood, fatigue, meals, medications, and weight changes. IBDPal can help you organize patterns and export a visit summary.</p>
                    <p><a href="/guides/track-ibd-symptoms-food">Symptom tracking guide</a> · <a href="/#app">IBDPal app</a></p>
                </section>
                <section class="seo-landing__block">
                    <h2>5. Find support you can trust</h2>
                    <p>Use national organizations and clinician-reviewed resources alongside your medical team. IBDPal links out to trusted networks; Foundation Marks/content appear under license and do not imply endorsement.</p>
                    <p><a href="/crohns-colitis-foundation-resources">Crohn's &amp; Colitis Foundation resources</a> · <a href="/trusted-ibd-resources">Trusted IBD resources</a> · <a href="/#community">State support map</a></p>
                </section>
            </article>
        """,
    ),
    "newly-diagnosed.html": (
        "Newly Diagnosed with IBD | First Steps | IBDPal",
        "Newly diagnosed with Crohn's or ulcerative colitis? Questions for your GI, IBDPal app basics, IBD support groups, and trusted national resources.",
        "/newly-diagnosed",
        """
            <article class="support-section seo-landing">
                <h1>Newly Diagnosed with IBD?</h1>
                <p class="support-intro">A Crohn's disease or ulcerative colitis diagnosis is a lot to absorb. This hub gathers calm next steps, not a substitute for your gastroenterologist.</p>
                <section class="seo-landing__block">
                    <h2>Crohn's vs. ulcerative colitis (briefly)</h2>
                    <p>Both are inflammatory bowel diseases. Crohn's can affect any part of the digestive tract; colitis primarily involves the colon. Your team will name your type, severity, and treatment goals.</p>
                    <p><a href="/what-is-ibd">What is IBD?</a> · <a href="/crohns-and-colitis">Crohn's and colitis compared</a></p>
                </section>
                <section class="seo-landing__block">
                    <h2>Questions for your first GI visits</h2>
                    <ul class="seo-landing__list">
                        <li>What type of IBD do I have, and how active is it?</li>
                        <li>What labs, imaging, or scopes are planned?</li>
                        <li>Which medications are options for me?</li>
                        <li>What symptoms should trigger a call or urgent visit?</li>
                        <li>Are there diet patterns or deficiencies I should watch?</li>
                    </ul>
                    <p><a href="/visit-prep" class="seo-landing__cta">Printable visit prep checklist →</a></p>
                </section>
                <section class="seo-landing__block">
                    <h2>How IBDPal can help day to day</h2>
                    <p>Track meals, symptoms, medications, and micronutrients; spot patterns; and feel more prepared for appointments. <a href="/#app">Explore the app</a> · <a href="/#overview">Download overview</a>.</p>
                    <p class="app-deep-links"><strong>In the app:</strong> Daily Log · Home Dashboard · Trend charts · Community (peer support).</p>
                </section>
                <section class="seo-landing__block">
                    <h2>Peer and national support</h2>
                    <p><a href="/ibd-crohns-support">IBD Crohn's support guide</a> · <a href="/#community">State community map</a> · CCF Help Center <a href="tel:8886948872">888-694-8872</a></p>
                </section>
            </article>
        """,
    ),
    "what-is-ibd.html": (
        "What Is IBD? Inflammatory Bowel Disease Explained | IBDPal",
        "What is inflammatory bowel disease (IBD)? Learn how Crohn's disease and ulcerative colitis differ from IBS, common symptoms, diagnosis steps, and trusted next resources.",
        "/what-is-ibd",
        """
            <article class="support-section seo-landing">
                <h1>What Is Inflammatory Bowel Disease (IBD)?</h1>
                <p class="support-intro">Inflammatory bowel disease (IBD) is a group of chronic conditions that cause inflammation in the digestive tract. The two main types are Crohn's disease and ulcerative colitis. This page explains the basics in plain language. It does not replace your gastroenterologist.</p>
                <section class="seo-landing__block">
                    <h2>Crohn's disease and ulcerative colitis</h2>
                    <p>Both are forms of IBD. Crohn's disease can affect any part of the digestive tract from mouth to anus and often has skip areas. Ulcerative colitis involves the colon and rectum in a continuous pattern. Some patients have features that do not fit neatly into one category; your GI team names your type after history, exam, labs, imaging, and often endoscopy.</p>
                    <p><a href="/crohns-and-colitis">Crohn's and colitis compared</a> · <a href="/crohns-disease">Crohn's disease hub</a> · <a href="/ulcerative-colitis">Ulcerative colitis hub</a></p>
                </section>
                <section class="seo-landing__block">
                    <h2>IBD is not the same as IBS</h2>
                    <p>Irritable bowel syndrome (IBS) is a functional bowel disorder. IBD involves inflammation that can damage the bowel over time and usually needs specialist monitoring and treatment. Only your clinician can tell which condition you have.</p>
                </section>
                <section class="seo-landing__block">
                    <h2>Common symptoms (not a diagnosis)</h2>
                    <ul class="seo-landing__list">
                        <li>Abdominal pain or cramping</li>
                        <li>Diarrhea, sometimes with blood or mucus</li>
                        <li>Urgency, fatigue, or unintended weight loss</li>
                        <li>Symptoms outside the gut, such as joint pain or skin changes (extraintestinal manifestations)</li>
                    </ul>
                    <p>Symptoms vary widely. Some people have mild disease; others have frequent flares. Track patterns and bring them to clinic visits.</p>
                    <p><a href="/flare-help">Flare help hub</a> · <a href="/ibd-red-flags-urgent-care">Red flags and urgent care</a></p>
                </section>
                <section class="seo-landing__block">
                    <h2>How IBD is usually diagnosed</h2>
                    <p>Diagnosis typically combines your story, physical exam, blood and stool tests, imaging, and endoscopy (colonoscopy or upper endoscopy). Pathology from biopsies helps confirm inflammation and rule out other causes.</p>
                    <p><a href="/newly-diagnosed">Newly diagnosed hub</a> · <a href="/visit-prep">Visit prep checklist</a> · <a href="/stool-labs-decoder">Stool and labs decoder</a></p>
                </section>
                <section class="seo-landing__block">
                    <h2>Treatment and day-to-day management</h2>
                    <p>Goals often include controlling inflammation, healing the bowel when possible, and improving quality of life. Plans may include medications, nutrition support, surgery in some cases, and mental health care. Diet supports medical care but does not replace prescribed treatment.</p>
                    <p><a href="/ibd-nutrition">Nutrition hub</a> · <a href="/guides/foundation-ibd-medication-guide">Medication guide bridge</a> · <a href="/start-here">Start here roadmap</a></p>
                </section>
                <section class="seo-landing__block">
                    <h2>Trusted Foundation education</h2>
                    <p>Selected IBDPal guides attribute patient education from the Crohn's &amp; Colitis Foundation and link to the original pages.</p>
                    <ul class="seo-landing__list">
                        <li><a href="https://www.crohnscolitisfoundation.org/what-is-ibd" rel="noopener noreferrer">Foundation: What is IBD</a></li>
                        <li><a href="/guides/what-is-ibd-foundation">IBDPal guide: What is IBD (Foundation basics)</a></li>
                        <li><a href="/crohns-colitis-foundation-resources">Foundation resources hub</a></li>
                    </ul>
                </section>
                <section class="seo-landing__block" id="faq">
                    <h2>Common questions</h2>
                    <h3>What is inflammatory bowel disease (IBD)?</h3>
                    <p>IBD is a group of chronic conditions that cause inflammation in the digestive tract. The two main types are Crohn's disease and ulcerative colitis. A gastroenterologist diagnoses IBD after history, exam, labs, imaging, and often endoscopy.</p>
                    <h3>Is IBD the same as irritable bowel syndrome (IBS)?</h3>
                    <p>No. IBD involves inflammation that can damage the bowel over time. IBS is a functional syndrome without the same inflammatory injury pattern. Only your clinician can tell which you have.</p>
                    <h3>Can diet alone cure Crohn's or colitis?</h3>
                    <p>No. Diet supports medical care but does not replace prescribed treatment. Many patients work with a GI doctor and sometimes a dietitian on nutrition plans alongside medication or other therapies.</p>
                    <p><a href="/faq">More IBD FAQ</a></p>
                </section>
            </article>
        """,
    ),
    "crohns-and-colitis.html": (
        "Crohn's and Colitis: What's the Difference? | IBDPal",
        "Crohn's disease vs ulcerative colitis: location in the gut, symptoms, diagnosis, treatment education, and when to call your clinic. Patient-friendly IBD comparison guide.",
        "/crohns-and-colitis",
        """
            <article class="support-section seo-landing">
                <h1>Crohn's and Colitis: What's the Difference?</h1>
                <p class="support-intro">People often search for Crohn's and colitis together because both are inflammatory bowel diseases (IBD). They share some symptoms but differ in where inflammation occurs and how disease behaves. Your gastroenterologist confirms your type and plan.</p>
                <section class="seo-landing__block">
                    <h2>Side-by-side overview</h2>
                    <table class="seo-landing__table">
                        <thead><tr><th scope="col">Topic</th><th scope="col">Crohn's disease</th><th scope="col">Ulcerative colitis</th></tr></thead>
                        <tbody>
                            <tr><th scope="row">Where it occurs</th><td>Any part of the digestive tract (mouth to anus); may skip segments</td><td>Colon and rectum; continuous pattern</td></tr>
                            <tr><th scope="row">Common symptoms</th><td>Abdominal pain, diarrhea, weight loss, fatigue; perianal disease in some patients</td><td>Bloody diarrhea, urgency, abdominal pain, fatigue</td></tr>
                            <tr><th scope="row">Depth of inflammation</th><td>Can affect full thickness of the bowel wall</td><td>Typically inner lining (mucosa) of the colon</td></tr>
                            <tr><th scope="row">Surgery</th><td>May be needed for strictures, fistulas, or refractory disease; not usually curative</td><td>Colectomy can be curative for colitis in some cases</td></tr>
                        </tbody>
                    </table>
                    <p>This table is educational only. Your endoscopy and pathology reports define your disease.</p>
                </section>
                <section class="seo-landing__block">
                    <h2>Shared features of Crohn's and colitis</h2>
                    <ul class="seo-landing__list">
                        <li>Chronic immune-mediated inflammation in the gut</li>
                        <li>Flares and remission periods for many patients</li>
                        <li>Need for gastroenterology follow-up and monitoring</li>
                        <li>Possible extraintestinal symptoms (joints, skin, eyes)</li>
                        <li>Nutrition, mental health, and family planning topics that overlap both conditions</li>
                    </ul>
                    <p><a href="/what-is-ibd">What is IBD?</a> · <a href="/ibd-autoimmune-associations">Autoimmune associations hub</a></p>
                </section>
                <section class="seo-landing__block">
                    <h2>When to call your clinic</h2>
                    <p>Follow your team's plan. Many clinics want a call for worsening pain, frequent bloody stools, fever, signs of dehydration, or symptoms that match your usual flare pattern.</p>
                    <p><a href="/ibd-red-flags-urgent-care">Red flags guide</a> · <a href="/flare-help">Flare help hub</a> · CCF Help Center <a href="tel:8886948872">888-694-8872</a> (education, not emergency care)</p>
                </section>
                <section class="seo-landing__block">
                    <h2>Go deeper by condition</h2>
                    <ul class="seo-landing__list">
                        <li><a href="/crohns-disease">Crohn's disease hub</a> (symptoms, diet, surgery topics)</li>
                        <li><a href="/ulcerative-colitis">Ulcerative colitis hub</a> (flare diet, j-pouch basics)</li>
                        <li><a href="/guides/what-is-crohns-disease-foundation">Foundation guide: Crohn's basics</a></li>
                        <li><a href="/guides/what-is-ulcerative-colitis-foundation">Foundation guide: Colitis basics</a></li>
                        <li><a href="/newly-diagnosed">Newly diagnosed first steps</a></li>
                    </ul>
                </section>
                <section class="seo-landing__block">
                    <h2>Track patterns between visits</h2>
                    <p>Logging meals, stools, pain, and medications helps you and your clinician spot trends. <a href="/#app">Explore the IBDPal app</a> · <a href="/visit-prep">Printable visit prep</a></p>
                </section>
                <section class="seo-landing__block" id="faq">
                    <h2>Common questions</h2>
                    <h3>What is the difference between Crohn's disease and ulcerative colitis?</h3>
                    <p>Crohn's can affect any part of the digestive tract from mouth to anus and often skips areas. Ulcerative colitis involves the colon and rectum in a continuous pattern. Your GI team names your type after testing.</p>
                    <h3>Are Crohn's and colitis autoimmune diseases?</h3>
                    <p>IBD involves immune dysregulation and inflammation in the gut. Patients often hear "autoimmune" in education materials, but your clinician can explain how this applies to your case and treatment plan.</p>
                    <h3>When should I call my clinic for Crohn's or colitis symptoms?</h3>
                    <p>Follow your team's plan. Many clinics want a call for worsening pain, frequent bloody stools, fever, dehydration, or symptoms that feel like your usual flare pattern. See our red flags guide for urgent symptoms.</p>
                    <p><a href="/faq">More IBD FAQ</a></p>
                </section>
            </article>
        """,
    ),
    "visit-prep.html": (
        "IBD Doctor Visit Prep Checklist (Printable) | IBDPal",
        "Free printable Crohn's and colitis appointment checklist: symptoms, medications, questions, and trends to share with your gastroenterologist.",
        "/visit-prep",
        """
            <article class="support-section visit-prep-page">
                <h1>IBD Doctor Visit Prep</h1>
                <p class="support-intro">Bring this checklist to gastroenterology visits. Export logs from IBDPal when available.</p>
                <div class="visit-prep-sheet" id="visit-prep-print">
                    <h2>Before you go</h2>
                    <ul class="visit-checklist"><li>☐ Symptom summary (pain 0-10, stools/day, blood, fever)</li>
                    <li>☐ Medication list with doses and last refill dates</li>
                    <li>☐ Weight change or appetite notes</li>
                    <li>☐ Top 3 questions written down</li>
                    <li>☐ Insurance card and prior auth status (if on biologics)</li></ul>
                    <h2>Discuss with your clinician</h2>
                    <ul class="visit-checklist"><li>☐ Is my disease active, in remission, or uncertain?</li>
                    <li>☐ Nutrition labs or vitamin deficiencies?</li>
                    <li>☐ Adjustments to diet, meds, or scopes?</li>
                    <li>☐ When should I call or go to urgent care?</li></ul>
                    <h2>After the visit</h2>
                    <ul class="visit-checklist"><li>☐ Note follow-up date and portal messages</li>
                    <li>☐ Update IBDPal with plan changes</li></ul>
                </div>
                <p><button type="button" class="seo-landing__cta" onclick="window.print()">Print this checklist</button></p>
            </article>
        """,
    ),
    "resources.html": (
        "IBD Resource Library | Crohn's & Colitis Education | IBDPal",
        "Search 25+ IBD resources: nutrition blogs, Crohn's support, pediatric caregivers, visit prep, community map, and the free IBDPal iOS app.",
        "/resources",
        f"""
            <div class="resources-page" data-resource-library>
                <h1>IBD Resource Library</h1>
                <p class="support-intro">Filter trusted articles and tools. External links open in a new tab.</p>
{RESOURCE_TOOLBAR_HTML}
                <div class="resource-library__grid"></div>
            </div>
            <script src="/resources-data.js"></script>
            <script src="/resource-library.js" defer></script>
        """,
        "/#resources",
    ),
    "clinical-partnerships.html": (
        "Clinical Partnerships | IBDPal for IBD Programs | IBDPal",
        "Partner with MediVue: IBDPal as a companion self-management tool for hospital and clinic IBD programs, visit prep, logging, and patient education.",
        "/clinical-partnerships",
        """
            <article class="support-section">
                <h1>Clinical Partnerships</h1>
                <p class="support-intro">MediVue is a North Carolina 501(c)(3) nonprofit. IBDPal is designed as a <strong>companion</strong> to, not a replacement for, clinical care.</p>
                <section class="seo-landing__block"><h2>Partnership goals</h2>
                <ul class="seo-landing__list"><li>Improve visit preparation and home logging</li><li>Support nutrition and symptom awareness between appointments</li><li>Connect families to national and local IBD resources</li></ul></section>
                <section class="seo-landing__block"><h2>Interested programs</h2>
                <p>Academic IBD centers, pediatric ImproveCareNow sites, and community hospitals may pilot patient materials, export summaries, and waiting-room education.</p>
                <p>Contact <a href="mailto:contactus@ibdpal.org">contactus@ibdpal.org</a> · <a href="/for-clinicians">Clinician tools overview</a></p></section>
                <section class="seo-landing__block"><h2>Manufacturer &amp; program listings</h2>
                <p>Public patient-support program hubs are curated under <a href="/partners">Partners &amp; programs</a>. Propose a labeled listing via the <a href="/partners/media-kit">partner media kit</a>.</p></section>
            </article>
        """,
    ),
    "pediatric-caregivers.html": (
        "Pediatric IBD & Caregiver Resources | IBDPal",
        "IBD resources for kids and parents: ImproveCareNow, GIKids, school 504 plans, family blogs, and IBDPal tracking for pediatric Crohn's and colitis.",
        "/pediatric-caregivers",
        """
            <article class="support-section seo-landing">
                <h1>Pediatric IBD &amp; Caregivers</h1>
                <p class="support-intro">Children and teens with Crohn's or colitis need team-based care and family support. This page gathers parent, sibling, school, and teen resources in one place.</p>
                <section class="seo-landing__block">
                    <h2>For parents and caregivers</h2>
                    <ul class="seo-landing__list">
                        <li><a href="https://www.improvecarenow.org/patients-parents" rel="noopener noreferrer">ImproveCareNow | Patients, Parents &amp; Families</a></li>
                        <li><a href="https://www.improvecarenow.org/care-centers" rel="noopener noreferrer">Find a pediatric IBD care center</a></li>
                        <li><a href="https://gikids.org/" rel="noopener noreferrer">GIKids patient education</a></li>
                        <li><a href="/blog/icn-caregiver-coping-resource">ICN caregiver coping resource</a></li>
                        <li><a href="/guides/pediatric-crohns-colitis-help">Pediatric Crohn's and colitis help guide</a></li>
                    </ul>
                </section>
                <section class="seo-landing__block">
                    <h2>For siblings</h2>
                    <p>Siblings may feel worry, resentment, guilt, or confusion when plans change around flares and appointments. Short, age-appropriate explanations and one-on-one time can help.</p>
                    <p><a href="/blog/siblings-when-child-has-ibd">When a sibling has IBD</a> · <a href="/blog/living-with-ibd-kids">Living with IBD as a family</a></p>
                </section>
                <section class="seo-landing__block">
                    <h2>For school nurses and 504 teams</h2>
                    <ul class="seo-landing__list">
                        <li>Bathroom access, attendance flexibility, hydration, and medication storage often need explicit plans.</li>
                        <li>Ask the GI team for documentation that supports school accommodations.</li>
                        <li>Keep emergency contacts and after-hours instructions current.</li>
                    </ul>
                    <p><a href="/blog/icn-accommodations-toolkit-ibd">ICN accommodations toolkit</a> · <a href="/guides/ibd-workplace-school-rights">School rights guide</a> · <a href="/blog/workplace-school-ibd-rights">School 504 overview</a></p>
                </section>
                <section class="seo-landing__block">
                    <h2>For teens</h2>
                    <p>Teens may need privacy, independence, and practical scripts for school, sports, dating, and clinic visits. Practice self-advocacy in small steps before transfer to adult care.</p>
                    <p><a href="/teens-and-school">Teens and school hub</a> · <a href="/blog/high-school-ibd-survival-guide">High school survival guide</a> · <a href="/blog/icn-transfer-toolkit-adult-care">Transition to adult care</a></p>
                </section>
                <section class="seo-landing__block">
                    <h2>Tracking between visits</h2>
                    <p>IBDPal can help families log meals, symptoms, sleep, medications, and notes for clinic visits. Use exports as a conversation aid, not as a diagnosis tool.</p>
                    <p><a href="/visit-prep">Visit prep checklist</a> · <a href="/guides/track-ibd-symptoms-food">Symptom tracking guide</a> · <a href="/#app">IBDPal app</a></p>
                </section>
            </article>
        """,
    ),
    "crohns-colitis-foundation-resources.html": (
        "Crohn's & Colitis Foundation Resources Guide | IBDPal",
        "Use Crohn's & Colitis Foundation resources with IBDPal: IBD Help Center (888-MY-GUT-PAIN), Camp Oasis, diet education, prior authorization help, chapters, and support - selected Foundation content under license.",
        "/crohns-colitis-foundation-resources",
        """
            <article class="support-section seo-landing">
                <h1>Crohn's &amp; Colitis Foundation Resources on IBDPal</h1>
                <p class="support-intro">Selected Crohn&rsquo;s &amp; Colitis Foundation educational content and Marks are used on IBDPal under license. This hub points you to Foundation programs and education, then links to IBDPal guides that attribute the Foundation as the source.</p>
                <section class="ccf-home-license ccf-home-license--hub" aria-label="Foundation attribution">
                    <a class="ccf-home-license__logo-link" href="https://www.crohnscolitisfoundation.org/" rel="noopener noreferrer" aria-label="Crohn's and Colitis Foundation website">
                        <img class="ccf-home-license__logo" src="/assets/partners/ccf-logo.svg" width="200" height="60" decoding="async" alt="Crohn's &amp; Colitis Foundation logo">
                    </a>
                    <div class="ccf-home-license__copy">
                        <p class="ccf-home-license__eyebrow">Licensed education</p>
                        <p class="ccf-home-license__headline">Selected education under license from the Crohn&rsquo;s &amp; Colitis Foundation</p>
                        <p class="ccf-home-license__note">Logo and Marks appear unmodified. Foundation pages are the original source. The Foundation does not endorse IBDPal or MediVue.</p>
                    </div>
                </section>
                <section class="seo-landing__block">
                    <h2>What IBDPal may do under license</h2>
                    <ul class="seo-landing__list">
                        <li>Display the Foundation logo unmodified and link to the Foundation website</li>
                        <li>Use selected Foundation educational content with attribution to the original Foundation page</li>
                        <li>Help patients find Help Center, chapter, diet, Camp Oasis, insurance, advocacy, and education resources</li>
                    </ul>
                    <p>We do not mirror every Foundation article or claim Foundation endorsement.</p>
                </section>
                <section class="seo-landing__block">
                    <h2>IBD Help Center</h2>
                    <p>The Foundation's IBD Help Center can help with education, support, and referrals to programs. It does not replace your gastroenterologist or emergency services.</p>
                    <ul class="seo-landing__list">
                        <li>Phone: <a href="tel:8886948872">888-MY-GUT-PAIN (888-694-8872)</a></li>
                        <li>Use for general education, local resources, support groups, and program referrals.</li>
                        <li>For severe symptoms, call your GI team, urgent care, or emergency services.</li>
                    </ul>
                    <p><a href="/blog/when-to-call-ibd-help-center">When to call the Help Center vs your clinic</a> · <a href="/guides/ibd-crohns-colitis-helpline">Helpline numbers guide</a> · <a href="https://www.crohnscolitisfoundation.org/patientsandcaregivers/ibdhelpcenter" rel="noopener noreferrer">Foundation Help Center</a></p>
                </section>
                <section class="seo-landing__block">
                    <h2>Education and disease basics</h2>
                    <p>Read Foundation patient education on the Foundation site (original source). Use those materials alongside guidance from your clinician.</p>
                    <ul class="seo-landing__list">
                        <li><a href="https://www.crohnscolitisfoundation.org/patientsandcaregivers" rel="noopener noreferrer">Patients &amp; caregivers hub</a></li>
                        <li><a href="https://www.crohnscolitisfoundation.org/what-is-crohns-disease" rel="noopener noreferrer">What is Crohn's disease</a></li>
                        <li><a href="https://www.crohnscolitisfoundation.org/what-is-ulcerative-colitis" rel="noopener noreferrer">What is ulcerative colitis</a></li>
                    </ul>
                    <p><a href="https://www.crohnscolitisfoundation.org/" rel="noopener noreferrer">crohnscolitisfoundation.org</a> · <a href="/research">IBDPal trusted sources</a></p>
                </section>
                <section class="seo-landing__block">
                    <h2>Disease basics (Foundation education)</h2>
                    <p>Start with Foundation disease overviews, then use IBDPal guides that attribute those pages and link back to the originals.</p>
                    <ul class="seo-landing__list">
                        <li><a href="https://www.crohnscolitisfoundation.org/what-is-ibd" rel="noopener noreferrer">Foundation: What is IBD</a></li>
                        <li><a href="/guides/what-is-ibd-foundation">IBDPal guide: What is IBD (Foundation basics)</a></li>
                        <li><a href="/guides/what-is-crohns-disease-foundation">IBDPal guide: What is Crohn's disease (Foundation basics)</a></li>
                        <li><a href="/guides/what-is-ulcerative-colitis-foundation">IBDPal guide: What is ulcerative colitis (Foundation basics)</a></li>
                        <li><a href="/guides/newly-diagnosed-foundation-first-week">IBDPal guide: Newly diagnosed first week pathway</a></li>
                    </ul>
                </section>
                <section class="seo-landing__block">
                    <h2>Diet and nutrition</h2>
                    <p>Foundation patient education covers therapeutic diets, working with an IBD dietitian, and nutrition during flares and remission. IBDPal tracks meals and symptoms so you can bring clearer notes to clinic visits.</p>
                    <ul class="seo-landing__list">
                        <li><a href="https://www.crohnscolitisfoundation.org/patientsandcaregivers" rel="noopener noreferrer">Foundation patients &amp; caregivers hub</a> (diet and lifestyle education)</li>
                        <li><a href="/guides/foundation-diet-nutrition-ibd">IBDPal guide: Foundation diet and nutrition resources</a></li>
                        <li><a href="/guides/what-should-i-eat-crohns-colitis">What should I eat with Crohn's or colitis?</a></li>
                        <li><a href="/ibd-nutrition">IBDPal nutrition hub</a></li>
                    </ul>
                </section>
                <section class="seo-landing__block">
                    <h2>Kids, teens, school, and Camp Oasis</h2>
                    <p>The Foundation offers youth and parent education plus Camp Oasis, a summer program for children and teens with IBD. Confirm eligibility, locations, and dates on the Foundation site.</p>
                    <ul class="seo-landing__list">
                        <li><a href="https://www.crohnscolitisfoundation.org/patientandcaregivers/youth-parent-resources" rel="noopener noreferrer">Kids, parents, and teens resources</a></li>
                        <li><a href="https://www.crohnscolitisfoundation.org/get-involved/camp-oasis" rel="noopener noreferrer">Camp Oasis</a></li>
                        <li><a href="/guides/camp-oasis-kids-ibd">IBDPal guide: Camp Oasis and youth IBD support</a></li>
                        <li><a href="/guides/youth-school-foundation-resources">IBDPal guide: youth and school Foundation resources</a></li>
                        <li><a href="/guides/pregnancy-ibd-foundation-resources">IBDPal guide: pregnancy and IBD Foundation resources</a></li>
                        <li><a href="/guides/pediatric-crohns-colitis-help">Pediatric Crohn's and colitis help</a></li>
                        <li><a href="/pediatric-caregivers">Pediatric caregivers hub</a></li>
                    </ul>
                </section>
                <section class="seo-landing__block">
                    <h2>Medications and treatment education</h2>
                    <p>The Foundation IBD Medication Guide helps patients learn drug classes and prepare questions. Therapy choices belong with your gastroenterologist.</p>
                    <ul class="seo-landing__list">
                        <li><a href="https://www.crohnscolitisfoundation.org/patientsandcaregivers/ibd-medication-guide" rel="noopener noreferrer">Foundation IBD Medication Guide</a></li>
                        <li><a href="/guides/foundation-ibd-medication-guide">IBDPal guide: Foundation Medication Guide bridge</a></li>
                        <li><a href="/guides/foundation-ibd-vaccines-infection">IBDPal guide: vaccines and infection risk</a></li>
                        <li><a href="/guides/foundation-complementary-medicine-ibd">IBDPal guide: complementary medicine</a></li>
                        <li><a href="/blog/understanding-biologics-ibd">Understanding biologics article</a></li>
                    </ul>
                </section>
                <section class="seo-landing__block">
                    <h2>Insurance and prior authorization</h2>
                    <p>Many IBD medications require prior authorization. The Foundation publishes patient-facing guidance on navigating denials, appeals, and step therapy. Your clinic and insurer remain the authorities for your case.</p>
                    <ul class="seo-landing__list">
                        <li><a href="https://www.crohnscolitisfoundation.org/your-guide-to-navigating-prior-authorization" rel="noopener noreferrer">Foundation prior authorization guide</a></li>
                        <li><a href="/guides/ibd-prior-authorization-foundation">IBDPal guide: prior authorization with Foundation resources</a></li>
                        <li><a href="/guides/foundation-ibd-appeal-letters">IBDPal guide: insurance appeal letters</a></li>
                        <li><a href="/guides/step-therapy-safe-step-act-ibd">IBDPal guide: step therapy and Safe Step Act</a></li>
                        <li><a href="/blog/insurance-biologics-ibd">Insurance and biologics article</a></li>
                        <li><a href="/blog/prior-authorization-biologics-timeline">Prior authorization timeline article</a></li>
                    </ul>
                </section>
                <section class="seo-landing__block">
                    <h2>Pain, fatigue, and symptoms beyond the gut</h2>
                    <p>Foundation education covers pain, fatigue, and extraintestinal issues such as joints, skin, and eyes. Track patterns and bring them to your care team.</p>
                    <ul class="seo-landing__list">
                        <li><a href="https://www.crohnscolitisfoundation.org/patientsandcaregivers/pain-and-fatigue/pain-management" rel="noopener noreferrer">Foundation pain management</a></li>
                        <li><a href="https://www.crohnscolitisfoundation.org/patientsandcaregivers/pain-and-fatigue/managing-fatigue" rel="noopener noreferrer">Foundation managing fatigue</a></li>
                        <li><a href="/guides/foundation-ibd-pain-fatigue">IBDPal guide: pain and fatigue</a></li>
                        <li><a href="/guides/foundation-ibd-extraintestinal-manifestations">IBDPal guide: extraintestinal manifestations</a></li>
                        <li><a href="/ibd-autoimmune-associations">IBD autoimmune associations hub</a></li>
                    </ul>
                </section>
                <section class="seo-landing__block">
                    <h2>Mental health and emotional wellness</h2>
                    <p>Living with IBD often includes stress, anxiety, or depression. Use Foundation education and peer support alongside licensed mental health care when needed.</p>
                    <ul class="seo-landing__list">
                        <li><a href="https://www.crohnscolitisfoundation.org/patientsandcaregivers" rel="noopener noreferrer">Foundation patients &amp; caregivers hub</a></li>
                        <li><a href="/guides/foundation-emotional-wellness-ibd">IBDPal guide: Foundation emotional wellness resources</a></li>
                        <li><a href="/guides/stress-anxiety-ibd">Stress and anxiety guide</a></li>
                        <li><a href="/blog/stress-emotional-wellness-ibd">Emotional wellness article</a></li>
                        <li><a href="/blog/depression-anxiety-ibd">Depression and anxiety article</a></li>
                    </ul>
                </section>
                <section class="seo-landing__block">
                    <h2>Research and clinical trials</h2>
                    <p>The Foundation funds research and helps patients learn about clinical trial participation. Trial eligibility is decided by study teams and your clinician, not by IBDPal.</p>
                    <ul class="seo-landing__list">
                        <li><a href="https://www.crohnscolitisfoundation.org/" rel="noopener noreferrer">Foundation home</a> (research and trial education)</li>
                        <li><a href="/guides/foundation-ibd-clinical-trials">IBDPal guide: clinical trials and Foundation research education</a></li>
                        <li><a href="/research">IBDPal trusted clinical sources</a></li>
                        <li><a href="/blog/free-government-ibd-research-sources">Free government research sources</a></li>
                    </ul>
                </section>
                <section class="seo-landing__block">
                    <h2>Surgery and ostomy</h2>
                    <p>Some people with Crohn's or ulcerative colitis need surgery or live with an ostomy or pouch. Use Foundation patient education for vocabulary and questions, then decide with your surgical and GI teams.</p>
                    <ul class="seo-landing__list">
                        <li><a href="https://www.crohnscolitisfoundation.org/patientsandcaregivers" rel="noopener noreferrer">Foundation patients &amp; caregivers hub</a></li>
                        <li><a href="/guides/foundation-ibd-surgery-ostomy">IBDPal guide: surgery and ostomy Foundation bridge</a></li>
                        <li><a href="/blog/j-pouch-basics-ibd">J-pouch basics</a></li>
                        <li><a href="/blog/ostomy-basics-ibd">Ostomy basics</a></li>
                    </ul>
                </section>
                <section class="seo-landing__block">
                    <h2>Workplace and school rights</h2>
                    <p>Students and workers with IBD often need bathroom access, flexible attendance, and documentation for accommodations. Foundation education helps families prepare questions. This is not legal advice.</p>
                    <ul class="seo-landing__list">
                        <li><a href="/guides/foundation-workplace-school-rights-ibd">IBDPal guide: Foundation workplace and school rights deep dive</a></li>
                        <li><a href="/guides/ibd-workplace-school-rights">IBDPal overview: workplace and school rights</a></li>
                        <li><a href="/guides/youth-school-foundation-resources">Youth and school Foundation resources</a></li>
                        <li><a href="https://www.crohnscolitisfoundation.org/patientandcaregivers/youth-parent-resources" rel="noopener noreferrer">Foundation youth and parent resources</a></li>
                    </ul>
                </section>
                <section class="seo-landing__block">
                    <h2>Travel, restroom access, and daily living</h2>
                    <p>Foundation We Can't Wait and patient education help with bathroom urgency, travel planning, and intimacy topics. Education only; not legal or sexual-health prescribing advice.</p>
                    <ul class="seo-landing__list">
                        <li><a href="https://www.crohnscolitisfoundation.org/patientsandcaregivers/wecantwait" rel="noopener noreferrer">Foundation We Can't Wait / restroom access</a></li>
                        <li><a href="/guides/foundation-ibd-travel-restroom-access">IBDPal guide: travel and restroom access</a></li>
                        <li><a href="/guides/foundation-ibd-intimacy-sexual-health">IBDPal guide: intimacy and sexual health</a></li>
                        <li><a href="/blog/travel-with-ibd">Travel with IBD article</a></li>
                    </ul>
                </section>
                <section class="seo-landing__block">
                    <h2>Colonoscopy and cancer surveillance</h2>
                    <p>Long-standing colitis often raises surveillance colonoscopy questions. Use Foundation patient education for vocabulary, then follow intervals set by your gastroenterologist.</p>
                    <ul class="seo-landing__list">
                        <li><a href="https://www.crohnscolitisfoundation.org/patientsandcaregivers" rel="noopener noreferrer">Foundation patients &amp; caregivers hub</a></li>
                        <li><a href="/guides/foundation-ibd-colonoscopy-cancer-surveillance">IBDPal guide: colonoscopy and cancer surveillance</a></li>
                        <li><a href="/guides/what-is-ulcerative-colitis-foundation">What is ulcerative colitis (Foundation basics)</a></li>
                    </ul>
                </section>
                <section class="seo-landing__block">
                    <h2>Chapters, events, and support groups</h2>
                    <p>Local chapters can help families find education events, community programs, and support groups. Availability varies by region.</p>
                    <ul class="seo-landing__list">
                        <li><a href="https://www.crohnscolitisfoundation.org/chapters" rel="noopener noreferrer">Find a Foundation chapter</a></li>
                        <li><a href="https://www.crohnscolitisfoundation.org/find-a-support-group" rel="noopener noreferrer">Find a support group</a></li>
                        <li><a href="/guides/find-ccf-chapter-support-group">IBDPal guide: find a chapter or support group</a></li>
                        <li><a href="/#community">IBDPal support by state</a></li>
                        <li><a href="/guides/ibd-support-near-me">Support near me guide</a></li>
                        <li><a href="/guides/crohns-colitis-support-groups">Support groups guide</a></li>
                    </ul>
                </section>
                <section class="seo-landing__block">
                    <h2>Advocacy</h2>
                    <p>The Foundation Action Center helps patients contact lawmakers about IBD access issues such as step therapy. Advocacy is separate from medical advice.</p>
                    <ul class="seo-landing__list">
                        <li><a href="https://www.crohnscolitisfoundation.org/get-involved/be-an-advocate/action-center" rel="noopener noreferrer">Foundation Action Center</a></li>
                        <li><a href="/guides/step-therapy-safe-step-act-ibd">IBDPal guide: step therapy and Safe Step Act</a></li>
                        <li><a href="/#news">IBDPal policy news</a></li>
                    </ul>
                </section>
                <section class="seo-landing__block">
                    <h2>IBDPal guides that attribute the Foundation</h2>
                    <p>These IBDPal pages explain Foundation programs in plain language and link to the original Foundation sources.</p>
                    <ul class="seo-landing__list">
                        <li><a href="/guides/what-is-ibd-foundation">What is IBD (Foundation basics)</a></li>
                        <li><a href="/guides/what-is-crohns-disease-foundation">What is Crohn's disease (Foundation basics)</a></li>
                        <li><a href="/guides/what-is-ulcerative-colitis-foundation">What is ulcerative colitis (Foundation basics)</a></li>
                        <li><a href="/guides/newly-diagnosed-foundation-first-week">Newly diagnosed first-week pathway</a></li>
                        <li><a href="/guides/camp-oasis-kids-ibd">Camp Oasis and youth IBD support</a></li>
                        <li><a href="/guides/youth-school-foundation-resources">Youth and school Foundation resources</a></li>
                        <li><a href="/guides/pregnancy-ibd-foundation-resources">Pregnancy and IBD Foundation resources</a></li>
                        <li><a href="/guides/ibd-prior-authorization-foundation">Prior authorization with Foundation resources</a></li>
                        <li><a href="/guides/foundation-ibd-appeal-letters">Insurance appeal letters</a></li>
                        <li><a href="/guides/step-therapy-safe-step-act-ibd">Step therapy and Safe Step Act</a></li>
                        <li><a href="/guides/foundation-diet-nutrition-ibd">Foundation diet and nutrition resources</a></li>
                        <li><a href="/guides/foundation-emotional-wellness-ibd">Foundation emotional wellness resources</a></li>
                        <li><a href="/guides/find-ccf-chapter-support-group">Find a chapter or support group</a></li>
                        <li><a href="/guides/foundation-ibd-clinical-trials">Clinical trials and Foundation research education</a></li>
                        <li><a href="/guides/foundation-ibd-surgery-ostomy">Surgery and ostomy Foundation bridge</a></li>
                        <li><a href="/guides/foundation-workplace-school-rights-ibd">Workplace and school rights deep dive</a></li>
                        <li><a href="/guides/foundation-ibd-medication-guide">Medication Guide bridge</a></li>
                        <li><a href="/guides/foundation-ibd-pain-fatigue">Pain and fatigue</a></li>
                        <li><a href="/guides/foundation-ibd-extraintestinal-manifestations">Extraintestinal manifestations</a></li>
                        <li><a href="/guides/foundation-complementary-medicine-ibd">Complementary medicine</a></li>
                        <li><a href="/guides/foundation-ibd-travel-restroom-access">Travel and restroom access</a></li>
                        <li><a href="/guides/foundation-ibd-intimacy-sexual-health">Intimacy and sexual health</a></li>
                        <li><a href="/guides/foundation-ibd-vaccines-infection">Vaccines and infection risk</a></li>
                        <li><a href="/guides/foundation-ibd-colonoscopy-cancer-surveillance">Colonoscopy and cancer surveillance</a></li>
                        <li><a href="/guides/ibd-crohns-colitis-helpline">Help Center phone numbers</a></li>
                        <li><a href="/blog/when-to-call-ibd-help-center">Help Center vs clinic</a></li>
                    </ul>
                </section>
                <section class="seo-landing__block">
                    <h2>IBDPal's role</h2>
                    <p>IBDPal curates links to reputable public resources and provides a free tracking app and education library. We do not speak for the Foundation, claim partnership or endorsement, or provide medical advice.</p>
                    <p><a href="/about">About IBDPal</a> · <a href="/trusted-ibd-resources">Trusted IBD resources comparison</a></p>
                </section>
            </article>
        """,
    ),
    "ibd-autoimmune-associations.html": (
        "IBD Autoimmune Associations | EIMs, PSC, Skin & Joints | IBDPal",
        "IBD-centered guide to autoimmune associations and extraintestinal manifestations: joints, eyes, skin, PSC, celiac overlap, bone health, and research links.",
        "/ibd-autoimmune-associations",
        """
            <article class="support-section seo-landing">
                <h1>IBD autoimmune associations</h1>
                <p class="support-intro">Crohn's disease and ulcerative colitis are immune-mediated conditions. Related problems can appear in joints, eyes, skin, liver, mouth, and bones. This hub links IBDPal education and research gateways. It is not a diagnosis tool.</p>
                <section class="seo-landing__block">
                    <h2>Start here</h2>
                    <ul class="seo-landing__list">
                        <li><a href="/blog/ibd-autoimmune-overlap">IBD and autoimmune overlap</a></li>
                        <li><a href="/blog/ibd-extraintestinal-manifestations">Extraintestinal manifestations map</a></li>
                        <li><a href="/research">Research and publication sources</a></li>
                    </ul>
                </section>
                <section class="seo-landing__block">
                    <h2>Joints, skin, and eyes</h2>
                    <ul class="seo-landing__list">
                        <li><a href="/blog/ibd-joint-pain-arthritis">Joint pain and arthritis</a></li>
                        <li><a href="/blog/ankylosing-spondylitis-ibd">Ankylosing spondylitis and IBD</a></li>
                        <li><a href="/blog/psoriasis-ibd-connection">Psoriasis and IBD</a></li>
                        <li><a href="/blog/uveitis-eye-inflammation-ibd">Uveitis and eye inflammation</a></li>
                        <li><a href="/blog/pyoderma-erythema-nodosum-ibd">Erythema nodosum and pyoderma</a></li>
                    </ul>
                </section>
                <section class="seo-landing__block">
                    <h2>Liver, nutrition, and systemic risk</h2>
                    <ul class="seo-landing__list">
                        <li><a href="/blog/psc-ibd-liver">PSC and IBD</a></li>
                        <li><a href="/blog/autoimmune-hepatitis-ibd">Autoimmune hepatitis themes</a></li>
                        <li><a href="/blog/celiac-ibd-screening">Celiac screening with IBD</a></li>
                        <li><a href="/blog/osteoporosis-bone-health-ibd">Osteoporosis and bone health</a></li>
                        <li><a href="/blog/thrombosis-clot-risk-ibd">Clot risk awareness</a></li>
                        <li><a href="/blog/fatigue-autoimmune-ibd">Fatigue across autoimmune and IBD life</a></li>
                        <li><a href="/blog/vaccine-autoimmune-immunosuppression">Vaccines with immunosuppression</a></li>
                    </ul>
                </section>
                <section class="seo-landing__block">
                    <h2>Nutrition guides in this cluster</h2>
                    <ul class="seo-landing__list">
                        <li><a href="/guides/anti-inflammatory-diet-ibd">Anti-inflammatory diet guide</a></li>
                        <li><a href="/guides/iron-deficiency-nutrition-ibd">Iron deficiency nutrition</a></li>
                        <li><a href="/guides/vitamin-d-bone-nutrition-ibd">Vitamin D and bone nutrition</a></li>
                        <li><a href="/guides/protein-healing-ibd-flare">Protein during flares</a></li>
                        <li><a href="/guides/elimination-diet-when-to-stop-ibd">When to stop an elimination diet</a></li>
                    </ul>
                </section>
                <section class="seo-landing__block">
                    <h2>Trusted external starting points</h2>
                    <ul class="seo-landing__list">
                        <li><a href="https://pubmed.ncbi.nlm.nih.gov/?term=extraintestinal+manifestations+inflammatory+bowel+disease" rel="noopener noreferrer">PubMed: extraintestinal manifestations</a></li>
                        <li><a href="https://www.niddk.nih.gov/health-information/liver-disease/primary-sclerosing-cholangitis" rel="noopener noreferrer">NIDDK: primary sclerosing cholangitis</a></li>
                        <li><a href="/trusted-ibd-resources">Trusted IBD resources comparison</a></li>
                    </ul>
                </section>
            </article>
        """,
    ),
    "trusted-ibd-resources.html": (
        "Trusted IBD Resources | IBDPal, CCF, ICN, GI Kids, ACG, AGA",
        "Compare trusted public IBD resources for Crohn's and colitis patients: IBDPal, Crohn's & Colitis Foundation, ImproveCareNow, GI Kids, ACG, AGA, NASPGHAN, and NIH.",
        "/trusted-ibd-resources",
        """
            <article class="support-section seo-landing">
                <h1>Trusted IBD Resources</h1>
                <p class="support-intro">No single website should be your only source for IBD education. Use IBDPal as a guide to practical tracking and patient-friendly pages, then verify decisions with your care team and reputable organizations.</p>
                <section class="seo-landing__block">
                    <h2>Where each resource fits</h2>
                    <ul class="seo-landing__list">
                        <li><strong>IBDPal:</strong> free tracking app, practical guides, state support links, and curated patient education.</li>
                        <li><strong>Crohn's &amp; Colitis Foundation:</strong> national patient education, Help Center, chapters, research, and advocacy.</li>
                        <li><strong>ImproveCareNow:</strong> pediatric IBD quality-improvement network and co-produced family resources.</li>
                        <li><strong>GI Kids / NASPGHAN:</strong> pediatric GI education for families.</li>
                        <li><strong>ACG and AGA:</strong> professional society information and clinical guideline context.</li>
                        <li><strong>NIH / MedlinePlus:</strong> federal health education and condition summaries.</li>
                    </ul>
                </section>
                <section class="seo-landing__block">
                    <h2>Quick links</h2>
                    <ul class="seo-landing__list">
                        <li><a href="https://www.crohnscolitisfoundation.org/" rel="noopener noreferrer">Crohn's &amp; Colitis Foundation</a></li>
                        <li><a href="https://www.improvecarenow.org/" rel="noopener noreferrer">ImproveCareNow</a></li>
                        <li><a href="https://gikids.org/" rel="noopener noreferrer">GI Kids</a></li>
                        <li><a href="https://gi.org/" rel="noopener noreferrer">American College of Gastroenterology</a></li>
                        <li><a href="https://gastro.org/" rel="noopener noreferrer">American Gastroenterological Association</a></li>
                        <li><a href="https://medlineplus.gov/inflammatoryboweldiseases.html" rel="noopener noreferrer">MedlinePlus: inflammatory bowel diseases</a></li>
                    </ul>
                </section>
                <section class="seo-landing__block">
                    <h2>How to use resource pages safely</h2>
                    <p>Look for publication dates, source citations, medical disclaimers, and whether content separates general education from personal medical advice. Bring questions to your GI team before changing medications, supplements, or flare plans.</p>
                    <p><a href="/research">IBDPal trusted clinical sources</a> · <a href="/crohns-colitis-foundation-resources">Foundation resources guide</a> · <a href="/library">IBDPal content library</a></p>
                </section>
            </article>
        """,
    ),
    "ibd-red-flags-urgent-care.html": (
        "IBD Red Flags | When to Call Your GI Team or Seek Urgent Care",
        "Conservative educational guide to IBD warning signs: dehydration, heavy bleeding, fever, severe pain, obstruction symptoms, medication reactions, and when to contact your care team.",
        "/ibd-red-flags-urgent-care",
        """
            <article class="support-section seo-landing">
                <h1>IBD Red Flags: When to Call or Seek Urgent Care</h1>
                <p class="support-intro">This guide is educational and conservative. If symptoms feel severe, new, or unsafe, contact your gastroenterologist, urgent care, emergency services, or local emergency number.</p>
                <section class="seo-landing__block">
                    <h2>Call your GI team promptly</h2>
                    <ul class="seo-landing__list">
                        <li>Symptoms are clearly worsening compared with your usual baseline.</li>
                        <li>New or increasing blood in stool.</li>
                        <li>Persistent diarrhea, urgency, or nighttime stools.</li>
                        <li>Fever, chills, or signs of infection while on immune-suppressing medicine.</li>
                        <li>You cannot keep medications down or missed an infusion, injection, or refill.</li>
                        <li>Weight loss, poor intake, or dehydration symptoms that are not improving.</li>
                    </ul>
                </section>
                <section class="seo-landing__block">
                    <h2>Consider urgent care or emergency care now</h2>
                    <ul class="seo-landing__list">
                        <li>Severe or rapidly worsening abdominal pain.</li>
                        <li>Fainting, confusion, chest pain, trouble breathing, or signs of shock.</li>
                        <li>Inability to keep fluids down, very dark urine, dizziness, or rapid heartbeat.</li>
                        <li>Heavy rectal bleeding or black/tarry stool.</li>
                        <li>Severe vomiting, swollen abdomen, or inability to pass stool or gas.</li>
                        <li>High fever, severe weakness, or concern for infection after surgery or while immunosuppressed.</li>
                    </ul>
                </section>
                <section class="seo-landing__block">
                    <h2>What to keep ready</h2>
                    <ul class="seo-landing__list">
                        <li>GI clinic phone number and after-hours instructions.</li>
                        <li>Current medication list, allergies, recent procedures, and diagnosis summary.</li>
                        <li>Insurance card, photo ID, and preferred hospital if your team has one.</li>
                        <li>IBDPal export or symptom log if you have it, without delaying urgent care.</li>
                    </ul>
                    <p><a href="/guides/ibd-flare-emergency-supplies">Flare emergency supplies guide</a> · <a href="/blog/when-to-go-er-ibd">When to go to the ER article</a> · <a href="/flare-help">Flare help hub</a></p>
                </section>
                <section class="seo-landing__block">
                    <h2>Do not wait for a website to decide</h2>
                    <p>IBDPal cannot triage your symptoms. When you are unsure whether symptoms are urgent, it is reasonable to call your care team or seek urgent medical advice.</p>
                </section>
            </article>
        """,
    ),
    "for-clinicians.html": (
        "For Clinicians | IBD Visit Summaries & Patient Logs | IBDPal",
        "IBDPal helps IBD patients export symptom, nutrition, and trend summaries for gastroenterology visits, companion tool, not a medical device.",
        "/for-clinicians",
        """
            <article class="support-section">
                <h1>For Clinicians</h1>
                <p class="support-intro">IBDPal helps patients organize self-reported nutrition, symptoms, medications, and trends between visits.</p>
                <section class="seo-landing__block"><h2>Visit summary exports</h2>
                <p>Patients can export PDF or CSV summaries from the iOS app (Settings) to support shared decision-making. Data is patient-entered and should be interpreted in clinical context.</p></section>
                <section class="seo-landing__block"><h2>Medication &amp; appointment reminders</h2>
                <p>The app supports medication logging and notification reminders patients configure for infusions, injections, and follow-ups, reducing missed doses between portal messages.</p></section>
                <section class="seo-landing__block"><h2>Not a medical device</h2>
                <p>IBDPal does not diagnose, prescribe, or replace clinician judgment. Partner inquiries: <a href="mailto:contactus@ibdpal.org">contactus@ibdpal.org</a> · <a href="/clinical-partnerships">Partnerships</a></p></section>
            </article>
        """,
    ),
    "about.html": (
        "About IBDPal | Free IBD Patient Education | MediVue",
        "IBDPal helps people with Crohn's and ulcerative colitis through free patient education, guides, licensed Foundation resources, and a nonprofit iOS tracking app built by MediVue.",
        "/about",
        f"""
            <article class="support-section seo-landing">
                <h1>About IBDPal</h1>
                <p class="support-intro mission-block"><strong>Our mission:</strong> IBDPal helps people with Crohn's disease and ulcerative colitis understand nutrition, flares, and daily management through free patient education and a tracking app from nonprofit MediVue.</p>
                <p class="last-updated">Last updated: August 2026</p>
                <section class="seo-landing__block">
                    <h2>Who we are</h2>
                    <p><strong>IBDPal</strong> is a program of <strong>MediVue</strong>, a North Carolina 501(c)(3) nonprofit focused on IBD community education and self-management tools. We combine a free iOS app for food and symptom tracking with a growing library of articles, guides, and state support resources on ibdpal.org.</p>
                    <p>We are not a hospital, drug company, or substitute for your gastroenterologist. Everything on this site is educational. Clinical decisions belong with your care team.</p>
                    {ccf_nonaffiliation_about_en()}
                </section>
                <section class="seo-landing__block">
                    <h2>Crohn's &amp; Colitis Foundation</h2>
                    <p>Selected Foundation educational content and Marks appear on IBDPal under license. The logo is shown unmodified and linked to the Foundation website. We guide patients to Foundation programs and education, then offer IBDPal tools for tracking between visits.</p>
                    <ul class="seo-landing__list">
                        <li><a href="/crohns-colitis-foundation-resources">Foundation resources hub on IBDPal</a> (Help Center, Camp Oasis, diet, prior authorization, chapters, advocacy)</li>
                        <li>Attributed IBDPal guides: <a href="/guides/camp-oasis-kids-ibd">Camp Oasis</a>, <a href="/guides/ibd-prior-authorization-foundation">prior authorization</a>, <a href="/guides/foundation-diet-nutrition-ibd">diet and nutrition</a>, <a href="/guides/ibd-crohns-colitis-helpline">Help Center numbers</a></li>
                        <li>Foundation links in the <a href="/resources">resource library</a> and sitewide footer attribution</li>
                    </ul>
                    <p>We do not republish the Foundation's full site, and we do not claim endorsement or partnership.</p>
                    <p><a href="https://www.crohnscolitisfoundation.org/" rel="noopener noreferrer">crohnscolitisfoundation.org</a> · <a href="/blog/when-to-call-ibd-help-center">Help Center vs clinic</a></p>
                </section>
                <section class="seo-landing__block">
                    <h2>What you will find here</h2>
                    <ul class="seo-landing__list">
                        <li><a href="/blog">213 in-depth articles</a> on nutrition, treatment, wellness, autoimmune topics, associations, and daily life</li>
                        <li><a href="/guides">58 step-by-step patient guides</a></li>
                        <li><a href="/resources">335+ searchable resource library entries</a> (site pages, articles, and trusted external links)</li>
                        <li><a href="/#community">50 state support pages</a> (all 50 states + DC)</li>
                        <li><a href="/library">375+ education and sitemap pages</a> across hubs, guides, articles, and Spanish resources</li>
                        <li>Free <a href="/#app">IBDPal iOS app</a> for logging meals, symptoms, and visit prep</li>
                        <li>Homepage topic search, Tools Lab, recipe ideas, and nutrition targets</li>
                    </ul>
                </section>
                <section class="seo-landing__block">
                    <h2>The Founder</h2>
                    <p>IBDPal grew from a belief that people navigating Crohn&rsquo;s and ulcerative colitis deserve clear education and calm tools between clinic visits. The founder built IBDPal around that standard.</p>
                    <p><a href="/#about-founders">Read the Founders story</a></p>
                </section>
                <section class="seo-landing__block">
                    <h2>ImproveCareNow resources</h2>
                    <p>We highlight select co-produced resources from <a href="https://www.improvecarenow.org/" rel="noopener noreferrer">ImproveCareNow (ICN)</a> under their Creative Commons policy, with attribution and links to originals. IBDPal is not an ICN partner or listed care center.</p>
                    <p><a href="/blog/icn-accommodations-toolkit-ibd">Browse ICN resource highlights</a></p>
                </section>
                <section class="seo-landing__block">
                    <h2>Learn more</h2>
                    <p><a href="/#site-updates">Site updates</a> · <a href="/impact">Impact</a> · <a href="/contact">Contact</a> · <a href="/clinical-partnerships">Clinical partnerships</a> · <a href="/research">Trusted sources</a> · <a href="/trusted-ibd-resources">Trusted IBD resources</a></p>
                    <p>Organizational overview for funders: <a href="/executive-summary">Executive summary</a></p>
                </section>
            </article>
        """,
    ),
    "founder.html": (
        "The Founder | IBDPal",
        "Why IBDPal exists: a vision for clear IBD education, calm tracking tools, and useful next steps for the Crohn's and colitis community.",
        "/founder",
        """
            <article class="support-section seo-landing">
                <h1>The Founder</h1>
                <figure class="founder-name-mark">
                    <img src="/assets/founder-name.png" width="643" height="102" alt="" decoding="async" loading="lazy" draggable="false">
                </figure>
                <p class="support-intro mission-block">Every lasting program begins with a simple standard: make tomorrow a little clearer than today.</p>
                <section class="seo-landing__block">
                    <h2>Why IBDPal exists</h2>
                    <p>IBDPal grew from a belief that people navigating Crohn's disease and ulcerative colitis deserve education and tools that respect their time, their intelligence, and the complexity of life between clinic visits. Not flashy promises. Not jargon for its own sake. Clear guidance, calm tracking, and a place to return when the next question appears.</p>
                    <p>The founder built <strong>IBDPal</strong> around that standard. The vision is straightforward: honest, readable education that stays free; an iOS app that helps turn scattered notes into patterns a care team can discuss; and a website that keeps expanding so useful answers are never hard to find.</p>
                </section>
                <section class="seo-landing__block">
                    <h2>What the work stands for</h2>
                    <p>Progress here is measured in usefulness. A guide someone can finish in one sitting. A state page that points to real support. A visit summary that makes the next appointment feel less rushed. A nutrition note that helps someone prepare questions, not replace a clinician.</p>
                    <p>That standard shapes every choice: write with care, cite trusted sources, keep the experience calm, and improve what readers actually need. The founder's commitment is to keep showing up for the IBD community with clarity, dignity, and practical help.</p>
                </section>
                <section class="seo-landing__block">
                    <h2>Building forward</h2>
                    <p>Today that mission continues through published articles and guides, the free IBDPal app, Foundation-licensed education where we are authorized to share it, and resources that keep education accessible. The goal has not changed: leave each visitor with one more useful next step.</p>
                    <ul class="seo-landing__list">
                        <li>Write and review education that is honest and readable</li>
                        <li>Maintain the IBDPal app and website</li>
                        <li>Curate trusted external resources (AGA, CCF, ImproveCareNow, NIH)</li>
                        <li>Share ICN Creative Commons materials with proper attribution</li>
                        <li>Listen to community feedback through support channels and outreach</li>
                    </ul>
                </section>
                <section class="seo-landing__block">
                    <h2>Try IBDPal</h2>
                    <p><a href="https://apps.apple.com/app/ibdpal" class="app-store-badge" rel="noopener noreferrer">Download on the App Store</a></p>
                    <p><a href="/#about-founders">Founders on homepage</a> · <a href="/about">About IBDPal</a> · <a href="/impact">Our impact</a> · <a href="/contact">Contact us</a></p>
                </section>
            </article>
        """,
    ),
    "contact.html": (
        "Contact IBDPal | MediVue Nonprofit",
        "Contact MediVue and IBDPal: general inquiries, app support, privacy requests, and partnership questions.",
        "/contact",
        """
            <article class="support-section seo-landing">
                <h1>Contact IBDPal</h1>
                <p class="support-intro">Reach the MediVue team by email. We respond to patient, clinician, and partnership inquiries as capacity allows.</p>
                <section class="seo-landing__block">
                    <h2>Email</h2>
                    <ul class="seo-landing__list">
                        <li><strong>General:</strong> <a href="mailto:info@ibdpal.org">info@ibdpal.org</a></li>
                        <li><strong>App support:</strong> <a href="mailto:support@ibdpal.org">support@ibdpal.org</a> · <a href="/support">Support page</a></li>
                        <li><strong>Privacy:</strong> <a href="mailto:privacy@ibdpal.org">privacy@ibdpal.org</a> · <a href="/privacy">Privacy policy</a></li>
                        <li><strong>Partnerships &amp; outreach:</strong> <a href="mailto:contactus@ibdpal.org">contactus@ibdpal.org</a></li>
                    </ul>
                </section>
                <section class="seo-landing__block">
                    <h2>Organization</h2>
                    <p><strong>MediVue</strong> (501(c)(3) nonprofit) · IBDPal patient education program<br>
                    Website: <a href="https://www.ibdpal.org">ibdpal.org</a></p>
                </section>
                <section class="seo-landing__block">
                    <h2>Before you write</h2>
                    <p>IBDPal cannot provide personal medical advice by email. For urgent symptoms, contact your gastroenterologist or emergency services. For app how-to questions, see <a href="/support">App Support</a> and <a href="/faq">FAQ</a>.</p>
                </section>
            </article>
        """,
    ),
    "impact.html": (
        "IBDPal Impact | Patient Education & App Reach | MediVue",
        "IBDPal impact: 375+ free education and resource pages, 213 articles, Foundation-licensed education, App Store reach, and nonprofit mission outcomes for the IBD community.",
        "/impact",
        """
            <article class="support-section seo-landing">
                <h1>Our Impact</h1>
                <p class="support-intro">IBDPal measures impact by useful education published, app availability, and community reach, not by replacing clinical care.</p>
                <section class="seo-landing__block">
                    <h2>Education library (August 2026)</h2>
                    <ul class="seo-landing__list">
                        <li><strong>213 articles</strong> including ImproveCareNow resource highlights and autoimmune association topics</li>
                        <li><strong>58 patient guides</strong> for diet, flares, travel, clinic prep, and Foundation-attributed topics</li>
                        <li><strong>50 state support pages</strong> with chapters and helplines</li>
                        <li><strong>335+</strong> curated entries in the <a href="/resources">resource library</a>, including Crohn&rsquo;s &amp; Colitis Foundation and PubMed research links</li>
                        <li><strong>375+ total education and resource pages</strong> including hubs, FAQ, glossary, Spanish resources, the <a href="/crohns-colitis-foundation-resources">Foundation resources hub</a>, and <a href="/ibd-autoimmune-associations">autoimmune associations</a></li>
                    </ul>
                    <p><a href="/library">Browse the full content library →</a></p>
                </section>
                <section class="seo-landing__block">
                    <h2>IBDPal iOS app</h2>
                    <ul class="seo-landing__list">
                        <li>Free nutrition and symptom tracking for Crohn's and colitis</li>
                        <li>App Store search visibility: 2.0K+ impressions (organic)</li>
                        <li>Visit summary exports for gastroenterology appointments</li>
                    </ul>
                    <p><a href="https://apps.apple.com/app/ibdpal" rel="noopener noreferrer">Download on the App Store</a></p>
                </section>
                <section class="seo-landing__block">
                    <h2>Community engagement</h2>
                    <p>MediVue participates in the broader IBD learning community. We share ImproveCareNow Creative Commons resources with attribution, contribute to patient advisory pathways, and attend community events such as the ICN Community Conference Engagement Fair.</p>
                </section>
                <section class="seo-landing__block">
                    <h2>Mission</h2>
                    <p class="mission-block">Help people with IBD understand nutrition, flares, and daily management through free education and tools from MediVue.</p>
                    <p><a href="/about">About</a> · <a href="/founder">MediVue Founders</a> · <a href="/#news">IBD policy news</a> · <a href="/#site-updates">Site updates</a></p>
                </section>
            </article>
        """,
    ),
    "library.html": (
        "IBD Content Library | 375+ Free Education Pages | IBDPal",
        "Full index of IBDPal education: articles, guides, Foundation resources, autoimmune associations, state support, Spanish pages, ICN resources, and topic hubs for Crohn's and colitis.",
        "/library",
        """
            <article class="support-section seo-landing">
                <h1>Content Library</h1>
                <p class="support-intro">Every page below is free patient education from MediVue's IBDPal program. Nothing here replaces your gastroenterologist.</p>
                <section class="seo-landing__block">
                    <h2>By the numbers (August 2026)</h2>
                    <div class="library-stats-grid">
                        <div class="library-stat"><span class="library-stat__n">213</span><span class="library-stat__l">Articles</span></div>
                        <div class="library-stat"><span class="library-stat__n">58</span><span class="library-stat__l">Patient guides</span></div>
                        <div class="library-stat"><span class="library-stat__n">50</span><span class="library-stat__l">State support pages</span></div>
                        <div class="library-stat"><span class="library-stat__n">9</span><span class="library-stat__l">Spanish pages</span></div>
                        <div class="library-stat"><span class="library-stat__n">335+</span><span class="library-stat__l">Resource library entries</span></div>
                        <div class="library-stat"><span class="library-stat__n">375+</span><span class="library-stat__l">Education and resource pages</span></div>
                    </div>
                </section>
                <section class="seo-landing__block">
                    <h2>Start here</h2>
                    <ul class="seo-landing__list">
                        <li><a href="/start-here">Start here roadmap</a></li>
                        <li><a href="/what-is-ibd">What is IBD?</a></li>
                        <li><a href="/crohns-and-colitis">Crohn's and colitis guide</a></li>
                        <li><a href="/newly-diagnosed">Newly diagnosed</a></li>
                        <li><a href="/ibd-autoimmune-associations">IBD autoimmune associations</a></li>
                        <li><a href="/crohns-colitis-foundation-resources">Crohn&rsquo;s &amp; Colitis Foundation resources</a></li>
                        <li><a href="/ibd-nutrition">Nutrition hub</a></li>
                        <li><a href="/flare-help">Flare help</a></li>
                        <li><a href="/ibd-red-flags-urgent-care">Red flags and urgent care</a></li>
                        <li><a href="/visit-prep">Visit prep checklist</a></li>
                        <li><a href="/faq">FAQ</a> · <a href="/glossary">Glossary</a></li>
                    </ul>
                </section>
                <section class="seo-landing__block">
                    <h2>Articles &amp; guides</h2>
                    <ul class="seo-landing__list">
                        <li><a href="/blog">All articles</a> (nutrition, wellness, treatment basics, lifestyle)</li>
                        <li><a href="/guides">All patient guides</a> (step-by-step topics)</li>
                        <li><a href="/patient-stories">Patient stories</a></li>
                    </ul>
                </section>
                <section class="seo-landing__block">
                    <h2>ImproveCareNow highlights (CC attributed)</h2>
                    <ul class="seo-landing__list">
                        <li><a href="/blog/icn-accommodations-toolkit-ibd">School &amp; workplace accommodations</a></li>
                        <li><a href="/blog/icn-college-ibd-toolkit">College &amp; IBD handbook</a></li>
                        <li><a href="/blog/icn-caregiver-coping-resource">Caregiver coping resource</a></li>
                        <li><a href="/blog/icn-mental-health-provider-guide">Mental health provider guide</a></li>
                        <li><a href="/blog/icn-transfer-toolkit-adult-care">Transfer to adult care</a></li>
                        <li><a href="/blog/icn-ostomy-toolkit-pediatric">Ostomy toolkit</a></li>
                        <li><a href="/blog/icn-ibd-holidays-special-occasions">Holidays &amp; special occasions</a></li>
                        <li><a href="/blog/icn-self-management-handbook-ibd">Self-management handbook</a></li>
                        <li><a href="/blog/icn-health-literacy-toolkit-ibd">Health literacy toolkit</a></li>
                        <li><a href="/blog/icn-lifestyle-ibd-toolkit">Lifestyle &amp; IBD toolkit</a></li>
                    </ul>
                </section>
                <section class="seo-landing__block">
                    <h2>Support &amp; tools</h2>
                    <ul class="seo-landing__list">
                        <li><a href="/#community">Find support by state</a></li>
                        <li><a href="/resources">Searchable resource library</a></li>
                        <li><a href="/research">Trusted clinical sources</a></li>
                        <li><a href="/trusted-ibd-resources">Trusted IBD resources comparison</a></li>
                        <li><a href="/crohns-colitis-foundation-resources">Crohn's &amp; Colitis Foundation resources</a></li>
                        <li><a href="/#app">IBDPal iOS app</a></li>
                    </ul>
                </section>
            </article>
        """,
    ),
    "news.html": (
        "IBD Policy News | Advocacy & Legislation | IBDPal",
        "Federal and state IBD policy highlights: prior authorization reform, Safe Step Act, and Crohn's and Colitis Foundation advocacy.",
        "/news",
        f"""
            {IBD_NEWS_TAB_HTML}
        """,
    ),
    "site-updates.html": (
        "IBDPal Site Updates | Monthly Release Notes",
        "Month-by-month site improvements on IBDPal since September 2025 launch.",
        "/site-updates",
        f"""
            <article class="support-section seo-landing tab-page-section tab-page-section--compact">
                <header class="page-header-compact">
                    <h2 class="page-header-compact__title">Site Updates</h2>
                    <p class="page-header-compact__lead">Month-by-month changelog &middot; <a href="/#site-updates">View on homepage About tab</a></p>
                </header>
{UPDATES_MONTHLY_SECTIONS_HTML}
                <section class="seo-landing__block">
                    <h2>Stay current</h2>
                    <p><a href="/blog">All articles</a> &middot; <a href="/#news">IBD policy news</a> &middot; <a href="/contact">Contact</a></p>
                </section>
            </article>
        """,
    ),
}


def main():
    for name, spec in PAGES.items():
        active = spec[4] if len(spec) > 4 else ""
        extra = [VISIT_PREP_HOWTO] if name == "visit-prep.html" else PILLAR_EXTRA_GRAPH.get(name)
        html_out = shell(spec[0], spec[1], spec[2], spec[3], active, extra_graph=extra)
        (ROOT / name).write_text(html_out, encoding="utf-8")
        print("wrote", name)
    from generate_es_pages import main as generate_es_pages # noqa: E402

    generate_es_pages()


if __name__ == "__main__":
    main()
