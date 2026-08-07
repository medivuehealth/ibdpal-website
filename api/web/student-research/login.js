import { cleanText, db, json, methodNotAllowed, parseBody } from '../../_web-db.js';
import { newSessionToken, sessionExpiry, verifyPassword } from '../../_student-research-auth.js';

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return methodNotAllowed(res, ['POST']);
  }

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
