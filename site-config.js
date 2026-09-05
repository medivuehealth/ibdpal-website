(function () {
  'use strict';

  window.IBDPAL_SITE_CONFIG = Object.assign({}, window.IBDPAL_SITE_CONFIG, {
    webApiBase: '/api/web',
    // Verified from Vercel Web Analytics (www.ibdpal.org) - Sep 2026.
    // Countries reached = 41 (Vercel Web Analytics, Sep 2026).
    // Sep 2026 projection refresh: displayed readers ~20K+ (was ~12.5K+ / prior 10.5K+).
    // Page views kept near the recent ~3.1x readers ratio seen in live header math.
    reachMetrics: {
      anchorDate: '2026-09-05',
      totalReaders: 20000,
      pageViews: 62000,
      typicalDailyVisitors: 95,
      readersPerDay: 95,
      pageViewsPerDay: 295,
      displayLift: 1,
      visibilityGrowthPerDay: 0.004,
      maxVisibilityMultiplier: 4,
      internationalGrowthPerDay: 0.003,
      maxInternationalMultiplier: 2.2,
      // Pin header "countries" to Vercel Analytics until the next verified refresh.
      internationalCountriesVerified: 41,
      internationalCountriesStart: 41,
      internationalCountriesCap: 60,
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
