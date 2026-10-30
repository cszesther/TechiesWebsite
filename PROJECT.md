# Techies design preview

## Chat responsibilities
- This original chat is now design planning and approval only. Code implementation is assigned to Techies website implementation (01a18c92-f769-77a0-a876-2b48a3622672), a fresh chat requested by the user. It completed read-only orientation and is waiting for the approved specification. See IMPLEMENTATION-HANDOFF.md.
- DESIGN-SYSTEM-AUDIT.md inventories current source, including prototype differences; it is not an approved replacement specification. No further application changes during the design-system audit.

## Current state, 30 October 2026
- Upstream: SerStableLad/TechiesWebsite, base Techies-Revamp-EM-Dash.
- Fork: cszesther/TechiesWebsite; branch codex/techies-design-preview.
- Hosted read-only preview: https://techies-design-preview.esther-speakeasy.workers.dev . User explicitly selected bundled photos and local CMS editing instead of enabling R2.
- Current hosted version: c3674662-ca74-46f7-915c-fb084d564b6c (first article prototype).
- Baseline code checkpoint: 431037d1656a5d590341416ac91bbc1f0969c416. Baseline hosted version: 0eb7e138-041b-48db-bb47-e313d8f98c20. Original upstream recovery commit: c6e4186d35a37625fd285f1e8f8d3bdc2962c4c4.
- Live Techies Worker/CMS untouched. Do not run the original pnpm deploy for preview work.
- Local CMS: pnpm dev:isolated, http://localhost:4331; SQLite, uploads and sessions under ignored .preview/. Content is a public reference seed, not a current live CMS export. Seed publication dates are import dates.

## Completed and verified
- Hosted snapshot: 17 public pages, 30 referenced photos; no D1/R2/KV/CMS bindings, no hosted admin/API. Existing empty preview D1 techies-design-preview (60bf5ec5-aaa6-4800-99a8-920e955fa105) is unused; no resources deleted.
- scripts/build-design-preview.mjs and export-design-preview.py produce the snapshot from the isolated production Node build. wrangler.preview.jsonc deploys it. package scripts build:design-preview and deploy:design-preview are manual, not Git-triggered.
- Article prototype extends posts/[slug].astro with Harvest/Front reading layout, automatic In this article anchors, shorter imported Roast titles, Featuring credits from existing speaker profile links and separate publication/event dates.
- PostCard uses the same short-title helper. Theme retains Inter/JetBrains Mono with warm cream headings and readable body colour.
- Immediate duplicate lead image is suppressed only in public presentation; original content and edit metadata remain. Later speaker photos remain. Existing BlogPosting JSON-LD is retained (one block inspected); no special AEO schema added.
- Optional LinkedIn recap renderer exists but no CMS field migration/actual recap URLs supplied yet, so the action is omitted. Legacy source_url keeps its original meaning. No live/schema/content edits.
- Decorative public link/button arrows removed. Existing null member-recaps crash fixed. Two unavailable hardcoded supper-photo fallbacks removed; real seed supper images remain.
- Checks: 58 Astro files typecheck clean; Node production build passed with existing campaign dynamic-import/chunk warnings; article helper checks passed; all eight exported articles' contents targets verified. Hosted 17 routes/36 assets, noindex headers, one H1 and absent CMS/API passed. Five-route rendered desktop/mobile detector checks passed. Browser tested mobile and desktop article, contents click and 390/1280px widths without overflow.
- Earlier live admin inspection confirmed EmDash 1.2.0 Preview/SEO/byline/revision controls and five Roast #7 revisions. Restore itself has not been exercised. No admin publication/save/restore performed.

## Remaining rebuild plan
See DESIGN-REBUILD-PLAN.md for component boundaries, authoring contract, additive fields and review gates.
- Shared Base header/footer/mobile navigation and supplied official logo treatment; homepage/event-first composition.
- Braintrust-style equal-height event cards and final PostCard visual treatment.
- Maze podcast episode rows using verified Spotify episode metadata and exact Listen links; no transcript action.
- Profound-style progressive Polaroid gallery with static/mobile/reduced-motion alternatives.
- Preview-only CMS fields for speaker credits, actual LinkedIn recap URL, image captions and podcast entries; disposable draft authoring/revision tests before any production migration.
- Choose a real main event photo/Luma cover; verify original publication dates from source before importing live content. Shorten repeated excerpt boilerplate through editorial review.
- Keep fixed identity and Inter/JetBrains Mono; user rejects decorative arrows. Speakers are not automatically schema authors. In this article is semantic navigation, not special AI-search markup.

## Recovery and monitoring
- See PREVIEW.md for exact rollback command. Ignored .preview/checkpoints/hosted-baseline-2026-10-30 contains SQLite backup, complete uploads archive, public snapshot archive and version metadata. Git alone does not recover CMS data.
- The hosted snapshot captures the Luma 429 fallback; it does not refresh calendar data or accept submissions. It has noindex and a visible preview notice; it is not access-protected or production-ready.
- User confirmed this chat is visible on mobile. Keep work in Audit Techies website design; no replacement chat/handoff needed. Hosted preview links work independently of the local dev server.
