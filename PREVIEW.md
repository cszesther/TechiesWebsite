# Isolated design preview

Base branch: `Techies-Revamp-EM-Dash`.
Baseline commit: `c6e4186d35a37625fd285f1e8f8d3bdc2962c4c4`.
Fork: https://github.com/cszesther/TechiesWebsite
Design branch: `codex/techies-design-preview`.

## Run locally

```sh
pnpm install --frozen-lockfile
pnpm dev:isolated
```

Open http://localhost:4331 and http://localhost:4331/_emdash/admin.
Complete the local setup using the bundled content. This is an independent
development CMS, not a copy of the latest live database.

The launcher forces the Node adapter, project-local `.preview/techies.db`,
`.preview/uploads` and `.preview/sessions`. It uses no Cloudflare D1, R2 or
session KV bindings. Public preview pages emit `noindex, nofollow`. Keep the
server on loopback; noindex is not access control. Do not use `pnpm deploy`
for the preview: the original Wrangler configuration still targets production.

## Existing templates to extend

| File | Shared responsibility | Agreed direction |
| --- | --- | --- |
| `src/layouts/Base.astro` | Header, footer, metadata | Existing brand; plain links without decorative arrows |
| `src/components/PageSections.astro` and `PageSection.astro` | Editable page-builder sections | Reuse for homepage and new pages |
| `src/components/PostCard.astro` | Homepage, post and taxonomy cards | Short title, date once, aligned actions |
| `src/pages/posts/[slug].astro` | Every blog article | Harvest reading layout, Front contents navigation |
| `src/components/HangoutCollage.astro` | Event/supper photos | Polaroid frames and progressive reveal |
| `src/pages/events.astro` | Event formats and calendar | Aligned Braintrust-inspired cards |
| `src/styles/theme.css` | Shared typography and colours | Existing Inter/JetBrains Mono roles |

The podcast currently uses a generic CTA section. Maze-style episode rows need
a dedicated episode block/data model using verified Spotify metadata and links;
do not fill it with invented episodes. Article speaker credits and LinkedIn
post URL need explicit CMS fields; the existing source URL is a legacy recap URL.

## Version history and recovery

- Commit code changes in small groups. Review before merging or deploying.
- Retain the baseline commit; Git can recover the old renderer without changing CMS content.
- CMS revisions preserve article content changes, separately from Git.
- Back up the database and media together before any production content/schema migration.
- A fully editable Cloudflare-hosted CMS preview must have its own Worker, D1 database, supported persistent media storage (R2 in the current config), session KV,
  encryption/auth settings and site URL. Keep mail/integrations and maintenance
  schedules disabled unless explicitly needed. Do not bind it to production resources.
- Validate one representative article and a rollback in the isolated preview first.
- Production publication and deployment require review of the finished preview.

The local launcher provisions no hosted resources. A separate empty preview D1 database has since been created; no hosted preview deployment or R2 bucket exists.

A read-only hosted design snapshot can instead bundle existing photos as static files and avoid R2. It can test public layouts on mobile, but cannot test hosted CMS editing, uploads, sign-in or content revisions. The independent local CMS remains available for those checks. Hosting approach is pending the user's selection.

## Verified checkpoint

The initial checkpoint adds the isolated launcher, noindex preview metadata and
plain public links. The shared design templates listed above are inventoried;
the Harvest/Front article, Maze episode list and photo animation are not yet rebuilt.

Run `node scripts/check-isolated-preview.mjs` with the preview running to verify
the local database/media directories, page responses, noindex and link labels.
The initial seed exposed a nullable member-recaps bug; the shared formatter now
accepts null and the check covers it. No live CMS entries were edited.

## Hosted baseline (30 October 2026)

User selected a read-only hosted design preview with bundled photos.
- URL: https://techies-design-preview.esther-speakeasy.workers.dev
- Cloudflare version: `0eb7e138-041b-48db-bb47-e313d8f98c20`.
- `wrangler.preview.jsonc` deploys only static assets; no D1/R2/KV/live CMS bindings. The original `wrangler.jsonc` is unchanged.
- `pnpm build:design-preview` builds the Node adapter, briefly serves the local seeded CMS on port 4333, then exports 17 linked public pages and 30 referenced photos into ignored `.preview/site`. Run `pnpm dev:isolated` and finish local setup first for a fresh checkout.
- Export refuses query-pagination and submission forms instead of publishing silently broken interactions. Native profile dialogs remain functional. No CMS/admin/API is exported.
- `pnpm deploy:design-preview` publishes this snapshot; `python3 scripts/check-design-preview.py` checks the hosted pages/assets, noindex and absent CMS/API. Updates are manual, not automatically deployed by Git pushes.
- Bundled content is a reference seed, not a fresh live export. The Luma feed returned 429 during capture; the hosted snapshot shows the useful calendar fallback and direct Luma link. It is not a live-updating calendar.
- Two stale hardcoded supper-image fallback references returned unavailable responses and were removed; the two real seed supper photos remain.
- Checkpoint in ignored `.preview/checkpoints/hosted-baseline-2026-10-30/` contains a SQLite backup, a public snapshot archive including its referenced media, and version metadata. No sessions/credentials are backed up there.
- Restore preview deployment: `pnpm exec wrangler rollback 0eb7e138-041b-48db-bb47-e313d8f98c20 --config wrangler.preview.jsonc`. Git code recovery and local CMS data recovery are separate.
- Verified 17 page responses and 36 referenced assets, X-Robots-Tag, one H1, no localhost asset URLs, absent CMS/API routes; source typecheck 55 files clean; source plus five-route rendered desktop/mobile detectors passed. Browser inspected mobile/home/article; homepage width 390px matches document width.

See DESIGN-REBUILD-PLAN.md for the staged template overhaul.
