# IBDPal website analytics (Vercel)

Track **visitors**, **page views**, **clicks**, and **section impressions** on [ibdpal.org](https://ibdpal.org) hosted on Vercel.

## 1. Enable Vercel Web Analytics (recommended)

1. Open [Vercel Dashboard](https://vercel.com) → your **ibdpal-website** project.
2. Go to **Analytics** → **Web Analytics** → **Enable**.
3. Deploy the site (analytics scripts are already included in HTML).

**What you get in Vercel:** unique visitors, page views, top pages, referrers, countries, devices. Data appears after real traffic (often within minutes).

## 2. Optional: Google Analytics 4 (clicks & custom events)

For richer event reports (tab views, blog clicks, outbound links):

1. [Google Analytics](https://analytics.google.com) → create a **Web** property for `ibdpal.org`.
2. Copy the **Measurement ID** (`G-XXXXXXXXXX`).
3. Edit `analytics-config.js`:

```javascript
ga4MeasurementId: 'G-XXXXXXXXXX',
```

4. Commit, push, and redeploy on Vercel.

In GA4: **Reports → Engagement → Events** for `click`, `tab_view`, `section_impression`, `email_signup`.

## 3. Events collected

| Event | When |
|--------|------|
| `page_view` | Each page load |
| `click` | Links, tab buttons, blog cards, footer, header |
| `tab_view` | Homepage tab change (Overview, Features, Blogs, …) |
| `section_impression` | Section scrolls into view (≥35% visible) |
| `email_signup` | Notify Me form submitted on homepage |

## 4. Debug locally

Add `?analytics_debug=1` to the URL and open the browser console to see logged events. Vercel Insights only records on the **production** Vercel deployment, not `file://` or arbitrary local servers.

## 5. Privacy

Update your [Privacy Policy](/privacy) to mention anonymous website analytics (Vercel and/or Google). No health data is sent from these scripts.

## 6. Files

- `analytics-config.js` — turn Vercel/GA4 on or off, set GA4 ID
- `analytics.js` — tracking implementation
- Included on all public HTML pages before `script.js`
