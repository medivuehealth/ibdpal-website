import { db, filterPublicSearchRows, json, methodNotAllowed, normalizeTerm } from '../_web-db.js';

/**
 * Articles readers clicked after searching a term ("Because people searched X").
 */
export default async function handler(req, res) {
  if (req.method !== 'GET') {
    return methodNotAllowed(res, ['GET']);
  }

  try {
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

    // Also: if this request is for an article slug, show terms that led here.
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
  } catch (error) {
    console.error('search-related error', error);
    return json(res, 500, {
      success: false,
      error: 'Failed to fetch related search content.'
    });
  }
}
