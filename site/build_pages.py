"""Assemble the static pages: src/*.html + partials/*.html -> *.html

Usage: python3 site/build_pages.py
In a source page:
  <!-- @include header -->   inserts partials/header.html
  <!-- @page watch -->        marks the current page (nav link gets aria-current)
Nav links in the header use {{nav:NAME}} for their href, resolved from NAV below.
"""
import os, re
HERE = os.path.dirname(os.path.abspath(__file__))
NAV = {"watch": "watch.html", "parents": "parents.html", "educators": "educators.html", "about": "about.html", "team": "team.html", "partners": "partners.html", "news": "news.html"}  # fill in as pages are built

def build(name):
    src = open(os.path.join(HERE, "src", name), encoding="utf-8").read()
    page = (re.search(r"<!-- @page (\w+) -->", src) or [None, None])[1]
    out = re.sub(r"<!-- @include ([\w-]+) -->",
                 lambda m: open(os.path.join(HERE, "partials", m.group(1) + ".html"), encoding="utf-8").read().rstrip("\n"), src)
    out = re.sub(r"\{\{nav:(\w+)\}\}", lambda m: NAV.get(m.group(1), "#"), out)
    if page:
        out = out.replace(f'class="elementor-item" data-nav="{page}"', f'class="elementor-item elementor-item-active" aria-current="page" data-nav="{page}"')
    out = re.sub(r"<!-- @page \w+ -->\n?", "", out)
    open(os.path.join(HERE, name), "w", encoding="utf-8").write(out)
    print("built", name)

for f in sorted(os.listdir(os.path.join(HERE, "src"))):
    if f.endswith(".html"):
        build(f)
