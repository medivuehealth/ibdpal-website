CREATE TABLE IF NOT EXISTS ibdpal_reader_questions (
    question_id SERIAL PRIMARY KEY,
    question_text TEXT NOT NULL,
    email TEXT,
    display_name TEXT,
    source TEXT NOT NULL DEFAULT 'ask_page',
    page_url TEXT,
    search_term TEXT,
    ip_hash TEXT,
    user_agent TEXT,
    status TEXT NOT NULL DEFAULT 'new'
        CHECK (status IN ('new', 'reviewed', 'answered', 'spam', 'rejected')),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_ibdpal_reader_questions_created_at
    ON ibdpal_reader_questions (created_at DESC);

CREATE INDEX IF NOT EXISTS idx_ibdpal_reader_questions_status
    ON ibdpal_reader_questions (status, created_at DESC);

CREATE INDEX IF NOT EXISTS idx_ibdpal_reader_questions_source
    ON ibdpal_reader_questions (source, created_at DESC);
