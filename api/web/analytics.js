import { db, filterPublicSearchRows, json, methodNotAllowed } from '../../lib/web-db.js';

/**
 * Shared Hobby-plan function for read-only insights analytics.
 * vercel.json rewrites map legacy paths onto ?action=.
 */
function resolveAction(req) {
  const q = String(req.query.action || '').toLowerCase();
  if (q) return q;
  const url = String(req.url || '');
  if (url.includes('content-brief')) return 'brief';
  if (url.includes('content-ideas')) return 'ideas';
  if (url.includes('search-gaps')) return 'gaps';
  if (url.includes('top-searches')) return 'top-searches';
  if (url.includes('top-content')) return 'top-content';
  return '';
}

function titleFromTerm(term) {
  const label = String(term || '').trim();
  if (!label) return 'A clearer patient guide from recent searches';
  return `${label}: questions to ask and what to track`;
}

async function handleBrief(req, res) {
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
}

async function handleIdeas(req, res) {
  const days = Math.max(1, Math.min(parseInt(req.query.days, 10) || 30, 90));
  const limit = Math.max(1, Math.min(parseInt(req.query.limit, 10) || 5, 25));
  const fetchLimit = Math.min(Math.max(limit * 4, 12), 40);

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
      AND normalized_term !~ '[0-9]{5,}'
      AND normalized_term !~* '(deployment|verification|localhost|undefined|testid|playwright|selenium|cypress)'
    GROUP BY normalized_term
    ORDER BY
      CASE WHEN AVG(result_count) <= 1 THEN 0 ELSE 1 END,
      search_count DESC,
      last_searched_at DESC
    LIMIT $2`,
    [days, fetchLimit]
  );

  const ideas = filterPublicSearchRows(result.rows)
    .slice(0, limit)
    .map((row) => ({
      term: row.normalized_term,
      label: row.label,
      title: titleFromTerm(row.label),
      reason: Number(row.avg_result_count) <= 1
        ? 'Readers searched this but found few matching resources.'
        : 'Readers are asking about this topic often.',
      count: row.search_count
    }));

  return json(res, 200, { success: true, days, ideas });
}

async function handleGaps(req, res) {
  const days = Math.max(1, Math.min(parseInt(req.query.days, 10) || 30, 90));
  const limit = Math.max(1, Math.min(parseInt(req.query.limit, 10) || 8, 25));
  const maxResults = Math.max(0, Math.min(parseInt(req.query.maxResults, 10) || 1, 5));
  const minCount = Math.max(1, Math.min(parseInt(req.query.minCount, 10) || 1, 25));
  const fetchLimit = Math.min(Math.max(limit * 4, 12), 40);

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
      AND normalized_term !~ '[0-9]{5,}'
      AND normalized_term !~* '(deployment|verification|localhost|undefined|testid|playwright|selenium|cypress)'
    GROUP BY normalized_term
    HAVING COUNT(*) >= $3
    ORDER BY search_count DESC, last_searched_at DESC
    LIMIT $4`,
    [days, maxResults, minCount, fetchLimit]
  );

  return json(res, 200, {
    success: true,
    days,
    maxResults,
    minCount,
    gaps: filterPublicSearchRows(result.rows).slice(0, limit).map((row) => ({
      term: row.normalized_term,
      label: row.label,
      count: row.search_count,
      averageResults: Number(row.avg_result_count)
    }))
  });
}

async function handleTopSearches(req, res) {
  const days = Math.max(1, Math.min(parseInt(req.query.days, 10) || 7, 90));
  const limit = Math.max(1, Math.min(parseInt(req.query.limit, 10) || 6, 25));
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
}

async function handleTopContent(req, res) {
  const ALLOWED_EVENTS = new Set(['view', 'click']);
  const days = Math.max(1, Math.min(parseInt(req.query.days, 10) || 7, 90));
  const limit = Math.max(1, Math.min(parseInt(req.query.limit, 10) || 6, 25));
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
}

export default async function handler(req, res) {
  if (req.method !== 'GET') {
    return methodNotAllowed(res, ['GET']);
  }

  const action = resolveAction(req);
  try {
    switch (action) {
      case 'brief':
        return await handleBrief(req, res);
      case 'ideas':
        return await handleIdeas(req, res);
      case 'gaps':
        return await handleGaps(req, res);
      case 'top-searches':
        return await handleTopSearches(req, res);
      case 'top-content':
        return await handleTopContent(req, res);
      default:
        return json(res, 404, { success: false, error: 'Unknown analytics action.' });
    }
  } catch (error) {
    console.error('analytics error', action, error);
    return json(res, 500, { success: false, error: 'Failed to fetch analytics.' });
  }
}
