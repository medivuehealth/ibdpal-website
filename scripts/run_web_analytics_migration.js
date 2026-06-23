const { Client } = require('pg');
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const MIGRATIONS = [
  {
    file: path.join(ROOT, 'scripts', 'db', 'migration_add_ibdpal_web_search_events.sql'),
    tableName: 'ibdpal_web_search_events'
  },
  {
    file: path.join(ROOT, 'scripts', 'db', 'migration_add_ibdpal_web_content_events.sql'),
    tableName: 'ibdpal_web_content_events'
  }
];

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

async function verifyTable(client, tableName) {
  const tableResult = await client.query(
    `SELECT table_name
     FROM information_schema.tables
     WHERE table_schema = $1 AND table_name = $2`,
    ['public', tableName]
  );

  if (tableResult.rows.length === 0) {
    throw new Error(`${tableName} was not found after migration.`);
  }

  const indexResult = await client.query(
    `SELECT indexname
     FROM pg_indexes
     WHERE schemaname = $1 AND tablename = $2
     ORDER BY indexname`,
    ['public', tableName]
  );

  console.log(`Verified table: ${tableName}`);
  console.log('Verified indexes:');
  indexResult.rows.forEach((row) => {
    console.log(`- ${row.indexname}`);
  });
}

async function main() {
  const connectionString = databaseUrl();
  if (!connectionString) {
    console.error('DATABASE_URL is not set. Set it in the environment or keep ../ibdpal-server/config.env available locally.');
    process.exit(1);
  }

  const client = new Client({
    connectionString,
    ssl: {
      rejectUnauthorized: false
    }
  });

  try {
    console.log('Connecting to hosted database...');
    await client.connect();
    console.log('Connected. Running ibdpal_web analytics migrations...');

    for (const migration of MIGRATIONS) {
      await client.query(fs.readFileSync(migration.file, 'utf8'));
      await verifyTable(client, migration.tableName);
    }

    console.log('Web analytics migrations completed successfully.');
  } catch (error) {
    console.error('Web analytics migration failed:', error.message);
    process.exitCode = 1;
  } finally {
    await client.end();
    console.log('Database connection closed.');
  }
}

main();
