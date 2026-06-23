import { db, json, methodNotAllowed } from '../_web-db.js';

const ALLOWED_EVENTS = new Set(['view', 'click']);

export default async function handler(req, res) {
  if (req.method !== 'GET') {
    return methodNotAllowed(res, ['GET']);
  }

  try {
    const days = Math.max(1, Math.min(parseInt(req.query.days, 10) || 7, 90));
    const limit = Math.max(1, Math.min(parseInt(req.query.limit, 10) || 6, 12));
    const minCount = Math.max(1, Math.min(parseInt(req.query.minCount, 10) || 3, 25));
    const eventType = ALLOWED_EVENTS.has(req.query.eventType) ? req.query.eventType : 'view';

    const result = await db().query(
      `SELECT
        content_url,
        content_slug,
        content_type,
        COUNT(*)::int AS event_count,
        MAX(created_at) AS last_seen_at
      FROM ibdpal_web_content_events
      WHERE created_at >= NOW() - ($1::int * INTERVAL '1 day')
        AND event_type = $2
        AND content_url <> ''
      GROUP BY content_url, content_slug, content_type
      HAVING COUNT(*) >= $3
      ORDER BY event_count DESC, last_seen_at DESC
      LIMIT $4`,
      [days, eventType, minCount, limit]
    );

    return json(res, 200, {
      success: true,
      days,
      minCount,
      eventType,
      content: result.rows.map((row) => ({
        url: row.content_url,
        slug: row.content_slug,
        type: row.content_type,
        count: row.event_count
      }))
    });
  } catch (error) {
    console.error('top-content error', error);
    return json(res, 500, {
      success: false,
      error: 'Failed to fetch top content.'
    });
  }
}
