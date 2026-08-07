import crypto from 'crypto';
import { cleanText, db, json } from './web-db.js';

const SESSION_DAYS = 21;

export function hashPassword(password, salt = crypto.randomBytes(16).toString('hex')) {
  const hash = crypto.scryptSync(String(password), salt, 64).toString('hex');
  return { hash, salt };
}

export function verifyPassword(password, hash, salt) {
  try {
    const next = crypto.scryptSync(String(password), salt, 64).toString('hex');
    const a = Buffer.from(hash, 'hex');
    const b = Buffer.from(next, 'hex');
    if (a.length !== b.length) return false;
    return crypto.timingSafeEqual(a, b);
  } catch {
    return false;
  }
}

export function newSessionToken() {
  return crypto.randomBytes(32).toString('hex');
}

export function sessionExpiry() {
  return new Date(Date.now() + SESSION_DAYS * 24 * 60 * 60 * 1000);
}

export function bearerToken(req) {
  const header = req.headers.authorization || req.headers.Authorization || '';
  const match = String(header).match(/^Bearer\s+(.+)$/i);
  if (match) return match[1].trim();
  const bodyToken = cleanText(req.body?.sessionToken || req.body?.token, 128);
  return bodyToken;
}

export async function requireResearcher(req, res) {
  const token = bearerToken(req);
  if (!token) {
    json(res, 401, { success: false, error: 'Sign in required.' });
    return null;
  }
  const result = await db().query(
    `SELECT researcher_id, email, full_name, school, session_expires_at
     FROM ibdpal_student_researchers
     WHERE session_token = $1`,
    [token]
  );
  const row = result.rows[0];
  if (!row || !row.session_expires_at || new Date(row.session_expires_at) < new Date()) {
    json(res, 401, { success: false, error: 'Session expired. Sign in again.' });
    return null;
  }
  return row;
}

export function requireAdmin(req, res) {
  const expected = process.env.ADMIN_TOKEN || process.env.STUDENT_RESEARCH_ADMIN_TOKEN;
  if (!expected) {
    json(res, 503, { success: false, error: 'Admin token is not configured.' });
    return false;
  }
  const provided =
    cleanText(req.headers['x-admin-token'], 200) ||
    cleanText(bearerToken(req), 200) ||
    cleanText(req.body?.adminToken, 200);
  if (!provided || provided !== expected) {
    json(res, 401, { success: false, error: 'Admin authorization failed.' });
    return false;
  }
  return true;
}

export function normalizeTopics(value) {
  if (Array.isArray(value)) {
    return value.map((t) => cleanText(t, 60)).filter(Boolean).slice(0, 8);
  }
  if (typeof value === 'string') {
    return value
      .split(',')
      .map((t) => cleanText(t, 60))
      .filter(Boolean)
      .slice(0, 8);
  }
  return [];
}

export function publicSubmission(row) {
  return {
    id: row.submission_id,
    title: row.title,
    abstract: row.abstract,
    topics: row.topics || [],
    externalUrl: row.external_url,
    publishedAt: row.published_at,
    authorName: row.full_name,
    school: row.school
  };
}
