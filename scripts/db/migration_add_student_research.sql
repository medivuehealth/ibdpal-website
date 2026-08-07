CREATE TABLE IF NOT EXISTS ibdpal_student_research_interest (
    interest_id SERIAL PRIMARY KEY,
    full_name TEXT NOT NULL,
    email TEXT NOT NULL,
    school TEXT,
    topic TEXT,
    title TEXT NOT NULL,
    external_url TEXT,
    abstract TEXT,
    status TEXT NOT NULL DEFAULT 'new',
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_ibdpal_student_research_interest_created
    ON ibdpal_student_research_interest (created_at DESC);

CREATE INDEX IF NOT EXISTS idx_ibdpal_student_research_interest_email
    ON ibdpal_student_research_interest (email);

CREATE TABLE IF NOT EXISTS ibdpal_student_researchers (
    researcher_id SERIAL PRIMARY KEY,
    email TEXT NOT NULL UNIQUE,
    full_name TEXT NOT NULL,
    school TEXT,
    password_hash TEXT NOT NULL,
    password_salt TEXT NOT NULL,
    session_token TEXT,
    session_expires_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_ibdpal_student_researchers_session
    ON ibdpal_student_researchers (session_token);

CREATE TABLE IF NOT EXISTS ibdpal_student_submissions (
    submission_id SERIAL PRIMARY KEY,
    researcher_id INTEGER NOT NULL REFERENCES ibdpal_student_researchers(researcher_id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    abstract TEXT NOT NULL,
    topics TEXT[] NOT NULL DEFAULT '{}',
    external_url TEXT,
    status TEXT NOT NULL DEFAULT 'draft',
    admin_notes TEXT,
    reviewed_at TIMESTAMPTZ,
    published_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    CONSTRAINT ibdpal_student_submissions_status_chk
        CHECK (status IN ('draft', 'submitted', 'approved', 'rejected'))
);

CREATE INDEX IF NOT EXISTS idx_ibdpal_student_submissions_status
    ON ibdpal_student_submissions (status, updated_at DESC);

CREATE INDEX IF NOT EXISTS idx_ibdpal_student_submissions_researcher
    ON ibdpal_student_submissions (researcher_id, updated_at DESC);

CREATE TABLE IF NOT EXISTS ibdpal_student_submission_events (
    event_id SERIAL PRIMARY KEY,
    submission_id INTEGER NOT NULL REFERENCES ibdpal_student_submissions(submission_id) ON DELETE CASCADE,
    event_type TEXT NOT NULL,
    actor TEXT NOT NULL DEFAULT 'system',
    note TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_ibdpal_student_submission_events_submission
    ON ibdpal_student_submission_events (submission_id, created_at DESC);
