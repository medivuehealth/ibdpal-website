import { db, json, methodNotAllowed } from '../_web-db.js';

function titleFromTerm(term) {
  const label = String(term || '').trim();
  if (!label) return 'A clearer patient guide from recent searches';
  return `${label}: questions to ask and what to track`;
}

export default async function handler(req, res) {
  if (req.method !== 'GET') {
    return methodNotAllowed(res, ['GET']);
  }

  try {
    const days = Math.max(1, Math.min(parseInt(req.query.days, 10) || 30, 90));
    const limit = Math.max(1, Math.min(parseInt(req.query.limit, 10) || 5, 10));

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
      GROUP BY normalized_term
      ORDER BY
        CASE WHEN AVG(result_count) <= 1 THEN 0 ELSE 1 END,
        search_count DESC,
        last_searched_at DESC
      LIMIT $2`,
      [days, limit]
    );

    return json(res, 200, {
      success: true,
      days,
      ideas: result.rows.map((row) => ({
        term: row.normalized_term,
        label: row.label,
        title: titleFromTerm(row.label),
        reason: Number(row.avg_result_count) <= 1
          ? 'Readers searched this but found few matching resources.'
          : 'Readers are asking about this topic often.',
        count: row.search_count
      }))
    });
  } catch (error) {
    console.error('content-ideas error', error);
    return json(res, 500, {
      success: false,
      error: 'Failed to fetch content ideas.'
    });
  }
}
