/**
 * Lightweight fuzzy autocomplete for IBDPal search boxes.
 * Combines curated aliases, resource vocabulary, prefix match, and edit distance.
 */
(function () {
  'use strict';

  var STOP = {
    a: 1, an: 1, the: 1, and: 1, or: 1, of: 1, for: 1, to: 1, in: 1, on: 1, with: 1,
    your: 1, you: 1, from: 1, that: 1, this: 1, are: 1, is: 1, as: 1, at: 1, by: 1,
    what: 1, when: 1, how: 1, why: 1, who: 1, into: 1, about: 1
  };

  var SEED_TERMS = [
    'biologics', 'biologic', 'enteral', 'exclusive enteral nutrition', 'een',
    'fatigue', 'flare', 'diarrhea', 'constipation', 'remission', 'prednisone',
    'steroids', 'mesalamine', 'immunosuppressants', 'humira', 'entyvio',
    'calprotectin', 'anemia', 'iron', 'vitamin d', 'b12', 'gluten', 'dairy',
    'lactose', 'fodmap', 'low residue', 'fiber', 'hydration', 'ostomy',
    'fistula', 'abscess', 'arthritis', 'joint pain', 'uveitis', 'crohn',
    'colitis', 'ulcerative colitis', 'self management', 'newly diagnosed',
    'visit prep', 'infusion', 'vaccine', 'probiotics', 'protein', 'nutrition'
  ];

  var vocabCache = null;

  function normalize(value) {
    return String(value || '')
      .toLowerCase()
      .replace(/[^\w\s'-]/g, ' ')
      .replace(/\s+/g, ' ')
      .trim();
  }

  function titleCase(term) {
    return String(term || '').replace(/\b\w/g, function (ch) {
      return ch.toUpperCase();
    });
  }

  function addTerm(map, term, weight) {
    var n = normalize(term);
    if (!n || n.length < 3 || STOP[n]) return;
    if (!map[n] || map[n] < weight) map[n] = weight;
    n.split(/\s+/).forEach(function (tok) {
      if (tok.length < 4 || STOP[tok]) return;
      if (!map[tok] || map[tok] < weight - 1) map[tok] = weight - 1;
    });
  }

  function buildVocab() {
    if (vocabCache) return vocabCache;
    var map = {};
    SEED_TERMS.forEach(function (term) {
      addTerm(map, term, 8);
    });

    var eng = window.IBDPAL_HOME_ENGAGEMENT;
    if (eng && eng.aliases) {
      Object.keys(eng.aliases).forEach(function (from) {
        // Index canonical targets only; misspellings resolve via alias lookup.
        addTerm(map, eng.aliases[from], 9);
      });
    }

    var resources = window.IBDPAL_RESOURCES || [];
    resources.forEach(function (item) {
      addTerm(map, item.title, 5);
      (item.tags || []).forEach(function (tag) { addTerm(map, tag, 7); });
      (item.keywords || []).forEach(function (kw) { addTerm(map, kw, 8); });
    });

    vocabCache = Object.keys(map).map(function (term) {
      return { term: term, weight: map[term] };
    });
    return vocabCache;
  }

  function levenshtein(a, b) {
    if (a === b) return 0;
    if (!a.length) return b.length;
    if (!b.length) return a.length;
    if (Math.abs(a.length - b.length) > 4) return 99;

    var prev = new Array(b.length + 1);
    var cur = new Array(b.length + 1);
    var i;
    var j;
    for (j = 0; j <= b.length; j++) prev[j] = j;
    for (i = 1; i <= a.length; i++) {
      cur[0] = i;
      for (j = 1; j <= b.length; j++) {
        var cost = a.charCodeAt(i - 1) === b.charCodeAt(j - 1) ? 0 : 1;
        cur[j] = Math.min(cur[j - 1] + 1, prev[j] + 1, prev[j - 1] + cost);
      }
      var tmp = prev;
      prev = cur;
      cur = tmp;
    }
    return prev[b.length];
  }

  function maxDistance(len) {
    if (len <= 4) return 1;
    if (len <= 7) return 2;
    if (len <= 11) return 3;
    return 4;
  }

  function resolveAlias(query) {
    var q = normalize(query);
    var eng = window.IBDPAL_HOME_ENGAGEMENT;
    if (eng && typeof eng.suggestAlias === 'function') {
      var viaFn = eng.suggestAlias(q);
      if (viaFn && viaFn !== q) return viaFn;
    }
    if (eng && eng.aliases && eng.aliases[q] && eng.aliases[q] !== q) {
      return normalize(eng.aliases[q]);
    }
    return null;
  }

  /**
   * Rank vocabulary completions for a typed query.
   * Returns [{ term, label, score, reason }]
   */
  function completions(query, limit) {
    var q = normalize(query);
    if (q.length < 2) return [];
    limit = limit || 6;
    var vocab = buildVocab();
    var scored = [];

    var alias = resolveAlias(q);
    if (alias) {
      scored.push({ term: alias, label: titleCase(alias), score: 1000, reason: 'alias' });
    }

    vocab.forEach(function (row) {
      var term = row.term;
      var score = 0;
      var reason = '';

      if (term === q) {
        score = 900 + row.weight;
        reason = 'exact';
      } else if (term.indexOf(q) === 0) {
        // Prefix autocomplete: biolog -> biologics
        score = 700 + row.weight * 10 - (term.length - q.length);
        reason = 'prefix';
      } else if (q.length >= 4 && term.indexOf(q) !== -1) {
        score = 500 + row.weight;
        reason = 'contains';
      } else if (q.length >= 4) {
        var dist = levenshtein(q, term);
        var allowed = maxDistance(Math.max(q.length, term.length));
        if (dist <= allowed) {
          // Prefer shared stems (biolog*)
          var shared = 0;
          var maxShare = Math.min(q.length, term.length, 6);
          while (shared < maxShare && q.charAt(shared) === term.charAt(shared)) shared += 1;
          // Prefer common clinical plurals/canonical forms when close.
          var canonicalBoost = /ics$|itis$|osis$|tion$/.test(term) ? 25 : 0;
          score = 400 - dist * 40 + shared * 15 + row.weight + canonicalBoost;
          reason = 'fuzzy';
        }
      }

      if (score > 0) {
        scored.push({ term: term, label: titleCase(term), score: score, reason: reason });
      }
    });

    scored.sort(function (a, b) {
      return b.score - a.score || a.term.length - b.term.length;
    });

    var seen = {};
    var out = [];
    for (var i = 0; i < scored.length && out.length < limit; i++) {
      var item = scored[i];
      if (seen[item.term]) continue;
      if (item.term === q && item.reason === 'exact') continue;
      seen[item.term] = true;
      out.push(item);
    }
    return out;
  }

  /** Best single correction for a misspelled/partial query. */
  function bestCorrection(query) {
    var list = completions(query, 1);
    return list.length ? list[0].term : null;
  }

  /** Expand a query with corrections for ranking content. */
  function expandQuery(query) {
    var q = normalize(query);
    var terms = [q];
    var corr = bestCorrection(q);
    if (corr && corr !== q) terms.push(corr);
    completions(q, 4).forEach(function (item) {
      if (terms.indexOf(item.term) === -1) terms.push(item.term);
    });
    return terms;
  }

  function invalidate() {
    vocabCache = null;
  }

  window.IBDPAL_SEARCH_FUZZY = {
    completions: completions,
    bestCorrection: bestCorrection,
    expandQuery: expandQuery,
    invalidate: invalidate,
    normalize: normalize
  };
})();
