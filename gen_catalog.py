#!/usr/bin/env python3
# gen_catalog.py — emits js/data.js + products_build.json from the CUP catalog spec.
# variant ids verified against shopify 2026-07-12: sequential (+32768), row-major
# over option grids, first group slowest. re-verify if products are re-imported.

import itertools, json, os

OUT = os.path.dirname(os.path.abspath(__file__))
STEP = 32768
SIG = "vrsn · rebel in luxury · est. 3:33\ncase — 002 · the standard pack"

# options: list of (label, [values]). prices: default + optional per-value override
# keyed on a value of the price_group option.
CATALOG = [
    dict(id="the-standard-issue", name="the standard issue", observed="required equipment",
         type="hazmat suit", handle="hazmat-suit", first=50397275816129, price=333.00,
         img="https://cdn.shopify.com/s/files/1/0865/2721/3761/files/3039026_0_3d.jpg?v=1783804262",
         categories=["men", "women"],
         options=[("select size", ["s", "m", "l", "xl"]),
                  ("select cord", ["white", "black", "orange", "pink", "green"])],
         desc="issued.\n\nhazmat suit. poly waterproof fabric. zip-up front. hooded. handmade to order.\n\nchest stamp: commission for uniform provision · standard issue — tier 2 · cycle 04.\nback: barcode. unit no. 04-2891.\n\nyou are not a person wearing clothes. you are a unit carrying its current cycle's issue."),
    dict(id="the-poncho", name="the poncho", observed="scheduled precipitation",
         type="rain poncho", handle="pullover-rain-poncho", first=50397275095233, price=283.00,
         img="https://cdn.shopify.com/s/files/1/0865/2721/3761/files/3039022_0_3d.jpg?v=1783804244",
         categories=["men", "women"],
         options=[("select cord", ["white", "black", "orange", "pink", "green"]),
                  ("select pocket", ["no pocket", "with pocket"]),
                  ("select hardware", ["silver", "graphite"])],
         desc="issued.\n\npullover rain poncho. waterproof. hooded. handmade to order.\n\nchest stamp: commission for uniform provision · standard issue — tier 2 · cycle 07.\nback: barcode. unit no. 04-2891.\n\nprecipitation is scheduled. so is your protection from it."),
    dict(id="the-roll-neck", name="the roll neck", observed="a managed input",
         type="base layer top", handle="mens-slim-fit-roll-neck", first=50397525180609, price=113.00,
         img="https://cdn.shopify.com/s/files/1/0865/2721/3761/files/3039036_0_3d.jpg?v=1783825131",
         categories=["men", "women"],
         options=[("select size", ["2xs", "xs", "s", "m", "l", "xl", "2xl"]),
                  ("select fabric", ["recycled jersey", "silky jersey"])],
         desc="issued.\n\nbase layer, slim fit roll neck. recycled polyester jersey, 200gsm, black trim. handmade to order.\n\nchest stamp: commission for uniform provision · standard issue — tier 2 · cycle 04.\nback: barcode. unit no. 04-2891.\n\nrecycled material. the commission manages its inputs. you are one of them."),
    dict(id="the-trousers", name="the trousers", observed="the lower allotment",
         type="base layer bottom", handle="mens-pyjama-bottoms", first=50397267820737, price=93.00,
         img="https://cdn.shopify.com/s/files/1/0865/2721/3761/files/3039498_0_3d.jpg?v=1783803969",
         categories=["men", "women"],
         options=[("select size", ["xs", "s", "m", "l", "xl", "2xl", "3xl", "4xl", "5xl", "6xl", "7xl"]),
                  ("select fabric", ["jersey", "organic cotton"])],
         price_overrides={"organic cotton": 123.00}, price_group=1,
         desc="issued.\n\nbase layer bottom. elastic waistband, side pockets, loose fit. handmade to order.\n\npairs with the roll neck. a unit's base layer is issued as a set.\n\nchest stamp: commission for uniform provision · standard issue — tier 2 · cycle 04.\nunit no. 04-2891."),
    dict(id="the-tee", name="the tee", observed="cycle 04",
         type="oversized tee", handle="mens-oversized-t-shirt", first=50397284597953, price=123.00,
         img="https://cdn.shopify.com/s/files/1/0865/2721/3761/files/3039042_0_3d.jpg?v=1783806188",
         categories=["men", "women"],
         options=[("select size", ["xs", "s", "m", "l", "xl", "2xl", "3xl", "4xl", "5xl", "6xl", "7xl"]),
                  ("select fabric", ["ponte jersey", "bounce cotton"])],
         price_overrides={"bounce cotton": 163.00}, price_group=1,
         desc="issued.\n\noversized boxy tee. heavyweight jersey. handmade to order.\n\nchest stamp: commission for uniform provision · standard issue — tier 2 · cycle 04.\nback: barcode, high and centered below the collar seam. unit no. 04-2891.\n\nequity of appearance: nobody over, nobody under, nobody anybody."),
    dict(id="the-tag", name="the tag", observed="you, in ledger form",
         type="unit identifier", handle="leather-keyring", first=50397278109889, price=123.00,
         img="https://cdn.shopify.com/s/files/1/0865/2721/3761/files/3039051_0_3d.jpg?v=1783804523",
         categories=["accessories"],
         options=[("select shape", ["rectangle", "heart"]),
                  ("select leather", ["smooth nappa", "textured nappa"]),
                  ("select edge", ["black thread", "charcoal", "cream", "red", "blue", "brown"])],
         desc="issued.\n\nunit identifier. printed, padded leather. double sided. silver ring. handmade to order.\n\nfront: barcode. unit no. 04-2891.\nback: commission for uniform provision · standard issue — tier 2 · cycle 04.\n\nthe garments are what the allotment entitles you to. this is the allotment. carry it."),
    dict(id="the-fanny-pack", name="the fanny pack", observed="carried weight",
         type="carry unit", handle="fanny-pack", first=50397284466881, price=343.00,
         img="https://cdn.shopify.com/s/files/1/0865/2721/3761/files/3039048_0_3d.jpg?v=1783804707",
         categories=["accessories"],
         options=[("select strap", ["standard · waist", "long · cross body"]),
                  ("select material", ["nappa leather", "brushed twill"])],
         desc="issued.\n\ncarry unit. 100% nappa leather, handmade to order. adjustable strap.\n\nstamp, small scale, beside the zipper: commission for uniform provision · standard issue — tier 2 · cycle 04.\n\ncontents are the unit's own. this is noted, not encouraged."),
    dict(id="the-vest", name="the vest", observed="black issue",
         type="puffer vest", handle="unisex-gilet", first=50397279125697, price=833.00,
         img="https://cdn.shopify.com/s/files/1/0865/2721/3761/files/3039057_0_3d.jpg?v=1783804553",
         categories=["men", "women"],
         options=[("select size", ["xs", "s", "m", "l", "xl", "2xl", "3xl", "4xl"]),
                  ("select fabric", ["splash proof", "silk satin"]),
                  ("select zip", ["white", "black", "cream", "red", "green", "blue", "yellow", "pink"])],
         price_overrides={"silk satin": 1033.00}, price_group=1,
         desc="issued.\n\npuffer vest, black. the only black-base piece in the pack. handmade to order.\n\nfront, white ink, beside the zip pull: commission for uniform provision · standard issue — tier 2 · cycle 04.\nback, below the collar: barcode. unit no. 04-2891.\n\nblack issue exists. the reason is not disclosed at this tier."),
    dict(id="the-jacket", name="the jacket", observed="read before spoken to",
         type="puffer jacket", handle="mens-puffer-jacket", first=50397274505409, price=343.00,
         img="https://cdn.shopify.com/s/files/1/0865/2721/3761/files/3039061_0_3d.jpg?v=1783805591",
         categories=["men", "women"],
         options=[("select size", ["xs", "s", "m", "l", "xl", "2xl"]),
                  ("select fabric", ["splash proof", "silk satin"])],
         price_overrides={"silk satin": 633.00}, price_group=1,
         desc="issued.\n\npuffer jacket, white. handmade to order. the pack's outerwear piece, and the one that inverts the layout.\n\nfront, oversized, split across the center zipper seam: barcode. unit no. 04-2891.\nback, upper panel: commission for uniform provision · standard issue — tier 2 · cycle 04.\n\na unit wearing this one is barcode-forward. read before spoken to."),
    dict(id="the-beanie", name="the beanie", observed="a warm standard",
         type="knit cap", handle="beanie", first=50397272277185, price=63.00,
         img="https://cdn.shopify.com/s/files/1/0865/2721/3761/files/3039496_0_3d.jpg?v=1783806252",
         categories=["men", "women", "accessories"],
         options=[("select size", ["xs", "s/m", "l/xl", "xxl"])],
         desc="issued.\n\nknit cap. recycled poly jersey, double layered. handmade to order.\n\ncuff stamp, wraparound: commission for uniform provision · standard issue — tier 2 · cycle 04.\nunit no. 04-2891.\n\nheads are standardized for a reason. warmth is an allotment like anything else."),
    dict(id="the-ration", name="the ration", observed="a unit of measure",
         type="thermal bottle", handle="stainless-steel-thermal-bottle", first=50397274439873, price=53.00,
         img="https://cdn.shopify.com/s/files/1/0865/2721/3761/files/3039059_0_3d.jpg?v=1783805472",
         categories=["accessories"],
         options=[("select finish", ["silver", "white"])],
         desc="issued.\n\nthermal bottle, stainless steel. 7oz. screw top. bpa free. handmade to order.\n\nstamp: commission for uniform provision · standard issue — tier 2 · cycle 04.\nunit no. 04-2891.\n\na cup is a unit of measure. the commission does not just measure what you drink."),
]

products = []
for p in CATALOG:
    values = [opt[1] for opt in p["options"]]
    variants = {}
    for i, combo in enumerate(itertools.product(*values)):
        key = "|".join(combo)
        v = {"vid": p["first"] + i * STEP}
        og = p.get("price_group")
        if og is not None:
            ov = p.get("price_overrides", {}).get(combo[og])
            if ov:
                v["price"] = ov
        variants[key] = v
    products.append({
        "id": p["id"], "name": p["name"], "observed": p["observed"],
        "sub": "case — 002 · the standard pack", "type": p["type"],
        "price": p["price"], "handle": p["handle"], "categories": p["categories"],
        "img": p["img"],
        "options": [{"label": l, "values": v} for l, v in p["options"]],
        "variants": variants,
        "desc": p["desc"] + "\n\n" + SIG.replace("case — 002 · the standard pack", "case — 002 · the standard pack"),
        "alt": "the object in question."
    })

header = """/* data.js — the objects on record. GENERATED by gen_catalog.py — do not hand-edit.
   the standard pack · case — 002 · unit no. 04-2891.
   prices + variant ids mirror the shopify store (iesefi-cx.myshopify.com).
   images served from the shopify cdn, width-capped, rendered b&w by css. */

window.VRSN_STORE = 'https://iesefi-cx.myshopify.com';

window.VRSN_PRODUCTS = """

footer = """;

window.VRSN_IMG = function (url, w) {
  return url + '&width=' + (w || 900);
};

window.VRSN_VARIANT = function (p, sel) {
  if (!p.variants) return null;
  return p.variants[sel.join('|')] || null;
};
"""

with open(os.path.join(OUT, "js/data.js"), "w") as f:
    f.write(header + json.dumps(products, indent=2, ensure_ascii=False) + footer)
with open(os.path.join(OUT, "products_build.json"), "w") as f:
    json.dump(products, f, indent=2, ensure_ascii=False)
total = sum(len(p["variants"]) for p in products)
print(f"wrote {len(products)} products, {total} variants")
