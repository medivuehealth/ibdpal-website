/**
 * Ask a question form: saves reader questions via /api/web/reader-questions.
 * Profanity is rejected server-side; client validates length and honeypot only.
 */
(function () {
  'use strict';

  var form = document.getElementById('ask-question-form');
  if (!form) return;

  var questionEl = document.getElementById('ask-question-text');
  var emailEl = document.getElementById('ask-question-email');
  var nameEl = document.getElementById('ask-question-name');
  var statusEl = document.getElementById('ask-question-status');
  var submitBtn = document.getElementById('ask-question-submit');
  var honeypot = document.getElementById('ask-question-website');
  var minLen = 15;

  function apiBase() {
    if (window.IBDPAL_SITE_CONFIG && window.IBDPAL_SITE_CONFIG.webApiBase) {
      return window.IBDPAL_SITE_CONFIG.webApiBase;
    }
    return '/api/web';
  }

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

  function prefillFromUrl() {
    var q = queryParam('q') || queryParam('search');
    if (q && questionEl && !questionEl.value.trim()) {
      questionEl.value = q.slice(0, 2000);
    }
    var source = queryParam('from');
    if (source) form.dataset.source = source.slice(0, 40);
  }

  prefillFromUrl();

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

    var payload = {
      question: question,
      email: emailEl ? emailEl.value.trim() : '',
      displayName: nameEl ? nameEl.value.trim() : '',
      source: form.dataset.source || readMeta('ask-source') || 'ask_page',
      pageUrl: document.referrer || window.location.href,
      searchTerm: queryParam('q') || queryParam('search') || '',
      website: honeypot ? honeypot.value : ''
    };

    fetch(apiBase() + '/reader-questions', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
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
})();
