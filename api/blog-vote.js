import { get, list, put } from '@vercel/blob';

const LOG_PATH = 'blog-votes/votes.log';
const COUNTS_PATH = 'blog-votes/counts.json';
/** ibdpal-blob is a public store — must use access: "public" (not private). */
const BLOB_ACCESS = 'public';

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

function blobOptions() {
  const token = getBlobToken();
  return token ? { token } : {};
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

async function readBlobText(pathname) {
  const token = getBlobToken();
  if (!token) {
    return '';
  }
  const { blobs } = await list({ prefix: 'blog-votes/', token });
  const blob = blobs.find((b) => b.pathname === pathname);
  if (!blob) {
    return '';
  }
  const result = await get(blob.url, { access: BLOB_ACCESS, token });
  return result.text();
}

async function writeBlobText(pathname, content) {
  const token = getBlobToken();
  if (!token) {
    throw new Error('MISSING_BLOB_TOKEN');
  }
  await put(pathname, content, {
    access: BLOB_ACCESS,
    addRandomSuffix: false,
    allowOverwrite: true,
    token
  });
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

async function runDiagnostic() {
  const token = getBlobToken();
  const out = {
    ok: false,
    hasBlobReadWriteToken: Boolean(token),
    hasBlobStoreId: Boolean(process.env.BLOB_STORE_ID),
    vercelEnv: process.env.VERCEL_ENV || null,
    hint: setupMessage()
  };

  if (!token) {
    return out;
  }

  try {
    await put('blog-votes/.health-check', 'ok', {
      access: BLOB_ACCESS,
      addRandomSuffix: false,
      allowOverwrite: true,
      token
    });
    out.ok = true;
    out.hint = 'Blob is configured. Voting should work.';
  } catch (err) {
    out.blobError = err?.message || String(err);
  }

  return out;
}

export default async function handler(req, res) {
  if (req.method === 'GET' && req.query?.check === '1') {
    return json(res, 200, await runDiagnostic());
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
