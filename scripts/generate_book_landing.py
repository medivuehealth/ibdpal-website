#!/usr/bin/env python3
"""Generate the Eating With IBD book landing page (Amazon offer + Book schema)."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from seo_head import SITE, render_seo_head  # noqa: E402
from site_footer import SITE_FOOTER_STATIC  # noqa: E402
from site_nav import PAGE_SCRIPTS  # noqa: E402

AMAZON_URL = "https://www.amazon.com/dp/B0HHYZL27M"
PATH = "/eating-with-ibd"
COVER = f"{SITE}/assets/books/eating-with-ibd-cover.jpg"
COVER_THUMB = f"{SITE}/assets/books/eating-with-ibd-cover-thumb.jpg"
AUTHOR_NAME = "Aryan Shashi Kumar"

TITLE = "Eating With IBD by Aryan Shashi Kumar | IBDPal"
DESC = (
    "Eating With IBD by Aryan Shashi Kumar (MediVue / IBDPal): Crohn’s and ulcerative colitis "
    "nutrition education on Amazon. Companion to free IBDPal guides. Education only, not medical advice."
)


def book_graph() -> list[dict]:
    book_id = f"{SITE}{PATH}#book"
    author = {
        "@type": "Person",
        "@id": f"{SITE}/#about-founders",
        "name": AUTHOR_NAME,
        "url": f"{SITE}/#about-founders",
        "sameAs": [
            f"{SITE}/founder",
            f"{SITE}/about-founders",
            f"{SITE}/eating-with-ibd",
            AMAZON_URL,
        ],
        "jobTitle": "Founder",
        "worksFor": {"@id": f"{SITE}/#organization"},
    }
    return [
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "IBDPal", "item": f"{SITE}/"},
                {"@type": "ListItem", "position": 2, "name": "Eating With IBD", "item": f"{SITE}{PATH}"},
            ],
        },
        {
            "@type": "WebPage",
            "@id": f"{SITE}{PATH}#webpage",
            "url": f"{SITE}{PATH}",
            "name": TITLE,
            "description": DESC,
            "isPartOf": {"@id": f"{SITE}/#website"},
            "about": {"@id": book_id},
            "author": {"@id": f"{SITE}/#about-founders"},
            "primaryImageOfPage": {"@type": "ImageObject", "url": COVER},
            "mainEntity": {"@id": book_id},
        },
        author,
        {
            "@type": ["Book", "Product"],
            "@id": book_id,
            "name": "Eating With IBD",
            "alternateName": [
                "Eating With IBD nutrition book",
                "IBDPal Eating With IBD",
                "Crohn's and colitis nutrition book",
                f"{AUTHOR_NAME} Eating With IBD",
                "Eating With IBD Amazon book",
            ],
            "url": f"{SITE}{PATH}",
            "image": [COVER, COVER_THUMB],
            "description": (
                f"Eating With IBD by {AUTHOR_NAME}, founder of MediVue and IBDPal: a practical nutrition "
                "guide for Crohn’s disease and ulcerative colitis. Available on Amazon; companion to free "
                "IBDPal education on ibdpal.org."
            ),
            "inLanguage": "en",
            "genre": "Health & Fitness / Diseases / Gastrointestinal",
            "isbn": "B0HHYZL27M",
            "author": {"@id": f"{SITE}/#about-founders"},
            "creator": {"@id": f"{SITE}/#about-founders"},
            "publisher": {"@id": f"{SITE}/#organization"},
            "brand": {"@id": f"{SITE}/#organization"},
            "sameAs": [AMAZON_URL],
            "workExample": [
                {
                    "@type": "Book",
                    "bookFormat": "https://schema.org/EBook",
                    "name": "Eating With IBD",
                    "url": AMAZON_URL,
                    "sameAs": [AMAZON_URL],
                    "author": {"@id": f"{SITE}/#about-founders"},
                    "bookEdition": "Amazon Kindle / print",
                }
            ],
            "offers": {
                "@type": "Offer",
                "url": AMAZON_URL,
                "availability": "https://schema.org/InStock",
                "itemCondition": "https://schema.org/NewCondition",
                "priceCurrency": "USD",
                "seller": {"@type": "Organization", "name": "Amazon.com"},
            },
            "audience": {
                "@type": "PatientAudience",
                "healthCondition": [
                    {"@type": "MedicalCondition", "name": "Inflammatory bowel disease"},
                    {"@type": "MedicalCondition", "name": "Crohn's disease"},
                    {"@type": "MedicalCondition", "name": "Ulcerative colitis"},
                ],
            },
            "isRelatedTo": [
                {"@type": "WebPage", "url": f"{SITE}/ibd-nutrition", "name": "IBD nutrition hub"},
                {"@type": "SoftwareApplication", "name": "IBDPal", "url": f"{SITE}/"},
                {"@type": "WebPage", "url": f"{SITE}/founder", "name": f"{AUTHOR_NAME}, MediVue founder"},
            ],
        },
    ]


def page_html() -> str:
    head = render_seo_head(
        title=TITLE,
        description=DESC,
        path=PATH,
        og_type="book",
        og_image=COVER,
        keywords=(
            "Eating With IBD, Aryan Shashi Kumar, Aryan Shashi Kumar Eating With IBD, "
            "Eating With IBD Amazon book, IBD nutrition book, Crohn's diet book, "
            "ulcerative colitis nutrition guide, IBDPal book, MediVue Amazon"
        ),
        json_ld=book_graph(),
        hreflang_es=None,
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
{head}
    <meta property="og:image:alt" content="Eating With IBD book cover by {AUTHOR_NAME}">
    <meta name="twitter:image" content="{COVER}">
    <meta name="author" content="{AUTHOR_NAME}">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="stylesheet" href="/styles.css">
    <link rel="stylesheet" href="/site-layout-icn.css">
    <link rel="stylesheet" href="/site-polish.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet">
    <link rel="icon" type="image/x-icon" href="/favicon.ico">
    <link rel="icon" type="image/png" href="/IBDPal_Logo.png">
    <link rel="apple-touch-icon" href="/IBDPal_Logo.png">
</head>
<body>
    <div class="container">
        <header class="header">
            <div class="header__inner">
                <div class="logo">
                    <a href="/" class="logo-brand" aria-label="IBDPal home">
                        <img src="/IBDPal_Logo.png" alt="IBDPal" class="logo-img" width="52" height="52" decoding="async">
                    </a>
                    <div class="logo-text">
                        <p class="logo-name"><a href="/">IBDPal</a></p>
                        <p class="tagline">Empowering IBD Patients</p>
                    </div>
                </div>
            </div>
        </header>

        <main class="main-content">
            <article class="support-section seo-landing tab-page-section book-landing" data-track-impression="eating_with_ibd" data-track-label="Eating With IBD book landing" itemscope itemtype="https://schema.org/Book">
                <header class="page-header-compact">
                    <p class="page-header-compact__eyebrow">MediVue · IBDPal · Amazon book</p>
                    <h1 class="page-header-compact__title" itemprop="name">Eating With IBD</h1>
                    <p class="page-header-compact__lead">
                        By <strong itemprop="author">{AUTHOR_NAME}</strong>, founder of MediVue and IBDPal.
                        A practical nutrition book for Crohn&rsquo;s disease and ulcerative colitis, available on Amazon.
                        Education only; not a substitute for personalized medical or dietitian advice.
                    </p>
                </header>

                <section class="book-landing__hero" aria-labelledby="book-buy-heading">
                    <img
                        class="book-landing__cover"
                        src="/assets/books/eating-with-ibd-cover.jpg"
                        width="480"
                        height="720"
                        alt="Cover of Eating With IBD by {AUTHOR_NAME} on Amazon"
                        itemprop="image"
                        decoding="async"
                    >
                    <div class="book-landing__buy">
                        <h2 id="book-buy-heading">Get the book on Amazon</h2>
                        <p>
                            Purchase <strong>Eating With IBD</strong> by <strong>{AUTHOR_NAME}</strong> directly from Amazon.
                            Use it alongside free IBDPal articles, hubs, and the iOS tracking app.
                        </p>
                        <p class="book-landing__actions">
                            <a
                                class="book-landing__cta"
                                href="{AMAZON_URL}"
                                target="_blank"
                                rel="noopener noreferrer"
                                itemprop="url"
                                data-track-click="book_landing_amazon"
                                data-track-label="Eating With IBD Amazon CTA"
                            >Buy on Amazon</a>
                            <a class="book-landing__secondary" href="/ibd-nutrition">Free nutrition hub</a>
                        </p>
                        <p class="book-landing__asin">Amazon: <a href="{AMAZON_URL}" target="_blank" rel="noopener noreferrer">{AMAZON_URL}</a></p>
                    </div>
                </section>

                <section class="seo-landing__block">
                    <h2>About the author</h2>
                    <p>
                        <strong>{AUTHOR_NAME}</strong> founded <strong>MediVue</strong>, a North Carolina nonprofit,
                        and built <strong>IBDPal</strong> to make Crohn&rsquo;s and ulcerative colitis education clearer
                        between clinic visits. <em>Eating With IBD</em> is his Amazon nutrition companion to the free
                        guides and articles on ibdpal.org.
                    </p>
                    <p>
                        <a href="/founder">{AUTHOR_NAME} founder page</a> ·
                        <a href="/#about-founders">Founders story on the homepage</a> ·
                        <a href="{AMAZON_URL}" target="_blank" rel="noopener noreferrer">Eating With IBD on Amazon</a>
                    </p>
                </section>

                <section class="seo-landing__block">
                    <h2>Who this book is for</h2>
                    <ul class="seo-landing__list">
                        <li>People newly diagnosed with Crohn&rsquo;s or ulcerative colitis who want clearer food language</li>
                        <li>Patients in remission rebuilding meals after flares or restrictive phases</li>
                        <li>Caregivers and teens looking for practical, clinic-friendly nutrition framing</li>
                        <li>Readers who already use <a href="/">IBDPal</a> education and want a deeper print/Kindle companion</li>
                    </ul>
                </section>

                <section class="seo-landing__block">
                    <h2>Related free education on IBDPal</h2>
                    <ul class="seo-landing__list">
                        <li><a href="/ibd-nutrition">IBD nutrition hub</a></li>
                        <li><a href="/newly-diagnosed">Newly diagnosed roadmap</a></li>
                        <li><a href="/flare-help">Flare help</a></li>
                        <li><a href="/blog">Patient education articles</a></li>
                        <li><a href="/ask">Reader Q&amp;A</a></li>
                    </ul>
                </section>

                <section class="seo-landing__block">
                    <h2>Medical disclaimer</h2>
                    <p>
                        This book and IBDPal.org are for educational purposes only and are not medical advice,
                        diagnosis, or treatment. Always discuss diet changes with your gastroenterologist or
                        registered dietitian, especially during flares, after surgery, or while on immunosuppression.
                    </p>
                </section>
            </article>
        </main>

{SITE_FOOTER_STATIC}
    </div>
{PAGE_SCRIPTS}
</body>
</html>
"""


def main() -> None:
    out = ROOT / "eating-with-ibd.html"
    out.write_text(page_html(), encoding="utf-8")
    print("wrote", out.relative_to(ROOT))


if __name__ == "__main__":
    main()
