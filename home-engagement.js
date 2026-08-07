/**
 * Homepage engagement rails: new content, seasonal packs, continue reading, gap answers.
 */
(function () {
  'use strict';

  var RECENT_KEY = 'ibdpal_recent_pages_v1';
  var MAX_RECENT = 6;

  function escapeHtml(s) {
    return String(s || '').replace(/[&<>"']/g, function (char) {
      return {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#39;'
      }[char];
    });
  }

  function data() {
    return window.IBDPAL_HOME_ENGAGEMENT || null;
  }

  function fillLinks(container, items, emptyMessage) {
    if (!container) return;
    if (!items || !items.length) {
      container.innerHTML = '<p class="home-rail-empty">' + escapeHtml(emptyMessage || 'Nothing here yet.') + '</p>';
      return;
    }
    container.innerHTML = items.map(function (item) {
      var badge = item.badge
        ? '<span class="home-rail-badge">' + escapeHtml(item.badge) + '</span>'
        : '';
      return (
        '<a href="' + escapeHtml(item.url) + '">' +
        badge +
        escapeHtml(item.title) +
        '</a>'
      );
    }).join('');
  }

  function revealRail(section) {
    if (!section) return;
    var rail = section.closest('.home-side-rail');
    if (rail) rail.hidden = false;
    section.hidden = false;
  }

  function renderNewContent() {
    var eng = data();
    var weekSection = document.querySelector('[data-new-week]');
    var monthSection = document.querySelector('[data-new-month]');
    if (!eng) {
      if (weekSection) weekSection.hidden = true;
      if (monthSection) monthSection.hidden = true;
      return;
    }
    var week = (eng.recent && eng.recent.week) || [];
    var month = (eng.recent && eng.recent.month) || [];
    if (weekSection) {
      if (week.length) {
        fillLinks(weekSection.querySelector('[data-new-week-list]'), week, '');
        revealRail(weekSection);
      } else {
        weekSection.hidden = true;
      }
    }
    if (monthSection) {
      var weekUrls = {};
      week.forEach(function (item) { weekUrls[item.url] = true; });
      var monthOnly = month.filter(function (item) { return !weekUrls[item.url]; });
      var monthItems = monthOnly.length ? monthOnly : month;
      if (monthItems.length) {
        fillLinks(monthSection.querySelector('[data-new-month-list]'), monthItems.slice(0, 6), '');
        revealRail(monthSection);
      } else {
        monthSection.hidden = true;
      }
    }
  }

  function renderSeasonal() {
    var section = document.querySelector('[data-seasonal-pack]');
    if (!section) return;
    var eng = data();
    var packs = (eng && eng.seasonal) || [];
    if (!packs.length) {
      section.hidden = true;
      return;
    }
    var pack = packs[0];
    var eyebrow = section.querySelector('[data-seasonal-eyebrow]');
    var title = section.querySelector('[data-seasonal-title]');
    var note = section.querySelector('[data-seasonal-note]');
    var list = section.querySelector('[data-seasonal-list]');
    if (eyebrow) eyebrow.textContent = pack.eyebrow || 'Seasonal';
    if (title) title.textContent = pack.title || 'Seasonal pack';
    if (note) note.textContent = pack.note || '';
    fillLinks(list, pack.links || [], 'Pack links coming soon.');
    revealRail(section);
  }

  function renderGapAnswers() {
    var section = document.querySelector('[data-gap-answers]');
    if (!section) return;
    var eng = data();
    var items = (eng && eng.gap_answers) || [];
    if (!items.length) {
      section.hidden = true;
      return;
    }
    fillLinks(section.querySelector('[data-gap-answers-list]'), items, '');
    revealRail(section);
  }

  function readRecent() {
    try {
      var raw = window.localStorage.getItem(RECENT_KEY);
      var parsed = raw ? JSON.parse(raw) : [];
      return Array.isArray(parsed) ? parsed : [];
    } catch (error) {
      return [];
    }
  }

  function renderContinue() {
    var section = document.querySelector('[data-continue-reading]');
    if (!section) return;
    var items = readRecent().slice(0, MAX_RECENT);
    if (!items.length) {
      section.hidden = true;
      return;
    }
    fillLinks(section.querySelector('[data-continue-list]'), items, '');
    revealRail(section);
  }

  // Expose helpers for site-global / search.
  window.IBDPAL_ENGAGEMENT = {
    rememberPage: function (url, title) {
      if (!url || url === '/' || url.indexOf('/insights') === 0) return;
      var items = readRecent().filter(function (item) {
        return item.url !== url;
      });
      items.unshift({
        url: url,
        title: title || url,
        savedAt: new Date().toISOString()
      });
      try {
        window.localStorage.setItem(RECENT_KEY, JSON.stringify(items.slice(0, MAX_RECENT)));
      } catch (error) {
        // Ignore quota / private mode.
      }
    },
    aliases: function () {
      var eng = data();
      return (eng && eng.aliases) || {};
    },
    suggestAlias: function (term) {
      var normalized = String(term || '').toLowerCase().trim();
      var aliases = this.aliases();
      if (aliases[normalized]) return aliases[normalized];
      var keys = Object.keys(aliases);
      for (var i = 0; i < keys.length; i++) {
        var key = keys[i];
        if (normalized.indexOf(key) !== -1 || key.indexOf(normalized) !== -1) {
          return aliases[key];
        }
      }
      return null;
    }
  };

  function boot() {
    renderNewContent();
    renderSeasonal();
    renderGapAnswers();
    renderContinue();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
