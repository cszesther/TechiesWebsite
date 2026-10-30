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
- A hosted preview must have its own Worker, D1 database, R2 bucket, session KV,
  encryption/auth settings and site URL. Keep mail/integrations and maintenance
  schedules disabled unless explicitly needed. Do not bind it to production resources.
- Validate one representative article and a rollback in the isolated preview first.
- Production publication and deployment require review of the finished preview.

No hosted preview resources are provisioned by this document or the local launcher.

## Verified checkpoint

The initial checkpoint adds the isolated launcher, noindex preview metadata and
plain public links. The shared design templates listed above are inventoried;
the Harvest/Front article, Maze episode list and photo animation are not yet rebuilt.

Run `node scripts/check-isolated-preview.mjs` with the preview running to verify
the local database/media directories, page responses, noindex and link labels.
The initial seed exposed a nullable member-recaps bug; the shared formatter now
accepts null and the check covers it. No live CMS entries were edited.
