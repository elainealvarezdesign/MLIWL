"""Assemble the static pages: src/*.html + partials/*.html -> *.html

Usage: python3 site/build_pages.py
In a source page:
  <!-- @include header -->   inserts partials/header.html
  <!-- @page watch -->        marks the current page (nav link gets aria-current)
Nav links in the header use {{nav:NAME}} for their href, resolved from NAV below.
"""
import html, json, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
NAV = {"watch": "watch.html", "parents": "parents.html", "educators": "educators.html", "about": "about.html", "team": "team.html", "partners": "partners.html", "news": "news.html", "help": "get-help.html", "privacy": "privacy.html"}  # fill in as pages are built

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
# Longer "about" text per story: verbatim from the current site's Lessons page (mylifeisworthliving.org/lessons, Nov 2026).
ABOUT = {
 "amie": [
  "Jam-packed days and meticulous planning help 16-year-old Amie stay organized and pursue her goals. They also help her forget that her parents treat her like she’s made of glass, and that her boyfriend worries about her. They help her forget the dark years of medications and diagnoses that led her to the hospital, and they help her ignore the negative thoughts that continue to darken the corners of her mind. With the help of her therapist, her family, and her boyfriend, Amie is learning that there’s no shame in continuing to struggle, that relying on the support of loved ones doesn’t make her a burden, and that a sense of hope and purpose can help her cope with negative thoughts."
 ],
 "kyle": [
  "Persistent bullying becomes a waking nightmare for 16-year-old Kyle, whose struggles with negative thinking take center stage when it seems like everyone at school is against him. Feeling trapped and alone, Kyle turns to alcohol to suppress the self-critical voice that echoes in his head. Kyle hides the bullying and the alcoholism from his father Mario, who he believes could never understand what he’s going through. Sensing that something is wrong, Mario shares about his own struggle with PTSD after the service, and helps Kyle get comfortable communicating about his feelings. Alcohol doesn’t numb the pain forever, but when his negative thoughts become overpowering again, Kyle finds that opening up about his struggle with people who care about him is a more powerful remedy than drinking could ever be."
 ],
 "dante": [
  "Negative thoughts become a world of despair for a high school football star, whose struggles with identity and an overbearing father challenge him to accept support from peers and from himself. Dante is outgoing with friends, confident in school, and a strong member of his football team; no one would suspect that he feels utterly depressed and trapped by the expectations of his family and peers. Now approaching graduation, Dante can no longer bear the pain of hiding his passions and his identity from his father and himself.",
  "As he struggles to overcome the feelings of hopelessness that have characterized his teen years, Dante will find unexpected allies in his football coach and the coach’s son, a mental health mentor. He will also learn that his conflicts with his father are not his fault, that he is strong enough to control the negative voice in his head, and that he is worthy of love and support."
 ],
 "danny": [
  "Danny has experienced life threatening physical trauma after a fire that happened in his home. Now that he is dealing with physical disability and visible physical difference, he is struggling greatly with his sense of self-worth. Before the accident, Danny was a music lover and a jokester, who loved messing with his little brother, Angel, of whom he was also highly protective. Since the accident, he’s lost interest in a lot of the things he used to love. He feels isolated from his now-distant peers and he feels guilty that his family has to see him struggling to adjust to his new life.",
  "With the support of his family and medical team, he is learning how to accept his new normal and openly communicate in hard times so that he stays safe and feels connected."
 ],
 "emily": [
  "Emily is a creative, sometimes introverted person that has a close relationship with her mother, Theresa. They frequently make each other laugh and have always been supportive of one another. When Emily’s mom started dating someone seriously last year, Emily was excited for her. She has loved seeing her mom so happy, feeling inspired by her capacity to balance career, love, and family.",
  "Recently, Emily has been trying to balance this important relationship with her mom with the new uneasiness she has been experiencing about her mom’s fiancé, Brandon. Recurring moments of discomfort with him have now become more recognizable as sexual abuse. Currently, Emily is struggling to connect with her mother about what is going on, feeling guilt and shame about what has been happening, and beginning to have suicidal thoughts. With the support of her best friend Shayla and Shayla’s mother Carla, she is able to feel supported enough to confide in her mother and know that her story matters."
 ],
 "kaia": [
  "Negative thoughts continue to creep into Kaia’s mind. She wants to accept all parts of herself – but her low self-esteem and lack of confidence make her feel like she does not measure up. She finds hope and no longer has to avoid social situations and activities due to her insecurities."
 ],
 "vince": [
  "When Vince must be a groomsman in his sister’s wedding, he begins to have negative thoughts. He can’t stand people looking at him. His insecurities start to bubble up, and his brother notices he may be overdoing it and struggling to accept all parts of himself – his brother’s support is crucial as he combats negative thoughts."
 ]
}

# Video lengths, read from the channel's YouTube page (screenshot from the client, Nov 2026). "?" = to confirm.
DURATION = {
 "HOvFQKGUfhE": "3:41", "-emjHyVSuwg": "5:28", "lJeRqYpjiRs": "4:21", "kPp-ABkfYgI": "4:36",
 "BVI7TgdnLRo": "1:18", "rx3X1VJqEq4": "5:05", "zqM-XCifn0o": "5:29", "X16x2TxAgmQ": "4:30", "HA3HBeDBUME": "5:11",
 "63b8BqdvpVc": "3:58", "eH3O9Snp5UI": "5:43", "C6IQDQFvf8o": "4:50", "HixhTwoEShg": "4:49", "n-8R8t-uUM4": "4:28",
 "qPROOH2vxxc": "1:00", "oR9LztZi_Yc": "6:04", "ukA7G-Xegsg": "5:36", "NNzdFqGC3M8": "4:42", "b0YYGUzc0gk": "5:11",
 "e7Zw3wF7a-8": "1:00", "8AdBvbjgFBo": "4:41", "6JmPWTu9kNs": "5:41", "_KzgMJhcmXo": "5:36", "igoYAbfphOE": "4:41",
 "HCY9eeS5IL4": "0:56", "gctypUcTLyg": "5:15", "rqZvp0gnsrM": "5:22",
 "eCPYIYrYwmw": "0:38", "CwLyLMSx81M": "4:03", "GzACs2yieGo": "5:46",
}
TOTAL_MIN = {"amie": 19}  # Amie episode 3 is not readable in the screenshot: total from her "complete story" video (18:57)

# Class activities PDFs from the client (Nov 2026), in assets/pdf/<slug>-class-activities.pdf
PDF_PAGES = {"amie": 8, "kyle": 8, "dante": 8, "danny": 8, "emily": 8, "kaia": 4, "vince": 4}
def pdf_info(slug):
    path = os.path.join(HERE, "assets", "pdf", f"{slug}-class-activities.pdf")
    if not os.path.isfile(path):
        return None
    mb = os.path.getsize(path) / 1_000_000
    return f"assets/pdf/{slug}-class-activities.pdf", (f"{mb:.1f} MB" if mb >= 1 else f"{round(mb * 1000)} KB")

def secs(d): m, s = d.split(":"); return int(m) * 60 + int(s)

STORIES = [
    dict(slug="amie", topic="Suicide survivor", name="Amie", alt="Amie, a teen with red braids and glasses, in a green cardigan", trailer=("HOvFQKGUfhE", "Amie Struggles With Depression and Perfectionism"), title="Amie’s story", count=4, note="suicide attempt", lesson="lesson plan",
         desc="When negative thoughts keep haunting a teenage suicide survivor, the support of her family and boyfriend helps her find purpose.",
         # (YouTube video id, episode title) from the client, Nov 11 2026
         videos=[("-emjHyVSuwg", "Amie Opens Up About Her Mental Health in Therapy"),
                 ("lJeRqYpjiRs", "Amie and Nick Struggle to Reconnect After Her Suicide Attempt"),
                 ("tjlKxi8oQ_w", "Amie Learns About Her Mom’s Struggle With Mental Health"),
                 ("kPp-ABkfYgI", "Amie Learns to Accept Help From Her Friends and Family")]),
    dict(slug="kyle", topic="Bullying + substance use", name="Kyle", alt="Kyle, a teen in a light blue hoodie with a backpack on one shoulder", trailer=("BVI7TgdnLRo", "Kyle Struggles With Bullying and Addiction"), title="Kyle’s story", count=4, note="bullying, alcohol use", lesson="lesson plan",
         desc="Bullied at school, a teen turns to alcohol to drown out the bad feelings and his own negative voice.",
         # (YouTube video id, episode title) from the client, Nov 24 2026
         videos=[("rx3X1VJqEq4", "Bullied at School, Kyle Turns to Alcohol to Cope"),
                 ("zqM-XCifn0o", "Online Bullying Fuels Kyle’s Self-Loathing"),
                 ("X16x2TxAgmQ", "Kyle Learns About Dad’s Military PTSD & Addiction"),
                 ("HA3HBeDBUME", "Kyle Learns How to Cope With Negative Self-Talk Through Therapy")]),
    dict(slug="dante", topic="LGBTQ+", name="Dante", alt="Dante, a teen in a purple jacket over a pink T-shirt", trailer=("63b8BqdvpVc", "Dante Struggles With Rejection and LGBTQ+ Acceptance"), title="Dante’s story", count=4, note="identity, family conflict", lesson="lesson plan",
         desc="A football star’s struggles with identity and an overbearing father challenge him to accept support.",
         # (YouTube video id, episode title) from the client, Nov 24 2026
         videos=[("eH3O9Snp5UI", "Dante Struggles With His Father’s Narrow Expectations"),
                 ("C6IQDQFvf8o", "Dante Worries His Teammates Will Reject His LGBTQ+ Identity"),
                 ("HixhTwoEShg", "Dante Learns How to Cope With His Negative Thoughts"),
                 ("n-8R8t-uUM4", "Dante Shares His Journey and Reconnects With His Dad")]),
    dict(slug="danny", topic="Trauma survivor", name="Danny", alt="Danny, a teen with glasses and a shaved side cut, in a brown jacket and navy hoodie", trailer=("qPROOH2vxxc", "Danny Learns a New Normal"), title="Danny’s story", count=4, note="serious injury, trauma", lesson="lesson plan",
         desc="After a life-changing accident, a teen learns to rely on his network of supporters.",
         # (YouTube video id, episode title) from the client, Nov 24 2026
         videos=[("oR9LztZi_Yc", "Danny’s Inspiring Road to Recovery as a Burn Survivor"),
                 ("ukA7G-Xegsg", "Danny Is Given a Safety Plan to Help Him Cope With His Trauma"),
                 ("NNzdFqGC3M8", "Danny Reaches Out When He Needs Help"),
                 ("b0YYGUzc0gk", "Danny Is Ready to Embrace His Life After Trauma")]),
    dict(slug="emily", topic="Abuse", name="Emily", alt="Emily, a teen with two hair puffs, a choker and a green backpack", trailer=("e7Zw3wF7a-8", "Emily Shares Her Story to Stop Abuse"), title="Emily’s story", count=4, note="abuse at home", lesson="lesson plan",
         desc="Escaping an abusive home, a teen protects her own wellbeing while shielding her mother from the truth.",
         # (YouTube video id, episode title) from the client, Nov 24 2026
         videos=[("8AdBvbjgFBo", "Emily Uses Her Support Network to Escape Abuse"),
                 ("6JmPWTu9kNs", "Emily Shares Her Story With a Friend"),
                 ("_KzgMJhcmXo", "Emily Opens Up About the Abuse to a Trusted Adult"),
                 ("igoYAbfphOE", "Emily Learns Coping Skills as She Continues to Adjust to New Home")]),
    dict(slug="kaia", topic="Body image", name="Kaia", alt="Kaia, a teen with a ponytail and glasses, in a black T-shirt and a necklace", trailer=("HCY9eeS5IL4", "Introducing Kaia’s Story"), title="Kaia’s story", count=2, note="low self-esteem, body image", lesson="lesson plan",
         desc="Low self-esteem makes Kaia feel she doesn’t measure up, until she finds hope in the people she loves.",
         # (YouTube video id, episode title) from the client, Nov 24 2026
         videos=[("gctypUcTLyg", "Taking Up Space"),
                 ("rqZvp0gnsrM", "Rallying Together")]),
    dict(slug="vince", topic="Body image", name="Vince", alt="Vince, a teen in a denim shirt over a black T-shirt", trailer=("eCPYIYrYwmw", "Introducing Vince’s Story"), title="Vince’s story", count=2, note="body image, anxiety", lesson="lesson plan",
         desc="Asked to be a groomsman, Vince can’t stand people looking at him. His brother’s support is crucial.",
         # (YouTube video id, episode title) from the client, Nov 24 2026
         videos=[("CwLyLMSx81M", "Muscle Isolation"),
                 ("GzACs2yieGo", "Quest for Rest")]),
    dict(slug="raquelle", topic="Bullying", name="Raquelle", alt="Raquelle, a teen with curly hair and a gray hoodie, looking worried", title="Are You OK?", count=1, film=True, note="bullying", lesson="classroom activities",
         desc="An award-winning short film about bullying, and how much one simple question — “Are you OK?” — can mean to someone who is struggling.",
         # One award-winning short film, not a series (from the client, Nov 24 2026)
         videos=[("tJsGGsPNakw", "Are You OK?")]),
]

def build_stories():
    tpl = open(os.path.join(HERE, "src", "_story.tpl"), encoding="utf-8").read()
    for st in STORIES:
        n = st["count"] if isinstance(st["count"], int) else 4
        current = ' aria-current="true"'  # no backslashes inside f-string braces: Python < 3.12 rejects them
        videos = st.get("videos", [])
        film = st.get("film", False)
        label = "Short film" if film else "Episode"
        def ep(i):
            vid, title = videos[i - 1] if i <= len(videos) else ("", f"[Episode {i} title]")
            title = html.escape(title, quote=True)  # titles can hold & or quotes
            data = f' data-video="{vid}" data-title="{title}"' if vid else ""
            thumb = f' style="background-image:url(https://i.ytimg.com/vi/{vid}/mqdefault.jpg)"' if vid else ""
            return (f'          <li><button class="mliwl-episode" type="button" data-episode="{i}"{data}{current if i == 1 else ""}>'
                    f'<span class="mliwl-episode-thumb" aria-hidden="true"{thumb}><svg><use href="#i-play"/></svg></span>'
                    f'<span class="mliwl-episode-text"><span class="mliwl-caps-link">{label if film else label + " " + str(i)}<span class="mliwl-now"> · Now playing</span></span>'
                    f'<span class="text-body-strong">{title}</span><span class="text-caption mliwl-muted-text">{DURATION.get(vid, "[mm:ss]")}</span></span></button></li>')
        rows = "\n".join(ep(i) for i in range(1, n + 1))
        if st.get("trailer"):  # trailer first in the list; the player still starts on episode 1
            tvid, ttitle = st["trailer"]
            ttitle = html.escape(ttitle, quote=True)
            rows = (f'          <li><button class="mliwl-episode mliwl-episode-trailer" type="button" data-episode="trailer" data-video="{tvid}" data-title="{ttitle}">'
                    f'<span class="mliwl-episode-thumb" aria-hidden="true" style="background-image:url(https://i.ytimg.com/vi/{tvid}/mqdefault.jpg)"><svg><use href="#i-play"/></svg></span>'
                    f'<span class="mliwl-episode-text"><span class="mliwl-caps-link">Trailer<span class="mliwl-now"> · Now playing</span></span>'
                    f'<span class="text-body-strong">{ttitle}</span><span class="text-caption mliwl-muted-text">{DURATION.get(tvid, "[mm:ss]")}</span></span></button></li>\n') + rows
        first = videos[0][0] if videos else ""
        play_href = f"https://www.youtube.com/watch?v={first}" if first else "#"
        eps = [DURATION.get(v) for v, _ in videos]
        total = TOTAL_MIN.get(st["slug"]) or (round(sum(secs(d) for d in eps) / 60) if eps and all(eps) else None)
        total_txt = f"{total} min" if total else "[total min]"
        if st.get("film"):
            looks = dict(episode_tag="Short film", summary_line="Award-winning short film · [mm:ss]",
                         list_heading="Watch", list_line="Award-winning short film")
        else:
            looks = dict(episode_tag=f"Episode 1 of {st['count']}", summary_line=f"{st['count']} episodes · {total_txt} · Animated short",
                         list_heading="Episodes", list_line=f"{st['count']} episodes · {total_txt}")
        with open(os.path.join(HERE, "assets", "lottie", st["slug"] + ".json"), encoding="utf-8") as lf:
            lj = json.load(lf)
        scene = st["trailer"][0] if st.get("trailer") else first   # the trailer still sets the scene
        watch_label = "Watch the film" if film else f"Watch {st['name']}’s story"
        about = ABOUT.get(st['slug'])
        about_html = ''.join(f'\n          <p class="text-body-small mliwl-muted-text">{html.escape(t, quote=False)}</p>' for t in about) if about else '\n          <p class="text-body-small mliwl-muted-text">[Client copy: 2–3 sentences about the story — not on the current site.]</p>'
        pdf = pdf_info(st["slug"])
        if pdf:
            lesson_href, lesson_size = pdf[0], pdf[1]
            lesson_desc = "Thought questions, a journal prompt and a group activity for each episode."
            lesson_meta = f"PDF · {lesson_size} · {PDF_PAGES.get(st['slug'], '?')} pages · Grades 6–12"
        else:
            lesson_href, lesson_size = "#", "[size]"
            lesson_desc = "A 45-minute class plan with goals, activities and discussion prompts."
            lesson_meta = "PDF · [size] · Grades 6–12"
        fields = dict(st, **looks, lesson_href=lesson_href, lesson_desc=lesson_desc, lesson_meta=lesson_meta, about_html=about_html, art_w=lj["w"], art_h=lj["h"], scene=scene, watch_label=watch_label, name_len=len(st["name"]), episodes=f"{st['count']} episodes", episode_rows=rows, video=first, play_href=play_href,
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
