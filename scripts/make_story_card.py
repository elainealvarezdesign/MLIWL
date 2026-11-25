"""Make a story card image (assets/img/story-<slug>.webp) from a character's transparent PNG.

Usage: python3 scripts/make_story_card.py <slug> [<slug> ...]
Reads scripts/character-src/<slug>.png and the card's current background
(colour + zip-tone dots, taken from the top-left corner of the existing card).
Output: 1152x864 WebP (2x the 576x432 card, sharp on retina screens).
Layout: the character stands on the bottom edge, its top at 22% of the height
so the topic tag (top-left, HTML) never covers the head. Needs Pillow.
"""
import os, sys
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W, H = 1152, 864
TOP = 0.22          # room for the topic tag
TILE = 44           # the zip-tone dot pattern repeats every 44px in the 1x cards


def make(slug):
    out = os.path.join(ROOT, "site", "assets", "img", f"story-{slug}.webp")
    old = Image.open(out).convert("RGB")
    scale = old.width / 576
    tile = old.crop((0, 0, round(TILE * scale), round(TILE * scale))).resize((TILE * 2, TILE * 2), Image.LANCZOS)
    card = Image.new("RGB", (W, H))
    for y in range(0, H, tile.height):
        for x in range(0, W, tile.width):
            card.paste(tile, (x, y))
    ch = Image.open(os.path.join(ROOT, "scripts", "character-src", f"{slug}.png")).convert("RGBA")
    ch = ch.crop(ch.getchannel("A").point(lambda a: 255 if a > 24 else 0).getbbox())  # ignore faint edge pixels
    h = round(H * (1 - TOP))
    w = round(ch.width * h / ch.height)
    if w > W * 0.8:                      # very wide art: fit the width instead
        w = round(W * 0.8); h = round(ch.height * w / ch.width)
    src = ch.size
    ch = ch.resize((w, h), Image.LANCZOS)
    card.paste(ch, ((W - w) // 2, H - h), ch)
    card.save(out, "WEBP", quality=86, method=6)
    print(f"story-{slug}.webp: character {w}x{h} from a {src[0]}x{src[1]} source" + ("  (low-res source: send a ~1000px PNG)" if src[1] < h else ""))


for s in sys.argv[1:]:
    make(s)
