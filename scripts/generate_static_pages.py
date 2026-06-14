#!/usr/bin/env python3
"""Generate static patient-resource HTML pages with full SEO heads."""
from __future__ import annotations
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from eeat_blocks import content_note_en, edu_disclaimer_en, hub_disclaimer_en, page_review_props  # noqa: E402
from es_mirrors import es_url_for_en_path  # noqa: E402
from seo_head import breadcrumb_json, howto_json, render_seo_head, web_page_json  # noqa: E402
from site_nav import PAGE_SCRIPTS, TAB_NAV_HTML, site_header_html  # noqa: E402
from site_footer import SITE_FOOTER_STATIC  # noqa: E402
from ui_snippets import (  # noqa: E402
    IBD_NEWS_TAB_HTML,
    RESOURCE_TOOLBAR_HTML,
    SITE_UPDATES_SUBTAB_HTML,
    UPDATES_MONTHLY_SECTIONS_HTML,
)

SITE = "https://www.ibdpal.org"
EEAT_PATHS = {"/newly-diagnosed", "/visit-prep", "/pediatric-caregivers", "/resources"}

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
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
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
            <article class="support-section">
                <h1>Pediatric IBD &amp; Caregivers</h1>
                <p class="support-intro">Children and teens with Crohn's or colitis need team-based care and family support. Start with these trusted networks.</p>
                <ul class="seo-landing__list">
                    <li><a href="https://www.improvecarenow.org/patients-parents" rel="noopener noreferrer">ImproveCareNow | Patients, Parents &amp; Families</a></li>
                    <li><a href="https://www.improvecarenow.org/care-centers" rel="noopener noreferrer">Find a pediatric IBD care center</a></li>
                    <li><a href="https://gikids.org/" rel="noopener noreferrer">GIKids</a></li>
                    <li><a href="/blog/living-with-ibd-kids">Blog: Living with IBD as a family</a></li>
                    <li><a href="/blog/workplace-school-ibd-rights">Blog: School 504 plans</a></li>
                </ul>
                <p>IBDPal can help families log meals, symptoms, and sleep, use exports for clinic visits. <a href="/visit-prep">Visit prep checklist</a></p>
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
        """
            <article class="support-section seo-landing">
                <h1>About IBDPal</h1>
                <p class="support-intro mission-block"><strong>Our mission:</strong> IBDPal helps people with Crohn's disease and ulcerative colitis understand nutrition, flares, and daily management through free patient education and a tracking app from nonprofit MediVue.</p>
                <section class="seo-landing__block">
                    <h2>Who we are</h2>
                    <p><strong>IBDPal</strong> is a program of <strong>MediVue</strong>, a North Carolina 501(c)(3) nonprofit focused on IBD community education and self-management tools. We combine a free iOS app for food and symptom tracking with a growing library of articles, guides, and state support resources on ibdpal.org.</p>
                    <p>We are not a hospital, drug company, or substitute for your gastroenterologist. Everything on this site is educational. Clinical decisions belong with your care team.</p>
                </section>
                <section class="seo-landing__block">
                    <h2>What you will find here</h2>
                    <ul class="seo-landing__list">
                        <li><a href="/blog">50+ in-depth articles</a> on nutrition, treatment basics, wellness, and daily life</li>
                        <li><a href="/guides">24 step-by-step patient guides</a> for flares, diet, travel, and more</li>
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
                        <li><strong>51+ articles</strong> including ImproveCareNow resource highlights</li>
                        <li><strong>24 patient guides</strong> for diet, flares, travel, and clinic prep</li>
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
                        <div class="library-stat"><span class="library-stat__n">51+</span><span class="library-stat__l">Articles</span></div>
                        <div class="library-stat"><span class="library-stat__n">24</span><span class="library-stat__l">Patient guides</span></div>
                        <div class="library-stat"><span class="library-stat__n">50</span><span class="library-stat__l">State support pages</span></div>
                        <div class="library-stat"><span class="library-stat__n">8</span><span class="library-stat__l">Spanish pages</span></div>
                        <div class="library-stat"><span class="library-stat__n">140+</span><span class="library-stat__l">Total education pages</span></div>
                    </div>
                </section>
                <section class="seo-landing__block">
                    <h2>Start here</h2>
                    <ul class="seo-landing__list">
                        <li><a href="/newly-diagnosed">Newly diagnosed</a></li>
                        <li><a href="/ibd-nutrition">Nutrition hub</a></li>
                        <li><a href="/flare-help">Flare help</a></li>
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
                    </ul>
                </section>
                <section class="seo-landing__block">
                    <h2>Support &amp; tools</h2>
                    <ul class="seo-landing__list">
                        <li><a href="/#community">Find support by state</a></li>
                        <li><a href="/resources">Searchable resource library</a></li>
                        <li><a href="/research">Trusted clinical sources</a></li>
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
            <article class="support-section seo-landing">
                <h1>Site Updates</h1>
                <p class="support-intro">Site improvements phased month by month since launch in September 2025. <a href="/#site-updates">View on homepage About tab</a>.</p>
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
