/**
 * Ask IBDPal: submit questions, list published answers, load answer detail pages.
 */
(function () {
  'use strict';

  var page = document.body.getAttribute('data-ask-page') || 'index';

  function apiBase() {
    if (window.IBDPAL_SITE_CONFIG && window.IBDPAL_SITE_CONFIG.webApiBase) {
      return window.IBDPAL_SITE_CONFIG.webApiBase;
    }
    return '/api/web';
  }

  function escapeHtml(value) {
    return String(value || '')
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function formatDate(iso) {
    if (!iso) return '';
    try {
      return new Date(iso).toLocaleDateString(undefined, {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
      });
    } catch (e) {
      return '';
    }
  }

  function renderAnswerHtml(text) {
    var parts = String(text || '')
      .split(/\n\s*\n/)
      .map(function (p) {
        return p.trim();
      })
      .filter(Boolean);
    if (!parts.length) return '';
    return parts
      .map(function (p) {
        if (/^Related education:/i.test(p)) {
          return '<p class="reader-qa-related"><em>' + escapeHtml(p) + '</em></p>';
        }
        return '<p>' + escapeHtml(p) + '</p>';
      })
      .join('\n');
  }

  function slugFromPath() {
    var parts = window.location.pathname.replace(/\/+$/, '').split('/');
    if (parts.length >= 2 && parts[parts.length - 2] === 'ask') {
      return decodeURIComponent(parts[parts.length - 1] || '');
    }
    return '';
  }

  function initForm() {
    var form = document.getElementById('ask-question-form');
    if (!form) return;

    var questionEl = document.getElementById('ask-question-text');
    var emailEl = document.getElementById('ask-question-email');
    var nameEl = document.getElementById('ask-question-name');
    var statusEl = document.getElementById('ask-question-status');
    var submitBtn = document.getElementById('ask-question-submit');
    var honeypot = document.getElementById('ask-question-website');
    var minLen = 15;

    function readMeta(name) {
      var el = document.querySelector('meta[name="' + name + '"]');
      return el ? el.getAttribute('content') || '' : '';
    }

    function setStatus(message, type) {
      if (!statusEl) return;
      statusEl.hidden = !message;
      statusEl.textContent = message || '';
      statusEl.className = 'ask-question__status' + (type ? ' ask-question__status--' + type : '');
    }

    function queryParam(name) {
      try {
        return new URLSearchParams(window.location.search).get(name) || '';
      } catch (e) {
        return '';
      }
    }

    var q = queryParam('q') || queryParam('search');
    if (q && questionEl && !questionEl.value.trim()) {
      questionEl.value = q.slice(0, 2000);
    }
    var source = queryParam('from');
    if (source) form.dataset.source = source.slice(0, 40);

    if (window.location.hash === '#ask-form' && questionEl) {
      questionEl.focus();
    }

    form.addEventListener('submit', function (event) {
      event.preventDefault();
      if (!questionEl) return;

      var question = questionEl.value.trim();
      if (question.length < minLen) {
        setStatus('Please write at least ' + minLen + ' characters so we understand your question.', 'error');
        questionEl.focus();
        return;
      }

      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.setAttribute('aria-busy', 'true');
      }
      setStatus('Sending…', 'pending');

      fetch(apiBase() + '/reader-questions', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          question: question,
          email: emailEl ? emailEl.value.trim() : '',
          displayName: nameEl ? nameEl.value.trim() : '',
          source: form.dataset.source || readMeta('ask-source') || 'ask_page',
          pageUrl: document.referrer || window.location.href,
          searchTerm: q || '',
          website: honeypot ? honeypot.value : ''
        })
      })
        .then(function (res) {
          return res.json().then(function (body) {
            return { ok: res.ok, status: res.status, body: body };
          });
        })
        .then(function (result) {
          if (result.ok && result.body && result.body.success) {
            form.reset();
            setStatus(result.body.message || 'Thanks. We received your question.', 'success');
            return;
          }
          var err =
            (result.body && result.body.error) ||
            (result.status === 429
              ? 'Too many submissions. Please wait and try again.'
              : 'Something went wrong. Try again or email info@ibdpal.org.');
          setStatus(err, 'error');
        })
        .catch(function () {
          setStatus('Network error. Check your connection or email info@ibdpal.org.', 'error');
        })
        .finally(function () {
          if (submitBtn) {
            submitBtn.disabled = false;
            submitBtn.removeAttribute('aria-busy');
          }
        });
    });
  }

  function renderListCard(item) {
    var date = formatDate(item.publishedAt);
    return (
      '<a href="/ask/' +
      encodeURIComponent(item.slug) +
      '" class="reader-qa-item">' +
      '<h3 class="reader-qa-item__title">' +
      escapeHtml(item.title) +
      '</h3>' +
      '<p class="reader-qa-item__meta">' +
      (date ? 'Answered ' + escapeHtml(date) : 'Answered') +
      '</p>' +
      '<p class="reader-qa-item__excerpt">' +
      escapeHtml(item.excerpt || '') +
      '</p>' +
      '</a>'
    );
  }

  function initList() {
    var list = document.getElementById('reader-qa-list');
    if (!list) return;

    fetch(apiBase() + '/reader-questions?action=published&limit=50')
      .then(function (res) {
        return res.json();
      })
      .then(function (data) {
        if (!data.success || !data.items || !data.items.length) {
          list.innerHTML =
            '<p class="reader-qa-list__empty">No published answers yet. Be the first to <a href="#ask-form">ask a question</a>.</p>';
          return;
        }
        list.innerHTML = data.items.map(renderListCard).join('');
      })
      .catch(function () {
        list.innerHTML =
          '<p class="reader-qa-list__empty">Could not load answered questions. <a href="/ask">Refresh</a> or try again later.</p>';
      });
  }

  function initDetail() {
    var slug = slugFromPath();
    var titleEl = document.getElementById('reader-qa-title');
    var dateEl = document.getElementById('reader-qa-date');
    var questionEl = document.getElementById('reader-qa-question');
    var answerEl = document.getElementById('reader-qa-answer');
    var errorEl = document.getElementById('reader-qa-error');

    if (!slug) {
      if (errorEl) {
        errorEl.hidden = false;
        errorEl.textContent = 'Missing question link.';
      }
      return;
    }

    fetch(apiBase() + '/reader-questions?action=by-slug&slug=' + encodeURIComponent(slug))
      .then(function (res) {
        return res.json().then(function (body) {
          return { ok: res.ok, body: body };
        });
      })
      .then(function (result) {
        if (!result.ok || !result.body.item) {
          if (titleEl) titleEl.textContent = 'Answer not found';
          if (errorEl) {
            errorEl.hidden = false;
            errorEl.textContent = 'This answer is not available. Browse all questions on Ask IBDPal.';
          }
          return;
        }
        var item = result.body.item;
        if (titleEl) titleEl.textContent = item.title;
        if (dateEl) {
          dateEl.innerHTML =
            'Ask IBDPal &middot; Reader Q&amp;A' +
            (item.publishedAt ? ' &middot; Answered ' + escapeHtml(formatDate(item.publishedAt)) : '');
        }
        if (questionEl) questionEl.textContent = item.question;
        if (answerEl) answerEl.innerHTML = renderAnswerHtml(item.answer);

        document.title = item.title + ' | Ask IBDPal';
        var desc = (item.excerpt || item.answer || '').slice(0, 155);
        var meta = document.querySelector('meta[name="description"]');
        if (meta && desc) meta.setAttribute('content', desc);
        var canonical = document.querySelector('link[rel="canonical"]');
        if (canonical) canonical.setAttribute('href', 'https://www.ibdpal.org/ask/' + item.slug);
      })
      .catch(function () {
        if (titleEl) titleEl.textContent = 'Could not load answer';
        if (errorEl) {
          errorEl.hidden = false;
          errorEl.textContent = 'Network error. Try again later.';
        }
      });
  }

  if (page === 'detail') {
    initDetail();
  } else {
    initForm();
    initList();
  }
})();
