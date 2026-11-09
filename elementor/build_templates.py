"""Build the Elementor Pro templates (header, footer, mobile menu popup) for MLIWL.

Usage: python3 elementor/build_templates.py
Writes elementor/templates/*.json (Elementor template export format, version 0.4).

The templates carry structure, copy and links only. Colors, type and spacing come
from the MLIWL Design System plugin (tokens.css + components.css) through the CSS classes below,
so Figma stays the single source for visual values.
"""
import hashlib
import json
import os

OUT = os.path.join(os.path.dirname(__file__), "templates")
_seq = [0]


def uid(seed):
    _seq[0] += 1
    return hashlib.md5(f"{seed}-{_seq[0]}".encode()).hexdigest()[:7]


def px(v):
    return {"unit": "px", "size": v, "sizes": []}


def box(t, r, b, l):
    return {"unit": "px", "top": str(t), "right": str(r), "bottom": str(b), "left": str(l), "isLinked": False}


def gap(v):
    return {"unit": "px", "size": v, "column": str(v), "row": str(v), "isLinked": True}


def container(name, children, css="", direction="row", justify="", align="", wrap="", g=None, full=True,
              padding=None, tag="", hide=(), extra=None, inner=False):
    s = {"_title": name, "content_width": "full" if full else "boxed", "flex_direction": direction}
    if css:
        s["css_classes"] = css
    if justify:
        s["flex_justify_content"] = justify
    if align:
        s["flex_align_items"] = align
    if wrap:
        s["flex_wrap"] = wrap
    if g is not None:
        s["flex_gap"] = gap(g)
    if padding is not None:
        s["padding"] = box(*padding)
    if tag:
        s["html_tag"] = tag
    for d in hide:
        s[f"hide_{d}"] = f"hidden-{d}"
    if extra:
        s.update(extra)
    return {"id": uid(name), "elType": "container", "settings": s, "elements": children, "isInner": inner}


def widget(kind, name, settings, css="", hide=()):
    s = dict(settings)
    s["_title"] = name
    if css:
        s["_css_classes"] = css
    for d in hide:
        s[f"hide_{d}"] = f"hidden-{d}"
    return {"id": uid(name), "elType": "widget", "widgetType": kind, "settings": s, "elements": []}


def link(url, external=False):
    return {"url": url, "is_external": "on" if external else "", "nofollow": "", "custom_attributes": ""}


def button(name, text, url, css, external=False, aria="", icon=None, hide=()):
    s = {"text": text, "link": link(url, external)}
    if aria:
        s["link"]["custom_attributes"] = f"aria-label|{aria}"
    if icon:
        s["selected_icon"] = icon
    return widget("button", name, s, css=css, hide=hide)


def text(name, html, css="", hide=()):
    return widget("text-editor", name, {"editor": html}, css=css, hide=hide)


def heading(name, title, size="h2", css=""):
    return widget("heading", name, {"title": title, "header_size": size}, css=css)


def link_list(name, items, css=""):
    return widget("icon-list", name, {
        "view": "traditional",
        "icon_list": [{"_id": uid(name + t), "text": t, "selected_icon": {"value": "", "library": ""},
                       "link": link(u, ext)} for t, u, ext in items],
    }, css=css)


def site_logo(name, hide=()):
    # Elementor Pro "Site Logo": uses the logo set in Site Settings > Site Identity. Alt text = site name.
    return widget("theme-site-logo", name, {"link_to": "custom", "link": link("/")}, css="mliwl-logo", hide=hide)


def nav_menu(name, menu_slug, layout="horizontal", css="mliwl-nav", hide=()):
    # Elementor Pro "Nav Menu". dropdown=none: phones use the MLIWL Mobile Menu popup instead.
    return widget("nav-menu", name, {"menu": menu_slug, "layout": layout, "pointer": "none",
                                     "dropdown": "none", "submenu_icon": {"value": "", "library": ""}},
                  css=css, hide=hide)


LANG_SELECT = """<label class="mliwl-lang">
  <span class="screen-reader-text">Video language</span>
  <select onchange="if(this.value){window.location.href=this.value}">
    <option value="/stories" selected>English</option>
    <option value="/stories?lang=es" lang="es">Español</option>
    <option value="/stories?lang=pt" lang="pt">Português</option>
    <option value="/stories?lang=ja" lang="ja">日本語</option>
    <option value="/stories?lang=zh" lang="zh">中文</option>
  </select>
</label>"""

CRISIS_DESKTOP = ('<p><strong>Struggling right now? You are not alone.</strong> '
                  '<a href="tel:988">Call 988</a> <a href="sms:988">Text 988</a> '
                  '<span class="mliwl-crisis-note">Free and confidential, 24/7 in the U.S.</span> '
                  '<a href="https://findahelpline.com" target="_blank" rel="noopener">Outside the U.S.? Find a helpline<span class="screen-reader-text"> (opens in a new tab)</span></a></p>')
CRISIS_MOBILE = '<p><strong>Need help now?</strong> <a href="tel:988">Call 988</a> <a href="sms:988">Text 988</a></p>'

NAV_ITEMS = [("Watch", "/stories"), ("For parents", "/parents"), ("For educators", "/educators"), ("About", "/about")]


def doc(title, kind, content, page_settings=None):
    return {"content": content, "page_settings": page_settings or [], "version": "0.4", "title": title, "type": kind}


# ---------- Header ----------
header = doc("MLIWL Header", "header", [
    container("Crisis bar", [
        text("Crisis message (desktop, tablet)", CRISIS_DESKTOP, hide=("mobile",)),
        text("Crisis message (mobile)", CRISIS_MOBILE, hide=("desktop", "tablet")),
    ], css="mliwl-crisis-bar", justify="center", align="center", padding=(0, 0, 0, 0), tag="aside",
        extra={"_element_id": "crisis-bar"}),
    container("Header", [
        site_logo("Logo"),
        container("Header actions", [
            nav_menu("Main navigation", "main", hide=("tablet", "mobile")),
            button("Get help now (desktop, tablet)", "Get help now", "/get-help", "mliwl-btn-primary mliwl-btn-sm", hide=("mobile",)),
            button("Get help (mobile)", "Get help", "/get-help", "mliwl-btn-primary mliwl-btn-sm", hide=("desktop", "tablet")),
            widget("html", "Video language", {"html": LANG_SELECT}, hide=("tablet", "mobile")),
            button("Menu button", "", "#mliwl-open-menu", "mliwl-menu-button", aria="Open menu",
                   icon={"value": "fas fa-bars", "library": "fa-solid"}, hide=("desktop",)),
        ], css="mliwl-header-actions", justify="flex-end", align="center", g=24, padding=(0, 0, 0, 0), inner=True,
            extra={"flex_gap_mobile": gap(12)}),
    ], css="mliwl-header", justify="space-between", align="center", g=24, full=False, tag="header"),
])

# ---------- Footer ----------
footer = doc("MLIWL Footer", "footer", [
    container("Footer", [
        container("Footer columns", [
            container("Brand", [
                site_logo("Logo"),
                text("Produced by", "<p>Produced by The Cook Center for Human Connection and Wonder Media.</p>"),
                text("Grant sponsor label", '<p class="mliwl-footer-label">Grant sponsor</p>'),
                widget("image", "Lovell Foundation logo", {"image": {"url": "", "id": "", "alt": "The David and Lura Lovell Foundation"},
                                                           "link_to": "custom", "link": link("https://lovellfoundation.org", True)}),
            ], css="mliwl-footer-col", direction="column", g=16, padding=(0, 0, 0, 0), inner=True),
            container("Explore", [
                heading("Explore heading", "Explore", "h2", css="mliwl-footer-heading"),
                link_list("Explore links", [("Watch", "/stories", False), ("Lessons for educators", "/educators", False),
                                            ("Parent playbooks", "/parents", False), ("About", "/about", False)]),
            ], css="mliwl-footer-col", direction="column", g=16, padding=(0, 0, 0, 0), tag="nav", inner=True,
                extra={"_element_id": "footer-explore"}),
            container("Follow", [
                heading("Follow heading", "Follow", "h2", css="mliwl-footer-heading"),
                link_list("Social links", [("YouTube", "https://www.youtube.com/", True), ("Instagram", "https://www.instagram.com/", True),
                                           ("TikTok", "https://www.tiktok.com/", True), ("Facebook", "https://www.facebook.com/", True)]),
            ], css="mliwl-footer-col", direction="column", g=16, padding=(0, 0, 0, 0), inner=True),
            container("Need help now", [
                heading("Help heading", "Need help now?", "h2", css="mliwl-footer-heading"),
                text("Help lines", '<p><a href="tel:988">Call</a> or <a href="sms:988">text 988</a> any time.</p>'
                                   '<p>Text HOME to <a href="sms:741741?&amp;body=HOME">741741</a>.</p>'
                                   '<p>Outside the U.S.: <a href="https://findahelpline.com" target="_blank" rel="noopener">findahelpline.com</a></p>'),
            ], css="mliwl-footer-col", direction="column", g=16, padding=(0, 0, 0, 0), inner=True),
        ], css="mliwl-footer-columns", wrap="wrap", g=24, padding=(0, 0, 0, 0), inner=True),
        container("Legal", [
            text("Legal text", '<p>© The Cook Center for Human Connection · <a href="/privacy">Privacy policy</a></p>'),
        ], css="mliwl-footer-legal", padding=(0, 0, 0, 0), inner=True),
    ], css="mliwl-footer", direction="column", g=40, full=False, tag="footer"),
])

# ---------- Mobile menu popup ----------
menu = doc("MLIWL Mobile Menu", "popup", [
    container("Mobile menu", [
        nav_menu("Menu links", "main", layout="vertical", css="mliwl-menu-items"),
        container("Video language", [
            text("Language label", '<p class="mliwl-footer-label">Video language</p>'),
            widget("html", "Language select", {"html": LANG_SELECT}),
        ], direction="column", g=8, padding=(0, 0, 0, 0), inner=True),
        container("Crisis help", [
            heading("Crisis heading", "Struggling right now?", "h2"),
            text("Crisis text", "<p>You are not alone. Free and confidential, 24/7 in the U.S.</p>"),
            container("Crisis buttons", [
                button("Call 988", "Call 988", "tel:988", "mliwl-btn-accent mliwl-btn-sm"),
                button("Text 988", "Text 988", "sms:988", "mliwl-btn-outline-inverse mliwl-btn-sm"),
            ], g=8, padding=(0, 0, 0, 0), inner=True),
            text("Outside the U.S.", '<p><a href="https://findahelpline.com" target="_blank" rel="noopener">Outside the U.S.? Find a helpline</a></p>'),
        ], css="mliwl-menu-crisis", direction="column", g=16, inner=True),
    ], css="mliwl-mobile-menu", direction="column", g=24, padding=(24, 16, 32, 16)),
], page_settings={"width": {"unit": "vw", "size": 100, "sizes": []},
                  "height_type": "fit_to_screen",
                  "horizontal_position": "center", "vertical_position": "top",
                  "close_button_position": "inside", "close_button_vertical": {"unit": "px", "size": 24, "sizes": []},
                  "close_button_horizontal": {"unit": "px", "size": 16, "sizes": []},
                  "prevent_close_on_esc_key": "", "avoid_multiple_popups": "yes",
                  "entrance_animation": "", "exit_animation": ""})

os.makedirs(OUT, exist_ok=True)
for name, d in [("mliwl-header", header), ("mliwl-footer", footer), ("mliwl-mobile-menu", menu)]:
    with open(os.path.join(OUT, name + ".json"), "w", encoding="utf-8") as f:
        json.dump(d, f, indent=2, ensure_ascii=False)
    print("wrote", name + ".json")
