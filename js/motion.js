/* motion.js — the slow drift. gsap + scrolltrigger.
   everything moves slightly. nothing announces itself. */

(function () {
  'use strict';

  var REDUCED = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (REDUCED || typeof gsap === 'undefined') {
    document.querySelectorAll('.reveal').forEach(function (el) {
      el.style.opacity = '1';
      el.style.transform = 'none';
    });
    return;
  }

  gsap.registerPlugin(ScrollTrigger);

  function init() {

    /* hero — slow settle + scroll parallax */
    var heroMedia = document.querySelector('.hero-media');
    if (heroMedia) {
      gsap.fromTo(heroMedia, { scale: 1.1 }, { scale: 1, duration: 2.8, ease: 'power2.out' });
      gsap.to(heroMedia, {
        yPercent: 14,
        ease: 'none',
        scrollTrigger: { trigger: '.hero', start: 'top top', end: 'bottom top', scrub: true }
      });
      var hc = document.querySelector('.hero-content');
      if (hc) {
        gsap.fromTo(hc.children, { opacity: 0, y: 24 },
          { opacity: 1, y: 0, duration: 1.4, stagger: 0.25, delay: 0.5, ease: 'power2.out' });
        gsap.to(hc, {
          opacity: 0, y: -60,
          scrollTrigger: { trigger: '.hero', start: '20% top', end: 'bottom top', scrub: true }
        });
      }
    }

    /* panels — depth drift: each image drifts at its own rate */
    document.querySelectorAll('.panel img, .apex-media img').forEach(function (img, i) {
      gsap.fromTo(img, { yPercent: -5 }, {
        yPercent: 5,
        ease: 'none',
        scrollTrigger: { trigger: img.closest('.panel, .apex-media'), start: 'top bottom', end: 'bottom top', scrub: true }
      });
    });

    /* reveals */
    document.querySelectorAll('.reveal').forEach(function (el) {
      gsap.to(el, {
        opacity: 1, y: 0,
        duration: 1.1,
        ease: 'power2.out',
        scrollTrigger: { trigger: el, start: 'top 88%', once: true }
      });
    });

    /* quote blocks — slow rise, slight scale */
    document.querySelectorAll('.quote-block blockquote').forEach(function (q) {
      gsap.fromTo(q, { opacity: 0, scale: 0.97, y: 30 }, {
        opacity: 1, scale: 1, y: 0,
        duration: 1.3, ease: 'power2.out',
        scrollTrigger: { trigger: q, start: 'top 80%', once: true }
      });
    });

    ScrollTrigger.refresh();
  }

  /* wait for the loading screen if it's running */
  if (window.vrsnReady) init();
  else window.addEventListener('vrsn:ready', init, { once: true });

})();
