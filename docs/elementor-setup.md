# Elementor setup

How to make Elementor match the Figma design system. Do this once per site (staging first).
Source of every value: `tokens/figma-export.json` (exported from Figma). If Figma changes, regenerate with `tokens/build.py` and update these settings.

## 1. Install the plugin

1. Zip the folder `plugin/mliwl-design-system/` and upload it in Plugins › Add New › **Upload Plugin**. Activate **MLIWL Design System**.
2. It works with the current theme (Astra) or any other; no theme change is needed.
3. It loads Montserrat, `tokens.css` and `components.css` on the site and inside the Elementor editor, after Astra's and Elementor's own styles so the MLIWL classes win.

## 2. Breakpoints

Elementor › Site Settings › Layout › Breakpoints:

| Elementor device | Value | Figma frame |
|---|---|---|
| Mobile | max 767px | Mobile (390) |
| Tablet | **max 1023px** (change from the default 1024) | Tablet (768) |
| Desktop | 1024px and up | Desktop (1440) |

Layout › Content width: **1200px**. Container padding: 24px desktop · 32px tablet · 16px mobile. Widgets space: 24px.

## 3. Global colors

Site Settings › Design System › Global Colors. Set the four system colors, then add the rest as custom colors with exactly these names, so editors pick roles instead of hex values.

| Elementor name | Hex | Token | Use |
|---|---|---|---|
| bg · page | `#ffffff` | `--color-bg-page` | Default page background. |
| bg · subtle | `#f7f5f0` | `--color-bg-subtle` | Warm alternate section (Start here). |
| bg · muted | `#eeeeee` | `--color-bg-muted` | Muted section (Stories). |
| bg · inverse | `#181a1d` | `--color-bg-inverse` | Crisis bar, footer, primary buttons. |
| bg · hero | `#65276d` | `--color-bg-hero` | Hero section. |
| bg · help | `#406c96` | `--color-bg-help` | Get help section. |
| bg · featured | `#2b5d8a` | `--color-bg-featured` | Featured story panel. |
| bg · highlight | `#cfac38` | `--color-bg-highlight` | Awards band, badges. |
| Text (system) | `#181a1d` | `--color-text-primary` | Headings and body. |
| Secondary (system) | `#55575c` | `--color-text-secondary` | Supporting text. |
| text · inverse | `#ffffff` | `--color-text-inverse` | Text on dark, hero, help and character colors. |
| Primary (system) | `#c40000` | `--color-text-brand` | Eyebrows and links on light backgrounds. |
| text · accent-on-dark | `#cfac38` | `--color-text-accent-on-dark` | Eyebrow on the purple hero. |
| border · default | `#dddddd` | `--color-border-default` | Card and section dividers. |
| border · input | `#77797e` | `--color-border-input` | Form inputs (3:1+). |
| Accent (system) | `#cfac38` | `--color-action-accent-bg` | Hero CTA fill (Watch free). |
| character · dante | `#65276d` | `--color-character-dante` | Dante story color. |
| character · amie | `#40a070` | `--color-character-amie` | Amie story color. |
| character · emily | `#61579c` | `--color-character-emily` | Emily story color. |
| character · kyle | `#406c96` | `--color-character-kyle` | Kyle story color. |
| character · danny | `#902d16` | `--color-character-danny` | Danny story color. |
| character · group | `#cfac38` | `--color-character-group` | Group / Are You OK? color. |
| character · kaia | `#37998a` | `--color-character-kaia` | Kaia story color. |
| character · vince | `#2b6d99` | `--color-character-vince` | Vince story color. |
| action · primary · bg-hover | `#3a3c40` | `--color-action-primary-bg-hover` | Primary button hover. |
| action · accent · bg-hover | `#b8962a` | `--color-action-accent-bg-hover` | Gold button hover. |

Small colored text uses **text · brand** (`#c40000`), never the brighter brand red. White text is never placed on gold.

## 4. Global fonts

Site Settings › Design System › Global Fonts. Family **Montserrat** for all. Sizes are `font-size / line-height` in px; set each device with the responsive toggle.

| Global font | Weight | Desktop (≥1024) | Tablet (768–1023) | Mobile (≤767) | Case / spacing |
|---|---|---|---|---|---|
| Display | 900 | 66 / 64 | 52 / 56 | 40 / 40 | UPPERCASE, -1% |
| Heading/H1 | 900 | 48 / 50 | 40 / 44 | 34 / 36 | UPPERCASE |
| Heading/H2 | 900 | 40 / 42 | 34 / 40 | 30 / 32 | UPPERCASE |
| Heading/H3 | 900 | 24 / 28 | 22 / 28 | 20 / 24 | UPPERCASE |
| Heading/H4 | 900 | 20 / 24 | 19 / 24 | 18 / 24 | UPPERCASE |
| Body/Large | 400 | 19 / 30 | 18 / 28 | 18 / 28 | — |
| Body/Default | 400 | 17 / 28 | 16 / 24 | 16 / 24 | — |
| Body/Strong | 700 | 17 / 28 | 16 / 24 | 16 / 24 | — |
| Body/Small | 400 | 15 / 24 | 15 / 24 | 15 / 24 | — |
| Caption | 500 | 13 / 20 | 13 / 20 | 13 / 20 | — |
| Eyebrow | 800 | 13 / 16 | 12 / 16 | 12 / 16 | UPPERCASE, 16% |
| Label/Button | 800 | 15 / 24 | 15 / 24 | 15 / 24 | UPPERCASE, 6% |
| Label/Button Small | 800 | 13 / 16 | 13 / 16 | 13 / 16 | UPPERCASE, 6% |
| Label/Nav | 800 | 13 / 16 | 13 / 16 | 13 / 16 | UPPERCASE, 10% |
| Label/Tag | 800 | 11 / 16 | 11 / 16 | 11 / 16 | UPPERCASE, 10% |

Letter spacing in % equals em ÷ 100 (16% → 0.16em). In Elementor use `em`.

## 5. Components: Figma → Elementor

Put the class in the widget's **Advanced › CSS Classes**. Classes come from `components.css`.

| Figma component | Elementor widget | CSS class |
|---|---|---|
| Button / Primary | Button | `mliwl-btn-primary` |
| Button / Accent (gold) | Button | `mliwl-btn-accent` |
| Button / Outline | Button | `mliwl-btn-outline` |
| Button / Outline Inverse (on dark) | Button | `mliwl-btn-outline-inverse` |
| Button / Size Small | Button | add `mliwl-btn-sm` |
| Text Field, Select, Checkbox, Radio | Form (Elementor Pro) | `mliwl-form` on the widget |
| Tag | Text Editor / HTML | `<span class="mliwl-tag">` (+ `mliwl-tag-inverse`, `-highlight`, `-on-image`) |
| Chip (filters) | HTML or a filter plugin | `<button class="mliwl-chip" aria-pressed="false">` inside `.mliwl-chip-group` |
| Story / Lesson / Person / Partner / Article Card | Container (or Loop Item template) | `mliwl-card` on the container |
| Crisis Bar | Header template, top container | `mliwl-crisis-bar` |
| Section/Crisis Strip | Container | `mliwl-crisis-strip` |
| Header, Footer, Section/Get Help, Section/Newsletter | **Theme Builder templates** (header, footer) and **saved Templates** (sections) | — build once, insert everywhere |
| Dialog (Read bio) | Popup (Elementor Pro) | — Popup settings: close on Escape, focus trap on |

Build each repeated section once as a saved Template and insert it as a Template widget; editing the template updates every page, just like the Figma components.

## 6. Accessibility checks in Elementor

- Every Button widget: link text says where it goes (“Watch Kyle’s story”, not “Play”).
- Icon-only buttons: set the aria-label in Advanced › Attributes (`aria-label|Close menu`).
- Images: set alt text in the media library; decorative images get empty alt.
- Headings: one H1 per page; pick the HTML tag in the Heading widget, not only the size.
- Phone links: `tel:988`, `sms:988`, `sms:741741?&body=HOME`.
- Test with the keyboard (Tab, Shift+Tab, Enter, Escape) on every page before publishing.
