import { cleanText, db, json, methodNotAllowed, parseBody } from '../../_web-db.js';
import { hashPassword, newSessionToken, sessionExpiry } from '../../_student-research-auth.js';

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return methodNotAllowed(res, ['POST']);
  }

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
      return json(res, 409, { success: false, error: 'An account with that email already exists. Sign in instead.' });
    }
    console.error('student-research register error', error);
    return json(res, 500, { success: false, error: 'Registration failed.' });
  }
}
