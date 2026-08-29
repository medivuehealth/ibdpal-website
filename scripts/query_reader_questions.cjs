const { Client } = require('pg');
const fs = require('fs');
const path = require('path');

function readConfigEnv(filePath) {
  if (!fs.existsSync(filePath)) return {};
  return fs.readFileSync(filePath, 'utf8').split(/\r?\n/).reduce((values, line) => {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith('#')) return values;
    const idx = trimmed.indexOf('=');
    if (idx === -1) return values;
    values[trimmed.slice(0, idx).trim()] = trimmed.slice(idx + 1).trim();
    return values;
  }, {});
}

const cs =
  process.env.DATABASE_URL ||
  readConfigEnv(path.resolve(__dirname, '..', '..', 'ibdpal-server', 'config.env')).DATABASE_URL;

async function main() {
  const client = new Client({ connectionString: cs, ssl: { rejectUnauthorized: false } });
  await client.connect();
  const result = await client.query(
    `SELECT question_id, question_text, status, source, email, display_name,
            title, slug, published_at, created_at
     FROM ibdpal_reader_questions
     ORDER BY created_at DESC
     LIMIT 10`
  );
  console.log(JSON.stringify(result.rows, null, 2));
  await client.end();
}

main().catch((err) => {
  console.error(err.message);
  process.exit(1);
});
