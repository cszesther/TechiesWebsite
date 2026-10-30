# Techies Astro template rebuild

Planning baseline: 30 October 2026. Work on `codex/techies-design-preview` in the `cszesther/TechiesWebsite` fork. Hosted baseline and a recovery checkpoint precede substantial UI changes. Hosting choice is pending: read-only design snapshot with bundled photos, or fully editable hosted CMS with isolated persistent media. The local CMS remains isolated. This document is a plan, not a claim that the new layouts are implemented.

## Direction and boundaries

The user has approved overhauling the shared layout, PostCard, article template and typography. Keep the fixed Techies identity, supplied logo artwork, existing event artwork, natural-colour photographs, Inter and JetBrains Mono. The supplied official square logo takes precedence over older guide examples; preserve its proportions and colours instead of synthesising a text substitute or cropping it into a new lockup.

The experience should lead with the next event and show the people and practical technical discussions behind it. Keep real content, links, CMS editing, readable server-rendered HTML and existing public URLs. Reference layout structure, not another site's palette or copy. Public links/buttons have no decorative arrows. Native admin controls remain EmDash/Kumo.

| Surface | Decision | Source |
| --- | --- | --- |
| Articles | Reading column plus adjacent contents navigation; short title, explicit credits and images near relevant discussion | [Harvest](https://mobbin.com/sites/sections/d8b28f9f-a640-4d0e-95a7-db737d105f1e), [Front](https://front.com/blog/ai-agents-teammates-launch) |
| Podcast | Visible episode rows with artwork, topic, available metadata and Listen on Spotify | [Maze](https://mobbin.com/sites/sections/d554b7ef-05fd-4809-ac98-b3032398d8b0) |
| Event formats | Topic/person-led visual cards, equal top/bottom edges and action baselines per desktop row | [Braintrust](https://mobbin.com/sites/sections/2211c3b6-e574-429a-84ca-82909e0cb07b) |
| Community photos | Polaroid frames accumulating around a readable central statement over a short scroll sequence | [Profound](https://www.tryprofound.com/careers) |

## Proposed page composition

Homepage: compact shared navigation → existing tagline with a real community visual → next event → event formats → event/supper photo section → recent articles → podcast episodes → concise community/about material → footer. A next event may sit beside the hero on wide screens and immediately below it on mobile. Keep the calendar fallback independent of the external feed.

Hero: one primary action. Show event title/date/venue with RSVP on Luma when a verified event is published; otherwise Follow our Luma calendar. An optional Explore our event formats text link serves undecided visitors. About remains in navigation. Measure outbound intent separately from completed registrations; no promised conversion lift.

Article: back link → short H1 → concise introduction → Featuring speaker names/profile links → publication date (event date separately labelled when different) → LinkedIn icon with View the LinkedIn recap → one main event photo/official cover → body and In this article navigation → credits, related articles, next-event action. Use an actual recap-post URL, not a LinkedIn share dialog.

Desktop article body uses a left contents column and a reading column around 65–75 characters; mobile puts the complete contents list above the body. Keep navigation directly visible rather than introducing a new accordion. Include major speaker/project sections in contents; add subsection nesting only if the real article needs it. Stable anchors derive from Portable Text block keys, with readable labels; rendering and contents use the same ID helper. No empty contents block for short posts.

## Shared system and component boundaries

| Existing file | Rebuild responsibility |
| --- | --- |
| `src/styles/theme.css` | Semantic colour/type/spacing roles; global reading, buttons, grids, links and focus rules |
| `src/layouts/Base.astro` | Header/footer, mobile navigation, official identity, consistent page shell and preview metadata |
| `src/components/PostCard.astro` | Same card on homepage/archive/taxonomy pages; short title, one date, selective excerpt, equal image slot and aligned actions |
| `src/pages/posts/[slug].astro` | Header, real publication/event metadata, speaker credits, lead image, body/contents layout and optional LinkedIn recap link |
| `src/components/PageSection.astro` and `PageSections.astro` | Continue rendering existing CMS page blocks; route new podcast block without replacing the page-builder system |
| `src/pages/events.astro` | Aligned event-format composition; next events more prominent; preserve calendar and recap routes |
| `src/components/HangoutCollage.astro` | Complete Polaroid composition; use CMS media references instead of hardcoded live media IDs |

Add an `ArticleContents` component and one article-content utility only where the shared renderer needs them. Add a `PodcastEpisodes` component for the new CMS block. Reuse Image, PortableText and existing Link/LinkedIn SVG patterns; no new UI framework or second CMS/template engine. Keep campaign forms, operational controls and member-directory behaviour intact while checking their shared typography/navigation.

Typography starting contract: Inter 700–800 for display/article H1 (hero 40–64px, article 36–48px responsive), section headings 28–36px, article H2 28–32px, H3 22–24px, reading text 18px/1.7, general body 16–18px, metadata/captions 14–16px. Use JetBrains Mono only for real code and short technical identifiers. Map these to named roles, not per-post overrides. Headings use off-white, body uses readable off-white/grey, metadata supporting grey, orange for actions. Verify actual contrast; preserve incident red and artwork-specific colours in their existing roles.

## Minimum additive CMS model

Use existing content fields unless a separate editorial fact needs its own field. Verify exact field/API syntax against installed EmDash documentation before migration; the names below are the content contract.

| Area | Keep | Add or extend |
| --- | --- | --- |
| Posts | `title`, `excerpt`, `featured_image`, `content`, `event_date`, `source_url`, native publication dates and bylines | Optional `linkedin_post_url`; optional `speakers` repeater with name, project name, optional member reference and optional profile URL; optional `featured_image_caption` |
| Speaker body | Existing Portable Text headings, paragraphs, images/captions, code and links | No parallel body store. Each speaker/project is a major heading with its own relevant image in the same content field. |
| Podcast | Existing CTA block and stored show URL remain valid | `podcast_episodes` collection: title, description, artwork, Spotify episode URL; optional release date, duration seconds, episode number and guest text. Draft/revision/preview support. A `page_podcast` block holds heading, show description, show URL, status note and episode count. |
| Photo section | Existing `page_images` content and layouts | Optional caption for each image; additive Polaroid layout option. Raise maximum images from four to six for a short curated sequence if content warrants it; retain four-image layouts. |

Do not label speakers as authors unless they wrote the article. Native bylines identify the actual writer/editor; visible Featuring credits and schema mentions describe speakers. Store publication date separately from the event date. Use `featured_image` for the one main photo or original Luma artwork; contain text-heavy/square covers rather than cropping away titles. Legacy `source_url` remains the original recap URL and must not be silently relabelled as LinkedIn.

A new post requires a short title, excerpt, body and chosen imagery; the template supplies all presentation and contents navigation. An editor can start by duplicating a draft example with placeholder instructions, then replace text/media. No HTML/CSS editing is required. Missing optional speaker, LinkedIn or podcast metadata is omitted cleanly.

## Migration and compatibility

- Add nullable fields and new block/collection definitions through an idempotent preview-only migration first. Back up schema, affected entries and media mapping before applying it. Updating `seed/seed.json` alone does not update an existing hosted database.
- Deploy a renderer that tolerates absent new fields before applying the additive schema. Keep the existing generic podcast CTA and page-image layouts working until editors replace those blocks.
- Preview title cleanup for the six imported Roast posts and remove dates only from recognised legacy titles; do not rewrite arbitrary community/partnership titles or slugs. Preserve the original records in revisions/backup. Keep the date once on cards and explicit dates in article metadata.
- Replace the repeated excerpt boilerplate with source-grounded editorial copy. This is content editing, not a CSS truncation rule.
- Remove a duplicate body image only when the editor deliberately chooses it as the same lead visual; do not globally delete all repeated image references. Speaker images remain.
- Import only verified public Spotify episode metadata. Do not invent guests, durations, release dates or show status. The live site currently says Season 1 complete/on pause; verify against current publishing before changing that label.
- Existing posts with no speakers/new fields remain readable. Existing page block types keep their data and keys. Preserve route slugs, taxonomy URLs, visual-edit bindings, cache hints, previews and author ownership.

## SEO and accessible rendering

Generate the public article and contents server-side. One H1; descriptive H2/H3 sections; anchor links usable without JavaScript; image dimensions/alt text and accurate captions. Keep plain link names, visible focus, sufficient tap targets and keyboard-operable mobile navigation. Podcast links open the specific episode; no transcript action. The photo sequence shows a static complete composition when scripts fail, uses a simple mobile gallery and honours reduced motion. No mandatory long scroll or images obscuring the central statement.

Retain accurate canonical/description/Open Graph metadata. Validate one Article/BlogPosting representation from the existing EmDash metadata path before adding any extra JSON-LD; avoid duplicate/conflicting schema. Match actual author, publisher, headline, image, first publication and real modification dates. In this article is navigation, not special AEO schema or a promise of AI citations. Hosted preview remains excluded from indexing and protected as configured; production URLs must not point at preview.

## Phased commits and review gates

| Commit group | Concrete result | Review evidence |
| --- | --- | --- |
| 1. Hosted baseline | Hosted design snapshot with bundled media, or separate Worker/D1/media/KV for editable CMS; named baseline deployment and matching backups | Main routes and images on hosted preview; admin sign-in/draft/restore checked locally for a static snapshot, or on isolated hosted CMS when provisioned |
| 2. Shared shell/type | Header/footer/mobile navigation, agreed typography roles and link treatment | Homepage, article, people, events and campaign desktop/mobile screenshots |
| 3. Article prototype | Rebuild Roast #7 using existing real content; TOC, short title, metadata, lead/speaker images, optional LinkedIn field | All TOC anchors, image crops/captions, one date line, no duplicate lead, metadata inspection |
| 4. Authoring contract | Additive schema, native editor labels/help, reusable draft example, guarded content-cleanup migration | Create/edit/preview a disposable post without HTML; rollback to its prior revision |
| 5. Cards/events | Shared short PostCards and aligned Braintrust-style format cards | Homepage/archive/category/tag routes, long/missing-image titles, keyboard and mobile |
| 6. Podcast | Maze episode rows and real Spotify entries | Every Listen URL matched to its episode; empty/missing metadata states |
| 7. Photo section/home | Profound-style Polaroids, final homepage ordering and event CTA | Scroll, reduced motion, script-free layout, phone gallery, calendar failure state |
| 8. Release review | Bounded final regression and documented recovery | Preview sign-off; no production deploy/merge without final approval |

Run `pnpm typecheck`, build, source detector and rendered desktop/mobile detector checks against the actual preview origin. `pnpm design:check:site` currently targets port 4321; point equivalent checks at 4331 or the hosted preview rather than accidentally checking another process. Use 390×844 and desktop captures together, fix findings as one batch, then perform at most one confirmation pass. Tests should cover anchor IDs/links, absent fields, data-cleanup dry run and migration idempotency rather than mirror CSS implementation. Exercise at least one ordinary non-event post and a short article as well as Roast #7.

Code recovery uses the named baseline deployment/commit. CMS recovery uses preview content revisions and database/media backup. A renderer rollback does not restore content or undo a destructive schema migration; keep migrations additive. The baseline and redesign must remain reviewable without touching the live Techies Worker or CMS.
