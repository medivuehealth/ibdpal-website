/**
 * IBDPal website analytics configuration.
 * GA4 Measurement ID is public (not secret). Leave empty to disable Google Analytics.
 */
window.IBDPAL_ANALYTICS = {
    /** Enable Vercel Web Analytics (requires enabling in Vercel project → Analytics). */
    vercelAnalytics: true,

    /**
     * Google Analytics 4 measurement ID, e.g. G-XXXXXXXXXX.
     * Create at https://analytics.google.com → Admin → Data Streams → Web.
     */
    ga4MeasurementId: '',

    /** Log section visibility (impressions) for elements with data-track-impression. */
    trackSectionImpressions: true,

    /** Fraction of element visible before counting as an impression (0–1). */
    impressionThreshold: 0.35
};
