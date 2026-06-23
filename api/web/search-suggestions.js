import { db, json, methodNotAllowed } from '../_web-db.js';

const ALLOWED_SOURCES = new Set(['tools_lab', 'patient_library', 'homepage']);

export default async function handler(req, res) {
  if (req.method !== 'GET') {
    return methodNotAllowed(res, ['GET']);
  }

  try {
    const days = Math.max(1, Math.min(parseInt(req.query.days, 10) || 14, 90));
    const limit = Math.max(1, Math.min(parseInt(req.query.limit, 10) || 8, 12));
    const source = ALLOWED_SOURCES.has(req.query.source) ? req.query.source : null;
    const params = [days, limit];
    const sourceFilter = source ? 'AND source = $3' : '';
    if (source) params.push(source);

    const result = await db().query(
      `SELECT
        normalized_term,
        INITCAP(MIN(term)) AS label,
        COUNT(*)::int AS search_count,
        MAX(created_at) AS last_searched_at
      FROM ibdpal_web_search_events
      WHERE created_at >= NOW() - ($1::int * INTERVAL '1 day')
        AND clicked_article_slug IS NULL
        AND normalized_term <> ''
        ${sourceFilter}
      GROUP BY normalized_term
      ORDER BY search_count DESC, last_searched_at DESC
      LIMIT $2`,
      params
    );

    return json(res, 200, {
      success: true,
      days,
      source,
      suggestions: result.rows.map((row) => ({
        term: row.normalized_term,
        label: row.label,
        count: row.search_count
      }))
    });
  } catch (error) {
    console.error('search-suggestions error', error);
    return json(res, 500, {
      success: false,
      error: 'Failed to fetch search suggestions.'
    });
  }
}
