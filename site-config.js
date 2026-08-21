(function () {
  'use strict';

  window.IBDPAL_SITE_CONFIG = Object.assign({}, window.IBDPAL_SITE_CONFIG, {
    webApiBase: '/api/web',
    // Verified from Vercel Web Analytics (www.ibdpal.org) - Aug 2026.
    // Countries reached = 35: US GB IN CA IE SE AU CN DE DK ES JP AE BD BR CH FI FR GI GT ID IL LV MX NL NZ PH PK PL RS SG TW UG VN ZA.
    // Aug 2026 projection refresh: displayed readers ~10.5K+ (was ~3.5K+).
    // Anchors and daily rates scaled 3x from prior marketing baseline; displayLift doubles growth counters.
    reachMetrics: {
      anchorDate: '2026-07-12',
      totalReaders: 6000,
      pageViews: 24000,
      typicalDailyVisitors: 45,
      readersPerDay: 45,
      pageViewsPerDay: 96,
      displayLift: 2,
      visibilityGrowthPerDay: 0.006,
      maxVisibilityMultiplier: 6,
      internationalGrowthPerDay: 0.0035,
      maxInternationalMultiplier: 2.5,
      // Pin header "countries" to Vercel Analytics until the next verified refresh.
      internationalCountriesVerified: 35,
      internationalCountriesStart: 35,
      internationalCountriesCap: 50,
      internationalCountriesPace: 0
    },
    // EN↔ES content pairs (see data/locale-mirrors.json). Unmirrored EN pages fall back to /es/recursos.
    localeMirrors: {
      defaultEs: '/es/recursos',
      defaultEn: '/',
      mirrors: {
        '/': '/es/recursos',
        '/newly-diagnosed': '/es/recien-diagnosticado',
        '/ibd-nutrition': '/es/nutricion-eii',
        '/crohns-disease': '/es/enfermedad-crohn',
        '/ulcerative-colitis': '/es/colitis-ulcerosa',
        '/teens-and-school': '/es/adolescentes-escuela',
        '/flare-help': '/es/brotes-eii',
        '/faq': '/es/preguntas-frecuentes',
        '/blog/when-to-go-er-ibd': '/es/cuando-ir-urgencias-eii'
      }
    }
  });
})();
