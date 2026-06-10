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
   - Test `/visit-prep` (HowTo + BreadcrumbList)
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
python scripts/generate_seo_hubs.py
python scripts/generate_seo_landings.py
python scripts/sync_llms_txt.py
python scripts/patch_blog_jsonld.py
```

- `generate_seo_hubs.py` rebuilds hub pages, patches related reading on all blogs, syncs `llms.txt`, and regenerates Spanish mirrors.
- `generate_es_pages.py` alone rebuilds `/es/*` pages from `data/es-pages.json`.
- `sync_llms_txt.py` alone refreshes blog, guide, and hub URL lists in `llms.txt`.

## Spanish mirrors (Tier 2)

| English | Spanish |
|---------|---------|
| `/` (hub) | `/es/recursos` |
| `/newly-diagnosed` | `/es/recien-diagnosticado` |
| `/ibd-nutrition` | `/es/nutricion-eii` |
| `/crohns-disease` | `/es/enfermedad-crohn` |
| `/ulcerative-colitis` | `/es/colitis-ulcerosa` |
| `/teens-and-school` | `/es/adolescentes-escuela` |
| `/flare-help` | `/es/brotes-eii` |
| `/faq` | `/es/preguntas-frecuentes` |

Paired `hreflang` tags connect English and Spanish URLs. Guides and blogs link to English articles with an (inglés) label until translated.

## Tier 3: glossary, stories, and new articles

```bash
python scripts/generate_tier3_seo.py
python scripts/generate_seo_hubs.py
python scripts/generate_amp_pages.py
python scripts/sync_llms_txt.py
```

| URL | Purpose |
|-----|---------|
| `/glossary` | IBD term definitions (`DefinedTermSet` schema) |
| `/patient-stories` | Story index with `ItemList` schema |
| `/patient-stories/:slug` | Individual crawlable patient stories |
| `/blog/ibd-pregnancy-planning` | Pregnancy planning with IBD |
| `/blog/college-with-ibd` | College accommodations and dining |
| `/blog/j-pouch-basics-ibd` | J-pouch patient-level overview |
| `/blog/when-to-go-er-ibd` | When to seek emergency care |

## IBD research sources

Homepage **Research** tab (`/#research`) and crawlable page `/research` list AGA, Congress, WebMD, and National Academies nutrition guidance.

```bash
python scripts/generate_research_page.py
```

Edit `data/research-sources.json` to add sources, then re-run the generator.

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

## SEO hubs & directories (Tier 1)

Crawlable hub pages (not hash tabs):

| URL | Purpose |
|-----|---------|
| `/blog` | Full blog index by category |
| `/ibd-nutrition` | Nutrition & diet cluster |
| `/crohns-disease` | Crohn's resources cluster |
| `/ulcerative-colitis` | UC resources cluster |
| `/teens-and-school` | Teen & high school cluster |
| `/flare-help` | Flare management cluster |
| `/faq` | FAQ with FAQPage schema |
| `/support` | IBD support by U.S. state (51 pages) |

**Regenerate after hub data changes:**

```bash
python scripts/generate_seo_hubs.py
```

Blog posts get automatic “Related topics” links to hubs when regenerated.
