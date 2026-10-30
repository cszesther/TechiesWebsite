# Techies implementation chat handoff

## Collaboration boundary
Esther requested separate chats on 30 October 2026: the original Audit Techies website design chat owns design planning/approval; the new implementation chat owns code, testing, preview deployment and recovery. Do not perform additional redesign implementation merely from this inventory. Read the context and wait for a specific approved design specification. Do not duplicate design exploration in the implementation chat or edit the same source concurrently.

Implementation chat created: Techies website implementation, ID 01a18c92-f769-77a0-a876-2b48a3622672. Read-only orientation completed; no files changed; waiting for approved specification.

## Start here
- Read AGENTS.md, PROJECT.md, PREVIEW.md, DESIGN-SYSTEM-AUDIT.md and DESIGN-REBUILD-PLAN.md from this repo. Follow referenced skills when implementation is actually assigned.
- Checkout: /Users/esthertan/.codex/.chatgpt-projects/g-p-6a83b796ec488191a8fef107c95316f7/techies-website . Parent is a ChatGPT project mirror; sources/ is read-only.
- Fork: cszesther/TechiesWebsite, branch codex/techies-design-preview. Current application checkpoint d077a64c380d50701a30dc790ee5848d0030ff12. Verify working tree and refs before edits; planning documentation may be newer/local.
- Upstream SerStableLad/TechiesWebsite, base Techies-Revamp-EM-Dash. No merge or production deployment without approval of the concrete result.

## Preview and recovery
- Hosted static design preview: https://techies-design-preview.esther-speakeasy.workers.dev . The esther-speakeasy portion is the Cloudflare account hostname, not a shared SpeakEasy app/backend.
- Current article prototype Cloudflare version c3674662-ca74-46f7-915c-fb084d564b6c. Baseline code 431037d1656a5d590341416ac91bbc1f0969c416; baseline hosted version 0eb7e138-041b-48db-bb47-e313d8f98c20.
- User chose no R2: bundled photos and static public HTML. CMS editing stays in isolated local Node/SQLite preview at localhost:4331. Hosted snapshot has no live/CMS/database bindings and noindex. Content is reference seed, not live export; publication dates are import dates, Luma feed captured its fallback.
- Use pnpm build:design-preview and deploy:design-preview only for the authorised static preview. Original pnpm deploy/wrangler.jsonc target the live environment; do not use them.
- Backups live in ignored .preview/checkpoints/hosted-baseline-2026-10-30, including database, full uploads and public artifact. Git and CMS recovery are separate. Do not delete resources/data as cleanup without explicit approval.
- GitHub connector writes to the fork; CLI gh token was invalid. Do not expose tokens or reuse credentials from other projects. Existing unused preview D1 is documented in PROJECT.md.

## Agreed direction awaiting canonical specification
Preserve supplied official logo/colours and real photography; plain action labels without decorative arrows. Broad Base/PostCard/article/typography overhaul is allowed, but new values/layouts are still being planned. Selected references: Harvest + Front article/contents; Braintrust aligned event cards; Maze podcast rows with exact Spotify episode links/no transcript; Profound Polaroid reveal with static/mobile/reduced-motion layout. Speakers are Featuring credits, not automatically schema authors. In this article is semantic navigation, not special AEO schema. Never invent episode or event facts.

## Existing prototype and checks
Shared article already has shorter imported titles, automatic contents, source-derived speaker links, labelled dates and non-destructive immediate lead suppression. Optional LinkedIn rendering awaits a real CMS field/verified recap URL; source_url is a legacy recap URL. UI shared text colours changed in prototype; audit labels them. The shell/home/podcast/gallery/full CMS authoring changes remain pending.

After approved code changes, run relevant typecheck/build/helper checks and required source plus desktop/mobile rendered checks against the actual preview. Inspect real screenshots, not only detector output; fix findings in a batch with a bounded confirmation pass. Preserve EmDash field/route/edit metadata contracts. Document exactly what changed, evidence, limitations and recovery checkpoint in PROJECT.md.
