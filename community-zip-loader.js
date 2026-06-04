(function () {
  'use strict';
  fetch('/assets/zip-prefix-state.json')
    .then(function (r) { return r.json(); })
    .then(function (data) { window.IBDPAL_ZIP_PREFIX = data; })
    .catch(function () { window.IBDPAL_ZIP_PREFIX = {}; });
})();
