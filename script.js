// IBDPal Website JavaScript

var IBDPAL_MAIN_TABS = ['overview', 'app', 'resources', 'blogs', 'community', 'contact'];
var IBDPAL_APP_SUBTABS = ['features', 'how-it-works', 'screenshots', 'research'];
var IBDPAL_DEFAULT_APP_SUBTAB = 'features';

document.addEventListener('DOMContentLoaded', function () {
    initializeTabNavigation();

    var emailForm = document.getElementById('emailForm');
    if (emailForm) {
        emailForm.addEventListener('submit', function (e) {
            e.preventDefault();
            var email = document.getElementById('email').value;
            if (email) {
                showNotification('Thank you! We\'ll notify you when IBDPal launches.', 'success');
                document.dispatchEvent(new CustomEvent('ibdpal:email_signup'));
                document.getElementById('email').value = '';
            }
        });
    }
});

function resolveTabFromHash(hash) {
    if (!hash) {
        return { main: 'overview', sub: null };
    }
    if (IBDPAL_MAIN_TABS.indexOf(hash) !== -1) {
        return {
            main: hash,
            sub: hash === 'app' ? IBDPAL_DEFAULT_APP_SUBTAB : null
        };
    }
    if (IBDPAL_APP_SUBTABS.indexOf(hash) !== -1) {
        return { main: 'app', sub: hash };
    }
    return { main: 'overview', sub: null };
}

function initializeTabNavigation() {
    var mainTabButtons = document.querySelectorAll('.tab-navigation .tab-button[data-tab]');
    var mainTabContents = document.querySelectorAll('main > .tab-content');
    var appSubButtons = document.querySelectorAll('.app-subtab-button[data-app-subtab]');
    var appSubContents = document.querySelectorAll('.app-subcontent');

    function switchAppSubTab(subTab, updateURL) {
        if (IBDPAL_APP_SUBTABS.indexOf(subTab) === -1) {
            subTab = IBDPAL_DEFAULT_APP_SUBTAB;
        }

        appSubButtons.forEach(function (btn) {
            btn.classList.toggle('active', btn.getAttribute('data-app-subtab') === subTab);
        });
        appSubContents.forEach(function (panel) {
            panel.classList.toggle('active', panel.id === subTab);
        });

        if (updateURL) {
            var newURL = window.location.pathname + '#' + subTab;
            window.history.pushState({ main: 'app', sub: subTab }, '', newURL);
        }

        document.dispatchEvent(new CustomEvent('ibdpal:tab', { detail: { tab: 'app', subTab: subTab } }));
    }

    function switchMainTab(mainTab, subTab, updateURL) {
        if (IBDPAL_MAIN_TABS.indexOf(mainTab) === -1) {
            mainTab = 'overview';
        }

        mainTabButtons.forEach(function (btn) {
            btn.classList.toggle('active', btn.getAttribute('data-tab') === mainTab);
        });
        mainTabContents.forEach(function (content) {
            content.classList.toggle('active', content.id === mainTab);
        });

        if (mainTab === 'app') {
            var targetSub = subTab && IBDPAL_APP_SUBTABS.indexOf(subTab) !== -1
                ? subTab
                : IBDPAL_DEFAULT_APP_SUBTAB;
            switchAppSubTab(targetSub, false);
        }

        if (updateURL) {
            var hash = mainTab === 'overview' ? '' : (mainTab === 'app' ? (subTab || IBDPAL_DEFAULT_APP_SUBTAB) : mainTab);
            var newURL = hash ? window.location.pathname + '#' + hash : window.location.pathname;
            window.history.pushState({ main: mainTab, sub: subTab || null }, '', newURL);
        }

        if (mainTab !== 'app') {
            document.dispatchEvent(new CustomEvent('ibdpal:tab', { detail: { tab: mainTab } }));
        }
    }

    mainTabButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            var mainTab = this.getAttribute('data-tab');
            var subTab = mainTab === 'app' ? IBDPAL_DEFAULT_APP_SUBTAB : null;
            switchMainTab(mainTab, subTab, true);
        });
    });

    appSubButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            var subTab = this.getAttribute('data-app-subtab');
            switchMainTab('app', subTab, true);
        });
    });

    window.addEventListener('popstate', function () {
        var hash = window.location.hash.substring(1);
        var resolved = resolveTabFromHash(hash);
        switchMainTab(resolved.main, resolved.sub, false);
    });

    var hash = window.location.hash.substring(1);
    var initial = resolveTabFromHash(hash);
    switchMainTab(initial.main, initial.sub, false);

    document.querySelectorAll('[data-app-subtab-link]').forEach(function (link) {
        link.addEventListener('click', function (e) {
            var sub = link.getAttribute('data-app-subtab-link');
            if (!sub) return;
            e.preventDefault();
            switchMainTab('app', sub, true);
        });
    });
}

function showNotification(message, type) {
    type = type || 'info';
    var notification = document.createElement('div');
    notification.className = 'notification notification-' + type;
    notification.textContent = message;
    notification.style.cssText =
        'position: fixed; top: 20px; right: 20px; background: ' +
        (type === 'success' ? '#4dcc33' : '#9933cc') +
        '; color: white; padding: 1rem 2rem; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.2); z-index: 1000; font-weight: 500; max-width: 300px; animation: slideIn 0.3s ease-out;';

    if (!document.getElementById('notification-styles')) {
        var style = document.createElement('style');
        style.id = 'notification-styles';
        style.textContent =
            '@keyframes slideIn { from { transform: translateX(100%); opacity: 0; } to { transform: translateX(0); opacity: 1; } }' +
            '@keyframes slideOut { from { transform: translateX(0); opacity: 1; } to { transform: translateX(100%); opacity: 0; } }';
        document.head.appendChild(style);
    }

    document.body.appendChild(notification);
    setTimeout(function () {
        notification.style.animation = 'slideOut 0.3s ease-in';
        setTimeout(function () {
            if (notification.parentNode) {
                notification.parentNode.removeChild(notification);
            }
        }, 300);
    }, 3000);
}

document.addEventListener('DOMContentLoaded', function () {
    var submitButtons = document.querySelectorAll('button[type="submit"]');
    submitButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            var originalText = this.textContent;
            this.style.opacity = '0.7';
            this.textContent = 'Sending...';
            setTimeout(function () {
                button.style.opacity = '1';
                button.textContent = originalText;
            }, 2000);
        });
    });
});

function getBlogShareSummary() {
    var fromBody = document.body && document.body.dataset && document.body.dataset.blogShareText;
    if (fromBody && fromBody.trim()) {
        return fromBody.trim();
    }
    var titleEl = document.querySelector('.blog-title');
    if (titleEl && titleEl.textContent.trim()) {
        return titleEl.textContent.trim();
    }
    return 'Check out this post on IBDPal';
}

function shareOnFacebook(event) {
    event.preventDefault();
    var url = encodeURIComponent(window.location.href);
    window.open('https://www.facebook.com/sharer/sharer.php?u=' + url, '_blank', 'width=600,height=400');
}

function shareOnTwitter(event) {
    event.preventDefault();
    var url = encodeURIComponent(window.location.href);
    var text = encodeURIComponent(getBlogShareSummary());
    window.open('https://twitter.com/intent/tweet?url=' + url + '&text=' + text, '_blank', 'width=600,height=400');
}

function shareViaEmail(event) {
    event.preventDefault();
    var url = window.location.href;
    var subject = encodeURIComponent(document.querySelector('.blog-title')?.textContent?.trim() || 'IBDPal Blog');
    var body = encodeURIComponent(getBlogShareSummary() + '\n\n' + url);
    window.location.href = 'mailto:?subject=' + subject + '&body=' + body;
}
