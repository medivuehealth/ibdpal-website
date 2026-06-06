/**
 * Redirect bare ibdpal.org to www.ibdpal.org (preserve path + hash).
 * Vercel already 307s apex → www; this is a client-side fallback for edge cases.
 */
(function () {
    if (window.location.hostname === 'ibdpal.org') {
        window.location.replace(
            'https://www.ibdpal.org' +
            window.location.pathname +
            window.location.search +
            window.location.hash
        );
    }
})();
