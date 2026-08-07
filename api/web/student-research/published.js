import { db, json, methodNotAllowed } from '../../_web-db.js';
import { publicSubmission } from '../../_student-research-auth.js';

export default async function handler(req, res) {
  if (req.method !== 'GET') {
    return methodNotAllowed(res, ['GET']);
  }

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
