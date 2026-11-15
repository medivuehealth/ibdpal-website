(function () {
  'use strict';

  var adminToken = '';
  var form = document.getElementById('pi-admin-form');
  var statusEl = document.getElementById('pi-admin-status');
  var listSection = document.getElementById('pi-list-section');
  var listEl = document.getElementById('pi-admin-list');
  var filterNew = document.getElementById('pi-filter-new');
  var filterAll = document.getElementById('pi-filter-all');

  function apiBase() {
    return (window.IBDPAL_SITE_CONFIG && window.IBDPAL_SITE_CONFIG.webApiBase) || '/api/web';
  }

  function status(msg, ok) {
    if (!statusEl) return;
    statusEl.textContent = msg || '';
    statusEl.style.color = ok ? '#1f6b3a' : '#8a2f1f';
  }

  function escapeHtml(v) {
    return String(v || '')
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function renderCard(item) {
    return (
      '<article class="admin-research-card" data-id="' +
      item.id +
      '">' +
      '<p><strong>#' +
      item.id +
      '</strong> · ' +
      escapeHtml(item.status) +
      ' · ' +
      escapeHtml(item.interestType) +
      ' · ' +
      escapeHtml(item.createdAt || '') +
      '</p>' +
      '<p><strong>' +
      escapeHtml(item.organizationName) +
      '</strong></p>' +
      '<p>' +
      escapeHtml(item.contactName) +
      ' · <a href="mailto:' +
      escapeHtml(item.contactEmail) +
      '">' +
      escapeHtml(item.contactEmail) +
      '</a></p>' +
      (item.programUrl
        ? '<p><a href="' +
          escapeHtml(item.programUrl) +
          '" target="_blank" rel="noopener noreferrer">' +
          escapeHtml(item.programUrl) +
          '</a></p>'
        : '') +
      '<p><em>' +
      escapeHtml(item.message) +
      '</em></p>' +
      '<label>Status <select class="pi-status">' +
      ['new', 'reviewed', 'contacted', 'closed', 'spam']
        .map(function (s) {
          return (
            '<option value="' +
            s +
            '"' +
            (s === item.status ? ' selected' : '') +
            '>' +
            s +
            '</option>'
          );
        })
        .join('') +
      '</select></label>' +
      '<label>Notes <textarea class="pi-notes" rows="3" maxlength="4000">' +
      escapeHtml(item.adminNotes || '') +
      '</textarea></label>' +
      '<div class="admin-research-card__actions">' +
      '<button type="button" class="pi-save">Save status</button>' +
      '</div>' +
      '</article>'
    );
  }

  function loadList(statusFilter) {
    var url = apiBase() + '/partner-inquiries?action=admin-list&limit=100';
    if (statusFilter) url += '&status=' + encodeURIComponent(statusFilter);

    fetch(url, { headers: { 'x-admin-token': adminToken } })
      .then(function (res) {
        return res.json();
      })
      .then(function (data) {
        if (!data.success) {
          status(data.error || 'Failed to load', false);
          return;
        }
        listSection.hidden = false;
        listEl.innerHTML = (data.items || []).map(renderCard).join('') || '<p>No inquiries yet.</p>';
        status('Loaded ' + (data.items || []).length + ' inquiries.', true);
      })
      .catch(function () {
        status('Network error loading inquiries.', false);
      });
  }

  if (form) {
    form.addEventListener('submit', function (event) {
      event.preventDefault();
      adminToken = (form.adminToken && form.adminToken.value) || '';
      if (!adminToken) {
        status('Enter admin token.', false);
        return;
      }
      loadList('new');
    });
  }

  if (filterNew) {
    filterNew.addEventListener('click', function () {
      loadList('new');
    });
  }
  if (filterAll) {
    filterAll.addEventListener('click', function () {
      loadList('');
    });
  }

  if (listEl) {
    listEl.addEventListener('click', function (event) {
      var btn = event.target.closest('.pi-save');
      if (!btn) return;
      var card = btn.closest('.admin-research-card');
      if (!card) return;
      var id = card.getAttribute('data-id');
      var statusSelect = card.querySelector('.pi-status');
      var notes = card.querySelector('.pi-notes');
      fetch(apiBase() + '/partner-inquiries?action=admin-update', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'x-admin-token': adminToken
        },
        body: JSON.stringify({
          id: Number(id),
          status: statusSelect ? statusSelect.value : 'reviewed',
          adminNotes: notes ? notes.value : ''
        })
      })
        .then(function (res) {
          return res.json();
        })
        .then(function (data) {
          if (!data.success) {
            status(data.error || 'Update failed', false);
            return;
          }
          status('Updated #' + id + ' → ' + data.status, true);
        })
        .catch(function () {
          status('Network error updating inquiry.', false);
        });
    });
  }
})();
