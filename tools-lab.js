(function () {
  'use strict';

  var STORAGE_KEY = 'ibdpal_food_detective_clues_v1';
  var NLM_ENDPOINT = 'https://clinicaltables.nlm.nih.gov/api/conditions/v3/search';
  var WEB_API_BASE = (window.IBDPAL_SITE_CONFIG && window.IBDPAL_SITE_CONFIG.webApiBase) ||
    'https://ibdpal-server-production.up.railway.app/api/web';
  var TERM_ALIASES = {
    fatigue: ['fatigue', 'tired', 'exhaustion', 'brain fog', 'energy', 'anemia', 'sleep', 'lethargy'],
    tired: ['fatigue', 'tired', 'exhaustion', 'brain fog', 'energy', 'anemia', 'sleep'],
    diarrhea: ['diarrhea', 'loose stool', 'stool', 'flare', 'hydration', 'urgent'],
    'abdominal pain': ['abdominal pain', 'pain', 'cramping', 'flare', 'urgent'],
    pain: ['pain', 'cramping', 'flare', 'urgent', 'joint pain'],
    'crohn\'s disease': ['crohn', 'crohn\'s disease', 'flare', 'nutrition', 'treatment'],
    crohn: ['crohn', 'crohn\'s disease', 'flare', 'nutrition', 'treatment'],
    'ulcerative colitis': ['ulcerative colitis', 'colitis', 'uc', 'flare', 'blood', 'urgency'],
    colitis: ['ulcerative colitis', 'colitis', 'uc', 'flare', 'blood', 'urgency']
  };
  var RELATED_FALLBACKS = {
    fatigue: [
      {
        title: 'IBD Fatigue and Brain Fog: Why You Feel Exhausted and What Helps',
        url: '/blog/ibd-fatigue-brain-fog',
        description: 'Inflammation, anemia, sleep, medications, pacing strategies, and labs to discuss.'
      },
      {
        title: 'Sleep and rest during IBD flares',
        url: '/guides/sleep-ibd-flares',
        description: 'Sleep disruption and fatigue during flares, with practical rest tips.'
      },
      {
        title: 'First gastroenterology appointment for IBD',
        url: '/guides/first-gastroenterology-appointment-ibd',
        description: 'What to bring and how to describe fatigue, stool changes, pain, and other patterns.'
      }
    ]
  };
  var FALLBACK_SUGGESTIONS = [
    { term: 'fatigue', label: 'Fatigue' },
    { term: 'flare symptoms', label: 'Flare symptoms' },
    { term: 'abdominal pain', label: 'Abdominal pain' },
    { term: 'diarrhea', label: 'Diarrhea' },
    { term: 'biologics', label: 'Biologics' }
  ];

  function debounce(fn, delay) {
    var timer = null;
    return function () {
      var args = arguments;
      window.clearTimeout(timer);
      timer = window.setTimeout(function () {
        fn.apply(null, args);
      }, delay);
    };
  }

  function readClues() {
    try {
      return JSON.parse(window.localStorage.getItem(STORAGE_KEY) || '[]');
    } catch (err) {
      return [];
    }
  }

  function writeClues(clues) {
    window.localStorage.setItem(STORAGE_KEY, JSON.stringify(clues.slice(0, 50)));
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

  function normalizeFood(value) {
    return String(value || '').trim().replace(/\s+/g, ' ');
  }

  function normalizeTerm(value) {
    return String(value || '').toLowerCase().replace(/[^\w\s'-]/g, ' ').replace(/\s+/g, ' ').trim();
  }

  function slugFromUrl(value) {
    var parts = String(value || '').split('?')[0].split('#')[0].split('/').filter(Boolean);
    return parts.length ? parts[parts.length - 1] : '';
  }

  function suggestionLabel(item) {
    return item.label || item.term || item.normalized_term || '';
  }

  function recordSearchEvent(payload) {
    var term = String(payload.term || '').trim();
    var normalizedTerm = normalizeTerm(payload.normalizedTerm || term);
    if (normalizedTerm.length < 2) return;

    window.fetch(WEB_API_BASE + '/search-events', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      keepalive: true,
      body: JSON.stringify({
        term: term.slice(0, 120),
        normalizedTerm: normalizedTerm,
        source: 'tools_lab',
        resultCount: payload.resultCount || 0,
        clickedArticleUrl: payload.clickedArticleUrl || null,
        clickedArticleSlug: payload.clickedArticleSlug || null
      })
    }).catch(function () {
      // Analytics should never interrupt patient education tools.
    });
  }

  function termsForRelatedSearch(value) {
    var normalized = normalizeTerm(value);
    var terms = normalized ? [normalized] : [];

    Object.keys(TERM_ALIASES).forEach(function (key) {
      if (normalized === key || normalized.indexOf(key) !== -1 || key.indexOf(normalized) !== -1) {
        terms = terms.concat(TERM_ALIASES[key]);
      }
    });

    return terms.filter(function (term, index, list) {
      return term && list.indexOf(term) === index;
    });
  }

  function initClinicalLookup() {
    var root = document.querySelector('[data-clinical-lookup]');
    if (!root) return;

    var input = document.getElementById('clinicalTermSearch');
    var results = document.getElementById('clinicalLookupResults');
    var status = document.getElementById('clinicalLookupHint');
    var related = root.querySelector('[data-clinical-related]');
    var relatedList = root.querySelector('[data-clinical-related-list]');
    var relatedNote = root.querySelector('[data-clinical-related-note]');
    var suggestions = root.querySelector('[data-clinical-suggestions]');
    var lastTrackedSearch = '';
    if (!input || !results || !status) return;

    function setStatus(message) {
      status.textContent = message;
    }

    function renderResults(items) {
      results.innerHTML = '';
      if (!items.length) {
        results.innerHTML = '<li class="clinical-lookup__empty">No matches found. Try a broader term.</li>';
        return;
      }

      results.innerHTML = items.map(function (item) {
        return '<li><button type="button" data-clinical-result="' + escapeHtml(item) + '">' + escapeHtml(item) + '</button></li>';
      }).join('');
    }

    function parseNlmPayload(payload) {
      var rows = Array.isArray(payload) && Array.isArray(payload[3]) ? payload[3] : [];
      return rows.map(function (row) {
        return Array.isArray(row) ? row[0] : row;
      }).filter(Boolean).slice(0, 8);
    }

    function resourceHaystack(resource) {
      return [
        resource.title,
        resource.description,
        (resource.tags || []).join(' '),
        (resource.keywords || []).join(' ')
      ].join(' ').toLowerCase();
    }

    function relatedFallbackFor(value) {
      var terms = termsForRelatedSearch(value);
      var key = terms.indexOf('fatigue') !== -1 ? 'fatigue' : '';
      return key ? RELATED_FALLBACKS[key] || [] : [];
    }

    function relatedResourcesFor(value) {
      var terms = termsForRelatedSearch(value);
      var resources = Array.isArray(window.IBDPAL_RESOURCES) ? window.IBDPAL_RESOURCES : [];
      if (!terms.length || !resources.length) {
        return relatedFallbackFor(value);
      }

      var scored = resources.map(function (resource) {
        if (resource.type === 'external') return null;

        var title = String(resource.title || '').toLowerCase();
        var description = String(resource.description || '').toLowerCase();
        var tags = (resource.tags || []).join(' ').toLowerCase();
        var keywords = (resource.keywords || []).join(' ').toLowerCase();
        var haystack = resourceHaystack(resource);
        var score = 0;

        terms.forEach(function (term) {
          if (title.indexOf(term) !== -1) score += 6;
          if (tags.indexOf(term) !== -1) score += 4;
          if (keywords.indexOf(term) !== -1) score += 4;
          if (description.indexOf(term) !== -1) score += 2;
          if (haystack.indexOf(term) !== -1) score += 1;
        });

        return score > 0 ? { score: score, resource: resource } : null;
      }).filter(Boolean).sort(function (a, b) {
        return b.score - a.score;
      }).slice(0, 4).map(function (entry) {
        return entry.resource;
      });

      return scored.length ? scored : relatedFallbackFor(value);
    }

    function renderRelated(value) {
      if (!related || !relatedList || !relatedNote) return 0;

      var term = String(value || '').trim();
      if (term.length < 2) {
        related.hidden = true;
        relatedList.innerHTML = '';
        relatedNote.textContent = 'Type or select a term to see matching IBDPal education links.';
        return 0;
      }

      var matches = relatedResourcesFor(term);
      related.hidden = false;
      relatedNote.textContent = matches.length
        ? 'Helpful IBDPal content related to "' + term + '":'
        : 'No close IBDPal matches yet. Try a broader term or browse the library.';

      if (!matches.length) {
        relatedList.innerHTML =
          '<a class="clinical-related-card" href="/resources">' +
          '<strong>Browse the full resource library</strong>' +
          '<span>Search all guides, articles, and trusted sources.</span>' +
          '</a>';
        return 0;
      }

      relatedList.innerHTML = matches.map(function (resource) {
        return '<a class="clinical-related-card" href="' + escapeHtml(resource.url) + '" data-clinical-related-card data-related-url="' + escapeHtml(resource.url) + '">' +
          '<strong>' + escapeHtml(resource.title) + '</strong>' +
          '<span>' + escapeHtml(resource.description || 'IBDPal education link.') + '</span>' +
          '</a>';
      }).join('');
      return matches.length;
    }

    function trackLookup(term, resultCount) {
      var normalized = normalizeTerm(term);
      if (normalized.length < 2 || normalized === lastTrackedSearch) return;
      lastTrackedSearch = normalized;
      recordSearchEvent({
        term: term,
        normalizedTerm: normalized,
        resultCount: resultCount
      });
    }

    function renderSuggestions(items, isFallback) {
      if (!suggestions) return;
      var source = (items && items.length ? items : FALLBACK_SUGGESTIONS).slice(0, 5);
      suggestions.innerHTML =
        '<span>' + (isFallback ? 'Try:' : 'Readers also search:') + '</span>' +
        source.map(function (item) {
          var label = suggestionLabel(item);
          var term = item.term || item.normalized_term || label;
          return '<button type="button" data-clinical-pick="' + escapeHtml(term) + '">' + escapeHtml(label) + '</button>';
        }).join('');
      suggestions.hidden = false;
    }

    function loadSuggestions() {
      if (!suggestions) return;
      window.fetch(WEB_API_BASE + '/search-suggestions?days=14&limit=5&source=tools_lab')
        .then(function (response) {
          if (!response.ok) throw new Error('Suggestions unavailable');
          return response.json();
        })
        .then(function (payload) {
          renderSuggestions(payload && payload.suggestions, false);
        })
        .catch(function () {
          renderSuggestions(FALLBACK_SUGGESTIONS, true);
        });
    }

    var runSearch = debounce(function () {
      var term = input.value.trim();
      if (term.length < 2) {
        results.innerHTML = '';
        setStatus('Type 2 or more letters. Results come from NLM Clinical Tables.');
        renderRelated(term);
        return;
      }

      setStatus('Searching NLM Clinical Tables...');
      var relatedCount = renderRelated(term);
      trackLookup(term, relatedCount);
      var url = NLM_ENDPOINT + '?terms=' + encodeURIComponent(term) + '&maxList=8&df=primary_name';

      window.fetch(url)
        .then(function (response) {
          if (!response.ok) throw new Error('NLM request failed');
          return response.json();
        })
        .then(function (payload) {
          var items = parseNlmPayload(payload);
          renderResults(items);
          setStatus(items.length ? 'Select a term to reuse it in your notes.' : 'No matches found.');
        })
        .catch(function () {
          results.innerHTML = '<li class="clinical-lookup__empty">NLM lookup is unavailable right now. You can still type terms manually.</li>';
          setStatus('Lookup unavailable. Try again later.');
        });
    }, 300);

    input.addEventListener('input', runSearch);

    root.addEventListener('click', function (event) {
      var relatedCard = event.target.closest('[data-clinical-related-card]');
      if (relatedCard) {
        var relatedUrl = relatedCard.getAttribute('data-related-url') || relatedCard.getAttribute('href') || '';
        recordSearchEvent({
          term: input.value,
          normalizedTerm: normalizeTerm(input.value),
          resultCount: relatedList ? relatedList.querySelectorAll('[data-clinical-related-card]').length : 0,
          clickedArticleUrl: relatedUrl,
          clickedArticleSlug: slugFromUrl(relatedUrl)
        });
        return;
      }

      var pick = event.target.closest('[data-clinical-pick], [data-clinical-result]');
      if (!pick) return;
      input.value = pick.getAttribute('data-clinical-pick') || pick.getAttribute('data-clinical-result') || '';
      results.innerHTML = '';
      setStatus('Selected term. This is terminology lookup only, not a clinical confirmation.');
      var relatedCount = renderRelated(input.value);
      trackLookup(input.value, relatedCount);
      input.focus();
    });

    var initialTerm = new URLSearchParams(window.location.search).get('toolTerm');
    if (initialTerm) {
      input.value = initialTerm;
      runSearch();
    }
    loadSuggestions();
  }

  function initFoodDetective() {
    var root = document.querySelector('[data-food-detective]');
    var form = document.getElementById('foodDetectiveForm');
    if (!root || !form) return;

    var foodInput = document.getElementById('detectiveFood');
    var symptomInput = document.getElementById('detectiveSymptoms');
    var severityInput = document.getElementById('detectiveSeverity');
    var alertBox = root.querySelector('[data-red-flag-alert]');
    var suspectList = root.querySelector('[data-suspect-list]');
    var clearButton = root.querySelector('[data-clear-detective]');

    function currentRedFlags() {
      return Array.prototype.slice.call(root.querySelectorAll('.food-detective-redflags input:checked')).map(function (item) {
        return item.value;
      });
    }

    function renderSuspects() {
      var clues = readClues();
      var byFood = {};

      clues.forEach(function (clue) {
        var key = clue.food.toLowerCase();
        if (!byFood[key]) {
          byFood[key] = {
            label: clue.food,
            count: 0,
            totalSeverity: 0,
            lastNote: ''
          };
        }
        byFood[key].count += 1;
        byFood[key].totalSeverity += Number(clue.severity || 1);
        byFood[key].lastNote = clue.symptoms || byFood[key].lastNote;
      });

      var suspects = Object.keys(byFood).map(function (key) {
        var suspect = byFood[key];
        suspect.averageSeverity = suspect.totalSeverity / suspect.count;
        return suspect;
      }).sort(function (a, b) {
        return (b.count * b.averageSeverity) - (a.count * a.averageSeverity);
      });

      if (!suspectList) return;
      if (!suspects.length) {
        suspectList.innerHTML = '<li class="food-detective-suspects__empty">No clues yet. Add a meal or ingredient to start a local suspect list.</li>';
        return;
      }

      suspectList.innerHTML = suspects.map(function (suspect) {
        var strength = suspect.count >= 3 ? 'possible pattern' : suspect.count === 2 ? 'watch item' : 'single clue';
        return '<li>' +
          '<div><strong>' + escapeHtml(suspect.label) + '</strong><span>' + strength + '</span></div>' +
          '<p>' + suspect.count + ' local clue' + (suspect.count === 1 ? '' : 's') + ' - average intensity ' + suspect.averageSeverity.toFixed(1) + '/5</p>' +
          (suspect.lastNote ? '<small>Latest note: ' + escapeHtml(suspect.lastNote) + '</small>' : '') +
          '</li>';
      }).join('');
    }

    root.addEventListener('change', function () {
      if (!alertBox) return;
      alertBox.hidden = currentRedFlags().length === 0;
    });

    form.addEventListener('submit', function (event) {
      event.preventDefault();
      var redFlags = currentRedFlags();
      if (redFlags.length && alertBox) {
        alertBox.hidden = false;
        alertBox.focus && alertBox.focus();
        return;
      }

      var food = normalizeFood(foodInput && foodInput.value);
      if (!food) return;

      var clues = readClues();
      clues.unshift({
        food: food,
        symptoms: symptomInput ? symptomInput.value.trim() : '',
        severity: severityInput ? Number(severityInput.value) : 1,
        createdAt: new Date().toISOString()
      });
      writeClues(clues);
      form.reset();
      renderSuspects();
    });

    if (clearButton) {
      clearButton.addEventListener('click', function () {
        window.localStorage.removeItem(STORAGE_KEY);
        renderSuspects();
      });
    }

    renderSuspects();
  }

  document.addEventListener('DOMContentLoaded', function () {
    initClinicalLookup();
    initFoodDetective();
  });
})();
