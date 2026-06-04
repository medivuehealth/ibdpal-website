import { get, list, put } from '@vercel/blob';

const LOG_PATH = 'blog-votes/votes.log';
const COUNTS_PATH = 'blog-votes/counts.json';

function json(res, status, body) {
  res.status(status).setHeader('Content-Type', 'application/json');
  res.end(JSON.stringify(body));
}

async function readBlobText(pathname) {
  const { blobs } = await list({ prefix: 'blog-votes/' });
  const blob = blobs.find((b) => b.pathname === pathname);
  if (!blob) {
    return '';
  }
  const result = await get(blob.url, { access: 'private' });
  return result.text();
}

async function writeBlobText(pathname, content) {
  await put(pathname, content, {
    access: 'private',
    addRandomSuffix: false,
    allowOverwrite: true
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

export default async function handler(req, res) {
  if (!process.env.BLOB_READ_WRITE_TOKEN) {
    return json(res, 503, {
      error: 'Vote storage is not configured. Add Vercel Blob to the project (see BLOG_VOTES_SETUP.md).'
    });
  }

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
}
