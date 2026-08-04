/**
 * Homepage topic search: fuzzy autocomplete, aliases, zero-result capture, related clicks.
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
    if (window.IBDPAL_SEARCH_FUZZY && window.IBDPAL_SEARCH_FUZZY.normalize) {
      return window.IBDPAL_SEARCH_FUZZY.normalize(value);
    }
    return String(value || '').toLowerCase().replace(/[^\w\s'-]/g, ' ').replace(/\s+/g, ' ').trim();
  }

  /** Canonical keyword for analytics (typos → biologics / enteral / etc.). */
  function canonicalTerm(term) {
    var n = normalizeTerm(term);
    if (!n) return n;
    if (window.IBDPAL_SEARCH_FUZZY && window.IBDPAL_SEARCH_FUZZY.resolveAlias) {
      var viaFuzzy = window.IBDPAL_SEARCH_FUZZY.resolveAlias(n);
      if (viaFuzzy && viaFuzzy !== n) return viaFuzzy;
    }
    if (window.IBDPAL_ENGAGEMENT && window.IBDPAL_ENGAGEMENT.suggestAlias) {
      var viaEng = window.IBDPAL_ENGAGEMENT.suggestAlias(n);
      if (viaEng && normalizeTerm(viaEng) !== n) return normalizeTerm(viaEng);
    }
    return n;
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
    // Exact keyword / tag hits (e.g. "enteral") rank above loose contains.
    var keywords = item.keywords || [];
    var tags = item.tags || [];
    for (var i = 0; i < keywords.length; i++) {
      if (normalizeTerm(keywords[i]) === q) {
        score += 14;
        break;
      }
    }
    for (var j = 0; j < tags.length; j++) {
      if (normalizeTerm(tags[j]) === q) {
        score += 10;
        break;
      }
    }
    var tokens = q.split(/\s+/).filter(Boolean);
    tokens.forEach(function (tok) {
      if (title.indexOf(tok) !== -1) score += 4;
      else if (hay.indexOf(tok) !== -1) score += 2;
    });
    return score;
  }

  function suggestCorrection(term) {
    if (window.IBDPAL_ENGAGEMENT && window.IBDPAL_ENGAGEMENT.suggestAlias) {
      var alias = window.IBDPAL_ENGAGEMENT.suggestAlias(term);
      if (alias && alias !== term) return alias;
    }
    if (window.IBDPAL_SEARCH_FUZZY && window.IBDPAL_SEARCH_FUZZY.bestCorrection) {
      return window.IBDPAL_SEARCH_FUZZY.bestCorrection(term);
    }
    return null;
  }

  function queryVariants(term) {
    if (window.IBDPAL_SEARCH_FUZZY && window.IBDPAL_SEARCH_FUZZY.expandQuery) {
      return window.IBDPAL_SEARCH_FUZZY.expandQuery(term);
    }
    var corr = suggestCorrection(term);
    return corr && corr !== term ? [term, corr] : [term];
  }

  function recordSearchEvent(term, resultCount, clickedUrl) {
    var normalizedTerm = canonicalTerm(term);
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
    var variants = queryVariants(q);
    var best = {};
    window.IBDPAL_RESOURCES.forEach(function (item) {
      var score = 0;
      variants.forEach(function (variant, index) {
        var part = scoreItem(item, variant);
        if (!part) return;
        // Exact typed query weighs more than fuzzy expansions.
        score = Math.max(score, part + (index === 0 ? 0 : Math.max(0, 4 - index)));
      });
      if (score > 0) best[item.url] = { item: item, score: score };
    });
    return Object.keys(best)
      .map(function (url) { return best[url]; })
      .sort(function (a, b) { return b.score - a.score; })
      .slice(0, MAX_RESULTS)
      .map(function (row) { return row.item; });
  }

  function initHomeSearch(root) {
    var input = root.querySelector('.home-search__input');
    var results = root.querySelector('[data-home-results]');
    var status = root.querySelector('[data-home-status]');
    var suggestions = root.querySelector('[data-home-suggestions]');
    var autocomplete = root.querySelector('[data-home-autocomplete]');
    var lastTracked = '';
    var activeIndex = -1;
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

    function clearAutocomplete() {
      if (!autocomplete) return;
      autocomplete.innerHTML = '';
      autocomplete.hidden = true;
      activeIndex = -1;
    }

    function renderAutocomplete(q) {
      if (!autocomplete || !window.IBDPAL_SEARCH_FUZZY) {
        clearAutocomplete();
        return;
      }
      var items = window.IBDPAL_SEARCH_FUZZY.completions(q, 6);
      if (!items.length || normalizeTerm(q).length < 2) {
        clearAutocomplete();
        return;
      }
      activeIndex = -1;
      autocomplete.innerHTML =
        '<p class="home-search__ac-label">Suggestions</p>' +
        items.map(function (item, index) {
          var hint = item.reason === 'fuzzy' || item.reason === 'alias'
            ? '<span class="home-search__ac-hint">Did you mean</span>'
            : '<span class="home-search__ac-hint">Complete</span>';
          return (
            '<button type="button" class="home-search__ac-item" role="option" data-home-ac="' +
            escapeHtml(item.term) + '" data-ac-index="' + index + '">' +
            hint +
            '<strong>' + escapeHtml(item.label) + '</strong>' +
            '</button>'
          );
        }).join('');
      autocomplete.hidden = false;
    }

    function applyTerm(term) {
      input.value = term;
      clearAutocomplete();
      var count = runSearch();
      lastTracked = normalizeTerm(term);
      recordSearchEvent(term, count);
      input.focus();
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

    function zeroResultHtml(q, correction) {
      var aliasBtn = correction
        ? '<p class="home-search__didyoumean">Did you mean ' +
          '<button type="button" class="home-search__alias" data-home-alias="' + escapeHtml(correction) + '">' +
          escapeHtml(correction) + '</button>?</p>'
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
      var correctedNote = opts.usedCorrection
        ? '<p class="home-search__corrected">Showing results for <strong>' +
          escapeHtml(opts.usedCorrection) +
          '</strong> (from "' + escapeHtml(q) + '")</p>'
        : '';
      var html = correctedNote + items.map(function (item) {
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
      html += relatedBlock(opts.usedCorrection || q);
      results.innerHTML = html;
      results.hidden = false;
      setExpanded(true);
      if (status) {
        status.hidden = false;
        status.textContent = items.length + ' match' + (items.length === 1 ? '' : 'es');
      }
      loadRelated(opts.usedCorrection || q);
      return items.length;
    }

    function runSearch() {
      var raw = normalizeTerm(input.value);
      if (raw.length < 2) {
        clearResults();
        clearAutocomplete();
        return 0;
      }
      renderAutocomplete(raw);
      var correction = suggestCorrection(raw);
      var ranked = rankQuery(raw);
      if (ranked.length && correction && correction !== raw) {
        // Fuzzy expansion already found content; note the correction used.
        var direct = rankQueryExact(raw);
        if (!direct.length) {
          return renderResults(ranked, raw, { alias: correction, usedCorrection: correction });
        }
      }
      if (!ranked.length && correction && correction !== raw) {
        ranked = rankQueryExact(correction);
        if (ranked.length) {
          return renderResults(ranked, raw, { alias: correction, usedCorrection: correction });
        }
      }
      return renderResults(ranked, raw, {
        alias: correction && correction !== raw ? correction : null
      });
    }

    function rankQueryExact(q) {
      return window.IBDPAL_RESOURCES
        .map(function (item) {
          return { item: item, score: scoreItem(item, q) };
        })
        .filter(function (row) { return row.score > 0; })
        .sort(function (a, b) { return b.score - a.score; })
        .slice(0, MAX_RESULTS)
        .map(function (row) { return row.item; });
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
        applyTerm(button.getAttribute('data-home-suggestion') || '');
      });
    }

    if (autocomplete) {
      autocomplete.addEventListener('click', function (event) {
        var button = event.target.closest('[data-home-ac]');
        if (!button) return;
        applyTerm(button.getAttribute('data-home-ac') || '');
      });
    }

    results.addEventListener('click', function (event) {
      var aliasBtn = event.target.closest('[data-home-alias]');
      if (aliasBtn) {
        applyTerm(aliasBtn.getAttribute('data-home-alias') || '');
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
      var items = autocomplete && !autocomplete.hidden
        ? autocomplete.querySelectorAll('[data-home-ac]')
        : [];
      if (event.key === 'ArrowDown' && items.length) {
        event.preventDefault();
        activeIndex = Math.min(items.length - 1, activeIndex + 1);
        items.forEach(function (el, i) {
          el.classList.toggle('is-active', i === activeIndex);
        });
        return;
      }
      if (event.key === 'ArrowUp' && items.length) {
        event.preventDefault();
        activeIndex = Math.max(0, activeIndex - 1);
        items.forEach(function (el, i) {
          el.classList.toggle('is-active', i === activeIndex);
        });
        return;
      }
      if (event.key === 'Enter' && activeIndex >= 0 && items[activeIndex]) {
        event.preventDefault();
        applyTerm(items[activeIndex].getAttribute('data-home-ac') || '');
        return;
      }
      if (event.key === 'Tab' && items.length && !event.shiftKey) {
        // Accept top suggestion quickly.
        event.preventDefault();
        applyTerm(items[0].getAttribute('data-home-ac') || '');
        return;
      }
      if (event.key === 'Escape') {
        clearAutocomplete();
        clearResults();
        input.blur();
      }
    });

    loadSuggestions();
  }

  function boot() {
    if (window.IBDPAL_SEARCH_FUZZY && window.IBDPAL_SEARCH_FUZZY.invalidate) {
      window.IBDPAL_SEARCH_FUZZY.invalidate();
    }
    document.querySelectorAll('[data-home-search]').forEach(initHomeSearch);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
