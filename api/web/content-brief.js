import { db, filterPublicSearchRows, json, methodNotAllowed } from '../_web-db.js';

/**
 * Weekly content brief for /insights: searches, hard gaps, top pages.
 */
export default async function handler(req, res) {
  if (req.method !== 'GET') {
    return methodNotAllowed(res, ['GET']);
  }

  try {
    const days = Math.max(1, Math.min(parseInt(req.query.days, 10) || 7, 90));
    const limit = Math.max(1, Math.min(parseInt(req.query.limit, 10) || 10, 25));
    const fetchLimit = Math.min(Math.max(limit * 3, 15), 40);

    const [topSearches, hardGaps, topViews, topClicks, searchVolume] = await Promise.all([
      db().query(
        `SELECT
          normalized_term,
          INITCAP(MIN(term)) AS label,
          COUNT(*)::int AS search_count,
          AVG(result_count)::numeric(6,2) AS avg_result_count,
          MAX(created_at) AS last_searched_at
        FROM ibdpal_web_search_events
        WHERE created_at >= NOW() - ($1::int * INTERVAL '1 day')
          AND normalized_term <> ''
        GROUP BY normalized_term
        ORDER BY search_count DESC, last_searched_at DESC
        LIMIT $2`,
        [days, fetchLimit]
      ),
      db().query(
        `SELECT
          normalized_term,
          INITCAP(MIN(term)) AS label,
          COUNT(*)::int AS search_count,
          AVG(result_count)::numeric(6,2) AS avg_result_count,
          MAX(created_at) AS last_searched_at
        FROM ibdpal_web_search_events
        WHERE created_at >= NOW() - ($1::int * INTERVAL '1 day')
          AND normalized_term <> ''
          AND result_count = 0
        GROUP BY normalized_term
        ORDER BY search_count DESC, last_searched_at DESC
        LIMIT $2`,
        [days, fetchLimit]
      ),
      db().query(
        `SELECT content_url, content_slug, content_type, COUNT(*)::int AS event_count
         FROM ibdpal_web_content_events
         WHERE created_at >= NOW() - ($1::int * INTERVAL '1 day')
           AND event_type = 'view'
           AND content_url <> ''
         GROUP BY content_url, content_slug, content_type
         ORDER BY event_count DESC
         LIMIT $2`,
        [days, limit]
      ),
      db().query(
        `SELECT content_url, content_slug, content_type, COUNT(*)::int AS event_count
         FROM ibdpal_web_content_events
         WHERE created_at >= NOW() - ($1::int * INTERVAL '1 day')
           AND event_type = 'click'
           AND content_url <> ''
         GROUP BY content_url, content_slug, content_type
         ORDER BY event_count DESC
         LIMIT $2`,
        [days, limit]
      ),
      db().query(
        `SELECT
           COUNT(*)::int AS searches,
           COUNT(*) FILTER (WHERE result_count = 0)::int AS zero_result_searches,
           COUNT(DISTINCT normalized_term)::int AS unique_terms
         FROM ibdpal_web_search_events
         WHERE created_at >= NOW() - ($1::int * INTERVAL '1 day')`,
        [days]
      )
    ]);

    const mapSearch = (rows) =>
      filterPublicSearchRows(rows).slice(0, limit).map((row) => ({
        term: row.normalized_term,
        label: row.label,
        count: row.search_count,
        averageResults: Number(row.avg_result_count)
      }));

    const mapContent = (rows) =>
      rows.map((row) => ({
        url: row.content_url,
        slug: row.content_slug,
        type: row.content_type,
        count: row.event_count
      }));

    const volume = searchVolume.rows[0] || {};

    return json(res, 200, {
      success: true,
      days,
      generatedAt: new Date().toISOString(),
      summary: {
        searches: volume.searches || 0,
        zeroResultSearches: volume.zero_result_searches || 0,
        uniqueTerms: volume.unique_terms || 0
      },
      topSearches: mapSearch(topSearches.rows),
      hardGaps: mapSearch(hardGaps.rows),
      topViews: mapContent(topViews.rows),
      topClicks: mapContent(topClicks.rows)
    });
  } catch (error) {
    console.error('content-brief error', error);
    return json(res, 500, {
      success: false,
      error: 'Failed to build content brief.'
    });
  }
}
