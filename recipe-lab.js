(function () {
  'use strict';

  var WEB_API_BASE = (window.IBDPAL_SITE_CONFIG && window.IBDPAL_SITE_CONFIG.webApiBase) || '/api/web';
  var LIMIT_KEY = 'ibdpal_recipe_requests_v2';
  var DAILY_LIMIT = 20;

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

  function todayKey() {
    return new Date().toISOString().slice(0, 10);
  }

  function readLimit() {
    try {
      var parsed = JSON.parse(window.localStorage.getItem(LIMIT_KEY) || '{}');
      return parsed.date === todayKey() ? parsed : { date: todayKey(), count: 0 };
    } catch (error) {
      return { date: todayKey(), count: 0 };
    }
  }

  function writeLimit(value) {
    window.localStorage.setItem(LIMIT_KEY, JSON.stringify(value));
  }

  function youtubeUrl(query) {
    return 'https://www.youtube.com/results?search_query=' + encodeURIComponent(query);
  }

  function renderRecipe(recipe) {
    var ingredients = Array.isArray(recipe.ingredients) ? recipe.ingredients : [];
    var steps = Array.isArray(recipe.steps) ? recipe.steps : [];
    var queries = Array.isArray(recipe.youtubeQueries) ? recipe.youtubeQueries : [];

    return '<article class="recipe-card">' +
      '<h3>' + escapeHtml(recipe.title) + '</h3>' +
      '<p>' + escapeHtml(recipe.whyItMayFit) + '</p>' +
      '<div class="recipe-card__section">' +
      '<h4>Ingredients</h4>' +
      '<ul>' + ingredients.map(function (item) {
        return '<li>' + escapeHtml(item) + '</li>';
      }).join('') + '</ul>' +
      '</div>' +
      '<div class="recipe-card__section">' +
      '<h4>Simple steps</h4>' +
      '<ol>' + steps.map(function (item) {
        return '<li>' + escapeHtml(item) + '</li>';
      }).join('') + '</ol>' +
      '</div>' +
      '<p class="recipe-card__note">' + escapeHtml(recipe.ibdNote) + '</p>' +
      '<div class="recipe-card__videos">' +
      '<h4>YouTube cooking searches</h4>' +
      queries.map(function (query) {
        return '<a href="' + youtubeUrl(query) + '" target="_blank" rel="noopener noreferrer">' + escapeHtml(query) + '</a>';
      }).join('') +
      '</div>' +
      '</article>';
  }

  function initRecipeIdeas() {
    var root = document.querySelector('[data-recipe-ideas]');
    if (!root) return;

    var form = document.getElementById('recipeIdeaForm');
    var goal = document.getElementById('recipeGoal');
    var ingredients = document.getElementById('recipeIngredients');
    var avoid = document.getElementById('recipeAvoid');
    var notes = document.getElementById('recipeNotes');
    var results = root.querySelector('[data-recipe-ideas-results]');
    var status = root.querySelector('[data-recipe-ideas-status]');
    var limitNote = root.querySelector('[data-recipe-ideas-limit-note]');
    if (!form || !results || !status) return;

    function updateLimitNote() {
      var limit = readLimit();
      if (limitNote) {
        limitNote.textContent = 'To protect the free recipe quota, this browser has ' + Math.max(0, DAILY_LIMIT - limit.count) + ' of ' + DAILY_LIMIT + ' recipe requests left today.';
      }
    }

    form.addEventListener('submit', function (event) {
      event.preventDefault();
      var limit = readLimit();
      if (limit.count >= DAILY_LIMIT) {
        status.textContent = 'Daily recipe limit reached in this browser.';
        results.innerHTML = '<p class="recipe-ideas-empty">Try again tomorrow, or use the Food Detective notebook and nutrition guides today.</p>';
        updateLimitNote();
        return;
      }

      var ingredientText = ingredients ? ingredients.value.trim() : '';
      if (ingredientText.length < 2) {
        status.textContent = 'Add at least one ingredient first.';
        return;
      }

      status.textContent = 'Generating recipe ideas...';
      results.innerHTML = '<p class="recipe-ideas-empty">Preparing cautious recipe ideas and cooking-video search topics.</p>';

      window.fetch(WEB_API_BASE + '/recipe-suggestions', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          goal: goal ? goal.value : '',
          ingredients: ingredientText,
          avoid: avoid ? avoid.value.trim() : '',
          notes: notes ? notes.value.trim() : ''
        })
      })
        .then(function (response) {
          if (!response.ok) throw new Error('Recipe request failed');
          return response.json();
        })
        .then(function (payload) {
          var recipes = payload && Array.isArray(payload.recipes) ? payload.recipes : [];
          if (!recipes.length) throw new Error('No recipes returned');
          if (!payload.fallback) {
            limit.count += 1;
            writeLimit(limit);
          }
          status.textContent = payload.fallback ? 'Showing fallback recipe ideas.' : 'Generated recipe ideas.';
          results.innerHTML =
            '<p class="recipe-ideas-disclaimer">' + escapeHtml(payload.disclaimer || 'Recipe ideas are educational and are not medical advice.') + '</p>' +
            recipes.map(renderRecipe).join('');
          updateLimitNote();
        })
        .catch(function () {
          status.textContent = 'Recipe helper is unavailable right now.';
          results.innerHTML = '<p class="recipe-ideas-empty">Please try again later. You can still browse nutrition guides and Food Detective notes.</p>';
        });
    });

    updateLimitNote();
  }

  document.addEventListener('DOMContentLoaded', initRecipeIdeas);
})();
