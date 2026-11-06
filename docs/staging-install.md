# Install on staging

Step-by-step to try the MLIWL child theme and templates on a **staging copy** of mylifeisworthliving.org.
Nothing here touches the live site. Plan about 1–2 hours.

> **Important: the live site uses the Astra theme** (with an `astra-child` theme), not Hello Elementor.
> This package is a child theme of **Hello Elementor**, so installing it means switching themes on staging.
> Before step 4, check `astra-child/functions.php` for custom code (tracking snippets, shortcodes, redirects)
> that would need to move over. If switching themes is not an option, ask for the plugin version of this
> package instead: same CSS and templates, works with Astra.

## 0. What you need

- A staging copy of the site: your host's **Create staging** tool, or the free **WP Staging** plugin.
- Admin login on staging.
- **Elementor Pro** active and licensed on staging (Templates › Theme Builder must be available).
- The package from GitHub: open the repo, pick the branch `claude/keen-knuth-y433vw`, then **Code › Download ZIP**, and unzip it.

## 1. Create and protect the staging site

1. Create the staging copy from your host's panel (or WP Staging › Create new staging site).
2. Settings › Reading › tick **Discourage search engines from indexing this site**.
3. Note the active theme (Appearance › Themes) so you can switch back: it should be **Astra Child**.

## 2. Check versions

Dashboard › Updates: update WordPress, Elementor and Elementor Pro on staging. Templates were built against Elementor 4.3.

## 3. Install the parent theme

Appearance › Themes › Add New › search **Hello Elementor** › **Install**. Do not activate it.

## 4. Install the MLIWL child theme

1. From the downloaded package, zip the folder `theme/mliwl-child` so the zip contains `mliwl-child/style.css` at its top level.
2. Appearance › Themes › Add New › **Upload Theme** › choose `mliwl-child.zip` › Install › **Activate**.
3. Open a few pages. Expect the old Astra header and footer to disappear (the new ones come in step 8) and Montserrat to load.

## 5. Elementor site settings

Follow `docs/elementor-setup.md`:

1. Elementor › Site Settings › Layout › **Breakpoints**: Tablet = **1023**.
2. Layout › Content width **1200px**.
3. Design System › **Global Colors** and **Global Fonts**: enter the values from the tables.

## 6. Menu and logo

1. Appearance › Menus › create **Main**: Watch `/stories`, For parents `/parents`, For educators `/educators`, About `/about`.
   On staging, if those pages don't exist yet, point them at the current pages (Watch, Parent Guidance, Lessons, About).
2. Elementor › Site Settings › Site Identity › **Site Logo**: upload the logo, alt text "My Life Is Worth Living".

## 7. Import the templates

Templates › Saved Templates › **Import Templates** and import, one at a time:
`elementor/templates/mliwl-header.json`, `mliwl-footer.json`, `mliwl-mobile-menu.json`.

## 8. Publish header, footer and mobile menu

Follow `docs/elementor-templates.md`. In short:

1. **Header**: open it, pick the **Main** menu in the Nav Menu widget, Publish › Conditions › **Entire Site**.
2. **Footer**: choose the Lovell Foundation logo image, replace the 4 social URLs, Publish › **Entire Site**.
3. **Mobile Menu** popup: pick the **Main** menu, Publish › Conditions **Entire Site**, Triggers **none**. Keep the title exactly *MLIWL Mobile Menu*.
4. Theme Builder: make sure no other header or footer is still active.

## 9. Clear caches

1. Elementor › Tools › **Regenerate CSS & Data**.
2. Clear any cache plugin and the host or CDN cache.

## 10. Test

On a desktop browser, a tablet (or a window about 800px wide) and a phone:

- [ ] Crisis bar shows on every page; on a phone, **Call 988** opens the dialer and **Text 988** opens messages.
- [ ] Header: nav on desktop; menu icon on tablet and phone opens the full-screen menu; **Escape** closes it.
- [ ] Keyboard only: Tab moves through crisis links, logo, nav, Get help, language; the gold focus ring is visible.
- [ ] Footer: 4 columns on desktop, 2 on tablet, 1 on phone; all links work.
- [ ] Existing pages still look right with the new theme (watch for layout, fonts, spacing and any Astra-only features).
- [ ] No errors in the browser console.

Write down anything that looks wrong (page, device, screenshot) and send it over; fixes go into the same pull request.

## Roll back

Appearance › Themes › activate **Astra Child** again. In Theme Builder, unpublish the MLIWL header and footer (or set their conditions to none).
Nothing else needs undoing; the imported templates and settings can stay on staging.
