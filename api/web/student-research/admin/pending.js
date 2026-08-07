import { db, json, methodNotAllowed, parseBody } from '../../../_web-db.js';
import { requireAdmin } from '../../../_student-research-auth.js';

export default async function handler(req, res) {
  req.body = parseBody(req);

  if (req.method === 'GET') {
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

  return methodNotAllowed(res, ['GET']);
}
