import { get, list, put } from '@vercel/blob';

const LOG_PATH = 'blog-votes/votes.log';
const COUNTS_PATH = 'blog-votes/counts.json';
const STORE_NAME = 'ibdpal-blob';

function json(res, status, body) {
  res.status(status).setHeader('Content-Type', 'application/json');
  res.end(JSON.stringify(body));
}

/** Token for local dev; on Vercel, OIDC + BLOB_STORE_ID is used when connected. */
function blobOptions() {
  const token =
    process.env.BLOB_READ_WRITE_TOKEN ||
    process.env.IBDPAL_BLOB_READ_WRITE_TOKEN;
  return token ? { token } : {};
}

function storageConfigured() {
  if (process.env.BLOB_READ_WRITE_TOKEN) {
    return true;
  }
  if (process.env.BLOB_STORE_ID) {
    return true;
  }
  if (process.env.VERCEL) {
    return true;
  }
  return false;
}

function storageSetupMessage() {
  return (
    'Blob store "' +
    STORE_NAME +
    '" must be connected to the ibdpal-website project: ' +
    'Vercel → Storage → ' +
    STORE_NAME +
    ' → Projects → Connect to Project → ibdpal-website (Production + Preview), then Redeploy.'
  );
}

async function readBlobText(pathname) {
  const { blobs } = await list({ prefix: 'blog-votes/', ...blobOptions() });
  const blob = blobs.find((b) => b.pathname === pathname);
  if (!blob) {
    return '';
  }
  const result = await get(blob.url, { access: 'private', ...blobOptions() });
  return result.text();
}

async function writeBlobText(pathname, content) {
  await put(pathname, content, {
    access: 'private',
    addRandomSuffix: false,
    allowOverwrite: true,
    ...blobOptions()
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

function isBlobConfigError(err) {
  const msg = String(err?.message || err || '').toLowerCase();
  return (
    msg.includes('token') ||
    msg.includes('blob') ||
    msg.includes('unauthorized') ||
    msg.includes('not configured')
  );
}

export default async function handler(req, res) {
  if (!storageConfigured()) {
    return json(res, 503, { error: storageSetupMessage() });
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
    if (isBlobConfigError(err)) {
      return json(res, 503, { error: storageSetupMessage() });
    }
    console.error('blog-vote error', err);
    return json(res, 500, { error: 'Could not save vote. Try again later.' });
  }
}
