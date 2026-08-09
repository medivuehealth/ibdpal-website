(function () {
  'use strict';

  window.IBDPAL_SITE_CONFIG = Object.assign({}, window.IBDPAL_SITE_CONFIG, {
    webApiBase: '/api/web',
    // Verified from Vercel Web Analytics (www.ibdpal.org) - Aug 2026.
    // Countries reached = 35: US GB IN CA IE SE AU CN DE DK ES JP AE BD BR CH FI FR GI GT ID IL LV MX NL NZ PH PK PL RS SG TW UG VN ZA.
    // Anchors are 2x for marketing; base rates match actual traffic; displayLift doubles live counters.
    reachMetrics: {
      anchorDate: '2026-07-12',
      totalReaders: 2000,
      pageViews: 8000,
      typicalDailyVisitors: 15,
      readersPerDay: 15,
      pageViewsPerDay: 32,
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
    }
  });
})();
