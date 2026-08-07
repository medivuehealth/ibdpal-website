import {
  db, filterPublicSearchRows, json, methodNotAllowed, normalizeTerm
} from '../_web-db.js';

const ALLOWED_SOURCES = new Set(['tools_lab', 'patient_library', 'homepage']);

/**
 * Hobby-plan slot shared by search-suggestions and search-related
 * (rewritten via vercel.json).
 */
async function handleSuggestions(req, res) {
  const days = Math.max(1, Math.min(parseInt(req.query.days, 10) || 14, 90));
  const limit = Math.max(1, Math.min(parseInt(req.query.limit, 10) || 8, 12));
  const source = ALLOWED_SOURCES.has(req.query.source) ? req.query.source : null;
  const fetchLimit = Math.min(Math.max(limit * 4, 12), 40);
  const params = [days, fetchLimit];
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
      AND normalized_term !~ '[0-9]{5,}'
      AND normalized_term !~* '(deployment|verification|localhost|undefined|testid|playwright|selenium|cypress)'
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
    suggestions: filterPublicSearchRows(result.rows).slice(0, limit).map((row) => ({
      term: row.normalized_term,
      label: row.label,
      count: row.search_count
    }))
  });
}

async function handleRelated(req, res) {
  const term = normalizeTerm(req.query.term || '');
  const days = Math.max(1, Math.min(parseInt(req.query.days, 10) || 90, 180));
  const limit = Math.max(1, Math.min(parseInt(req.query.limit, 10) || 5, 12));

  if (term.length < 2) {
    return json(res, 400, { success: false, error: 'term is required' });
  }

  const byTerm = await db().query(
    `SELECT
      clicked_article_url AS url,
      clicked_article_slug AS slug,
      COUNT(*)::int AS click_count
    FROM ibdpal_web_search_events
    WHERE created_at >= NOW() - ($1::int * INTERVAL '1 day')
      AND clicked_article_slug IS NOT NULL
      AND clicked_article_url IS NOT NULL
      AND (
        normalized_term = $2
        OR normalized_term LIKE $2 || ' %'
        OR normalized_term LIKE '% ' || $2
        OR normalized_term LIKE '% ' || $2 || ' %'
      )
    GROUP BY clicked_article_url, clicked_article_slug
    ORDER BY click_count DESC
    LIMIT $3`,
    [days, term, limit]
  );

  const slug = String(req.query.slug || '').trim().slice(0, 120);
  let inboundSearches = [];
  if (slug) {
    const inbound = await db().query(
      `SELECT
        normalized_term,
        INITCAP(MIN(term)) AS label,
        COUNT(*)::int AS search_count
      FROM ibdpal_web_search_events
      WHERE created_at >= NOW() - ($1::int * INTERVAL '1 day')
        AND clicked_article_slug = $2
        AND normalized_term <> ''
      GROUP BY normalized_term
      ORDER BY search_count DESC
      LIMIT $3`,
      [days, slug, limit]
    );
    inboundSearches = filterPublicSearchRows(inbound.rows).map((row) => ({
      term: row.normalized_term,
      label: row.label,
      count: row.search_count
    }));
  }

  return json(res, 200, {
    success: true,
    term,
    days,
    related: byTerm.rows.map((row) => ({
      url: row.url,
      slug: row.slug,
      count: row.click_count
    })),
    inboundSearches
  });
}

export default async function handler(req, res) {
  if (req.method !== 'GET') {
    return methodNotAllowed(res, ['GET']);
  }

  const url = String(req.url || '');
  const action = String(req.query.action || '').toLowerCase();
  const isRelated = action === 'related' || url.includes('search-related');

  try {
    if (isRelated) return await handleRelated(req, res);
    return await handleSuggestions(req, res);
  } catch (error) {
    console.error(isRelated ? 'search-related error' : 'search-suggestions error', error);
    return json(res, 500, {
      success: false,
      error: isRelated
        ? 'Failed to fetch related search content.'
        : 'Failed to fetch search suggestions.'
    });
  }
}
