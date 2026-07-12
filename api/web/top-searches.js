import { db, filterPublicSearchRows, json, methodNotAllowed } from '../_web-db.js';

export default async function handler(req, res) {
  if (req.method !== 'GET') {
    return methodNotAllowed(res, ['GET']);
  }

  try {
    const days = Math.max(1, Math.min(parseInt(req.query.days, 10) || 7, 90));
    const limit = Math.max(1, Math.min(parseInt(req.query.limit, 10) || 6, 12));
    const minCount = Math.max(1, Math.min(parseInt(req.query.minCount, 10) || 3, 25));
    const fetchLimit = Math.min(Math.max(limit * 4, 12), 40);

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
        AND normalized_term !~ '[0-9]{5,}'
        AND normalized_term !~* '(deployment|verification|localhost|undefined|testid|playwright|selenium|cypress)'
      GROUP BY normalized_term
      HAVING COUNT(*) >= $2
      ORDER BY search_count DESC, last_searched_at DESC
      LIMIT $3`,
      [days, minCount, fetchLimit]
    );

    return json(res, 200, {
      success: true,
      days,
      minCount,
      searches: filterPublicSearchRows(result.rows).slice(0, limit).map((row) => ({
        term: row.normalized_term,
        label: row.label,
        count: row.search_count
      }))
    });
  } catch (error) {
    console.error('top-searches error', error);
    return json(res, 500, {
      success: false,
      error: 'Failed to fetch top searches.'
    });
  }
}
