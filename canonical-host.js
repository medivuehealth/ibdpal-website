/**
 * Redirect www.ibdpal.org to canonical https://ibdpal.org (preserve path + hash).
 * Load synchronously in <head> so navigation stays on a valid TLS host.
 */
(function () {
    if (window.location.hostname === 'www.ibdpal.org') {
        window.location.replace(
            'https://ibdpal.org' +
            window.location.pathname +
            window.location.search +
            window.location.hash
        );
    }
})();
