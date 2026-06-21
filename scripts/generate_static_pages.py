#!/usr/bin/env python3
"""Generate static patient-resource HTML pages with full SEO heads."""
from __future__ import annotations
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from eeat_blocks import content_note_en, ccf_nonaffiliation_about_en, edu_disclaimer_en, hub_disclaimer_en, page_review_props  # noqa: E402
from es_mirrors import es_url_for_en_path  # noqa: E402
from seo_head import breadcrumb_json, howto_json, render_seo_head, web_page_json, THEME_COLOR_META, VIEWPORT_META  # noqa: E402
from site_nav import PAGE_SCRIPTS, TAB_NAV_HTML, site_header_html  # noqa: E402
from site_footer import SITE_FOOTER_STATIC  # noqa: E402
from ui_snippets import (  # noqa: E402
    IBD_NEWS_TAB_HTML,
    RESOURCE_TOOLBAR_HTML,
    SITE_UPDATES_SUBTAB_HTML,
    UPDATES_MONTHLY_SECTIONS_HTML,
)

SITE = "https://www.ibdpal.org"
EEAT_PATHS = {
    "/start-here",
    "/newly-diagnosed",
    "/visit-prep",
    "/pediatric-caregivers",
    "/resources",
    "/crohns-colitis-foundation-resources",
    "/trusted-ibd-resources",
    "/ibd-red-flags-urgent-care",
}

NAV = TAB_NAV_HTML

FOOTER = SITE_FOOTER_STATIC

SCRIPTS = PAGE_SCRIPTS

HEAD_ASSETS = """    <link rel="preconnect" href="https://fonts.googleapis.com">
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
        body = content_note_en() + edu_disclaimer_en() + body + f"\n                {hub_disclaimer_en()}"
    graph = [
        breadcrumb_json(path, crumb_name),
        {**web_page_json(path, crumb_name, description), **(page_review_props() if path in EEAT_PATHS else {})},
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
                    <p><a href="/newly-diagnosed">Newly diagnosed hub</a> · <a href="/crohns-disease">Crohn's overview</a> · <a href="/ulcerative-colitis">Ulcerative colitis overview</a></p>
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
                    <p>Use national organizations and clinician-reviewed resources alongside your medical team. IBDPal is independent and links out because patients benefit from strong support networks.</p>
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
                    <ul class="visit-checklist"><li>☐ Symptom summary (pain 0–10, stools/day, blood, fever)</li>
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
        "Crohn's & Colitis Foundation Resources | IBDPal",
        "How IBD patients can use Crohn's & Colitis Foundation public resources: Help Center, chapters, education, support groups, and advocacy. IBDPal is independent.",
        "/crohns-colitis-foundation-resources",
        """
            <article class="support-section seo-landing">
                <h1>Crohn's &amp; Colitis Foundation Resources</h1>
                <p class="support-intro">The Crohn's &amp; Colitis Foundation is a major public source for IBD education, support programs, advocacy, and local chapters. IBDPal is independent and not affiliated with or endorsed by the Foundation.</p>
                <section class="seo-landing__block">
                    <h2>IBD Help Center</h2>
                    <p>The Foundation's IBD Help Center can help with education, support, and referrals to programs. It does not replace your gastroenterologist or emergency services.</p>
                    <ul class="seo-landing__list">
                        <li>Phone: <a href="tel:8886948872">888-MY-GUT-PAIN (888-694-8872)</a></li>
                        <li>Use for general education, local resources, support groups, and program referrals.</li>
                        <li>For severe symptoms, call your GI team, urgent care, or emergency services.</li>
                    </ul>
                    <p><a href="/blog/when-to-call-ibd-help-center">When to call the Help Center vs your clinic</a></p>
                </section>
                <section class="seo-landing__block">
                    <h2>Education and disease basics</h2>
                    <p>The Foundation publishes patient education on Crohn's disease, ulcerative colitis, medications, diet, tests, research, and living with IBD. Use those materials alongside guidance from your clinician.</p>
                    <p><a href="https://www.crohnscolitisfoundation.org/" rel="noopener noreferrer">Visit crohnscolitisfoundation.org</a> · <a href="/research">IBDPal trusted sources</a></p>
                </section>
                <section class="seo-landing__block">
                    <h2>Chapters, events, and support groups</h2>
                    <p>Local chapters can help families find education events, community programs, and support groups. Availability varies by region.</p>
                    <p><a href="/#community">Find support by state</a> · <a href="/guides/ibd-support-near-me">Support near me guide</a></p>
                </section>
                <section class="seo-landing__block">
                    <h2>IBDPal's role</h2>
                    <p>IBDPal curates links to reputable public resources and provides a free tracking app and education library. We do not speak for the Foundation, imply partnership, or provide medical advice.</p>
                    <p><a href="/about">About IBDPal</a> · <a href="/trusted-ibd-resources">Trusted IBD resources comparison</a></p>
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
        "IBDPal helps people with Crohn's and ulcerative colitis through free patient education, guides, and a nonprofit iOS tracking app built by MediVue.",
        "/about",
        f"""
            <article class="support-section seo-landing">
                <h1>About IBDPal</h1>
                <p class="support-intro mission-block"><strong>Our mission:</strong> IBDPal helps people with Crohn's disease and ulcerative colitis understand nutrition, flares, and daily management through free patient education and a tracking app from nonprofit MediVue.</p>
                <section class="seo-landing__block">
                    <h2>Who we are</h2>
                    <p><strong>IBDPal</strong> is a program of <strong>MediVue</strong>, a North Carolina 501(c)(3) nonprofit focused on IBD community education and self-management tools. We combine a free iOS app for food and symptom tracking with a growing library of articles, guides, and state support resources on ibdpal.org.</p>
                    <p>We are not a hospital, drug company, or substitute for your gastroenterologist. Everything on this site is educational. Clinical decisions belong with your care team.</p>
                    {ccf_nonaffiliation_about_en()}
                </section>
                <section class="seo-landing__block">
                    <h2>What you will find here</h2>
                    <ul class="seo-landing__list">
                        <li><a href="/blog">55+ in-depth articles</a> on nutrition, treatment basics, wellness, and daily life</li>
                        <li><a href="/guides">27 step-by-step patient guides</a> for flares, diet, travel, and more</li>
                        <li><a href="/#community">50 state support pages</a> with chapters and helplines</li>
                        <li><a href="/library">140+ total education pages</a> including Spanish resources and topic hubs</li>
                        <li>Free <a href="/#app">IBDPal iOS app</a> for logging meals, symptoms, and visit prep</li>
                    </ul>
                </section>
                <section class="seo-landing__block">
                    <h2>MediVue Founders</h2>
                    <p>IBDPal began after identifying a gap between clinic visits: hard-to-track meals, unpredictable symptoms, and scattered education online.</p>
                    <p>The MediVue Founders team set out to build a calm place to log food and symptoms between appointments, plus honest, readable education that does not require a medical degree to understand.</p>
                    <p><a href="/founder">Read the full founders page</a> · <a href="/#about">View on homepage</a></p>
                </section>
                <section class="seo-landing__block">
                    <h2>ImproveCareNow resources</h2>
                    <p>We highlight select co-produced resources from <a href="https://www.improvecarenow.org/" rel="noopener noreferrer">ImproveCareNow (ICN)</a> under their Creative Commons policy, with attribution and links to originals. IBDPal is not an ICN partner or listed care center.</p>
                    <p><a href="/blog/icn-accommodations-toolkit-ibd">Browse ICN resource highlights →</a></p>
                </section>
                <section class="seo-landing__block">
                    <h2>Learn more</h2>
                    <p><a href="/#site-updates">Site updates</a> · <a href="/impact">Impact</a> · <a href="/contact">Contact</a> · <a href="/clinical-partnerships">Clinical partnerships</a> · <a href="/research">Trusted sources</a></p>
                    <p>Organizational overview for funders: <a href="/executive-summary">Executive summary</a></p>
                </section>
            </article>
        """,
    ),
    "founder.html": (
        "MediVue Founders | IBD Education Nonprofit | IBDPal",
        "Meet the MediVue Founders behind IBDPal: a nonprofit building free IBD education and an iOS tracking app for Crohn's and colitis.",
        "/founder",
        """
            <article class="support-section seo-landing">
                <h1>MediVue Founders</h1>
                <p class="support-intro">IBDPal began after identifying a gap between clinic visits: hard-to-track meals, unpredictable symptoms, and scattered education online.</p>
                <section class="seo-landing__block">
                    <h2>Why we built IBDPal</h2>
                    <p>The MediVue Founders team set out to build two things: a calm place to log food and symptoms between appointments, and honest, readable education that does not require a medical degree to understand.</p>
                    <p>We built the <strong>IBDPal iOS app</strong> for daily tracking, micronutrient awareness, and visit summaries. We built <strong>ibdpal.org</strong> as a free library of articles, guides, and state support links so no one starts from zero after diagnosis.</p>
                </section>
                <section class="seo-landing__block">
                    <h2>What the team does today</h2>
                    <ul class="seo-landing__list">
                        <li>Write and review patient education articles and guides</li>
                        <li>Maintain the IBDPal app and website as a MediVue nonprofit program</li>
                        <li>Curate trusted external resources (AGA, CCF, ImproveCareNow, NIH)</li>
                        <li>Share ICN Creative Commons materials with proper attribution</li>
                        <li>Listen to community feedback through support channels and outreach</li>
                    </ul>
                </section>
                <section class="seo-landing__block">
                    <h2>Nonprofit structure</h2>
                    <p>MediVue is a 501(c)(3) nonprofit registered in North Carolina. IBDPal is a trademark of MediVue. We pursue grants and community partnerships to keep patient education free.</p>
                    <p>We are growing participation in the IBD patient community, including ImproveCareNow's Patient Advisory Council pathway, while continuing to publish resources our readers find useful.</p>
                </section>
                <section class="seo-landing__block">
                    <h2>Try IBDPal</h2>
                    <p><a href="https://apps.apple.com/app/ibdpal" class="app-store-badge" rel="noopener noreferrer">Download on the App Store</a></p>
                    <p><a href="/#about">About IBDPal</a> · <a href="/impact">Our impact</a> · <a href="/contact">Contact us</a></p>
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
        "IBDPal impact: 140+ free education pages, 50+ articles, App Store reach, and nonprofit mission outcomes for the IBD community.",
        "/impact",
        """
            <article class="support-section seo-landing">
                <h1>Our Impact</h1>
                <p class="support-intro">IBDPal measures impact by useful education published, app availability, and community reach, not by replacing clinical care.</p>
                <section class="seo-landing__block">
                    <h2>Education library (June 2026)</h2>
                    <ul class="seo-landing__list">
                        <li><strong>55+ articles</strong> including ImproveCareNow resource highlights</li>
                        <li><strong>27 patient guides</strong> for diet, flares, travel, and clinic prep</li>
                        <li><strong>50 state support pages</strong> with chapters and helplines</li>
                        <li><strong>140+ total education pages</strong> including hubs, FAQ, glossary, and Spanish resources</li>
                    </ul>
                    <p><a href="/library">Browse the full content library →</a></p>
                </section>
                <section class="seo-landing__block">
                    <h2>IBDPal iOS app</h2>
                    <ul class="seo-landing__list">
                        <li>Free nutrition and symptom tracking for Crohn's and colitis</li>
                        <li>App Store search visibility: 1.5K+ impressions (organic)</li>
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
        "IBD Content Library | 140+ Free Education Pages | IBDPal",
        "Full index of IBDPal education: articles, guides, state support, Spanish pages, ICN resources, and topic hubs for Crohn's and colitis.",
        "/library",
        """
            <article class="support-section seo-landing">
                <h1>Content Library</h1>
                <p class="support-intro">Every page below is free patient education from MediVue's IBDPal program. Nothing here replaces your gastroenterologist.</p>
                <section class="seo-landing__block">
                    <h2>By the numbers (June 2026)</h2>
                    <div class="library-stats-grid">
                        <div class="library-stat"><span class="library-stat__n">55+</span><span class="library-stat__l">Articles</span></div>
                        <div class="library-stat"><span class="library-stat__n">27</span><span class="library-stat__l">Patient guides</span></div>
                        <div class="library-stat"><span class="library-stat__n">50</span><span class="library-stat__l">State support pages</span></div>
                        <div class="library-stat"><span class="library-stat__n">8</span><span class="library-stat__l">Spanish pages</span></div>
                        <div class="library-stat"><span class="library-stat__n">140+</span><span class="library-stat__l">Total education pages</span></div>
                    </div>
                </section>
                <section class="seo-landing__block">
                    <h2>Start here</h2>
                    <ul class="seo-landing__list">
                        <li><a href="/start-here">Start here roadmap</a></li>
                        <li><a href="/newly-diagnosed">Newly diagnosed</a></li>
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
                    <h1 class="page-header-compact__title">Site Updates</h1>
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
        extra = [VISIT_PREP_HOWTO] if name == "visit-prep.html" else None
        html_out = shell(spec[0], spec[1], spec[2], spec[3], active, extra_graph=extra)
        (ROOT / name).write_text(html_out, encoding="utf-8")
        print("wrote", name)
    from generate_es_pages import main as generate_es_pages  # noqa: E402

    generate_es_pages()


if __name__ == "__main__":
    main()
