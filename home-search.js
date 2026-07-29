/**
 * Homepage topic search: instant matches, aliases, zero-result capture, related clicks.
 */
(function () {
  'use strict';

  var WEB_API_BASE = (window.IBDPAL_SITE_CONFIG && window.IBDPAL_SITE_CONFIG.webApiBase) || '/api/web';
  var FALLBACK_SUGGESTIONS = [
    { term: 'enteral', label: 'Enteral' },
    { term: 'fatigue', label: 'Fatigue' },
    { term: 'flare', label: 'Flare' },
    { term: 'biologics', label: 'Biologics' },
    { term: 'low residue', label: 'Low residue' }
  ];
  var MAX_RESULTS = 8;

  function escapeHtml(s) {
    return String(s || '').replace(/[&<>"']/g, function (char) {
      return {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#39;'
      }[char];
    });
  }

  function normalizeTerm(value) {
    return String(value || '').toLowerCase().replace(/[^\w\s'-]/g, ' ').replace(/\s+/g, ' ').trim();
  }

  function debounce(fn, delay) {
    var timer = null;
    return function () {
      var args = arguments;
      window.clearTimeout(timer);
      timer = window.setTimeout(function () {
        fn.apply(null, args);
      }, delay);
    };
  }

  function buildHaystack(item) {
    return (
      item.title +
      ' ' +
      (item.description || '') +
      ' ' +
      (item.tags || []).join(' ') +
      ' ' +
      (item.keywords || []).join(' ')
    ).toLowerCase();
  }

  function scoreItem(item, q) {
    if (!q) return 0;
    var title = String(item.title || '').toLowerCase();
    var hay = buildHaystack(item);
    var score = 0;
    if (title.indexOf(q) !== -1) score += 12;
    if (hay.indexOf(q) !== -1) score += 6;
    var tokens = q.split(/\s+/).filter(Boolean);
    tokens.forEach(function (tok) {
      if (title.indexOf(tok) !== -1) score += 4;
      else if (hay.indexOf(tok) !== -1) score += 2;
    });
    return score;
  }

  function suggestAlias(term) {
    if (window.IBDPAL_ENGAGEMENT && window.IBDPAL_ENGAGEMENT.suggestAlias) {
      return window.IBDPAL_ENGAGEMENT.suggestAlias(term);
    }
    return null;
  }

  function recordSearchEvent(term, resultCount, clickedUrl) {
    var normalizedTerm = normalizeTerm(term);
    if (normalizedTerm.length < 2) return;
    window.fetch(WEB_API_BASE + '/search-events', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      keepalive: true,
      body: JSON.stringify({
        term: String(term || '').trim().slice(0, 120),
        normalizedTerm: normalizedTerm,
        source: 'homepage',
        resultCount: resultCount || 0,
        clickedArticleUrl: clickedUrl || null
      })
    }).catch(function () {});
  }

  function suggestionLabel(item) {
    return item.label || item.term || item.normalized_term || '';
  }

  function typeLabel(item) {
    if (item.type === 'blog') return 'Article';
    if (item.type === 'external') return 'External';
    return 'Guide';
  }

  function rankQuery(q) {
    return window.IBDPAL_RESOURCES
      .map(function (item) {
        return { item: item, score: scoreItem(item, q) };
      })
      .filter(function (row) {
        return row.score > 0;
      })
      .sort(function (a, b) {
        return b.score - a.score;
      })
      .slice(0, MAX_RESULTS)
      .map(function (row) {
        return row.item;
      });
  }

  function initHomeSearch(root) {
    var input = root.querySelector('.home-search__input');
    var results = root.querySelector('[data-home-results]');
    var status = root.querySelector('[data-home-status]');
    var suggestions = root.querySelector('[data-home-suggestions]');
    var lastTracked = '';
    if (!input || !results || !window.IBDPAL_RESOURCES) return;

    function setExpanded(open) {
      input.setAttribute('aria-expanded', open ? 'true' : 'false');
    }

    function clearResults() {
      results.innerHTML = '';
      results.hidden = true;
      setExpanded(false);
      if (status) {
        status.hidden = true;
        status.textContent = '';
      }
    }

    function relatedBlock(term) {
      return (
        '<div class="home-search__related" data-home-related data-related-term="' + escapeHtml(term) + '">' +
        '<p class="home-search__related-title">Because people searched "' + escapeHtml(term) + '"</p>' +
        '<div class="home-search__related-list">Loading related reads…</div>' +
        '</div>'
      );
    }

    function loadRelated(term) {
      var box = results.querySelector('[data-home-related]');
      if (!box) return;
      var list = box.querySelector('.home-search__related-list');
      window.fetch(WEB_API_BASE + '/search-related?term=' + encodeURIComponent(term) + '&days=90&limit=4')
        .then(function (response) {
          if (!response.ok) throw new Error('related unavailable');
          return response.json();
        })
        .then(function (payload) {
          var rows = (payload && payload.related) || [];
          if (!rows.length) {
            box.hidden = true;
            return;
          }
          list.innerHTML = rows.map(function (row) {
            var title = (row.slug || row.url || '').replace(/^\/blog\//, '').replace(/-/g, ' ');
            return '<a href="' + escapeHtml(row.url) + '">' + escapeHtml(title) + '</a>';
          }).join('');
        })
        .catch(function () {
          box.hidden = true;
        });
    }

    function zeroResultHtml(q, alias) {
      var aliasBtn = alias
        ? '<p class="home-search__didyoumean">Did you mean ' +
          '<button type="button" class="home-search__alias" data-home-alias="' + escapeHtml(alias) + '">' +
          escapeHtml(alias) + '</button>?</p>'
        : '';
      return (
        '<div class="home-search__empty-wrap">' +
        '<p class="home-search__empty">No matches yet for "' + escapeHtml(q) + '".</p>' +
        aliasBtn +
        '<p class="home-search__gap-note">We noted this topic for future education. Try a start question below, or browse <a href="/#guides">Guides &amp; tools</a>.</p>' +
        '<div class="home-search__zero-links">' +
        '<a href="/flare-help">Flare help</a>' +
        '<a href="/ibd-nutrition">Nutrition hub</a>' +
        '<a href="/newly-diagnosed">Newly diagnosed</a>' +
        '<a href="/visit-prep">Visit prep</a>' +
        '</div>' +
        '</div>'
      );
    }

    function renderResults(items, q, opts) {
      opts = opts || {};
      if (!q) {
        clearResults();
        return items.length;
      }
      if (!items.length) {
        results.innerHTML = zeroResultHtml(q, opts.alias || null);
        results.hidden = false;
        setExpanded(true);
        if (status) {
          status.hidden = false;
          status.textContent = '0 matches (saved as a content gap)';
        }
        return 0;
      }
      var html = items.map(function (item) {
        return (
          '<a class="home-search__hit" role="option" href="' + escapeHtml(item.url) + '" data-home-hit>' +
          '<span class="home-search__hit-type">' + escapeHtml(typeLabel(item)) + '</span>' +
          '<span class="home-search__hit-title">' + escapeHtml(item.title) + '</span>' +
          (item.description
            ? '<span class="home-search__hit-desc">' + escapeHtml(String(item.description).slice(0, 110)) + '</span>'
            : '') +
          '</a>'
        );
      }).join('');
      html += relatedBlock(q);
      results.innerHTML = html;
      results.hidden = false;
      setExpanded(true);
      if (status) {
        status.hidden = false;
        status.textContent = items.length + ' match' + (items.length === 1 ? '' : 'es');
      }
      loadRelated(q);
      return items.length;
    }

    function runSearch() {
      var raw = normalizeTerm(input.value);
      if (raw.length < 2) {
        clearResults();
        return 0;
      }
      var alias = suggestAlias(raw);
      var ranked = rankQuery(raw);
      if (!ranked.length && alias && alias !== raw) {
        ranked = rankQuery(alias);
        if (ranked.length) {
          return renderResults(ranked, raw, { alias: alias, usedAlias: true });
        }
      }
      return renderResults(ranked, raw, { alias: alias && alias !== raw ? alias : null });
    }

    var trackSearch = debounce(function () {
      var q = input.value.trim();
      var normalized = normalizeTerm(q);
      if (normalized.length < 2 || normalized === lastTracked) return;
      lastTracked = normalized;
      recordSearchEvent(q, runSearch());
    }, 650);

    function renderSuggestions(items, isFallback) {
      if (!suggestions) return;
      var source = (items && items.length ? items : FALLBACK_SUGGESTIONS).slice(0, 5);
      suggestions.innerHTML =
        '<span>' + (isFallback ? 'Try:' : 'Popular:') + '</span>' +
        source.map(function (item) {
          var label = suggestionLabel(item);
          var term = item.term || item.normalized_term || label;
          return '<button type="button" data-home-suggestion="' + escapeHtml(term) + '">' + escapeHtml(label) + '</button>';
        }).join('');
      suggestions.hidden = false;
    }

    function loadSuggestions() {
      if (!suggestions) return;
      window.fetch(WEB_API_BASE + '/search-suggestions?days=14&limit=5')
        .then(function (response) {
          if (!response.ok) throw new Error('Suggestions unavailable');
          return response.json();
        })
        .then(function (payload) {
          renderSuggestions(payload && payload.suggestions, false);
        })
        .catch(function () {
          renderSuggestions(FALLBACK_SUGGESTIONS, true);
        });
    }

    if (suggestions) {
      suggestions.addEventListener('click', function (event) {
        var button = event.target.closest('[data-home-suggestion]');
        if (!button) return;
        input.value = button.getAttribute('data-home-suggestion') || '';
        var count = runSearch();
        lastTracked = normalizeTerm(input.value);
        recordSearchEvent(input.value, count);
        input.focus();
      });
    }

    results.addEventListener('click', function (event) {
      var aliasBtn = event.target.closest('[data-home-alias]');
      if (aliasBtn) {
        input.value = aliasBtn.getAttribute('data-home-alias') || '';
        var count = runSearch();
        lastTracked = normalizeTerm(input.value);
        recordSearchEvent(input.value, count);
        input.focus();
        return;
      }
      var hit = event.target.closest('[data-home-hit]');
      if (!hit) return;
      var q = input.value.trim();
      if (normalizeTerm(q).length >= 2) {
        recordSearchEvent(q, results.querySelectorAll('[data-home-hit]').length, hit.getAttribute('href'));
      }
    });

    input.addEventListener('input', function () {
      runSearch();
      trackSearch();
    });

    input.addEventListener('keydown', function (event) {
      if (event.key === 'Escape') {
        clearResults();
        input.blur();
      }
    });

    loadSuggestions();
  }

  function boot() {
    document.querySelectorAll('[data-home-search]').forEach(initHomeSearch);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
