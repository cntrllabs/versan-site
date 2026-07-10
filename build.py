#!/usr/bin/env python3
# build.py — emits every page of the versan site from one chrome template.
# run: python3 build.py

import os, json

OUT = os.path.dirname(os.path.abspath(__file__))
V = "4"  # bump on every deploy — cache-busts css/js

FAVICON = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' fill='%230D0D0B'/%3E%3Ctext x='32' y='42' font-family='Georgia,serif' font-size='38' fill='%23F4F1EB' text-anchor='middle'%3EV%3C/text%3E%3Crect x='18' y='50' width='24' height='2.5' fill='%232D6A4F'/%3E%3C/svg%3E"

SOURCE_COMMENT = """<!--
  you found this.
  most people don't look.

  this is the versan source.
  rebel in luxury.
  est. 3:33.
  nosce te ipsum.

  if you're reading this you're
  already one of us.
-->"""

def chrome(title, body, root=".", active="", extra_head="", extra_js=""):
    nav_items = [
        ("shop", "shop.html"), ("men", "mens.html"), ("women", "womens.html"),
        ("accessories", "accessories.html"),
        ("the unknown series", "unknown-series.html"), ("about", "about.html"),
    ]
    cur = ' aria-current="page"'
    nav = "\n".join(
        f'        <li><a href="{root}/{href}"{cur if active == label else ""}>{label}</a></li>'
        for label, href in nav_items)
    mnav = "\n".join(f'      <li><a href="{root}/{href}">{label}</a></li>' for label, href in nav_items)
    return f"""<!DOCTYPE html>
<html lang="en">
{SOURCE_COMMENT}
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="versan. rebel in luxury. est. 3:33. nosce te ipsum.">
<link rel="icon" href="{FAVICON}">
<link rel="preload" href="{root}/assets/fonts/CormorantGaramond-Light.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{root}/assets/fonts/DMMono-Light.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{root}/css/tokens.css?v={V}">
<link rel="stylesheet" href="{root}/css/main.css?v={V}">
{extra_head}
</head>
<body data-root="{root}">

<div id="loading-screen">
  <div class="loading-lines">
    <p>identifying visitor</p>
    <p>cross-referencing preferences</p>
    <p>building your profile</p>
    <p>selecting your content</p>
    <p>welcome back.</p>
  </div>
</div>

<div id="policy-bar">
  <span>something has changed. it probably affects you. most people will not read it.</span>
  <button type="button">[ acknowledge ]</button>
  <button type="button">[ ignore, as intended ]</button>
</div>

<nav id="main-nav" aria-label="primary">
  <a class="wordmark" href="{root}/index.html" aria-label="versan home"><span class="vd">v</span>rsn</a>
  <ul>
{nav}
  </ul>
  <div class="nav-utils">
    <button id="search-open" type="button" aria-label="search">search</button>
    <a href="{root}/cart.html" aria-label="your record">record <span class="cart-count"></span></a>
    <button id="nav-toggle" type="button" aria-label="open navigation">menu</button>
  </div>
</nav>

<div id="mobile-nav" aria-label="mobile navigation">
  <span class="mobile-header">you are navigating vrsn</span>
  <button class="close-btn" type="button">close</button>
  <ul>
{mnav}
      <li><a href="{root}/cart.html">record</a></li>
  </ul>
</div>

<div id="search-overlay" role="dialog" aria-label="search">
  <button id="search-close" type="button">close</button>
  <input type="search" placeholder="what are you looking for." aria-label="search products">
  <div id="search-results"></div>
</div>

{body}

<footer>
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <div class="foot-mark"><span class="vd">v</span>rsn</div>
        <div class="foot-lore">rebel in luxury<br>est. 3:33<br>nosce te ipsum<br>45.5231&deg; n, 122.6765&deg; w</div>
      </div>
      <nav aria-label="footer">
        <a href="{root}/shop.html">shop</a>
        <a href="{root}/mens.html">men</a>
        <a href="{root}/womens.html">women</a>
        <a href="{root}/accessories.html">accessories</a>
        <a href="{root}/unknown-series.html">the unknown series</a>
        <a href="{root}/about.html">about</a>
        <a href="{root}/privacy.html">privacy policy</a>
      </nav>
    </div>
    <div class="foot-legal">&copy; vrsn 2026 &mdash; all objects reserved.</div>
    <div class="foot-fine">by visiting this site you have agreed to be observed.
this observation is mutual.
we see you seeing us.
absurd realism &mdash; the normalization of things
that should not be normal,
presented without comment,
worn without apology.

rebel in luxury.</div>
  </div>
</footer>

<div id="toast" role="status">
  <div class="t-head">noted.</div>
  <div class="t-body"></div>
  <div class="t-actions">
    <a href="{root}/cart.html">[ view record ]</a>
    <a href="{root}/shop.html">[ continue acquiring ]</a>
  </div>
</div>

<div id="cookie-banner">
  <div class="cb-inner">
    <span class="cb-strong">this site uses cookies.</span><br>
    so does everything else.<br>
    you accepted that a long time ago.
    <div class="cb-actions">
      <button type="button">[ i know ]</button>
      <button type="button">[ tell me more* ]</button>
    </div>
    <div class="cb-fine">*there is nothing more to tell.</div>
  </div>
</div>

<canvas id="atmosphere" aria-hidden="true"></canvas>
<div id="cursor" aria-hidden="true"></div>
<div id="scroll-progress" aria-hidden="true"></div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script src="{root}/js/shopify-config.js?v={V}"></script>
<script src="{root}/js/data.js?v={V}"></script>
<script src="{root}/js/site.js?v={V}"></script>
<script src="{root}/js/motion.js?v={V}"></script>
{extra_js}
</body>
</html>
"""

PRODUCTS = json.load(open(os.path.join(OUT, "products_build.json")))

def card_grid_js(target_id, filter_expr="true"):
    return f"""<script>
(function () {{
  var grid = document.getElementById('{target_id}');
  if (!grid) return;
  grid.innerHTML = window.VRSN_PRODUCTS.filter(function (p) {{ return {filter_expr}; }})
    .map(window.VRSN_CARD).join('');
  if (window.gsap && !matchMedia('(prefers-reduced-motion: reduce)').matches) {{
    grid.querySelectorAll('.reveal').forEach(function (el) {{
      gsap.to(el, {{ opacity: 1, y: 0, duration: 1, ease: 'power2.out',
        scrollTrigger: {{ trigger: el, start: 'top 90%', once: true }} }});
    }});
  }} else {{
    grid.querySelectorAll('.reveal').forEach(function (el) {{ el.style.opacity = 1; el.style.transform = 'none'; }});
  }}
}})();
</script>"""

pages = {}

# ── index ────────────────────────────────────────────────
pages["index.html"] = chrome(
    "vrsn · you are here",
    """
<main>
  <section class="hero" aria-label="versan">
    <div class="hero-media">
      <img src="assets/images/editorial/hero_home_2.webp" alt="a person wearing something. observed." fetchpriority="high">
    </div>
    <div class="hero-content">
      <div class="hero-lockup"><span class="vd">V</span>ERS<span class="vo">A</span>N</div>
      <h1>rebel in luxury.</h1>
    </div>
    <a class="scroll-indicator" href="#enter">continue</a>
  </section>

  <section id="enter" class="split" aria-label="sections">
    <a class="panel" href="mens.html">
      <img loading="lazy" src="assets/images/editorial/hero_male_3.webp" alt="a person wearing something. observed.">
      <span class="panel-meta">subject: men</span>
      <span class="panel-label">men</span>
    </a>
    <a class="panel" href="womens.html">
      <img loading="lazy" src="assets/images/editorial/hero_female_3.webp" alt="another person. also observed.">
      <span class="panel-meta">subject: women</span>
      <span class="panel-label">women</span>
    </a>
    <a class="panel panel-full" href="accessories.html">
      <img loading="lazy" src="assets/images/editorial/hero_accessories_1.webp" alt="objects. catalogued.">
      <span class="panel-meta">subject: objects</span>
      <span class="panel-label">accessories</span>
    </a>
  </section>

  <section class="statement wrap">
    <div class="display reveal"><span class="vd">v</span>rsn</div>
    <div class="marks reveal">est. 3:33<br>nosce te ipsum<br>45.5231&deg; n, 122.6765&deg; w</div>
    <div class="claim reveal">we make things.<br>you decide what they mean.</div>
  </section>

  <section class="wrap" aria-label="drop 001">
    <div class="grid-head reveal">
      <h2>drop 001<br>the unknown series</h2>
      <div class="sub">these are the available objects.</div>
    </div>
    <div class="product-grid" id="home-grid"></div>
  </section>

  <section class="newsletter wrap">
    <div class="nl-inner reveal">
      <h2>join the list.</h2>
      <p>we will contact you when
something worth saying happens.

this may be never.</p>
      <form>
        <input type="email" placeholder="your address" aria-label="email address" required>
        <button type="submit">[ add me ]</button>
      </form>
      <p class="nl-confirm" hidden>noted.</p>
    </div>
  </section>
</main>
""",
    active="", extra_js=card_grid_js("home-grid"))

# ── shop ─────────────────────────────────────────────────
pages["shop.html"] = chrome(
    "vrsn · acquiring",
    """
<main class="wrap">
  <header class="page-head">
    <h1 class="reveal">drop 001<br>the unknown series</h1>
    <p class="sub reveal">these are the available objects.</p>
  </header>

  <section class="apex-feature reveal" aria-label="apex">
    <a class="apex-media" href="product/the-standard-issue.html">
      <img loading="lazy" src="https://cdn.shopify.com/s/files/1/0865/2721/3761/files/3003603_0_3d.jpg?v=1780386196&width=1100" alt="the object in question." width="1100" height="1375">
    </a>
    <div>
      <div class="mono-label">apex &middot; capsule 001</div>
      <h3><a href="product/the-standard-issue.html">the standard issue</a></h3>
      <div class="apex-copy">hazmat suit &middot; drop 001 &middot; $333

produced for general use.
33 units. numbered. never restocked.
<span data-apex-live>33 of 33 remain on the record.</span>

when it is gone, the record is closed.</div>
    </div>
  </section>

  <div class="filters" role="group" aria-label="filters">
    <button class="is-active" data-filter="all">all objects</button>
    <button data-filter="men">men</button>
    <button data-filter="women">women</button>
    <button data-filter="accessories">accessories</button>
  </div>

  <div class="product-grid" id="shop-grid"></div>
</main>
""",
    active="shop",
    extra_js=card_grid_js("shop-grid") + """
<script>
(function () {
  var btns = document.querySelectorAll('.filters button');
  btns.forEach(function (b) {
    b.addEventListener('click', function () {
      btns.forEach(function (x) { x.classList.remove('is-active'); });
      b.classList.add('is-active');
      var f = b.getAttribute('data-filter');
      document.querySelectorAll('#shop-grid .product-card').forEach(function (c) {
        c.style.display = (f === 'all' || c.getAttribute('data-cats').split(' ').indexOf(f) > -1) ? '' : 'none';
      });
    });
  });
})();
</script>""")

# ── category pages ───────────────────────────────────────
def category_page(fname, title, h1, cat, hero_img, hero_alt):
    return chrome(title, f"""
<main>
  <section class="hero" style="height:72vh" aria-label="{h1}">
    <div class="hero-media">
      <img src="assets/images/editorial/{hero_img}" alt="{hero_alt}" fetchpriority="high">
    </div>
    <div class="hero-content">
      <h1>{h1}</h1>
    </div>
  </section>
  <div class="wrap">
    <div class="grid-head reveal">
      <h2>drop 001 &middot; the unknown series</h2>
      <div class="sub">these are the available objects.</div>
    </div>
    <div class="product-grid" id="cat-grid"></div>
  </div>
</main>
""", active=h1, extra_js=card_grid_js("cat-grid", f"p.categories.indexOf('{cat}') > -1"))

pages["mens.html"] = category_page("mens.html", "vrsn · subject: men", "men", "men",
                                   "hero_male_1.webp", "a person wearing something. observed.")
pages["womens.html"] = category_page("womens.html", "vrsn · subject: women", "women", "women",
                                     "hero_female_2.webp", "another person. also observed.")
pages["accessories.html"] = category_page("accessories.html", "vrsn · subject: objects", "accessories", "accessories",
                                          "hero_accessorie_2.webp", "objects. catalogued.")

# ── product pages ────────────────────────────────────────
for p in PRODUCTS:
    desc_html = p["desc"] + "\n\nvrsn &middot; rebel in luxury &middot; est. 3:33\nthe unknown series"
    apex_line = ""
    if p["tier"] == "apex":
        apex_line = ('<div class="mono-label" style="margin-bottom:8px">apex &middot; capsule 001 &middot; numbered &middot; never restocked</div>'
                     '<div class="mono-label" id="apex-remaining" data-apex-live style="margin-bottom:18px"></div>')
    body = f"""
<main class="wrap">
  <article class="pdp">
    <div class="pdp-media reveal">
      <div class="main-img">
        <img src="{p['img']}&width=1200" alt="{p['alt']}" width="1200" height="1500" fetchpriority="high">
      </div>
    </div>
    <div class="pdp-info">
      <h1 class="reveal">{p['name']}</h1>
      <div class="drop-line reveal">drop {p['drop']} &middot; the unknown series</div>
      {apex_line}
      <div class="price reveal" id="price">${p['price']:.2f}</div>
      <div class="desc reveal">{desc_html}</div>

      <div id="options"></div>
      <button class="size-guide-link" type="button" id="size-guide-open">sizing notes &rarr;</button>

      <button class="add-btn" id="add-btn" data-id="{p['id']}" data-name="{p['name']}">[ add to record ]</button>

      <details class="toggle-block">
        <summary>shipping + handling &rarr;</summary>
        <div class="toggle-body">produced somewhere.
arrives in 5&ndash;7 business days.

we do not control what happens
between there and here.

neither do you.</div>
      </details>
      <details class="toggle-block">
        <summary>returns &rarr;</summary>
        <div class="toggle-body">if it arrives damaged, we will fix it.
if you changed your mind, we understand.
contact us within 14 days.

some things cannot be returned.
this is not one of them.</div>
      </details>
    </div>
  </article>

  <section class="related">
    <h2>also observed</h2>
    <div class="product-grid" id="related-grid"></div>
  </section>
</main>

<div class="modal" id="size-modal" role="dialog" aria-label="sizing notes">
  <div class="modal-box">
    <h3>sizing notes</h3>
    <p>our garments run as expected.
your body is not a problem to be solved.

if between sizes, take the larger one.
more fabric. less compromise.

measurements are approximate.
like most things.</p>
    <button class="modal-close" type="button">[ close ]</button>
  </div>
</div>
"""
    extra = card_grid_js("related-grid", f"p.id !== '{p['id']}'") + """
<script>
(function () {
  var add = document.getElementById('add-btn');
  var product = window.VRSN_PRODUCTS.find(function (x) { return x.id === add.getAttribute('data-id'); });
  var priceEl = document.getElementById('price');
  var sel = product.options.map(function () { return null; });

  /* render option groups */
  var wrap = document.getElementById('options');
  product.options.forEach(function (opt, gi) {
    var label = document.createElement('div');
    label.className = 'variant-label';
    label.textContent = opt.label;
    var row = document.createElement('div');
    row.className = 'variant-row';
    opt.values.forEach(function (v) {
      var b = document.createElement('button');
      b.type = 'button';
      b.textContent = v;
      b.addEventListener('click', function () {
        row.querySelectorAll('button').forEach(function (x) { x.classList.remove('is-selected'); });
        b.classList.add('is-selected');
        sel[gi] = v;
        update();
      });
      row.appendChild(b);
    });
    wrap.appendChild(label);
    wrap.appendChild(row);
  });

  /* pre-select the first value of every option group —
     the add button must never appear dead */
  wrap.querySelectorAll('.variant-row').forEach(function (row) {
    var first = row.querySelector('button');
    if (first) first.click();
  });

  function currentVariant() {
    if (sel.some(function (s) { return s === null; })) return undefined;
    return window.VRSN_VARIANT(product, sel);
  }

  function update() {
    var v = currentVariant();
    if (v && v.price) priceEl.textContent = '$' + v.price.toFixed(2);
    else priceEl.textContent = '$' + product.price.toFixed(2);
    if (v && v.qty === 0) {
      add.textContent = 'gone.';
      add.setAttribute('disabled', '');
    } else {
      add.removeAttribute('disabled');
      if (!add._done) add.textContent = '[ add to record ]';
    }
  }

  /* apex depletion */
  var ar = document.getElementById('apex-remaining');
  if (ar && product.apex) {
    ar.textContent = product.apex.remaining + ' of ' + product.apex.cap + ' remain on the record.';
  }

  add.addEventListener('mouseenter', function () {
    if (!add._done && !add.hasAttribute('disabled')) add.textContent = '[ adding... ]';
  });
  add.addEventListener('mouseleave', function () {
    if (!add._done && !add.hasAttribute('disabled')) add.textContent = '[ add to record ]';
  });
  add.addEventListener('click', function () {
    if (sel.some(function (s) { return s === null; })) {
      add.textContent = '[ make your selections ]';
      setTimeout(function () { add.textContent = '[ add to record ]'; }, 1800);
      return;
    }
    var v = currentVariant();
    if (!v || v.qty === 0) return;
    window.VRSN_RECORD.add(product.id, sel.join('|'));
    window.VRSN_TOAST(product.name);
    add.textContent = '[ recorded ]';
    add._done = true;
    setTimeout(function () { add._done = false; add.textContent = '[ add to record ]'; }, 3000);
  });

  var m = document.getElementById('size-modal');
  document.getElementById('size-guide-open').addEventListener('click', function () { m.classList.add('is-open'); });
  m.querySelector('.modal-close').addEventListener('click', function () { m.classList.remove('is-open'); });
  m.addEventListener('click', function (e) { if (e.target === m) m.classList.remove('is-open'); });
})();
</script>"""
    pages[f"product/{p['id']}.html"] = chrome("vrsn · considering", body, root="..", extra_js=extra)

# ── unknown series ───────────────────────────────────────
QUOTES = [
    ("the-standard-issue", "it's fine. everything is fine."),
    ("the-bucket", "it never used to flood here."),
    ("the-corduroy-cap", "everyone agreed. no one was asked."),
    ("the-fanny", "you can't be too careful anymore."),
    ("the-annette", "i don't remember agreeing to this."),
]
qblocks = ""
for pid, q in QUOTES:
    prod = next(x for x in PRODUCTS if x["id"] == pid)
    qblocks += f"""
  <section class="quote-block">
    <blockquote>&ldquo;{q}&rdquo;</blockquote>
    <div class="attr">&mdash; unknown</div>
    <div class="q-product"><a href="product/{pid}.html">{prod['name']} &middot; ${prod['price']:.2f}</a></div>
  </section>
"""
pages["unknown-series.html"] = chrome(
    "vrsn · you found it",
    f"""
<main>
  <header class="page-head wrap">
    <h1 class="reveal">the unknown series<br>capsule 001</h1>
    <p class="sub reveal">these pieces ask something.
they do not wait for an answer.</p>
  </header>

  <section class="quote-block">
    <blockquote>&ldquo;we have always done it this way.&rdquo;</blockquote>
    <div class="attr">&mdash; unknown</div>
    <div class="q-product">who told you that was true?</div>
  </section>
{qblocks}
</main>
""",
    active="the unknown series")

# ── about ────────────────────────────────────────────────
pages["about.html"] = chrome(
    "vrsn · looking for something",
    """
<main class="wrap">
  <section class="manifesto">
    <div class="display reveal"><span class="vd">v</span>rsn</div>
    <p class="reveal">we make things that say something<br>without saying it.</p>
    <p class="reveal">every piece is an argument.<br>every garment is a position.<br>you wear it. you carry it.</p>
    <p class="reveal">this is not a fashion house.<br>this is a question about why<br>fashion houses exist.</p>
    <p class="fine reveal">absurd realism.<br>est. 3:33.<br>nosce te ipsum.</p>
    <p class="reveal">rebel in luxury.</p>
    <p class="fine reveal">&mdash;<br><br>45.5231&deg; n, 122.6765&deg; w</p>
    <p class="hidden-line">absurd realism was coined here.
you are welcome to use it.
credit is optional.
understanding is required.</p>
  </section>
</main>
""",
    active="about")

# ── cart ─────────────────────────────────────────────────
pages["cart.html"] = chrome(
    "vrsn · committed",
    """
<main class="wrap">
  <section class="cart-page">
    <h1>your record</h1>
    <div class="cart-count-line" id="cart-count-line"></div>
    <div id="cart-lines"></div>
    <div id="cart-summary-wrap"></div>
    <div class="cart-foot-note">taxes calculated at checkout.
shipping calculated at checkout.
everything is calculated, eventually.</div>
  </section>
</main>
""",
    extra_js="""
<script>
(function () {
  function money(n) { return '$' + n.toFixed(2); }
  function render() {
    var r = window.VRSN_RECORD.get();
    var lines = document.getElementById('cart-lines');
    var sumWrap = document.getElementById('cart-summary-wrap');
    var count = document.getElementById('cart-count-line');
    var n = r.reduce(function (s, l) { return s + l.qty; }, 0);
    if (n === 0) {
      count.textContent = '';
      sumWrap.innerHTML = '';
      lines.innerHTML = '<div class="cart-empty"><p>nothing here.\\n\\nthis is either restraint or hesitation.\\nboth are acceptable.</p>' +
        '<div class="utility-actions"><a href="shop.html">[ return to shop ]</a></div></div>';
      return;
    }
    count.textContent = n + ' item' + (n === 1 ? '' : 's') + ' selected for acquisition.';
    var total = 0;
    var permalink = [];
    lines.innerHTML = r.map(function (l, i) {
      var p = window.VRSN_PRODUCTS.find(function (x) { return x.id === l.id; });
      if (!p) return '';
      var v = p.variants ? p.variants[l.variant] : null;
      var unit = (v && v.price) ? v.price : p.price;
      total += unit * l.qty;
      if (v && v.vid) permalink.push(v.vid + ':' + l.qty);
      return '<div class="cart-line">' +
        '<img src="' + window.VRSN_IMG(p.img, 200) + '" alt="' + p.alt + '">' +
        '<div><div class="cl-name">' + p.name + '</div>' +
        '<div class="cl-meta">' + l.variant.split('|').join(' &middot; ') + ' &middot; qty ' + l.qty + '</div>' +
        '<button class="cl-remove" data-i="' + i + '">remove from record</button></div>' +
        '<div class="cl-price">' + money(unit * l.qty) + '</div></div>';
    }).join('');
    sumWrap.innerHTML = '<div class="cart-summary"><div class="sum-label">summary</div>' +
      '<div class="sum-row"><span>subtotal</span><span>' + money(total) + '</span></div>' +
      '<div class="utility-actions"><button id="proceed-btn">[ proceed ]</button></div>' +
      '<p class="dim" style="font-size:10px;letter-spacing:0.08em;margin-top:16px">point of no return.<br>complete your acquisition below.</p></div>';
    lines.querySelectorAll('.cl-remove').forEach(function (b) {
      b.addEventListener('click', function () {
        window.VRSN_RECORD.remove(parseInt(b.getAttribute('data-i'), 10));
        render();
      });
    });
    var pr = document.getElementById('proceed-btn');
    if (pr) pr.addEventListener('click', function () {
      var items = [];
      r.forEach(function (l) {
        var p = window.VRSN_PRODUCTS.find(function (x) { return x.id === l.id; });
        var v = p && p.variants ? p.variants[l.variant] : null;
        if (v && v.vid) items.push({ vid: v.vid, qty: l.qty });
      });
      if (items.length === 0) return;
      pr.textContent = '[ proceeding... ]';
      window.VRSN_CHECKOUT(items).then(function (url) { location.href = url; });
    });
  }
  render();
})();
</script>""")

# ── privacy ──────────────────────────────────────────────
pages["privacy.html"] = chrome(
    "vrsn · you won't read this",
    """
<main class="wrap">
  <section class="utility-page" style="min-height:auto">
    <h1 style="font-size:clamp(34px,5vw,56px)">privacy policy</h1>
    <p>your data belongs to us.
it always has.
you agreed to this.</p>
    <p>we collect what we need.
we keep what we collect.
we use it to understand you
better than you understand yourself.</p>
    <p class="dim">this is standard practice.
this is considered acceptable.</p>
    <p>scroll to the bottom to confirm
you did not read this.</p>
    <div class="utility-actions">
      <button type="button" onclick="location.href='index.html'">[ i have read and understood ]</button>
      <button type="button" onclick="location.href='index.html'">[ i have not read this ]</button>
    </div>
    <p class="dim" style="margin-top:2em">both buttons go to the same place.</p>
    <p class="dim">&mdash;

for actual data inquiries:
ops@cntrllabs.art

last updated: july 2026
because something changed.</p>
  </section>
</main>
""")

# ── 404 ──────────────────────────────────────────────────
pages["404.html"] = chrome(
    "vrsn · lost, like most things",
    """
<main class="wrap">
  <section class="utility-page">
    <h1>404</h1>
    <p>this page has been removed.</p>
    <p class="dim">like the community garden on
45th and morrison.
like the affordable housing proposal.
like your search history.</p>
    <p>it was here.
now it isn't.
this is normal.</p>
    <div class="utility-actions">
      <a href="index.html">[ return to what remains ]</a>
    </div>
  </section>
</main>
""")

# ── write everything ─────────────────────────────────────
for path, html in pages.items():
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(html)
    print("wrote", path)
