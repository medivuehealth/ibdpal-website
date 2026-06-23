import { cleanText, contentTypeFromUrl, db, json, methodNotAllowed, parseBody, pathFromUrl, slugFromUrl } from '../_web-db.js';

const ALLOWED_SOURCES = new Set(['direct', 'tools_lab', 'patient_library', 'articles_tab', 'research_tab', 'homepage', 'site_nav']);
const ALLOWED_EVENTS = new Set(['view', 'click']);

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return methodNotAllowed(res, ['POST']);
  }

  try {
    const body = parseBody(req);
    const contentUrl = cleanText(body.contentUrl, 240);
    const pathname = pathFromUrl(contentUrl);
    const contentSlug = cleanText(body.contentSlug, 120) || slugFromUrl(contentUrl);
    const contentType = cleanText(body.contentType, 40) || contentTypeFromUrl(contentUrl);
    const source = ALLOWED_SOURCES.has(body.source) ? body.source : 'direct';
    const eventType = ALLOWED_EVENTS.has(body.eventType) ? body.eventType : 'view';
    const referrerPath = cleanText(body.referrerPath, 160);

    if (!contentUrl || !pathname || pathname === '/') {
      return json(res, 400, {
        success: false,
        error: 'A valid content URL is required.'
      });
    }

    await db().query(
      `INSERT INTO ibdpal_web_content_events (
        content_url,
        content_slug,
        content_type,
        source,
        event_type,
        referrer_path
      ) VALUES ($1, $2, $3, $4, $5, $6)`,
      [pathname, contentSlug, contentType, source, eventType, referrerPath]
    );

    return json(res, 201, { success: true });
  } catch (error) {
    console.error('content-events error', error);
    return json(res, 500, {
      success: false,
      error: 'Failed to record content event.'
    });
  }
}
