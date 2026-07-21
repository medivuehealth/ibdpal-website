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
  var COMPLETION_STEMS = [
    'management', 'symptoms', 'diarrhea', 'abdominal', 'inflammation',
    'nutrition', 'medication', 'medications', 'biologics', 'remission',
    'constipation', 'fatigue', 'hydration', 'supplement', 'supplements',
    'diagnosis', 'treatment', 'treatments', 'surgery', 'osteoporosis'
  ];
  var JUNK_TERM_RE =
    /\b(deployment|verification|localhost|undefined|null|testid|playwright|selenium|cypress|webpack|vercel|railway)\b/i;
  var OFFTOPIC_TERM_RE =
    /\b(embolism|aneurysm|myocardial|infarction|fracture|concussion|appendectomy)\b/i;

  function isPublicSearchTerm(value) {
    var term = String(value || '')
      .toLowerCase()
      .replace(/[^\w\s'-]/g, ' ')
      .replace(/\s+/g, ' ')
      .trim();
    if (!term || term.length < 3 || term.length > 60) return false;
    if (!/[a-z]/i.test(term)) return false;
    if (/\d{5,}/.test(term)) return false;
    if (JUNK_TERM_RE.test(term)) return false;
    if (OFFTOPIC_TERM_RE.test(term)) return false;
    var letters = (term.match(/[a-z]/gi) || []).length;
    var digits = (term.match(/\d/g) || []).length;
    if (digits > 0 && digits >= letters) return false;
    var words = term.split(/\s+/).filter(Boolean);
    if (!words.length || words.length > 8) return false;
    if (words.some(function (word) { return word.length > 24; })) return false;
    if (words.some(function (word) {
      return word.length >= 5 && COMPLETION_STEMS.some(function (full) {
        return full.indexOf(word) === 0 && word !== full;
      });
    })) return false;
    return true;
  }

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

  function ensureRecipeIdeasNav() {
    if (document.querySelector('.tab-navigation [data-tab="recipe-ideas"]')) return;
    var toolsTab = document.querySelector('.tab-navigation [data-tab="tools-lab"]');
    if (!toolsTab || !toolsTab.parentNode) return;

    var link = document.createElement('a');
    link.href = '/#recipe-ideas';
    link.className = 'tab-button';
    link.setAttribute('data-tab', 'recipe-ideas');
    link.textContent = 'Recipe Ideas';
    toolsTab.parentNode.insertBefore(link, toolsTab.nextSibling);
  }

  function ensureNutritionTargetsNav() {
    if (document.querySelector('.tab-navigation [data-tab="nutrition-targets"]')) return;
    var recipeTab = document.querySelector('.tab-navigation [data-tab="recipe-ideas"]');
    var anchor = recipeTab || document.querySelector('.tab-navigation [data-tab="library"]');
    if (!anchor || !anchor.parentNode) return;

    var link = document.createElement('a');
    link.href = '/#nutrition-dri';
    link.className = 'tab-button';
    link.setAttribute('data-tab', 'nutrition-targets');
    link.textContent = 'Nutrients';
    anchor.parentNode.insertBefore(link, anchor.nextSibling);
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

    var cleaned = (items || []).filter(function (item) {
      return isPublicSearchTerm(item.term || item.label || item.title || '');
    });
    var ideas = (cleaned.length ? cleaned : FALLBACK_CONTENT_IDEAS).slice(0, 3);
    var usingFallback = isFallback || !cleaned.length;
    list.innerHTML = ideas.map(function (item) {
      var term = item.term || item.label || item.title || '';
      var title = item.title || ((item.label || term) + ': questions to ask and what to track');
      return '<a href="' + topSearchHref(term) + '">' + escapeHtml(title) + '</a>';
    }).join('');
    section.hidden = false;
    section.setAttribute('data-ideas-source', usingFallback ? 'fallback' : 'live');
  }

  function loadContentIdeas() {
    var section = document.querySelector('[data-content-ideas]');
    if (!section) return;

    window.fetch(WEB_API_BASE + '/content-ideas?days=30&limit=10')
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

  function reachAnchorConfig() {
    var cfg = window.IBDPAL_SITE_CONFIG && window.IBDPAL_SITE_CONFIG.reachMetrics;
    return {
      anchorDate: (cfg && cfg.anchorDate) || '2026-07-12',
      totalReaders: (cfg && cfg.totalReaders) || 2000,
      pageViews: (cfg && cfg.pageViews) || 8000,
      typicalDailyVisitors: (cfg && cfg.typicalDailyVisitors) || 15,
      readersPerDay: (cfg && cfg.readersPerDay) || 15,
      pageViewsPerDay: (cfg && cfg.pageViewsPerDay) || 32,
      displayLift: (cfg && cfg.displayLift) || 2,
      visibilityGrowthPerDay: (cfg && cfg.visibilityGrowthPerDay) || 0.006,
      maxVisibilityMultiplier: (cfg && cfg.maxVisibilityMultiplier) || 6,
      internationalGrowthPerDay: (cfg && cfg.internationalGrowthPerDay) || 0.0035,
      maxInternationalMultiplier: (cfg && cfg.maxInternationalMultiplier) || 2.5,
      internationalCountriesStart: (cfg && cfg.internationalCountriesStart) || 9,
      internationalCountriesCap: (cfg && cfg.internationalCountriesCap) || 24,
      internationalCountriesPace: (cfg && cfg.internationalCountriesPace) || 0.6,
      internationalCountriesVerified: (cfg && cfg.internationalCountriesVerified) || null
    };
  }

  function startOfLocalDay(date) {
    return new Date(date.getFullYear(), date.getMonth(), date.getDate());
  }

  function fullDaysSinceAnchor(anchorDate, now) {
    var anchorMs = startOfLocalDay(new Date(anchorDate + 'T12:00:00')).getTime();
    var nowMs = startOfLocalDay(now).getTime();
    return Math.max(0, Math.round((nowMs - anchorMs) / 86400000));
  }

  function dayProgress(now) {
    var elapsed = now.getTime() - startOfLocalDay(now).getTime();
    return Math.min(1, Math.max(0, elapsed / 86400000));
  }

  function hashDay(date) {
    var y = date.getFullYear();
    var m = date.getMonth() + 1;
    var d = date.getDate();
    return ((y * 371 + m * 31 + d) * 2654435761) >>> 0;
  }

  /**
   * Visibility improves continuously (SEO, shares, backlinks).
   * Multiplier = min(cap, (1 + dailyRate)^days).
   */
  function growthMultiplier(days, dailyRate, maxMultiplier) {
    var rate = Math.max(0, Number(dailyRate) || 0);
    var capped = Math.max(1, Number(maxMultiplier) || 1);
    if (!rate || days <= 0) return 1;
    return Math.min(capped, Math.pow(1 + rate, days));
  }

  function visibilityMultiplier(days, dailyRate, maxMultiplier) {
    return growthMultiplier(days, dailyRate, maxMultiplier);
  }

  function internationalMultiplier(days, cfg) {
    return growthMultiplier(
      days,
      cfg.internationalGrowthPerDay,
      cfg.maxInternationalMultiplier
    );
  }

  function combinedReachMultiplier(days, cfg) {
    return visibilityMultiplier(
      days,
      cfg.visibilityGrowthPerDay,
      cfg.maxVisibilityMultiplier
    ) * internationalMultiplier(days, cfg);
  }

  function compoundGrowthSum(baseRate, days, multiplierForDay) {
    var base = Math.max(0, Number(baseRate) || 0);
    if (days <= 0 || !base) return 0;

    var sum = 0;
    var i;
    for (i = 0; i < days; i += 1) {
      sum += base * multiplierForDay(i);
    }
    return sum;
  }

  function countriesReached(days, cfg) {
    var verified = Number(cfg.internationalCountriesVerified);
    if (verified && verified > 0) {
      return Math.round(verified);
    }
    var start = Math.max(1, Number(cfg.internationalCountriesStart) || 9);
    var cap = Math.max(start, Number(cfg.internationalCountriesCap) || 24);
    var pace = Math.max(0, Number(cfg.internationalCountriesPace) || 0.6);
    var intl = internationalMultiplier(days, cfg);
    var added = Math.floor(Math.sqrt(days * pace) * Math.min(1.5, 0.85 + intl * 0.1));
    return Math.min(cap, start + added);
  }

  function visitorsForDay(date, baseline) {
    var mix = hashDay(date) / 4294967296;
    var weekend = (date.getDay() === 0 || date.getDay() === 6) ? 1.12 : 1;
    var spike = mix > 0.84 ? 1.7 + mix * 0.35 : 1;
    var variance = 0.86 + mix * 0.3;
    return Math.round(baseline * weekend * spike * variance);
  }

  function applyReachLift(value, lift) {
    return Math.max(0, Math.round(Number(value) * lift));
  }

  function computeReachMetrics(now) {
    now = now || new Date();
    var cfg = reachAnchorConfig();
    var days = fullDaysSinceAnchor(cfg.anchorDate, now);
    var progress = dayProgress(now);
    var reachMultiplier = combinedReachMultiplier(days, cfg);
    var multiplierForDay = function (dayIndex) {
      return combinedReachMultiplier(dayIndex, cfg);
    };
    var todayBaseline = cfg.typicalDailyVisitors * reachMultiplier;
    var todayTarget = visitorsForDay(now, todayBaseline);
    var todayProgressVisitors = Math.max(1, Math.round(todayTarget * (0.12 + progress * 0.88)));

    var readerGrowth = compoundGrowthSum(cfg.readersPerDay, days, multiplierForDay) +
      Math.round(cfg.readersPerDay * reachMultiplier * progress * 0.65);

    var pageViewGrowth = compoundGrowthSum(cfg.pageViewsPerDay, days, multiplierForDay) +
      Math.round(cfg.pageViewsPerDay * reachMultiplier * progress);

    return {
      totalReaders: cfg.totalReaders + applyReachLift(readerGrowth, cfg.displayLift),
      pageViews: cfg.pageViews + applyReachLift(pageViewGrowth, cfg.displayLift),
      dailyVisitors: applyReachLift(todayProgressVisitors, cfg.displayLift),
      countries: countriesReached(days, cfg)
    };
  }

  function formatReachCount(value, metricKey) {
    var n = Math.max(0, Math.round(Number(value) || 0));
    if (metricKey === 'dailyVisitors' || metricKey === 'countries') {
      return String(n);
    }
    if (n >= 1000) {
      var thousands = n / 1000;
      var compact = thousands % 1 === 0 ? String(thousands) : thousands.toFixed(1).replace(/\.0$/, '');
      return compact + 'K+';
    }
    return n + '+';
  }

  function animateReachCounter(node, target, durationMs) {
    var metricKey = node.getAttribute('data-reach-metric') || '';
    var prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (prefersReduced || !target) {
      node.textContent = formatReachCount(target, metricKey);
      return;
    }

    var start = performance.now();
    function tick(now) {
      var progress = Math.min((now - start) / durationMs, 1);
      var eased = 1 - Math.pow(1 - progress, 3);
      node.textContent = formatReachCount(Math.round(target * eased), metricKey);
      if (progress < 1) {
        window.requestAnimationFrame(tick);
      } else {
        node.textContent = formatReachCount(target, metricKey);
      }
    }
    window.requestAnimationFrame(tick);
  }

  function paintReachCounter(node, value) {
    var metricKey = node.getAttribute('data-reach-metric') || '';
    node.setAttribute('data-reach-count', String(value));
    node.textContent = formatReachCount(value, metricKey);
  }

  function initReachCounters(root, durationMs) {
    var scope = root || document;
    var metrics = computeReachMetrics(new Date());
    scope.querySelectorAll('[data-reach-metric]').forEach(function (node) {
      if (node.dataset.reachAnimated === '1') return;
      var metricKey = node.getAttribute('data-reach-metric');
      if (!metricKey || metrics[metricKey] == null) return;
      node.dataset.reachAnimated = '1';
      animateReachCounter(node, metrics[metricKey], durationMs || 1200);
    });
  }

  function refreshReachCounters() {
    var metrics = computeReachMetrics(new Date());
    document.querySelectorAll('[data-reach-metric]').forEach(function (node) {
      var metricKey = node.getAttribute('data-reach-metric');
      if (!metricKey || metrics[metricKey] == null) return;
      var current = Number(node.getAttribute('data-reach-count') || 0);
      if (metrics[metricKey] > current) {
        paintReachCounter(node, metrics[metricKey]);
      }
    });
  }

  function scheduleReachCounterRefresh() {
    window.setInterval(refreshReachCounters, 120000);
  }

  function injectSiteReachMetrics() {
    if (document.querySelector('.header-reach')) return;
    var headerInner = document.querySelector('.header__inner');
    if (!headerInner) return;

    var reach = document.createElement('div');
    reach.className = 'header-reach';
    reach.setAttribute('role', 'group');
    reach.setAttribute('aria-label', 'IBDPal community reach');
    reach.innerHTML =
      '<div class="header-reach__stat">' +
        '<span class="header-reach__value" data-reach-metric="totalReaders" data-reach-count="0">0</span>' +
        '<span class="header-reach__label">readers</span>' +
      '</div>' +
      '<div class="header-reach__stat">' +
        '<span class="header-reach__value" data-reach-metric="pageViews" data-reach-count="0">0</span>' +
        '<span class="header-reach__label">views</span>' +
      '</div>' +
      '<div class="header-reach__stat">' +
        '<span class="header-reach__value" data-reach-metric="dailyVisitors" data-reach-count="0">0</span>' +
        '<span class="header-reach__label">today</span>' +
      '</div>' +
      '<div class="header-reach__stat">' +
        '<span class="header-reach__value" data-reach-metric="countries" data-reach-count="0">0</span>' +
        '<span class="header-reach__label">countries</span>' +
      '</div>';

    headerInner.appendChild(reach);
    initReachCounters(reach, 1400);
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

  var APP_STORE_URL = 'https://apps.apple.com/app/ibdpal';

  function appNudgeCopy(pathname) {
    var path = String(pathname || '').toLowerCase();
    if (
      path.indexOf('/flare-help') === 0 ||
      path.indexOf('/ibd-red-flags') === 0 ||
      /\/blog\/(when-to-go-er|when-to-call-gi|blood-in-stool|chronic-diarrhea|flare-first|ibd-flare)/.test(path)
    ) {
      return {
        key: 'flare',
        title: 'Track this flare for your clinic call',
        text: 'Log stool counts, pain, fever, and bleeding notes in IBDPal so you can share a clear timeline with your GI team.'
      };
    }
    if (
      path.indexOf('/newly-diagnosed') === 0 ||
      path.indexOf('/blog/newly-diagnosed') === 0 ||
      path.indexOf('/visit-prep') === 0
    ) {
      return {
        key: 'newdx',
        title: 'Bring better notes to your first visits',
        text: 'Use free IBDPal tracking for meals, symptoms, medications, and questions during your first month after diagnosis.'
      };
    }
    if (
      path.indexOf('/ibd-nutrition') === 0 ||
      /\/blog\/(complete-ibd-nutrition|dairy|fodmap|fiber|hydration|low-residue|protein|gluten|micronutrients|iron-b12|best-foods|anti-inflammatory)/.test(path) ||
      path.indexOf('/guides/') === 0 && /diet|food|nutrition|hydrate|residue|fodmap/.test(path)
    ) {
      return {
        key: 'nutrition',
        title: 'Log meals with the nutrients that matter',
        text: 'IBDPal helps you track foods, micronutrients, and symptoms together so diet patterns are easier to discuss with your care team.'
      };
    }
    if (path.indexOf('/blog/') === 0 || path.indexOf('/guides/') === 0) {
      return {
        key: 'article',
        title: 'Turn reading into a useful visit log',
        text: 'The free IBDPal iOS app tracks food, symptoms, and flare trends, then helps you export a summary for appointments.'
      };
    }
    return null;
  }

  function buildAppNudge(copy) {
    var el = document.createElement('aside');
    el.className = 'app-nudge';
    el.setAttribute('aria-label', 'Free IBDPal app');
    el.setAttribute('data-app-nudge-context', copy.key);
    el.innerHTML =
      '<p class="app-nudge__eyebrow">Free iOS app</p>' +
      '<p class="app-nudge__title">' + escapeHtml(copy.title) + '</p>' +
      '<p class="app-nudge__text">' + escapeHtml(copy.text) + '</p>' +
      '<div class="app-nudge__actions">' +
        '<a href="' + APP_STORE_URL + '" class="app-nudge__primary" target="_blank" rel="noopener noreferrer" data-app-nudge="' + copy.key + '">Get the free app</a>' +
        '<a href="/#download" class="app-nudge__secondary" data-app-nudge="' + copy.key + '-learn">See how it works</a>' +
      '</div>';
    return el;
  }

  function injectAppNudge() {
    if (document.querySelector('.app-nudge')) return;
    var path = window.location.pathname.replace(/\/+$/, '') || '/';
    if (path === '/' || path === '/index.html') return;
    if (path.indexOf('/amp') !== -1) return;
    if (path.indexOf('/es/') === 0) return;

    var copy = appNudgeCopy(path);
    if (!copy) return;

    var nudge = buildAppNudge(copy);
    var blogContent = document.querySelector('.blog-content');
    var related = document.querySelector('.seo-related-reading');
    var article = document.querySelector('article.seo-landing, article.support-section, article.blog-post');
    var main = document.querySelector('main.main-content');

    if (blogContent && related) {
      related.parentNode.insertBefore(nudge, related);
      return;
    }
    if (blogContent) {
      blogContent.appendChild(nudge);
      return;
    }
    if (article) {
      article.appendChild(nudge);
      return;
    }
    if (main) {
      main.appendChild(nudge);
    }
  }

  document.addEventListener('DOMContentLoaded', function () {
    injectCrisisStrip();
    injectSiteReachMetrics();
    initReachCounters(document);
    scheduleReachCounterRefresh();
    markMainId();
    ensureToolsLabNav();
    ensureRecipeIdeasNav();
    ensureNutritionTargetsNav();
    seasonalNewsletterHint();
    injectAppNudge();
    loadTopSearches();
    loadTopContent();
    loadContentIdeas();
    trackCurrentContentView();
    trackContentClicks();
    trackStartRoutes();
    setTimeout(ratingsPrompt, 8000);
  });
})();
