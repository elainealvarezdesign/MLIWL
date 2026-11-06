# MLIWL design system

The design rules for **My Life Is Worth Living**, for anyone building or editing the site, with or without Figma open.

- **Figma (source of truth):** [Design System - MLIWL](https://www.figma.com/design/pji462RDmAcvludSloZL2w/Design-System---MLIWL?node-id=0-1)
- **Tokens in code:** `tokens/` and `plugin/mliwl-design-system/assets/css/tokens.css` (see [README](README.md))
- **Building in Elementor:** [docs/elementor-setup.md](docs/elementor-setup.md)

If this file and Figma disagree, Figma wins; update this file.

---

## 1. Principles

1. **Help is always one tap away.** 988 (call and text) appears on every page: the Crisis Bar on top, the Get help section or Crisis Strip near the bottom, and the footer. Never hide it behind a menu or a "click here".
2. **Warn before sensitive content.** Every story lists its topics (suicide, self-harm, abuse, substance use…) before the video plays, and links to help.
3. **Stay on our site.** "Watch" buttons go to the story page on mylifeisworthliving.org, not to YouTube.
4. **Say what things do.** Buttons and links name their destination: "Watch Kyle's story", "Visit Mental Health America", "Download playbook (PDF)". Never "Play", "Read more" or "Click here".
5. **Teens, parents and educators each have a path.** Home routes each audience to its page; content is never mixed without a label.
6. **Accessible by default.** WCAG 2.2 AA, 48px touch targets, visible focus, real text instead of text inside images.

## 2. Pages and routes

Every page has Desktop (1440), Tablet (768) and Mobile (390) frames in Figma. Sitemap: [Figma › Sitemap](https://www.figma.com/design/pji462RDmAcvludSloZL2w/Design-System---MLIWL?node-id=160-987).

| Page | Route | Replaces today |
|---|---|---|
| Home | `/` | Home |
| Watch | `/stories` | Watch (+ language versions) |
| Story page (×8) | `/stories/:slug` | — (new; videos opened on YouTube) |
| For parents | `/parents` | Parent Guidance |
| Educator hub | `/educators` | Lessons |
| Get help | `/get-help` | Get Help (old Lifeline number) |
| About | `/about` | About the Series |
| Meet the team | `/about/team` | Meet the Team |
| Partners | `/about/partners` | Partners |
| News & media | `/about/news` | Media + Blog (merged) |
| Privacy policy | `/privacy` | — |
| Page not found | 404 | — |

Designs: [Desktop](https://www.figma.com/design/pji462RDmAcvludSloZL2w/Design-System---MLIWL?node-id=87-764) · [Tablet](https://www.figma.com/design/pji462RDmAcvludSloZL2w/Design-System---MLIWL?node-id=212-26) · [Mobile](https://www.figma.com/design/pji462RDmAcvludSloZL2w/Design-System---MLIWL?node-id=87-765). Old URLs must 301-redirect to the new routes (list in [Figma › Dev Handoff](https://www.figma.com/design/pji462RDmAcvludSloZL2w/Design-System---MLIWL?node-id=156-987)).

## 3. Layout

| | Desktop (≥1024) | Tablet (768–1023) | Mobile (≤767) |
|---|---|---|---|
| Frame | 1440 | 768 | 390 |
| Content width | 1200 centered | 704 | 358 |
| Side padding | 120 at 1440 (min 24) | 32 | 16 |
| Section padding (top/bottom) | 72 | 64 | 48 |
| Card grid | 3–4 columns, 24 gap | 2 columns, 24 gap | 1 column (carousels for stories) |

- **8px grid.** Every size, gap and padding is a multiple of 8. 4, 12 and 20 are allowed only inside small elements (icon offsets, tag padding).
- **Text line heights** sit on a 4px base.
- **Touch targets** are at least 48 × 48 px.

## 4. Color

Use **semantic tokens** (what the color is for), never raw hex. Primitives exist only so semantic tokens can point to them. Foundations: [Figma › Foundations](https://www.figma.com/design/pji462RDmAcvludSloZL2w/Design-System---MLIWL?node-id=0-1).

| Token | Hex | Use |
|---|---|---|
| `bg/page` | `#ffffff` | Default page background. |
| `bg/subtle` | `#f7f5f0` | Warm alternate section (Start here). |
| `bg/muted` | `#eeeeee` | Muted section (Stories). |
| `bg/surface` | `#ffffff` | Cards on any background. |
| `bg/inverse` | `#181a1d` | Crisis bar, footer, primary buttons. |
| `bg/brand` | `#e70000` | Brand red fills. |
| `bg/hero` | `#65276d` | Hero section. |
| `bg/help` | `#406c96` | Get help section. |
| `bg/featured` | `#2b5d8a` | Featured story panel. |
| `bg/highlight` | `#cfac38` | Awards band, badges. |
| `text/primary` | `#181a1d` | Headings and body. |
| `text/secondary` | `#55575c` | Supporting text. |
| `text/inverse` | `#ffffff` | Text on dark, hero, help and character colors. |
| `text/brand` | `#c40000` | Eyebrows and links on light backgrounds. |
| `text/accent-on-dark` | `#cfac38` | Eyebrow on the purple hero. |
| `text/success` | `#2b6b49` | Success status text. |
| `border/default` | `#dddddd` | Card and section dividers. |
| `border/quiet` | `#bdbdbd` | Chips and secondary outlines. |
| `border/input` | `#77797e` | Form inputs (3:1+). |
| `border/strong` | `#181a1d` | Outlined buttons and active chips. |
| `border/inverse` | `#ffffff` | Outlined buttons on dark. |
| `action/primary/bg` | `#181a1d` | Primary button fill (black CTA). |
| `action/primary/text` | `#ffffff` | Primary button label. |
| `action/accent/bg` | `#cfac38` | Hero CTA fill (Watch free). |
| `action/accent/text` | `#181a1d` | Label on gold CTA. |
| `action/link` | `#c40000` | Inline links. |
| `focus/ring` | `#cfac38` | Keyboard focus outline (paired with black halo). |
| `character/dante` | `#65276d` | Dante story color. |
| `character/amie` | `#40a070` | Amie story color. |
| `character/emily` | `#61579c` | Emily story color. |
| `character/kyle` | `#406c96` | Kyle story color. |
| `character/danny` | `#902d16` | Danny story color. |
| `character/group` | `#cfac38` | Group / Are You OK? color. |
| `character/kaia` | `#37998a` | Kaia story color. |
| `character/vince` | `#2b6d99` | Vince story color. |
| `character/raquelle` | `#a33a72` | Raquelle / Are You OK? story color (raspberry). White text 6.2:1. |
| `action/primary/bg-hover` | `#3a3c40` | Primary button hover. |
| `action/accent/bg-hover` | `#b8962a` | Gold button hover. |
| `action/outline/bg-hover` | `#eeeeee` | Outline button hover on light backgrounds. |
| `action/inverse/bg-hover` | `#ffffff` | Outline-on-dark hover: fills white, label turns ink. |
| `action/primary/bg-pressed` | `#55575c` | Primary button pressed. |
| `action/accent/bg-pressed` | `#9c7f22` | Gold button pressed. |
| `action/outline/bg-pressed` | `#dddddd` | Outline button pressed. |
| `action/inverse/bg-pressed` | `#dddddd` | Outline-on-dark pressed (label ink). |
| `action/selected/bg` | `#65276d` | Selected / current state of Primary (white label, 10.2:1). |
| `action/disabled/bg` | `#dddddd` | Disabled fill. |
| `action/disabled/text` | `#77797e` | Disabled label (exempt from contrast; never the only cue). |
| `action/disabled/border` | `#bdbdbd` | Disabled outline. |
| `text/inverse-secondary` | `#dddddd` | Secondary text on ink (12.8:1). |
| `border/brand` | `#e70000` | Brand red underline for nav hover/current. |
| `action/selected/bg-hover` | `#4e1e55` | Language select / selected hover. |

**Contrast rules**

- Small colored text uses `text/brand` (#c40000), not the brighter `bg/brand` red.
- On gold (`bg/highlight`, `action/accent/bg`) text is always ink, never white.
- Character colors carry white text only at large sizes or on their `/700` variants.
- Disabled styling is never the only signal; pair it with text or `aria-disabled`.

## 5. Typography

**Montserrat only** (400, 500, 700, 800, 900). Headings are Black, all caps. Japanese and Chinese labels fall back to Noto Sans JP / SC.
Sizes are `font-size / line-height` in px; they change by breakpoint through the Typography variables.

| Style | Weight | Desktop | Tablet | Mobile | Case |
|---|---|---|---|---|---|
| Display | 900 | 66/64 | 52/56 | 40/40 | Caps · -1% tracking |
| Heading/H1 | 900 | 48/50 | 40/44 | 34/36 | Caps |
| Heading/H2 | 900 | 40/42 | 34/40 | 30/32 | Caps |
| Heading/H3 | 900 | 24/28 | 22/28 | 20/24 | Caps |
| Heading/H4 | 900 | 20/24 | 19/24 | 18/24 | Caps |
| Body/Large | 400 | 19/30 | 18/28 | 18/28 | Sentence |
| Body/Default | 400 | 17/28 | 16/24 | 16/24 | Sentence |
| Body/Strong | 700 | 17/28 | 16/24 | 16/24 | Sentence |
| Body/Small | 400 | 15/24 | 15/24 | 15/24 | Sentence |
| Caption | 500 | 13/20 | 13/20 | 13/20 | Sentence |
| Eyebrow | 800 | 13/16 | 12/16 | 12/16 | Caps · 16% tracking |
| Label/Button | 800 | 15/24 | 15/24 | 15/24 | Caps · 6% tracking |
| Label/Button Small | 800 | 13/16 | 13/16 | 13/16 | Caps · 6% tracking |
| Label/Nav | 800 | 13/16 | 13/16 | 13/16 | Caps · 10% tracking |
| Label/Tag | 800 | 11/16 | 11/16 | 11/16 | Caps · 10% tracking |

- One H1 per page. Pick the HTML heading level for structure, then the style for looks.
- Body copy: `Body/Default` (17px desktop). Never set paragraphs smaller than `Body/Small` (15px).
- Long headlines (articles, press) use `Body/Strong`, not caps headings, so they stay readable.

## 6. Radius and elevation

| Token | px | Use |
|---|---|---|
| `radius/xs` | 4 | Tags |
| `radius/sm` | 8 | Small controls, skip link |
| `radius/md` | 12 | Inputs, selects |
| `radius/ml` | 16 | Notes, tips, thumbnails |
| `radius/lg` | 20 | Help cards |
| `radius/xl` | 24 | Story, lesson, person, partner and article cards |
| `radius/2xl` | 28 | Featured panel |
| `radius/3xl` | 32 | Large panels |
| `radius/full` | 999 | Buttons, chips, language select |

Shadows: `Elevation/Hover` (cards on hover), `Elevation/Raised` (dialogs, floating play button), `Elevation/Tag` (tags on artwork).

**Focus:** a 3px gold ring (`focus/ring`) with a 2px ink halo on every interactive element. Never remove the focus outline.

## 7. Components

Each component has a Figma page with a table of every state. Build pages only from these components and sections.

| Component | Variants | Use | Figma |
|---|---|---|---|
| Button | Primary · Accent · Outline · Outline Inverse; Default 56 / Small 48; Default, Hover, Pressed, Selected, Focus, Disabled | Primary = main action (black). Accent (gold) only in heroes. Outline Inverse on purple, blue or ink. Icons left or right. | [Button](https://www.figma.com/design/pji462RDmAcvludSloZL2w/Design-System---MLIWL?node-id=12-2) |
| Tag | On Image · Inverse · Highlight · Subtle | Static label (topic, "Now playing", "Episode 1 of 4"). Not clickable. | [Tag & Chip](https://www.figma.com/design/pji462RDmAcvludSloZL2w/Design-System---MLIWL?node-id=18-2) |
| Chip | Selected / not; Default, Hover, Focus | Filters (`<button aria-pressed>`). One per group always selected ("All"). Result count in `role="status"`. | [Tag & Chip](https://www.figma.com/design/pji462RDmAcvludSloZL2w/Design-System---MLIWL?node-id=18-2) |
| Text Field | Single line · Multi line; Default, Hover, Focus, Filled, Error, Disabled | Label always visible. Error = red border + message that says how to fix it. | [Form](https://www.figma.com/design/pji462RDmAcvludSloZL2w/Design-System---MLIWL?node-id=149-987) |
| Select | Default, Hover, Focus, Disabled | Native `<select>` only. | [Form](https://www.figma.com/design/pji462RDmAcvludSloZL2w/Design-System---MLIWL?node-id=149-987) |
| Checkbox / Radio | Unchecked, Checked, Focus, Disabled | Native inputs in 48px rows, grouped in `<fieldset>` + `<legend>`. | [Form](https://www.figma.com/design/pji462RDmAcvludSloZL2w/Design-System---MLIWL?node-id=149-987) |
| Story Card | Default, Hover | One per story: art, topic tag, title, description (max 4 lines), content note, Watch button, lesson link. | [Story Card](https://www.figma.com/design/pji462RDmAcvludSloZL2w/Design-System---MLIWL?node-id=20-2) |
| Featured Story | Desktop · Mobile | Newest story, once at the top of Stories. | [Featured Story](https://www.figma.com/design/pji462RDmAcvludSloZL2w/Design-System---MLIWL?node-id=58-2) |
| Episode Row | Default, Now playing, Watched | Episode list on the story page; loads the video in the on-page player. | [Episode Row](https://www.figma.com/design/pji462RDmAcvludSloZL2w/Design-System---MLIWL?node-id=126-490) |
| Lesson Card | Default, Hover | Lesson plans (Educator hub) and parent playbooks (For parents). Download shows type and size. | [Lesson Card](https://www.figma.com/design/pji462RDmAcvludSloZL2w/Design-System---MLIWL?node-id=136-678) |
| Audience Card | Teens · Parents · Educators; Default, Hover, Focus | "Start here" on Home. | [Audience Card](https://www.figma.com/design/pji462RDmAcvludSloZL2w/Design-System---MLIWL?node-id=43-2) |
| Help Card | — | One help line with tap-to-call / tap-to-text. | [Help Card](https://www.figma.com/design/pji462RDmAcvludSloZL2w/Design-System---MLIWL?node-id=44-2) |
| Person Card | Default, Hover, Focus | Team and advisory board; "Read bio" opens a Dialog. | [Person & Partner Card](https://www.figma.com/design/pji462RDmAcvludSloZL2w/Design-System---MLIWL?node-id=174-26) |
| Partner Card | Default, Hover, Focus | Partner logo box (96px), name, description, "Visit {name}" (new tab). | [Person & Partner Card](https://www.figma.com/design/pji462RDmAcvludSloZL2w/Design-System---MLIWL?node-id=174-26) |
| Article Card | News · Article; Default, Hover, Focus | Press coverage and our own articles. Headline is the only link. | [Article Card](https://www.figma.com/design/pji462RDmAcvludSloZL2w/Design-System---MLIWL?node-id=188-26) |
| Dialog | Desktop · Mobile | Read bio and other modals. Focus trapped, Escape closes, focus returns to the trigger. | [Dialog & Empty State](https://www.figma.com/design/pji462RDmAcvludSloZL2w/Design-System---MLIWL?node-id=206-26) |
| Empty State | — | Replaces a card grid when filters return nothing; "Clear filters". | [Dialog & Empty State](https://www.figma.com/design/pji462RDmAcvludSloZL2w/Design-System---MLIWL?node-id=206-26) |
| Crisis Bar | Desktop · Mobile | Top of every page: Call 988, Text 988, outside-U.S. link. | [Crisis Bar](https://www.figma.com/design/pji462RDmAcvludSloZL2w/Design-System---MLIWL?node-id=55-2) |
| Header, Nav Link, Language Select | Desktop · Mobile; Nav: Default, Hover, Current, Focus | Logo, 4 nav links, Get help now, video language. | [Header](https://www.figma.com/design/pji462RDmAcvludSloZL2w/Design-System---MLIWL?node-id=56-2) |
| Mobile Menu, Menu Item | Menu Item: Default, Pressed, Current, Focus | Full-screen menu on phones; 988 visible without scrolling. | [Header](https://www.figma.com/design/pji462RDmAcvludSloZL2w/Design-System---MLIWL?node-id=56-2) |
| Footer | Desktop · Tablet · Mobile | Brand, Explore, Follow, Need help now?, legal. | [Footer](https://www.figma.com/design/pji462RDmAcvludSloZL2w/Design-System---MLIWL?node-id=61-2) |
| Section/Get Help | Desktop · Tablet · Mobile | "Need to talk to someone now?" band with four Help Cards. | [Sections](https://www.figma.com/design/pji462RDmAcvludSloZL2w/Design-System---MLIWL?node-id=200-26) |
| Section/Newsletter | Desktop · Mobile; Default, Error, Success | Sign-up with audience chips. | [Sections](https://www.figma.com/design/pji462RDmAcvludSloZL2w/Design-System---MLIWL?node-id=200-26) |
| Section/Crisis Strip | Desktop · Mobile | Gold 988 strip above the footer on inner pages. | [Sections](https://www.figma.com/design/pji462RDmAcvludSloZL2w/Design-System---MLIWL?node-id=200-26) |

Icons (11, 24px, single color): [Icons](https://www.figma.com/design/pji462RDmAcvludSloZL2w/Design-System---MLIWL?node-id=11-7). Characters and story art: [Characters](https://www.figma.com/design/pji462RDmAcvludSloZL2w/Design-System---MLIWL?node-id=76-740). Logos and award laurels: [Brand Assets](https://www.figma.com/design/pji462RDmAcvludSloZL2w/Design-System---MLIWL?node-id=54-2).

**Repeated sections are components.** Get help, Newsletter, Crisis Strip, Header and Footer are edited in one place (Figma component / Elementor saved template) and update everywhere.

## 8. Content rules

- **Voice:** warm, direct, plain English (around grade 7). Talk to the reader ("you"). Short sentences.
- **Crisis copy** names the action and the number: "Call or text 988", "Text HOME to 741741", "Call 911 if you're in danger".
- **Content notes** list topics plainly: "Includes: suicide attempt, self-harm. Need to talk? Call or text 988."
- **Language:** pages are in English. Videos exist in Spanish, Portuguese, Japanese and Mandarin; label those options with their own name and `lang` attribute.
- **Placeholders** in designs are in [brackets]; never publish a page that still has one.
- Clinical copy (Get help, warning signs, conversation starters, safe-viewing tips) needs review by the client's clinical team before publishing.

## 9. Accessibility checklist

- Contrast: semantic text-on-background pairs only (section 4).
- Focus: gold ring on everything interactive; logical tab order; no keyboard traps except inside an open dialog.
- Structure: skip link → Crisis Bar → Header → main → Footer. One H1. Lists of cards are `<ul>/<li>`.
- Images: meaningful images have alt text; decorative art has empty alt. No text inside images.
- Forms: visible labels, errors linked with `aria-describedby`, `aria-invalid` on the field.
- Media: captions on by default, transcripts linked, no autoplay, content note before the player.
- Motion: respect `prefers-reduced-motion`; carousels never auto-advance.
- External links say they open a new tab.

## 10. Waiting on the client

Tracked in [Figma › Dev Handoff](https://www.figma.com/design/pji462RDmAcvludSloZL2w/Design-System---MLIWL?node-id=156-987). Main items: story descriptions and episode data, content notes, lesson and playbook details, clinical review of crisis copy, help-line verification, CDC figure and source, team photos, partner logos (including the new 988 logo), press dates and press kit, legal privacy text, next story title, Raquelle's color.
