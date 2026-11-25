"""Make a character's Lottie (breathing loop) and its still image for the story pages.

Usage: python3 scripts/make_character_lottie.py <slug> <transparent PNG> [<slug> <png> ...]
Writes, for each character:
  site/assets/lottie/<slug>.json      Lottie with the image embedded (works in Elementor's Lottie widget)
  site/assets/img/character-<slug>.webp  the same picture, shown first and when motion is reduced
The animation: 4 s loop at 30 fps, grows 2% and tilts ±0.35° from the bottom centre,
so a character cut off at the waist stays on the bottom edge. Needs Pillow.
"""
import base64, io, json, os, sys
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAX_H = 760          # tall enough for the profile block on retina screens
SIDE, TOP = 24, 32   # room for the scale and tilt, so hair and arms never clip
FR, OP = 30, 120


def kf(t, v, last=False):
    k = {"t": t, "s": v}
    if not last:
        k.update({"i": {"x": [0.45] * len(v), "y": [1] * len(v)}, "o": {"x": [0.55] * len(v), "y": [0] * len(v)}})
    return k


def make(slug, src):
    im = Image.open(src).convert("RGBA")
    im = im.crop(im.getbbox())
    if im.height > MAX_H:
        im = im.resize((round(im.width * MAX_H / im.height), MAX_H), Image.LANCZOS)
    w, h = im.size
    buf = io.BytesIO(); im.save(buf, "WEBP", quality=88, method=6)  # WebP keeps the file small; lottie-web shows it fine
    cw, ch = w + 2 * SIDE, h + TOP
    layer_ks = {
        "o": {"a": 0, "k": 100},
        "r": {"a": 1, "k": [kf(0, [0]), kf(30, [0.35]), kf(90, [-0.35]), kf(120, [0], True)]},
        "p": {"a": 0, "k": [cw / 2, ch, 0]},
        "a": {"a": 0, "k": [w / 2, h, 0]},
        "s": {"a": 1, "k": [kf(0, [100, 100, 100]), kf(60, [102, 102, 100]), kf(120, [100, 100, 100], True)]},
    }
    lottie = {"v": "5.7.4", "fr": FR, "ip": 0, "op": OP, "w": cw, "h": ch, "nm": f"{slug} - breathing loop", "ddd": 0,
              "assets": [{"id": "image_0", "w": w, "h": h, "u": "", "e": 1,
                          "p": "data:image/webp;base64," + base64.b64encode(buf.getvalue()).decode()}],
              "layers": [{"ddd": 0, "ind": 1, "ty": 2, "nm": slug, "refId": "image_0", "sr": 1, "ks": layer_ks,
                          "ao": 0, "ip": 0, "op": OP, "st": 0, "bm": 0}], "markers": []}
    out = os.path.join(ROOT, "site", "assets", "lottie", f"{slug}.json")
    with open(out, "w") as f:
        json.dump(lottie, f, separators=(",", ":"))
    # Still image on the same canvas, so swapping it for the animation does not shift anything
    still = Image.new("RGBA", (cw, ch), (0, 0, 0, 0)); still.paste(im, (SIDE, TOP), im)
    still.save(os.path.join(ROOT, "site", "assets", "img", f"character-{slug}.webp"), "WEBP", quality=88, method=6)
    print(f"{slug}: image {w}x{h}, canvas {cw}x{ch}, lottie {os.path.getsize(out) // 1024} KB")


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args or len(args) % 2:
        sys.exit(__doc__)
    for slug, src in zip(args[::2], args[1::2]):
        make(slug, src)
