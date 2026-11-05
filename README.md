# My Life Is Worth Living — website

Design system and WordPress child theme for [mylifeisworthliving.org](https://mylifeisworthliving.org), which runs on **WordPress + Elementor**.

Design source: Figma file **Design System - MLIWL** (`pji462RDmAcvludSloZL2w`). Figma variables are the source of truth for every color, size and font.

## What's here

| Path | Contents |
|---|---|
| `tokens/figma-export.json` | Variables, text styles and shadows exported from Figma |
| `tokens/build.py` | Builds `tokens/dist/tokens.css` (CSS variables) and `tokens/dist/mliwl.tokens.json` (W3C format) |
| `theme/mliwl-child/` | Hello Elementor child theme: loads Montserrat, `tokens.css` and `components.css` on the site and in the editor |
| `theme/mliwl-child/assets/css/components.css` | Component classes (`mliwl-btn-primary`, `mliwl-tag`, `mliwl-chip`, `mliwl-form`, `mliwl-card`…) to use from Elementor's CSS Classes field |
| `DESIGN.md` | Design rules: principles, pages, layout, color, type, components, content and accessibility |
| `docs/elementor-setup.md` | Elementor breakpoints, Global Colors, Global Fonts and the Figma → Elementor component map |
| `catalog/index.html` | Static page with every component, to review in a browser |

## Update tokens after a Figma change

```bash
python3 tokens/build.py tokens/figma-export.json tokens/dist
cp tokens/dist/tokens.css theme/mliwl-child/assets/css/tokens.css
```

Then update Elementor's Global Colors and Global Fonts if those values changed (see `docs/elementor-setup.md`).

## Install on WordPress

1. Install and keep **Hello Elementor** as the parent theme.
2. Zip `theme/mliwl-child/` and upload it in Appearance › Themes › Add New › Upload. Activate it on staging first.
3. Follow `docs/elementor-setup.md`.
