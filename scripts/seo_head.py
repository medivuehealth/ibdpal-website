"""Shared SEO <head> fragments for ibdpal.org static pages."""
from __future__ import annotations
import html
import json

SITE = "https://ibdpal.org"
DEFAULT_OG_IMAGE = f"{SITE}/blogs/assets/ibdpal-tracking/ibdpal_app_tracker_1.png"


def render_seo_head(
    *,
    title: str,
    description: str,
    path: str,
    lang: str = "en",
    og_type: str = "website",
    og_image: str = DEFAULT_OG_IMAGE,
    robots: str = "index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1",
    hreflang_es: str | None = "https://ibdpal.org/es/recursos",
    hreflang_en: str | None = None,
    json_ld: dict | list | None = None,
    extra_head: str = "",
) -> str:
    canonical = SITE + path
    title_esc = html.escape(title)
    desc_esc = html.escape(description)
    og_title = title_esc.replace(" | IBDPal", "").replace(" | ibdpal.org", "")

    lines = [
        f'    <title>{title_esc}</title>',
        f'    <meta name="description" content="{desc_esc}">',
        f'    <meta name="robots" content="{robots}">',
        f'    <link rel="canonical" href="{canonical}">',
    ]
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
        '    <link rel="alternate" type="text/plain" title="LLM summary" href="https://ibdpal.org/llms.txt">',
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
