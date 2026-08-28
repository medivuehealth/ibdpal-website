(function () {
  'use strict';

  var adminToken = '';
  var form = document.getElementById('rq-admin-form');
  var statusEl = document.getElementById('rq-admin-status');
  var listSection = document.getElementById('rq-list-section');
  var listEl = document.getElementById('rq-admin-list');
  var filterNew = document.getElementById('rq-filter-new');
  var filterAll = document.getElementById('rq-filter-all');

  function apiBase() {
    return (window.IBDPAL_SITE_CONFIG && window.IBDPAL_SITE_CONFIG.webApiBase) || '/api/web';
  }

  function status(msg, ok) {
    if (!statusEl) return;
    statusEl.textContent = msg || '';
    statusEl.style.color = ok ? '#1f6b3a' : '#8a2f1f';
  }

  function headers() {
    return { 'Content-Type': 'application/json', 'x-admin-token': adminToken };
  }

  function escapeHtml(v) {
    return String(v || '')
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;');
  }

  function renderCard(q) {
    var published =
      q.publishedAt && q.slug
        ? '<p><a href="/ask/' + encodeURIComponent(q.slug) + '" target="_blank" rel="noopener">View public answer</a></p>'
        : '';
    return (
      '<article class="admin-research-card" data-id="' +
      q.id +
      '">' +
      '<p><strong>#' +
      q.id +
      '</strong> · ' +
      escapeHtml(q.status) +
      ' · ' +
      escapeHtml(q.createdAt || '') +
      '</p>' +
      '<p><em>' +
      escapeHtml(q.question) +
      '</em></p>' +
      (q.email ? '<p>Email: ' + escapeHtml(q.email) + '</p>' : '') +
      published +
      '<label>Title <input class="rq-title" value="' +
      escapeHtml(q.title || '') +
      '" maxlength="240"></label>' +
      '<label>Slug <input class="rq-slug" value="' +
      escapeHtml(q.slug || '') +
      '" maxlength="80" placeholder="auto-from-title"></label>' +
      '<label>Answer <textarea class="rq-answer" rows="8" maxlength="12000">' +
      escapeHtml(q.answer || '') +
      '</textarea></label>' +
      '<div class="admin-research-card__actions">' +
      '<button type="button" class="rq-publish">Publish / update answer</button>' +
      '<button type="button" class="rq-unpublish">Unpublish</button>' +
      '</div>' +
      '</article>'
    );
  }

  function loadList(statusFilter) {
    var url = apiBase() + '/reader-questions?action=admin-list&limit=100';
    if (statusFilter) url += '&status=' + encodeURIComponent(statusFilter);

    fetch(url, { headers: { 'x-admin-token': adminToken } })
      .then(function (res) {
        return res.json();
      })
      .then(function (data) {
        if (!data.success) {
          status(data.error || 'Load failed.', false);
          return;
        }
        listSection.hidden = false;
        listEl.innerHTML = data.questions.length
          ? data.questions.map(renderCard).join('')
          : '<p>No questions in this filter.</p>';
        status('Loaded ' + data.questions.length + ' question(s).', true);
        bindCards();
      })
      .catch(function () {
        status('Network error.', false);
      });
  }

  function bindCards() {
    listEl.querySelectorAll('.admin-research-card').forEach(function (card) {
      var id = parseInt(card.getAttribute('data-id'), 10);
      card.querySelector('.rq-publish').addEventListener('click', function () {
        var title = card.querySelector('.rq-title').value.trim();
        var slug = card.querySelector('.rq-slug').value.trim();
        var answer = card.querySelector('.rq-answer').value.trim();
        fetch(apiBase() + '/reader-questions?action=admin-publish', {
          method: 'POST',
          headers: headers(),
          body: JSON.stringify({ id: id, title: title, slug: slug, answer: answer, publish: true })
        })
          .then(function (res) {
            return res.json();
          })
          .then(function (data) {
            status(data.message || data.error || 'Done.', !!data.success);
            if (data.success) loadList('');
          });
      });
      card.querySelector('.rq-unpublish').addEventListener('click', function () {
        fetch(apiBase() + '/reader-questions?action=admin-publish', {
          method: 'POST',
          headers: headers(),
          body: JSON.stringify({ id: id, publish: false })
        })
          .then(function (res) {
            return res.json();
          })
          .then(function (data) {
            status(data.message || data.error || 'Done.', !!data.success);
            if (data.success) loadList('');
          });
      });
    });
  }

  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      adminToken = form.adminToken.value.trim();
      if (!adminToken) return;
      loadList('new');
    });
  }
  if (filterNew) filterNew.addEventListener('click', function () {
    if (adminToken) loadList('new');
  });
  if (filterAll) filterAll.addEventListener('click', function () {
    if (adminToken) loadList('');
  });
})();
