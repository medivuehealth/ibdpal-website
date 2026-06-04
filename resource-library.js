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
        var hay = (item.title + ' ' + (item.tags || []).join(' ')).toLowerCase();
        var matchQ = !q || hay.indexOf(q) !== -1;
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
