import pg from 'pg';

const { Pool } = pg;

let pool;

export function json(res, status, body) {
  res.status(status).setHeader('Content-Type', 'application/json');
  res.end(JSON.stringify(body));
}

export function db() {
  if (!process.env.DATABASE_URL) {
    throw new Error('DATABASE_URL is not configured for ibdpal-website.');
  }

  if (!pool) {
    pool = new Pool({
      connectionString: process.env.DATABASE_URL,
      ssl: {
        rejectUnauthorized: false
      },
      max: 5,
      idleTimeoutMillis: 30000,
      connectionTimeoutMillis: 5000
    });
  }

  return pool;
}

export function normalizeTerm(value) {
  return String(value || '')
    .toLowerCase()
    .replace(/[^\w\s'-]/g, ' ')
    .replace(/\s+/g, ' ')
    .trim()
    .slice(0, 80);
}

export function cleanText(value, maxLength) {
  const text = String(value || '').trim();
  return text ? text.slice(0, maxLength) : null;
}

export function pathFromUrl(url) {
  const cleanUrl = cleanText(url, 240);
  if (!cleanUrl) return null;

  try {
    const parsed = new URL(cleanUrl, 'https://www.ibdpal.org');
    return parsed.pathname || '/';
  } catch {
    return null;
  }
}

export function slugFromUrl(url) {
  const pathname = pathFromUrl(url);
  if (!pathname) return null;
  const parts = pathname.split('/').filter(Boolean);
  return parts.length ? parts[parts.length - 1].slice(0, 120) : null;
}

export function contentTypeFromUrl(url) {
  const pathname = pathFromUrl(url) || '';
  if (pathname.startsWith('/blog/')) return 'article';
  if (pathname.startsWith('/guides/')) return 'guide';
  if (pathname === '/research' || pathname.startsWith('/research/')) return 'research';
  if (pathname === '/resources' || pathname === '/library') return 'library';
  return 'page';
}

export function parseBody(req) {
  if (typeof req.body === 'string') {
    try {
      return JSON.parse(req.body);
    } catch {
      return {};
    }
  }
  return req.body || {};
}

export function methodNotAllowed(res, methods) {
  res.setHeader('Allow', methods.join(', '));
  return json(res, 405, { success: false, error: 'Method not allowed' });
}
