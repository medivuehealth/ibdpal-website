/**
 * IndexNow — notify Bing (and IndexNow partners) of URL updates.
 *
 * POST /api/indexnow
 * Body: { "url": "https://www.ibdpal.org/path" }
 *    or { "urls": ["https://www.ibdpal.org/a", "..."] }  (max 100)
 *    or { "sitemap": true }  to submit homepage + sitemap URL
 *
 * Auth: set INDEXNOW_SUBMIT_TOKEN in Vercel env, then send header
 *   x-indexnow-token: <same value>
 * Or omit the env var to allow unauthenticated submits only from
 * Vercel cron / same-deployment tooling (still rate-limit carefully).
 *
 * Key file (public): /a50b1f808a1d4c41b89fc4b35d46418a.txt
 */
const INDEXNOW_KEY = 'a50b1f808a1d4c41b89fc4b35d46418a';
const HOST = 'www.ibdpal.org';
const KEY_LOCATION = `https://${HOST}/${INDEXNOW_KEY}.txt`;
const ENDPOINT = 'https://api.indexnow.org/indexnow';

function json(res, status, body) {
  res.status(status).setHeader('Content-Type', 'application/json');
  res.setHeader('Cache-Control', 'no-store');
  res.end(JSON.stringify(body));
}

function authorized(req) {
  const expected = process.env.INDEXNOW_SUBMIT_TOKEN;
  if (!expected) return true;
  const got = req.headers['x-indexnow-token'] || '';
  return got === expected;
}

function normalizeUrl(u) {
  try {
    const parsed = new URL(String(u));
    if (parsed.protocol !== 'https:') return null;
    if (parsed.hostname !== HOST && parsed.hostname !== 'ibdpal.org') return null;
    parsed.hostname = HOST;
    parsed.hash = '';
    return parsed.toString().replace(/\/$/, '') || `https://${HOST}`;
  } catch {
    return null;
  }
}

async function submitToIndexNow(urlList) {
  const body = {
    host: HOST,
    key: INDEXNOW_KEY,
    keyLocation: KEY_LOCATION,
    urlList,
  };
  const resp = await fetch(ENDPOINT, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json; charset=utf-8' },
    body: JSON.stringify(body),
  });
  const text = await resp.text();
  return { status: resp.status, body: text };
}

module.exports = async function handler(req, res) {
  if (req.method === 'OPTIONS') {
    res.status(204).end();
    return;
  }
  if (req.method !== 'POST') {
    return json(res, 405, { error: 'POST only' });
  }
  if (!authorized(req)) {
    return json(res, 401, { error: 'unauthorized' });
  }

  let payload = req.body;
  if (typeof payload === 'string') {
    try {
      payload = JSON.parse(payload);
    } catch {
      return json(res, 400, { error: 'invalid JSON' });
    }
  }
  payload = payload || {};

  let urls = [];
  if (payload.sitemap) {
    urls = [`https://${HOST}/`, `https://${HOST}/sitemap.xml`];
  }
  if (payload.url) urls.push(payload.url);
  if (Array.isArray(payload.urls)) urls = urls.concat(payload.urls);

  const cleaned = [...new Set(urls.map(normalizeUrl).filter(Boolean))].slice(0, 100);
  if (!cleaned.length) {
    return json(res, 400, {
      error: 'provide url, urls[], or sitemap:true (https www.ibdpal.org only)',
    });
  }

  try {
    const result = await submitToIndexNow(cleaned);
    return json(res, result.status >= 200 && result.status < 300 ? 200 : 502, {
      ok: result.status >= 200 && result.status < 300,
      indexNowStatus: result.status,
      submitted: cleaned.length,
      urls: cleaned,
      detail: result.body || null,
    });
  } catch (err) {
    return json(res, 502, { error: 'IndexNow request failed', detail: String(err.message || err) });
  }
};
