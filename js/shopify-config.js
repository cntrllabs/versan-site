/* shopify-config.js — the only shopify credential in this repo.
   the storefront access token is public by design (client-side, read/checkout only). */

window.VRSN_SHOPIFY = {
  domain: 'iesefi-cx.myshopify.com',
  storefrontAccessToken: '7d64d0d227b6f8ae60ee254d3787616b',
  apiVersion: '2024-10',

  /* archived: the shopify plan lapsed 2026-10-01 and the store is frozen.
     the storefront api and hosted checkout no longer answer. the site itself
     is static and unaffected — product data lives in js/data.js, imagery in
     assets/products/. set true to skip the dead api call and show the archive
     notice immediately. left false, checkout still degrades to the same notice
     on failure, just one round-trip later. */
  archived: false,

  archiveNote: 'this storefront ran live commerce on the shopify storefront ' +
    'api through september 2026 — real variants, real cart, real hosted ' +
    'checkout. the plan has since lapsed and the store is frozen, so checkout ' +
    'is retired. everything else you see is the original build, unchanged.'
};
