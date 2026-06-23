CREATE TABLE IF NOT EXISTS ibdpal_web_search_events (
    event_id SERIAL PRIMARY KEY,
    term TEXT NOT NULL,
    normalized_term TEXT NOT NULL,
    source TEXT NOT NULL DEFAULT 'tools_lab',
    result_count INTEGER NOT NULL DEFAULT 0 CHECK (result_count >= 0),
    clicked_article_slug TEXT,
    clicked_article_url TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_ibdpal_web_search_events_normalized_term
    ON ibdpal_web_search_events (normalized_term);

CREATE INDEX IF NOT EXISTS idx_ibdpal_web_search_events_created_at
    ON ibdpal_web_search_events (created_at DESC);

CREATE INDEX IF NOT EXISTS idx_ibdpal_web_search_events_term_recent
    ON ibdpal_web_search_events (normalized_term, created_at DESC);
