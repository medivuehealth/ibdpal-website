# Blog thumbs up / down (Vercel Blob: ibdpal-blob)

Votes are stored in your **private** Blob store **`ibdpal-blob`** as:

| File in store | Purpose |
|---------------|---------|
| `blog-votes/votes.log` | Text log: `time`, `slug`, `up` or `down` |
| `blog-votes/counts.json` | Totals per blog post |

**Private** is correct — visitors never get a public URL to the log; only the API and your Vercel dashboard can read it.

---

## Fix: "Vote storage is not configured"

Creating the store under **Storage → All Databases** is not enough. You must **connect** it to the **ibdpal-website** project.

### Step A — Connect store to project

1. [Vercel Dashboard](https://vercel.com) → **Storage** → open **`ibdpal-blob`**
2. Open the **Projects** tab (not only Quickstart)
3. Click **Connect to Project**
4. Choose **`ibdpal-website`**
5. Enable **Production** and **Preview** → Connect

### Step B — Confirm environment variables

1. Open project **`ibdpal-website`** → **Settings** → **Environment Variables**
2. You should see at least one of:
   - `BLOB_READ_WRITE_TOKEN`, or
   - `BLOB_STORE_ID` (+ `VERCEL_OIDC_TOKEN` on deployments)

If neither exists, repeat Step A.

### Step C — Redeploy

1. **ibdpal-website** → **Deployments**
2. Latest deployment → **⋯** → **Redeploy** (use **Redeploy** after connecting storage)

### Step D — Test

1. Open https://ibdpal.org/blog/hydration-tips-ibd  
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

Each log line stores only timestamp, article slug, and up/down — no health data or email.
