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

## Hosted preview decision, 30 October 2026
- User questions enabling R2. R2 is needed by the current hosted media adapter, not Astro itself. Do not enable R2 or accept billing/terms on the user's behalf.
- Cloudflare account cszesther has isolated D1 database techies-design-preview (60bf5ec5-aaa6-4800-99a8-920e955fa105), empty at verification. No R2 bucket or hosted preview deployment created.
- Pending choice: hosted read-only design snapshot with bundled photos and local CMS editing, or fully editable hosted EmDash with a supported persistent media backend. Do not claim a static snapshot tests hosted CMS uploads/auth/revisions.
- Parallel design plan completed in DESIGN-REBUILD-PLAN.md; implementation of the new shared templates remains pending. User approves changing Base, PostCard, article template and typography.
- Mobile monitoring: existing local Codex chat is Audit Techies website design; official Codex Remote documentation describes steering connected-computer chats from mobile. This is separate from normal ChatGPT project conversation history; do not create a replacement chat without a request.

## Hosted baseline ready
- User chose hosted design snapshot with bundled photos; no R2 service required. URL and recovery version are recorded in PREVIEW.md.
- Export/build/deploy/check scripts implemented; 17 public routes and 30 photos hosted independently. Source typecheck and desktop/mobile checks passed.
- Saved local database and public/media checkpoint; hosted version 0eb7e138-041b-48db-bb47-e313d8f98c20 is the pre-redesign recovery deployment.
- D1 created earlier remains unused; static preview binds no database, R2 or sessions. No resources deleted.
- Beginning first article prototype next; larger home/podcast/gallery stages remain in DESIGN-REBUILD-PLAN.md.
