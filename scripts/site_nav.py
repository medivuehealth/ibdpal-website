"""Shared site chrome for static HTML generators (nav + analytics scripts)."""

TAB_NAV_HTML = """
        <nav class="tab-navigation">
            <div class="tab-container">
                <a href="/#overview" class="tab-button" data-tab="overview">Overview</a>
                <a href="/#app" class="tab-button" data-tab="app">IBDPal App</a>
                <a href="/#resources" class="tab-button" data-tab="resources">Resources</a>
                <a href="/#blogs" class="tab-button" data-tab="blogs">Blogs</a>
                <a href="/#community" class="tab-button" data-tab="community">Community</a>
                <a href="/#contact" class="tab-button" data-tab="contact">Contact</a>
            </div>
        </nav>
"""

# Required on every public page — loads Vercel Web Analytics + optional GA4
PAGE_SCRIPTS = """
    <script src="/site-global.js" defer></script>
    <script src="/analytics-config.js"></script>
    <script src="/analytics.js" defer></script>
"""
