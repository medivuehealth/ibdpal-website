#!/usr/bin/env python3
"""Generate static patient-resource HTML pages with full SEO heads."""
from __future__ import annotations
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from seo_head import breadcrumb_json, render_seo_head, web_page_json  # noqa: E402
from site_nav import PAGE_SCRIPTS, TAB_NAV_HTML, site_header_html  # noqa: E402

NAV = TAB_NAV_HTML

FOOTER = """
        <footer class="footer">
            <div class="footer-content">
                <div class="footer-links">
                    <a href="/ibd-crohns-support" class="footer-link">IBD Crohn's Support</a>
                    <a href="/resources" class="footer-link">Resource Library</a>
                    <a href="/newly-diagnosed" class="footer-link">Newly Diagnosed</a>
                    <a href="/visit-prep" class="footer-link">Visit Prep</a>
                    <a href="/privacy" class="footer-link">Privacy Policy</a>
                    <a href="/support" class="footer-link">App Support</a>
                    <a href="/es/recursos" class="footer-link">Español</a>
                </div>
                <p><strong>IBDPal</strong> — MediVue nonprofit · Education only, not medical advice.</p>
                <p>&copy; 2025 MediVue. All rights reserved.</p>
            </div>
        </footer>
"""

SCRIPTS = PAGE_SCRIPTS

HEAD_ASSETS = """    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="stylesheet" href="/styles.css">
    <link rel="stylesheet" href="/site-layout-icn.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="icon" type="image/x-icon" href="/favicon.ico">
    <link rel="icon" type="image/png" href="/IBDPal_Logo.png">
    <link rel="apple-touch-icon" href="/IBDPal_Logo.png">
"""


def shell(title: str, description: str, path: str, body: str, active_nav: str = "") -> str:
    nav = NAV
    if active_nav:
        nav = nav.replace(
            f'href="{active_nav}" class="tab-button"',
            f'href="{active_nav}" class="tab-button active"',
            1,
        )
    crumb_name = title.split("|")[0].strip()
    json_ld = {
        "@context": "https://schema.org",
        "@graph": [
            breadcrumb_json(path, crumb_name),
            web_page_json(path, crumb_name, description),
        ],
    }
    seo = render_seo_head(
        title=title,
        description=description,
        path=path,
        json_ld=json_ld,
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
        "Newly Diagnosed with IBD — First Steps | IBDPal",
        "Newly diagnosed with Crohn's or ulcerative colitis? Questions for your GI, IBDPal app basics, IBD support groups, and trusted national resources.",
        "/newly-diagnosed",
        """
            <article class="support-section seo-landing">
                <h1>Newly Diagnosed with IBD?</h1>
                <p class="support-intro">A Crohn's disease or ulcerative colitis diagnosis is a lot to absorb. This hub gathers calm next steps—not a substitute for your gastroenterologist.</p>
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
        "IBD Resource Library — Crohn's & Colitis Education | IBDPal",
        "Search 25+ IBD resources: nutrition blogs, Crohn's support, pediatric caregivers, visit prep, community map, and the free IBDPal iOS app.",
        "/resources",
        """
            <div class="resources-page" data-resource-library>
                <h1>IBD Resource Library</h1>
                <p class="support-intro">Filter trusted articles and tools. External links open in a new tab.</p>
                <div class="resource-library__toolbar">
                    <label>Category <select class="resource-library__filter" aria-label="Filter by category">
                        <option value="">All</option>
                        <option value="getting-started">Getting started</option>
                        <option value="community">Community</option>
                        <option value="nutrition">Nutrition</option>
                        <option value="wellness">Wellness</option>
                        <option value="treatment">Treatment</option>
                        <option value="family">Family</option>
                        <option value="clinical">Clinical</option>
                    </select></label>
                    <label>Search <input type="search" class="resource-library__search" placeholder="e.g. flare, school, ostomy" aria-label="Search resources"></label>
                </div>
                <div class="resource-library__grid"></div>
            </div>
            <script src="/resources-data.js"></script>
            <script src="/resource-library.js" defer></script>
        """,
        "/#resources",
    ),
    "patient-stories.html": (
        "IBD Patient Stories — Living With Crohn's & Colitis | IBDPal",
        "Real-world stories from people using IBDPal for Crohn's disease and ulcerative colitis—shared with consent for education only.",
        "/patient-stories",
        """
            <article class="support-section">
                <h1>Patient Stories</h1>
                <p class="support-intro">These vignettes are shared with permission, de-identified, and for encouragement only—not medical outcomes data.</p>
                <div class="story-card"><h2>Maya, 34 — Crohn's disease</h2>
                <p>"Tracking protein and hydration before infusion days helped me stop guessing what to tell my nurse. IBDPal logs made my appointments shorter and clearer."</p></div>
                <div class="story-card"><h2>James, 41 — ulcerative colitis</h2>
                <p>"During a flare I used the low-residue articles on the blog and my symptom log to show my GI what the week looked like. We adjusted meds faster."</p></div>
                <div class="story-card"><h2>Priya, parent of teen with IBD</h2>
                <p>"ImproveCareNow pointed us to a pediatric center; IBDPal helped our son notice sleep and stress patterns before finals week."</p></div>
                <p><em>Want to share your story?</em> Email <a href="mailto:info@ibdpal.org">info@ibdpal.org</a> with "Patient story" in the subject. We never publish without written consent.</p>
            </article>
        """,
    ),
    "clinical-partnerships.html": (
        "Clinical Partnerships — IBDPal for IBD Programs | IBDPal",
        "Partner with MediVue: IBDPal as a companion self-management tool for hospital and clinic IBD programs—visit prep, logging, and patient education.",
        "/clinical-partnerships",
        """
            <article class="support-section">
                <h1>Clinical Partnerships</h1>
                <p class="support-intro">MediVue is a North Carolina 501(c)(3) nonprofit. IBDPal is designed as a <strong>companion</strong> to—not a replacement for—clinical care.</p>
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
                    <li><a href="https://www.improvecarenow.org/patients-parents" rel="noopener noreferrer">ImproveCareNow — Patients, Parents &amp; Families</a></li>
                    <li><a href="https://www.improvecarenow.org/care-centers" rel="noopener noreferrer">Find a pediatric IBD care center</a></li>
                    <li><a href="https://gikids.org/" rel="noopener noreferrer">GIKids</a></li>
                    <li><a href="/blog/living-with-ibd-kids">Blog: Living with IBD as a family</a></li>
                    <li><a href="/blog/workplace-school-ibd-rights">Blog: School 504 plans</a></li>
                </ul>
                <p>IBDPal can help families log meals, symptoms, and sleep—use exports for clinic visits. <a href="/visit-prep">Visit prep checklist</a></p>
            </article>
        """,
    ),
    "for-clinicians.html": (
        "For Clinicians — IBD Visit Summaries & Patient Logs | IBDPal",
        "IBDPal helps IBD patients export symptom, nutrition, and trend summaries for gastroenterology visits—companion tool, not a medical device.",
        "/for-clinicians",
        """
            <article class="support-section">
                <h1>For Clinicians</h1>
                <p class="support-intro">IBDPal helps patients organize self-reported nutrition, symptoms, medications, and trends between visits.</p>
                <section class="seo-landing__block"><h2>Visit summary exports</h2>
                <p>Patients can export PDF or CSV summaries from the iOS app (Settings) to support shared decision-making. Data is patient-entered and should be interpreted in clinical context.</p></section>
                <section class="seo-landing__block"><h2>Medication &amp; appointment reminders</h2>
                <p>The app supports medication logging and notification reminders patients configure for infusions, injections, and follow-ups—reducing missed doses between portal messages.</p></section>
                <section class="seo-landing__block"><h2>Not a medical device</h2>
                <p>IBDPal does not diagnose, prescribe, or replace clinician judgment. Partner inquiries: <a href="mailto:contactus@ibdpal.org">contactus@ibdpal.org</a> · <a href="/clinical-partnerships">Partnerships</a></p></section>
            </article>
        """,
    ),
}


def es_page() -> str:
    desc = "Recursos educativos en español para enfermedad inflamatoria intestinal (EII), Crohn y colitis ulcerosa. Solo educación, no consejo médico."
    json_ld = {
        "@context": "https://schema.org",
        "@graph": [
            breadcrumb_json("/es/recursos", "Recursos en español"),
            web_page_json("/es/recursos", "Recursos IBD y Crohn", desc),
        ],
    }
    seo = render_seo_head(
        title="Recursos IBD y Crohn en Español | IBDPal",
        description=desc,
        path="/es/recursos",
        lang="es",
        hreflang_es=None,
        hreflang_en="https://ibdpal.org/",
        json_ld=json_ld,
    )
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
{seo}{HEAD_ASSETS}</head>
<body>
    <div class="container">
{site_header_html(tagline="Apoyo a pacientes con EII")}
        <nav class="tab-navigation" aria-label="Main">
            <div class="tab-container">
                <a href="/#overview" class="tab-button" data-tab="overview">Overview</a>
                <a href="/#app" class="tab-button" data-tab="app">IBDPal App</a>
                <a href="/#resources" class="tab-button" data-tab="resources">Resources</a>
                <a href="/#blogs" class="tab-button" data-tab="blogs">Blogs</a>
                <a href="/#community" class="tab-button" data-tab="community">Community</a>
                <a href="/#contact" class="tab-button" data-tab="contact">Contact</a>
                <a href="/privacy" class="tab-button">Privacy</a>
                <a href="/support" class="tab-button">Support</a>
                <a href="/" class="tab-button">English</a>
            </div>
        </nav>
        <main class="main-content" id="main-content" data-track-impression="page_main" data-track-label="Spanish resources">
            <article class="support-section">
                <h1>Recursos para EII y Crohn</h1>
                <p>IBDPal ofrece una aplicación gratuita y artículos educativos. <strong>No sustituye la atención médica.</strong></p>
                <ul class="seo-landing__list">
                    <li><a href="/ibd-crohns-support">Guía de apoyo (inglés)</a></li>
                    <li><a href="/resources">Biblioteca de recursos</a></li>
                    <li><a href="/newly-diagnosed">Recién diagnosticado (inglés)</a></li>
                    <li><a href="https://www.crohnscolitisfoundation.org/" rel="noopener noreferrer">Crohn's &amp; Colitis Foundation</a></li>
                    <li><a href="https://gikids.org/es" rel="noopener noreferrer">GIKids (español)</a></li>
                </ul>
                <p>Emergencias: llame al 911. Síntomas urgentes: contacte a su gastroenterólogo.</p>
            </article>
        </main>
        <footer class="footer"><div class="footer-content"><p>&copy; 2025 MediVue · <a href="/">ibdpal.org</a></p></div></footer>
    </div>
{PAGE_SCRIPTS}
</body>
</html>
"""


def main():
    for name, spec in PAGES.items():
        active = spec[4] if len(spec) > 4 else ""
        html_out = shell(spec[0], spec[1], spec[2], spec[3], active)
        (ROOT / name).write_text(html_out, encoding="utf-8")
        print("wrote", name)
    es_dir = ROOT / "es"
    es_dir.mkdir(exist_ok=True)
    (es_dir / "recursos.html").write_text(es_page(), encoding="utf-8")
    print("wrote es/recursos.html")


if __name__ == "__main__":
    main()
