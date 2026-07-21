# Search engine webmaster tools (beyond Google)

IBDPal sitemap: `https://www.ibdpal.org/sitemap.xml`

## Done in the repo (automated / deployable)

| Item | Location |
|------|----------|
| Sitemap declared for all crawlers | `robots.txt` → `Sitemap: https://www.ibdpal.org/sitemap.xml` |
| Bingbot / DuckDuckBot allowed | `robots.txt` |
| **IndexNow** key file | `/a50b1f808a1d4c41b89fc4b35d46418a.txt` |
| IndexNow API (Vercel) | `POST /api/indexnow` |
| CLI bulk submit | `node scripts/submit_indexnow.js --sitemap` |

IndexNow notifies **Bing** (and IndexNow partners such as Yandex, Seznam, Naver) when URLs change — faster than waiting for crawl.

### After each deploy (optional but recommended)

```bash
# From ibdpal-website root, once the key file is live on production:
node scripts/submit_indexnow.js --sitemap
```

Or submit one URL:

```bash
node scripts/submit_indexnow.js https://www.ibdpal.org/newly-diagnosed
```

Or via the live API (set `INDEXNOW_SUBMIT_TOKEN` in Vercel if you want auth):

```bash
curl -X POST https://www.ibdpal.org/api/indexnow \
  -H "Content-Type: application/json" \
  -H "x-indexnow-token: YOUR_TOKEN" \
  -d "{\"sitemap\":true}"
```

---

## Manual steps (you must do these — requires your login)

### 1. Bing Webmaster Tools (required)

1. Open [https://www.bing.com/webmasters](https://www.bing.com/webmasters) and sign in (Microsoft account).
2. **Add site** → `https://www.ibdpal.org`
3. **Easiest verify:** choose **Import from Google Search Console** (if GSC already owns the property).
4. Otherwise verify with one of:
   - XML file Bing gives you (upload to site root and tell us to commit it), or
   - Meta tag (paste into shared head and redeploy), or
   - DNS CNAME/TXT at your domain registrar
5. **Sitemaps** → Submit: `https://www.ibdpal.org/sitemap.xml`
6. **URL Submission** / IndexNow: confirm IndexNow is recognized (key URL above).
7. After new posts: use **URL Inspection / Submit URL** for priority pages.

Bing also feeds **Yahoo** and often helps **DuckDuckGo** discovery.

### 2. Google Search Console (keep doing)

Already in [GOOGLE_SEO.md](./GOOGLE_SEO.md):

- Property: `https://www.ibdpal.org`
- Sitemap: `https://www.ibdpal.org/sitemap.xml`
- Inspect URL → Request indexing for new pages

### 3. Yandex Webmaster (optional)

Only if you want CIS/RU coverage:

1. [https://webmaster.yandex.com](https://webmaster.yandex.com)
2. Add `https://www.ibdpal.org`
3. Verify (meta/file/DNS)
4. Submit the same sitemap

### 4. Skip for now

- **Baidu** — China-focused; skip unless you target China.
- Paid “submit to 50 directories” services — usually noise.

---

## Checklist after this change ships

- [ ] Deploy so `/a50b1f808a1d4c41b89fc4b35d46418a.txt` returns the key
- [ ] Bing Webmaster: add + verify site
- [ ] Bing: submit sitemap
- [ ] Run `node scripts/submit_indexnow.js --sitemap` once
- [ ] Confirm header shows **16 countries** (Vercel Analytics verified: US GB IN CA DE AU BD GT HK ID IE JP MY PK SE VE)

## Security note

The IndexNow **key file must be public** (that is how Bing validates ownership). Optional `INDEXNOW_SUBMIT_TOKEN` protects only the submit API, not the key file.
