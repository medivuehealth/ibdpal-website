/**
 * Blog thumbs up / down — records votes via /api/blog-vote (Vercel serverless + Blob).
 */
(function () {
    'use strict';

    var STORAGE_PREFIX = 'ibdpal-blog-vote-';

    function getWidget() {
        return document.querySelector('.blog-vote[data-blog-slug]');
    }

    function getSlug(widget) {
        return widget.getAttribute('data-blog-slug');
    }

    function hasVoted(slug) {
        try {
            return localStorage.getItem(STORAGE_PREFIX + slug) !== null;
        } catch (e) {
            return false;
        }
    }

    function markVoted(slug, vote) {
        try {
            localStorage.setItem(STORAGE_PREFIX + slug, vote);
        } catch (e) {
            /* ignore */
        }
    }

    function setCounts(widget, counts) {
        var upEl = widget.querySelector('[data-vote-count="up"]');
        var downEl = widget.querySelector('[data-vote-count="down"]');
        if (upEl) {
            upEl.textContent = String(counts.up || 0);
        }
        if (downEl) {
            downEl.textContent = String(counts.down || 0);
        }
    }

    function setStatus(widget, message, isError) {
        var status = widget.querySelector('.blog-vote-status');
        if (!status) {
            return;
        }
        status.textContent = message;
        status.hidden = !message;
        status.classList.toggle('blog-vote-status--error', !!isError);
    }

    function disableButtons(widget) {
        widget.querySelectorAll('.blog-vote-btn').forEach(function (btn) {
            btn.disabled = true;
            btn.setAttribute('aria-disabled', 'true');
        });
        widget.classList.add('blog-vote--voted');
    }

    function loadCounts(slug, widget) {
        fetch('/api/blog-vote?slug=' + encodeURIComponent(slug))
            .then(function (res) {
                if (!res.ok) {
                    throw new Error('load failed');
                }
                return res.json();
            })
            .then(function (counts) {
                setCounts(widget, counts);
            })
            .catch(function () {
                setStatus(widget, '', false);
            });
    }

    function submitVote(slug, vote, widget) {
        setStatus(widget, 'Saving…', false);
        fetch('/api/blog-vote', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ slug: slug, vote: vote })
        })
            .then(function (res) {
                return res.json().then(function (data) {
                    return { ok: res.ok, data: data };
                });
            })
            .then(function (result) {
                if (!result.ok) {
                    throw new Error(result.data?.error || 'Vote failed');
                }
                markVoted(slug, vote);
                disableButtons(widget);
                setCounts(widget, result.data.counts);
                setStatus(widget, 'Thanks for your feedback.', false);
                if (typeof window.ibdpalTrack === 'function') {
                    window.ibdpalTrack('blog_vote', { slug: slug, vote: vote });
                }
            })
            .catch(function (err) {
                setStatus(widget, err.message || 'Could not save vote. Try again later.', true);
            });
    }

    function init() {
        var widget = getWidget();
        if (!widget) {
            return;
        }

        var slug = getSlug(widget);
        if (!slug) {
            return;
        }

        loadCounts(slug, widget);

        if (hasVoted(slug)) {
            disableButtons(widget);
            var prior = localStorage.getItem(STORAGE_PREFIX + slug);
            setStatus(widget, 'You voted ' + (prior === 'up' ? '👍' : '👎') + ' on this article.', false);
        }

        widget.addEventListener('click', function (e) {
            var btn = e.target.closest('.blog-vote-btn');
            if (!btn || btn.disabled) {
                return;
            }
            var vote = btn.getAttribute('data-vote');
            if (vote !== 'up' && vote !== 'down') {
                return;
            }
            if (hasVoted(slug)) {
                return;
            }
            submitVote(slug, vote, widget);
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
