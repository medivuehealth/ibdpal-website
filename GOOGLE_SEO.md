# Google SEO checklist for ibdpal.org

Site technical SEO is implemented in HTML (meta tags, canonical URLs, Open Graph, JSON-LD) and `sitemap.xml`.

## After each deploy

1. **Google Search Console** | [search.google.com/search-console](https://search.google.com/search-console)
   - Property: `https://ibdpal.org`
   - Submit sitemap: `https://ibdpal.org/sitemap.xml`
   - Request indexing for new URLs (Inspect URL → Request indexing):
     - `https://ibdpal.org/resources`
     - `https://ibdpal.org/newly-diagnosed`
     - `https://ibdpal.org/ibd-crohns-support`
     - New blog posts under `/blog/…`

2. **Validate structured data** | [search.google.com/test/rich-results](https://search.google.com/test/rich-results)
   - Test homepage (FAQ + ItemList)
   - Test `/ibd-crohns-support` (FAQ)
   - Test a blog article (Article + BreadcrumbList)

## Target queries (content already aligned)

| Query theme | Primary URL |
|-------------|-------------|
| IBD Crohn's support | `/ibd-crohns-support`, `/#community` |
| Newly diagnosed Crohn's / colitis | `/newly-diagnosed` |
| IBD diet / flare foods | `/blog/…`, `/#blogs` |
| Crohn's app / nutrition tracker | `/`, `/#app` |

## Notes

- Tab URLs (`/#community`, `/#blogs`) are secondary; **crawlable pages** (`/resources`, `/newly-diagnosed`, etc.) are in the sitemap for Google.
- Content is educational only; do not claim medical outcomes in meta descriptions.
- `llms.txt` and `robots.txt` allow full crawling.

## Regenerating pages

```bash
python scripts/generate_static_pages.py
python scripts/patch_blog_jsonld.py
```

Blog generator: `python scripts/generate_blog_posts.py` (June lifestyle posts only).

## Accelerated Mobile Pages (AMP)

AMP variants exist for **all blog posts** and **patient guides** (fast mobile cache, no custom JS).

| Content | Canonical URL | AMP URL |
|---------|---------------|---------|
| Blog post | `/blog/{slug}` | `/blog/{slug}/amp` |
| Patient guide | `/guides/{slug}` | `/guides/{slug}/amp` |

Canonical pages include `<link rel="amphtml">`. AMP pages link back via `<link rel="canonical">`.

**Regenerate after blog or guide changes:**

```bash
python scripts/generate_amp_pages.py
```

**Validate after deploy:** [validator.ampproject.org](https://validator.ampproject.org/) using a live AMP URL.

**Out of AMP scope:** homepage tabs, community map, resource library (require custom JavaScript).
