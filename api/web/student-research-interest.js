import { cleanText, db, json, methodNotAllowed, parseBody } from '../_web-db.js';

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return methodNotAllowed(res, ['POST']);
  }

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
