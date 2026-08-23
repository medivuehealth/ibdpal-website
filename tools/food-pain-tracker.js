/**
 * Food & pain tracking sheet (browser-local). Education only.
 * Storage key: ibdpal_food_pain_sheet_v1
 */
(function () {
  'use strict';

  var STORAGE_KEY = 'ibdpal_food_pain_sheet_v1';
  var MAX_ROWS = 200;
  var SYMPTOMS = [
    { id: 'cramp', label: 'Cramp' },
    { id: 'sharp', label: 'Sharp' },
    { id: 'dull', label: 'Dull ache' },
    { id: 'bloating', label: 'Bloating' },
    { id: 'urgency', label: 'Urgency' },
    { id: 'nausea', label: 'Nausea' },
    { id: 'gas', label: 'Gas' },
    { id: 'burning', label: 'Burning' },
    { id: 'joint', label: 'Joint pain' },
    { id: 'fatigue', label: 'Fatigue' }
  ];

  function $(sel, root) {
    return (root || document).querySelector(sel);
  }

  function todayLocal() {
    var d = new Date();
    return (
      d.getFullYear() +
      '-' +
      String(d.getMonth() + 1).padStart(2, '0') +
      '-' +
      String(d.getDate()).padStart(2, '0')
    );
  }

  function nowTime() {
    var d = new Date();
    return String(d.getHours()).padStart(2, '0') + ':' + String(d.getMinutes()).padStart(2, '0');
  }

  function loadRows() {
    try {
      var parsed = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]');
      return Array.isArray(parsed) ? parsed : [];
    } catch (e) {
      return [];
    }
  }

  function saveRows(rows) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(rows.slice(0, MAX_ROWS)));
  }

  function escapeHtml(s) {
    return String(s || '')
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function csvEscape(s) {
    var v = String(s == null ? '' : s);
    if (/[",\n]/.test(v)) return '"' + v.replace(/"/g, '""') + '"';
    return v;
  }

  function symptomLabels(ids) {
    var map = {};
    SYMPTOMS.forEach(function (s) {
      map[s.id] = s.label;
    });
    return (ids || [])
      .map(function (id) {
        return map[id] || id;
      })
      .join('; ');
  }

  function renderSymptomChecks(container) {
    container.innerHTML = SYMPTOMS.map(function (s) {
      return (
        '<label class="fps-check"><input type="checkbox" name="symptoms" value="' +
        s.id +
        '"> ' +
        escapeHtml(s.label) +
        '</label>'
      );
    }).join('');
  }

  function renderTable(tbody, rows) {
    if (!rows.length) {
      tbody.innerHTML =
        '<tr><td colspan="9" class="fps-empty">No entries yet. Add a meal or pain note above. Data stays in this browser only.</td></tr>';
      return;
    }
    var sorted = rows.slice().sort(function (a, b) {
      return ((b.date || '') + 'T' + (b.time || '00:00')).localeCompare(
        (a.date || '') + 'T' + (a.time || '00:00')
      );
    });
    tbody.innerHTML = sorted
      .map(function (r) {
        return (
          '<tr>' +
          '<td>' +
          escapeHtml(r.date) +
          '</td><td>' +
          escapeHtml(r.time) +
          '</td><td>' +
          escapeHtml(r.meal) +
          '</td><td>' +
          escapeHtml(r.food) +
          '</td><td>' +
          escapeHtml(r.hours) +
          '</td><td>' +
          escapeHtml(r.severity) +
          '</td><td>' +
          escapeHtml(r.pain) +
          '</td><td>' +
          escapeHtml(symptomLabels(r.symptoms)) +
          '</td><td class="fps-actions"><button type="button" class="fps-btn fps-btn--ghost" data-delete="' +
          escapeHtml(r.id) +
          '">Delete</button></td></tr>'
        );
      })
      .join('');
  }

  function collectForm(form) {
    var symptoms = Array.prototype.map.call(
      form.querySelectorAll('input[name="symptoms"]:checked'),
      function (el) {
        return el.value;
      }
    );
    return {
      id: Date.now() + '-' + Math.random().toString(36).slice(2, 7),
      date: form.date.value,
      time: form.time.value,
      meal: form.meal.value,
      food: (form.food.value || '').trim(),
      hours: (form.hours.value || '').trim(),
      severity: form.severity.value,
      pain: form.pain.value,
      symptoms: symptoms,
      notes: (form.notes.value || '').trim()
    };
  }

  function resetForm(form) {
    form.reset();
    form.date.value = todayLocal();
    form.time.value = nowTime();
    form.severity.value = '';
    form.pain.value = '';
    form.meal.value = 'Breakfast';
  }

  function exportCsv(rows) {
    var lines = [
      'Date,Time,Meal,Food,Hours after meal,Severity,Pain level,Pain symptoms,Notes'
    ];
    rows.forEach(function (r) {
      lines.push(
        [
          csvEscape(r.date),
          csvEscape(r.time),
          csvEscape(r.meal),
          csvEscape(r.food),
          csvEscape(r.hours),
          csvEscape(r.severity),
          csvEscape(r.pain),
          csvEscape(symptomLabels(r.symptoms)),
          csvEscape(r.notes)
        ].join(',')
      );
    });
    var blob = new Blob([lines.join('\n')], { type: 'text/csv;charset=utf-8' });
    var url = URL.createObjectURL(blob);
    var a = document.createElement('a');
    a.href = url;
    a.download = 'ibdpal-food-pain-sheet-' + todayLocal() + '.csv';
    a.click();
    URL.revokeObjectURL(url);
  }

  function init() {
    var root = $('[data-food-pain-sheet]');
    if (!root) return;
    var form = $('[data-fps-form]', root);
    var tbody = $('[data-fps-body]', root);
    var countEl = $('[data-fps-count]', root);
    var symptomBox = $('[data-fps-symptoms]', root);
    if (!form || !tbody || !symptomBox) return;

    renderSymptomChecks(symptomBox);
    resetForm(form);
    var rows = loadRows();

    function refresh() {
      renderTable(tbody, rows);
      if (countEl) countEl.textContent = String(rows.length);
    }

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var entry = collectForm(form);
      if (!entry.date || !entry.food) {
        form.food.focus();
        return;
      }
      rows.unshift(entry);
      if (rows.length > MAX_ROWS) rows = rows.slice(0, MAX_ROWS);
      saveRows(rows);
      refresh();
      resetForm(form);
      form.food.focus();
    });

    tbody.addEventListener('click', function (e) {
      var btn = e.target.closest('[data-delete]');
      if (!btn) return;
      var id = btn.getAttribute('data-delete');
      rows = rows.filter(function (r) {
        return r.id !== id;
      });
      saveRows(rows);
      refresh();
    });

    var exportBtn = $('[data-fps-export]', root);
    if (exportBtn) exportBtn.addEventListener('click', function () {
      exportCsv(rows);
    });
    var printBtn = $('[data-fps-print]', root);
    if (printBtn) printBtn.addEventListener('click', function () {
      window.print();
    });
    var clearBtn = $('[data-fps-clear]', root);
    if (clearBtn) {
      clearBtn.addEventListener('click', function () {
        if (!rows.length) return;
        if (!window.confirm('Clear all saved rows on this device? This cannot be undone.')) return;
        rows = [];
        saveRows(rows);
        refresh();
      });
    }

    refresh();
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
