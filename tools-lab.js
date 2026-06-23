(function () {
  'use strict';

  var STORAGE_KEY = 'ibdpal_food_detective_clues_v1';
  var NLM_ENDPOINT = 'https://clinicaltables.nlm.nih.gov/api/conditions/v3/search';

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

  function initClinicalLookup() {
    var root = document.querySelector('[data-clinical-lookup]');
    if (!root) return;

    var input = document.getElementById('clinicalTermSearch');
    var results = document.getElementById('clinicalLookupResults');
    var status = document.getElementById('clinicalLookupHint');
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

    var runSearch = debounce(function () {
      var term = input.value.trim();
      if (term.length < 2) {
        results.innerHTML = '';
        setStatus('Type 2 or more letters. Results come from NLM Clinical Tables.');
        return;
      }

      setStatus('Searching NLM Clinical Tables...');
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
      var pick = event.target.closest('[data-clinical-pick], [data-clinical-result]');
      if (!pick) return;
      input.value = pick.getAttribute('data-clinical-pick') || pick.getAttribute('data-clinical-result') || '';
      results.innerHTML = '';
      setStatus('Selected term. This is terminology lookup only, not a clinical confirmation.');
      input.focus();
    });
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
