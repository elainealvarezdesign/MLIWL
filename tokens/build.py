"""Build MLIWL design tokens from the Figma variable export.

Usage: python3 -I build.py <figma-export.json> <out-dir>
Outputs: mliwl.tokens.json (W3C DTCG), tokens.css
"""
import json, sys, os

src, out = sys.argv[1], sys.argv[2]
data = json.load(open(src))
os.makedirs(out, exist_ok=True)

WEIGHTS = {"Black": 900, "ExtraBold": 800, "Bold": 700, "Medium": 500, "Regular": 400}
PREFIX = {"Primitives": "color", "Color": "color", "Spacing": "space", "Radius": "radius", "Layout": "layout", "Typography": ""}
BREAKPOINTS = [("Mobile", None), ("Tablet", 768), ("Desktop", 1024)]


def css_name(collection, name):
    parts = name.split("/")
    if collection in ("Spacing", "Radius", "Layout"):
        parts = parts[1:]
    if collection == "Typography":
        parts = parts[1:]  # drop "font"
        if parts[0] in ("size", "line-height", "family", "weight"):
            parts = (["font-size"] if parts[0] == "size" else ["line-height"] if parts[0] == "line-height" else ["font-" + parts[0]]) + parts[1:]
        return "--" + "-".join(parts)
    pre = PREFIX[collection]
    return "--" + "-".join([pre] + parts)


# index: figma name -> (collection, css var)
index = {}
for c in data["collections"]:
    for name, *_ in c["vars"]:
        index[name] = (c["name"], css_name(c["name"], name))


def css_value(v, typ):
    if isinstance(v, dict):
        return f"var({index[v['ref']][1]})"
    if typ == "F":
        return f"{v}px" if v != 0 else "0"
    return v


def dtcg_path(collection, name):
    group = {"Primitives": "primitive", "Color": "color", "Spacing": "space", "Radius": "radius", "Layout": "layout", "Typography": "type"}[collection]
    parts = name.split("/")
    if collection in ("Spacing", "Radius", "Layout"):
        parts = parts[1:]
    if collection == "Typography":
        parts = parts[1:]
    return [group] + parts


def dtcg_value(v, typ):
    if isinstance(v, dict):
        col = index[v["ref"]][0]
        return "{" + ".".join(dtcg_path(col, v["ref"])) + "}"
    if typ == "F":
        return {"value": v, "unit": "px"}
    return v


# ---------- DTCG JSON ----------
tree = {"$description": "My Life Is Worth Living design tokens. Generated from Figma file pji462RDmAcvludSloZL2w. Do not edit by hand."}
for c in data["collections"]:
    for name, typ, values, desc in c["vars"]:
        path = dtcg_path(c["name"], name)
        node = tree
        for p in path[:-1]:
            node = node.setdefault(p, {})
        ttype = {"C": "color", "F": "dimension", "S": "string"}[typ]
        if c["name"] == "Typography" and "line-height" in name:
            ttype = "dimension"
        tok = {"$type": ttype, "$value": dtcg_value(values[0], typ)}
        if desc:
            tok["$description"] = desc
        if len(c["modes"]) > 1:
            tok["$extensions"] = {"mliwl.modes": {m: dtcg_value(v, typ) for m, v in zip(c["modes"], values)}}
        node[path[-1]] = tok
tree["shadow"] = {}
for name, (x, y, blur, spread, color) in data["effects"]:
    tree["shadow"][name.split("/")[1].lower()] = {"$type": "shadow", "$value": {"color": color, "offsetX": {"value": x, "unit": "px"}, "offsetY": {"value": y, "unit": "px"}, "blur": {"value": blur, "unit": "px"}, "spread": {"value": spread, "unit": "px"}}}
tree["typography"] = {}
for name, weight, key, case, ls in data["text"]:
    k = name.lower().replace("/", "-").replace(" ", "-")
    tree["typography"][k] = {"$type": "typography", "$value": {
        "fontFamily": "Montserrat", "fontWeight": WEIGHTS[weight],
        "fontSize": "{type.size." + key + "}", "lineHeight": "{type.line-height." + key + "}",
        "letterSpacing": ls if ls else 0}, "$extensions": {"mliwl.textTransform": "uppercase" if case == "UPPER" else "none"}}
json.dump(tree, open(os.path.join(out, "mliwl.tokens.json"), "w"), indent=2, ensure_ascii=False)

# ---------- CSS ----------
L = ["/* My Life Is Worth Living — design tokens", " * Generated from Figma (file pji462RDmAcvludSloZL2w). Do not edit by hand: change Figma, re-export, rebuild.",
     " * Mobile-first: base values are Mobile; Tablet from 768px; Desktop from 1024px. */", "",
     ":root {", "  --font-family-base: 'Montserrat', 'Noto Sans JP', 'Noto Sans SC', system-ui, sans-serif;"]
for w, n in WEIGHTS.items():
    L.append(f"  --font-weight-{w.lower()}: {n};")
for c in data["collections"]:
    L.append(f"\n  /* {c['name']} */")
    mi = c["modes"].index("Mobile") if "Mobile" in c["modes"] else 0
    for name, typ, values, desc in c["vars"]:
        L.append(f"  {index[name][1]}: {css_value(values[mi], typ)};" + (f" /* {desc} */" if desc and c['name'] in ('Color',) else ""))
L.append("\n  /* Elevation */")
for name, (x, y, blur, spread, color) in data["effects"]:
    L.append(f"  --shadow-{name.split('/')[1].lower()}: {x}px {y}px {blur}px {spread}px {color};")
L.append("  --focus-ring: 0 0 0 3px var(--color-focus-ring), 0 0 0 5px var(--color-ink-900);")
L.append("}")
for k, (mode, bp) in enumerate(BREAKPOINTS[1:], start=1):
    prev = BREAKPOINTS[k - 1][0]
    L.append(f"\n@media (min-width: {bp}px) {{\n  :root {{")
    for c in data["collections"]:
        if mode not in c["modes"]:
            continue
        i, mi = c["modes"].index(mode), c["modes"].index(prev)
        for name, typ, values, desc in c["vars"]:
            if values[i] != values[mi]:
                L.append(f"    {index[name][1]}: {css_value(values[i], typ)};")
    L.append("  }\n}")
L.append("\n/* Text styles (match Figma text styles 1:1) */")
for name, weight, key, case, ls in data["text"]:
    cls = name.lower().replace("/", "-").replace(" ", "-")
    lsv = "0" if not ls else (f"{float(ls[:-1]) / 100:g}em" if ls.endswith("%") else ls)
    L.append(f".text-{cls} {{ font-family: var(--font-family-base); font-weight: var(--font-weight-{weight.lower()}); "
             f"font-size: var(--font-size-{key}); line-height: var(--line-height-{key}); letter-spacing: {lsv};"
             + (" text-transform: uppercase;" if case == "UPPER" else "") + " }")
open(os.path.join(out, "tokens.css"), "w").write("\n".join(L) + "\n")

print("ok", sum(len(c["vars"]) for c in data["collections"]), "variables")
