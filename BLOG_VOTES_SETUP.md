# Blog thumbs up / down (server-side log)

Each blog post has 👍 / 👎 buttons. Votes are stored on Vercel as **text files in Blob storage** (not on the static site disk—Vercel cannot append to a local `.txt` file).

## Files created by voting

| Blob path | Format |
|-----------|--------|
| `blog-votes/votes.log` | Tab-separated log, one line per click: `ISO8601-time\tslug\tup\|down` |
| `blog-votes/counts.json` | Aggregated counts per blog slug |

Example `votes.log`:

```
2026-06-04T14:22:01.123Z	hydration-tips-ibd	up
2026-06-04T14:25:10.456Z	introducing-ibdpal	down
```

## One-time Vercel setup

1. [Vercel Dashboard](https://vercel.com) → **ibdpal-website** project.
2. **Storage** → **Create Database / Store** → **Blob** → create store (e.g. `ibdpal-blob`).
3. **Connect to project** — Vercel adds `BLOB_READ_WRITE_TOKEN` to the project automatically.
4. **Redeploy** production (Deployments → … → Redeploy) so the API route picks up the token.

## API

- `GET /api/blog-vote?slug=hydration-tips-ibd` → `{ "up": 3, "down": 1 }`
- `POST /api/blog-vote` with JSON `{ "slug": "hydration-tips-ibd", "vote": "up" }`

## Download the log

1. Vercel → **Storage** → your Blob store → browse `blog-votes/votes.log`.
2. Download or copy contents for analysis.

## Behavior

- One vote per browser per article (`localStorage`).
- Buttons disabled after voting.
- If Blob is not configured, users see an error when voting (counts still show 0).

## Privacy

The log stores **time, article slug, and up/down only**—no email or health data. Mention optional feedback in your privacy policy if you expand this later.
