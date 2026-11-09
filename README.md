# My Life Is Worth Living — website

Design system, WordPress plugin and clickable prototype for [mylifeisworthliving.org](https://mylifeisworthliving.org), a free animated series about teen mental health.

**Prototype:** https://mliwl.netlify.app (published from `main` by Netlify)

The live site runs on **WordPress + Elementor**; this repo holds the design tokens, the plugin that styles it, Elementor templates and a static HTML prototype of every page.

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
| `site/` | The prototype: every page built from Figma as static HTML using the plugin CSS. Edit `site/src/` and `site/partials/`, then run `python3 site/build_pages.py` |
| `scripts/build_netlify.py` + `netlify.toml` | Builds the prototype into `dist/` and publishes it on Netlify |
| `plugin/mliwl-design-system/assets/css/sections.css` | Page section styles (hero, featured story, audience cards, stories, newsletter, about, get help) |
| `elementor/templates/` + `build_templates.py` | Elementor Pro templates: header, footer and mobile menu popup |
| `docs/elementor-templates.md` | How to import and publish those templates |
| `docs/staging-install.md` | Step-by-step install and test on a staging copy |
| `catalog/index.html` | Static page with every component, to review in a browser |
| `catalog/header-footer.html` | Static preview of the header, footer and mobile menu styles |

## Prototype on Netlify

The prototype is published at **https://mliwl.netlify.app** from this repo with Netlify. `netlify.toml` holds the settings, so nothing has to be typed in Netlify's UI:

| Setting | Value |
|---|---|
| Build command | `python3 scripts/build_netlify.py` |
| Publish directory | `dist` |
| Production branch | `main` |

- Each pull request gets its own **Deploy Preview** link from Netlify.
- Every page sends `X-Robots-Tag: noindex` and `robots.txt` blocks crawlers, because the copy is still placeholder. Remove both before using it as a public site.
- Build locally: `python3 scripts/build_netlify.py`, then open `dist/index.html` or run `python3 -m http.server -d dist`.

Pages: Home, Watch, the 8 story pages, For parents, For educators, Get help, About, Meet the team, Partners, News & media. Still to build: Privacy and 404.

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
