/**
 * Filterable resource library (resources tab + /resources page).
 */
(function () {
  'use strict';

  var WEB_API_BASE = (window.IBDPAL_SITE_CONFIG && window.IBDPAL_SITE_CONFIG.webApiBase) ||
    'https://ibdpal-server-production.up.railway.app/api/web';

  var CATEGORY_LABELS = {
    'getting-started': 'Getting started',
    community: 'Community & support',
    nutrition: 'Nutrition',
    wellness: 'Wellness & lifestyle',
    treatment: 'Treatment basics',
    family: 'Kids & caregivers',
    clinical: 'Clinical tools'
  };

  var PILL_CATEGORIES = [
    '',
    'getting-started',
    'nutrition',
    'treatment',
    'wellness',
    'community',
    'family',
    'clinical'
  ];
  var FALLBACK_SUGGESTIONS = [
    { term: 'fatigue', label: 'Fatigue' },
    { term: 'flare', label: 'Flare' },
    { term: 'low residue', label: 'Low residue' },
    { term: 'biologics', label: 'Biologics' },
    { term: 'school', label: 'School' }
  ];

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

  function normalizeTerm(value) {
    return String(value || '').toLowerCase().replace(/[^\w\s'-]/g, ' ').replace(/\s+/g, ' ').trim();
  }

  function recordSearchEvent(term, resultCount) {
    var normalizedTerm = normalizeTerm(term);
    if (normalizedTerm.length < 2) return;

    window.fetch(WEB_API_BASE + '/search-events', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      keepalive: true,
      body: JSON.stringify({
        term: String(term || '').trim().slice(0, 120),
        normalizedTerm: normalizedTerm,
        source: 'patient_library',
        resultCount: resultCount || 0
      })
    }).catch(function () {
      // Search analytics should never interrupt the resource library.
    });
  }

  function suggestionLabel(item) {
    return item.label || item.term || item.normalized_term || '';
  }

  function matchesQuery(hay, q) {
    if (!q) return true;
    if (hay.indexOf(q) !== -1) return true;
    var tokens = q.split(/\s+/).filter(function (t) {
      return t.length > 0;
    });
    if (!tokens.length) return true;
    var words = hay.split(/[^a-z0-9]+/).filter(Boolean);
    return tokens.every(function (tok) {
      if (hay.indexOf(tok) !== -1) return true;
      for (var i = 0; i < words.length; i++) {
        var w = words[i];
        if (w.indexOf(tok) === 0 || tok.indexOf(w) === 0) return true;
      }
      return false;
    });
  }

  function renderCard(item) {
    var cat = CATEGORY_LABELS[item.category] || item.category;
    var badge = item.type === 'external' ? 'External' : item.type === 'blog' ? 'Article' : 'On ibdpal.org';
    var desc = item.description ? '<p class="resource-card__desc">' + escapeHtml(item.description.slice(0, 100)) + '</p>' : '';
    return (
      '<article class="resource-card" data-category="' + escapeHtml(item.category) + '">' +
      '<span class="resource-card__badge resource-card__badge--' + escapeHtml(item.type) + '">' + escapeHtml(badge) + '</span>' +
      '<h4 class="resource-card__title"><a href="' + escapeHtml(item.url) + '">' + escapeHtml(item.title) + '</a></h4>' +
      '<p class="resource-card__meta">' + escapeHtml(cat) + '</p>' +
      desc +
      '</article>'
    );
  }

  function syncPills(root, cat) {
    root.querySelectorAll('.resource-pill').forEach(function (pill) {
      var active = (pill.getAttribute('data-category') || '') === cat;
      pill.classList.toggle('is-active', active);
    });
  }

  function initLibrary(root) {
    var list = root.querySelector('.resource-library__grid');
    var filter = root.querySelector('.resource-library__filter');
    var search = root.querySelector('.resource-library__search');
    var suggestions = root.querySelector('[data-resource-suggestions]');
    var empty = root.querySelector('.resource-library__empty');
    var lastTrackedSearch = '';
    if (!list || !window.IBDPAL_RESOURCES) return;

    list.innerHTML = window.IBDPAL_RESOURCES.map(renderCard).join('');

    function apply() {
      var cat = filter ? filter.value : '';
      var q = search ? search.value.trim().toLowerCase() : '';
      var visible = 0;
      list.querySelectorAll('.resource-card').forEach(function (card, i) {
        var item = window.IBDPAL_RESOURCES[i];
        var matchCat = !cat || item.category === cat;
        var matchQ = matchesQuery(buildHaystack(item), q);
        var show = matchCat && matchQ;
        card.style.display = show ? '' : 'none';
        if (show) visible += 1;
      });
      if (empty) {
        empty.hidden = visible > 0;
      }
      list.hidden = visible === 0 && !!empty;
      return visible;
    }

    var trackSearch = debounce(function () {
      if (!search) return;
      var q = search.value.trim();
      var normalized = normalizeTerm(q);
      if (normalized.length < 2 || normalized === lastTrackedSearch) return;
      lastTrackedSearch = normalized;
      recordSearchEvent(q, apply());
    }, 700);

    function renderSuggestions(items, isFallback) {
      if (!suggestions) return;
      var source = (items && items.length ? items : FALLBACK_SUGGESTIONS).slice(0, 5);
      suggestions.innerHTML =
        '<span>' + (isFallback ? 'Try:' : 'Popular searches:') + '</span>' +
        source.map(function (item) {
          var label = suggestionLabel(item);
          var term = item.term || item.normalized_term || label;
          return '<button type="button" data-resource-suggestion="' + escapeHtml(term) + '">' + escapeHtml(label) + '</button>';
        }).join('');
      suggestions.hidden = false;
    }

    function loadSuggestions() {
      if (!suggestions) return;
      window.fetch(WEB_API_BASE + '/search-suggestions?days=14&limit=5&source=patient_library')
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

    root.querySelectorAll('.resource-pill').forEach(function (pill) {
      pill.addEventListener('click', function () {
        var cat = pill.getAttribute('data-category') || '';
        if (filter) filter.value = cat;
        syncPills(root, cat);
        apply();
      });
    });

    if (suggestions) {
      suggestions.addEventListener('click', function (event) {
        var button = event.target.closest('[data-resource-suggestion]');
        if (!button || !search) return;
        search.value = button.getAttribute('data-resource-suggestion') || '';
        var visible = apply();
        var normalized = normalizeTerm(search.value);
        lastTrackedSearch = normalized;
        recordSearchEvent(search.value, visible);
        search.focus();
      });
    }

    if (filter) filter.addEventListener('change', function () {
      syncPills(root, filter.value);
      apply();
    });
    if (search) search.addEventListener('input', function () {
      apply();
      trackSearch();
    });
    loadSuggestions();
    apply();
  }

  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('[data-resource-library]').forEach(initLibrary);
  });
})();
