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

/** Stems used to catch truncated typed queries like "self manageme". */
const COMPLETION_STEMS = [
  'management', 'symptoms', 'diarrhea', 'abdominal', 'inflammation',
  'nutrition', 'medication', 'medications', 'biologics', 'remission',
  'constipation', 'fatigue', 'hydration', 'supplement', 'supplements',
  'diagnosis', 'treatment', 'treatments', 'surgery', 'osteoporosis'
];

const JUNK_TERM_RE =
  /\b(deployment|verification|localhost|undefined|null|testid|playwright|selenium|cypress|webpack|vercel|railway)\b/i;

/** Off-topic medical noise that should not become homepage “cover next” ideas. */
const OFFTOPIC_TERM_RE =
  /\b(embolism|aneurysm|myocardial|infarction|fracture|concussion|appendectomy)\b/i;

/**
 * Keep homepage/search analytics free of bot, QA, ID, and truncated junk.
 * Used on ingest and when surfacing top searches / content ideas.
 */
export function isPublicSearchTerm(value) {
  const term = normalizeTerm(value);
  if (!term || term.length < 3 || term.length > 60) return false;
  if (!/[a-z]/i.test(term)) return false;
  if (/\d{5,}/.test(term)) return false;
  if (JUNK_TERM_RE.test(term)) return false;
  if (OFFTOPIC_TERM_RE.test(term)) return false;

  const letters = (term.match(/[a-z]/gi) || []).length;
  const digits = (term.match(/\d/g) || []).length;
  if (digits > 0 && digits >= letters) return false;

  const words = term.split(/\s+/).filter(Boolean);
  if (!words.length || words.length > 8) return false;
  if (words.some((word) => word.length > 24)) return false;

  // Truncated common education words ("manageme" -> management).
  if (words.some((word) => (
    word.length >= 5 &&
    COMPLETION_STEMS.some((full) => full.startsWith(word) && word !== full)
  ))) {
    return false;
  }

  return true;
}

export function filterPublicSearchRows(rows, termKey = 'normalized_term') {
  if (!Array.isArray(rows)) return [];
  return rows.filter((row) => isPublicSearchTerm(row?.[termKey] || row?.term || row?.label));
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
