# Header, footer and mobile menu templates

Three Elementor Pro templates, in `elementor/templates/`:

| File | Elementor type | What it is | Figma |
|---|---|---|---|
| `mliwl-header.json` | Header | Crisis bar (988) + logo, main nav, Get help, video language, Menu button | Crisis Bar, Header |
| `mliwl-footer.json` | Footer | Brand, Explore, Follow, Need help now?, legal line | Footer |
| `mliwl-mobile-menu.json` | Popup | Full-screen phone/tablet menu with 988 block | Mobile Menu, Menu Item |

The templates hold structure, copy and links only. Colors, type and spacing come from the child theme
(`tokens.css` + `components.css`) through CSS classes, so a Figma change never has to be redone by hand in Elementor.
To change the templates, edit `elementor/build_templates.py` and run `python3 elementor/build_templates.py`.

## Before you import

1. The **MLIWL child theme** is active (see `docs/elementor-setup.md`).
2. **Menu:** Appearance › Menus › create a menu named **Main** with: Watch (`/stories`), For parents (`/parents`), For educators (`/educators`), About (`/about`).
3. **Logo:** Site Settings › Site Identity › Site Logo: upload the MLIWL logo (alt text: "My Life Is Worth Living").

## Import (staging first)

Templates › Saved Templates › **Import Templates** › choose each JSON file. Then:

### Header
1. Templates › Theme Builder › Header › open **MLIWL Header**.
2. Click the Nav Menu widget and pick the **Main** menu (imports can't carry the menu ID).
3. Publish › Display Conditions › **Entire Site**.
4. Unpublish or remove the old header so only one header applies.

### Footer
1. Open **MLIWL Footer**.
2. Lovell Foundation image: choose the logo from the Media Library (alt text is already set).
3. Follow links: replace the four social URLs with the real MLIWL accounts. They point to the platforms' home pages now.
4. Publish › Display Conditions › **Entire Site**.

### Mobile menu popup
1. Open **MLIWL Mobile Menu**. Pick the **Main** menu in the Nav Menu widget.
2. Publish › Conditions › **Entire Site**. Triggers: **none**. Advanced rules: none.
3. Keep the title exactly **MLIWL Mobile Menu**: the child theme finds the popup by that title and wires the header's Menu button to it (`assets/js/mobile-menu.js`). No popup ID has to be copied anywhere.
4. Popup settings to confirm after import: width 100vw, height fit to screen, position top/center, close button inside, close on Escape on, no entrance animation.

## What happens on each device

| | Desktop ≥1024 | Tablet 768–1023 | Mobile ≤767 |
|---|---|---|---|
| Crisis bar | Full message, 56px | Full message (wraps) | "Need help now? Call 988 · Text 988", 64px |
| Header | 96px: logo, nav, Get help now, language | 80px: logo, Get help now, menu icon | 80px: logo, Get help, menu icon |
| Footer | 4 columns | 2 columns | 1 column |

## Checks after publishing

- Keyboard: Tab reaches the crisis links first, then logo, nav, Get help, language. On a phone-width window, the menu icon opens the popup, Escape closes it and focus returns to the menu icon.
- Current page: the nav underlines the page you're on (Elementor marks it active).
- `tel:` and `sms:` links open the dialer and messages on a phone.
- Screen reader: the menu icon reads "Open menu"; the language select reads "Video language".

## Testing note

The JSON uses Elementor 4.3.6 control names, checked against Elementor's source. The CSS was checked with
`catalog/header-footer.html`, a static copy of the markup these widgets produce, at 375, 800 and 1280px.
The import itself has not been run on a WordPress site yet: do it on staging first and report anything that doesn't import cleanly.
