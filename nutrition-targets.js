(function () {
  'use strict';

  var BASELINES_URL = '/data/nutrition-dri-baselines.json';
  var FOOD_SOURCES_URL = '/data/nutrition-food-sources.json';
  var STORAGE_KEY = 'ibdpal_nutrition_profile_v1';
  var NUTRIENT_STORAGE_KEY = 'ibdpal_nutrition_nutrient_v1';

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

  function renderFoodTable(rows, emptyLabel) {
    if (!rows || !rows.length) {
      return '<p class="nutrition-targets-empty">' + escapeHtml(emptyLabel) + '</p>';
    }
    return (
      '<div class="nutrition-targets-table-wrap">' +
      '<table class="nutrition-targets-table nutrition-targets-table--foods">' +
      '<thead><tr><th scope="col">Food</th><th scope="col">Serving</th><th scope="col">Amount</th><th scope="col">Per oz</th></tr></thead>' +
      '<tbody>' +
      rows.map(function (row) {
        return '<tr>' +
          '<th scope="row">' + escapeHtml(row.food) + '</th>' +
          '<td>' + escapeHtml(row.serving) + '</td>' +
          '<td>' + escapeHtml(row.amount) + '</td>' +
          '<td>' + escapeHtml(row.perOz || '—') + '</td>' +
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

  function renderRemissionContext(context) {
    if (!context) return '';
    return (
      '<article class="nutrition-targets-card nutrition-targets-card--wide nutrition-targets-card--remission">' +
      '<h2>' + escapeHtml(context.title) + '</h2>' +
      '<ul class="nutrition-targets-facts">' +
      (context.points || []).map(function (point) {
        return '<li>' + escapeHtml(point) + '</li>';
      }).join('') +
      '</ul></article>'
    );
  }

  function renderNutrientDetail(nutrient) {
    if (!nutrient) {
      return '<p class="nutrition-targets-empty">Select a micronutrient to see food sources.</p>';
    }

    var gentle = (nutrient.gentleIbd || []).map(function (item) {
      return '<li>' + escapeHtml(item) + '</li>';
    }).join('');

    return (
      '<div class="nutrition-food-detail">' +
      '<p class="nutrition-food-detail__dri"><strong>NIH DRI:</strong> ' +
      escapeHtml(nutrient.driAdultFemale) + ' · ' + escapeHtml(nutrient.driAdultMale) + '</p>' +
      '<p class="nutrition-food-detail__ibd">' + escapeHtml(nutrient.ibdNote) + '</p>' +
      '<h3 class="nutrition-targets-section-title">Top natural food sources</h3>' +
      renderFoodTable(nutrient.foods, 'No food source data for this nutrient.') +
      '<h3 class="nutrition-targets-section-title">Fruits &amp; vegetables (per serving)</h3>' +
      renderFoodTable(
        nutrient.produce,
        nutrient.produce && nutrient.produce.length
          ? ''
          : 'This nutrient is mainly found in fish, dairy, fortified foods, or supplements rather than produce.'
      ) +
      (gentle
        ? '<h3 class="nutrition-targets-section-title">Gentler options for Crohn\'s &amp; colitis (team-approved)</h3>' +
          '<ul class="nutrition-targets-facts nutrition-targets-facts--gentle">' + gentle + '</ul>'
        : '') +
      '</div>'
    );
  }

  function initNutritionTargets() {
    var root = document.querySelector('[data-nutrition-targets]');
    if (!root) return;

    var profileSelect = root.querySelector('[data-nutrition-profile]');
    var nutrientSelect = root.querySelector('[data-nutrition-nutrient]');
    var macroTable = root.querySelector('[data-nutrition-macros]');
    var microTable = root.querySelector('[data-nutrition-micros]');
    var sourcesList = root.querySelector('[data-nutrition-sources]');
    var postsGrid = root.querySelector('[data-nutrition-posts]');
    var postFilter = root.querySelector('[data-nutrition-post-filter]');
    var profileNote = root.querySelector('[data-nutrition-profile-note]');
    var foodIntro = root.querySelector('[data-nutrition-food-intro]');
    var foodDetail = root.querySelector('[data-nutrition-food-detail]');
    var remissionSlot = root.querySelector('[data-nutrition-remission]');
    var baselines = null;
    var foodData = null;
    var currentFilter = 'all';

    function saveProfile(id) {
      try { window.localStorage.setItem(STORAGE_KEY, id); } catch (err) { /* ignore */ }
    }

    function readProfile() {
      try { return window.localStorage.getItem(STORAGE_KEY) || ''; } catch (err) { return ''; }
    }

    function saveNutrient(id) {
      try { window.localStorage.setItem(NUTRIENT_STORAGE_KEY, id); } catch (err) { /* ignore */ }
    }

    function readNutrient() {
      try { return window.localStorage.getItem(NUTRIENT_STORAGE_KEY) || ''; } catch (err) { return ''; }
    }

    function profileById(id) {
      if (!baselines || !baselines.profiles) return null;
      for (var i = 0; i < baselines.profiles.length; i++) {
        if (baselines.profiles[i].id === id) return baselines.profiles[i];
      }
      return baselines.profiles[0] || null;
    }

    function nutrientById(id) {
      if (!foodData || !foodData.nutrients) return null;
      for (var i = 0; i < foodData.nutrients.length; i++) {
        if (foodData.nutrients[i].id === id) return foodData.nutrients[i];
      }
      return foodData.nutrients[0] || null;
    }

    function renderProfile(profile) {
      if (!profile) return;
      if (macroTable) macroTable.innerHTML = renderTable(profile.macros, 'Macronutrient data unavailable.');
      if (microTable) microTable.innerHTML = renderTable(profile.micros, 'Micronutrient data unavailable.');
      if (profileNote && baselines && baselines.sourceNote) {
        profileNote.textContent = baselines.sourceNote;
      }
    }

    function renderPostsSection() {
      if (!postsGrid || !baselines) return;
      postsGrid.innerHTML = renderPosts(baselines.relatedPosts, currentFilter);
    }

    function renderFoodSection() {
      if (!foodDetail || !foodData) return;
      var selected = nutrientSelect ? nutrientSelect.value : '';
      foodDetail.innerHTML = renderNutrientDetail(nutrientById(selected));
    }

    function bindProfileSelect() {
      if (!profileSelect || !baselines) return;
      profileSelect.innerHTML = baselines.profiles.map(function (profile) {
        return '<option value="' + escapeHtml(profile.id) + '">' + escapeHtml(profile.label) + '</option>';
      }).join('');

      var saved = readProfile();
      if (saved && profileById(saved)) profileSelect.value = saved;

      renderProfile(profileById(profileSelect.value));
      profileSelect.addEventListener('change', function () {
        saveProfile(profileSelect.value);
        renderProfile(profileById(profileSelect.value));
      });
    }

    function bindNutrientSelect() {
      if (!nutrientSelect || !foodData) return;
      nutrientSelect.innerHTML = foodData.nutrients.map(function (nutrient) {
        return '<option value="' + escapeHtml(nutrient.id) + '">' + escapeHtml(nutrient.name) + '</option>';
      }).join('');

      var saved = readNutrient();
      if (saved && nutrientById(saved)) nutrientSelect.value = saved;

      renderFoodSection();
      nutrientSelect.addEventListener('change', function () {
        saveNutrient(nutrientSelect.value);
        renderFoodSection();
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

    Promise.all([
      window.fetch(BASELINES_URL).then(function (response) {
        if (!response.ok) throw new Error('Baselines unavailable');
        return response.json();
      }),
      window.fetch(FOOD_SOURCES_URL).then(function (response) {
        if (!response.ok) throw new Error('Food sources unavailable');
        return response.json();
      })
    ])
      .then(function (results) {
        baselines = results[0];
        foodData = results[1];

        bindProfileSelect();
        bindNutrientSelect();

        if (sourcesList) {
          var sources = (baselines.researchSources || []).slice();
          if (foodData.dataSource) {
            sources.unshift({
              title: foodData.dataSource.title,
              url: foodData.dataSource.url,
              use: foodData.dataSource.note
            });
          }
          sourcesList.innerHTML = renderSources(sources);
        }

        if (foodIntro && foodData.intro) {
          foodIntro.textContent = foodData.intro;
        }

        if (remissionSlot && foodData.remissionContext) {
          remissionSlot.innerHTML = renderRemissionContext(foodData.remissionContext);
        }

        renderPostsSection();
      })
      .catch(function () {
        if (macroTable) {
          macroTable.innerHTML = '<p class="nutrition-targets-empty">Reference tables are temporarily unavailable. See <a href="/blog/how-ibdpal-nutrition-targets-work">how IBDPal sets nutrition targets</a>.</p>';
        }
        if (microTable) microTable.innerHTML = '';
        if (foodDetail) {
          foodDetail.innerHTML = '<p class="nutrition-targets-empty">Food source tables are temporarily unavailable.</p>';
        }
      });
  }

  document.addEventListener('DOMContentLoaded', initNutritionTargets);
})();
