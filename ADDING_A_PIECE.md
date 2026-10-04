# adding a piece — the workflow, crystallized

There's a real, repeatable pipeline now (confirmed live, checkout tested end to
end). This doc is that pipeline, written down once, with **the sarong** worked
through as the live example so nothing here is theoretical.

---

## the pipeline

```
1. CONCEPT        → name, drop #, tier, price, copy (this doc / a doc like it)
2. ARTWORK        → generate/prepare the print or graphic (OpenArt / Midjourney / Firefly)
3. CONTRADO       → create the base product + place artwork
                     05_CODE/contrado_upload.js  (add product to products.json first)
4. SHOPIFY        → confirm the product landed, set price, set inventory/cap
                     publish to BOTH "Online Store" AND "Buy Button" sales channels
                     (miss this and the storefront API can't see it — this exact
                     bug took down add-to-cart for 2 of 5 products, see
                     SESSION_HANDOFF_2026-07-09.md)
5. DATA.JS        → add one object to window.VRSN_PRODUCTS in versan_site_v2/js/data.js
                     (variant ids come from Shopify admin → product → variants,
                     each one's numeric ID is in its admin URL)
6. BUILD          → bump V in build.py, run `python3 build.py`
                     (never hand-edit the generated html — it gets overwritten)
7. SHIP           → git add -A && git commit && git push
                     GitHub Actions deploys to versan.store automatically
```

Steps 1–2 are creative/Cole's call. Steps 3–7 are mechanical once 1–2 are locked.

---

## worked example: the sarong

Reimagining Contrado's "Custom Sarongs" base (Paris Chiffon, 100% silk or faux
silk sensation, 2 sizes to 4XL) — currently a busy color-block geometric print —
as a VERSVN object.

### the reframe

A sarong is a leisure signifier — beachwear, vacation, dry land you chose to
stand near water on. VERSVN's water is the other kind: still, dark, flood water,
present in every piece of editorial photography planned for this brand but
never yet in a product itself. **This is the first object to carry that motif
directly, not just be photographed near it.** The print isn't a pattern — it's
a single still-water photograph, full bleed, black and white, edge to edge. No
color block. No "vacation." A garment for water that isn't asking to be there.

### concept

| field | value |
|---|---|
| name | the sarong |
| drop | 006 |
| tier | signature (leather/silk-tier material story, small seasonal cap — same shelf as the fanny, not open-ended like the accessible tier, not apex-scarce) |
| type | silk wrap |
| price | **$143** — continues the `$X3` motif (33 · 63 · 73 · 93 · 133 · **143** · 333), sits just above the fanny |
| categories | women, accessories |
| observed (hover-swap) | **the last dry thing** |
| base | Contrado custom sarong — Paris Chiffon, 100% silk or faux silk sensation, hand-rolled hem, 2 size options to 4XL |
| print | full-bleed b&w still-water photograph. no color. forest green appears only as a small woven v-mark tag at one corner — never in the print itself, per brand rule |

### copy (matches the `desc` field pattern used by every other object in data.js)

```
a wrap.

silk chiffon, hand-rolled hem. one continuous print —
still water, edge to edge, black and white.

it was made for water. so were you, eventually.
```

### draft `data.js` entry — paste in once Contrado/Shopify steps are done

```js
{
  id: 'the-sarong',
  name: 'the sarong',
  observed: 'the last dry thing',
  drop: '006',
  tier: 'signature',
  type: 'silk wrap',
  price: 143.00,
  handle: '[shopify handle once created]',
  categories: ['women', 'accessories'],
  img: '[shopify cdn url once product image is uploaded]',
  options: [
    { label: 'select size', values: ['standard', 'plus · 4xl'] },
    { label: 'select fabric', values: ['silk chiffon', 'faux silk sensation'] }
  ],
  variants: {
    /* fill in after creating the product in shopify —
       admin → products → the sarong → each variant's numeric id
       is in that variant row's admin url */
    'standard|silk chiffon': { vid: 0 },
    'standard|faux silk sensation': { vid: 0 },
    'plus · 4xl|silk chiffon': { vid: 0 },
    'plus · 4xl|faux silk sensation': { vid: 0 }
  },
  desc: 'a wrap.\n\nsilk chiffon, hand-rolled hem. one continuous print —\nstill water, edge to edge, black and white.\n\nit was made for water. so were you, eventually.',
  alt: 'the object in question.'
}
```

### draft `05_CODE/products.json` entry — add before running `contrado_upload.js`

```json
"sarong": {
  "label": "VERSAN Silk Sarong",
  "contradoProductSlug": "custom-sarongs",
  "contradoProductTypeId": null,
  "price": { "amount": 143.0, "currency": "USD" },
  "defaultZone": "full-bleed",
  "printSpec": {
    "widthPx": 5315,
    "heightPx": 2657,
    "dpi": 300,
    "fit": "cover",
    "background": "transparent",
    "format": "png"
  }
}
```
`contradoProductSlug` and dimensions are `[VERIFY]` — same caveat as every other
entry in that file (the Contrado API contract was never confirmed against real
docs). Confirm against the actual product page before running `--commit`.

### open decisions for Cole

1. **Price** — $143 continues the motif; say the word if you want a different number.
2. **The print photograph** — use one of the 4 unreviewed stage-4 editorial
   images (flooded-street / studio / reversed-chair / submerged-office —
   CDN urls are in the 2026-07-09 chat, not yet downloaded or reviewed), or
   generate something new specifically for this piece.
3. **Tier** — signature as proposed, or move to accessible (open, no seasonal cap)?
4. **Name** — "the sarong" is plain/deadpan on purpose, matching "the bucket" /
   "the fanny." Could also go proper-noun like "the annette" if you want it
   named after someone.

Once those are locked, steps 2–7 above are mechanical.

---

## worked example: the dayshift

Reimagining Contrado's "Custom Women's Luxury Silk Pyjamas" base — silk
charmeuse separates, handmade, 2 fabrics, sizes 2XS–7XL, choice of black or
white thread/buttons — as a VERSVN **men's day fit**. Not sleepwear. The
construction (matching silk shirt + trouser separates) is the same logic
Contrado sells as pyjamas, but this is styled, named, and worn as a going-out
look — open collar, sleeves rolled, tucked, upright. Source from Contrado's
men's silk shirting/trouser listings, not the pyjama category — `[VERIFY]`
the exact slug before running the pipeline; the reference screenshot was the
women's sleepwear version, used here only for the fabric/construction idea.

### the reframe

The absurdity isn't "the bedroom is surveilled" (wrong category) — it's that
**comfort has become a public performance.** Clothes engineered for rest are
now worn deliberately, in daylight, to be seen — the softest possible fabric
styled as a hard, composed silhouette. Silk built for lying down, tailored
instead for standing up. That contradiction is the whole piece: designed for
ease, worn as a statement, photographed either way. "We see you seeing us" —
now applied to what people wear specifically to be looked at while claiming
to be relaxed.

### concept

| field | value |
|---|---|
| name | the dayshift |
| drop | 007 |
| tier | signature (silk-tier material story, same shelf as the fanny/the sarong) |
| type | silk day-fit co-ord (shirt + trouser, worn open) |
| price | **$163** — continues the `$X3` motif (33 · 63 · 73 · 93 · 133 · 143 · **163** · 333) |
| categories | men |
| observed (hover-swap) | **the appearance of rest** |
| base | Contrado silk shirting + trouser construction (sourced from the men's silk line, not the pyjama listing) — handmade separates, black thread/buttons |
| print | tone-on-tone obsidian silk, wordmark woven throughout, barely visible except at an angle. bone-white piping at collar, cuffs, and front placket — the only contrast. black buttons. no color block, no loungewear styling |

### copy (matches the `desc` field pattern in data.js)

```
a set.

silk shirting and trouser, handmade separates, worn open.
tone-on-tone v mark woven throughout. bone piping at
collar and cuff.

engineered for comfort. photographed anyway.
```

### draft `data.js` entry — paste in once Contrado/Shopify steps are done

```js
{
  id: 'the-dayshift',
  name: 'the dayshift',
  observed: 'the appearance of rest',
  drop: '007',
  tier: 'signature',
  type: 'silk day-fit co-ord',
  price: 163.00,
  handle: '[shopify handle once created]',
  categories: ['men'],
  img: '[shopify cdn url once product image is uploaded]',
  options: [
    { label: 'select size', values: ['s', 'm', 'l', 'xl', '2xl'] },
    { label: 'select fabric', values: ['silk charmeuse', 'washed silk'] }
  ],
  variants: {
    /* fill in after creating the product in shopify */
    's|silk charmeuse': { vid: 0 },
    's|washed silk': { vid: 0 },
    'm|silk charmeuse': { vid: 0 },
    'm|washed silk': { vid: 0 },
    'l|silk charmeuse': { vid: 0 },
    'l|washed silk': { vid: 0 },
    'xl|silk charmeuse': { vid: 0 },
    'xl|washed silk': { vid: 0 },
    '2xl|silk charmeuse': { vid: 0 },
    '2xl|washed silk': { vid: 0 }
  },
  desc: 'a set.\n\nsilk shirting and trouser, handmade separates, worn open.\ntone-on-tone v mark woven throughout. bone piping at\ncollar and cuff.\n\nengineered for comfort. photographed anyway.',
  alt: 'the object in question.'
}
```

### draft `05_CODE/products.json` entry

```json
"dayshift": {
  "label": "VERSAN Silk Day Fit",
  "contradoProductSlug": "custom-mens-silk-shirt-trouser-set",
  "contradoProductTypeId": null,
  "price": { "amount": 163.0, "currency": "USD" },
  "defaultZone": "full-bleed",
  "printSpec": {
    "widthPx": 4724,
    "heightPx": 4724,
    "dpi": 300,
    "fit": "tile",
    "background": "transparent",
    "format": "png"
  }
}
```
`contradoProductSlug` is `[VERIFY]` — the base construction exists on Contrado
as a pyjama-category listing; confirm whether to source it from there directly
(fine — it's just fabric/construction, VERSVN's framing is what changes it)
or find a shirting-category equivalent before running `--commit`. `fit: "tile"`
because this is a repeating tone-on-tone pattern, not a full-bleed photograph
like the sarong.

### reference visuals — generating now via OpenArt (gpt-image-2)

First pass was generated under the wrong framing (styled/described as
sleepwear) and rejected — regenerating as an actual daytime look:
1. **editorial hero** — man in the reimagined set, high-top fade, black
   sunglasses, standing ankle-deep in still flood water against a plain white
   backdrop, styled open-collar with sleeves rolled and tucked — upright,
   composed, a fashion stance, explicitly not a resting/bedroom pose. Black &
   white, clinical/observed mood.
2. **fabric/print detail** — macro shot of the tone-on-tone woven wordmark
   silk with the bone piping edge, black & white, product-swatch style.

These will render as OpenArt result cards in the chat where this was
requested. Download and drop into `assets/images/editorial/` (hero) and
`assets/images/products/` (swatch) once approved — neither is committed yet.

### open decisions for Cole

1. **Price** — $163 continues the motif.
2. **Fabric option naming** — "silk charmeuse" / "washed silk," or match
   Contrado's actual two-fabric split once the real listing is sourced.
3. **Tone-on-tone print** — approve the woven-wordmark direction, or prefer
   a plain solid (no print at all, piping does all the work)?
4. **The two OpenArt references** — approve, regenerate, or scrap in favor
   of real photography later (per the men's gallery shoot already planned).

---

## notes for whoever runs this next

- `js/data.js` is the single source of truth for what's on the site. Shopify
  is the source of truth for what can actually be bought. They have to agree —
  a product missing from the buy button channel, or a variant id that doesn't
  match, breaks checkout silently (exactly what happened last session).
- Pricing follows the apex/signature/accessible tier structure in
  `fable_build_kit/VERSVN_apex_capsule_pricing.md` — read that before pricing
  anything new.
- Copy voice rules are absolute — see the "voice reminders for claude code"
  section at the bottom of `01_ANCHORS/versan_site_v1/COPY.md`. No exclamation
  points, no "explore/discover/elevate/journey/curate," no explaining the joke.
- If `git` complains about `HEAD.lock` when pushing, that's the mounted-drive
  artifact noted in `SESSION_HANDOFF_2026-07-09.md` — `rm -f .git/HEAD.lock`
  and retry.
