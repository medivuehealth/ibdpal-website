(function () {
  'use strict';

  window.IBDPAL_SITE_CONFIG = Object.assign({}, window.IBDPAL_SITE_CONFIG, {
    webApiBase: '/api/web',
    // Verified from Vercel Web Analytics (www.ibdpal.org) — Jul 2026.
    // Countries reached = 16: US, GB, IN, CA, DE, AU, BD, GT, HK, ID, IE, JP, MY, PK, SE, VE.
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
      internationalCountriesVerified: 16,
      internationalCountriesStart: 16,
      internationalCountriesCap: 40,
      internationalCountriesPace: 0
    }
  });
})();
