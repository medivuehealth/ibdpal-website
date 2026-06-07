/**
 * Site-wide: crisis strip, skip link, seasonal newsletter hint, App Store ratings prompt.
 */
(function () {
  'use strict';

  var CRISIS_HTML =
    '<aside class="crisis-strip" role="note" aria-label="Urgent care reminder">' +
    '<p><strong>Education only | not emergency care.</strong> ' +
    'For life-threatening symptoms call <strong>911</strong>. ' +
    'For urgent IBD symptoms contact your clinician. ' +
    'IBD Help Center: <a href="tel:8886948872">888-MY-GUT-PAIN (888-694-8872)</a> · ' +
    '<a href="https://www.crohnscolitisfoundation.org/live-full/live-full-ibd-help-center" target="_blank" rel="noopener noreferrer">CCF Help Center</a></p>' +
    '</aside>';

  var SKIP_HTML = '<a class="skip-link" href="#main-content">Skip to main content</a>';

  function injectCrisisStrip() {
    if (document.querySelector('.crisis-strip')) return;
    var skip = document.createElement('div');
    skip.innerHTML = SKIP_HTML;
    document.body.insertBefore(skip.firstChild, document.body.firstChild);
    var container = document.querySelector('.app-container') || document.querySelector('.container');
    var crisis = document.createElement('div');
    crisis.innerHTML = CRISIS_HTML;
    if (container) {
      container.insertBefore(crisis.firstChild, container.firstChild);
    } else {
      document.body.insertBefore(crisis.firstChild, skip.nextSibling);
    }
  }

  function markMainId() {
    var main = document.querySelector('main.main-content');
    if (main && !main.id) main.id = 'main-content';
  }

  function seasonalNewsletterHint() {
    var form = document.getElementById('emailForm');
    if (!form) return;
    var note = form.querySelector('.newsletter-seasonal');
    if (note) return;
    var month = new Date().getMonth();
    var tips = [
      'Winter: hydration, illness prep, and gentle foods when appetite is low.',
      'Spring: travel and outdoor event planning with bathroom maps.',
      'Summer: heat, dehydration, and picnic food safety.',
      'Fall: back-to-school 504 plans and holiday eating strategies.'
    ];
    var seasonIndex = month <= 1 || month === 11 ? 0 : month <= 4 ? 1 : month <= 7 ? 2 : 3;
    var p = document.createElement('p');
    p.className = 'newsletter-seasonal form-note';
    p.textContent = 'Seasonal tip with your updates: ' + tips[seasonIndex];
    form.appendChild(p);
  }

  function ratingsPrompt() {
    if (localStorage.getItem('ibdpal_ratings_dismissed')) return;
    var eligible = document.querySelector('[data-tab="blogs"].active') ||
      document.querySelector('[data-tab="resources"].active') ||
      document.body.dataset.blogShareText ||
      window.location.pathname.indexOf('/blog/') !== -1 ||
      window.location.pathname.indexOf('/patient-stories') !== -1;
    if (!eligible) return;

    var box = document.createElement('div');
    box.className = 'ratings-prompt';
    box.setAttribute('role', 'dialog');
    box.setAttribute('aria-label', 'Rate IBDPal on the App Store');
    box.innerHTML =
      '<p>Is IBDPal helping your IBD journey? A quick App Store review helps other patients find us.</p>' +
      '<div class="ratings-prompt__actions">' +
      '<a href="https://apps.apple.com/us/search?term=ibdpal" target="_blank" rel="noopener noreferrer" class="ratings-prompt__btn">Find IBDPal on App Store</a>' +
      '<button type="button" class="ratings-prompt__dismiss">Not now</button>' +
      '</div>';
    document.body.appendChild(box);
    box.querySelector('.ratings-prompt__dismiss').addEventListener('click', function () {
      localStorage.setItem('ibdpal_ratings_dismissed', '1');
      box.remove();
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    injectCrisisStrip();
    markMainId();
    seasonalNewsletterHint();
    setTimeout(ratingsPrompt, 8000);
  });
})();
