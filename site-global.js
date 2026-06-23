/**
 * Site-wide: crisis strip, skip link, seasonal newsletter hint, App Store ratings prompt.
 */
(function () {
  'use strict';

  var CRISIS_HTML =
    '<aside class="crisis-strip" role="note" aria-label="Educational use reminder">' +
    '<p><span class="crisis-strip__icon" aria-hidden="true">ⓘ</span> ' +
    '<span class="crisis-strip__text">Educational resource only. ' +
    'For emergencies call <strong>911</strong>.</span></p>' +
    '</aside>';

  var SKIP_HTML = '<a class="skip-link" href="#main-content">Skip to main content</a>';
  var WEB_API_BASE = (window.IBDPAL_SITE_CONFIG && window.IBDPAL_SITE_CONFIG.webApiBase) ||
    'https://ibdpal-server-production.up.railway.app/api/web';
  var FALLBACK_SEARCHES = [
    { term: 'fatigue', label: 'Fatigue' },
    { term: 'diarrhea', label: 'Diarrhea' },
    { term: 'abdominal pain', label: 'Abdominal pain' },
    { term: 'crohn diet', label: 'Crohn\'s diet' },
    { term: 'flare symptoms', label: 'Flare symptoms' }
  ];
  var FALLBACK_CONTENT = [
    { url: '/blog/ibd-fatigue-brain-fog', title: 'IBD fatigue and brain fog' },
    { url: '/blog/flare-first-48-hours', title: 'First 48 hours of a flare' },
    { url: '/blog/hydration-tips-ibd', title: 'Hydration tips for IBD' },
    { url: '/guides/sleep-ibd-flares', title: 'Sleep and rest during flares' },
    { url: '/research', title: 'IBD research sources' }
  ];
  var FALLBACK_CONTENT_IDEAS = [
    { title: 'Fatigue: questions to ask and what to track', term: 'fatigue' },
    { title: 'Flare foods: gentle options and red flags', term: 'flare foods' },
    { title: 'Biologics: visit questions for new starts', term: 'biologics' }
  ];

  function escapeHtml(value) {
    return String(value || '').replace(/[&<>"']/g, function (char) {
      return {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#39;'
      }[char];
    });
  }

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

  function ensureToolsLabNav() {
    if (document.querySelector('.tab-navigation [data-tab="tools-lab"]')) return;
    var libraryTab = document.querySelector('.tab-navigation [data-tab="library"]');
    if (!libraryTab || !libraryTab.parentNode) return;

    var link = document.createElement('a');
    link.href = '/#tools-lab';
    link.className = 'tab-button';
    link.setAttribute('data-tab', 'tools-lab');
    link.textContent = 'Tools Lab';
    libraryTab.parentNode.insertBefore(link, libraryTab.nextSibling);
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

  function topSearchHref(term) {
    return '/?toolTerm=' + encodeURIComponent(term) + '#tools-lab';
  }

  function titleFromSlug(slug) {
    return String(slug || '')
      .replace(/-/g, ' ')
      .replace(/\bibd\b/gi, 'IBD')
      .replace(/\buc\b/gi, 'UC')
      .replace(/\b\w/g, function (char) {
        return char.toUpperCase();
      });
  }

  function resourceTitleForUrl(url) {
    var pathname = String(url || '');
    var resources = Array.isArray(window.IBDPAL_RESOURCES) ? window.IBDPAL_RESOURCES : [];
    for (var i = 0; i < resources.length; i++) {
      if (resources[i].url === pathname) return resources[i].title;
    }
    if (pathname === '/research') return 'IBD research sources';
    if (pathname === '/resources') return 'Guides and tools';
    if (pathname === '/library') return 'Patient library';
    return titleFromSlug(contentSlugFromPath(pathname));
  }

  function contentTypeFromPath(pathname) {
    if (pathname.indexOf('/blog/') === 0) return 'article';
    if (pathname.indexOf('/guides/') === 0) return 'guide';
    if (pathname === '/research' || pathname.indexOf('/research/') === 0) return 'research';
    if (pathname === '/resources' || pathname === '/library') return 'library';
    return 'page';
  }

  function contentSlugFromPath(pathname) {
    var parts = String(pathname || '').split('/').filter(Boolean);
    return parts.length ? parts[parts.length - 1] : '';
  }

  function isTrackableContentPath(pathname) {
    return pathname.indexOf('/blog/') === 0 ||
      pathname.indexOf('/guides/') === 0 ||
      pathname === '/research' ||
      pathname.indexOf('/research/') === 0 ||
      pathname === '/resources' ||
      pathname === '/library';
  }

  function recordContentEvent(payload) {
    var contentUrl = payload.contentUrl || window.location.pathname;
    if (!contentUrl || contentUrl === '/') return;

    window.fetch(WEB_API_BASE + '/content-events', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      keepalive: true,
      body: JSON.stringify({
        contentUrl: contentUrl,
        contentSlug: payload.contentSlug || contentSlugFromPath(contentUrl),
        contentType: payload.contentType || contentTypeFromPath(contentUrl),
        source: payload.source || 'direct',
        eventType: payload.eventType || 'view',
        referrerPath: payload.referrerPath || window.location.pathname
      })
    }).catch(function () {
      // Content analytics should never block navigation or reading.
    });
  }

  function trackCurrentContentView() {
    var pathname = window.location.pathname;
    if (!isTrackableContentPath(pathname)) return;
    recordContentEvent({
      contentUrl: pathname,
      contentSlug: contentSlugFromPath(pathname),
      contentType: contentTypeFromPath(pathname),
      source: document.referrer ? 'direct' : 'direct',
      eventType: 'view',
      referrerPath: document.referrer ? new URL(document.referrer, window.location.origin).pathname : ''
    });
  }

  function sourceFromLink(anchor) {
    if (anchor.closest('[data-clinical-related]')) return 'tools_lab';
    if (anchor.closest('[data-resource-library]')) return 'patient_library';
    if (anchor.closest('#articles')) return 'articles_tab';
    if (anchor.closest('#sources')) return 'research_tab';
    if (anchor.closest('#home')) return 'homepage';
    if (anchor.closest('.tab-navigation')) return 'site_nav';
    return 'direct';
  }

  function trackContentClicks() {
    document.addEventListener('click', function (event) {
      var anchor = event.target.closest('a[href]');
      if (!anchor) return;
      if (anchor.closest('[data-start-route]')) return;

      var url;
      try {
        url = new URL(anchor.getAttribute('href'), window.location.origin);
      } catch (error) {
        return;
      }

      if (url.origin !== window.location.origin || !isTrackableContentPath(url.pathname)) return;

      recordContentEvent({
        contentUrl: url.pathname,
        contentSlug: contentSlugFromPath(url.pathname),
        contentType: contentTypeFromPath(url.pathname),
        source: sourceFromLink(anchor),
        eventType: 'click',
        referrerPath: window.location.pathname + window.location.hash
      });
    });
  }

  function renderTopSearches(items, isFallback) {
    var section = document.querySelector('[data-top-searches]');
    if (!section) return;

    var list = section.querySelector('[data-top-searches-list]');
    var title = section.querySelector('[data-top-searches-title]');
    var note = section.querySelector('[data-top-searches-note]');
    if (!list || !title || !note) return;

    var searches = (items && items.length ? items : FALLBACK_SEARCHES).slice(0, 5);
    title.textContent = 'Readers are looking for';
    note.textContent = isFallback || !items || !items.length
      ? 'Common topics while daily search data builds.'
      : 'Tap a topic to open Tools Lab with related education links.';

    list.innerHTML = searches.map(function (item) {
      var term = item.term || item.normalized_term || item.label || '';
      var label = item.label || term;
      return '<a href="' + topSearchHref(term) + '">' + escapeHtml(label) + '</a>';
    }).join('');
    section.hidden = false;
  }

  function loadTopSearches() {
    var section = document.querySelector('[data-top-searches]');
    if (!section) return;

    window.fetch(WEB_API_BASE + '/top-searches?days=1&limit=5&minCount=2')
      .then(function (response) {
        if (!response.ok) throw new Error('Top searches unavailable');
        return response.json();
      })
      .then(function (payload) {
        renderTopSearches(payload && payload.searches, false);
      })
      .catch(function () {
        renderTopSearches(FALLBACK_SEARCHES, true);
      });
  }

  function renderTopContent(items, isFallback) {
    var section = document.querySelector('[data-top-content]');
    if (!section) return;

    var list = section.querySelector('[data-top-content-list]');
    var heading = section.querySelector('[data-top-content-title]');
    var windowLabel = section.querySelector('[data-top-content-window]');
    var note = section.querySelector('[data-top-content-note]');
    if (!list || !note) return;

    var content = (items && items.length ? items : FALLBACK_CONTENT).slice(0, 5);
    if (heading) heading.textContent = 'Most helpful this week';
    if (windowLabel) windowLabel.textContent = 'This week';
    note.textContent = isFallback || !items || !items.length
      ? 'Common reads while weekly view data builds.'
      : 'Articles and guides readers are opening most this week.';

    list.innerHTML = content.map(function (item) {
      var url = item.url || item.content_url || '/blog';
      var contentTitle = item.title || resourceTitleForUrl(url);
      return '<a href="' + escapeHtml(url) + '">' + escapeHtml(contentTitle) + '</a>';
    }).join('');
    section.hidden = false;
  }

  function loadTopContent() {
    var section = document.querySelector('[data-top-content]');
    if (!section) return;

    window.fetch(WEB_API_BASE + '/top-content?days=7&limit=5&minCount=1&eventType=view')
      .then(function (response) {
        if (!response.ok) throw new Error('Top content unavailable');
        return response.json();
      })
      .then(function (payload) {
        if (payload && payload.content && payload.content.length) {
          renderTopContent(payload.content, false);
          return;
        }
        return window.fetch(WEB_API_BASE + '/top-content?days=7&limit=5&minCount=1&eventType=click')
          .then(function (response) {
            if (!response.ok) throw new Error('Top clicked content unavailable');
            return response.json();
          })
          .then(function (clickPayload) {
            renderTopContent(clickPayload && clickPayload.content, false);
          });
      })
      .catch(function () {
        renderTopContent(FALLBACK_CONTENT, true);
      });
  }

  function renderContentIdeas(items, isFallback) {
    var section = document.querySelector('[data-content-ideas]');
    if (!section) return;

    var list = section.querySelector('[data-content-ideas-list]');
    if (!list) return;

    var ideas = (items && items.length ? items : FALLBACK_CONTENT_IDEAS).slice(0, 3);
    list.innerHTML = ideas.map(function (item) {
      var term = item.term || item.label || item.title || '';
      var title = item.title || ((item.label || term) + ': questions to ask and what to track');
      return '<a href="' + topSearchHref(term) + '">' + escapeHtml(title) + '</a>';
    }).join('');
    section.hidden = false;
  }

  function loadContentIdeas() {
    var section = document.querySelector('[data-content-ideas]');
    if (!section) return;

    window.fetch(WEB_API_BASE + '/content-ideas?days=30&limit=3')
      .then(function (response) {
        if (!response.ok) throw new Error('Content ideas unavailable');
        return response.json();
      })
      .then(function (payload) {
        renderContentIdeas(payload && payload.ideas, false);
      })
      .catch(function () {
        renderContentIdeas(FALLBACK_CONTENT_IDEAS, true);
      });
  }

  function trackStartRoutes() {
    document.addEventListener('click', function (event) {
      var route = event.target.closest('[data-start-route]');
      if (!route) return;

      var url;
      try {
        url = new URL(route.getAttribute('href'), window.location.origin);
      } catch (error) {
        return;
      }

      if (url.origin !== window.location.origin) return;
      recordContentEvent({
        contentUrl: url.pathname,
        contentSlug: contentSlugFromPath(url.pathname),
        contentType: contentTypeFromPath(url.pathname),
        source: 'homepage',
        eventType: 'click',
        referrerPath: 'start_route:' + (route.getAttribute('data-start-route') || '')
      });
    });
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
    ensureToolsLabNav();
    seasonalNewsletterHint();
    loadTopSearches();
    loadTopContent();
    loadContentIdeas();
    trackCurrentContentView();
    trackContentClicks();
    trackStartRoutes();
    setTimeout(ratingsPrompt, 8000);
  });
})();
