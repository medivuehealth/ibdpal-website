import { cleanText, db, json, methodNotAllowed, parseBody } from '../../_web-db.js';
import {
  normalizeTopics,
  requireResearcher
} from '../../_student-research-auth.js';

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

export default async function handler(req, res) {
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
