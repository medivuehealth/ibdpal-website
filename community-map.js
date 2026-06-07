/**
 * Interactive U.S. map for Community tab (D3 + us-atlas).
 */
(function () {
  'use strict';

  var MAP_URL = 'https://cdn.jsdelivr.net/npm/us-atlas@3/states-10m.json';
  var FIPS_TO_ABBR = {
    '01': 'AL', '02': 'AK', '04': 'AZ', '05': 'AR', '06': 'CA', '08': 'CO', '09': 'CT',
    '10': 'DE', '11': 'DC', '12': 'FL', '13': 'GA', '15': 'HI', '16': 'ID', '17': 'IL',
    '18': 'IN', '19': 'IA', '20': 'KS', '21': 'KY', '22': 'LA', '23': 'ME', '24': 'MD',
    '25': 'MA', '26': 'MI', '27': 'MN', '28': 'MS', '29': 'MO', '30': 'MT', '31': 'NE',
    '32': 'NV', '33': 'NH', '34': 'NJ', '35': 'NM', '36': 'NY', '37': 'NC', '38': 'ND',
    '39': 'OH', '40': 'OK', '41': 'OR', '42': 'PA', '44': 'RI', '45': 'SC', '46': 'SD',
    '47': 'TN', '48': 'TX', '49': 'UT', '50': 'VT', '51': 'VA', '53': 'WA', '54': 'WV',
    '55': 'WI', '56': 'WY'
  };

  var STATE_NAMES = {
    AL: 'Alabama', AK: 'Alaska', AZ: 'Arizona', AR: 'Arkansas', CA: 'California',
    CO: 'Colorado', CT: 'Connecticut', DE: 'Delaware', DC: 'District of Columbia',
    FL: 'Florida', GA: 'Georgia', HI: 'Hawaii', ID: 'Idaho', IL: 'Illinois',
    IN: 'Indiana', IA: 'Iowa', KS: 'Kansas', KY: 'Kentucky', LA: 'Louisiana',
    ME: 'Maine', MD: 'Maryland', MA: 'Massachusetts', MI: 'Michigan', MN: 'Minnesota',
    MS: 'Mississippi', MO: 'Missouri', MT: 'Montana', NE: 'Nebraska', NV: 'Nevada',
    NH: 'New Hampshire', NJ: 'New Jersey', NM: 'New Mexico', NY: 'New York',
    NC: 'North Carolina', ND: 'North Dakota', OH: 'Ohio', OK: 'Oklahoma', OR: 'Oregon',
    PA: 'Pennsylvania', RI: 'Rhode Island', SC: 'South Carolina', SD: 'South Dakota',
    TN: 'Tennessee', TX: 'Texas', UT: 'Utah', VT: 'Vermont', VA: 'Virginia',
    WA: 'Washington', WV: 'West Virginia', WI: 'Wisconsin', WY: 'Wyoming'
  };

  var mapBuilt = false;
  var mapBuildInProgress = false;
  var selectedAbbr = null;
  var stateSelectReady = false;
  var zipSearchReady = false;

  function escapeHtml(s) {
    if (!s) return '';
    return String(s)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function linkOrText(url, label) {
    if (!url) return escapeHtml(label || '');
    return '<a href="' + escapeHtml(url) + '" target="_blank" rel="noopener noreferrer">' + escapeHtml(label || url) + '</a>';
  }

  function renderResourceCard(r) {
    var parts = [
      '<article class="community-resource-card">',
      '<h4 class="community-resource-card__title">' + escapeHtml(r.name) + '</h4>'
    ];
    if (r.type) {
      parts.push('<p class="community-resource-card__type">' + escapeHtml(r.type) + '</p>');
    }
    if (r.notes) {
      parts.push('<p class="community-resource-card__notes">' + escapeHtml(r.notes) + '</p>');
    }
    parts.push('<ul class="community-resource-card__meta">');
    if (r.website) {
      parts.push('<li><strong>Website:</strong> ' + linkOrText(r.website, r.website.replace(/^https?:\/\//, '')) + '</li>');
    }
    if (r.phone) {
      var tel = r.phone.replace(/[^\d+]/g, '');
      parts.push('<li><strong>Phone:</strong> <a href="tel:' + escapeHtml(tel) + '">' + escapeHtml(r.phoneLabel || r.phone) + '</a></li>');
    }
    if (r.email) {
      parts.push('<li><strong>Email:</strong> <a href="mailto:' + escapeHtml(r.email) + '">' + escapeHtml(r.email) + '</a></li>');
    }
    if (r.address) {
      parts.push('<li><strong>Address:</strong> ' + escapeHtml(r.address) + '</li>');
    }
    parts.push('</ul></article>');
    return parts.join('');
  }

  function renderPanel(abbr) {
    var panel = document.getElementById('community-detail');
    var data = window.IBDPAL_COMMUNITY;
    if (!panel || !data) return;

    selectedAbbr = abbr;
    var state = data.states[abbr];
    var stateName = STATE_NAMES[abbr] || abbr;
    var html = '';

    document.querySelectorAll('.community-map-svg .state').forEach(function (el) {
      el.classList.toggle('is-selected', el.getAttribute('data-state') === abbr);
    });

    var select = document.getElementById('community-state-select');
    if (select) select.value = abbr;

    if (state && state.resources && state.resources.length) {
      html += '<h3 class="community-detail__title">' + escapeHtml(state.name || stateName) + '</h3>';
      html += '<p class="community-detail__intro">Organizations and programs that support people with Crohn’s disease, ulcerative colitis, and related conditions. Listing is for information only, not an endorsement.</p>';
      if (state.ccfChapter) {
        html += '<div class="community-chapter-banner">';
        html += '<p><strong>Local Crohn’s &amp; Colitis Foundation chapter:</strong> ' + escapeHtml(state.ccfChapter.name) + '</p>';
        if (state.ccfChapter.serves) {
          html += '<p class="community-chapter-banner__serves">Serves: ' + escapeHtml(state.ccfChapter.serves) + '</p>';
        }
        html += '</div>';
      }
      html += '<div class="community-resource-list">';
      state.resources.forEach(function (r) {
        html += renderResourceCard(r);
      });
      html += '</div>';
    } else {
      var hint = data.stateChapterHints && data.stateChapterHints[abbr];
      html += '<h3 class="community-detail__title">' + escapeHtml(stateName) + '</h3>';
      html += '<p class="community-detail__intro">Detailed local listings are coming soon for this state. Use the national resources below and the Crohn’s &amp; Colitis Foundation chapter finder for programs near you.</p>';
      if (hint) {
        html += '<p class="community-detail__hint"><strong>Typical CCF chapter for this area:</strong> ' + escapeHtml(hint) + '. <a href="' + escapeHtml(data.defaultChapterUrl) + '" target="_blank" rel="noopener noreferrer">View all chapters</a>.</p>';
      }
      html += '<div class="community-resource-list">';
      data.national.resources.forEach(function (r) {
        html += renderResourceCard(r);
      });
      html += '</div>';
    }

    panel.innerHTML = html;
    panel.scrollIntoView({ behavior: 'smooth', block: 'nearest' });

    if (typeof window.ibdpalTrack === 'function') {
      window.ibdpalTrack('community_state_select', { state: abbr });
    }
  }

  function lookupZip(zip) {
    var prefix = String(zip).replace(/\D/g, '').slice(0, 3);
    if (prefix.length < 3) return null;
    return window.IBDPAL_ZIP_PREFIX && window.IBDPAL_ZIP_PREFIX[prefix];
  }

  function buildZipSearch() {
    var input = document.getElementById('community-zip-input');
    var btn = document.getElementById('community-zip-btn');
    if (!input || !btn || zipSearchReady) return;
    zipSearchReady = true;
    function go() {
      var abbr = lookupZip(input.value);
      if (abbr) {
        renderPanel(abbr);
        input.setAttribute('aria-invalid', 'false');
      } else {
        input.setAttribute('aria-invalid', 'true');
        var panel = document.getElementById('community-detail');
        if (panel) {
          panel.innerHTML = '<p class="community-detail__intro">Enter a valid 5-digit U.S. ZIP code to jump to your state.</p>';
        }
      }
    }
    btn.addEventListener('click', go);
    input.addEventListener('keydown', function (e) {
      if (e.key === 'Enter') {
        e.preventDefault();
        go();
      }
    });
  }

  function buildStateSelect() {
    var select = document.getElementById('community-state-select');
    if (!select || stateSelectReady) return;
    stateSelectReady = true;
    var opts = ['<option value="">Select a state…</option>'];
    Object.keys(STATE_NAMES).sort(function (a, b) {
      return STATE_NAMES[a].localeCompare(STATE_NAMES[b]);
    }).forEach(function (abbr) {
      opts.push('<option value="' + abbr + '">' + escapeHtml(STATE_NAMES[abbr]) + '</option>');
    });
    select.innerHTML = opts.join('');
    select.addEventListener('change', function () {
      if (select.value) renderPanel(select.value);
    });
  }

  function buildMap() {
    var container = document.getElementById('community-map');
    if (!container) return;
    if (container.querySelector('.community-map-svg')) {
      mapBuilt = true;
      return;
    }
    if (mapBuilt || mapBuildInProgress) return;
    if (typeof d3 === 'undefined' || typeof topojson === 'undefined') {
      if (!container.querySelector('.community-map-fallback')) {
        container.innerHTML = '<p class="community-map-fallback">Map loading… If this persists, use the state dropdown.</p>';
      }
      return;
    }

    mapBuildInProgress = true;
    container.innerHTML = '';

    var width = 960;
    var height = 600;
    var svg = d3.select(container).append('svg')
      .attr('viewBox', '0 0 ' + width + ' ' + height)
      .attr('class', 'community-map-svg')
      .attr('role', 'img')
      .attr('aria-label', 'Map of the United States. Click a state to view IBD support resources.');

    var projection = d3.geoAlbersUsa().scale(1280).translate([width / 2, height / 2]);
    var path = d3.geoPath().projection(projection);

    fetch(MAP_URL)
      .then(function (res) { return res.json(); })
      .then(function (us) {
        var states = topojson.feature(us, us.objects.states).features;
        svg.append('g')
          .attr('class', 'states-layer')
          .selectAll('path')
          .data(states)
          .enter()
          .append('path')
          .attr('class', 'state')
          .attr('d', path)
          .attr('data-state', function (d) { return FIPS_TO_ABBR[d.id]; })
          .attr('tabindex', '0')
          .attr('role', 'button')
          .attr('aria-label', function (d) {
            var abbr = FIPS_TO_ABBR[d.id];
            return (STATE_NAMES[abbr] || abbr) + '. Click for IBD community resources.';
          })
          .on('click', function (event, d) {
            var abbr = FIPS_TO_ABBR[d.id];
            if (abbr) renderPanel(abbr);
          })
          .on('keydown', function (event, d) {
            if (event.key === 'Enter' || event.key === ' ') {
              event.preventDefault();
              var abbr = FIPS_TO_ABBR[d.id];
              if (abbr) renderPanel(abbr);
            }
          });

        mapBuilt = true;
        mapBuildInProgress = false;
        renderPanel('NC');
      })
      .catch(function () {
        mapBuildInProgress = false;
        container.innerHTML = '<p class="community-map-fallback">Could not load map. Please use the state dropdown below.</p>';
        renderPanel('NC');
      });
  }

  function whenLibsReady(fn) {
    function tick() {
      if (typeof d3 !== 'undefined' && typeof topojson !== 'undefined') {
        fn();
      } else {
        setTimeout(tick, 50);
      }
    }
    tick();
  }

  function init() {
    buildStateSelect();
    buildZipSearch();
    whenLibsReady(buildMap);
  }

  document.addEventListener('DOMContentLoaded', init);
  document.addEventListener('ibdpal:tab', function (e) {
    if (e.detail && e.detail.tab === 'community') {
      whenLibsReady(function () {
        buildMap();
        if (mapBuilt && !selectedAbbr) renderPanel('NC');
      });
    }
  });
})();
