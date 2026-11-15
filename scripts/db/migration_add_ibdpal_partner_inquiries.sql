CREATE TABLE IF NOT EXISTS ibdpal_partner_inquiries (
    inquiry_id SERIAL PRIMARY KEY,
    organization_name TEXT NOT NULL,
    contact_name TEXT NOT NULL,
    contact_email TEXT NOT NULL,
    interest_type TEXT NOT NULL DEFAULT 'listing'
        CHECK (interest_type IN (
            'listing',
            'underwriting',
            'clinic_materials',
            'other'
        )),
    program_url TEXT,
    message TEXT NOT NULL,
    source TEXT NOT NULL DEFAULT 'media_kit',
    page_url TEXT,
    ip_hash TEXT,
    user_agent TEXT,
    status TEXT NOT NULL DEFAULT 'new'
        CHECK (status IN ('new', 'reviewed', 'contacted', 'closed', 'spam')),
    admin_notes TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_ibdpal_partner_inquiries_created_at
    ON ibdpal_partner_inquiries (created_at DESC);

CREATE INDEX IF NOT EXISTS idx_ibdpal_partner_inquiries_status
    ON ibdpal_partner_inquiries (status, created_at DESC);

CREATE INDEX IF NOT EXISTS idx_ibdpal_partner_inquiries_interest
    ON ibdpal_partner_inquiries (interest_type, created_at DESC);
