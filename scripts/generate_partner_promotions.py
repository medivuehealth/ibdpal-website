#!/usr/bin/env python3
"""Generate Partners pages and patch News > Partners subtab from partner-promotions.json."""
from __future__ import annotations

import html
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "partner-promotions.json"
INDEX = ROOT / "index.html"
OUT_PARTNERS = ROOT / "partners.html"
OUT_MEDIA = ROOT / "partners" / "media-kit.html"
SITEMAP = ROOT / "sitemap.xml"
VERCEL = ROOT / "vercel.json"
LLMS = ROOT / "llms.txt"
SITE = "https://www.ibdpal.org"

sys.path.insert(0, str(ROOT / "scripts"))
from seo_head import breadcrumb_json, render_seo_head, web_page_json  # noqa: E402
from site_nav import PAGE_SCRIPTS, TAB_NAV_HTML, site_header_html  # noqa: E402

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

FOOTER = """
        <footer class="footer">
            <div class="footer-content">
                <div class="footer-links">
                    <a href="/#news" class="footer-link">News</a>
                    <a href="/partners" class="footer-link">Partners</a>
                    <a href="/partners/media-kit" class="footer-link">Media kit</a>
                    <a href="/clinical-partnerships" class="footer-link">Clinical partnerships</a>
                    <a href="/contact" class="footer-link">Contact</a>
                </div>
                <p><strong>IBDPal</strong> · MediVue nonprofit · Education only, not medical advice. Listings are not endorsements.</p>
                <p>&copy; 2026 MediVue. All rights reserved.</p>
            </div>
        </footer>
"""


def partner_cards(items: list[dict], *, compact: bool = False) -> str:
    cards: list[str] = []
    for item in items:
        topics = ", ".join(html.escape(t) for t in item.get("topics", []))
        label = html.escape(item.get("label", "Partner program"))
        org = html.escape(item.get("org", ""))
        posted = html.escape(str(item.get("posted_on", "")))
        disclaimer = html.escape(item.get("disclaimer", ""))
        cards.append(
            f'<article class="ibd-news-card partner-promo-card" id="{html.escape(item["id"])}">'
            f'<p class="ibd-news-card__tag">{label}'
            + (f" · {org}" if org else "")
            + "</p>"
            f'<h3 class="ibd-news-card__title"><a href="{html.escape(item["url"])}" rel="noopener noreferrer">'
            f'{html.escape(item["title"])}</a></h3>'
            f'<p>{html.escape(item["summary"])}</p>'
            + (f'<p class="research-source-meta"><span class="research-source-topics">{topics}</span></p>' if topics else "")
            + (f'<p class="research-source-meta"><em>{disclaimer}</em></p>' if disclaimer else "")
            + (
                f'<p class="ibd-news-card__actions"><a href="{html.escape(item["url"])}" rel="noopener noreferrer">'
                f"Visit program →</a>"
                + (f" · Listed {posted}" if posted else "")
                + "</p>"
                if not compact
                else ""
            )
            + "</article>"
        )
    return "\n".join(cards)


def partners_panel_html(data: dict) -> str:
    items = data.get("items", [])
    intro = html.escape(data.get("intro", ""))
    return f"""                <div class="news-subcontent" id="news-partners">
                    <article class="support-section seo-landing tab-page-section">
                        <h1>Partners &amp; programs</h1>
                        <p class="support-intro">{intro}</p>
                        <p class="support-intro">Propose a listing: <a href="/partners/media-kit">Partner media kit</a> · <a href="mailto:info@ibdpal.org">info@ibdpal.org</a></p>
                        <section class="seo-landing__block partner-promo-grid" id="partner-promo-grid">
<!-- partner-cards -->
{partner_cards(items)}
<!-- /partner-cards -->
                        </section>
                        <section class="seo-landing__block">
                            <h2>More</h2>
                            <p><a href="/partners">Full partners page →</a> · <a href="/#news-advocacy" data-news-subtab-link="news-advocacy">Advocacy news</a> · <a href="/clinical-partnerships">Clinical partnerships</a></p>
                        </section>
                    </article>
                </div>"""


ADVOCACY_INNER = """                    <article class="support-section seo-landing tab-page-section">
                        <h1>IBD Policy &amp; Advocacy News</h1>
                        <p class="support-intro">Federal and state IBD policy highlights with links to the <a href="https://www.crohnscolitisfoundation.org/" rel="noopener noreferrer">Crohn&rsquo;s &amp; Colitis Foundation</a>. Education only.</p>

                        <section class="seo-landing__block ibd-news-featured">
                            <h2>Under review</h2>
                            <article class="ibd-news-card">
                                <p class="ibd-news-card__tag">Federal regulation &middot; Prior authorization</p>
                                <h3 class="ibd-news-card__title">Days, not weeks: faster prior authorization decisions</h3>
                                <p>The federal <strong>CMS Interoperability and Prior Authorization Final Rule (CMS-0057-F)</strong> sets maximum turnaround times for many government-backed plans (Medicare Advantage, Medicaid managed care, CHIP, and Affordable Care Act marketplace plans). Insurers must approve or deny <strong>urgent</strong> requests within <strong>72 hours</strong> and <strong>standard</strong> requests within <strong>7 calendar days</strong>.</p>
                                <p>This is a crucial first step toward shorter waits for IBD tests and treatments. Patient advocates are urging federal officials to fully implement and expand these protections.</p>
                                <p class="ibd-news-card__actions">
                                    <a href="https://www.cms.gov/newsroom/fact-sheets/cms-interoperability-and-prior-authorization-final-rule-cms-0057-f" rel="noopener noreferrer">CMS fact sheet</a>
                                    &middot;
                                    <a href="https://www.crohnscolitisfoundation.org/your-guide-to-navigating-prior-authorization" rel="noopener noreferrer">CCF prior authorization guide</a>
                                    &middot;
                                    <a href="https://www.crohnscolitisfoundation.org/get-involved/be-an-advocate/action-center" rel="noopener noreferrer">Take action (CCF)</a>
                                </p>
                            </article>
                            <article class="ibd-news-card">
                                <p class="ibd-news-card__tag">Congress &middot; Step therapy</p>
                                <h3 class="ibd-news-card__title">Safe Step Act: reforming fail-first protocols</h3>
                                <p>The <strong>Safe Step Act</strong> (H.R. 2630 / S. 652) would create a clearer appeal process when insurers require patients to try and fail on preferred drugs before covering a provider-prescribed treatment. More than 40% of IBD patients report experiencing step therapy barriers.</p>
                                <p>At a recent U.S. House committee hearing, lawmakers highlighted how step therapy can leave patients behind. The Crohn&rsquo;s &amp; Colitis Foundation continues grassroots advocacy on Capitol Hill for commonsense reform.</p>
                                <p class="ibd-news-card__actions">
                                    <a href="https://www.crohnscolitisfoundation.org/get-involved/be-advocate/advocacy-priorities/step-therapy/federal-safe-step-act" rel="noopener noreferrer">Safe Step Act overview</a>
                                    &middot;
                                    <a href="https://action.crohnscolitisfoundation.org/a/ssa-webpage" rel="noopener noreferrer">Ask Congress to pass it</a>
                                </p>
                            </article>
                        </section>

                        <section class="seo-landing__block">
                            <h2>Recently approved &amp; in effect</h2>
                            <ul class="seo-landing__list">
                                <li><strong>Jan. 1, 2026:</strong> Faster prior authorization decision timelines under CMS-0057-F begin for impacted federal plans</li>
                                <li><strong>March 31, 2026:</strong> First public prior authorization performance metrics due from impacted payers</li>
                                <li><strong>Jan. 1, 2027:</strong> Prior authorization and interoperability FHIR APIs required in production (next implementation milestone)</li>
                            </ul>
                        </section>

                        <section class="seo-landing__block">
                            <h2>Advocacy highlights</h2>
                            <ul class="seo-landing__list">
                                <li><strong>Capitol Hill briefing:</strong> The Crohn&rsquo;s &amp; Colitis Foundation hosted a bipartisan briefing on how additional federal IBD research investment could accelerate prevention and treatment progress</li>
                                <li><strong>Step therapy in Congress:</strong> Rep. Lucy McBath cited an IBD volunteer&rsquo;s story at a House committee hearing, calling step therapy a sweeping mandate that too often leaves patients behind</li>
                                <li><strong>Prior auth pushback:</strong> After thousands of patient letters and a rally, UnitedHealthcare delayed a planned expansion of prior authorization for many endoscopy and colonoscopy procedures</li>
                            </ul>
                            <p><em>Source: Crohn&rsquo;s &amp; Colitis Foundation federal and grassroots advocacy updates.</em></p>
                        </section>

                        <section class="seo-landing__block">
                            <h2>Take action</h2>
                            <ul class="seo-landing__list">
                                <li><a href="https://www.crohnscolitisfoundation.org/get-involved/be-an-advocate/action-center" rel="noopener noreferrer">CCF Action Center</a> - contact lawmakers in two clicks</li>
                                <li><a href="https://action.crohnscolitisfoundation.org/a/ssa-webpage" rel="noopener noreferrer">Support the Safe Step Act</a></li>
                                <li><a href="https://www.crohnscolitisfoundation.org/science-and-professionals/program-materials/appeal-letters" rel="noopener noreferrer">Appeal letter templates</a> for denied biologics and treatments</li>
                                <li><a href="https://www.crohnscolitisfoundation.org/get-involved/be-an-advocate/advocacy-priorities/step-therapy/state-legislation" rel="noopener noreferrer">Step therapy state legislation</a></li>
                            </ul>
                        </section>

                        <section class="seo-landing__block">
                            <h2>More resources</h2>
                            <p><a href="/#news-partners" data-news-subtab-link="news-partners">Partners &amp; programs</a> · <a href="/#site-updates" data-about-subtab-link="site-updates">IBDPal site updates</a> · <a href="/#about">About MediVue</a> · <a href="/research">Trusted clinical sources</a> · <a href="/#community">Find support by state</a></p>
                        </section>
                    </article>"""


def news_tab_html(data: dict) -> str:
    return f"""            <!-- News Tab -->
            <div class="tab-content" id="news">
                <section class="about-tab-shell news-tab-shell">
                <div class="ibd-segmented-subtabs" id="news-subtab-bar" role="tablist" aria-label="News sections">
                    <button type="button" class="ibd-segmented-subtab active" role="tab" aria-selected="true" aria-controls="news-advocacy" id="news-subtab-advocacy" data-news-subtab="news-advocacy">Advocacy</button>
                    <button type="button" class="ibd-segmented-subtab" role="tab" aria-selected="false" aria-controls="news-partners" id="news-subtab-partners" data-news-subtab="news-partners">Partners &amp; programs</button>
                </div>
                <div class="ibd-segmented-panels">
                <div class="news-subcontent active" id="news-advocacy">
{ADVOCACY_INNER}
                </div>
<!-- news-partners-panel -->
{partners_panel_html(data)}
<!-- /news-partners-panel -->
                </div>
                </section>
            </div>
"""


def patch_index_news(data: dict) -> None:
    text = INDEX.read_text(encoding="utf-8")
    block = news_tab_html(data)
    if "<!-- News Tab -->" in text and "<!-- About Tab -->" in text:
        text = re.sub(
            r"            <!-- News Tab -->.*?            <!-- About Tab -->",
            block + "\n            <!-- About Tab -->",
            text,
            count=1,
            flags=re.S,
        )
    else:
        raise SystemExit("Could not locate News Tab markers in index.html")
    INDEX.write_text(text, encoding="utf-8")
    print(f"patched index.html News tab ({len(data.get('items', []))} partner cards)")


def wrap_page(*, title: str, description: str, path: str, body: str, crumb_name: str) -> str:
    seo = render_seo_head(
        title=title,
        description=description,
        path=path,
        keywords="IBD partners, biologic patient support, Crohn's, ulcerative colitis",
        json_ld=[
            breadcrumb_json(path, crumb_name),
            web_page_json(path, title, description),
        ],
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <meta name="theme-color" content="#FFE5DC">
{seo}{HEAD_ASSETS}</head>
<body>
    <div class="container">
{site_header_html()}
{TAB_NAV_HTML}
        <main class="main-content" id="main-content">
{body}
        </main>
{FOOTER}
    </div>
{PAGE_SCRIPTS}
</body>
</html>
"""


def write_partners_page(data: dict) -> None:
    items = data.get("items", [])
    body = f"""
            <article class="support-section seo-landing">
                <h1>Partners &amp; programs</h1>
                <p class="support-intro">{html.escape(data.get("intro", ""))}</p>
                <p class="support-intro"><a href="/partners/media-kit">Media kit for promoters</a> · <a href="mailto:info@ibdpal.org">Propose a listing</a> · <a href="/#news-partners">View in News tab</a></p>
                <section class="seo-landing__block partner-promo-grid">
{partner_cards(items)}
                </section>
            </article>
"""
    OUT_PARTNERS.write_text(
        wrap_page(
            title="Partners & Programs | IBDPal",
            description="Curated biologic manufacturer patient-support programs and IBD organization education listings. Not endorsements. Education only.",
            path="/partners",
            body=body,
            crumb_name="Partners",
        ),
        encoding="utf-8",
    )
    print("wrote partners.html")


def write_media_kit() -> None:
    OUT_MEDIA.parent.mkdir(parents=True, exist_ok=True)
    body = """
            <article class="support-section seo-landing">
                <h1>Partner media kit</h1>
                <p class="support-intro">Share this page with manufacturer patient-support, medical affairs, or IBD program teams who want a labeled listing on IBDPal.</p>

                <section class="seo-landing__block">
                    <h2>What IBDPal is</h2>
                    <ul class="seo-landing__list">
                        <li>Free nonprofit education site and iOS companion app from MediVue (501(c)(3))</li>
                        <li>Patient Library: guides, trusted sources, research publications, and articles</li>
                        <li>Topics include biologics, prior authorization, nutrition, autoimmune associations, and daily living with Crohn&rsquo;s and ulcerative colitis</li>
                        <li>Education only - not medical advice and not a prescribing tool</li>
                    </ul>
                </section>

                <section class="seo-landing__block">
                    <h2>What a Partners listing includes</h2>
                    <ul class="seo-landing__list">
                        <li>Public program title, organization name, short summary, and outbound link</li>
                        <li>Clear label such as Manufacturer education, Partner program, or Foundation</li>
                        <li>Non-endorsement disclaimer on every card</li>
                        <li>Placement on <a href="/partners">/partners</a> and under News → Partners &amp; programs</li>
                    </ul>
                </section>

                <section class="seo-landing__block">
                    <h2>Labeling rules</h2>
                    <ul class="seo-landing__list">
                        <li>We prefer patient-support and education hubs over pure advertising creatives</li>
                        <li>Listings are curated by MediVue; we may edit summaries for clarity and neutrality</li>
                        <li>A listing is <strong>not</strong> an endorsement of any product, brand, or company</li>
                        <li>Patients must still discuss treatment and coverage with their clinicians</li>
                    </ul>
                </section>

                <section class="seo-landing__block">
                    <h2>How to propose a listing</h2>
                    <p>Email <a href="mailto:info@ibdpal.org?subject=Partner%20listing%20proposal">info@ibdpal.org</a> with:</p>
                    <ul class="seo-landing__list">
                        <li>Program name and official public URL</li>
                        <li>One-paragraph patient-facing summary (education tone)</li>
                        <li>Organization legal name and contact for updates</li>
                        <li>Confirmation that materials may be summarized and linked with a non-endorsement label</li>
                    </ul>
                    <p>Phase 1 listings are free. We review proposals manually.</p>
                </section>

                <section class="seo-landing__block">
                    <h2>Also see</h2>
                    <p><a href="/partners">Current partner listings</a> · <a href="/clinical-partnerships">Clinical partnerships</a> · <a href="/contact">Contact</a></p>
                </section>
            </article>
"""
    OUT_MEDIA.write_text(
        wrap_page(
            title="Partner Media Kit | IBDPal",
            description="Propose a labeled manufacturer or IBD program listing on IBDPal. Non-endorsement education listings for patient-support hubs.",
            path="/partners/media-kit",
            body=body,
            crumb_name="Partner media kit",
        ),
        encoding="utf-8",
    )
    print("wrote partners/media-kit.html")


def patch_vercel() -> None:
    text = VERCEL.read_text(encoding="utf-8")
    inserts = []
    if '"/partners"' not in text:
        inserts.append('    {\n      "source": "/partners",\n      "destination": "/partners.html"\n    },\n')
    if '"/partners/media-kit"' not in text:
        inserts.append(
            '    {\n      "source": "/partners/media-kit",\n      "destination": "/partners/media-kit.html"\n    },\n'
        )
    if inserts:
        text = text.replace('"rewrites": [\n', '"rewrites": [\n' + "".join(inserts))
        VERCEL.write_text(text, encoding="utf-8")
        print("patched vercel.json partner rewrites")


def patch_sitemap() -> None:
    today = date.today().isoformat()
    text = SITEMAP.read_text(encoding="utf-8")
    block = (
        f"  <!-- partners-pages -->\n"
        f"  <url>\n    <loc>{SITE}/partners</loc>\n    <lastmod>{today}</lastmod>\n"
        f"    <changefreq>weekly</changefreq>\n    <priority>0.82</priority>\n  </url>\n"
        f"  <url>\n    <loc>{SITE}/partners/media-kit</loc>\n    <lastmod>{today}</lastmod>\n"
        f"    <changefreq>monthly</changefreq>\n    <priority>0.7</priority>\n  </url>"
    )
    if "<!-- partners-pages -->" in text:
        text = re.sub(
            r"  <!-- partners-pages -->.*?(?=  <!-- |\n</urlset>)",
            block + "\n",
            text,
            count=1,
            flags=re.S,
        )
    else:
        text = text.replace("</urlset>", block + "\n</urlset>")
    SITEMAP.write_text(text, encoding="utf-8")
    print("patched sitemap.xml partners URLs")


def patch_llms() -> None:
    if not LLMS.exists():
        return
    text = LLMS.read_text(encoding="utf-8")
    lines = [f"- {SITE}/partners", f"- {SITE}/partners/media-kit"]
    marker = "## Partners"
    if marker in text:
        return
    block = marker + "\n" + "\n".join(lines) + "\n\n"
    if "## Research sources" in text:
        text = text.replace("## Research sources", block + "## Research sources")
    else:
        text = text.rstrip() + "\n\n" + block
    LLMS.write_text(text, encoding="utf-8")
    print("patched llms.txt partners")


def main() -> None:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    patch_index_news(data)
    write_partners_page(data)
    write_media_kit()
    patch_vercel()
    patch_sitemap()
    patch_llms()
    print("partner promotions generation complete")


if __name__ == "__main__":
    main()
