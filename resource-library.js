/**
 * Filterable resource library (resources tab + /resources page).
 */
(function () {
  'use strict';

  var CATEGORY_LABELS = {
    'getting-started': 'Getting started',
    community: 'Community & support',
    nutrition: 'Nutrition',
    wellness: 'Wellness & lifestyle',
    treatment: 'Treatment basics',
    family: 'Kids & caregivers',
    clinical: 'Clinical tools'
  };

  function escapeHtml(s) {
    return String(s || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
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
    return (
      '<article class="resource-card" data-category="' + escapeHtml(item.category) + '">' +
      '<span class="resource-card__badge">' + escapeHtml(badge) + '</span>' +
      '<h4 class="resource-card__title"><a href="' + escapeHtml(item.url) + '">' + escapeHtml(item.title) + '</a></h4>' +
      '<p class="resource-card__meta">' + escapeHtml(cat) + '</p>' +
      '</article>'
    );
  }

  function initLibrary(root) {
    var list = root.querySelector('.resource-library__grid');
    var filter = root.querySelector('.resource-library__filter');
    var search = root.querySelector('.resource-library__search');
    if (!list || !window.IBDPAL_RESOURCES) return;

    list.innerHTML = window.IBDPAL_RESOURCES.map(renderCard).join('');

    function apply() {
      var cat = filter ? filter.value : '';
      var q = search ? search.value.trim().toLowerCase() : '';
      list.querySelectorAll('.resource-card').forEach(function (card, i) {
        var item = window.IBDPAL_RESOURCES[i];
        var matchCat = !cat || item.category === cat;
        var matchQ = matchesQuery(buildHaystack(item), q);
        card.style.display = matchCat && matchQ ? '' : 'none';
      });
    }

    if (filter) filter.addEventListener('change', apply);
    if (search) search.addEventListener('input', apply);
  }

  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('[data-resource-library]').forEach(initLibrary);
  });
})();
