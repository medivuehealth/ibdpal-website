"""Shared HTML snippets for premium UI (resource toolbar, etc.)."""

RESOURCE_TOOLBAR_HTML = """
                    <div class="resource-library__toolbar resource-library__toolbar--premium">
                        <div class="resource-library__search-wrap">
                            <svg class="resource-library__search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3-3"/></svg>
                            <input type="search" class="resource-library__search" placeholder="Search dairy, gluten, flare, school…" aria-label="Search resources">
                        </div>
                        <div class="resource-library__pills" role="group" aria-label="Filter by category">
                            <button type="button" class="resource-pill is-active" data-category="">All</button>
                            <button type="button" class="resource-pill" data-category="getting-started">Getting started</button>
                            <button type="button" class="resource-pill" data-category="nutrition">Nutrition</button>
                            <button type="button" class="resource-pill" data-category="treatment">Treatment</button>
                            <button type="button" class="resource-pill" data-category="wellness">Wellness</button>
                            <button type="button" class="resource-pill" data-category="community">Community</button>
                            <button type="button" class="resource-pill" data-category="family">Family</button>
                            <button type="button" class="resource-pill" data-category="clinical">Clinical</button>
                        </div>
                        <select class="resource-library__filter sr-only" aria-hidden="true" tabindex="-1">
                            <option value="">All</option>
                            <option value="getting-started">Getting started</option>
                            <option value="community">Community</option>
                            <option value="nutrition">Nutrition</option>
                            <option value="wellness">Wellness</option>
                            <option value="treatment">Treatment</option>
                            <option value="family">Family</option>
                            <option value="clinical">Clinical</option>
                        </select>
                    </div>
                    <div class="resource-library__empty" hidden>
                        <svg class="resource-library__empty-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M21 21l-4.3-4.3M10.5 18a7.5 7.5 0 1 0 0-15 7.5 7.5 0 0 0 0 15z"/><path d="M8 10h5M8 13h3"/></svg>
                        <p class="resource-library__empty-title">No matches yet</p>
                        <p class="resource-library__empty-hint">Try <strong>dairy</strong>, <strong>gluten</strong>, <strong>immune</strong>, or clear your filters.</p>
                    </div>
"""

BLOG_FILTER_PILLS_HTML = """
                    <div class="blog-index-toolbar" role="group" aria-label="Filter articles">
                        <button type="button" class="blog-pill is-active" data-blog-filter="">All topics</button>
                        <button type="button" class="blog-pill" data-blog-filter="nutrition">Nutrition</button>
                        <button type="button" class="blog-pill" data-blog-filter="treatment">Treatment</button>
                        <button type="button" class="blog-pill" data-blog-filter="wellness">Wellness</button>
                        <button type="button" class="blog-pill" data-blog-filter="family">Family</button>
                        <button type="button" class="blog-pill" data-blog-filter="teen">Teens</button>
                        <button type="button" class="blog-pill" data-blog-filter="flare">Flares</button>
                    </div>
"""

BLOG_VOTE_THUMB_UP_SVG = (
    '<svg class="blog-vote-svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false">'
    '<path fill="currentColor" d="M1 21h4V9H1v12zm22-11c0-1.1-.9-2-2-2h-6.31l.95-4.57.03-.32c0-.41-.17-.79-.44-1.06L14.17 1 7.59 7.59C7.22 7.96 7 8.45 7 9v10c0 1.1.9 2 2 2h9c.83 0 1.54-.5 1.84-1.22l3.02-7.05c.09-.23.14-.47.14-.73v-2z"/>'
    "</svg>"
)

BLOG_VOTE_THUMB_DOWN_SVG = (
    '<svg class="blog-vote-svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false">'
    '<path fill="currentColor" d="M15 3H6c-.83 0-1.54.5-1.84 1.22l-3.02 7.05c-.09.23-.14.47-.14.73v2c0 1.1.9 2 2 2h6.31l-.95 4.57-.03.32c0 .41-.17.79-.44 1.06L9.83 23 16.41 16.41c.37-.37.59-.86.59-1.41V5c0-1.1-.9-2-2-2zm4 0v12h4V3h-4z"/>'
    "</svg>"
)

BLOG_BACK_LINK_HTML = (
    '<p class="blog-back">'
    '<a href="/#articles" class="blog-back-link">&larr; All posts</a></p>'
)

UPDATES_MONTHLY_SECTIONS_HTML = """
                    <section class="seo-landing__block updates-month">
                        <h2>June 2026</h2>
                        <ul class="seo-landing__list">
                            <li><strong>ImproveCareNow (ICN):</strong> Published <strong>7 resource highlights</strong> with Creative Commons attribution and direct PDF downloads &mdash; <a href="/blog/icn-accommodations-toolkit-ibd">accommodations</a>, <a href="/blog/icn-college-ibd-toolkit">college</a>, <a href="/blog/icn-caregiver-coping-resource">caregivers</a>, <a href="/blog/icn-mental-health-provider-guide">mental health</a>, <a href="/blog/icn-transfer-toolkit-adult-care">adult transfer</a>, <a href="/blog/icn-ostomy-toolkit-pediatric">ostomy</a>, <a href="/blog/icn-ibd-holidays-special-occasions">holidays</a></li>
                            <li><strong>Crohn&rsquo;s &amp; Colitis Foundation:</strong> Linked <a href="https://www.crohnscolitisfoundation.org/" rel="noopener noreferrer">CCF</a> across patient education content notes site-wide</li>
                            <li>Compact ICN source footnotes; article topic filter fix; sitemap rebuild for Google indexing</li>
                            <li>New nonprofit pages: <a href="/about">About</a>, <a href="/founder">MediVue Founders</a>, <a href="/contact">Contact</a>, <a href="/impact">Impact</a>, <a href="/library">Content library</a></li>
                        </ul>
                    </section>
                    <section class="seo-landing__block updates-month">
                        <h2>May 2026</h2>
                        <ul class="seo-landing__list">
                            <li><strong>7 wellness articles:</strong> <a href="/blog/depression-anxiety-ibd">depression &amp; anxiety</a>, <a href="/blog/probiotics-ibd-gut-health">probiotics</a>, <a href="/blog/micronutrients-ibd-deficiencies">micronutrients</a>, <a href="/blog/stress-coping-strategies-ibd">stress coping</a>, <a href="/blog/ibd-fatigue-brain-fog">fatigue &amp; brain fog</a>, <a href="/blog/ibd-joint-pain-arthritis">joint pain</a>, <a href="/blog/ibd-night-sweats">night sweats</a></li>
                            <li>Nutrition article series with imagery: <a href="/blog/best-foods-crohns-flare">flare nutrition</a>, <a href="/blog/foods-that-may-trigger-uc-symptoms">UC food triggers</a>, <a href="/blog/hydration-tips-ibd">hydration</a>, <a href="/blog/how-nutrition-impacts-gut-health-ibd">gut health</a>, <a href="/blog/tracking-food-symptoms-ibdpal">food &amp; symptom tracking</a></li>
                            <li>Patient Library navigation: six main tabs with docked sub-tabs for mobile</li>
                            <li>SEO improvements: meta tags, structured data, and organic discovery metrics on Overview</li>
                        </ul>
                    </section>
                    <section class="seo-landing__block updates-month">
                        <h2>April 2026</h2>
                        <ul class="seo-landing__list">
                            <li>Lifestyle and treatment articles: travel, biologics, low-residue diet, workplace rights</li>
                            <li>Homepage refresh with start-here hub and magazine-style article cards</li>
                            <li>Resources search tuned for common patient terms (dairy, gluten, flare, school)</li>
                        </ul>
                    </section>
                    <section class="seo-landing__block updates-month">
                        <h2>March 2026</h2>
                        <ul class="seo-landing__list">
                            <li>Patient guides expansion: flares, nutrition, pediatric help, ostomy living</li>
                            <li>Searchable <a href="/resources">resource library</a> with category filters</li>
                            <li><a href="/research">Trusted clinical sources</a> hub for AGA, NIH, and partner organizations</li>
                        </ul>
                    </section>
                    <section class="seo-landing__block updates-month">
                        <h2>February 2026</h2>
                        <ul class="seo-landing__list">
                            <li>50-state <a href="/#community">community support map</a> refreshed with local chapters and programs</li>
                            <li><a href="/clinical-partnerships">Clinical partnerships</a> and admissions information pages</li>
                        </ul>
                    </section>
                    <section class="seo-landing__block updates-month">
                        <h2>January 2026</h2>
                        <ul class="seo-landing__list">
                            <li>Patient Library <a href="/#articles">Articles tab</a> launched with topic filters</li>
                            <li>First IBDPal introduction article and social sharing on blog posts</li>
                            <li>App Store QR code; homepage updated from &ldquo;Coming Soon&rdquo; to <a href="/#app">Available at App Store</a></li>
                            <li>Tab URL routing so sections open via direct links (e.g. <code>/#articles</code>)</li>
                        </ul>
                    </section>
                    <section class="seo-landing__block updates-month">
                        <h2>December 2025</h2>
                        <ul class="seo-landing__list">
                            <li>Age-inclusive language across site copy and blog content</li>
                            <li>Medical disclaimer blocks added to patient education articles</li>
                        </ul>
                    </section>
                    <section class="seo-landing__block updates-month">
                        <h2>November 2025</h2>
                        <ul class="seo-landing__list">
                            <li><strong>How it Works</strong> tab: Track &amp; Discover, Optimize &amp; Reduce, Test &amp; Verify, Sustain &amp; Evolve</li>
                            <li>Phase imagery and tagline highlighting micronutrient tracking from daily foods</li>
                        </ul>
                    </section>
                    <section class="seo-landing__block updates-month">
                        <h2>October 2025</h2>
                        <ul class="seo-landing__list">
                            <li>Deployed to <strong>Vercel</strong> with clean URLs for all pages</li>
                            <li><a href="/privacy">Privacy</a>, <a href="/support">Support</a>, and <a href="/terms">Terms</a> pages with full legal content</li>
                            <li>Tab-based navigation, compact healthcare layout, and app screenshots gallery</li>
                        </ul>
                    </section>
                    <section class="seo-landing__block updates-month">
                        <h2>September 2025</h2>
                        <ul class="seo-landing__list">
                            <li><strong>ibdpal.org</strong> launch as MediVue nonprofit patient education site</li>
                            <li>MediVue legal, trademark, and 501(c)(3) information in site footer</li>
                            <li>Website palette aligned with IBDPal iOS app and App Store branding</li>
                        </ul>
                    </section>
"""


def blog_vote_widget(slug: str) -> str:
    """Thumbs up/down feedback block for blog articles (SVG icons, encoding-safe)."""
    return f"""                    <div class="blog-vote" data-blog-slug="{slug}">
                        <p class="blog-vote-prompt">Was this article helpful?</p>
                        <div class="blog-vote-actions">
                            <button type="button" class="blog-vote-btn blog-vote-btn--up" data-vote="up" aria-label="Thumbs up, helpful">
                                {BLOG_VOTE_THUMB_UP_SVG}
                                <span class="blog-vote-count" data-vote-count="up">0</span>
                            </button>
                            <button type="button" class="blog-vote-btn blog-vote-btn--down" data-vote="down" aria-label="Thumbs down, not helpful">
                                {BLOG_VOTE_THUMB_DOWN_SVG}
                                <span class="blog-vote-count" data-vote-count="down">0</span>
                            </button>
                        </div>
                        <p class="blog-vote-status" hidden></p>
                    </div>"""
