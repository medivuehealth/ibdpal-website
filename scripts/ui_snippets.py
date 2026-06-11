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
