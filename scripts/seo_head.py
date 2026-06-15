"""Shared SEO <head> fragments for ibdpal.org static pages."""
from __future__ import annotations
import html
import json

SITE = "https://www.ibdpal.org"
SITEMAP_URL = f"{SITE}/sitemap.xml"
DEFAULT_OG_IMAGE = f"{SITE}/blogs/assets/ibdpal-tracking/ibdpal_app_tracker_1.png"
CANONICAL_HOST_SCRIPT = '    <script src="/canonical-host.js"></script>\n'
VIEWPORT_META = (
    '    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">'
)
THEME_COLOR_META = '    <meta name="theme-color" content="#FFE5DC">'

from seo_keywords import keywords_for_path


def render_seo_head(
    *,
    title: str,
    description: str,
    path: str,
    lang: str = "en",
    og_type: str = "website",
    og_image: str = DEFAULT_OG_IMAGE,
    robots: str = "index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1",
    hreflang_es: str | None = "https://www.ibdpal.org/es/recursos",
    hreflang_en: str | None = None,
    json_ld: dict | list | None = None,
    extra_head: str = "",
    amphtml_path: str | None = None,
    keywords: str | None = None,
    include_sitemap_link: bool = True,
) -> str:
    canonical = SITE + path
    title_esc = html.escape(title)
    desc_esc = html.escape(description)
    kw = keywords or keywords_for_path(path)
    kw_esc = html.escape(kw)
    og_title = title_esc.replace(" | IBDPal", "").replace(" | ibdpal.org", "")

    lines = [
        CANONICAL_HOST_SCRIPT.rstrip(),
        f'    <title>{title_esc}</title>',
        f'    <meta name="description" content="{desc_esc}">',
        f'    <meta name="keywords" content="{kw_esc}">',
        f'    <meta name="robots" content="{robots}">',
        f'    <meta name="author" content="MediVue">',
        f'    <link rel="canonical" href="{canonical}">',
    ]
    if include_sitemap_link:
        lines.append(f'    <link rel="sitemap" type="application/xml" title="Sitemap" href="{SITEMAP_URL}">')
    if amphtml_path:
        lines.append(f'    <link rel="amphtml" href="{SITE}{amphtml_path}/amp">')
    if lang == "en" and hreflang_es:
        lines.append(f'    <link rel="alternate" hreflang="es" href="{hreflang_es}">')
        lines.append(f'    <link rel="alternate" hreflang="en" href="{canonical}">')
    if lang == "es" and hreflang_en:
        lines.append(f'    <link rel="alternate" hreflang="en" href="{hreflang_en}">')
        lines.append(f'    <link rel="alternate" hreflang="es" href="{canonical}">')
    lines.extend([
        f'    <meta property="og:type" content="{og_type}">',
        f'    <meta property="og:url" content="{canonical}">',
        f'    <meta property="og:title" content="{og_title}">',
        f'    <meta property="og:description" content="{desc_esc}">',
        '    <meta property="og:site_name" content="IBDPal">',
        f'    <meta property="og:locale" content="{"en_US" if lang == "en" else "es_US"}">',
        f'    <meta property="og:image" content="{og_image}">',
        '    <meta name="twitter:card" content="summary_large_image">',
        f'    <meta name="twitter:title" content="{og_title}">',
        f'    <meta name="twitter:description" content="{desc_esc}">',
        '    <link rel="alternate" type="text/plain" title="LLM summary" href="https://www.ibdpal.org/llms.txt">',
    ])
    if json_ld is not None:
        payload = json.dumps(json_ld, separators=(",", ":"), ensure_ascii=False)
        lines.append(f'    <script type="application/ld+json">{payload}</script>')
    if extra_head:
        lines.append(extra_head.rstrip())
    return "\n".join(lines) + "\n"


def breadcrumb_json(path: str, name: str) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "IBDPal", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": name, "item": SITE + path},
        ],
    }


def howto_json(
    *,
    name: str,
    description: str,
    path: str,
    steps: list[dict[str, str]],
) -> dict:
    return {
        "@type": "HowTo",
        "@id": f"{SITE}{path}#howto",
        "name": name,
        "description": description,
        "inLanguage": "en-US",
        "step": [
            {
                "@type": "HowToStep",
                "position": i + 1,
                "name": step["name"],
                "text": step["text"],
            }
            for i, step in enumerate(steps)
        ],
    }


def web_page_json(path: str, title: str, description: str) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "url": SITE + path,
        "name": title,
        "description": description,
        "isPartOf": {"@type": "WebSite", "name": "IBDPal", "url": SITE + "/"},
        "publisher": {"@type": "Organization", "name": "MediVue", "url": SITE + "/"},
    }
