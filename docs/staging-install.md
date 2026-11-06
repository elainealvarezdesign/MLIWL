# Install on staging

Step-by-step to try the MLIWL Design System plugin and templates on a **staging copy** of mylifeisworthliving.org.
Nothing here touches the live site. Plan about 1 hour.

The site keeps its current theme (**Astra** with `astra-child`). The package is a plugin, so there is no theme switch.

## 0. What you need

- A staging copy of the site: your host's **Create staging** tool, or the free **WP Staging** plugin.
- Admin login on staging.
- **Elementor Pro** active and licensed on staging (Templates › Theme Builder must be available).
- The package from GitHub: open the repo, pick the branch `claude/keen-knuth-y433vw`, then **Code › Download ZIP**, and unzip it.

## 1. Create and protect the staging site

1. Create the staging copy from your host's panel (or WP Staging › Create new staging site).
2. Settings › Reading › tick **Discourage search engines from indexing this site**.

## 2. Check versions

Dashboard › Updates: update WordPress, Astra, Elementor and Elementor Pro on staging. Templates were built against Elementor 4.3.

## 3. Install the plugin

1. From the downloaded package, zip the folder `plugin/mliwl-design-system` so the zip contains `mliwl-design-system/mliwl-design-system.php` at its top level.
2. Plugins › Add New › **Upload Plugin** › choose `mliwl-design-system.zip` › Install › **Activate**.
3. Open a few pages. Expect body text to switch to Montserrat. Nothing else should change yet: the new header and footer come in step 7.

## 4. Elementor site settings

Follow `docs/elementor-setup.md`:

1. Elementor › Site Settings › Layout › **Breakpoints**: Tablet = **1023**.
2. Layout › Content width **1200px**.
3. Design System › **Global Colors** and **Global Fonts**: enter the values from the tables.

## 5. Menu and logo

1. Appearance › Menus › create **Main**: Watch `/stories`, For parents `/parents`, For educators `/educators`, About `/about`.
   On staging, if those pages don't exist yet, point them at the current pages (Watch, Parent Guidance, Lessons, About).
2. Elementor › Site Settings › Site Identity › **Site Logo**: upload the logo, alt text "My Life Is Worth Living".

## 6. Import the templates

Templates › Saved Templates › **Import Templates** and import, one at a time:
`elementor/templates/mliwl-header.json`, `mliwl-footer.json`, `mliwl-mobile-menu.json`.

## 7. Publish header, footer and mobile menu

Follow `docs/elementor-templates.md`. In short:

1. **Header**: open it, pick the **Main** menu in the Nav Menu widget, Publish › Conditions › **Entire Site**.
2. **Footer**: choose the Lovell Foundation logo image, replace the 4 social URLs, Publish › **Entire Site**.
3. **Mobile Menu** popup: pick the **Main** menu, Publish › Conditions **Entire Site**, Triggers **none**. Keep the title exactly *MLIWL Mobile Menu*.
4. Theme Builder: make sure no other header or footer template is still active.
5. Astra steps aside automatically when an Elementor Pro header and footer are published. If the old Astra header still shows above the new one, check the page isn't using an Astra "custom layout" or a page-level header setting.

## 8. Clear caches

1. Elementor › Tools › **Regenerate CSS & Data**.
2. Clear any cache plugin and the host or CDN cache.

## 9. Test

On a desktop browser, a tablet (or a window about 800px wide) and a phone:

- [ ] Crisis bar shows on every page; on a phone, **Call 988** opens the dialer and **Text 988** opens messages.
- [ ] Header: nav on desktop; menu icon on tablet and phone opens the full-screen menu; **Escape** closes it.
- [ ] Keyboard only: Tab moves through crisis links, logo, nav, Get help, language; the gold focus ring is visible.
- [ ] Footer: 4 columns on desktop, 2 on tablet, 1 on phone; all links work.
- [ ] Existing pages still look right. The plugin sets the body font and page background site-wide; check pages that relied on Astra's fonts or colors.
- [ ] No errors in the browser console.

Write down anything that looks wrong (page, device, screenshot) and send it over; fixes go into the same pull request.

## Roll back

1. Theme Builder: unpublish the MLIWL header and footer (or set their conditions to none). Astra's header and footer come back.
2. Plugins › **Deactivate** MLIWL Design System.

The imported templates and Elementor settings can stay on staging.
