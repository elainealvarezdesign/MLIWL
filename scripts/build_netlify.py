"""Build the static prototype into dist/ for Netlify.

Usage: python3 scripts/build_netlify.py
- Rebuilds the pages from site/src (site/build_pages.py)
- Copies site/*.html and site/assets into dist/
- Copies the plugin CSS (tokens, components, sections) into dist/assets/css
  and points the pages at it, so dist/ works on its own
Standard library only: runs on Netlify's default build image.
"""
import os, re, shutil, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(ROOT, "site")
PLUGIN_CSS = os.path.join(ROOT, "plugin", "mliwl-design-system", "assets", "css")
DIST = os.path.join(ROOT, "dist")

subprocess.run([sys.executable, os.path.join(SITE, "build_pages.py")], check=True, stdout=subprocess.DEVNULL)

shutil.rmtree(DIST, ignore_errors=True)
shutil.copytree(os.path.join(SITE, "assets"), os.path.join(DIST, "assets"))
os.makedirs(os.path.join(DIST, "assets", "css"), exist_ok=True)
for name in ("tokens.css", "components.css", "sections.css"):
    shutil.copy(os.path.join(PLUGIN_CSS, name), os.path.join(DIST, "assets", "css", name))
# sections.css uses ../img/zip-tone.png, which resolves to assets/img/ in dist as well.

pages = sorted(f for f in os.listdir(SITE) if f.endswith(".html"))
for page in pages:
    html = open(os.path.join(SITE, page), encoding="utf-8").read()
    html = html.replace("../plugin/mliwl-design-system/assets/css/", "assets/css/")
    if "../" in re.sub(r"<!--.*?-->", "", html, flags=re.S):
        raise SystemExit(f"{page}: a path still points outside site/")
    open(os.path.join(DIST, page), "w", encoding="utf-8").write(html)

shutil.copy(os.path.join(SITE, "robots.txt"), os.path.join(DIST, "robots.txt"))

print(f"dist/: {len(pages)} pages, CSS from the plugin, assets copied")
