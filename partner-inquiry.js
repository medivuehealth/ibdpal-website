/**
 * Partner / education-underwriting inquiry form → /api/web/partner-inquiries
 */
(function () {
  'use strict';

  function apiBase() {
    if (window.IBDPAL_SITE_CONFIG && window.IBDPAL_SITE_CONFIG.webApiBase) {
      return window.IBDPAL_SITE_CONFIG.webApiBase;
    }
    return '/api/web';
  }

  function initForm() {
    var form = document.getElementById('partner-inquiry-form');
    if (!form) return;

    var statusEl = document.getElementById('partner-inquiry-status');
    var submitBtn = document.getElementById('partner-inquiry-submit');
    var honeypot = document.getElementById('partner-inquiry-website');

    function setStatus(message, type) {
      if (!statusEl) return;
      statusEl.hidden = !message;
      statusEl.textContent = message || '';
      statusEl.className =
        'ask-question__status' + (type ? ' ask-question__status--' + type : '');
    }

    form.addEventListener('submit', function (event) {
      event.preventDefault();
      setStatus('Saving…', 'pending');
      if (submitBtn) submitBtn.disabled = true;

      var payload = {
        organizationName: (form.organizationName && form.organizationName.value) || '',
        contactName: (form.contactName && form.contactName.value) || '',
        contactEmail: (form.contactEmail && form.contactEmail.value) || '',
        interestType: (form.interestType && form.interestType.value) || 'listing',
        programUrl: (form.programUrl && form.programUrl.value) || '',
        message: (form.message && form.message.value) || '',
        website: honeypot ? honeypot.value : '',
        source: form.getAttribute('data-source') || 'media_kit',
        pageUrl: window.location.href
      };

      fetch(apiBase() + '/partner-inquiries?action=submit', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      })
        .then(function (res) {
          return res.json().then(function (data) {
            return { ok: res.ok, status: res.status, data: data };
          });
        })
        .then(function (result) {
          if (result.data && result.data.success) {
            setStatus(result.data.message || 'Saved. Thank you.', 'success');
            form.reset();
            return;
          }
          setStatus(
            (result.data && result.data.error) ||
              'Could not save. Please try again.',
            'error'
          );
        })
        .catch(function () {
          setStatus('Network error. Please try again.', 'error');
        })
        .finally(function () {
          if (submitBtn) submitBtn.disabled = false;
        });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initForm);
  } else {
    initForm();
  }
})();
