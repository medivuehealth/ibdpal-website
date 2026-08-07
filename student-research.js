(function () {
  var TOKEN_KEY = 'ibdpal_student_research_session';

  function apiBase() {
    return '/api/web';
  }

  function setStatus(el, message, ok) {
    if (!el) return;
    el.textContent = message || '';
    el.style.color = ok ? '#1f6b3a' : '#8a2f1f';
  }

  function escapeHtml(value) {
    return String(value || '')
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function renderApproved(items) {
    var host = document.getElementById('student-research-approved-feed');
    if (!host) return;
    var filtered = (items || []).filter(function (item) {
      return item && item.id !== 'nhsjs-stem-cell-crohns-2025';
    });
    if (!filtered.length) {
      host.innerHTML = '';
      return;
    }
    host.innerHTML =
      '<h3>Recently approved</h3>' +
      filtered
        .map(function (item) {
          var link = item.externalUrl
            ? '<a href="' +
              escapeHtml(item.externalUrl) +
              '" rel="noopener noreferrer">' +
              escapeHtml(item.title) +
              '</a>'
            : escapeHtml(item.title);
          return (
            '<article class="ibd-news-card">' +
            '<p class="ibd-news-card__tag">Approved student research</p>' +
            '<h3 class="ibd-news-card__title">' +
            link +
            '</h3>' +
            '<p class="research-source-meta"><strong>' +
            escapeHtml(item.authorName || 'Student researcher') +
            '</strong>' +
            (item.school ? ' · ' + escapeHtml(item.school) : '') +
            '</p>' +
            '<p>' +
            escapeHtml(item.abstract) +
            '</p>' +
            '</article>'
          );
        })
        .join('');
  }

  function loadPublished() {
    fetch(apiBase() + '/student-research/published')
      .then(function (res) {
        return res.json();
      })
      .then(function (data) {
        if (data && data.success) renderApproved(data.items);
      })
      .catch(function () {});
  }

  function wireInterestForm() {
    var form = document.getElementById('student-research-interest-form');
    if (!form) return;
    var status = document.getElementById('student-research-interest-status');
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var fd = new FormData(form);
      var payload = {
        fullName: String(fd.get('fullName') || '').trim(),
        email: String(fd.get('email') || '').trim(),
        school: String(fd.get('school') || '').trim(),
        topic: String(fd.get('topic') || '').trim(),
        title: String(fd.get('title') || '').trim(),
        externalUrl: String(fd.get('externalUrl') || '').trim(),
        abstract: String(fd.get('abstract') || '').trim()
      };
      setStatus(status, 'Sending…', true);
      fetch(apiBase() + '/student-research-interest', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      })
        .then(function (res) {
          return res.json().then(function (data) {
            return { ok: res.ok, data: data };
          });
        })
        .then(function (result) {
          if (!result.ok || !result.data.success) {
            setStatus(status, (result.data && result.data.error) || 'Could not send proposal.', false);
            return;
          }
          form.reset();
          setStatus(status, result.data.message || 'Thanks - we received your proposal.', true);
        })
        .catch(function () {
          setStatus(status, 'Network error. Email info@ibdpal.org instead.', false);
        });
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    wireInterestForm();
    loadPublished();
  });

  window.IBDPAL_STUDENT_RESEARCH = {
    getToken: function () {
      try {
        return localStorage.getItem(TOKEN_KEY) || '';
      } catch (e) {
        return '';
      }
    },
    setToken: function (token) {
      try {
        if (token) localStorage.setItem(TOKEN_KEY, token);
        else localStorage.removeItem(TOKEN_KEY);
      } catch (e) {}
    }
  };
})();
