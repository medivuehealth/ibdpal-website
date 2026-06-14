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
