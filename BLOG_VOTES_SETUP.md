# Blog thumbs up / down (Vercel Blob: ibdpal-blob)

Votes are stored in your Blob store **`ibdpal-blob`** as:

| File in store | Purpose |
|---------------|---------|
| `blog-votes/votes.log` | Text log: `time`, `slug`, `up` or `down` |
| `blog-votes/counts.json` | Totals per blog post |

**ibdpal-blob** is a **private** Blob store. Vote files are only readable/writable via the server API using `BLOB_READ_WRITE_TOKEN` | not public URLs on the website.

---

## Fix: "Vote storage is not configured"

Creating the store under **Storage → All Databases** is not enough. You must **connect** it to the **ibdpal-website** project.

### Step A | Connect store to project

1. [Vercel Dashboard](https://vercel.com) → **Storage** → open **`ibdpal-blob`**
2. Open the **Projects** tab (not only Quickstart)
3. Click **Connect to Project**
4. Choose **`ibdpal-website`**
5. Enable **Production** and **Preview** → Connect

### Step B | Environment variables (dashboard only | never commit secrets)

1. Open **`ibdpal-website`** → **Settings** → **Environment Variables**
2. Confirm both exist for **Production** and **Preview**:
   - `BLOB_STORE_ID` (e.g. `store_…`)
   - `BLOB_READ_WRITE_TOKEN` (starts with `vercel_blob_rw_…`)
3. If you connect the store from the dashboard, Vercel usually adds these automatically. If not, paste the values from **Storage → ibdpal-blob** (not into git).
4. Do **not** put tokens in HTML, JavaScript, or commit them to GitHub.

If neither variable exists, repeat Step A.

### Step C | Redeploy

1. **ibdpal-website** → **Deployments**
2. Latest deployment → **⋯** → **Redeploy** (use **Redeploy** after connecting storage)

### Step D | Test

1. API health: https://ibdpal.org/api/blog-vote?check=1 | must show `"ok":true` and `"apiBuild":"rest-v4-private"` (if missing, Production has not picked up the latest deploy).
2. Full path: https://ibdpal.org/api/blog-vote?check=1&deep=1 (read/write like voting)
3. Open https://ibdpal.org/blog/hydration-tips-ibd  
2. Click 👍  
3. Message: **Thanks for your feedback.**

In **Storage → ibdpal-blob**, you should then see `blog-votes/votes.log`.

---

## Alternative: connect from the project

1. **ibdpal-website** → **Storage** tab  
2. **Connect Store** → select existing **`ibdpal-blob`**  
3. **Redeploy**

---

## API

- `GET /api/blog-vote?slug=hydration-tips-ibd` → `{ "up": 0, "down": 0 }`
- `POST /api/blog-vote` → `{ "slug": "hydration-tips-ibd", "vote": "up" }`

---

## Privacy

Each log line stores only timestamp, article slug, and up/down | no health data or email.
