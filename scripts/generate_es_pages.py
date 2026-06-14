#!/usr/bin/env python3
"""Generate Spanish mirror pages under /es/ from data/es-pages.json."""
from __future__ import annotations

import html
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "es-pages.json"
SEO_DATA = ROOT / "data" / "seo-expansion.json"
ES_DIR = ROOT / "es"
BLOGS = ROOT / "blogs"
SITEMAP = ROOT / "sitemap.xml"
VERCEL = ROOT / "vercel.json"
LLMS = ROOT / "llms.txt"
SITE = "https://www.ibdpal.org"

sys.path.insert(0, str(ROOT / "scripts"))
from amp_utils import discover_blogs  # noqa: E402
from eeat_blocks import content_note_es, edu_disclaimer_es, hub_disclaimer_es  # noqa: E402
from seo_head import breadcrumb_json, render_seo_head, web_page_json  # noqa: E402
from site_nav import PAGE_SCRIPTS, site_header_html  # noqa: E402

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

ES_NAV = """
        <nav class="tab-navigation" aria-label="Principal">
            <div class="tab-container">
                <a href="/es/recursos" class="tab-button active">Recursos</a>
                <a href="/es/nutricion-eii" class="tab-button">Nutrición</a>
                <a href="/es/preguntas-frecuentes" class="tab-button">FAQ</a>
                <a href="/#app" class="tab-button">App IBDPal</a>
                <a href="/" class="tab-button">English</a>
            </div>
        </nav>
"""

ES_FOOTER = """
        <footer class="footer">
            <div class="footer-content">
                <p><strong>IBDPal</strong> · MediVue · Solo educación, no consejo médico.</p>
                <p>&copy; 2026 MediVue. <a href="/">ibdpal.org (English)</a></p>
            </div>
        </footer>
"""


def load_en_hubs() -> dict[str, dict]:
    data = json.loads(SEO_DATA.read_text(encoding="utf-8"))
    return {h["slug"]: h for h in data.get("hubs", [])}


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


def es_shell(
    *,
    title: str,
    description: str,
    path: str,
    body: str,
    json_ld: dict,
    hreflang_en: str,
    active: str = "recursos",
) -> str:
    nav = ES_NAV.replace('class="tab-button active"', 'class="tab-button"')
    if active:
        nav = nav.replace(
            f'href="/es/{active}" class="tab-button"',
            f'href="/es/{active}" class="tab-button active"',
            1,
        )
    seo = render_seo_head(
        title=title,
        description=description,
        path=path,
        lang="es",
        hreflang_es=None,
        hreflang_en=hreflang_en,
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
{nav}
        <main class="main-content" id="main-content">
{body}
        </main>
{ES_FOOTER}
    </div>
{PAGE_SCRIPTS}
</body>
</html>
"""


def link_list(items: list[dict]) -> str:
    return "<ul class=\"seo-landing__list\">" + "".join(
        f'<li><a href="{html.escape(i["url"])}">{html.escape(i["label"])}</a></li>' for i in items
    ) + "</ul>"


def render_recursos(page: dict) -> str:
    path = "/es/recursos"
    hubs = link_list(page["hub_links"])
    other = link_list(page["other_links"])
    body = f"""
            <article class="support-section seo-landing">
{content_note_es()}{edu_disclaimer_es()}
                <h1>{html.escape(page['h1'])}</h1>
                <p class="support-intro">{html.escape(page['intro'])}</p>
                <section class="seo-landing__block"><h2>Temas en español</h2>{hubs}</section>
                <section class="seo-landing__block"><h2>Más recursos</h2>{other}</section>
                <p>Emergencias: llame al 911. Síntomas urgentes: contacte a su gastroenterólogo.</p>
                {hub_disclaimer_es()}
            </article>"""
    ld = {
        "@context": "https://schema.org",
        "@graph": [
            breadcrumb_json(path, "Recursos en español"),
            web_page_json(path, page["h1"], page["description"]),
        ],
    }
    return es_shell(
        title=page["title"],
        description=page["description"],
        path=path,
        body=body,
        json_ld=ld,
        hreflang_en=SITE + "/",
        active="recursos",
    )


def render_newly_diagnosed(page: dict) -> str:
    path = "/es/recien-diagnosticado"
    sections = ""
    for sec in page.get("sections", []):
        paras = "".join(f"<p>{html.escape(p)}</p>" for p in sec.get("paragraphs", []))
        lst = ""
        if sec.get("list"):
            lst = "<ul class=\"seo-landing__list\">" + "".join(
                f"<li>{html.escape(item)}</li>" for item in sec["list"]
            ) + "</ul>"
        sections += f"<section class=\"seo-landing__block\"><h2>{html.escape(sec['heading'])}</h2>{paras}{lst}</section>"
    body = f"""
            <article class="support-section seo-landing">
{content_note_es()}{edu_disclaimer_es()}
                <h1>{html.escape(page['h1'])}</h1>
                <p class="support-intro">{html.escape(page['intro'])}</p>
{sections}
                <p><a href="/visit-prep" class="seo-landing__cta">Lista para citas médicas (inglés) →</a></p>
                {hub_disclaimer_es()}
            </article>"""
    ld = {
        "@context": "https://schema.org",
        "@graph": [
            breadcrumb_json(path, page["h1"]),
            web_page_json(path, page["h1"], page["description"]),
        ],
    }
    return es_shell(
        title=page["title"],
        description=page["description"],
        path=path,
        body=body,
        json_ld=ld,
        hreflang_en=SITE + "/newly-diagnosed",
        active="recursos",
    )


def render_hub(hub: dict, en_hub: dict, posts: dict[str, dict]) -> str:
    path = f"/es/{hub['slug']}"
    guide_links = [
        {"url": g["url"], "label": g["label"] + " (inglés)"}
        for g in en_hub.get("guides", [])
    ]
    blog_items = [posts[s] for s in en_hub.get("blog_slugs", []) if s in posts]
    sections = ""
    for sec in hub.get("sections", []):
        paras = "".join(f"<p>{html.escape(p)}</p>" for p in sec.get("paragraphs", []))
        sections += f"<section class=\"seo-landing__block\"><h2>{html.escape(sec['heading'])}</h2>{paras}</section>"
    blog_cards = ""
    for p in blog_items[:6]:
        blog_cards += (
            f'<li><a href="/blog/{html.escape(p["slug"])}">{html.escape(p["title"])}</a> (inglés)</li>'
        )
    body = f"""
            <article class="support-section seo-landing">
{content_note_es()}{edu_disclaimer_es()}
                <p class="blog-back"><a href="/es/recursos" class="blog-back-link">← Recursos en español</a></p>
                <h1>{html.escape(hub['h1'])}</h1>
                <p class="support-intro">{html.escape(hub['intro'])}</p>
                <p class="seo-guide-keywords"><small>Temas: {html.escape(', '.join(hub.get('keywords', [])))}</small></p>
{sections}
                <section class="seo-landing__block"><h2>Guías para pacientes</h2>{link_list(guide_links)}</section>
                <section class="seo-landing__block"><h2>Artículos relacionados</h2><ul class="seo-landing__list">{blog_cards}</ul></section>
                <p><a href="/es/preguntas-frecuentes" class="seo-landing__cta">Preguntas frecuentes →</a></p>
                {hub_disclaimer_es()}
            </article>"""
    en_path = f"/{hub['en_slug']}"
    ld = {
        "@context": "https://schema.org",
        "@graph": [
            breadcrumb_json(path, hub["h1"]),
            {**web_page_json(path, hub["h1"], hub["description"]), "keywords": ", ".join(hub.get("keywords", []))},
        ],
    }
    return es_shell(
        title=hub["title"],
        description=hub["description"],
        path=path,
        body=body,
        json_ld=ld,
        hreflang_en=SITE + en_path,
        active=hub["slug"],
    )


def render_faq(faq: dict) -> str:
    path = f"/es/{faq['slug']}"
    items_html = ""
    for item in faq["items"]:
        items_html += f"<h3>{html.escape(item['q'])}</h3><p>{html.escape(item['a'])}</p>"
    body = f"""
            <article class="support-section seo-landing seo-landing__faq">
{content_note_es()}{edu_disclaimer_es()}
                <h1>{html.escape(faq['h1'])}</h1>
                <p class="support-intro">{html.escape(faq['intro'])}</p>
                <section class="seo-landing__block" id="faq">
{items_html}
                </section>
                <p><a href="/guides">Guías (inglés)</a> · <a href="/blog">Blog (inglés)</a> · <a href="/es/recursos">Recursos en español</a></p>
                {hub_disclaimer_es()}
            </article>"""
    ld = {
        "@context": "https://schema.org",
        "@graph": [
            breadcrumb_json(path, faq["h1"]),
            web_page_json(path, faq["h1"], faq["description"]),
            faq_json_ld(faq["items"], path),
        ],
    }
    return es_shell(
        title=faq["title"],
        description=faq["description"],
        path=path,
        body=body,
        json_ld=ld,
        hreflang_en=SITE + "/faq",
        active="preguntas-frecuentes",
    )


def patch_vercel(slugs: list[str]) -> None:
    text = VERCEL.read_text(encoding="utf-8")
    inserts = []
    for slug in slugs:
        src = f"/es/{slug}"
        if f'"source": "{src}"' in text:
            continue
        inserts.append(
            f'    {{\n      "source": "{src}",\n      "destination": "/es/{slug}.html"\n    }}'
        )
    if not inserts:
        return
    block = ",\n".join(inserts) + ",\n"
    text = text.replace('"rewrites": [\n', f'"rewrites": [\n{block}')
    VERCEL.write_text(text, encoding="utf-8")


def patch_sitemap(paths: list[str]) -> None:
    today = date.today().isoformat()
    text = SITEMAP.read_text(encoding="utf-8")
    if "<!-- es-pages -->" in text:
        text = re.sub(r"\n  <!-- es-pages -->.*?(?=\n  <!-- |\n</urlset>)", "", text, flags=re.DOTALL)
    entries = []
    for loc in paths:
        entries.append(
            f"  <url>\n    <loc>{SITE}{loc}</loc>\n    <lastmod>{today}</lastmod>\n"
            f"    <changefreq>monthly</changefreq>\n    <priority>0.86</priority>\n  </url>"
        )
    block = "  <!-- es-pages -->\n" + "\n".join(entries)
    anchor = "  <!-- amp-pages -->"
    if anchor in text:
        text = text.replace(anchor, block + "\n" + anchor)
    else:
        text = text.replace("</urlset>", block + "\n</urlset>")
    SITEMAP.write_text(text, encoding="utf-8")


def patch_llms(paths: list[str]) -> None:
    if not LLMS.exists():
        return
    text = LLMS.read_text(encoding="utf-8")
    marker = "## Spanish (español)"
    block = marker + "\n" + "\n".join(f"- {SITE}{p}" for p in sorted(paths))
    if marker in text:
        text = re.sub(r"## Spanish \(español\).*?(?=\n## |\Z)", block + "\n", text, flags=re.DOTALL)
    else:
        org = "## Organization"
        if org in text:
            text = text.replace(org, block + "\n\n" + org)
        else:
            text = text.rstrip() + "\n\n" + block + "\n"
    LLMS.write_text(text, encoding="utf-8")


def main() -> None:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    en_hubs = load_en_hubs()
    posts = discover_blogs(BLOGS)
    ES_DIR.mkdir(parents=True, exist_ok=True)

    es_paths: list[str] = []

    (ES_DIR / "recursos.html").write_text(render_recursos(data["recursos"]), encoding="utf-8")
    es_paths.append("/es/recursos")
    print("wrote es/recursos.html")

    (ES_DIR / "recien-diagnosticado.html").write_text(
        render_newly_diagnosed(data["newly_diagnosed"]), encoding="utf-8"
    )
    es_paths.append("/es/recien-diagnosticado")
    print("wrote es/recien-diagnosticado.html")

    slugs = ["recursos", "recien-diagnosticado"]
    for hub in data["hubs"]:
        en_hub = en_hubs.get(hub["en_slug"], {})
        out = ES_DIR / f"{hub['slug']}.html"
        out.write_text(render_hub(hub, en_hub, posts), encoding="utf-8")
        es_paths.append(f"/es/{hub['slug']}")
        slugs.append(hub["slug"])
        print("wrote", out.name)

    faq = data["faq"]
    (ES_DIR / f"{faq['slug']}.html").write_text(render_faq(faq), encoding="utf-8")
    es_paths.append(f"/es/{faq['slug']}")
    slugs.append(faq["slug"])
    print("wrote es/" + faq["slug"] + ".html")

    patch_vercel(slugs)
    patch_sitemap(es_paths)
    patch_llms(es_paths)
    print(f"Updated vercel.json, sitemap.xml, llms.txt ({len(es_paths)} Spanish URLs)")


if __name__ == "__main__":
    main()
