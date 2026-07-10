/* data.js — the objects on record.
   prices + variant ids mirror the shopify store (iesefi-cx.myshopify.com).
   checkout via shopify cart permalinks — no credentials required.
   images served from the shopify cdn, width-capped, rendered b&w by css. */

window.VRSN_STORE = 'https://iesefi-cx.myshopify.com';

window.VRSN_PRODUCTS = [
  {
    id: 'the-standard-issue',
    name: 'the standard issue',
    observed: 'required equipment',
    drop: '001',
    tier: 'apex',
    type: 'hazmat suit',
    price: 333.00,
    handle: 'the-standard-issue-drop-001',
    categories: ['men', 'women'],
    img: 'https://cdn.shopify.com/s/files/1/0865/2721/3761/files/3003603_0_3d.jpg?v=1780386196',
    apex: { cap: 33, remaining: 33 },
    options: [
      { label: 'select size', values: ['s', 'm', 'l', 'xl'] },
      { label: 'select cord', values: ['white', 'black', 'orange', 'pink', 'green'] }
    ],
    variants: {
      's|white': { vid: 50284954386625, qty: 2 },
      's|black': { vid: 50284954419393, qty: 2 },
      's|orange': { vid: 50284954452161, qty: 2 },
      's|pink': { vid: 50284954484929, qty: 2 },
      's|green': { vid: 50284954517697, qty: 2 },
      'm|white': { vid: 50284954550465, qty: 2 },
      'm|black': { vid: 50284954583233, qty: 2 },
      'm|orange': { vid: 50284954616001, qty: 2 },
      'm|pink': { vid: 50284954648769, qty: 2 },
      'm|green': { vid: 50284954681537, qty: 2 },
      'l|white': { vid: 50284954714305, qty: 2 },
      'l|black': { vid: 50284954747073, qty: 2 },
      'l|orange': { vid: 50284954779841, qty: 2 },
      'l|pink': { vid: 50284954812609, qty: 2 },
      'l|green': { vid: 50284954845377, qty: 2 },
      'xl|white': { vid: 50284954878145, qty: 1 },
      'xl|black': { vid: 50284954910913, qty: 1 },
      'xl|orange': { vid: 50284954943681, qty: 1 },
      'xl|pink': { vid: 50284954976449, qty: 0 },
      'xl|green': { vid: 50284955009217, qty: 0 }
    },
    desc: 'a suit.\n\nproduced for general use. all-over print on poly waterproof fabric. zip-up front. hooded. the versan mark repeated across the entire surface.\n\n33 units. numbered. never restocked.\nwhen it is gone, the record is closed.',
    alt: 'the object in question.'
  },
  {
    id: 'the-corduroy-cap',
    name: 'the corduroy cap',
    observed: 'a manufactured desire',
    drop: '002',
    tier: 'accessible',
    type: 'embroidered cap',
    price: 63.00,
    handle: 'vintage-corduroy-cap',
    categories: ['men', 'women', 'accessories'],
    img: 'https://cdn.shopify.com/s/files/1/0865/2721/3761/files/vintage-corduroy-cap-black-front-6a1de7159cc2b.jpg?v=1780344619',
    options: [
      { label: 'select color', values: ['black', 'navy', 'brown', 'olive', 'burgundy'] }
    ],
    variants: {
      'black': { vid: 50282921525441 },
      'navy': { vid: 50282921558209 },
      'brown': { vid: 50282921590977 },
      'olive': { vid: 50282921623745 },
      'burgundy': { vid: 50282921656513 }
    },
    desc: 'a cap.\n\n100% cotton corduroy. unstructured 6-panel, low profile. the v mark embroidered at the front.\n\nwear it like you know something.',
    alt: 'the object in question.'
  },
  {
    id: 'the-bucket',
    name: 'the bucket',
    observed: 'shelter from nothing',
    drop: '003',
    tier: 'accessible',
    type: 'bucket hat',
    price: 73.00,
    handle: 'the-bucket',
    categories: ['men', 'women', 'accessories'],
    img: 'https://cdn.shopify.com/s/files/1/0865/2721/3761/files/3003618_0_3d.jpg?v=1780388610',
    options: [
      { label: 'select size', values: ['xs', 's/m', 'l/xl', 'xxl'] },
      { label: 'select fabric', values: ['cotton denim', 'woven canvas', 'waterproof'] }
    ],
    variants: {
      'xs|cotton denim': { vid: 50285075792065 },
      'xs|woven canvas': { vid: 50285075824833 },
      'xs|waterproof': { vid: 50285075857601 },
      's/m|cotton denim': { vid: 50285075890369 },
      's/m|woven canvas': { vid: 50285075923137 },
      's/m|waterproof': { vid: 50285075955905 },
      'l/xl|cotton denim': { vid: 50285075988673 },
      'l/xl|woven canvas': { vid: 50285076021441 },
      'l/xl|waterproof': { vid: 50285076054209 },
      'xxl|cotton denim': { vid: 50285076086977 },
      'xxl|woven canvas': { vid: 50285076119745 },
      'xxl|waterproof': { vid: 50285076152513 }
    },
    desc: 'a hat.\n\nwoven, reversible. printed inside and out, matte finish. classic bucket silhouette.\n\nit will not protect you from what is coming. it is a hat.',
    alt: 'the object in question.'
  },
  {
    id: 'the-fanny',
    name: 'the fanny',
    observed: 'carried weight',
    drop: '004',
    tier: 'signature',
    type: 'leather fanny pack',
    price: 133.00,
    handle: 'the-fanny',
    categories: ['accessories'],
    img: 'https://cdn.shopify.com/s/files/1/0865/2721/3761/files/3003628_0_3d.jpg?v=1780390195',
    options: [
      { label: 'select strap', values: ['standard · waist', 'long · cross body'] },
      { label: 'select material', values: ['nappa leather', 'brushed twill'] }
    ],
    variants: {
      'standard · waist|nappa leather': { vid: 50285160726721 },
      'standard · waist|brushed twill': { vid: 50285160759489 },
      'long · cross body|nappa leather': { vid: 50285160792257 },
      'long · cross body|brushed twill': { vid: 50285160825025 }
    },
    desc: 'a bag.\n\n100% nappa leather, handmade to order. adjustable strap. the versan wordmark debossed on the front.\n\neverything you carry is recorded somewhere.',
    alt: 'the object in question.'
  },
  {
    id: 'the-annette',
    name: 'the annette',
    observed: 'named after someone',
    drop: '005',
    tier: 'accessible',
    type: 'oversized tee',
    price: 93.00,
    handle: 'the-annette-oversized-graphic-t-shirt',
    categories: ['men', 'women'],
    img: 'https://cdn.shopify.com/s/files/1/0865/2721/3761/files/3003663_0_3d.jpg?v=1780396700',
    options: [
      { label: 'select size', values: ['xs', 's', 'm', 'l', 'xl', '2xl', '3xl', '4xl', '5xl', '6xl', '7xl'] },
      { label: 'select fabric', values: ['ponte jersey', 'bounce cotton'] }
    ],
    variants: {
      'xs|ponte jersey': { vid: 50286262616257 },
      'xs|bounce cotton': { vid: 50286262649025, price: 123.00, qty: 0 },
      's|ponte jersey': { vid: 50286262681793 },
      's|bounce cotton': { vid: 50286262714561, price: 123.00, qty: 0 },
      'm|ponte jersey': { vid: 50286262747329 },
      'm|bounce cotton': { vid: 50286262780097, price: 123.00, qty: 0 },
      'l|ponte jersey': { vid: 50286262812865 },
      'l|bounce cotton': { vid: 50286262845633, price: 123.00, qty: 0 },
      'xl|ponte jersey': { vid: 50286262878401 },
      'xl|bounce cotton': { vid: 50286262911169, price: 123.00, qty: 0 },
      '2xl|ponte jersey': { vid: 50286262943937 },
      '2xl|bounce cotton': { vid: 50286262976705, price: 123.00, qty: 0 },
      '3xl|ponte jersey': { vid: 50286263009473 },
      '3xl|bounce cotton': { vid: 50286263042241, price: 123.00, qty: 0 },
      '4xl|ponte jersey': { vid: 50286263075009 },
      '4xl|bounce cotton': { vid: 50286263107777, price: 123.00, qty: 0 },
      '5xl|ponte jersey': { vid: 50286263140545 },
      '5xl|bounce cotton': { vid: 50286263173313, price: 123.00, qty: 0 },
      '6xl|ponte jersey': { vid: 50286263206081 },
      '6xl|bounce cotton': { vid: 50286263238849, price: 123.00, qty: 0 },
      '7xl|ponte jersey': { vid: 50286263271617 },
      '7xl|bounce cotton': { vid: 50286263304385, price: 123.00, qty: 0 }
    },
    desc: 'a shirt.\n\noversized fit, heavyweight jersey. the v mark at the chest.\n\nnamed after someone who knew something.',
    alt: 'the object in question.'
  }
];

window.VRSN_IMG = function (url, w) {
  return url + '&width=' + (w || 900);
};

/* resolve a variant record from a product + selected option values array */
window.VRSN_VARIANT = function (p, sel) {
  if (!p.variants) return null;
  return p.variants[sel.join('|')] || null;
};
