# Current Techies design system

Source audit: 30 October 2026, fork branch codex/techies-design-preview, application checkpoint d077a64c380d50701a30dc790ee5848d0030ff12. This inventories current CSS/components, not a newly approved design specification. It does not claim fresh live-site computed-style or full accessibility verification. No application styles changed during this audit.

## Scope and authority
- Fixed: supplied Techies logo, artwork proportions and colours; no decorative link/button arrows. Preserve genuine photos and event artwork.
- Current implementation: custom Astro frontend, shared theme.css plus component-scoped CSS, EmDash CMS. Public styling is separate from native EmDash/Kumo administration.
- DESIGN.md records existing source decisions but has historical prose and local exceptions; BRAND_GUIDE.md contains both observed and proposed standards. Resolve conflicts against source and explicit user choices.
- The current branch includes article-prototype changes not deployed to the live Techies website. The tables identify these where relevant.

## Typography
Inter is the default sans-serif for all public headings, paragraphs, navigation and controls. Requested weights: 400 regular, 500 medium, 600 semibold, 700 bold, 800 extra-bold. JetBrains Mono is requested at 400/500/600 for code, terminal detail, text wordmark and profile placeholders. Both come from Google Fonts with display=swap and generic fallbacks; font-synthesis is disabled.

| Role | Family / weight | Current size and leading | Colour / treatment |
| --- | --- | --- | --- |
| Main H1 / hero | Inter 800 | Fluid 40–64px; line-height 1.12 | Primary cream; -0.03em tracking, balanced wrapping |
| Section H2 | Inter 700 | Fluid 28–40px; 1.12 | Primary cream; -0.03em tracking |
| General H3 | Inter browser-default bold | 23px; 1.12 | Primary cream; -0.025em tracking |
| Item/event row heading | Inter bold | 20px; event rows 1.35 | Primary cream |
| Post-card title | Inter bold | 21px; 1.3 | Primary cream; 12px vertical margins |
| Member-card title | Inter bold | 26px; inherits H2 leading | Primary cream |
| General paragraph | Inter 400 | 16px; 1.65 (26.4px) | Secondary grey |
| Hero introduction | Inter 400 | 17px desktop; 16px at <=700px | Secondary grey |
| Page introduction | Inter 400 | 18px; 16px at <=640px | Secondary grey |
| Section support text | Inter 400 | 15px | Secondary grey |
| Metadata | Inter 500 | 14px | Secondary grey |
| Navigation | Inter 400 | 14px | Grey; active/hover cream |
| Button and text-action labels | Inter 600 | 14px | Primary: near-black on orange; secondary: cream |
| General article body | Inter 400 | 18px; 1.7 (30.6px) | Reading grey; 70ch maximum since prototype |
| Article H2 / H3 | Inter bold | 32px / 24px; 1.12 inherited | Cream unless a link inherits prose orange |
| Article title — prototype | Inter 800 | Fluid 36–48px; 1.12 | Primary cream |
| Article introduction — prototype | Inter 400 | 20px / 1.6; 18px <=900px | Secondary grey |
| Article speakers — prototype | Inter 400 | 16px | Cream linked names, grey Featuring label |
| Article contents — prototype | Inter bold label / regular links | Label 16px; links 14px / 1.5 | Cream label, grey links |
| Captions | Inter 400 | General 13px; prototype 14px / 1.5 | Secondary grey; prototype left aligned |
| Footer headings / links | Inter bold / regular | 16px / 14px | Cream / secondary grey |
| Text wordmark | JetBrains Mono 600 | 25px; 24px <=640px | Cream text, orange underscore; not the supplied official logo |
| Code | JetBrains Mono 400 | Terminal 14px / 1.9; inline .85em | Cream on dark surfaces |

Headings generally use sentence case; text is not globally transformed to uppercase. Blockquotes request italic, but no italic font faces are requested in the font import. H4–H6 have no complete global role scale; some local H4s use 18px. These are gaps to resolve, not approved new values.

## Current interface colours

| Token / role | Value | Notes |
| --- | --- | --- |
| Page background | #0a0a0f | Near-black |
| Surface | #111118 | Cards, alternate sections, footer |
| Raised/card surface | #16161f | Code, hover and image placeholders |
| Primary text | #fbf8ef | Cream; prototype changed from #e8e8ed |
| Reading text | #c7c5c0 | Prototype; previous prose literal #b8b8c6 |
| Secondary text | #9898a8 | Body introductions, metadata, supporting text |
| Orange action/accent | #f97316 | Buttons, links, focus, selected accents |
| Orange hover | #ea580c | Filled actions |
| Decorative border | #252530 | Cards and section dividers |
| Control border | #686878 | Outlined buttons, dialogs and fields |
| Incident red | #ef4444 | Event-specific exception |

These are existing UI values, not a complete official-logo palette. The fixed logo's green cursor and warm gradient are artwork; they are not currently represented as a general green UI action token. Branding artwork must not be recoloured to match these tokens.

## Controls and components

| Component | Current specification |
| --- | --- |
| Primary button | Orange fill and 1px orange border, near-black text; 14px/600; minimum 48px high; 13px vertical / 20px horizontal padding; 8px corners; darker orange hover |
| Secondary button | Same geometry/type; transparent fill, 1px control-grey outline, cream text; raised-dark hover |
| Text action | No fill/border; 14px/600; orange hover; no decorative arrow. It has no universal minimum target-height rule. |
| Join navigation action | Transparent outlined link; 8px corners; 9px/15px padding (12px horizontal on mobile); follows 14px navigation type, not primary button weight |
| Keyboard focus | 3px orange outline, 5px offset; applies to links, buttons, inputs and summary |
| Announcement | Orange bar, near-black copy; dark filled CTA with cream text, minimum 44px; 44px close control |
| Post card | Surface fill, 1px decorative border, 12px corners; 16:10 cropped image; 24px copy padding; 21px title, 16px excerpt, 14px date/action; action pushed to bottom; border brightens on hover |
| Member card | Same outer surface/border/corners; 26px name above square portrait; 20px header padding; 16px detail padding; 44px learn-more action; native dialog for biography/project details |
| Member dialog | Dark panel, 12px corners, stronger border, max 720px wide, 32px padding; full-screen with square corners and 24px/20px padding on small screens |
| Upcoming event | Horizontal row separated by borders; date + 112px square artwork + title/details + text action; reflows at 900/600px; not a uniform gallery card |
| Event-series section | Asymmetric two-column layout: larger flagship and smaller image/text formats; not yet equal-height Braintrust-style cards |
| Event recap archive | Native details/summary rows, not post cards; 20px/600 titles (18px mobile), 14px dates; disclosure chevron remains, distinct from removed decorative link arrows |
| Photo collage | Cream/off-white frames; 8px padding (6px mobile), rotations and soft shadow; static. Supplied image arrays with fewer than four images use an unrotated responsive grid. Not yet a progressive Profound-style Polaroid sequence. |
| Podcast | Generic split CTA with show title, status, description and outlined link. No episode-row component implemented yet. |
| Public campaign fields | Dark fill, stronger border, 8px corners, 12px padding, inherited font; labels/errors in text. Native CMS controls use Kumo rather than these public styles. |

## Layout, images and motion
- Main container: maximum 1180px; 32px side margins normally, 20px <=640px.
- Main sections: 88px vertical padding, 60px on mobile. Common gaps include 16/20/24/28/32/48/64px; these are literals rather than a coherent named spacing-token scale.
- Post grid: three columns, two <=900px, one <=640px; 24px gap.
- Hero: text/visual split 1.15:1 with 70px gap; stacks <=700px. Navigation wraps to a second row <=640px; no mobile menu pattern.
- Article prototype: header max 840px; lead max 1000px, uncropped/contained and max-height 640px; body max 720px. Desktop contents rail 216px + 48px gap; mobile contents above body <=900px. Body images span reading column; 8px corners, left-aligned 14px captions.
- General image treatment still includes 12px rounded/cropped images and the legacy 20px hero rule, so the article's 8px role is not yet a universal image system.
- Radius vocabulary currently includes 4px code/badges, 8px controls/article images, 12px cards/panels, 20px empty-state/legacy hero, and square photos within rounded member cards.
- Most panels use tonal layers and thin borders rather than shadows. The collage is the main soft-shadow exception.
- Hover transitions are approximately 180ms. Smooth anchor scrolling is enabled. Reduced-motion preferences disable smooth scrolling, transitions and animation.
- Breakpoints vary by component: 400/600/640/700/800/900/1000px. They have not been consolidated into semantic layout rules.

## Prototype differences from baseline
Compared directly against baseline code commit 431037d1656a5d590341416ac91bbc1f0969c416:
- Shared primary text changed from #e8e8ed to cream #fbf8ef; prose from #b8b8c6 to #c7c5c0.
- General prose max-width changed from 620px to 70ch; article prototype additionally caps its body at 720px.
- Article-specific title/introduction/contents, speaker credits, date labels and image treatment added. Post-card titles shortened through a helper; card geometry is unchanged.
- Base header/footer, homepage composition, Braintrust event cards, Maze podcast rows and progressive Polaroid gallery have not been rebuilt.

## Decisions to make next (not implementation approval)
1. Confirm typography roles: display, page/article title, section, subsection, card title, body, supporting text, metadata and caption. Set desktop/mobile behaviour and weights once.
2. Decide whether the current UI dark neutrals and cream/reading/secondary hierarchy are the right expression of the fixed logo brand. Define exactly when orange and the logo's green are used.
3. Agree primary/secondary/text actions, link decoration, focus/hover and target heights; keep labels plain.
4. Agree card anatomy, image ratios/cropping, corner roles, excerpt length and aligned action baselines.
5. Set container/reading widths, spacing roles and responsive navigation; then apply the selected page references using those shared rules.
6. Resolve documentation/source drift and generate one canonical approved specification before the implementation chat changes code.

## Source map
src/styles/theme.css; src/layouts/Base.astro; src/components/PageSection.astro; PostCard.astro; ProfileCard.astro; UpcomingEvents.astro; HangoutCollage.astro; ArticleContents.astro; AnnouncementBanner.astro; src/pages/posts/[slug].astro; src/pages/events.astro; src/styles/campaigns.css. DESIGN.md and BRAND_GUIDE.md supply context; current source overrides stale descriptive prose.
