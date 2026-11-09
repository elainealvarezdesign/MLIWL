"""Assemble the static pages: src/*.html + partials/*.html -> *.html

Usage: python3 site/build_pages.py
In a source page:
  <!-- @include header -->   inserts partials/header.html
  <!-- @page watch -->        marks the current page (nav link gets aria-current)
Nav links in the header use {{nav:NAME}} for their href, resolved from NAV below.
"""
import os, re
HERE = os.path.dirname(os.path.abspath(__file__))
NAV = {"watch": "watch.html", "parents": "parents.html", "educators": "educators.html", "about": "about.html", "team": "team.html", "partners": "partners.html", "news": "news.html", "help": "get-help.html"}  # fill in as pages are built

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

# Story pages: src/_story.tpl filled from STORIES -> story-<slug>.html
# (keep in step with the stories array in assets/site.js; on WordPress these are Story posts)
STORIES = [
    dict(slug="amie", title="Amie’s story", count=4, note="suicide attempt", lesson="lesson plan",
         desc="When negative thoughts keep haunting a teenage suicide survivor, the support of her family and boyfriend helps her find purpose."),
    dict(slug="kyle", title="Kyle’s story", count=4, note="bullying, alcohol use", lesson="lesson plan",
         desc="Bullied at school, a teen turns to alcohol to drown out the bad feelings and his own negative voice."),
    dict(slug="dante", title="Dante’s story", count=4, note="identity, family conflict", lesson="lesson plan",
         desc="A football star’s struggles with identity and an overbearing father challenge him to accept support."),
    dict(slug="danny", title="Danny’s story", count=4, note="serious injury, trauma", lesson="lesson plan",
         desc="After a life-changing accident, a teen learns to rely on his network of supporters."),
    dict(slug="emily", title="Emily’s story", count=4, note="abuse at home", lesson="lesson plan",
         desc="Escaping an abusive home, a teen protects her own wellbeing while shielding her mother from the truth."),
    dict(slug="kaia", title="Kaia’s story", count=2, note="low self-esteem, body image", lesson="lesson plan",
         desc="Low self-esteem makes Kaia feel she doesn’t measure up, until she finds hope in the people she loves."),
    dict(slug="vince", title="Vince’s story", count=2, note="body image, anxiety", lesson="lesson plan",
         desc="Asked to be a groomsman, Vince can’t stand people looking at him. His brother’s support is crucial."),
    dict(slug="raquelle", title="Are You OK?", count="[N]", note="bullying", lesson="classroom activities",
         desc="[CLIENT TO PROVIDE: one-sentence summary of Raquelle’s story]"),
]

def build_stories():
    tpl = open(os.path.join(HERE, "src", "_story.tpl"), encoding="utf-8").read()
    for st in STORIES:
        n = st["count"] if isinstance(st["count"], int) else 4
        current = ' aria-current="true"'  # no backslashes inside f-string braces: Python < 3.12 rejects them
        rows = "\n".join(
            f'          <li><button class="mliwl-episode" type="button" data-episode="{i}"{current if i == 1 else ""}>'
            f'<span class="mliwl-episode-thumb" aria-hidden="true"><svg><use href="#i-play"/></svg></span>'
            f'<span class="mliwl-episode-text"><span class="mliwl-caps-link">Episode {i}<span class="mliwl-now"> · Now playing</span></span>'
            f'<span class="text-body-strong">[Episode {i} title]</span><span class="text-caption mliwl-muted-text">[mm:ss]</span></span></button></li>'
            for i in range(1, n + 1))
        fields = dict(st, episodes=f"{st['count']} episodes", episode_rows=rows,
                      lesson_title=st["lesson"][0].upper() + st["lesson"][1:])
        out = re.sub(r"\{\{(\w+)\}\}", lambda m: str(fields.get(m.group(1), m.group(0))), tpl)
        tmp = f"_tmp_story_{st['slug']}.html"
        open(os.path.join(HERE, "src", tmp), "w", encoding="utf-8").write(out)
        build(tmp)
        os.replace(os.path.join(HERE, tmp), os.path.join(HERE, f"story-{st['slug']}.html"))
        os.remove(os.path.join(HERE, "src", tmp))
        print("  -> story-" + st["slug"] + ".html")

for f in sorted(os.listdir(os.path.join(HERE, "src"))):
    if f.endswith(".html") and not f.startswith("_"):
        build(f)
build_stories()
