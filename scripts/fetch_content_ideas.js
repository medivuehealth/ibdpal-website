const { Client } = require('pg');
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');

function readConfigEnv(filePath) {
  if (!fs.existsSync(filePath)) return {};
  return fs.readFileSync(filePath, 'utf8').split(/\r?\n/).reduce((values, line) => {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith('#')) return values;
    const idx = trimmed.indexOf('=');
    if (idx === -1) return values;
    const key = trimmed.slice(0, idx).trim();
    const value = trimmed.slice(idx + 1).trim().replace(/^["']|["']$/g, '');
    values[key] = value;
    return values;
  }, {});
}

function databaseUrl() {
  if (process.env.DATABASE_URL) return process.env.DATABASE_URL;
  const localServerEnv = path.resolve(ROOT, '..', 'ibdpal-server', 'config.env');
  return readConfigEnv(localServerEnv).DATABASE_URL || '';
}

const NOISE = /deployment|verification|test|embolism|^\d+$/i;

async function main() {
  const url = databaseUrl();
  if (!url) {
    console.error('No DATABASE_URL');
    process.exit(1);
  }
  const client = new Client({
    connectionString: url,
    ssl: url.includes('localhost') ? false : { rejectUnauthorized: false }
  });
  await client.connect();
  const result = await client.query(
    `SELECT
      normalized_term,
      INITCAP(MIN(term)) AS label,
      COUNT(*)::int AS search_count,
      AVG(result_count)::numeric(6,2) AS avg_result_count,
      MAX(created_at) AS last_searched_at
    FROM ibdpal_web_search_events
    WHERE created_at >= NOW() - INTERVAL '30 days'
      AND normalized_term <> ''
    GROUP BY normalized_term
    ORDER BY search_count DESC, last_searched_at DESC
    LIMIT 30`
  );
  await client.end();
  const ideas = result.rows.filter((row) => !NOISE.test(row.normalized_term));
  console.log(JSON.stringify(ideas, null, 2));
}

main().catch((error) => {
  console.error(error.message);
  process.exit(1);
});
