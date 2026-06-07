/**
 * Blog vote API | Vercel Blob REST API (no SDK).
 * ibdpal-blob is a private store | all uploads use x-vercel-blob-access: private.
 */
const BLOB_API = 'https://vercel.com/api/blob';
const BLOB_API_VERSION = '12';
const BLOB_ACCESS = 'private';
const API_BUILD = 'rest-v4-private';

const LOG_PATH = 'blog-votes/votes.log';
const COUNTS_PATH = 'blog-votes/counts.json';

function json(res, status, body) {
  res.status(status).setHeader('Content-Type', 'application/json');
  res.end(JSON.stringify(body));
}

function getBlobToken() {
  return process.env.BLOB_READ_WRITE_TOKEN || '';
}

function hasBlobCredentials() {
  return Boolean(getBlobToken());
}

function getStoreId(token) {
  const fromEnv = process.env.BLOB_STORE_ID;
  if (fromEnv && String(fromEnv).trim()) {
    const id = String(fromEnv).trim();
    return id.startsWith('store_') ? id.slice('store_'.length) : id;
  }
  const parts = token.split('_');
  if (parts.length >= 4) {
    const id = parts[3];
    return id.startsWith('store_') ? id.slice('store_'.length) : id;
  }
  return '';
}

function setupMessage() {
  return (
    'Add BLOB_READ_WRITE_TOKEN to ibdpal-website (Settings → Environment Variables, Production + Preview), ' +
    'connect store ibdpal-blob to this project, then Redeploy. ' +
    'Check status: /api/blog-vote?check=1'
  );
}

function formatError(err) {
  const msg = err?.message || String(err);
  if (msg.includes('MISSING_BLOB_TOKEN')) {
    return setupMessage();
  }
  if (!hasBlobCredentials()) {
    return setupMessage();
  }
  return 'Blob request failed: ' + msg + '. Confirm env vars are on Production and Redeploy.';
}

async function blobApi(path, { method, token, headers = {}, body }) {
  const storeId = getStoreId(token);
  if (!storeId) {
    throw new Error('Could not resolve Blob store id from token or BLOB_STORE_ID');
  }

  const res = await fetch(`${BLOB_API}${path}`, {
    method,
    headers: {
      authorization: `Bearer ${token}`,
      'x-api-version': BLOB_API_VERSION,
      'x-vercel-blob-store-id': storeId,
      ...headers
    },
    body
  });

  if (!res.ok) {
    let detail = `${res.status} ${res.statusText}`;
    try {
      const data = await res.json();
      if (data?.error?.message) {
        detail = data.error.message;
      }
    } catch {
      /* ignore */
    }
    throw new Error(detail);
  }

  if (res.status === 204) {
    return null;
  }
  const text = await res.text();
  return text ? JSON.parse(text) : null;
}

async function listBlobs(prefix, token) {
  const params = new URLSearchParams({ prefix });
  const data = await blobApi(`?${params.toString()}`, { method: 'GET', token });
  return data?.blobs || [];
}

async function putBlob(pathname, content, token) {
  const params = new URLSearchParams({ pathname });
  await blobApi(`/?${params.toString()}`, {
    method: 'PUT',
    token,
    headers: {
      'content-type': 'text/plain; charset=utf-8',
      'x-vercel-blob-access': BLOB_ACCESS,
      'x-add-random-suffix': '0',
      'x-allow-overwrite': '1'
    },
    body: content
  });
}

async function delBlob(url, token) {
  await blobApi('/delete', {
    method: 'POST',
    token,
    headers: { 'content-type': 'application/json' },
    body: JSON.stringify({ urls: [url] })
  });
}

async function readBlobText(pathname) {
  const token = getBlobToken();
  if (!token) {
    return '';
  }

  const blobs = await listBlobs('blog-votes/', token);
  const blob = blobs.find((b) => b.pathname === pathname);
  if (!blob) {
    return '';
  }

  const url = blob.downloadUrl || blob.url;
  const res = await fetch(url, {
    headers: { authorization: `Bearer ${token}` }
  });
  if (!res.ok) {
    throw new Error(`Failed to read ${pathname}: ${res.status}`);
  }
  return res.text();
}

async function writeBlobText(pathname, content) {
  const token = getBlobToken();
  if (!token) {
    throw new Error('MISSING_BLOB_TOKEN');
  }

  try {
    await putBlob(pathname, content, token);
  } catch (err) {
    const msg = err?.message || '';
    if (!msg.includes('already exists') && !msg.includes('conflict')) {
      throw err;
    }
    const blobs = await listBlobs('blog-votes/', token);
    const existing = blobs.find((b) => b.pathname === pathname);
    if (existing?.url) {
      await delBlob(existing.url, token);
    }
    await putBlob(pathname, content, token);
  }
}

function parseCounts(raw) {
  if (!raw) {
    return {};
  }
  try {
    const data = JSON.parse(raw);
    return typeof data === 'object' && data !== null ? data : {};
  } catch {
    return {};
  }
}

function isValidSlug(slug) {
  return typeof slug === 'string' && /^[a-z0-9-]+$/.test(slug) && slug.length <= 80;
}

async function runDiagnostic(deep) {
  const token = getBlobToken();
  const out = {
    ok: false,
    apiBuild: API_BUILD,
    hasBlobReadWriteToken: Boolean(token),
    hasBlobStoreId: Boolean(process.env.BLOB_STORE_ID),
    vercelEnv: process.env.VERCEL_ENV || null,
    hint: setupMessage()
  };

  if (!token) {
    return out;
  }

  try {
    await putBlob('blog-votes/.health-check', 'ok', token);
    if (deep) {
      await readBlobText(LOG_PATH);
      await readBlobText(COUNTS_PATH);
      const testPath = 'blog-votes/.health-check-rw';
      await putBlob(testPath, 'ok', token);
      const testBlob = (await listBlobs('blog-votes/', token)).find((b) => b.pathname === testPath);
      if (testBlob?.url) {
        await delBlob(testBlob.url, token);
      }
    }
    out.ok = true;
    out.hint = 'Blob is configured. Voting should work.';
  } catch (err) {
    out.blobError = err?.message || String(err);
  }

  return out;
}

export default async function handler(req, res) {
  if (req.method === 'GET' && req.query?.check === '1') {
    return json(res, 200, await runDiagnostic(req.query?.deep === '1'));
  }

  if (!hasBlobCredentials()) {
    return json(res, 503, { error: setupMessage() });
  }

  try {
    if (req.method === 'GET') {
      const slug = req.query?.slug;
      const counts = parseCounts(await readBlobText(COUNTS_PATH));

      if (slug) {
        if (!isValidSlug(slug)) {
          return json(res, 400, { error: 'Invalid slug' });
        }
        return json(res, 200, counts[slug] || { up: 0, down: 0 });
      }

      return json(res, 200, counts);
    }

    if (req.method === 'POST') {
      let body = req.body;
      if (typeof body === 'string') {
        try {
          body = JSON.parse(body);
        } catch {
          return json(res, 400, { error: 'Invalid JSON body' });
        }
      }

      const slug = body?.slug;
      const vote = body?.vote;

      if (!isValidSlug(slug) || (vote !== 'up' && vote !== 'down')) {
        return json(res, 400, { error: 'Invalid slug or vote' });
      }

      const timestamp = new Date().toISOString();
      const logLine = `${timestamp}\t${slug}\t${vote}\n`;

      const previousLog = await readBlobText(LOG_PATH);
      await writeBlobText(LOG_PATH, previousLog + logLine);

      const counts = parseCounts(await readBlobText(COUNTS_PATH));
      if (!counts[slug]) {
        counts[slug] = { up: 0, down: 0 };
      }
      counts[slug][vote] += 1;
      await writeBlobText(COUNTS_PATH, JSON.stringify(counts, null, 2) + '\n');

      return json(res, 200, { ok: true, counts: counts[slug] });
    }

    res.setHeader('Allow', 'GET, POST');
    return json(res, 405, { error: 'Method not allowed' });
  } catch (err) {
    console.error('blog-vote error', err);
    return json(res, 503, { error: formatError(err) });
  }
}
