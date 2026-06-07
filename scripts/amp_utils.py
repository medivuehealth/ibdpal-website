"""AMP HTML helpers for ibdpal.org blog posts and patient guides."""
from __future__ import annotations

import html
import json
import re
from pathlib import Path

SITE = "https://www.ibdpal.org"

AMP_BOILERPLATE = """body{-webkit-animation:-amp-start 8s steps(1,end) 0s 1 normal both;-moz-animation:-amp-start 8s steps(1,end) 0s 1 normal both;-ms-animation:-amp-start 8s steps(1,end) 0s 1 normal both;animation:-amp-start 8s steps(1,end) 0s 1 normal both}@-webkit-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@-moz-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@-ms-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@-o-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}"""

AMP_CUSTOM_CSS = """
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;font-size:17px;line-height:1.65;color:#1a1a1a;background:#f5f5f7;margin:0}
.amp-header{display:flex;align-items:center;gap:.75rem;padding:.85rem 1rem;background:#fff;border-bottom:1px solid #e5e5e5}
.amp-header a{color:#9933cc;text-decoration:none;font-weight:600}
.amp-logo{height:36px;width:auto}
.amp-main{max-width:720px;margin:0 auto;padding:1rem 1rem 2rem}
.amp-back{margin:0 0 1rem}
.amp-back a{color:#9933cc;text-decoration:none}
.article{background:#fff;border-radius:12px;padding:1.25rem 1.35rem;box-shadow:0 2px 8px rgba(0,0,0,.06)}
.article h1{font-size:1.55rem;line-height:1.3;margin:0 0 .5rem;font-weight:700}
.article .meta{font-size:.9rem;color:#666;font-style:italic;margin:0 0 1.25rem;padding-bottom:1rem;border-bottom:1px solid #e8e8e8}
.article h2{font-size:1.3rem;color:#9933cc;margin:1.75rem 0 .75rem;font-weight:600}
.article h3{font-size:1.1rem;margin:1.25rem 0 .5rem;font-weight:600}
.article p{margin:0 0 1rem}
.article ul{margin:1rem 0;padding-left:1.5rem}
.article li{margin-bottom:.5rem}
.article a{color:#9933cc}
.disclaimer{font-size:.9rem;background:#f8f9fa;border-left:4px solid #9933cc;padding:.75rem 1rem;margin:1rem 0;border-radius:6px}
.blog-figure-grid{margin:1.5rem 0}
.blog-figure-grid figure{margin:0 0 1rem}
.blog-photo-credit{font-size:.85rem;color:#666}
.amp-cta{margin-top:1.5rem;padding-top:1rem;border-top:1px solid #e8e8e8}
.amp-cta a{font-weight:600}
.amp-footer{max-width:720px;margin:0 auto;padding:1.5rem 1rem 2.5rem;font-size:.8rem;color:#666;line-height:1.5}
.amp-footer a{color:#9933cc}
.amp-canonical-note{font-size:.85rem;margin-top:1.25rem;padding-top:1rem;border-top:1px solid #eee}
"""

_IMG_TAG = re.compile(
    r'<img\s+([^>]*?)\s*/?>',
    re.IGNORECASE | re.DOTALL,
)


def amp_url_for(path: str) -> str:
    return f"{SITE}{path.rstrip('/')}/amp"


def _attr(attrs: str, name: str, default: str = "") -> str:
    m = re.search(rf'{name}=["\']([^"\']*)["\']', attrs, re.I)
    return html.unescape(m.group(1)) if m else default


def imgs_to_amp(fragment: str) -> str:
    def repl(match: re.Match[str]) -> str:
        attrs = match.group(1)
        src = _attr(attrs, "src")
        alt = html.escape(_attr(attrs, "alt", ""))
        width = _attr(attrs, "width", "800") or "800"
        height = _attr(attrs, "height", "600") or "600"
        if not src:
            return ""
        return (
            f'<amp-img layout="responsive" width="{width}" height="{height}" '
            f'src="{html.escape(src)}" alt="{alt}"></amp-img>'
        )

    return _IMG_TAG.sub(repl, fragment)


def sanitize_amp_body(fragment: str) -> str:
    text = imgs_to_amp(fragment)
    text = re.sub(r'\sloading=["\'][^"\']*["\']', "", text)
    text = re.sub(r'\sdecoding=["\'][^"\']*["\']', "", text)
    text = re.sub(r'\son\w+=["\'][^"\']*["\']', "", text, flags=re.I)
    return text


def amp_shell(
    *,
    title: str,
    description: str,
    canonical_path: str,
    body_html: str,
    json_ld: dict | list,
    back_href: str,
    back_label: str,
) -> str:
    canonical = f"{SITE}{canonical_path}"
    title_esc = html.escape(title)
    desc_esc = html.escape(description)
    ld_json = json.dumps(json_ld, separators=(",", ":"), ensure_ascii=False)
    body = sanitize_amp_body(body_html)

    return f"""<!doctype html>
<html amp lang="en">
<head>
    <meta charset="utf-8">
    <script async src="https://cdn.ampproject.org/v0.js"></script>
    <title>{title_esc}</title>
    <meta name="description" content="{desc_esc}">
    <link rel="canonical" href="{canonical}">
    <meta name="viewport" content="width=device-width,minimum-scale=1,initial-scale=1">
    <style amp-boilerplate>{AMP_BOILERPLATE}</style>
    <noscript><style amp-boilerplate>body{{visibility:visible}}</style></noscript>
    <style amp-custom>{AMP_CUSTOM_CSS}</style>
    <script type="application/ld+json">{ld_json}</script>
</head>
<body>
    <header class="amp-header">
        <a href="/"><amp-img class="amp-logo" src="/IBDPal_Logo.png" width="120" height="36" alt="IBDPal" layout="fixed"></amp-img></a>
    </header>
    <main class="amp-main">
        <p class="amp-back"><a href="{html.escape(back_href)}">{html.escape(back_label)}</a></p>
        <article class="article">
{body}
            <p class="amp-canonical-note">Read the full interactive version on <a href="{canonical}">ibdpal.org</a>.</p>
        </article>
    </main>
    <footer class="amp-footer">
        <p><strong>IBDPal</strong> · MediVue nonprofit · Education only, not medical advice.</p>
        <p><a href="/privacy">Privacy</a> · <a href="/support">Support</a> · <a href="/terms">Terms</a></p>
    </footer>
</body>
</html>
"""


def parse_blog_html(path: Path) -> dict | None:
    text = path.read_text(encoding="utf-8")
    slug = path.stem
    title_m = re.search(r'<h1 class="blog-title">(.*?)</h1>', text, re.S)
    desc_m = re.search(r'<meta name="description" content="([^"]*)"', text)
    date_m = re.search(r'<p class="blog-date">(.*?)</p>', text, re.S)
    content_m = re.search(
        r'<div class="blog-content">\s*(.*?)\s*</div>\s*<div class="blog-vote"',
        text,
        re.S,
    )
    if not title_m or not content_m:
        return None
    title = html.unescape(re.sub(r"<[^>]+>", "", title_m.group(1)).strip())
    return {
        "slug": slug,
        "title": title,
        "description": html.unescape(desc_m.group(1)) if desc_m else title,
        "date_display": html.unescape(date_m.group(1).strip()) if date_m else "",
        "body_html": content_m.group(1).strip(),
        "canonical_path": f"/blog/{slug}",
    }


def render_amp_blog(post: dict) -> str:
    slug = post["slug"]
    path = f"/blog/{slug}"
    header = f"""            <h1>{html.escape(post["title"])}</h1>
            <p class="meta">{html.escape(post.get("date_display", ""))}</p>
"""
    body_html = header + post["body_html"]
    ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "IBDPal", "item": SITE + "/"},
                    {"@type": "ListItem", "position": 2, "name": "Blog", "item": SITE + "/#blogs"},
                    {"@type": "ListItem", "position": 3, "name": post["title"], "item": SITE + path},
                ],
            },
            {
                "@type": "Article",
                "headline": post["title"],
                "description": post["description"],
                "author": {"@type": "Organization", "name": "MediVue"},
                "publisher": {"@type": "Organization", "name": "MediVue", "url": SITE + "/"},
                "mainEntityOfPage": SITE + path,
                "isAccessibleForFree": True,
            },
        ],
    }
    return amp_shell(
        title=f"{post['title']} | IBDPal Blog",
        description=post["description"],
        canonical_path=path,
        body_html=body_html,
        json_ld=ld,
        back_href="/#blogs",
        back_label="← All blog posts",
    )


def render_amp_guide(page: dict) -> str:
    path = f"/guides/{page['slug']}"
    sections = ""
    for sec in page.get("sections", []):
        paras = "".join(f"<p>{html.escape(p)}</p>" for p in sec.get("paragraphs", []))
        sections += f"<h2>{html.escape(sec['heading'])}</h2>{paras}"

    tips = page.get("tips") or []
    tips_html = ""
    if tips:
        tips_html = "<h2>Practical tips</h2><ul>" + "".join(f"<li>{html.escape(t)}</li>" for t in tips) + "</ul>"

    faq = page.get("faq") or []
    faq_html = ""
    if faq:
        faq_html = "<h2>Common questions</h2>"
        for item in faq:
            faq_html += f"<h3>{html.escape(item['q'])}</h3><p>{html.escape(item['a'])}</p>"

    related = page.get("related") or []
    related_html = ""
    if related:
        related_html = "<h2>Related resources</h2><ul>"
        for r in related:
            related_html += f'<li><a href="{html.escape(r["url"])}">{html.escape(r["label"])}</a></li>'
        related_html += "</ul>"

    body_html = f"""            <h1>{html.escape(page['h1'])}</h1>
            <p>{html.escape(page['intro'])}</p>
{sections}
{tips_html}
{faq_html}
{related_html}
            <div class="amp-cta"><p><a href="/#app">Explore the free IBDPal app →</a></p></div>
            <p class="disclaimer"><strong>Educational only.</strong> Not medical advice. Work with your IBD care team.</p>"""

    graph = [
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "IBDPal", "item": SITE + "/"},
                {"@type": "ListItem", "position": 2, "name": "Patient Guides", "item": SITE + "/guides"},
                {"@type": "ListItem", "position": 3, "name": page["h1"], "item": SITE + path},
            ],
        },
        {
            "@type": "WebPage",
            "url": SITE + path,
            "name": page["h1"],
            "description": page["description"],
        },
    ]
    return amp_shell(
        title=page["title"],
        description=page["description"],
        canonical_path=path,
        body_html=body_html,
        json_ld={"@context": "https://schema.org", "@graph": graph},
        back_href="/guides",
        back_label="← All patient guides",
    )
