# Techies design preview

## Working context
- Upstream: SerStableLad/TechiesWebsite, base branch Techies-Revamp-EM-Dash.
- Fork: cszesther/TechiesWebsite; work branch codex/techies-design-preview.
- Baseline commit c6e4186d35a37625fd285f1e8f8d3bdc2962c4c4 is the recovery point.
- Keep the live Worker, CMS database and media untouched. Review the preview before deployment.
- Run pnpm dev:isolated on localhost:4331; data, uploads and sessions are under ignored .preview/.
- This preview uses bundled reference content, not the latest live CMS snapshot.

## Completed foundation
- Inventoried the existing shared Astro templates; see PREVIEW.md.
- Added local Node/SQLite preview launcher and noindex preview metadata.
- Removed decorative arrows from public link/button templates, retaining technical content and brand artwork.
- Fixed optional null recap data crashing the member directory.
- Confirmed signed-in live admin exposes Preview, SEO, publication controls and five revisions for Roast #7. No live content changed.
- Local route checks cover homepage, events, people, posts and Roast #7; typecheck and design detector run against preview.

## Selected design work still to build
- Harvest article reading layout with Front-style In this article anchor navigation.
- Short titles; date metadata once; publication date distinct from event date.
- Header credits labelled Featuring for speakers, actual author separate in schema; LinkedIn post URL; event photo or Luma cover.
- Speaker sections retain relevant images/captions without immediately repeating the lead image.
- Maze episode rows using verified Spotify metadata and per-episode Listen links; no transcript button.
- Braintrust-style event cards aligned across each row.
- Profound-inspired progressive Polaroid collage of real event/supper photos, static/mobile alternative.
- Preserve fixed identity and existing Inter/JetBrains Mono typography roles. User rejects decorative link arrows.

## Recovery
Git tracks renderer changes; EmDash revisions track content; database/media backups protect stored records and files. A Git rollback does not restore CMS content. Hosted preview requires separate Worker/D1/R2/KV resources and is not provisioned in this checkpoint.
