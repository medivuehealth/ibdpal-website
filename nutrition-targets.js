(function () {
  'use strict';

  var DATA_URL = '/data/nutrition-dri-baselines.json';
  var STORAGE_KEY = 'ibdpal_nutrition_profile_v1';

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

  function renderTable(rows, emptyLabel) {
    if (!rows || !rows.length) {
      return '<p class="nutrition-targets-empty">' + escapeHtml(emptyLabel) + '</p>';
    }
    return (
      '<div class="nutrition-targets-table-wrap">' +
      '<table class="nutrition-targets-table">' +
      '<thead><tr><th scope="col">Nutrient</th><th scope="col">Daily reference</th><th scope="col">Notes for IBD readers</th></tr></thead>' +
      '<tbody>' +
      rows.map(function (row) {
        return '<tr>' +
          '<th scope="row">' + escapeHtml(row.nutrient) + '</th>' +
          '<td>' + escapeHtml(row.baseline) + '</td>' +
          '<td>' + escapeHtml(row.note || 'General NIH DRI reference for this profile.') + '</td>' +
          '</tr>';
      }).join('') +
      '</tbody></table></div>'
    );
  }

  function renderSources(sources) {
    if (!sources || !sources.length) return '';
    return (
      '<ul class="nutrition-targets-sources">' +
      sources.map(function (source) {
        return '<li><a href="' + escapeHtml(source.url) + '" rel="noopener noreferrer">' +
          escapeHtml(source.title) + '</a><span>' + escapeHtml(source.use) + '</span></li>';
      }).join('') +
      '</ul>'
    );
  }

  function renderPosts(posts, filter) {
    var list = (posts || []).filter(function (post) {
      return !filter || filter === 'all' || post.topic === filter;
    });
    if (!list.length) {
      return '<p class="nutrition-targets-empty">No matching articles yet.</p>';
    }
    return (
      '<div class="nutrition-targets-posts">' +
      list.map(function (post) {
        return '<a class="nutrition-targets-post" href="' + escapeHtml(post.url) + '">' +
          '<span class="nutrition-targets-post__topic">' + escapeHtml(post.topic) + '</span>' +
          '<strong>' + escapeHtml(post.title) + '</strong>' +
          '</a>';
      }).join('') +
      '</div>'
    );
  }

  function initNutritionTargets() {
    var root = document.querySelector('[data-nutrition-targets]');
    if (!root) return;

    var profileSelect = root.querySelector('[data-nutrition-profile]');
    var macroTable = root.querySelector('[data-nutrition-macros]');
    var microTable = root.querySelector('[data-nutrition-micros]');
    var sourcesList = root.querySelector('[data-nutrition-sources]');
    var postsGrid = root.querySelector('[data-nutrition-posts]');
    var postFilter = root.querySelector('[data-nutrition-post-filter]');
    var profileNote = root.querySelector('[data-nutrition-profile-note]');
    var payload = null;
    var currentFilter = 'all';

    function saveProfile(id) {
      try {
        window.localStorage.setItem(STORAGE_KEY, id);
      } catch (err) {
        // ignore
      }
    }

    function readProfile() {
      try {
        return window.localStorage.getItem(STORAGE_KEY) || '';
      } catch (err) {
        return '';
      }
    }

    function profileById(id) {
      if (!payload || !payload.profiles) return null;
      for (var i = 0; i < payload.profiles.length; i++) {
        if (payload.profiles[i].id === id) return payload.profiles[i];
      }
      return payload.profiles[0] || null;
    }

    function renderProfile(profile) {
      if (!profile) return;
      if (macroTable) macroTable.innerHTML = renderTable(profile.macros, 'Macronutrient data unavailable.');
      if (microTable) microTable.innerHTML = renderTable(profile.micros, 'Micronutrient data unavailable.');
      if (profileNote && payload && payload.sourceNote) {
        profileNote.textContent = payload.sourceNote;
      }
    }

    function renderPostsSection() {
      if (!postsGrid || !payload) return;
      postsGrid.innerHTML = renderPosts(payload.relatedPosts, currentFilter);
    }

    function bindProfileSelect() {
      if (!profileSelect || !payload) return;
      profileSelect.innerHTML = payload.profiles.map(function (profile) {
        return '<option value="' + escapeHtml(profile.id) + '">' + escapeHtml(profile.label) + '</option>';
      }).join('');

      var saved = readProfile();
      if (saved && profileById(saved)) {
        profileSelect.value = saved;
      }

      renderProfile(profileById(profileSelect.value));
      profileSelect.addEventListener('change', function () {
        saveProfile(profileSelect.value);
        renderProfile(profileById(profileSelect.value));
      });
    }

    if (postFilter) {
      postFilter.addEventListener('click', function (event) {
        var button = event.target.closest('[data-nutrition-filter]');
        if (!button) return;
        currentFilter = button.getAttribute('data-nutrition-filter') || 'all';
        postFilter.querySelectorAll('[data-nutrition-filter]').forEach(function (item) {
          item.classList.toggle('is-active', item === button);
        });
        renderPostsSection();
      });
    }

    window.fetch(DATA_URL)
      .then(function (response) {
        if (!response.ok) throw new Error('Nutrition data unavailable');
        return response.json();
      })
      .then(function (data) {
        payload = data;
        bindProfileSelect();
        if (sourcesList) sourcesList.innerHTML = renderSources(data.researchSources);
        renderPostsSection();
      })
      .catch(function () {
        if (macroTable) macroTable.innerHTML = '<p class="nutrition-targets-empty">Reference tables are temporarily unavailable. See <a href="/blog/how-ibdpal-nutrition-targets-work">how IBDPal sets nutrition targets</a>.</p>';
        if (microTable) microTable.innerHTML = '';
      });
  }

  document.addEventListener('DOMContentLoaded', initNutritionTargets);
})();
