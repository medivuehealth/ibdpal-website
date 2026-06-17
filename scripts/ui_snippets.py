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
                            <li><strong>Family &amp; lifestyle articles:</strong> 6 new posts &mdash; <a href="/blog/ibd-summer-heat-hydration">summer heat</a>, <a href="/blog/ibd-flare-go-bag">flare go-bag</a>, <a href="/blog/siblings-when-child-has-ibd">siblings</a>, <a href="/blog/when-to-call-ibd-help-center">Help Center vs clinic</a>, <a href="/blog/dining-out-ibd-restaurants">dining out</a>, <a href="/blog/infusion-day-what-to-expect">infusion day</a></li>
                            <li><strong>Patient guides:</strong> 3 new guides &mdash; <a href="/guides/first-gastroenterology-appointment-ibd">first GI appointment</a>, <a href="/guides/ibd-flare-emergency-supplies">flare supplies</a>, <a href="/guides/dining-out-with-ibd">dining out</a></li>
                            <li><strong>ImproveCareNow (ICN):</strong> <strong>10 resource highlights</strong> total (+3: <a href="/blog/icn-self-management-handbook-ibd">self-management handbook</a>, <a href="/blog/icn-health-literacy-toolkit-ibd">health literacy</a>, <a href="/blog/icn-lifestyle-ibd-toolkit">lifestyle toolkit</a>)</li>
                            <li><strong>Crohn&rsquo;s &amp; Colitis Foundation:</strong> CCF non-affiliation disclaimer on <a href="/about">About</a> and softened content notes site-wide</li>
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

SITE_UPDATES_SUBTAB_HTML = """
                <article class="support-section seo-landing tab-page-section tab-page-section--compact">
                    <header class="page-header-compact">
                        <h1 class="page-header-compact__title">Site Updates</h1>
                        <p class="page-header-compact__lead">Month-by-month changelog &middot; updated June 2026</p>
                    </header>
{UPDATES_MONTHLY_SECTIONS_HTML}
                    <section class="seo-landing__block">
                        <h2>Stay in the loop</h2>
                        <p><a href="/blog">All articles</a> &middot; <a href="/library">Content library</a> &middot; <a href="/#about">About MediVue</a></p>
                    </section>
                    <div class="signup-section signup-section--compact" data-track-impression="email_signup_section" data-track-label="Stay Updated signup">
                        <h3>Email updates</h3>
                        <p>Get notified about new IBDPal features and articles.</p>
                        <form class="email-form" id="emailForm">
                            <div class="input-group">
                                <input type="email" id="email" placeholder="Enter your email address" required>
                                <button type="submit">Notify Me</button>
                            </div>
                            <p class="form-note">We respect your privacy. Unsubscribe at any time.</p>
                        </form>
                    </div>
                </article>
"""

METRICS_SUBTAB_HTML = """
                <article class="support-section seo-landing tab-page-section tab-page-section--compact">
                    <header class="page-header-compact">
                        <h1 class="page-header-compact__title">Website &amp; App Analytics</h1>
                        <p class="page-header-compact__lead">App Store and site discovery snapshots</p>
                    </header>
                    <section class="discovery-dashboard discovery-dashboard--compact" aria-labelledby="metrics-app-heading">
                        <div class="discovery-dashboard__panel">
                            <header class="discovery-dashboard__head">
                                <p class="discovery-dashboard__eyebrow">IBDPal app</p>
                                <h2 id="metrics-app-heading" class="discovery-dashboard__title">App Store reach</h2>
                            </header>
                            <div class="discovery-metrics-rows" role="group" aria-label="App discovery snapshot">
                                <div class="discovery-metrics-row">
                                    <span class="discovery-metrics-row__label">Search visibility</span>
                                    <span class="discovery-metrics-row__value">1.5K+</span>
                                </div>
                                <div class="discovery-metrics-row">
                                    <span class="discovery-metrics-row__label">Total reach</span>
                                    <span class="discovery-metrics-row__value">1.6K+</span>
                                </div>
                                <div class="discovery-metrics-row">
                                    <span class="discovery-metrics-row__label">Organic discovery</span>
                                    <span class="discovery-metrics-row__value">87%</span>
                                </div>
                            </div>
                        </div>
                    </section>
                    <section class="seo-landing__block">
                        <h2>Website (ibdpal.org)</h2>
                        <ul class="seo-landing__list">
                            <li><strong>140+</strong> patient education pages (articles, guides, state support)</li>
                            <li>Privacy-oriented analytics via Vercel Web Analytics (anonymous page views, no PHI)</li>
                            <li>Structured data and sitemap for search discovery; organic SEO metrics on Overview</li>
                        </ul>
                    </section>
                </article>
"""

IBD_NEWS_TAB_HTML = """
                <article class="support-section seo-landing tab-page-section">
                    <h1>IBD Policy &amp; Advocacy News</h1>
                    <p class="support-intro">Federal and state IBD policy highlights with links to the <a href="https://www.crohnscolitisfoundation.org/" rel="noopener noreferrer">Crohn&rsquo;s &amp; Colitis Foundation</a>. Education only.</p>

                    <section class="seo-landing__block ibd-news-featured">
                        <h2>Under review</h2>
                        <article class="ibd-news-card">
                            <p class="ibd-news-card__tag">Federal regulation &middot; Prior authorization</p>
                            <h3 class="ibd-news-card__title">Days, not weeks: faster prior authorization decisions</h3>
                            <p>The federal <strong>CMS Interoperability and Prior Authorization Final Rule (CMS-0057-F)</strong> sets maximum turnaround times for many government-backed plans (Medicare Advantage, Medicaid managed care, CHIP, and Affordable Care Act marketplace plans). Insurers must approve or deny <strong>urgent</strong> requests within <strong>72 hours</strong> and <strong>standard</strong> requests within <strong>7 calendar days</strong>.</p>
                            <p>This is a crucial first step toward shorter waits for IBD tests and treatments. Patient advocates are urging federal officials to fully implement and expand these protections.</p>
                            <p class="ibd-news-card__actions">
                                <a href="https://www.cms.gov/newsroom/fact-sheets/cms-interoperability-and-prior-authorization-final-rule-cms-0057-f" rel="noopener noreferrer">CMS fact sheet</a>
                                &middot;
                                <a href="https://www.crohnscolitisfoundation.org/your-guide-to-navigating-prior-authorization" rel="noopener noreferrer">CCF prior authorization guide</a>
                                &middot;
                                <a href="https://www.crohnscolitisfoundation.org/get-involved/be-an-advocate/action-center" rel="noopener noreferrer">Take action (CCF)</a>
                            </p>
                        </article>
                        <article class="ibd-news-card">
                            <p class="ibd-news-card__tag">Congress &middot; Step therapy</p>
                            <h3 class="ibd-news-card__title">Safe Step Act: reforming fail-first protocols</h3>
                            <p>The <strong>Safe Step Act</strong> (H.R. 2630 / S. 652) would create a clearer appeal process when insurers require patients to try and fail on preferred drugs before covering a provider-prescribed treatment. More than 40% of IBD patients report experiencing step therapy barriers.</p>
                            <p>At a recent U.S. House committee hearing, lawmakers highlighted how step therapy can leave patients behind. The Crohn&rsquo;s &amp; Colitis Foundation continues grassroots advocacy on Capitol Hill for commonsense reform.</p>
                            <p class="ibd-news-card__actions">
                                <a href="https://www.crohnscolitisfoundation.org/get-involved/be-advocate/advocacy-priorities/step-therapy/federal-safe-step-act" rel="noopener noreferrer">Safe Step Act overview</a>
                                &middot;
                                <a href="https://action.crohnscolitisfoundation.org/a/ssa-webpage" rel="noopener noreferrer">Ask Congress to pass it</a>
                            </p>
                        </article>
                    </section>

                    <section class="seo-landing__block">
                        <h2>Recently approved &amp; in effect</h2>
                        <ul class="seo-landing__list">
                            <li><strong>Jan. 1, 2026:</strong> Faster prior authorization decision timelines under CMS-0057-F begin for impacted federal plans</li>
                            <li><strong>March 31, 2026:</strong> First public prior authorization performance metrics due from impacted payers</li>
                            <li><strong>Jan. 1, 2027:</strong> Prior authorization and interoperability FHIR APIs required in production (next implementation milestone)</li>
                        </ul>
                    </section>

                    <section class="seo-landing__block">
                        <h2>Advocacy highlights</h2>
                        <ul class="seo-landing__list">
                            <li><strong>Capitol Hill briefing:</strong> The Crohn&rsquo;s &amp; Colitis Foundation hosted a bipartisan briefing on how additional federal IBD research investment could accelerate prevention and treatment progress</li>
                            <li><strong>Step therapy in Congress:</strong> Rep. Lucy McBath cited an IBD volunteer&rsquo;s story at a House committee hearing, calling step therapy a sweeping mandate that too often leaves patients behind</li>
                            <li><strong>Prior auth pushback:</strong> After thousands of patient letters and a rally, UnitedHealthcare delayed a planned expansion of prior authorization for many endoscopy and colonoscopy procedures</li>
                        </ul>
                        <p><em>Source: Crohn&rsquo;s &amp; Colitis Foundation federal and grassroots advocacy updates.</em></p>
                    </section>

                    <section class="seo-landing__block">
                        <h2>Take action</h2>
                        <ul class="seo-landing__list">
                            <li><a href="https://www.crohnscolitisfoundation.org/get-involved/be-an-advocate/action-center" rel="noopener noreferrer">CCF Action Center</a> &mdash; contact lawmakers in two clicks</li>
                            <li><a href="https://action.crohnscolitisfoundation.org/a/ssa-webpage" rel="noopener noreferrer">Support the Safe Step Act</a></li>
                            <li><a href="https://www.crohnscolitisfoundation.org/science-and-professionals/program-materials/appeal-letters" rel="noopener noreferrer">Appeal letter templates</a> for denied biologics and treatments</li>
                            <li><a href="https://www.crohnscolitisfoundation.org/get-involved/be-an-advocate/advocacy-priorities/step-therapy/state-legislation" rel="noopener noreferrer">Step therapy state legislation</a></li>
                        </ul>
                    </section>

                    <section class="seo-landing__block">
                        <h2>More resources</h2>
                        <p><a href="/#site-updates">IBDPal site updates</a> &middot; <a href="/#about">About MediVue</a> &middot; <a href="/research">Trusted clinical sources</a> &middot; <a href="/#community">Find support by state</a></p>
                    </section>
                </article>
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
