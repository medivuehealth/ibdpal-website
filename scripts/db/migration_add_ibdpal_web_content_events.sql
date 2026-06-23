CREATE TABLE IF NOT EXISTS ibdpal_web_content_events (
    event_id SERIAL PRIMARY KEY,
    content_url TEXT NOT NULL,
    content_slug TEXT,
    content_type TEXT NOT NULL DEFAULT 'page',
    source TEXT NOT NULL DEFAULT 'direct',
    event_type TEXT NOT NULL DEFAULT 'view',
    referrer_path TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_ibdpal_web_content_events_content_slug
    ON ibdpal_web_content_events (content_slug);

CREATE INDEX IF NOT EXISTS idx_ibdpal_web_content_events_created_at
    ON ibdpal_web_content_events (created_at DESC);

CREATE INDEX IF NOT EXISTS idx_ibdpal_web_content_events_type_recent
    ON ibdpal_web_content_events (content_type, created_at DESC);

CREATE INDEX IF NOT EXISTS idx_ibdpal_web_content_events_url_recent
    ON ibdpal_web_content_events (content_url, created_at DESC);
