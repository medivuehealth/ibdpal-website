/**
 * Pediatric IBD food & pain tracking sheet (browser-local).
 * Download blank PDF, save log as PDF/CSV. Education only.
 * Storage: ibdpal_food_pain_sheet_v2
 */
(function () {
  'use strict';

  var STORAGE_KEY = 'ibdpal_food_pain_sheet_v2';
  var LEGACY_KEY = 'ibdpal_food_pain_sheet_v1';
  var MAX_ROWS = 200;

  var SYMPTOMS = [
    { id: 'cramp', label: 'Tummy cramp' },
    { id: 'sharp', label: 'Sharp hurt' },
    { id: 'dull', label: 'Dull ache' },
    { id: 'bloating', label: 'Puffy / bloated' },
    { id: 'urgency', label: 'Gotta go / urgency' },
    { id: 'nausea', label: 'Queasy' },
    { id: 'gas', label: 'Gas' },
    { id: 'burning', label: 'Burning' },
    { id: 'joint', label: 'Joint ache' },
    { id: 'fatigue', label: 'Tired / low energy' },
    { id: 'headache', label: 'Headache' },
    { id: 'feverish', label: 'Feverish' }
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
      var raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) {
        var legacy = localStorage.getItem(LEGACY_KEY);
        if (legacy) {
          var old = JSON.parse(legacy);
          if (Array.isArray(old)) {
            var migrated = old.map(migrateRow);
            saveRows(migrated);
            return migrated;
          }
        }
        return [];
      }
      var parsed = JSON.parse(raw);
      return Array.isArray(parsed) ? parsed : [];
    } catch (e) {
      return [];
    }
  }

  function migrateRow(r) {
    return {
      id: r.id || Date.now() + '-m',
      date: r.date || '',
      time: r.time || '',
      place: r.place || 'Home',
      meal: r.meal || '',
      food: r.food || '',
      hours: r.hours || '',
      severity: r.severity || '',
      pain: r.pain || '',
      appetite: r.appetite || '',
      meds: r.meds || '',
      medsNote: r.medsNote || '',
      symptoms: r.symptoms || [],
      notes: r.notes || ''
    };
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
        '<tr><td colspan="12" class="fps-empty">No entries yet. Add a meal or tummy note above. Data stays in this browser only.</td></tr>';
      return;
    }
    var sorted = rows.slice().sort(function (a, b) {
      return ((b.date || '') + 'T' + (b.time || '00:00')).localeCompare(
        (a.date || '') + 'T' + (a.time || '00:00')
      );
    });
    tbody.innerHTML = sorted
      .map(function (r) {
        var medsCell = r.meds || '';
        if (r.medsNote) medsCell += (medsCell ? ': ' : '') + r.medsNote;
        return (
          '<tr>' +
          '<td>' +
          escapeHtml(r.date) +
          '</td><td>' +
          escapeHtml(r.time) +
          '</td><td>' +
          escapeHtml(r.place) +
          '</td><td>' +
          escapeHtml(r.meal) +
          '</td><td>' +
          escapeHtml(r.food) +
          '</td><td>' +
          escapeHtml(r.hours) +
          '</td><td>' +
          escapeHtml(r.pain) +
          '</td><td>' +
          escapeHtml(r.severity) +
          '</td><td>' +
          escapeHtml(r.appetite) +
          '</td><td>' +
          escapeHtml(symptomLabels(r.symptoms)) +
          '</td><td>' +
          escapeHtml(medsCell) +
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
      place: form.place.value,
      meal: form.meal.value,
      food: (form.food.value || '').trim(),
      hours: (form.hours.value || '').trim(),
      severity: form.severity.value,
      pain: form.pain.value,
      appetite: form.appetite.value,
      meds: form.meds.value,
      medsNote: (form.medsNote.value || '').trim(),
      symptoms: symptoms,
      notes: (form.notes.value || '').trim()
    };
  }

  function resetForm(form) {
    form.reset();
    form.date.value = todayLocal();
    form.time.value = nowTime();
    form.place.value = 'Home';
    form.meal.value = 'Breakfast';
    form.severity.value = '';
    form.pain.value = '';
    form.appetite.value = '';
    form.meds.value = '';
  }

  function exportCsv(rows) {
    var lines = [
      'Date,Time,Place,Meal,Food,Hours after meal,Pain 0-10,Severity 1-10,Appetite,Pain symptoms,Medicine (optional),Medicine note,Caregiver notes'
    ];
    rows.forEach(function (r) {
      lines.push(
        [
          csvEscape(r.date),
          csvEscape(r.time),
          csvEscape(r.place),
          csvEscape(r.meal),
          csvEscape(r.food),
          csvEscape(r.hours),
          csvEscape(r.pain),
          csvEscape(r.severity),
          csvEscape(r.appetite),
          csvEscape(symptomLabels(r.symptoms)),
          csvEscape(r.meds),
          csvEscape(r.medsNote),
          csvEscape(r.notes)
        ].join(',')
      );
    });
    downloadBlob(lines.join('\n'), 'ibdpal-pediatric-food-pain-' + todayLocal() + '.csv', 'text/csv;charset=utf-8');
  }

  function downloadBlob(content, filename, mime) {
    var blob = content instanceof Blob ? content : new Blob([content], { type: mime || 'application/octet-stream' });
    var url = URL.createObjectURL(blob);
    var a = document.createElement('a');
    a.href = url;
    a.download = filename;
    a.click();
    URL.revokeObjectURL(url);
  }

  /* --- Minimal landscape PDF (Helvetica) for blank + filled sheets --- */
  function pdfEscape(str) {
    return String(str || '')
      .replace(/\\/g, '\\\\')
      .replace(/\(/g, '\\(')
      .replace(/\)/g, '\\)')
      .replace(/[^\x20-\x7E]/g, function (ch) {
        var c = ch.charCodeAt(0);
        if (c === 8217 || c === 8216) return "'";
        if (c === 8211 || c === 8212) return '-';
        return '?';
      });
  }

  function buildPdfDoc(lines) {
    // lines: array of content-stream strings (one page each)
    var objects = [];
    function addObj(body) {
      objects.push(body);
      return objects.length;
    }

    var fontId = addObj('<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>');
    var pageIds = [];
    var contentIds = [];

    lines.forEach(function (stream) {
      var streamBody = '<< /Length ' + stream.length + ' >>\nstream\n' + stream + '\nendstream';
      var contentId = addObj(streamBody);
      contentIds.push(contentId);
    });

    contentIds.forEach(function (contentId) {
      var pageId = addObj(
        '<< /Type /Page /Parent 0 0 R /MediaBox [0 0 792 612] /Resources << /Font << /F1 ' +
          fontId +
          ' 0 R >> >> /Contents ' +
          contentId +
          ' 0 R >>'
      );
      pageIds.push(pageId);
    });

    var kids = pageIds.map(function (id) {
      return id + ' 0 R';
    }).join(' ');
    var pagesId = addObj('<< /Type /Pages /Kids [ ' + kids + ' ] /Count ' + pageIds.length + ' >>');

    // Fix Parent refs on pages
    pageIds.forEach(function (pageId) {
      objects[pageId - 1] = objects[pageId - 1].replace('/Parent 0 0 R', '/Parent ' + pagesId + ' 0 R');
    });

    var catalogId = addObj('<< /Type /Catalog /Pages ' + pagesId + ' 0 R >>');

    var out = '%PDF-1.4\n';
    var offsets = [0];
    objects.forEach(function (body, i) {
      offsets.push(out.length);
      out += i + 1 + ' 0 obj\n' + body + '\nendobj\n';
    });
    var xrefPos = out.length;
    out += 'xref\n0 ' + (objects.length + 1) + '\n';
    out += '0000000000 65535 f \n';
    for (var i = 1; i <= objects.length; i++) {
      out += String(offsets[i]).padStart(10, '0') + ' 00000 n \n';
    }
    out += 'trailer\n<< /Size ' + (objects.length + 1) + ' /Root ' + catalogId + ' 0 R >>\n';
    out += 'startxref\n' + xrefPos + '\n%%EOF';
    return out;
  }

  function textAt(x, y, size, str) {
    return 'BT /F1 ' + size + ' Tf ' + x + ' ' + y + ' Td (' + pdfEscape(str) + ') Tj ET\n';
  }

  function line(x1, y1, x2, y2) {
    return x1 + ' ' + y1 + ' m ' + x2 + ' ' + y2 + ' l S\n';
  }

  function rect(x, y, w, h) {
    return x + ' ' + y + ' ' + w + ' ' + h + ' re S\n';
  }

  function blankSheetPage(weekLabel) {
    var s = '0.2 w\n';
    s += textAt(36, 580, 14, 'IBDPal pediatric food & pain sheet');
    s += textAt(36, 562, 9, 'Education only. Not medical advice. ibdpal.org/tools/food-pain-tracker');
    s += textAt(480, 580, 10, weekLabel || 'Week of: ____________');
    s += textAt(36, 544, 9, 'Child name: ____________________  Age: ____  Caregiver: ____________________');
    s += textAt(36, 528, 8, 'Belly pain 0=none ... 10=worst. Medicine column is optional (not a full med list).');

    var headers = ['Date', 'Place', 'Meal', 'Food / drink', 'Hrs', 'Pain', 'Sev', 'Appetite', 'Symptoms', 'Meds?', 'Notes'];
    var widths = [52, 48, 58, 120, 28, 28, 28, 52, 110, 48, 100];
    var x0 = 28;
    var y = 505;
    var rowH = 28;
    var x = x0;
    headers.forEach(function (h, i) {
      s += rect(x, y - 4, widths[i], 18);
      s += textAt(x + 2, y + 2, 7, h);
      x += widths[i];
    });

    for (var r = 0; r < 14; r++) {
      y -= rowH;
      x = x0;
      widths.forEach(function (w) {
        s += rect(x, y, w, rowH);
        x += w;
      });
    }

    s += textAt(36, 48, 8, 'Symptoms ideas: tummy cramp, sharp, bloated, urgency, queasy, gas, tired, joint ache.');
    s += textAt(36, 34, 8, 'Place: Home / School / Away. Appetite: Good / OK / Poor / None. Bring this sheet to your GI visit.');
    return s;
  }

  function filledSheetPages(rows) {
    var pages = [];
    var perPage = 12;
    var sorted = rows.slice().sort(function (a, b) {
      return ((a.date || '') + 'T' + (a.time || '')).localeCompare((b.date || '') + 'T' + (b.time || ''));
    });
    if (!sorted.length) {
      pages.push(blankSheetPage('My log (empty)'));
      return pages;
    }
    for (var start = 0; start < sorted.length; start += perPage) {
      var chunk = sorted.slice(start, start + perPage);
      var s = '0.2 w\n';
      s += textAt(36, 580, 13, 'IBDPal pediatric food & pain log');
      s += textAt(36, 562, 9, 'Saved entries · Education only · ibdpal.org · Page ' + (Math.floor(start / perPage) + 1));
      var headers = ['Date', 'Place', 'Meal', 'Food', 'Hrs', 'Pain', 'Sev', 'App', 'Symptoms', 'Meds', 'Notes'];
      var widths = [54, 46, 54, 100, 28, 28, 26, 36, 100, 70, 110];
      var x0 = 28;
      var y = 540;
      var rowH = 36;
      var x = x0;
      headers.forEach(function (h, i) {
        s += rect(x, y - 2, widths[i], 16);
        s += textAt(x + 2, y + 2, 7, h);
        x += widths[i];
      });
      chunk.forEach(function (r) {
        y -= rowH;
        x = x0;
        var meds = (r.meds || '') + (r.medsNote ? ' ' + r.medsNote : '');
        var cells = [
          (r.date || '') + ' ' + (r.time || ''),
          r.place || '',
          r.meal || '',
          r.food || '',
          r.hours || '',
          r.pain || '',
          r.severity || '',
          r.appetite || '',
          symptomLabels(r.symptoms),
          meds,
          r.notes || ''
        ];
        widths.forEach(function (w, i) {
          s += rect(x, y, w, rowH);
          var txt = String(cells[i] || '').slice(0, w < 40 ? 6 : w < 80 ? 18 : 28);
          s += textAt(x + 2, y + rowH - 12, 7, txt);
          x += w;
        });
      });
      pages.push(s);
    }
    return pages;
  }

  function downloadBlankPdf() {
    var pdf = buildPdfDoc([blankSheetPage('Week of: ____________'), blankSheetPage('Week of: ____________')]);
    downloadBlob(pdf, 'ibdpal-pediatric-food-pain-blank.pdf', 'application/pdf');
  }

  function downloadLogPdf(rows) {
    var pdf = buildPdfDoc(filledSheetPages(rows));
    downloadBlob(pdf, 'ibdpal-pediatric-food-pain-log-' + todayLocal() + '.pdf', 'application/pdf');
  }

  function openPrintSheet(mode, rows) {
    var win = window.open('', '_blank', 'noopener,noreferrer,width=1100,height=800');
    if (!win) {
      window.alert('Please allow pop-ups to print or save as PDF.');
      return;
    }
    var body;
    if (mode === 'blank') {
      body =
        '<h1>IBDPal pediatric food &amp; pain sheet</h1>' +
        '<p class="meta">Child: __________ Age: ____ Caregiver: __________ Week of: __________</p>' +
        '<p class="hint">Belly pain 0–10. Medicine column optional. Education only · ibdpal.org</p>' +
        blankTableHtml(14) +
        blankTableHtml(14);
    } else {
      body =
        '<h1>IBDPal pediatric food &amp; pain log</h1>' +
        '<p class="meta">Printed ' +
        escapeHtml(todayLocal()) +
        ' · Education only</p>' +
        filledTableHtml(rows);
    }
    win.document.write(
      '<!DOCTYPE html><html><head><title>IBDPal food &amp; pain sheet</title>' +
        '<style>' +
        '@page{size:landscape;margin:12mm}' +
        'body{font-family:system-ui,sans-serif;font-size:11px;color:#222}' +
        'h1{font-size:16px;margin:0 0 6px}' +
        '.meta,.hint{margin:0 0 8px;color:#444}' +
        'table{width:100%;border-collapse:collapse;margin:0 0 18px}' +
        'th,td{border:1px solid #333;padding:6px 4px;vertical-align:top}' +
        'th{background:#f4f4f4;font-size:10px}' +
        'td{height:28px}' +
        '@media print{.noprint{display:none}}' +
        '</style></head><body>' +
        '<p class="noprint"><button onclick="window.print()">Print / Save as PDF</button></p>' +
        body +
        '</body></html>'
    );
    win.document.close();
    setTimeout(function () {
      try {
        win.focus();
        win.print();
      } catch (e) {}
    }, 250);
  }

  function blankTableHtml(n) {
    var head =
      '<tr><th>Date</th><th>Place</th><th>Meal</th><th>Food / drink</th><th>Hrs</th><th>Pain 0–10</th><th>Severity</th><th>Appetite</th><th>Symptoms</th><th>Meds?</th><th>Notes</th></tr>';
    var rows = '';
    for (var i = 0; i < n; i++) {
      rows += '<tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>';
    }
    return '<table><thead>' + head + '</thead><tbody>' + rows + '</tbody></table>';
  }

  function filledTableHtml(rows) {
    var head =
      '<tr><th>Date</th><th>Time</th><th>Place</th><th>Meal</th><th>Food</th><th>Hrs</th><th>Pain</th><th>Sev</th><th>Appetite</th><th>Symptoms</th><th>Meds</th><th>Notes</th></tr>';
    if (!rows.length) {
      return '<table><thead>' + head + '</thead><tbody><tr><td colspan="12">No saved entries.</td></tr></tbody></table>';
    }
    var sorted = rows.slice().sort(function (a, b) {
      return ((a.date || '') + 'T' + (a.time || '')).localeCompare((b.date || '') + 'T' + (b.time || ''));
    });
    var body = sorted
      .map(function (r) {
        var meds = (r.meds || '') + (r.medsNote ? ': ' + r.medsNote : '');
        return (
          '<tr><td>' +
          escapeHtml(r.date) +
          '</td><td>' +
          escapeHtml(r.time) +
          '</td><td>' +
          escapeHtml(r.place) +
          '</td><td>' +
          escapeHtml(r.meal) +
          '</td><td>' +
          escapeHtml(r.food) +
          '</td><td>' +
          escapeHtml(r.hours) +
          '</td><td>' +
          escapeHtml(r.pain) +
          '</td><td>' +
          escapeHtml(r.severity) +
          '</td><td>' +
          escapeHtml(r.appetite) +
          '</td><td>' +
          escapeHtml(symptomLabels(r.symptoms)) +
          '</td><td>' +
          escapeHtml(meds) +
          '</td><td>' +
          escapeHtml(r.notes) +
          '</td></tr>'
        );
      })
      .join('');
    return '<table><thead>' + head + '</thead><tbody>' + body + '</tbody></table>';
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

    function bind(sel, fn) {
      var el = $(sel, root);
      if (el) el.addEventListener('click', fn);
    }

    bind('[data-fps-export]', function () {
      exportCsv(rows);
    });
    bind('[data-fps-pdf-blank]', function () {
      downloadBlankPdf();
    });
    bind('[data-fps-pdf-log]', function () {
      downloadLogPdf(rows);
    });
    bind('[data-fps-print-blank]', function () {
      openPrintSheet('blank');
    });
    bind('[data-fps-print]', function () {
      openPrintSheet('log', rows);
    });
    bind('[data-fps-clear]', function () {
      if (!rows.length) return;
      if (!window.confirm('Clear all saved rows on this device? This cannot be undone.')) return;
      rows = [];
      saveRows(rows);
      refresh();
    });

    refresh();
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
