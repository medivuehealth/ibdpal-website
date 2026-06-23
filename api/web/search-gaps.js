import { db, json, methodNotAllowed } from '../_web-db.js';

export default async function handler(req, res) {
  if (req.method !== 'GET') {
    return methodNotAllowed(res, ['GET']);
  }

  try {
    const days = Math.max(1, Math.min(parseInt(req.query.days, 10) || 30, 90));
    const limit = Math.max(1, Math.min(parseInt(req.query.limit, 10) || 8, 12));
    const maxResults = Math.max(0, Math.min(parseInt(req.query.maxResults, 10) || 1, 5));
    const minCount = Math.max(1, Math.min(parseInt(req.query.minCount, 10) || 1, 25));

    const result = await db().query(
      `SELECT
        normalized_term,
        INITCAP(MIN(term)) AS label,
        COUNT(*)::int AS search_count,
        AVG(result_count)::numeric(6,2) AS avg_result_count,
        MAX(created_at) AS last_searched_at
      FROM ibdpal_web_search_events
      WHERE created_at >= NOW() - ($1::int * INTERVAL '1 day')
        AND clicked_article_slug IS NULL
        AND normalized_term <> ''
        AND result_count <= $2
      GROUP BY normalized_term
      HAVING COUNT(*) >= $3
      ORDER BY search_count DESC, last_searched_at DESC
      LIMIT $4`,
      [days, maxResults, minCount, limit]
    );

    return json(res, 200, {
      success: true,
      days,
      maxResults,
      minCount,
      gaps: result.rows.map((row) => ({
        term: row.normalized_term,
        label: row.label,
        count: row.search_count,
        averageResults: Number(row.avg_result_count)
      }))
    });
  } catch (error) {
    console.error('search-gaps error', error);
    return json(res, 500, {
      success: false,
      error: 'Failed to fetch search gaps.'
    });
  }
}
