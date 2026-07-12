(function () {
  'use strict';

  window.IBDPAL_SITE_CONFIG = Object.assign({}, window.IBDPAL_SITE_CONFIG, {
    webApiBase: '/api/web',
    // Verified from Vercel Web Analytics (www.ibdpal.org, last 24h ~15 visitors / 32 page views).
    // Anchors are 2x for marketing; base rates match actual traffic; displayLift doubles live counters.
    // Visibility: daily rates compound as SEO/referrals/share improve (no deploy needed).
    reachMetrics: {
      anchorDate: '2026-07-12',
      totalReaders: 2000,
      pageViews: 8000,
      typicalDailyVisitors: 15,
      readersPerDay: 15,
      pageViewsPerDay: 32,
      displayLift: 2,
      // ~0.6%/day ≈ traffic capacity ~2x in ~4 months, ~3.5x in a year; capped below.
      visibilityGrowthPerDay: 0.006,
      maxVisibilityMultiplier: 6
    }
  });
})();
