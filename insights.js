(function () {
  'use strict';

  var WEB_API_BASE = (window.IBDPAL_SITE_CONFIG && window.IBDPAL_SITE_CONFIG.webApiBase) || '/api/web';
  var days = 30;

  function $(sel) {
    return document.querySelector(sel);
  }

  function escapeHtml(value) {
    return String(value || '')
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function setStatus(message, isError) {
    var el = $('[data-insights-status]');
    if (!el) return;
    el.textContent = message;
    el.classList.toggle('is-error', !!isError);
  }

  function titleFromPath(url, slug) {
    if (slug) return slug.replace(/-/g, ' ');
    return String(url || '').replace(/^\//, '') || 'page';
  }

  function fillTable(table, rows, columns) {
    var tbody = table && table.querySelector('tbody');
    if (!tbody) return;
    if (!rows || !rows.length) {
      tbody.innerHTML = '<tr><td colspan="' + columns + '">No rows in this window yet.</td></tr>';
      return;
    }
    tbody.innerHTML = rows.map(function (cells) {
      return '<tr>' + cells.map(function (cell) {
        return '<td>' + cell + '</td>';
      }).join('') + '</tr>';
    }).join('');
  }

  function fillIdeas(list, ideas) {
    if (!list) return;
    if (!ideas || !ideas.length) {
      list.innerHTML = '<li>No content ideas in this window yet.</li>';
      return;
    }
    list.innerHTML = ideas.map(function (idea) {
      var label = escapeHtml(idea.label || idea.term || '');
      var reason = escapeHtml(idea.reason || '');
      var title = escapeHtml(idea.title || label);
      return '<li><strong>' + label + '</strong>: ' + title +
        (reason ? '<br><span class="insights-idea-reason">' + reason + '</span>' : '') +
        '</li>';
    }).join('');
  }

  function fetchJson(path) {
    return window.fetch(WEB_API_BASE + path, { credentials: 'same-origin' })
      .then(function (res) {
        if (!res.ok) throw new Error('Request failed (' + res.status + ')');
        return res.json();
      });
  }

  function loadInsights() {
    setStatus('Loading live insights for the last ' + days + ' days…');

    var briefDays = days === 30 ? 7 : days;
    var gapsUrl = '/search-gaps?days=' + days + '&limit=12&minCount=1&maxResults=3';
    var searchesUrl = '/top-searches?days=' + days + '&limit=12&minCount=1';
    var ideasUrl = '/content-ideas?days=' + days + '&limit=10';
    var viewsUrl = '/top-content?days=' + days + '&limit=12&minCount=1&eventType=view';
    var clicksUrl = '/top-content?days=' + days + '&limit=12&minCount=1&eventType=click';
    var briefUrl = '/content-brief?days=' + briefDays + '&limit=10';

    return Promise.all([
      fetchJson(gapsUrl),
      fetchJson(searchesUrl),
      fetchJson(ideasUrl),
      fetchJson(viewsUrl),
      fetchJson(clicksUrl),
      fetchJson(briefUrl)
    ]).then(function (payloads) {
      var gaps = payloads[0];
      var searches = payloads[1];
      var ideas = payloads[2];
      var views = payloads[3];
      var clicks = payloads[4];
      var brief = payloads[5];

      var summary = brief.summary || {};
      var summaryEl = $('[data-insights-brief-summary]');
      if (summaryEl) {
        summaryEl.innerHTML =
          '<p><strong>' + (summary.searches || 0) + '</strong> searches · ' +
          '<strong>' + (summary.uniqueTerms || 0) + '</strong> unique terms · ' +
          '<strong>' + (summary.zeroResultSearches || 0) + '</strong> zero-result searches ' +
          '(brief window: ' + briefDays + 'd)</p>';
      }

      fillTable($('[data-insights-hard-gaps]'), (brief.hardGaps || []).map(function (row) {
        return [
          '<strong>' + escapeHtml(row.label || row.term) + '</strong>',
          String(row.count || 0)
        ];
      }), 2);

      fillTable($('[data-insights-brief-searches]'), (brief.topSearches || []).map(function (row) {
        return [
          '<strong>' + escapeHtml(row.label || row.term) + '</strong>',
          String(row.count || 0)
        ];
      }), 2);

      fillTable($('[data-insights-gaps]'), (gaps.gaps || []).map(function (row) {
        return [
          '<strong>' + escapeHtml(row.label || row.term) + '</strong>',
          String(row.count || 0),
          (row.averageResults == null ? '-' : Number(row.averageResults).toFixed(1))
        ];
      }), 3);

      fillTable($('[data-insights-searches]'), (searches.searches || []).map(function (row) {
        return [
          '<strong>' + escapeHtml(row.label || row.term) + '</strong>',
          String(row.count || 0)
        ];
      }), 2);

      fillIdeas($('[data-insights-ideas]'), ideas.ideas || []);

      fillTable($('[data-insights-views]'), (views.content || []).map(function (row) {
        var href = escapeHtml(row.url || '#');
        var label = escapeHtml(titleFromPath(row.url, row.slug));
        return [
          '<a href="' + href + '">' + label + '</a>',
          String(row.count || 0)
        ];
      }), 2);

      fillTable($('[data-insights-clicks]'), (clicks.content || []).map(function (row) {
        var href = escapeHtml(row.url || '#');
        var label = escapeHtml(titleFromPath(row.url, row.slug));
        return [
          '<a href="' + href + '">' + label + '</a>',
          String(row.count || 0)
        ];
      }), 2);

      setStatus('Updated for the last ' + days + ' days · ' + new Date().toLocaleString());
    }).catch(function (err) {
      console.error('insights load failed', err);
      setStatus('Could not load insights. Check DATABASE_URL /api/web routes.', true);
    });
  }

  function bindRange() {
    document.querySelectorAll('.insights-range__btn[data-days]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        days = parseInt(btn.getAttribute('data-days'), 10) || 30;
        document.querySelectorAll('.insights-range__btn[data-days]').forEach(function (el) {
          el.classList.toggle('is-active', el === btn);
        });
        loadInsights();
      });
    });
    var refresh = $('[data-insights-refresh]');
    if (refresh) {
      refresh.addEventListener('click', loadInsights);
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () {
      bindRange();
      loadInsights();
    });
  } else {
    bindRange();
    loadInsights();
  }
})();
