ALTER TABLE ibdpal_reader_questions
    ADD COLUMN IF NOT EXISTS title TEXT,
    ADD COLUMN IF NOT EXISTS answer_text TEXT,
    ADD COLUMN IF NOT EXISTS slug TEXT,
    ADD COLUMN IF NOT EXISTS published_at TIMESTAMPTZ,
    ADD COLUMN IF NOT EXISTS updated_at TIMESTAMPTZ;

CREATE UNIQUE INDEX IF NOT EXISTS idx_ibdpal_reader_questions_slug
    ON ibdpal_reader_questions (slug)
    WHERE slug IS NOT NULL;

CREATE INDEX IF NOT EXISTS idx_ibdpal_reader_questions_published
    ON ibdpal_reader_questions (published_at DESC NULLS LAST)
    WHERE published_at IS NOT NULL;

-- Seed first reader Q&A (calprotectin / getting worse) when not present
INSERT INTO ibdpal_reader_questions (
    question_text,
    title,
    answer_text,
    slug,
    source,
    status,
    published_at,
    created_at,
    updated_at
)
SELECT
    'Does my calprotectin number mean I am getting worse if I only have one test so far?',
    'Does my calprotectin number mean I am getting worse?',
    E'A single fecal calprotectin result tells you how much intestinal inflammation your clinician saw in that stool sample on that day. It does not, by itself, prove you are getting worse compared with last month.\n\nGetting worse usually means one of three things: your symptoms are escalating (more urgency, blood, pain, weight loss), your calprotectin is rising compared with your prior tests, or your scope or imaging looks more active than before. If this is your first calprotectin since diagnosis, there may be no earlier number to compare yet.\n\nA high calprotectin often means inflammation is present. That can match an active flare, but it can also appear when you are newly diagnosed and starting treatment. Your team uses the number together with how you feel, your exam, and sometimes colonoscopy or calprotectin trends over time.\n\nWhat to ask at your next visit: Is this level high for your lab reference range? Do we repeat calprotectin in a few weeks? Should we adjust medicine now or wait for another data point? How do my symptoms this week fit with this result?\n\nTrack symptoms in a simple log for one to two weeks. Pair numbers with stool frequency, blood, urgency, and fatigue so your appointment reflects trends, not only the lab printout.\n\nRelated education: Reading IBD labs article, high calprotectin what next, and newly diagnosed first 30 days on IBDPal.',
    'calprotectin-one-result-getting-worse',
    'seed',
    'answered',
    NOW(),
    NOW(),
    NOW()
WHERE NOT EXISTS (
    SELECT 1 FROM ibdpal_reader_questions WHERE slug = 'calprotectin-one-result-getting-worse'
);
