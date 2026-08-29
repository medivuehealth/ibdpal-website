import crypto from 'crypto';
import { cleanText, db, json, methodNotAllowed, parseBody } from '../_web-db.js';
import { containsProfanity, profanityErrorMessage } from '../_profanity.js';
import { requireAdmin } from '../_student-research-auth.js';

const MIN_QUESTION_LEN = 15;
const MAX_QUESTION_LEN = 2000;
const MAX_ANSWER_LEN = 12000;
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

function slugify(value) {
  const base = String(value || '')
    .toLowerCase()
    .replace(/[^\w\s-]/g, ' ')
    .replace(/\s+/g, '-')
    .replace(/-+/g, '-')
    .replace(/^-|-$/g, '')
    .slice(0, 80);
  return base || 'reader-question';
}

function excerpt(text, max = 160) {
  const flat = String(text || '').replace(/\s+/g, ' ').trim();
  if (flat.length <= max) return flat;
  return flat.slice(0, max - 1).trim() + '…';
}

function publicItem(row) {
  return {
    id: row.question_id,
    slug: row.slug,
    title: row.title || excerpt(row.question_text, 90),
    question: row.question_text,
    answer: row.answer_text,
    publishedAt: row.published_at,
    askerName: row.display_name || null
  };
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

async function uniqueSlug(base, excludeId) {
  let slug = slugify(base);
  let attempt = slug;
  let n = 2;
  while (true) {
    const params = excludeId ? [attempt, excludeId] : [attempt];
    const sql = excludeId
      ? `SELECT question_id FROM ibdpal_reader_questions WHERE slug = $1 AND question_id <> $2 LIMIT 1`
      : `SELECT question_id FROM ibdpal_reader_questions WHERE slug = $1 LIMIT 1`;
    const found = await db().query(sql, params);
    if (!found.rows.length) return attempt;
    attempt = `${slug}-${n}`;
    n += 1;
  }
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

    if (containsProfanity(question)) {
      return json(res, 400, {
        success: false,
        error: profanityErrorMessage()
      });
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
        null,
        null,
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
        'Thanks. We saved your question. When we publish an answer, it will appear in Answered questions below. This is not medical advice; for urgent symptoms contact your care team.'
    });
  } catch (error) {
    console.error('reader-questions submit error', error);
    return json(res, 500, {
      success: false,
      error: 'Could not save your question. Try again later or email info@ibdpal.org.'
    });
  }
}

async function handlePublished(req, res) {
  if (req.method !== 'GET') return methodNotAllowed(res, ['GET']);
  try {
    const limit = Math.max(1, Math.min(parseInt(req.query.limit, 10) || 20, 50));
    const offset = Math.max(0, parseInt(req.query.offset, 10) || 0);
    const q = cleanText(req.query.q, 120);

    const baseWhere = `
      published_at IS NOT NULL
      AND answer_text IS NOT NULL
      AND TRIM(answer_text) <> ''
      AND slug IS NOT NULL`;

    const params = [];
    let searchClause = '';
    if (q) {
      const term = q.replace(/[%_\\]/g, '').trim();
      if (term) {
        params.push('%' + term + '%');
        searchClause = ` AND (question_text ILIKE $1 OR COALESCE(title, '') ILIKE $1 OR slug ILIKE $1)`;
      }
    }

    const countResult = await db().query(
      `SELECT COUNT(*)::int AS total FROM ibdpal_reader_questions WHERE ${baseWhere}${searchClause}`,
      params
    );
    const total = countResult.rows[0]?.total || 0;

    const listParams = [...params, limit, offset];
    const limitIdx = params.length + 1;
    const offsetIdx = params.length + 2;
    const result = await db().query(
      `SELECT question_id, question_text, title, answer_text, slug, display_name, published_at
       FROM ibdpal_reader_questions
       WHERE ${baseWhere}${searchClause}
       ORDER BY published_at DESC
       LIMIT $${limitIdx} OFFSET $${offsetIdx}`,
      listParams
    );

    return json(res, 200, {
      success: true,
      total,
      limit,
      offset,
      items: result.rows.map((row) => ({
        ...publicItem(row),
        excerpt: excerpt(row.answer_text, 180)
      }))
    });
  } catch (error) {
    console.error('reader-questions published error', error);
    return json(res, 500, { success: false, error: 'Could not load answered questions.' });
  }
}

async function handleBySlug(req, res) {
  if (req.method !== 'GET') return methodNotAllowed(res, ['GET']);
  const slug = cleanText(req.query.slug, 80);
  if (!slug) {
    return json(res, 400, { success: false, error: 'Missing slug.' });
  }
  try {
    const result = await db().query(
      `SELECT question_id, question_text, title, answer_text, slug, display_name, published_at
       FROM ibdpal_reader_questions
       WHERE slug = $1
         AND published_at IS NOT NULL
         AND answer_text IS NOT NULL
       LIMIT 1`,
      [slug]
    );
    const row = result.rows[0];
    if (!row) {
      return json(res, 404, { success: false, error: 'Answer not found.' });
    }
    return json(res, 200, { success: true, item: publicItem(row) });
  } catch (error) {
    console.error('reader-questions by-slug error', error);
    return json(res, 500, { success: false, error: 'Could not load this answer.' });
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
      `SELECT question_id, question_text, title, answer_text, slug, email, display_name,
              source, page_url, search_term, status, published_at, created_at
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
        title: row.title,
        answer: row.answer_text,
        slug: row.slug,
        email: row.email,
        name: row.display_name,
        source: row.source,
        pageUrl: row.page_url,
        searchTerm: row.search_term,
        status: row.status,
        publishedAt: row.published_at,
        createdAt: row.created_at
      }))
    });
  } catch (error) {
    console.error('reader-questions admin list error', error);
    return json(res, 500, { success: false, error: 'Could not load questions.' });
  }
}

async function handleAdminPublish(req, res) {
  if (req.method !== 'POST') return methodNotAllowed(res, ['POST']);
  if (!requireAdmin(req, res)) return;

  try {
    const body = parseBody(req);
    const id = parseInt(body.id || body.questionId, 10);
    const title = cleanText(body.title, 240);
    const answer = cleanText(body.answer || body.answerText, MAX_ANSWER_LEN);
    const slugInput = cleanText(body.slug, 80);
    const unpublish = body.publish === false || body.unpublish === true;

    if (!id) {
      return json(res, 400, { success: false, error: 'Question id is required.' });
    }

    if (unpublish) {
      await db().query(
        `UPDATE ibdpal_reader_questions
         SET published_at = NULL, status = 'reviewed', updated_at = NOW()
         WHERE question_id = $1`,
        [id]
      );
      return json(res, 200, { success: true, message: 'Answer unpublished.' });
    }

    if (!answer || answer.length < 40) {
      return json(res, 400, { success: false, error: 'Answer must be at least 40 characters.' });
    }
    if (containsProfanity(answer) || containsProfanity(title || '')) {
      return json(res, 400, { success: false, error: profanityErrorMessage() });
    }

    const existing = await db().query(
      `SELECT question_id, question_text, title, slug FROM ibdpal_reader_questions WHERE question_id = $1`,
      [id]
    );
    const row = existing.rows[0];
    if (!row) {
      return json(res, 404, { success: false, error: 'Question not found.' });
    }

    const finalTitle = title || row.title || excerpt(row.question_text, 90);
    const slug = slugInput || row.slug || (await uniqueSlug(finalTitle, id));

    const result = await db().query(
      `UPDATE ibdpal_reader_questions
       SET title = $2,
           answer_text = $3,
           slug = $4,
           status = 'answered',
           published_at = COALESCE(published_at, NOW()),
           updated_at = NOW()
       WHERE question_id = $1
       RETURNING question_id, slug, title, published_at`,
      [id, finalTitle, answer, slug]
    );

    return json(res, 200, {
      success: true,
      item: publicItem({ ...row, ...result.rows[0], answer_text: answer }),
      message: 'Answer published.',
      url: `/ask/${result.rows[0].slug}`
    });
  } catch (error) {
    console.error('reader-questions admin publish error', error);
    return json(res, 500, { success: false, error: 'Could not publish answer.' });
  }
}

export default async function handler(req, res) {
  const action = resolveAction(req);
  if (action === 'published') return handlePublished(req, res);
  if (action === 'by-slug') return handleBySlug(req, res);
  if (action === 'admin-list') return handleAdminList(req, res);
  if (action === 'admin-publish') return handleAdminPublish(req, res);
  return handleSubmit(req, res);
}
