#!/usr/bin/env python3
# Prose style: do not use em dash.
"""Generate /tools/bristol-flare-checker interactive SEO page + vercel/sitemap wiring."""
from __future__ import annotations

import json
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "tools" / "bristol-flare-checker.html"
VERCEL = ROOT / "vercel.json"
SITEMAP = ROOT / "sitemap.xml"
SITE = "https://www.ibdpal.org"

sys_path = str(ROOT / "scripts")
import sys

sys.path.insert(0, sys_path)
from site_nav import PAGE_SCRIPTS, TAB_NAV_HTML, site_header_html  # noqa: E402
from site_footer import SITE_FOOTER_STATIC  # noqa: E402
from seo_head import breadcrumb_json, organization_json, website_json  # noqa: E402

BRISTOL = [
    (1, "Separate hard lumps", "Often constipation range"),
    (2, "Lumpy sausage", "Often constipation range"),
    (3, "Sausage with cracks", "Toward formed"),
    (4, "Smooth soft sausage", "Common quiet-goal form for many people"),
    (5, "Soft blobs with clear edges", "Looser"),
    (6, "Fluffy mushy pieces", "Diarrhea range; common in flares"),
    (7, "Entirely liquid", "Diarrhea range; hydrate and call if severe"),
]


def page_html() -> str:
    buttons = "".join(
        f'<button type="button" class="bristol-pick" data-type="{n}" aria-pressed="false">'
        f'<span class="bristol-pick__n">{n}</span>'
        f'<span class="bristol-pick__label">{label}</span>'
        f'<span class="bristol-pick__hint">{hint}</span></button>'
        for n, label, hint in BRISTOL
    )
    ld = {
        "@context": "https://schema.org",
        "@graph": [
            organization_json(),
            website_json(),
            breadcrumb_json("/tools/bristol-flare-checker", "Bristol and flare checker"),
            {
                "@type": "WebApplication",
                "name": "Bristol stool and flare checker",
                "url": f"{SITE}/tools/bristol-flare-checker",
                "applicationCategory": "HealthApplication",
                "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
                "description": "Educational Bristol stool scale selector and flare symptom checklist for IBD patients.",
            },
        ],
    }
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <meta name="theme-color" content="#FFE5DC">
    <title>Bristol Stool Chart &amp; Flare Checker | IBDPal Tools</title>
    <meta name="description" content="Interactive Bristol stool chart and flare symptom checklist for Crohn's and colitis. Education only. Not a diagnosis tool.">
    <meta name="keywords" content="Bristol stool chart, Bristol scale IBD, flare checker, stool type Crohn's, colitis diarrhea scale">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="{SITE}/tools/bristol-flare-checker">
    <link rel="stylesheet" href="/styles.css">
    <link rel="stylesheet" href="/site-layout-icn.css">
    <link rel="stylesheet" href="/site-polish.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet">
    <link rel="icon" type="image/png" href="/IBDPal_Logo.png">
    <meta property="og:title" content="Bristol Stool Chart &amp; Flare Checker | IBDPal">
    <meta property="og:description" content="Practice describing stool form and flare clues before your GI visit. Education only.">
    <meta property="og:url" content="{SITE}/tools/bristol-flare-checker">
    <meta property="og:type" content="website">
    <script type="application/ld+json">{json.dumps(ld, separators=(",", ":"))}</script>
    <style>
      .bristol-tool {{ max-width: 880px; margin: 0 auto; padding: 1.25rem 1rem 3rem; }}
      .bristol-grid {{ display: grid; gap: .75rem; grid-template-columns: 1fr; }}
      @media (min-width: 640px) {{ .bristol-grid {{ grid-template-columns: 1fr 1fr; }} }}
      .bristol-pick {{ text-align: left; border: 1px solid #e7d2c8; background: #fffaf7; border-radius: 12px; padding: .85rem 1rem; cursor: pointer; }}
      .bristol-pick[aria-pressed="true"] {{ border-color: #c45c3e; background: #ffe8e0; box-shadow: 0 0 0 2px rgba(196,92,62,.15); }}
      .bristol-pick__n {{ display: inline-block; font-weight: 800; font-family: "Plus Jakarta Sans", sans-serif; margin-right: .5rem; color: #c45c3e; }}
      .bristol-pick__label {{ font-weight: 600; }}
      .bristol-pick__hint {{ display: block; margin-top: .25rem; color: #6b5b55; font-size: .92rem; }}
      .bristol-flags {{ display: grid; gap: .5rem; margin: 1rem 0; }}
      .bristol-flags label {{ display: flex; gap: .6rem; align-items: flex-start; background: #fff; border: 1px solid #eee; border-radius: 10px; padding: .65rem .8rem; }}
      .bristol-result {{ margin-top: 1.25rem; padding: 1rem 1.1rem; border-radius: 12px; background: #f4f7fb; border: 1px solid #d7e3f0; }}
      .bristol-result--urgent {{ background: #fff1f0; border-color: #f0b4ae; }}
      .bristol-links {{ display: flex; flex-wrap: wrap; gap: .6rem; margin-top: .85rem; }}
      .bristol-links a {{ display: inline-block; padding: .45rem .75rem; border-radius: 999px; background: #fff; border: 1px solid #e7d2c8; text-decoration: none; color: #3b2f2a; font-size: .92rem; }}
    </style>
</head>
<body>
<div class="app-container">
{site_header_html()}
{TAB_NAV_HTML}
<main class="main-content">
  <article class="bristol-tool support-section" data-bristol-flare-tool>
    <p class="blog-back"><a href="/#tools-lab" class="blog-back-link">&larr; Tools Lab</a> · <a href="/stool-labs-decoder">Stool &amp; labs decoder</a></p>
    <h1>Bristol stool chart &amp; flare checker</h1>
    <p class="support-intro">Pick the Bristol type that best matches today, then check any warning symptoms. This tool helps you describe patterns for your care team. It does not diagnose Crohn's disease, ulcerative colitis, infection, or obstruction.</p>
    <div class="tools-lab-guardrail" role="note"><strong>Education only.</strong> If you have heavy bleeding, black tarry stools, fainting, high fever on immunosuppression, or vomiting with severe bloating, seek urgent care now.</div>

    <h2>1. Bristol stool type</h2>
    <div class="bristol-grid" role="group" aria-label="Bristol stool types">{buttons}</div>

    <h2>2. Extra clues (optional)</h2>
    <div class="bristol-flags">
      <label><input type="checkbox" data-flag="blood"> Visible blood in stool</label>
      <label><input type="checkbox" data-flag="black"> Black or tarry stool</label>
      <label><input type="checkbox" data-flag="night"> Nighttime stools waking you</label>
      <label><input type="checkbox" data-flag="fever"> Fever</label>
      <label><input type="checkbox" data-flag="vomit"> Vomiting or cannot keep fluids down</label>
      <label><input type="checkbox" data-flag="faint"> Dizziness or fainting</label>
      <label><input type="checkbox" data-flag="obstruct"> Severe bloating with little or no gas or stool</label>
    </div>

    <div class="bristol-result" data-bristol-result aria-live="polite">
      <p><strong>Select a Bristol type</strong> to see suggested wording and reading links.</p>
    </div>

    <h2>Learn more</h2>
    <div class="bristol-links">
      <a href="/blog/bristol-stool-chart-ibd">Bristol chart article</a>
      <a href="/stool-labs-decoder">Stool &amp; labs decoder hub</a>
      <a href="/blog/high-calprotectin-what-next">High calprotectin</a>
      <a href="/blog/blood-in-stool-ibd-when-to-worry">Blood in stool</a>
      <a href="/flare-help">Flare help</a>
      <a href="/#download">IBDPal app</a>
    </div>
  </article>
</main>
{SITE_FOOTER_STATIC}
</div>
{PAGE_SCRIPTS}
<script>
(function () {{
  var root = document.querySelector('[data-bristol-flare-tool]');
  if (!root) return;
  var result = root.querySelector('[data-bristol-result]');
  var selected = null;
  var copy = {{
    1: 'Type 1 (hard lumps) often sits in the constipation range. Note pain, straining, and whether opioids or dehydration play a role.',
    2: 'Type 2 (lumpy) often sits in the constipation range. Track fluids and ask before adding bulky fiber if you have strictures.',
    3: 'Type 3 is formed with cracks. Many people are moving toward a quieter pattern here.',
    4: 'Type 4 (smooth sausage) is a common quiet-goal form, but remission is more than stool shape alone.',
    5: 'Type 5 is softer. Note urgency, meals, and whether this is new for you.',
    6: 'Type 6 (mushy) is diarrhea-range and common in flares or infections. Prioritize hydration and clinic contact if it persists.',
    7: 'Type 7 (liquid) is diarrhea-range. Use oral rehydration guidance from your team and call for red-flag symptoms.'
  }};
  function flags() {{
    return Array.prototype.slice.call(root.querySelectorAll('[data-flag]:checked')).map(function (el) {{ return el.getAttribute('data-flag'); }});
  }}
  function render() {{
    if (!selected) {{
      result.className = 'bristol-result';
      result.innerHTML = '<p><strong>Select a Bristol type</strong> to see suggested wording and reading links.</p>';
      return;
    }}
    var f = flags();
    var urgent = f.indexOf('black') >= 0 || f.indexOf('faint') >= 0 || f.indexOf('obstruct') >= 0 || (f.indexOf('blood') >= 0 && f.indexOf('fever') >= 0) || f.indexOf('vomit') >= 0;
    result.className = 'bristol-result' + (urgent ? ' bristol-result--urgent' : '');
    var lines = [];
    lines.push('<p><strong>Suggested visit note:</strong> Bristol type ' + selected + '. ' + copy[selected] + '</p>');
    if (f.length) {{
      lines.push('<p><strong>Checked clues:</strong> ' + f.join(', ') + '.</p>');
    }}
    if (urgent) {{
      lines.push('<p><strong>Urgent pattern selected.</strong> This tool cannot triage emergencies. Contact your GI on-call line, urgent care, or emergency services now if you feel unsafe. Read <a href="/blog/when-to-go-er-ibd">when to go to the ER</a>.</p>');
    }} else if (selected >= 6) {{
      lines.push('<p>Consider reading <a href="/blog/electrolytes-flare-ibd">electrolytes during flares</a> and <a href="/flare-help">flare help</a>. Log today in IBDPal before your visit.</p>');
    }} else {{
      lines.push('<p>Compare with <a href="/stool-labs-decoder">stool and labs decoder</a> articles if color or labs also changed.</p>');
    }}
    result.innerHTML = lines.join('');
  }}
  root.querySelectorAll('.bristol-pick').forEach(function (btn) {{
    btn.addEventListener('click', function () {{
      selected = Number(btn.getAttribute('data-type'));
      root.querySelectorAll('.bristol-pick').forEach(function (b) {{ b.setAttribute('aria-pressed', b === btn ? 'true' : 'false'); }});
      render();
    }});
  }});
  root.querySelectorAll('[data-flag]').forEach(function (el) {{
    el.addEventListener('change', render);
  }});
}})();
</script>
</body>
</html>
"""


def patch_vercel() -> None:
    text = VERCEL.read_text(encoding="utf-8")
    block = (
        '    {\n      "source": "/tools/bristol-flare-checker",\n'
        '      "destination": "/tools/bristol-flare-checker.html"\n    },\n'
    )
    if '"/tools/bristol-flare-checker"' not in text:
        text = text.replace('"rewrites": [\n', '"rewrites": [\n' + block)
        VERCEL.write_text(text, encoding="utf-8")
        print("patched vercel tool rewrite")


def patch_sitemap() -> None:
    today = date.today().isoformat()
    text = SITEMAP.read_text(encoding="utf-8")
    marker = "<!-- bristol-flare-checker-tool -->"
    entry = (
        f"  {marker}\n  <url>\n    <loc>{SITE}/tools/bristol-flare-checker</loc>\n"
        f"    <lastmod>{today}</lastmod>\n    <changefreq>monthly</changefreq>\n"
        f"    <priority>0.9</priority>\n  </url>"
    )
    if marker in text:
        text = re.sub(
            rf"\n  {re.escape(marker)}.*?(?=\n  <!-- |\n</urlset>)",
            "",
            text,
            flags=re.DOTALL,
        )
    text = text.replace("</urlset>", entry + "\n</urlset>")
    SITEMAP.write_text(text, encoding="utf-8")
    print("patched sitemap tool url")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(page_html(), encoding="utf-8")
    print("wrote", OUT.relative_to(ROOT))
    patch_vercel()
    patch_sitemap()


if __name__ == "__main__":
    main()
