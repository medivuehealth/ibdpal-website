/**
 * Category filter pills for homepage Articles tab.
 */
(function () {
  'use strict';

  function normalizeMeta(text) {
    return String(text || '').toLowerCase();
  }

  function matchesFilter(meta, filter) {
    if (!filter) return true;
    var m = normalizeMeta(meta);
    if (filter === 'teen') {
      return m.indexOf('teen') !== -1 || m.indexOf('school') !== -1 || m.indexOf('college') !== -1;
    }
    if (filter === 'flare') {
      return m.indexOf('flare') !== -1 || m.indexOf('flares') !== -1;
    }
    if (filter === 'nutrition') {
      return m.indexOf('nutrition') !== -1 || m.indexOf('diet') !== -1;
    }
    if (filter === 'treatment') {
      return m.indexOf('treatment') !== -1 || m.indexOf('clinical') !== -1;
    }
    if (filter === 'wellness') {
      return m.indexOf('wellness') !== -1 || m.indexOf('lifestyle') !== -1 || m.indexOf('health') !== -1;
    }
    if (filter === 'family') {
      return m.indexOf('family') !== -1;
    }
    return m.indexOf(filter) !== -1;
  }

  function init() {
    var toolbar = document.querySelector('.blog-index-toolbar');
    if (!toolbar) return;

    var grid =
      toolbar.nextElementSibling && toolbar.nextElementSibling.classList.contains('blog-index-grid')
        ? toolbar.nextElementSibling
        : document.querySelector('#articles .blog-index-grid, #blogs .blog-index-grid');
    if (!grid) return;

    var cards = grid.querySelectorAll('.blog-card');

    toolbar.addEventListener('click', function (e) {
      var btn = e.target.closest('[data-blog-filter]');
      if (!btn) return;
      var filter = btn.getAttribute('data-blog-filter') || '';
      toolbar.querySelectorAll('.blog-pill').forEach(function (pill) {
        pill.classList.toggle('is-active', pill === btn);
      });
      cards.forEach(function (card) {
        var meta = card.querySelector('.blog-card-chip, .blog-card-meta');
        var show = matchesFilter(meta ? meta.textContent : '', filter);
        card.style.display = show ? '' : 'none';
      });
    });
  }

  document.addEventListener('DOMContentLoaded', init);
})();
