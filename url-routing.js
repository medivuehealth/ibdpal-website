// Client-side URL routing for clean URLs
// This handles the routing when server-side rewriting is not available

(function() {
    'use strict';
    
    // URL routing configuration
    const routes = {
        '/support': 'support.html',
        '/privacy': 'privacy.html', 
        '/terms': 'terms.html',
        '/about': 'executive-summary.html',
        '/': 'index.html'
    };
    
    // Get current path
    function getCurrentPath() {
        return window.location.pathname;
    }
    
    // Handle route
    function handleRoute() {
        const path = getCurrentPath();
        const targetFile = routes[path];
        
        if (targetFile && targetFile !== 'index.html') {
            // Redirect to the actual HTML file
            window.location.href = targetFile;
        }
    }
    
    // Initialize routing
    function init() {
        // Only handle routing if we're not already on an HTML file
        const currentPath = getCurrentPath();
        const isHtmlFile = currentPath.endsWith('.html') || currentPath === '/';
        
        if (!isHtmlFile) {
            handleRoute();
        }
    }
    
    // Run on page load
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
    
    // Handle browser back/forward buttons
    window.addEventListener('popstate', handleRoute);
    
})();

