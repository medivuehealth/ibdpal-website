import crypto from 'crypto';
import { cleanText, db, json, methodNotAllowed, parseBody } from '../_web-db.js';
import { containsProfanity, profanityErrorMessage } from '../_profanity.js';
import { requireAdmin } from '../_student-research-auth.js';

const RATE_LIMIT_MAX = 5;
const INTEREST_TYPES = new Set([
  'listing',
  'underwriting',
  'clinic_materials',
  'other'
]);
const STATUSES = new Set(['new', 'reviewed', 'contacted', 'closed', 'spam']);

function resolveAction(req) {
  return cleanText(req.query.action, 40) || 'submit';
}

function clientIp(req) {
  const forwarded = req.headers['x-forwarded-for'] || req.headers['X-Forwarded-For'];
  if (forwarded) {
    return String(forwarded).split(',')[0].trim();
  }
  return req.socket?.remoteAddress || '';
}

function ipHash(req) {
  const ip = clientIp(req);
  if (!ip) return null;
  return crypto.createHash('sha256').update(ip).digest('hex').slice(0, 64);
}

function looksLikeEmail(value) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(String(value || '').trim());
}

async function isRateLimited(hash) {
  if (!hash) return false;
  const result = await db().query(
    `SELECT COUNT(*)::int AS count
     FROM ibdpal_partner_inquiries
     WHERE ip_hash = $1
       AND created_at >= NOW() - INTERVAL '1 hour'`,
    [hash]
  );
  return (result.rows[0]?.count || 0) >= RATE_LIMIT_MAX;
}

function publicMessage() {
  return 'Thanks. We saved your inquiry. MediVue reviews partner requests in the admin desk — you do not need to email us.';
}

async function handleSubmit(req, res) {
  if (req.method !== 'POST') return methodNotAllowed(res, ['POST']);

  try {
    const body = parseBody(req);
    const honeypot = cleanText(body.website || body.fax, 120);
    if (honeypot) {
      return json(res, 201, { success: true, message: publicMessage() });
    }

    const organizationName = cleanText(body.organizationName || body.organization_name, 160);
    const contactName = cleanText(body.contactName || body.contact_name, 120);
    const contactEmail = cleanText(body.contactEmail || body.contact_email, 160);
    const interestType =
      cleanText(body.interestType || body.interest_type, 40) || 'listing';
    const programUrl = cleanText(body.programUrl || body.program_url, 400);
    const message = cleanText(body.message || body.summary, 4000);
    const source = cleanText(body.source, 40) || 'media_kit';
    const pageUrl = cleanText(body.pageUrl || body.page_url, 400);
    const hash = ipHash(req);

    if (!organizationName || organizationName.length < 2) {
      return json(res, 400, {
        success: false,
        error: 'Enter your organization name.'
      });
    }
    if (!contactName || contactName.length < 2) {
      return json(res, 400, {
        success: false,
        error: 'Enter a contact name.'
      });
    }
    if (!contactEmail || !looksLikeEmail(contactEmail)) {
      return json(res, 400, {
        success: false,
        error: 'Enter a valid work email so we can reply from the partner desk.'
      });
    }
    if (!INTEREST_TYPES.has(interestType)) {
      return json(res, 400, {
        success: false,
        error: 'Choose a valid interest type.'
      });
    }
    if (!message || message.length < 20) {
      return json(res, 400, {
        success: false,
        error: 'Add a short summary (at least 20 characters) about your program or request.'
      });
    }

    const textBlob = [organizationName, contactName, message, programUrl || ''].join(' ');
    if (containsProfanity(textBlob)) {
      return json(res, 400, {
        success: false,
        error: profanityErrorMessage()
      });
    }

    if (hash && (await isRateLimited(hash))) {
      return json(res, 429, {
        success: false,
        error: 'Too many inquiries in a short time. Please wait an hour and try again.'
      });
    }

    const result = await db().query(
      `INSERT INTO ibdpal_partner_inquiries (
        organization_name, contact_name, contact_email, interest_type,
        program_url, message, source, page_url, ip_hash, user_agent
      ) VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10)
      RETURNING inquiry_id, created_at`,
      [
        organizationName,
        contactName,
        contactEmail.toLowerCase(),
        interestType,
        programUrl,
        message,
        source.slice(0, 40),
        pageUrl,
        hash,
        cleanText(req.headers['user-agent'], 300)
      ]
    );

    return json(res, 201, {
      success: true,
      id: result.rows[0].inquiry_id,
      message: publicMessage()
    });
  } catch (error) {
    console.error('partner-inquiries submit error', error);
    return json(res, 500, {
      success: false,
      error: 'Could not save your inquiry. Please try again later.'
    });
  }
}

async function handleAdminList(req, res) {
  if (req.method !== 'GET') return methodNotAllowed(res, ['GET']);
  if (!requireAdmin(req, res)) return;

  try {
    const limit = Math.max(1, Math.min(parseInt(req.query.limit, 10) || 50, 100));
    const status = cleanText(req.query.status, 20);
    const params = [];
    let where = 'TRUE';
    if (status && STATUSES.has(status)) {
      params.push(status);
      where = `status = $${params.length}`;
    }
    params.push(limit);
    const result = await db().query(
      `SELECT inquiry_id, organization_name, contact_name, contact_email, interest_type,
              program_url, message, source, page_url, status, admin_notes, created_at, updated_at
       FROM ibdpal_partner_inquiries
       WHERE ${where}
       ORDER BY created_at DESC
       LIMIT $${params.length}`,
      params
    );

    return json(res, 200, {
      success: true,
      items: result.rows.map((row) => ({
        id: row.inquiry_id,
        organizationName: row.organization_name,
        contactName: row.contact_name,
        contactEmail: row.contact_email,
        interestType: row.interest_type,
        programUrl: row.program_url,
        message: row.message,
        source: row.source,
        pageUrl: row.page_url,
        status: row.status,
        adminNotes: row.admin_notes,
        createdAt: row.created_at,
        updatedAt: row.updated_at
      }))
    });
  } catch (error) {
    console.error('partner-inquiries admin-list error', error);
    return json(res, 500, { success: false, error: 'Could not load inquiries.' });
  }
}

async function handleAdminUpdate(req, res) {
  if (req.method !== 'POST') return methodNotAllowed(res, ['POST']);
  if (!requireAdmin(req, res)) return;

  try {
    const body = parseBody(req);
    const id = parseInt(body.id || body.inquiryId || body.inquiry_id, 10);
    const status = cleanText(body.status, 20);
    const adminNotes = cleanText(body.adminNotes || body.admin_notes, 4000);

    if (!id || Number.isNaN(id)) {
      return json(res, 400, { success: false, error: 'Missing inquiry id.' });
    }
    if (!status || !STATUSES.has(status)) {
      return json(res, 400, { success: false, error: 'Invalid status.' });
    }

    const result = await db().query(
      `UPDATE ibdpal_partner_inquiries
       SET status = $2,
           admin_notes = $3,
           updated_at = NOW()
       WHERE inquiry_id = $1
       RETURNING inquiry_id, status, updated_at`,
      [id, status, adminNotes]
    );
    if (!result.rows.length) {
      return json(res, 404, { success: false, error: 'Inquiry not found.' });
    }

    return json(res, 200, {
      success: true,
      id: result.rows[0].inquiry_id,
      status: result.rows[0].status,
      updatedAt: result.rows[0].updated_at
    });
  } catch (error) {
    console.error('partner-inquiries admin-update error', error);
    return json(res, 500, { success: false, error: 'Could not update inquiry.' });
  }
}

export default async function handler(req, res) {
  const action = resolveAction(req);
  if (action === 'submit') return handleSubmit(req, res);
  if (action === 'admin-list') return handleAdminList(req, res);
  if (action === 'admin-update') return handleAdminUpdate(req, res);
  return json(res, 400, { success: false, error: 'Unknown action.' });
}
