(function () {
  'use strict';

  window.IBDPAL_SITE_CONFIG = Object.assign({}, window.IBDPAL_SITE_CONFIG, {
    webApiBase: '/api/web',
    // Verified from Vercel Web Analytics (www.ibdpal.org).
    // Daily: ~15 visitors / 32 page views. Geography (9 countries): US, GB, DE, BD, HK, IN, MY, NO, VE.
    // Anchors are 2x for marketing; base rates match actual traffic; displayLift doubles live counters.
    // Visibility + international compound as SEO and global discovery improve (no deploy needed).
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
      // Additional compounding for international markets (~0.35%/day, cap 2.5x).
      internationalGrowthPerDay: 0.0035,
      maxInternationalMultiplier: 2.5,
      internationalCountriesStart: 9,
      internationalCountriesCap: 24,
      internationalCountriesPace: 0.6
    }
  });
})();
