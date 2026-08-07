import { cleanText, db, json, methodNotAllowed, parseBody } from '../../../_web-db.js';
import { requireAdmin } from '../../../_student-research-auth.js';

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return methodNotAllowed(res, ['POST']);
  }

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
