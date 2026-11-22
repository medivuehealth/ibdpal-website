/* Interactive month navigator for /ibd-awareness-calendar */
(function () {
  "use strict";

  var data = window.IBDPAL_AWARENESS_CALENDAR;
  if (!data || !data.months || !data.months.length) return;

  var root = document.getElementById("iac-root");
  if (!root) return;

  var year = data.year || new Date().getFullYear();
  var months = data.months;
  var byMonth = {};
  months.forEach(function (m) {
    byMonth[m.month] = m;
  });

  var labelEl = root.querySelector("[data-iac-month-label]");
  var gridEl = root.querySelector("[data-iac-grid]");
  var panelEl = root.querySelector("[data-iac-panel]");
  var prevBtn = root.querySelector("[data-iac-prev]");
  var nextBtn = root.querySelector("[data-iac-next]");
  var liveEl = root.querySelector("[data-iac-live]");
  var jumpBtns = root.querySelectorAll("[data-iac-jump]");

  var now = new Date();
  var viewMonth =
    now.getFullYear() === year ? now.getMonth() + 1 : months[0].month;
  if (!byMonth[viewMonth]) viewMonth = 5;
  var selectedDay = null;
  var syncingHash = false;

  function daysInMonth(y, m) {
    return new Date(y, m, 0).getDate();
  }

  function firstWeekday(y, m) {
    return new Date(y, m - 1, 1).getDay();
  }

  function escapeHtml(s) {
    return String(s || "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function linkList(items, external) {
    if (!items || !items.length) return "";
    return (
      '<ul class="seo-landing__list">' +
      items
        .map(function (item) {
          var rel =
            external || String(item.url || "").indexOf("http") === 0
              ? ' rel="noopener noreferrer"'
              : "";
          return (
            "<li><a href=\"" +
            escapeHtml(item.url) +
            "\"" +
            rel +
            ">" +
            escapeHtml(item.label) +
            "</a></li>"
          );
        })
        .join("") +
      "</ul>"
    );
  }

  function marksFor(monthNum) {
    var m = byMonth[monthNum] || {};
    return m.day_marks || { theme: false, peak_days: [], peak_label: "" };
  }

  function isPeak(monthNum, day) {
    var peaks = marksFor(monthNum).peak_days || [];
    return peaks.indexOf(day) !== -1;
  }

  function isTheme(monthNum, day) {
    var marks = marksFor(monthNum);
    if (isPeak(monthNum, day)) return false;
    return !!marks.theme;
  }

  function defaultSelectedDay(monthNum) {
    var peaks = marksFor(monthNum).peak_days || [];
    if (peaks.length) return peaks[0];
    if (
      now.getFullYear() === year &&
      now.getMonth() + 1 === monthNum
    ) {
      return now.getDate();
    }
    return 1;
  }

  function keepCalendarInView() {
    if (!root.getBoundingClientRect) return;
    var rect = root.getBoundingClientRect();
    if (rect.top < 0 || rect.top > window.innerHeight * 0.35) {
      root.scrollIntoView({ block: "start", behavior: "smooth" });
    }
  }

  function updateJumpActive() {
    jumpBtns.forEach(function (btn) {
      var m = Number(btn.getAttribute("data-iac-jump"));
      btn.classList.toggle("is-active", m === viewMonth);
      btn.setAttribute("aria-pressed", m === viewMonth ? "true" : "false");
    });
  }

  function writeHash(monthNum) {
    var next = "#m-" + String(monthNum).padStart(2, "0");
    if ((location.hash || "") === next) return;
    syncingHash = true;
    try {
      history.replaceState(null, "", next);
    } catch (e) {}
    syncingHash = false;
  }

  function monthFromHash() {
    var raw = (location.hash || "").replace(/^#/, "");
    var match = raw.match(/^(?:m-|month-)?(\d{1,2})$/i);
    if (!match) return null;
    var hashMonth = parseInt(match[1], 10);
    if (hashMonth >= 1 && hashMonth <= 12 && byMonth[hashMonth]) {
      return hashMonth;
    }
    return null;
  }

  function renderGrid() {
    var m = byMonth[viewMonth];
    var total = daysInMonth(year, viewMonth);
    var start = firstWeekday(year, viewMonth);
    var html = [];
    var i;
    for (i = 0; i < start; i += 1) {
      html.push(
        '<button type="button" class="iac__day iac__day--empty" tabindex="-1" aria-hidden="true"></button>'
      );
    }
    for (i = 1; i <= total; i += 1) {
      var classes = ["iac__day"];
      var label = String(i);
      if (isPeak(viewMonth, i)) {
        classes.push("iac__day--peak");
        label += ", event day";
      } else if (isTheme(viewMonth, i)) {
        classes.push("iac__day--theme");
        label += ", awareness theme day";
      }
      if (
        now.getFullYear() === year &&
        now.getMonth() + 1 === viewMonth &&
        now.getDate() === i
      ) {
        classes.push("iac__day--today");
      }
      if (selectedDay === i) classes.push("iac__day--selected");
      html.push(
        '<button type="button" class="' +
          classes.join(" ") +
          '" data-day="' +
          i +
          '" aria-label="' +
          escapeHtml(label) +
          '"' +
          (selectedDay === i ? ' aria-pressed="true"' : ' aria-pressed="false"') +
          ">" +
          i +
          "</button>"
      );
    }
    gridEl.innerHTML = html.join("");
    labelEl.textContent = m.name + " " + year;
    prevBtn.disabled = viewMonth <= 1;
    nextBtn.disabled = viewMonth >= 12;
    updateJumpActive();
    if (liveEl) {
      liveEl.textContent = "Showing " + m.name + " " + year;
    }
  }

  function renderPanel() {
    var m = byMonth[viewMonth];
    var marks = marksFor(viewMonth);
    var peakHit =
      selectedDay && isPeak(viewMonth, selectedDay)
        ? marks.peak_label || m.event
        : "";
    var kicker = m.major
      ? m.campaign_label || "Major campaign"
      : "Monthly awareness feature";
    var title = peakHit || m.event;
    var dayLine = "";
    if (selectedDay && isPeak(viewMonth, selectedDay)) {
      dayLine =
        "<p class=\"iac__panel-meta\"><strong>Highlighted day:</strong> " +
        escapeHtml(m.name) +
        " " +
        selectedDay +
        "</p>";
    } else if (marks.peak_days && marks.peak_days.length) {
      dayLine =
        "<p class=\"iac__panel-meta\"><strong>Key dates:</strong> " +
        escapeHtml(marks.peak_label || "Event days") +
        " · " +
        marks.peak_days.join(", ") +
        "</p>";
    } else if (marks.theme) {
      dayLine =
        "<p class=\"iac__panel-meta\">Month-long theme · every day is lightly marked</p>";
    }

    var highlights = "";
    if (m.highlight_dates && m.highlight_dates.length) {
      highlights =
        "<ul class=\"seo-landing__list\">" +
        m.highlight_dates
          .map(function (h) {
            return (
              "<li><strong>" +
              escapeHtml(h.label) +
              ":</strong> " +
              escapeHtml(h.date) +
              "</li>"
            );
          })
          .join("") +
        "</ul>";
    }

    var note = m.campaign_note
      ? '<p class="iac__panel-note">' + escapeHtml(m.campaign_note) + "</p>"
      : "";

    panelEl.classList.remove("is-updating");
    void panelEl.offsetWidth;
    panelEl.classList.add("is-updating");
    panelEl.innerHTML =
      '<p class="iac__panel-kicker">' +
      escapeHtml(kicker) +
      "</p>" +
      '<h3 class="iac__panel-title">' +
      escapeHtml(title) +
      "</h3>" +
      dayLine +
      '<p class="iac__panel-body">' +
      escapeHtml(m.relevance) +
      "</p>" +
      highlights +
      (m.external && m.external.length
        ? "<p><strong>Official links</strong></p>" + linkList(m.external, true)
        : "") +
      "<p><strong>IBDPal resources</strong></p>" +
      linkList(m.links || []) +
      note;
  }

  function setMonth(monthNum, keepDay, scroll) {
    viewMonth = monthNum;
    selectedDay = keepDay ? selectedDay : defaultSelectedDay(viewMonth);
    if (selectedDay > daysInMonth(year, viewMonth)) {
      selectedDay = defaultSelectedDay(viewMonth);
    }
    renderGrid();
    renderPanel();
    writeHash(viewMonth);
    if (scroll) keepCalendarInView();
  }

  prevBtn.addEventListener("click", function () {
    if (viewMonth > 1) setMonth(viewMonth - 1, false, true);
  });
  nextBtn.addEventListener("click", function () {
    if (viewMonth < 12) setMonth(viewMonth + 1, false, true);
  });

  jumpBtns.forEach(function (btn) {
    btn.addEventListener("click", function () {
      var m = Number(btn.getAttribute("data-iac-jump"));
      if (byMonth[m]) setMonth(m, false, true);
    });
  });

  gridEl.addEventListener("click", function (evt) {
    var btn = evt.target.closest("[data-day]");
    if (!btn || btn.classList.contains("iac__day--empty")) return;
    selectedDay = Number(btn.getAttribute("data-day"));
    renderGrid();
    renderPanel();
  });

  root.addEventListener("keydown", function (evt) {
    if (evt.key === "ArrowLeft" && !prevBtn.disabled) {
      evt.preventDefault();
      setMonth(viewMonth - 1, false, true);
    } else if (evt.key === "ArrowRight" && !nextBtn.disabled) {
      evt.preventDefault();
      setMonth(viewMonth + 1, false, true);
    }
  });

  window.addEventListener("hashchange", function () {
    if (syncingHash) return;
    var m = monthFromHash();
    if (m && m !== viewMonth) setMonth(m, false, true);
  });

  var fromHash = monthFromHash();
  if (fromHash) viewMonth = fromHash;
  selectedDay = defaultSelectedDay(viewMonth);
  setMonth(viewMonth, true, false);

  // Old bookmarks used #month-11 and scrolled past the calendar; pin view to grid.
  if (fromHash || (location.hash || "").indexOf("month-") === 1) {
    keepCalendarInView();
  }
})();
