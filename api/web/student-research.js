import { cleanText, db, json, methodNotAllowed, parseBody } from '../_lib/web-db.js';
import {
  hashPassword,
  newSessionToken,
  normalizeTopics,
  publicSubmission,
  requireAdmin,
  requireResearcher,
  sessionExpiry,
  verifyPassword
} from '../_lib/student-research-auth.js';

/**
 * Single Hobby-plan function for all Student Research routes.
 * Rewrites in vercel.json map legacy paths onto ?action=.
 */
function resolveAction(req) {
  const q = cleanText(req.query.action, 40);
  if (q) return q;
  const url = String(req.url || '');
  if (url.includes('student-research-interest') || url.includes('action=interest')) {
    return 'interest';
  }
  const match = url.match(/student-research\/(?:admin\/)?([a-z-]+)/i);
  if (!match) return '';
  if (url.includes('/admin/pending')) return 'admin-pending';
  if (url.includes('/admin/review')) return 'admin-review';
  return match[1];
}

async function handleInterest(req, res) {
  if (req.method !== 'POST') return methodNotAllowed(res, ['POST']);
  try {
    const body = parseBody(req);
    const fullName = cleanText(body.fullName || body.name, 120);
    const email = cleanText(body.email, 160);
    const school = cleanText(body.school, 160);
    const topic = cleanText(body.topic, 80);
    const title = cleanText(body.title, 240);
    const externalUrl = cleanText(body.externalUrl || body.url, 400);
    const abstract = cleanText(body.abstract, 4000);

    if (!fullName || !email || !title) {
      return json(res, 400, {
        success: false,
        error: 'Name, email, and title are required.'
      });
    }
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
      return json(res, 400, { success: false, error: 'Enter a valid email address.' });
    }

    const result = await db().query(
      `INSERT INTO ibdpal_student_research_interest (
        full_name, email, school, topic, title, external_url, abstract
      ) VALUES ($1, $2, $3, $4, $5, $6, $7)
      RETURNING interest_id, created_at`,
      [fullName, email.toLowerCase(), school, topic, title, externalUrl, abstract]
    );

    return json(res, 201, {
      success: true,
      id: result.rows[0].interest_id,
      message: 'Thanks. We received your proposal and will review it manually.'
    });
  } catch (error) {
    console.error('student-research-interest error', error);
    return json(res, 500, {
      success: false,
      error: 'Could not save your proposal. Try again later or email info@ibdpal.org.'
    });
  }
}

async function handleLogin(req, res) {
  if (req.method !== 'POST') return methodNotAllowed(res, ['POST']);
  try {
    const body = parseBody(req);
    const email = cleanText(body.email, 160);
    const password = String(body.password || '');
    if (!email || !password) {
      return json(res, 400, { success: false, error: 'Email and password are required.' });
    }

    const found = await db().query(
      `SELECT researcher_id, email, full_name, school, password_hash, password_salt
       FROM ibdpal_student_researchers WHERE email = $1`,
      [email.toLowerCase()]
    );
    const row = found.rows[0];
    if (!row || !verifyPassword(password, row.password_hash, row.password_salt)) {
      return json(res, 401, { success: false, error: 'Invalid email or password.' });
    }

    const token = newSessionToken();
    const expires = sessionExpiry();
    await db().query(
      `UPDATE ibdpal_student_researchers
       SET session_token = $1, session_expires_at = $2, updated_at = NOW()
       WHERE researcher_id = $3`,
      [token, expires, row.researcher_id]
    );

    return json(res, 200, {
      success: true,
      sessionToken: token,
      expiresAt: expires.toISOString(),
      researcher: {
        researcher_id: row.researcher_id,
        email: row.email,
        full_name: row.full_name,
        school: row.school
      }
    });
  } catch (error) {
    console.error('student-research login error', error);
    return json(res, 500, { success: false, error: 'Sign-in failed.' });
  }
}

async function handleRegister(req, res) {
  if (req.method !== 'POST') return methodNotAllowed(res, ['POST']);
  try {
    const body = parseBody(req);
    const fullName = cleanText(body.fullName || body.name, 120);
    const emailRaw = cleanText(body.email, 160);
    const school = cleanText(body.school, 160);
    const password = String(body.password || '');

    if (!fullName || !emailRaw || password.length < 8) {
      return json(res, 400, {
        success: false,
        error: 'Name, email, and a password of at least 8 characters are required.'
      });
    }
    const email = emailRaw.toLowerCase();
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
      return json(res, 400, { success: false, error: 'Enter a valid email address.' });
    }

    const { hash, salt } = hashPassword(password);
    const token = newSessionToken();
    const expires = sessionExpiry();

    const result = await db().query(
      `INSERT INTO ibdpal_student_researchers (
        email, full_name, school, password_hash, password_salt, session_token, session_expires_at
      ) VALUES ($1, $2, $3, $4, $5, $6, $7)
      RETURNING researcher_id, email, full_name, school`,
      [email, fullName, school, hash, salt, token, expires]
    );

    return json(res, 201, {
      success: true,
      sessionToken: token,
      expiresAt: expires.toISOString(),
      researcher: result.rows[0]
    });
  } catch (error) {
    if (String(error.message || '').includes('unique') || error.code === '23505') {
      return json(res, 409, {
        success: false,
        error: 'An account with that email already exists. Sign in instead.'
      });
    }
    console.error('student-research register error', error);
    return json(res, 500, { success: false, error: 'Registration failed.' });
  }
}

async function listMine(researcherId) {
  const result = await db().query(
    `SELECT submission_id, title, abstract, topics, external_url, status, admin_notes,
            created_at, updated_at, published_at, reviewed_at
     FROM ibdpal_student_submissions
     WHERE researcher_id = $1
     ORDER BY updated_at DESC`,
    [researcherId]
  );
  return result.rows;
}

async function handleSubmissions(req, res) {
  req.body = parseBody(req);

  if (req.method === 'GET') {
    try {
      const researcher = await requireResearcher(req, res);
      if (!researcher) return;
      const items = await listMine(researcher.researcher_id);
      return json(res, 200, { success: true, items });
    } catch (error) {
      console.error('student-research submissions GET', error);
      return json(res, 500, { success: false, error: 'Could not load submissions.' });
    }
  }

  if (req.method === 'POST') {
    try {
      const researcher = await requireResearcher(req, res);
      if (!researcher) return;
      const body = req.body;
      const title = cleanText(body.title, 240);
      const abstract = cleanText(body.abstract, 4000);
      const externalUrl = cleanText(body.externalUrl || body.url, 400);
      const topics = normalizeTopics(body.topics || body.topic);
      const status = body.submit ? 'submitted' : 'draft';

      if (!title || !abstract) {
        return json(res, 400, { success: false, error: 'Title and abstract are required.' });
      }

      const result = await db().query(
        `INSERT INTO ibdpal_student_submissions (
          researcher_id, title, abstract, topics, external_url, status
        ) VALUES ($1, $2, $3, $4, $5, $6)
        RETURNING submission_id, title, abstract, topics, external_url, status, created_at, updated_at`,
        [researcher.researcher_id, title, abstract, topics, externalUrl, status]
      );
      const row = result.rows[0];
      await db().query(
        `INSERT INTO ibdpal_student_submission_events (submission_id, event_type, actor, note)
         VALUES ($1, $2, $3, $4)`,
        [row.submission_id, status === 'submitted' ? 'submitted' : 'draft_created', 'researcher', null]
      );
      return json(res, 201, { success: true, item: row });
    } catch (error) {
      console.error('student-research submissions POST', error);
      return json(res, 500, { success: false, error: 'Could not save submission.' });
    }
  }

  if (req.method === 'PATCH') {
    try {
      const researcher = await requireResearcher(req, res);
      if (!researcher) return;
      const body = req.body;
      const submissionId = Number(body.submissionId || body.id);
      if (!Number.isFinite(submissionId)) {
        return json(res, 400, { success: false, error: 'submissionId is required.' });
      }

      const existing = await db().query(
        `SELECT * FROM ibdpal_student_submissions
         WHERE submission_id = $1 AND researcher_id = $2`,
        [submissionId, researcher.researcher_id]
      );
      const current = existing.rows[0];
      if (!current) {
        return json(res, 404, { success: false, error: 'Submission not found.' });
      }
      if (current.status === 'approved') {
        return json(res, 409, { success: false, error: 'Approved submissions cannot be edited.' });
      }

      const title = cleanText(body.title, 240) || current.title;
      const abstract = cleanText(body.abstract, 4000) || current.abstract;
      const externalUrl =
        body.externalUrl !== undefined || body.url !== undefined
          ? cleanText(body.externalUrl || body.url, 400)
          : current.external_url;
      const topics =
        body.topics !== undefined || body.topic !== undefined
          ? normalizeTopics(body.topics || body.topic)
          : current.topics;
      let status = current.status;
      if (body.submit) status = 'submitted';
      if (body.status === 'draft') status = 'draft';

      const result = await db().query(
        `UPDATE ibdpal_student_submissions
         SET title = $1, abstract = $2, topics = $3, external_url = $4, status = $5, updated_at = NOW()
         WHERE submission_id = $6
         RETURNING submission_id, title, abstract, topics, external_url, status, updated_at`,
        [title, abstract, topics, externalUrl, status, submissionId]
      );
      await db().query(
        `INSERT INTO ibdpal_student_submission_events (submission_id, event_type, actor)
         VALUES ($1, $2, 'researcher')`,
        [submissionId, status === 'submitted' ? 'submitted' : 'updated']
      );
      return json(res, 200, { success: true, item: result.rows[0] });
    } catch (error) {
      console.error('student-research submissions PATCH', error);
      return json(res, 500, { success: false, error: 'Could not update submission.' });
    }
  }

  return methodNotAllowed(res, ['GET', 'POST', 'PATCH']);
}

async function handlePublished(req, res) {
  if (req.method !== 'GET') return methodNotAllowed(res, ['GET']);
  try {
    const result = await db().query(
      `SELECT s.submission_id, s.title, s.abstract, s.topics, s.external_url, s.published_at,
              r.full_name, r.school
       FROM ibdpal_student_submissions s
       JOIN ibdpal_student_researchers r ON r.researcher_id = s.researcher_id
       WHERE s.status = 'approved'
       ORDER BY COALESCE(s.published_at, s.updated_at) DESC
       LIMIT 50`
    );
    return json(res, 200, {
      success: true,
      items: result.rows.map(publicSubmission)
    });
  } catch (error) {
    console.error('student-research published error', error);
    return json(res, 500, { success: false, error: 'Could not load published research.' });
  }
}

async function handleAdminPending(req, res) {
  req.body = parseBody(req);
  if (req.method !== 'GET') return methodNotAllowed(res, ['GET']);
  try {
    if (!requireAdmin(req, res)) return;
    const result = await db().query(
      `SELECT s.submission_id, s.title, s.abstract, s.topics, s.external_url, s.status,
              s.admin_notes, s.created_at, s.updated_at,
              r.full_name, r.email, r.school
       FROM ibdpal_student_submissions s
       JOIN ibdpal_student_researchers r ON r.researcher_id = s.researcher_id
       WHERE s.status = 'submitted'
       ORDER BY s.updated_at ASC
       LIMIT 100`
    );
    const interest = await db().query(
      `SELECT interest_id, full_name, email, school, topic, title, external_url, abstract, status, created_at
       FROM ibdpal_student_research_interest
       WHERE status = 'new'
       ORDER BY created_at ASC
       LIMIT 100`
    );
    return json(res, 200, {
      success: true,
      submissions: result.rows,
      interest: interest.rows
    });
  } catch (error) {
    console.error('admin pending error', error);
    return json(res, 500, { success: false, error: 'Could not load pending items.' });
  }
}

async function handleAdminReview(req, res) {
  if (req.method !== 'POST') return methodNotAllowed(res, ['POST']);
  try {
    const body = parseBody(req);
    req.body = body;
    if (!requireAdmin(req, res)) return;

    const action = cleanText(body.action, 40);
    const notes = cleanText(body.adminNotes || body.notes, 1000);

    if (action === 'interest-dismiss' || action === 'interest-approve-note') {
      const interestId = Number(body.interestId);
      if (!Number.isFinite(interestId)) {
        return json(res, 400, { success: false, error: 'interestId is required.' });
      }
      const status = action === 'interest-dismiss' ? 'dismissed' : 'reviewed';
      await db().query(
        `UPDATE ibdpal_student_research_interest SET status = $1 WHERE interest_id = $2`,
        [status, interestId]
      );
      return json(res, 200, { success: true, interestId, status });
    }

    const submissionId = Number(body.submissionId || body.id);
    if (!Number.isFinite(submissionId)) {
      return json(res, 400, { success: false, error: 'submissionId is required.' });
    }
    if (action !== 'approve' && action !== 'reject') {
      return json(res, 400, { success: false, error: 'action must be approve or reject.' });
    }

    const status = action === 'approve' ? 'approved' : 'rejected';
    const result = await db().query(
      `UPDATE ibdpal_student_submissions
       SET status = $1,
           admin_notes = $2,
           reviewed_at = NOW(),
           published_at = CASE WHEN $1 = 'approved' THEN NOW() ELSE published_at END,
           updated_at = NOW()
       WHERE submission_id = $3 AND status = 'submitted'
       RETURNING submission_id, status, published_at`,
      [status, notes, submissionId]
    );
    if (!result.rows.length) {
      return json(res, 404, { success: false, error: 'Submitted item not found.' });
    }
    await db().query(
      `INSERT INTO ibdpal_student_submission_events (submission_id, event_type, actor, note)
       VALUES ($1, $2, 'admin', $3)`,
      [submissionId, status, notes]
    );
    return json(res, 200, { success: true, item: result.rows[0] });
  } catch (error) {
    console.error('admin review error', error);
    return json(res, 500, { success: false, error: 'Review action failed.' });
  }
}

export default async function handler(req, res) {
  const action = resolveAction(req);
  switch (action) {
    case 'interest':
      return handleInterest(req, res);
    case 'login':
      return handleLogin(req, res);
    case 'register':
      return handleRegister(req, res);
    case 'submissions':
      return handleSubmissions(req, res);
    case 'published':
      return handlePublished(req, res);
    case 'admin-pending':
    case 'pending':
      return handleAdminPending(req, res);
    case 'admin-review':
    case 'review':
      return handleAdminReview(req, res);
    default:
      return json(res, 404, {
        success: false,
        error: 'Unknown student-research action.'
      });
  }
}
