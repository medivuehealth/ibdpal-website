#!/usr/bin/env node
/**
 * Submit URLs to IndexNow (Bing + partners).
 *
 * Usage:
 *   node scripts/submit_indexnow.js
 *   node scripts/submit_indexnow.js https://www.ibdpal.org/newly-diagnosed
 *   node scripts/submit_indexnow.js --sitemap
 *
 * After deploy, key must be live at:
 *   https://www.ibdpal.org/a50b1f808a1d4c41b89fc4b35d46418a.txt
 */
const fs = require('fs');
const path = require('path');

const INDEXNOW_KEY = 'a50b1f808a1d4c41b89fc4b35d46418a';
const HOST = 'www.ibdpal.org';
const KEY_LOCATION = `https://${HOST}/${INDEXNOW_KEY}.txt`;
const ENDPOINT = 'https://api.indexnow.org/indexnow';
const ROOT = path.join(__dirname, '..');

function urlsFromSitemap() {
  const xml = fs.readFileSync(path.join(ROOT, 'sitemap.xml'), 'utf8');
  const locs = [...xml.matchAll(/<loc>([^<]+)<\/loc>/g)].map((m) => m[1].trim());
  return locs.filter((u) => u.startsWith('https://'));
}

async function submit(urlList) {
  const chunkSize = 100;
  for (let i = 0; i < urlList.length; i += chunkSize) {
    const chunk = urlList.slice(i, i + chunkSize);
    const body = {
      host: HOST,
      key: INDEXNOW_KEY,
      keyLocation: KEY_LOCATION,
      urlList: chunk,
    };
    process.stdout.write(`Submitting ${chunk.length} URLs (${i + 1}-${i + chunk.length} of ${urlList.length})... `);
    const resp = await fetch(ENDPOINT, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json; charset=utf-8' },
      body: JSON.stringify(body),
    });
    const text = await resp.text();
    console.log(`${resp.status} ${text || '(empty)'}`);
    if (resp.status !== 200 && resp.status !== 202) {
      process.exitCode = 1;
      break;
    }
  }
}

async function main() {
  const args = process.argv.slice(2);
  let urls = [];
  if (args.includes('--sitemap') || args.length === 0) {
    urls = urlsFromSitemap();
    console.log(`Loaded ${urls.length} URLs from sitemap.xml`);
  } else {
    urls = args.filter((a) => !a.startsWith('--'));
  }
  if (!urls.length) {
    console.error('No URLs to submit');
    process.exit(1);
  }
  await submit(urls);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
