import crypto from 'crypto';
import { cleanText, db, json, methodNotAllowed, parseBody } from '../_web-db.js';
import { containsProfanity, profanityErrorMessage } from '../_profanity.js';
import { requireAdmin } from '../_student-research-auth.js';

const MIN_QUESTION_LEN = 15;
const MAX_QUESTION_LEN = 2000;
const RATE_LIMIT_WINDOW_MS = 60 * 60 * 1000;
const RATE_LIMIT_MAX = 5;

function resolveAction(req) {
  return cleanText(req.query.action, 40) || 'submit';
}

function clientIp(req) {
  const forwarded = req.headers['x-forwarded-for'] || req.headers['X-Forwarded-For'];
  if (forwarded) {
    return String(forwarded).split(',')[0].trim();
  }
  return req.socket?.remoteAddress || '';
}

function ipHash(req) {
  const ip = clientIp(req);
  if (!ip) return null;
  return crypto.createHash('sha256').update(ip).digest('hex').slice(0, 64);
}

async function isRateLimited(hash) {
  if (!hash) return false;
  const result = await db().query(
    `SELECT COUNT(*)::int AS count
     FROM ibdpal_reader_questions
     WHERE ip_hash = $1
       AND created_at >= NOW() - INTERVAL '1 hour'`,
    [hash]
  );
  return (result.rows[0]?.count || 0) >= RATE_LIMIT_MAX;
}

async function handleSubmit(req, res) {
  if (req.method !== 'POST') return methodNotAllowed(res, ['POST']);

  try {
    const body = parseBody(req);
    const honeypot = cleanText(body.website || body.company, 120);
    if (honeypot) {
      return json(res, 201, {
        success: true,
        message: 'Thanks. We received your question and will review it.'
      });
    }

    const question = cleanText(body.question || body.text, MAX_QUESTION_LEN);
    const email = cleanText(body.email, 160);
    const displayName = cleanText(body.displayName || body.name, 120);
    const source = cleanText(body.source, 40) || 'ask_page';
    const pageUrl = cleanText(body.pageUrl || body.page_url, 400);
    const searchTerm = cleanText(body.searchTerm || body.search_term, 120);
    const hash = ipHash(req);

    if (!question || question.length < MIN_QUESTION_LEN) {
      return json(res, 400, {
        success: false,
        error: `Enter at least ${MIN_QUESTION_LEN} characters so we understand your question.`
      });
    }

    if (containsProfanity(question) || containsProfanity(displayName || '')) {
      return json(res, 400, {
        success: false,
        error: profanityErrorMessage()
      });
    }

    if (email && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
      return json(res, 400, { success: false, error: 'Enter a valid email address or leave it blank.' });
    }

    if (hash && (await isRateLimited(hash))) {
      return json(res, 429, {
        success: false,
        error: 'Too many questions in a short time. Please wait an hour or email info@ibdpal.org.'
      });
    }

    const result = await db().query(
      `INSERT INTO ibdpal_reader_questions (
        question_text, email, display_name, source, page_url, search_term, ip_hash, user_agent
      ) VALUES ($1, $2, $3, $4, $5, $6, $7, $8)
      RETURNING question_id, created_at`,
      [
        question,
        email ? email.toLowerCase() : null,
        displayName,
        source.slice(0, 40),
        pageUrl,
        searchTerm,
        hash,
        cleanText(req.headers['user-agent'], 300)
      ]
    );

    return json(res, 201, {
      success: true,
      id: result.rows[0].question_id,
      message:
        'Thanks. We saved your question. We cannot reply to every submission, but it helps us know what to write next. This is not medical advice; for urgent symptoms contact your care team.'
    });
  } catch (error) {
    console.error('reader-questions submit error', error);
    return json(res, 500, {
      success: false,
      error: 'Could not save your question. Try again later or email info@ibdpal.org.'
    });
  }
}

async function handleAdminList(req, res) {
  if (req.method !== 'GET') return methodNotAllowed(res, ['GET']);
  if (!requireAdmin(req, res)) return;

  try {
    const limit = Math.max(1, Math.min(parseInt(req.query.limit, 10) || 50, 200));
    const status = cleanText(req.query.status, 20);
    const params = [limit];
    let where = '';
    if (status) {
      where = ' WHERE status = $2';
      params.push(status);
    }

    const result = await db().query(
      `SELECT question_id, question_text, email, display_name, source, page_url,
              search_term, status, created_at
       FROM ibdpal_reader_questions
       ${where}
       ORDER BY created_at DESC
       LIMIT $1`,
      params
    );

    return json(res, 200, {
      success: true,
      questions: result.rows.map((row) => ({
        id: row.question_id,
        question: row.question_text,
        email: row.email,
        name: row.display_name,
        source: row.source,
        pageUrl: row.page_url,
        searchTerm: row.search_term,
        status: row.status,
        createdAt: row.created_at
      }))
    });
  } catch (error) {
    console.error('reader-questions admin list error', error);
    return json(res, 500, { success: false, error: 'Could not load questions.' });
  }
}

export default async function handler(req, res) {
  const action = resolveAction(req);
  if (action === 'admin-list') return handleAdminList(req, res);
  return handleSubmit(req, res);
}
