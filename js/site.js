/* site.js — chrome, observation, record-keeping.
   you found this. most people don't look. */

(function () {
  'use strict';

  var REDUCED = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (REDUCED) document.documentElement.classList.add('no-motion');
  var ROOT = document.body.getAttribute('data-root') || '.';

  /* ── loading screen ─────────────────────────────────── */

  var loading = document.getElementById('loading-screen');
  var seen = sessionStorage.getItem('vrsn-loading-shown');

  function endLoading() {
    if (!loading) return;
    loading.style.transition = 'opacity 0.6s';
    loading.style.opacity = '0';
    setTimeout(function () {
      loading.hidden = true;
      document.documentElement.classList.remove('is-loading');
      window.dispatchEvent(new CustomEvent('vrsn:ready'));
      window.vrsnReady = true;
    }, 620);
  }

  if (loading && !seen && !REDUCED) {
    sessionStorage.setItem('vrsn-loading-shown', 'true');
    document.documentElement.classList.add('is-loading');
    var lines = loading.querySelectorAll('.loading-lines p');
    lines.forEach(function (p, i) {
      setTimeout(function () {
        p.style.transition = 'opacity 0.3s, transform 0.3s';
        p.style.opacity = '1';
        p.style.transform = 'translateY(0)';
      }, 120 + i * 200);
    });
    setTimeout(endLoading, 1500 + 400);
  } else {
    if (loading) loading.hidden = true;
    window.vrsnReady = true;
    setTimeout(function () {
      window.dispatchEvent(new CustomEvent('vrsn:ready'));
    }, 0);
  }

  /* ── cookie banner ──────────────────────────────────── */

  var cb = document.getElementById('cookie-banner');
  if (cb && !localStorage.getItem('vrsn-cookies')) {
    setTimeout(function () {
      cb.style.transition = 'transform 0.5s cubic-bezier(0.22,1,0.36,1)';
      cb.style.transform = 'translateY(0)';
    }, 2600);
    cb.querySelectorAll('button').forEach(function (b) {
      b.addEventListener('click', function () {
        localStorage.setItem('vrsn-cookies', 'acknowledged');
        cb.style.transform = 'translateY(110%)';
      });
    });
  }

  /* ── policy bar (return visits) ─────────────────────── */

  var pb = document.getElementById('policy-bar');
  var visits = parseInt(localStorage.getItem('vrsn-visits') || '0', 10) + 1;
  localStorage.setItem('vrsn-visits', String(visits));
  if (pb && visits > 1 && !sessionStorage.getItem('vrsn-policy-dismissed')) {
    pb.classList.add('is-visible');
    pb.querySelectorAll('button').forEach(function (b) {
      b.addEventListener('click', function () {
        sessionStorage.setItem('vrsn-policy-dismissed', '1');
        pb.classList.remove('is-visible');
      });
    });
  }

  /* ── mobile nav ─────────────────────────────────────── */

  var toggle = document.getElementById('nav-toggle');
  var mnav = document.getElementById('mobile-nav');
  if (toggle && mnav) {
    toggle.addEventListener('click', function () { mnav.classList.add('is-open'); });
    mnav.querySelector('.close-btn').addEventListener('click', function () {
      mnav.classList.remove('is-open');
    });
  }

  /* ── cursor — motion sensor trail ───────────────────── */

  var cursor = document.getElementById('cursor');
  if (cursor && matchMedia('(pointer: fine)').matches && !REDUCED) {
    document.body.classList.add('has-cursor');
    var lastTrail = 0;
    document.addEventListener('mousemove', function (e) {
      cursor.classList.add('is-active');
      cursor.style.left = e.clientX + 'px';
      cursor.style.top = e.clientY + 'px';
      var now = performance.now();
      if (now - lastTrail > 24) {
        lastTrail = now;
        var d = document.createElement('div');
        d.style.cssText = 'position:fixed;left:' + e.clientX + 'px;top:' + e.clientY +
          'px;width:5px;height:5px;border-radius:50%;background:#2D6A4F;opacity:0.6;' +
          'pointer-events:none;z-index:9999;transform:translate(-50%,-50%);transition:opacity 0.2s linear';
        document.body.appendChild(d);
        requestAnimationFrame(function () { d.style.opacity = '0'; });
        setTimeout(function () { d.remove(); }, 240);
      }
    }, { passive: true });
    document.addEventListener('mouseover', function (e) {
      var hit = e.target.closest('a, button, [role="button"], input, label, select, summary');
      cursor.classList.toggle('is-hover', !!hit);
    });
    document.addEventListener('mouseleave', function () { cursor.classList.remove('is-active'); });
  }

  /* ── atmosphere — rain + particle field ─────────────── */

  var canvas = document.getElementById('atmosphere');
  if (canvas && !REDUCED) {
    var ctx = canvas.getContext('2d');
    var W, H, DPR = Math.min(window.devicePixelRatio || 1, 1.5);
    var particles = [], drops = [];
    var running = true;

    function size() {
      W = canvas.width = Math.floor(innerWidth * DPR);
      H = canvas.height = Math.floor(innerHeight * DPR);
      canvas.style.width = innerWidth + 'px';
      canvas.style.height = innerHeight + 'px';
    }
    size();
    addEventListener('resize', size, { passive: true });

    var COUNT = innerWidth < 700 ? 16 : 34;
    for (var i = 0; i < COUNT; i++) {
      particles.push({
        x: Math.random(), y: Math.random(),
        vx: (Math.random() - 0.5) * 0.00006,
        vy: (Math.random() - 0.5) * 0.00005,
        r: Math.random() * 1.4 + 0.4,
        a: Math.random() * 0.09 + 0.03,
        ph: Math.random() * Math.PI * 2
      });
    }

    function spawnDrop() {
      if (drops.length < 4 && Math.random() < 0.012) {
        drops.push({
          x: Math.random(), y: -0.05,
          v: 0.006 + Math.random() * 0.008,
          len: 0.03 + Math.random() * 0.05,
          a: 0.05 + Math.random() * 0.07
        });
      }
    }

    var t = 0;
    function frame() {
      if (!running) return;
      t += 0.016;
      ctx.clearRect(0, 0, W, H);

      /* particle field — faint, forest-adjacent, near-invisible */
      for (var i = 0; i < particles.length; i++) {
        var p = particles[i];
        p.x += p.vx; p.y += p.vy;
        if (p.x < 0) p.x = 1; if (p.x > 1) p.x = 0;
        if (p.y < 0) p.y = 1; if (p.y > 1) p.y = 0;
        var breathe = 0.6 + 0.4 * Math.sin(t * 0.5 + p.ph);
        ctx.beginPath();
        ctx.arc(p.x * W, p.y * H, p.r * DPR, 0, Math.PI * 2);
        ctx.fillStyle = 'rgba(45,106,79,' + (p.a * breathe).toFixed(3) + ')';
        ctx.fill();
      }

      /* rain — occasional, vertical, unremarked */
      spawnDrop();
      for (var j = drops.length - 1; j >= 0; j--) {
        var d = drops[j];
        d.y += d.v;
        ctx.beginPath();
        ctx.moveTo(d.x * W, d.y * H);
        ctx.lineTo(d.x * W, (d.y + d.len) * H);
        ctx.strokeStyle = 'rgba(244,241,235,' + d.a.toFixed(3) + ')';
        ctx.lineWidth = 1 * DPR;
        ctx.stroke();
        if (d.y > 1.1) drops.splice(j, 1);
      }
      requestAnimationFrame(frame);
    }
    requestAnimationFrame(frame);

    document.addEventListener('visibilitychange', function () {
      running = !document.hidden;
      if (running) requestAnimationFrame(frame);
    });
  }

  /* ── scroll progress ────────────────────────────────── */

  var prog = document.getElementById('scroll-progress');
  if (prog) {
    var update = function () {
      var max = document.documentElement.scrollHeight - innerHeight;
      var n = max > 0 ? Math.min(100, Math.round(scrollY / max * 100)) : 100;
      prog.textContent = 'you are ' + n + '% through this page.';
    };
    addEventListener('scroll', update, { passive: true });
    update();
  }

  /* ── the record (cart) ──────────────────────────────── */

  /* v2 key — clears stage-1 test records that predate real variant ids.
     lines that can't resolve to a shopify variant are dropped on read. */
  function getRecord() {
    try {
      var r = JSON.parse(localStorage.getItem('vrsn-record-v2') || '[]');
      return r.filter(function (l) {
        var p = (window.VRSN_PRODUCTS || []).find(function (x) { return x.id === l.id; });
        return p && p.variants && p.variants[l.variant];
      });
    } catch (e) { return []; }
  }
  function setRecord(r) {
    localStorage.setItem('vrsn-record-v2', JSON.stringify(r));
    updateCount();
  }
  function updateCount() {
    var n = getRecord().reduce(function (s, l) { return s + l.qty; }, 0);
    document.querySelectorAll('.cart-count').forEach(function (el) {
      el.textContent = n > 0 ? '(' + n + ')' : '';
    });
  }
  updateCount();

  window.VRSN_RECORD = {
    get: getRecord,
    add: function (id, variant) {
      var r = getRecord();
      var line = r.find(function (l) { return l.id === id && l.variant === variant; });
      if (line) line.qty += 1;
      else r.push({ id: id, variant: variant, qty: 1 });
      setRecord(r);
    },
    remove: function (idx) {
      var r = getRecord();
      r.splice(idx, 1);
      setRecord(r);
    }
  };

  /* ── toast ──────────────────────────────────────────── */

  window.VRSN_TOAST = function (name) {
    var toast = document.getElementById('toast');
    if (!toast) return;
    toast.querySelector('.t-body').textContent = name + ' has been added\nto your record.';
    toast.classList.add('is-visible');
    clearTimeout(toast._t);
    toast._t = setTimeout(function () { toast.classList.remove('is-visible'); }, 4200);
  };

  /* ── search overlay ─────────────────────────────────── */

  var so = document.getElementById('search-overlay');
  var sBtn = document.getElementById('search-open');
  if (so && sBtn) {
    var input = so.querySelector('input');
    var results = document.getElementById('search-results');
    sBtn.addEventListener('click', function () {
      so.classList.add('is-open');
      input.focus();
    });
    document.getElementById('search-close').addEventListener('click', function () {
      so.classList.remove('is-open');
      input.value = ''; results.innerHTML = '';
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') so.classList.remove('is-open');
    });
    input.addEventListener('input', function () {
      var q = input.value.trim().toLowerCase();
      results.innerHTML = '';
      if (!q) return;
      var hits = (window.VRSN_PRODUCTS || []).filter(function (p) {
        return p.name.includes(q) || p.type.includes(q) || p.observed.includes(q);
      });
      if (hits.length === 0) {
        results.innerHTML = '<p class="sr-empty">nothing found for "' + q.replace(/</g, '&lt;') +
          '"\n\nthis doesn\'t mean it doesn\'t exist.\nit means we don\'t have it.\nyet.</p>';
      } else {
        hits.forEach(function (p) {
          var a = document.createElement('a');
          a.className = 'sr-item';
          a.href = ROOT + '/product/' + p.id + '.html';
          a.innerHTML = '<span>' + p.name + '</span><span>$' + p.price.toFixed(2) + '</span>';
          results.appendChild(a);
        });
      }
    });
  }

  /* ── newsletter ─────────────────────────────────────── */

  document.querySelectorAll('.newsletter form').forEach(function (f) {
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var email = f.querySelector('input').value.trim();
      if (!email) return;
      var list = JSON.parse(localStorage.getItem('vrsn-the-record-list') || '[]');
      list.push({ email: email, at: Date.now() });
      localStorage.setItem('vrsn-the-record-list', JSON.stringify(list));
      f.style.display = 'none';
      var c = f.parentElement.querySelector('.nl-confirm');
      if (c) c.hidden = false;
    });
  });

  /* ── storefront api ─────────────────────────────────── */

  window.VRSN_SF = function (query, variables) {
    var cfg = window.VRSN_SHOPIFY;
    if (!cfg) return Promise.reject(new Error('no storefront config'));
    return fetch('https://' + cfg.domain + '/api/' + cfg.apiVersion + '/graphql.json', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-Shopify-Storefront-Access-Token': cfg.storefrontAccessToken
      },
      body: JSON.stringify({ query: query, variables: variables || {} })
    }).then(function (r) { return r.json(); });
  };

  /* real checkout: storefront cart api → hosted checkout.
     falls back to a cart permalink if the api call fails. */
  window.VRSN_CHECKOUT = function (lines) {
    var permalink = (window.VRSN_STORE || '') + '/cart/' +
      lines.map(function (l) { return l.vid + ':' + l.qty; }).join(',');
    return window.VRSN_SF(
      'mutation cartCreate($input: CartInput!) {\n' +
      '  cartCreate(input: $input) {\n' +
      '    cart { checkoutUrl }\n' +
      '    userErrors { message }\n' +
      '  }\n' +
      '}',
      {
        input: {
          lines: lines.map(function (l) {
            return { quantity: l.qty, merchandiseId: 'gid://shopify/ProductVariant/' + l.vid };
          })
        }
      }
    ).then(function (res) {
      var url = res && res.data && res.data.cartCreate && res.data.cartCreate.cart &&
        res.data.cartCreate.cart.checkoutUrl;
      return url || permalink;
    }).catch(function () { return permalink; });
  };

  /* live apex depletion — sums quantityAvailable across apex variants.
     if the token's scopes don't expose inventory counts, the baked
     figures stay in place. availability flags still come through. */
  function liveApex() {
    var els = document.querySelectorAll('[data-apex-live]');
    if (!els.length || !window.VRSN_SHOPIFY) return;
    window.VRSN_SF(
      'query apex($handle: String!) {\n' +
      '  product(handle: $handle) {\n' +
      '    variants(first: 50) { nodes { quantityAvailable availableForSale } }\n' +
      '  }\n' +
      '}',
      { handle: 'the-standard-issue-drop-001' }
    ).then(function (res) {
      var nodes = res && res.data && res.data.product && res.data.product.variants &&
        res.data.product.variants.nodes;
      if (!nodes) return;
      var known = nodes.every(function (n) { return typeof n.quantityAvailable === 'number'; });
      if (!known) return; /* inventory scope not granted — keep baked count */
      var remaining = nodes.reduce(function (s, n) {
        return s + Math.max(0, n.quantityAvailable);
      }, 0);
      els.forEach(function (el) {
        el.textContent = remaining > 0
          ? remaining + ' of 33 remain on the record.'
          : 'the record is closed.';
      });
    }).catch(function () {});
  }
  liveApex();

  /* ── product card rendering ─────────────────────────── */

  window.VRSN_CARD = function (p) {
    var tierLabel = p.tier === 'apex' ? 'apex · capsule 001' : '';
    return '<a class="product-card reveal" href="' + ROOT + '/product/' + p.id + '.html" data-cats="' + p.categories.join(' ') + '">' +
      (tierLabel ? '<span class="p-tier">' + tierLabel + '</span>' : '') +
      '<div class="card-media"><img loading="lazy" src="' + window.VRSN_IMG(p.img, 800) + '" alt="' + p.alt + '" width="800" height="1000"></div>' +
      '<div class="card-meta">' +
      '<div class="p-name" data-name="' + p.name + '" data-observed="' + p.observed + '">' + p.name + '</div>' +
      '<div class="p-sub">' + (p.sub || '') + '</div>' +
      '<div class="p-price">$' + p.price.toFixed(2) + '</div>' +
      '</div></a>';
  };

  /* hover — the name you were given vs the name we use */
  document.addEventListener('mouseover', function (e) {
    var n = e.target.closest('.p-name');
    if (n) n.textContent = n.getAttribute('data-observed');
  });
  document.addEventListener('mouseout', function (e) {
    var n = e.target.closest('.p-name');
    if (n) n.textContent = n.getAttribute('data-name');
  });

})();
