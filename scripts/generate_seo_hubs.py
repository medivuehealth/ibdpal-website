#!/usr/bin/env python3
"""Generate SEO hub pages: /blog index, topic hubs, /faq, /support by state."""
from __future__ import annotations

import html
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "seo-expansion.json"
COMMUNITY = ROOT / "community-data.js"
BLOGS = ROOT / "blogs"
BLOG_INDEX = ROOT / "blog"
SUPPORT = ROOT / "support"
SITEMAP = ROOT / "sitemap.xml"
VERCEL = ROOT / "vercel.json"
LLMS = ROOT / "llms.txt"
RESOURCES = ROOT / "resources-data.js"

sys.path.insert(0, str(ROOT / "scripts"))
from amp_utils import parse_blog_html  # noqa: E402
from seo_head import breadcrumb_json, render_seo_head, web_page_json  # noqa: E402
from site_nav import PAGE_SCRIPTS, TAB_NAV_HTML, site_header_html  # noqa: E402

SITE = "https://www.ibdpal.org"

FOOTER = """
        <footer class="footer">
            <div class="footer-content">
                <div class="footer-links">
                    <a href="/blog" class="footer-link">Blog</a>
                    <a href="/guides" class="footer-link">Patient Guides</a>
                    <a href="/support" class="footer-link">Support by State</a>
                    <a href="/faq" class="footer-link">FAQ</a>
                    <a href="/ibd-crohns-support" class="footer-link">IBD Support</a>
                    <a href="/privacy" class="footer-link">Privacy</a>
                </div>
                <p><strong>IBDPal</strong> · MediVue nonprofit · Education only, not medical advice.</p>
                <p>&copy; 2025 MediVue. All rights reserved.</p>
            </div>
        </footer>
"""

HEAD_ASSETS = """    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="stylesheet" href="/styles.css">
    <link rel="stylesheet" href="/site-layout-icn.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="icon" type="image/x-icon" href="/favicon.ico">
    <link rel="icon" type="image/png" href="/IBDPal_Logo.png">
    <link rel="apple-touch-icon" href="/IBDPal_Logo.png">
"""

DISCLAIMER = (
    '<p class="community-edu-disclaimer"><strong>Educational only.</strong> '
    "Not medical advice. Verify organization details before you rely on them.</p>"
)

US_STATES: dict[str, tuple[str, str]] = {
    "AL": ("Alabama", "alabama"),
    "AK": ("Alaska", "alaska"),
    "AZ": ("Arizona", "arizona"),
    "AR": ("Arkansas", "arkansas"),
    "CA": ("California", "california"),
    "CO": ("Colorado", "colorado"),
    "CT": ("Connecticut", "connecticut"),
    "DE": ("Delaware", "delaware"),
    "DC": ("District of Columbia", "district-of-columbia"),
    "FL": ("Florida", "florida"),
    "GA": ("Georgia", "georgia"),
    "HI": ("Hawaii", "hawaii"),
    "ID": ("Idaho", "idaho"),
    "IL": ("Illinois", "illinois"),
    "IN": ("Indiana", "indiana"),
    "IA": ("Iowa", "iowa"),
    "KS": ("Kansas", "kansas"),
    "KY": ("Kentucky", "kentucky"),
    "LA": ("Louisiana", "louisiana"),
    "ME": ("Maine", "maine"),
    "MD": ("Maryland", "maryland"),
    "MA": ("Massachusetts", "massachusetts"),
    "MI": ("Michigan", "michigan"),
    "MN": ("Minnesota", "minnesota"),
    "MS": ("Mississippi", "mississippi"),
    "MO": ("Missouri", "missouri"),
    "MT": ("Montana", "montana"),
    "NE": ("Nebraska", "nebraska"),
    "NV": ("Nevada", "nevada"),
    "NH": ("New Hampshire", "new-hampshire"),
    "NJ": ("New Jersey", "new-jersey"),
    "NM": ("New Mexico", "new-mexico"),
    "NY": ("New York", "new-york"),
    "NC": ("North Carolina", "north-carolina"),
    "ND": ("North Dakota", "north-dakota"),
    "OH": ("Ohio", "ohio"),
    "OK": ("Oklahoma", "oklahoma"),
    "OR": ("Oregon", "oregon"),
    "PA": ("Pennsylvania", "pennsylvania"),
    "RI": ("Rhode Island", "rhode-island"),
    "SC": ("South Carolina", "south-carolina"),
    "SD": ("South Dakota", "south-dakota"),
    "TN": ("Tennessee", "tennessee"),
    "TX": ("Texas", "texas"),
    "UT": ("Utah", "utah"),
    "VT": ("Vermont", "vermont"),
    "VA": ("Virginia", "virginia"),
    "WA": ("Washington", "washington"),
    "WV": ("West Virginia", "west-virginia"),
    "WI": ("Wisconsin", "wisconsin"),
    "WY": ("Wyoming", "wyoming"),
}


def load_chapter_hints() -> dict[str, str]:
    text = COMMUNITY.read_text(encoding="utf-8")
    block = re.search(r"stateChapterHints:\s*\{([^}]+)\}", text, re.S)
    if not block:
        return {}
    hints: dict[str, str] = {}
    for m in re.finditer(r"([A-Z]{2}):\s*'([^']*)'", block.group(1)):
        hints[m.group(1)] = m.group(2)
    return hints


def discover_blogs() -> dict[str, dict]:
    posts: dict[str, dict] = {}
    for path in sorted(BLOGS.glob("*.html")):
        parsed = parse_blog_html(path)
        if not parsed:
            continue
        text = path.read_text(encoding="utf-8")
        thumb_m = re.search(r'class="blog-header-thumb"\s+src="([^"]+)"', text)
        cat_m = re.search(r'class="blog-date">[^·]*·\s*([^<]+)</p>', text)
        posts[parsed["slug"]] = {
            **parsed,
            "thumb": thumb_m.group(1) if thumb_m else "/blogs/assets/ibdpal-tracking/ibdpal_app_tracker_1.png",
            "category": cat_m.group(1).strip() if cat_m else "Wellness",
        }
    return posts


def faq_json_ld(items: list[dict], path: str) -> dict:
    return {
        "@type": "FAQPage",
        "@id": f"{SITE}{path}#faq",
        "mainEntity": [
            {
                "@type": "Question",
                "name": item["q"],
                "acceptedAnswer": {"@type": "Answer", "text": item["a"]},
            }
            for item in items
        ],
    }


def shell(
    title: str,
    description: str,
    path: str,
    body: str,
    json_ld: dict,
    active_tab: str = "",
) -> str:
    nav = TAB_NAV_HTML
    if active_tab:
        nav = nav.replace(
            f'data-tab="{active_tab}"',
            f'data-tab="{active_tab}" class="tab-button active"',
            1,
        ).replace(
            f'class="tab-button active" data-tab="{active_tab}"',
            f'class="tab-button active" data-tab="{active_tab}"',
            1,
        )
        # fix double class if already tab-button
        nav = re.sub(
            rf'class="tab-button"\s+class="tab-button active"\s+data-tab="{active_tab}"',
            f'class="tab-button active" data-tab="{active_tab}"',
            nav,
        )
        nav = nav.replace(
            f'href="/#{active_tab}" class="tab-button"',
            f'href="/#{active_tab}" class="tab-button active"',
            1,
        )
    crumb = title.split("|")[0].strip()
    seo = render_seo_head(title=title, description=description, path=path, json_ld=json_ld)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
{seo}{HEAD_ASSETS}</head>
<body>
    <div class="app-container">
{site_header_html()}
{nav}
        <main class="main-content" id="main-content">
{body}
        </main>
{FOOTER}
    </div>
{PAGE_SCRIPTS}
</body>
</html>
"""


def link_list(items: list[tuple[str, str]]) -> str:
    return "<ul class=\"seo-landing__list\">" + "".join(
        f'<li><a href="{html.escape(url)}">{html.escape(label)}</a></li>' for url, label in items
    ) + "</ul>"


def blog_cards(posts: list[dict]) -> str:
    cards = []
    for p in posts:
        url = f"/blog/{p['slug']}"
        cards.append(
            f'                        <a href="{url}" class="blog-card">\n'
            f'                            <img src="{html.escape(p["thumb"])}" alt="" class="blog-card-thumb" width="800" height="600" decoding="async">\n'
            f'                            <span class="blog-card-meta">{html.escape(p["category"])}</span>\n'
            f'                            <h4>{html.escape(p["title"])}</h4>\n'
            f'                            <p>{html.escape(p["description"][:120])}</p>\n'
            f"                        </a>"
        )
    return "\n".join(cards)


def render_blog_index(meta: dict, posts: dict[str, dict]) -> str:
    path = "/blog"
    by_cat: dict[str, list] = {}
    for p in posts.values():
        by_cat.setdefault(p["category"], []).append(p)
    sections = ""
    for cat in sorted(by_cat.keys()):
        items = sorted(by_cat[cat], key=lambda x: x["title"])
        sections += f"""
                <section class="seo-landing__block">
                    <h2>{html.escape(cat)}</h2>
                    <div class="blog-index-grid">
{blog_cards(items)}
                    </div>
                </section>"""
    hub_links = """
                <section class="seo-landing__block">
                    <h2>Browse by topic</h2>
                    <ul class="seo-landing__list">
                        <li><a href="/ibd-nutrition">Nutrition &amp; diet</a></li>
                        <li><a href="/crohns-disease">Crohn's disease</a></li>
                        <li><a href="/ulcerative-colitis">Ulcerative colitis</a></li>
                        <li><a href="/teens-and-school">Teens &amp; school</a></li>
                        <li><a href="/flare-help">Flare help</a></li>
                        <li><a href="/guides">All patient guides</a></li>
                    </ul>
                </section>"""
    body = f"""
            <article class="support-section seo-landing" data-track-impression="blog_index_page">
                <h1>{html.escape(meta['h1'])}</h1>
                <p class="support-intro">{html.escape(meta['intro'])}</p>
{hub_links}
{sections}
                {DISCLAIMER}
            </article>"""
    ld = {
        "@context": "https://schema.org",
        "@graph": [
            breadcrumb_json(path, meta["h1"]),
            web_page_json(path, meta["h1"], meta["description"]),
            {
                "@type": "CollectionPage",
                "url": SITE + path,
                "name": meta["h1"],
                "description": meta["description"],
            },
        ],
    }
    return shell(meta["title"], meta["description"], path, body, ld, active_tab="blogs")


def render_hub(hub: dict, posts: dict[str, dict]) -> str:
    path = f"/{hub['slug']}"
    guide_links = [(g["url"], g["label"]) for g in hub.get("guides", [])]
    blog_items = [posts[s] for s in hub.get("blog_slugs", []) if s in posts]
    sections = ""
    for sec in hub.get("sections", []):
        paras = "".join(f"<p>{html.escape(p)}</p>" for p in sec.get("paragraphs", []))
        sections += f"<section class=\"seo-landing__block\"><h2>{html.escape(sec['heading'])}</h2>{paras}</section>"
    body = f"""
            <article class="support-section seo-landing" data-track-impression="hub_{hub['slug']}">
                <p class="blog-back"><a href="/blog" class="blog-back-link">← All blog posts</a> · <a href="/guides">Patient guides</a></p>
                <h1>{html.escape(hub['h1'])}</h1>
                <p class="support-intro">{html.escape(hub['intro'])}</p>
                <p class="seo-guide-keywords"><small>Topics: {html.escape(', '.join(hub.get('keywords', [])))}</small></p>
{sections}
                <section class="seo-landing__block"><h2>Patient guides</h2>{link_list(guide_links)}</section>
                <section class="seo-landing__block"><h2>Related articles</h2><div class="blog-index-grid">{blog_cards(blog_items)}</div></section>
                <p><a href="/faq" class="seo-landing__cta">Common IBD questions (FAQ) →</a></p>
                {DISCLAIMER}
            </article>"""
    ld = {
        "@context": "https://schema.org",
        "@graph": [
            breadcrumb_json(path, hub["h1"]),
            {**web_page_json(path, hub["h1"], hub["description"]), "keywords": ", ".join(hub.get("keywords", []))},
        ],
    }
    return shell(hub["title"], hub["description"], path, body, ld)


def render_faq(faq: dict) -> str:
    path = "/faq"
    items_html = ""
    for item in faq["items"]:
        items_html += f"<h3>{html.escape(item['q'])}</h3><p>{html.escape(item['a'])}</p>"
    body = f"""
            <article class="support-section seo-landing seo-landing__faq" data-track-impression="faq_page">
                <h1>{html.escape(faq['h1'])}</h1>
                <p class="support-intro">{html.escape(faq['intro'])}</p>
                <section class="seo-landing__block" id="faq">
{items_html}
                </section>
                <p><a href="/guides">Patient guides</a> · <a href="/blog">Blog</a> · <a href="/support">Support by state</a></p>
                {DISCLAIMER}
            </article>"""
    ld = {
        "@context": "https://schema.org",
        "@graph": [
            breadcrumb_json(path, faq["h1"]),
            web_page_json(path, faq["h1"], faq["description"]),
            faq_json_ld(faq["items"], path),
        ],
    }
    return shell(faq["title"], faq["description"], path, body, ld)


def render_support_index(meta: dict, states: list[tuple[str, str, str]]) -> str:
    path = "/support"
    links = "".join(
        f'<li><a href="/support/{slug}">Crohn\'s &amp; colitis support in {html.escape(name)}</a></li>'
        for _code, name, slug in sorted(states, key=lambda x: x[1])
    )
    body = f"""
            <article class="support-section seo-landing">
                <h1>{html.escape(meta['h1'])}</h1>
                <p class="support-intro">{html.escape(meta['intro'])}</p>
                <section class="seo-landing__block">
                    <h2>National helpline</h2>
                    <p>Crohn's &amp; Colitis Foundation IBD Help Center: <a href="tel:8886948872">888-694-8872</a> · <a href="https://www.crohnscolitisfoundation.org/chapters" rel="noopener noreferrer">Find a chapter</a></p>
                </section>
                <section class="seo-landing__block">
                    <h2>All states</h2>
                    <ul class="seo-landing__list seo-guide-hub-list">{links}</ul>
                </section>
                <p><a href="/#community">Interactive community map</a> · <a href="/ibd-crohns-support">IBD support guide</a></p>
                {DISCLAIMER}
            </article>"""
    ld = {"@context": "https://schema.org", "@graph": [breadcrumb_json(path, meta["h1"]), web_page_json(path, meta["h1"], meta["description"])]}
    return shell(meta["title"], meta["description"], path, body, ld, active_tab="community")


def render_state_page(code: str, name: str, slug: str, chapter: str, nc_extra: dict | None) -> str:
    path = f"/support/{slug}"
    title = f"Crohn's & Colitis Support in {name} | IBDPal"
    description = f"IBD support in {name}: Crohn's & Colitis Foundation chapter info, national helpline, pediatric resources, and local education links."
    resources_html = ""
    if code == "NC" and nc_extra:
        ccf = nc_extra.get("ccf", {})
        resources_html += f"""
                <section class="seo-landing__block">
                    <h2>{html.escape(ccf.get('name', 'Local chapter'))}</h2>
                    <p>{html.escape(ccf.get('notes', ''))}</p>
                    <p><a href="{html.escape(ccf.get('website', ''))}" rel="noopener noreferrer">Chapter website</a>
                    · Phone: <a href="tel:{html.escape(ccf.get('phone', '').replace('-', ''))}">{html.escape(ccf.get('phone', ''))}</a></p>
                </section>"""
        resources_html += "<section class=\"seo-landing__block\"><h2>North Carolina clinical &amp; community resources</h2><ul class=\"seo-landing__list\">"
        for r in nc_extra.get("resources", []):
            phone = f' · <a href="tel:{r["phone"].replace("-", "")}">{html.escape(r["phone"])}</a>' if r.get("phone") else ""
            resources_html += (
                f"<li><strong>{html.escape(r['name'])}</strong> ({html.escape(r['type'])})"
                f' · <a href="{html.escape(r["website"])}" rel="noopener noreferrer">Website</a>{phone}'
                f"<br><span>{html.escape(r.get('notes', ''))}</span></li>"
            )
        resources_html += "</ul></section>"
    else:
        resources_html = f"""
                <section class="seo-landing__block">
                    <h2>Crohn's &amp; Colitis Foundation in {html.escape(name)}</h2>
                    <p>Likely chapter area: <strong>{html.escape(chapter)}</strong>. Confirm current contacts on the Foundation site.</p>
                    <p><a href="https://www.crohnscolitisfoundation.org/chapters" rel="noopener noreferrer">Find chapters</a>
                    · <a href="https://www.crohnscolitisfoundation.org/find-a-support-group" rel="noopener noreferrer">Find support groups in {html.escape(name)}</a></p>
                </section>"""
    body = f"""
            <article class="support-section seo-landing" data-track-impression="support_{code}">
                <p class="blog-back"><a href="/support" class="blog-back-link">← All states</a> · <a href="/#community">Community map</a></p>
                <h1>Crohn's &amp; colitis support in {html.escape(name)}</h1>
                <p class="support-intro">Educational directory for patients and families in {html.escape(name)}. Not a substitute for your care team or emergency services.</p>
{resources_html}
                <section class="seo-landing__block">
                    <h2>National resources (every state)</h2>
                    <ul class="seo-landing__list">
                        <li><a href="https://www.crohnscolitisfoundation.org/live-full/live-full-ibd-help-center" rel="noopener noreferrer">IBD Help Center</a> · 888-694-8872</li>
                        <li><a href="https://www.improvecarenow.org/patients-parents" rel="noopener noreferrer">ImproveCareNow (pediatric)</a></li>
                        <li><a href="https://gikids.org/" rel="noopener noreferrer">GIKids</a></li>
                        <li><a href="/guides/ibd-support-near-me">Guide: IBD support near me</a></li>
                    </ul>
                </section>
                {DISCLAIMER}
            </article>"""
    ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@context": "https://schema.org",
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "IBDPal", "item": SITE + "/"},
                    {"@type": "ListItem", "position": 2, "name": "Support by state", "item": SITE + "/support"},
                    {"@type": "ListItem", "position": 3, "name": name, "item": SITE + path},
                ],
            },
            web_page_json(path, f"IBD support in {name}", description),
        ],
    }
    return shell(title, description, path, body, ld, active_tab="community")


def patch_blog_related(posts: dict[str, dict], hubs: list[dict]) -> None:
    slug_hubs: dict[str, list[tuple[str, str]]] = {}
    for hub in hubs:
        label = hub["h1"]
        url = f"/{hub['slug']}"
        for s in hub.get("blog_slugs", []):
            slug_hubs.setdefault(s, []).append((url, label))
    marker = '<section class="seo-related-reading"'
    for slug, post in posts.items():
        path = BLOGS / f"{slug}.html"
        text = path.read_text(encoding="utf-8")
        if marker in text:
            text = re.sub(r"\s*<section class=\"seo-related-reading\".*?</section>", "", text, flags=re.S)
        related = slug_hubs.get(slug, [])[:3]
        if not related:
            continue
        links = "".join(f'<li><a href="{html.escape(u)}">{html.escape(l)}</a></li>' for u, l in related)
        block = (
            f'\n                    <section class="seo-related-reading" aria-labelledby="related-{slug}">\n'
            f'                        <h2 id="related-{slug}">Related topics</h2>\n'
            f'                        <ul class="seo-landing__list">{links}</ul>\n'
            f"                    </section>\n"
        )
        needle = '<div class="blog-vote" data-blog-slug='
        if needle not in text:
            continue
        path.write_text(text.replace(needle, block + "                    " + needle, 1), encoding="utf-8")


def patch_vercel(paths: list[str], support_slugs: list[str]) -> None:
    text = VERCEL.read_text(encoding="utf-8")
    inserts = []
    rules = {
        "/blog": "/blog/index.html",
        "/faq": "/faq.html",
        "/support": "/support/index.html",
    }
    for hub in paths:
        if hub not in ("/blog", "/faq", "/support"):
            rules[hub] = f"{hub}.html"
    for src, dest in rules.items():
        if f'"{src}"' in text or f'"source": "{src}"' in text:
            continue
        inserts.append(f'    {{\n      "source": "{src}",\n      "destination": "{dest}"\n    }}')
    if '"/support/:state"' not in text:
        inserts.append('    {\n      "source": "/support/:state",\n      "destination": "/support/:state.html"\n    }')
    if not inserts:
        return
    block = ",\n".join(inserts) + ",\n"
    text = text.replace('"rewrites": [\n', f'"rewrites": [\n{block}')
    VERCEL.write_text(text, encoding="utf-8")


def patch_sitemap(urls: list[tuple[str, float]]) -> None:
    today = date.today().isoformat()
    text = SITEMAP.read_text(encoding="utf-8")
    if "<!-- seo-expansion -->" in text:
        text = re.sub(r"\n  <!-- seo-expansion -->.*?(?=\n  <!-- |\n</urlset>)", "", text, flags=re.DOTALL)
    entries = []
    for loc, priority in urls:
        entries.append(
            f"  <url>\n    <loc>{SITE}{loc}</loc>\n    <lastmod>{today}</lastmod>\n"
            f"    <changefreq>monthly</changefreq>\n    <priority>{priority}</priority>\n  </url>"
        )
    block = "  <!-- seo-expansion -->\n" + "\n".join(entries)
    text = text.replace("  <!-- amp-pages -->", block + "\n  <!-- amp-pages -->")
    SITEMAP.write_text(text, encoding="utf-8")


def patch_resources() -> None:
    if not RESOURCES.exists():
        return
    text = RESOURCES.read_text(encoding="utf-8")
    new_entries = [
        "  { title: 'IBD Blog (all articles)', category: 'getting-started', type: 'site', url: '/blog', tags: ['articles', 'nutrition', 'flare'] },",
        "  { title: 'IBD Nutrition Hub', category: 'nutrition', type: 'site', url: '/ibd-nutrition', tags: ['food', 'diet'] },",
        "  { title: 'Crohn\\'s Disease Hub', category: 'getting-started', type: 'site', url: '/crohns-disease', tags: ['crohn'] },",
        "  { title: 'Ulcerative Colitis Hub', category: 'getting-started', type: 'site', url: '/ulcerative-colitis', tags: ['colitis'] },",
        "  { title: 'Teens & School Hub', category: 'family', type: 'site', url: '/teens-and-school', tags: ['teen', '504'] },",
        "  { title: 'IBD Flare Help Hub', category: 'wellness', type: 'site', url: '/flare-help', tags: ['flare'] },",
        "  { title: 'IBD FAQ', category: 'getting-started', type: 'site', url: '/faq', tags: ['questions'] },",
        "  { title: 'IBD Support by State', category: 'community', type: 'site', url: '/support', tags: ['local', 'map'] },",
    ]
    for entry in new_entries:
        if entry.split("url: ")[1].split(",")[0].strip("'") in text:
            continue
        text = text.replace(
            "window.IBDPAL_RESOURCES = [\n",
            "window.IBDPAL_RESOURCES = [\n" + entry + "\n",
            1,
        )
    text = text.replace("url: '/#community'", "url: '/support'", 1)
    RESOURCES.write_text(text, encoding="utf-8")


def patch_llms(urls: list[str]) -> None:
    if not LLMS.exists():
        return
    text = LLMS.read_text(encoding="utf-8")
    marker = "## SEO hubs & directories"
    block = marker + "\n" + "\n".join(f"- {SITE}{u}" for u in urls)
    if marker in text:
        text = re.sub(r"## SEO hubs & directories.*?(?=\n## |\Z)", block + "\n", text, flags=re.DOTALL)
    else:
        text = text.rstrip() + "\n\n" + block + "\n"
    LLMS.write_text(text, encoding="utf-8")


def main() -> None:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    posts = discover_blogs()
    hints = load_chapter_hints()
    BLOG_INDEX.mkdir(parents=True, exist_ok=True)
    SUPPORT.mkdir(parents=True, exist_ok=True)

    (BLOG_INDEX / "index.html").write_text(render_blog_index(data["blog_index"], posts), encoding="utf-8")
    print("wrote blog/index.html")

    hub_paths = ["/blog"]
    for hub in data["hubs"]:
        out = ROOT / f"{hub['slug']}.html"
        out.write_text(render_hub(hub, posts), encoding="utf-8")
        hub_paths.append(f"/{hub['slug']}")
        print("wrote", out.name)

    (ROOT / "faq.html").write_text(render_faq(data["faq"]), encoding="utf-8")
    hub_paths.append("/faq")
    print("wrote faq.html")

    state_triples = []
    support_slugs = []
    for code, (name, slug) in US_STATES.items():
        chapter = hints.get(code, "See CCF chapter finder")
        nc = data.get("nc_extra") if code == "NC" else None
        (SUPPORT / f"{slug}.html").write_text(render_state_page(code, name, slug, chapter, nc), encoding="utf-8")
        state_triples.append((code, name, slug))
        support_slugs.append(slug)
    (SUPPORT / "index.html").write_text(render_support_index(data["support_index"], state_triples), encoding="utf-8")
    hub_paths.append("/support")
    print(f"wrote support/index.html + {len(state_triples)} state pages")

    patch_blog_related(posts, data["hubs"])

    sitemap_urls = [(p, 0.9 if p == "/blog" else 0.88) for p in hub_paths]
    sitemap_urls += [(f"/support/{slug}", 0.82) for slug in support_slugs]
    patch_sitemap(sitemap_urls)
    patch_vercel(hub_paths, support_slugs)
    patch_resources()
    patch_llms(hub_paths + [f"/support/{s}" for s in support_slugs[:5]])

    print("Updated sitemap, vercel.json, resources-data.js, llms.txt")


if __name__ == "__main__":
    main()
