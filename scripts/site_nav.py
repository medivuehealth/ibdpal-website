"""Shared site chrome for static HTML generators (nav + analytics scripts)."""
from __future__ import annotations
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOGO_SRC = "/IBDPal_Logo.png"
TAGLINE = "Empowering IBD Patients"

_SOCIAL_SVGS = {
    "facebook": (
        '<svg class="site-social__svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false">'
        '<path fill="currentColor" d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/>'
        "</svg>"
    ),
    "youtube": (
        '<svg class="site-social__svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false">'
        '<path fill="currentColor" d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/>'
        "</svg>"
    ),
    "instagram": (
        '<svg class="site-social__svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false">'
        '<path fill="currentColor" d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 1 0 0 12.324 6.162 6.162 0 0 0 0-12.324zM12 16a4 4 0 1 1 0-8 4 4 0 0 1 0 8zm6.406-11.845a1.44 1.44 0 1 0 0 2.881 1.44 1.44 0 0 0 0-2.881z"/>'
        "</svg>"
    ),
    "x": (
        '<svg class="site-social__svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false">'
        '<path fill="currentColor" d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>'
        "</svg>"
    ),
    "linkedin": (
        '<svg class="site-social__svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false">'
        '<path fill="currentColor" d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 0 1-2.063-2.065 2.062 2.062 0 0 1 2.063-2.065 2.062 2.062 0 0 1 2.063 2.065 2.062 2.062 0 0 1-2.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>'
        "</svg>"
    ),
}

_SOCIAL_LABELS = {
    "facebook": "Facebook",
    "youtube": "YouTube",
    "instagram": "Instagram",
    "x": "X (Twitter)",
    "linkedin": "LinkedIn",
}


def _load_social_links() -> dict[str, str]:
    path = ROOT / "social-links.json"
    if not path.is_file():
        return {k: "" for k in _SOCIAL_SVGS}
    data = json.loads(path.read_text(encoding="utf-8"))
    return {key: (data.get(key) or "").strip() for key in _SOCIAL_SVGS}


def build_social_list_html() -> str:
    links = _load_social_links()
    items: list[str] = []
    for key, svg in _SOCIAL_SVGS.items():
        label = _SOCIAL_LABELS[key]
        url = links.get(key, "")
        if url:
            items.append(
                f'<li><a href="{html.escape(url)}" class="site-social__link" '
                f'target="_blank" rel="noopener noreferrer" aria-label="{html.escape(label)}">'
                f"{svg}</a></li>"
            )
        else:
            items.append(
                f'<li><span class="site-social__link site-social__link--pending" '
                f'title="{html.escape(label)} — add URL in social-links.json" '
                f'aria-label="{html.escape(label)} (link not configured)">{svg}</span></li>'
            )
    return f'<ul class="site-social__list" aria-label="Social media">{"".join(items)}</ul>'


def site_header_html(*, tagline: str = TAGLINE, lang: str = "en") -> str:
    name = "IBDPal"
    social = build_social_list_html()
    return f"""
        <header class="header">
            <div class="header__inner">
                <div class="logo">
                    <a href="/" class="logo-brand" aria-label="{html.escape(name)} home">
                        <img src="{LOGO_SRC}" alt="" class="logo-img" width="52" height="52" decoding="async">
                    </a>
                    <div class="logo-text">
                        <p class="logo-name"><a href="/">{html.escape(name)}</a></p>
                        <p class="tagline">{html.escape(tagline)}</p>
                    </div>
                </div>
                {social}
            </div>
        </header>
"""


SITE_HEADER_HTML = site_header_html()
SITE_HEADER_STATIC_HTML = SITE_HEADER_HTML

_CANONICAL = "https://www.ibdpal.org"

_TAB_LINKS = f"""
                <a href="{_CANONICAL}/#overview" class="tab-button" data-tab="overview">Overview</a>
                <a href="{_CANONICAL}/#app" class="tab-button" data-tab="app">IBDPal App</a>
                <a href="{_CANONICAL}/#resources" class="tab-button" data-tab="resources">Resources</a>
                <a href="{_CANONICAL}/#blogs" class="tab-button" data-tab="blogs">Blogs</a>
                <a href="{_CANONICAL}/#community" class="tab-button" data-tab="community">Community</a>
                <a href="{_CANONICAL}/#contact" class="tab-button" data-tab="contact">Contact</a>
                <a href="{_CANONICAL}/#privacy" class="tab-button" data-tab="privacy">Privacy</a>
                <a href="{_CANONICAL}/#support" class="tab-button" data-tab="support">Support</a>
"""

CANONICAL_HOST_SCRIPT = '    <script src="/canonical-host.js"></script>\n'

TAB_NAV_HTML = f"""
        <nav class="tab-navigation" aria-label="Main">
            <div class="tab-container">
{_TAB_LINKS}
            </div>
        </nav>
"""

TAB_NAV_HOME_HTML = """
        <nav class="tab-navigation" aria-label="Main">
            <div class="tab-container">
                <button type="button" class="tab-button active" data-tab="overview">Overview</button>
                <button type="button" class="tab-button" data-tab="app">IBDPal App</button>
                <button type="button" class="tab-button" data-tab="resources">Resources</button>
                <button type="button" class="tab-button" data-tab="blogs">Blogs</button>
                <button type="button" class="tab-button" data-tab="community">Community</button>
                <button type="button" class="tab-button" data-tab="contact">Contact</button>
                <button type="button" class="tab-button" data-tab="privacy">Privacy</button>
                <button type="button" class="tab-button" data-tab="support">Support</button>
            </div>
        </nav>
"""

PAGE_SCRIPTS = """
    <script src="/site-global.js" defer></script>
    <script src="/analytics-config.js"></script>
    <script src="/analytics.js" defer></script>
"""
