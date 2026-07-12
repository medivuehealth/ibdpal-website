import {
  cleanText, db, isPublicSearchTerm, json, methodNotAllowed,
  normalizeTerm, parseBody, slugFromUrl
} from '../_web-db.js';

const ALLOWED_SOURCES = new Set(['tools_lab', 'patient_library', 'homepage']);

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return methodNotAllowed(res, ['POST']);
  }

  try {
    const body = parseBody(req);
    const term = cleanText(body.term, 120);
    const normalizedTerm = normalizeTerm(body.normalizedTerm || term);
    const source = ALLOWED_SOURCES.has(body.source) ? body.source : 'tools_lab';
    const resultCount = Number.isFinite(Number(body.resultCount))
      ? Math.max(0, Math.min(Number(body.resultCount), 100))
      : 0;
    const clickedArticleUrl = cleanText(body.clickedArticleUrl, 240);
    const clickedArticleSlug = cleanText(body.clickedArticleSlug, 120) || slugFromUrl(clickedArticleUrl);

    if (!term || normalizedTerm.length < 2) {
      return json(res, 400, {
        success: false,
        error: 'Search term must be at least 2 characters.'
      });
    }

    // Soft-drop bot/QA/truncated junk so it never surfaces on the homepage.
    if (!isPublicSearchTerm(normalizedTerm)) {
      return json(res, 201, { success: true, ignored: true });
    }

    await db().query(
      `INSERT INTO ibdpal_web_search_events (
        term,
        normalized_term,
        source,
        result_count,
        clicked_article_slug,
        clicked_article_url
      ) VALUES ($1, $2, $3, $4, $5, $6)`,
      [term, normalizedTerm, source, resultCount, clickedArticleSlug, clickedArticleUrl]
    );

    return json(res, 201, { success: true });
  } catch (error) {
    console.error('search-events error', error);
    return json(res, 500, {
      success: false,
      error: 'Failed to record search event.'
    });
  }
}
