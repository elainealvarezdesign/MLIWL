# My Life Is Worth Living — website

Design system and WordPress plugin for [mylifeisworthliving.org](https://mylifeisworthliving.org), which runs on **WordPress + Elementor**.

Design source: Figma file **Design System - MLIWL** (`pji462RDmAcvludSloZL2w`). Figma variables are the source of truth for every color, size and font.

## What's here

| Path | Contents |
|---|---|
| `tokens/figma-export.json` | Variables, text styles and shadows exported from Figma |
| `tokens/build.py` | Builds `tokens/dist/tokens.css` (CSS variables) and `tokens/dist/mliwl.tokens.json` (W3C format) |
| `plugin/mliwl-design-system/` | WordPress plugin: loads Montserrat, `tokens.css`, `components.css` and the mobile-menu script. Works with Astra (the current theme) or any other theme |
| `plugin/mliwl-design-system/assets/css/components.css` | Component classes (`mliwl-btn-primary`, `mliwl-tag`, `mliwl-chip`, `mliwl-form`, `mliwl-card`…) to use from Elementor's CSS Classes field |
| `DESIGN.md` | Design rules: principles, pages, layout, color, type, components, content and accessibility |
| `docs/elementor-setup.md` | Elementor breakpoints, Global Colors, Global Fonts and the Figma → Elementor component map |
| `site/` | The website pages built from Figma, as static HTML using the plugin CSS (start with `site/index.html`, the Home) |
| `plugin/mliwl-design-system/assets/css/sections.css` | Page section styles (hero, featured story, audience cards, stories, newsletter, about, get help) |
| `elementor/templates/` + `build_templates.py` | Elementor Pro templates: header, footer and mobile menu popup |
| `docs/elementor-templates.md` | How to import and publish those templates |
| `docs/staging-install.md` | Step-by-step install and test on a staging copy |
| `catalog/index.html` | Static page with every component, to review in a browser |
| `catalog/header-footer.html` | Static preview of the header, footer and mobile menu styles |

## Update tokens after a Figma change

```bash
python3 tokens/build.py tokens/figma-export.json tokens/dist
cp tokens/dist/tokens.css plugin/mliwl-design-system/assets/css/tokens.css
```

Then update Elementor's Global Colors and Global Fonts if those values changed (see `docs/elementor-setup.md`).

## Install on WordPress

Full steps: [docs/staging-install.md](docs/staging-install.md). The site keeps its current theme (Astra); nothing is switched.

1. Zip `plugin/mliwl-design-system/` and upload it in Plugins › Add New › Upload Plugin. Activate it on staging first.
2. Elementor Pro is required for the header, footer and mobile menu templates.
3. Follow `docs/elementor-setup.md`.
