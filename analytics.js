/**
 * IBDPal site analytics: visitors, page views, clicks, and section impressions.
 * Works with Vercel Web Analytics and optional Google Analytics 4.
 */
(function () {
    'use strict';

    var config = window.IBDPAL_ANALYTICS || {};
    var vercelEnabled = config.vercelAnalytics !== false;
    var ga4Id = (config.ga4MeasurementId || '').trim();
    var trackImpressions = config.trackSectionImpressions !== false;
    var impressionThreshold = typeof config.impressionThreshold === 'number'
        ? config.impressionThreshold
        : 0.35;

    var impressionSeen = Object.create(null);

    function pagePath() {
        return window.location.pathname + window.location.search + window.location.hash;
    }

    function pageLabel() {
        return document.title || pagePath();
    }

    function trackEvent(eventName, params) {
        params = params || {};
        params.page_path = params.page_path || pagePath();
        params.page_title = params.page_title || pageLabel();

        if (vercelEnabled && typeof window.va === 'function') {
            window.va('event', { name: eventName, data: params });
        }

        if (ga4Id && typeof window.gtag === 'function') {
            window.gtag('event', eventName, params);
        }

        if (window.location.search.indexOf('analytics_debug=1') !== -1) {
            console.info('[IBDPal analytics]', eventName, params);
        }
    }

    function trackPageView(extra) {
        var payload = Object.assign({
            page_location: window.location.href,
            page_path: pagePath(),
            page_title: pageLabel()
        }, extra || {});

        trackEvent('page_view', payload);

        if (ga4Id && typeof window.gtag === 'function') {
            window.gtag('config', ga4Id, {
                page_path: payload.page_path,
                page_title: payload.page_title
            });
        }
    }

    function loadVercelAnalytics() {
        if (!vercelEnabled) return;
        window.va = window.va || function () {
            (window.vaq = window.vaq || []).push(arguments);
        };
        var script = document.createElement('script');
        script.defer = true;
        script.src = '/_vercel/insights/script.js';
        script.onerror = function () {
            if (window.location.search.indexOf('analytics_debug=1') !== -1) {
                console.warn('[IBDPal analytics] Vercel Insights script failed. Enable Web Analytics in the Vercel project.');
            }
        };
        document.head.appendChild(script);
    }

    function loadGa4() {
        if (!ga4Id) return;
        window.dataLayer = window.dataLayer || [];
        window.gtag = function () {
            window.dataLayer.push(arguments);
        };
        window.gtag('js', new Date());
        window.gtag('config', ga4Id, { send_page_view: false });

        var script = document.createElement('script');
        script.async = true;
        script.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(ga4Id);
        document.head.appendChild(script);
    }

    function linkCategory(anchor) {
        if (anchor.classList.contains('tab-button')) return 'tab_nav';
        if (anchor.closest('.blog-card')) return 'blog_card';
        if (anchor.closest('.blog-share')) return 'blog_share';
        if (anchor.closest('.footer-links')) return 'footer';
        if (anchor.closest('.header-nav')) return 'header_nav';
        if (anchor.closest('.discovery-dashboard')) return 'discovery_dashboard';
        if (anchor.closest('.email-form')) return 'email_form';
        return 'link';
    }

    function trackClick(target) {
        var anchor = target.closest('a[href]');
        var button = target.closest('button');

        if (anchor) {
            var href = anchor.getAttribute('href') || '';
            var isExternal = href.indexOf('http') === 0 &&
                href.indexOf(window.location.hostname) === -1;
            trackEvent('click', {
                link_url: href,
                link_text: (anchor.textContent || '').trim().slice(0, 120),
                link_category: linkCategory(anchor),
                outbound: isExternal ? 'true' : 'false',
                element_id: anchor.id || undefined,
                data_tab: anchor.getAttribute('data-tab') || undefined
            });
            return;
        }

        if (button && button.classList.contains('tab-button')) {
            trackEvent('click', {
                link_category: 'tab_button',
                link_text: (button.textContent || '').trim().slice(0, 120),
                data_tab: button.getAttribute('data-tab') || undefined
            });
        }
    }

    function setupClickTracking() {
        document.addEventListener('click', function (e) {
            var t = e.target;
            if (!t || !t.closest) return;
            if (t.closest('a[href], button.tab-button')) {
                trackClick(t);
            }
        }, { passive: true });
    }

    function setupTabTracking() {
        document.addEventListener('ibdpal:tab', function (e) {
            var tab = e.detail && e.detail.tab;
            if (!tab) return;
            trackEvent('tab_view', {
                tab_id: tab,
                page_path: window.location.pathname + '#' + tab
            });
        });
    }

    function setupEmailTracking() {
        document.addEventListener('ibdpal:email_signup', function () {
            trackEvent('email_signup', { form_id: 'emailForm' });
        });
    }

    function setupImpressionTracking() {
        if (!trackImpressions || !('IntersectionObserver' in window)) return;

        var nodes = document.querySelectorAll('[data-track-impression]');
        if (!nodes.length) return;

        var observer = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (!entry.isIntersecting || entry.intersectionRatio < impressionThreshold) return;
                var el = entry.target;
                var id = el.getAttribute('data-track-impression');
                if (!id || impressionSeen[id]) return;
                impressionSeen[id] = true;
                trackEvent('section_impression', {
                    section_id: id,
                    section_label: el.getAttribute('data-track-label') || id
                });
                observer.unobserve(el);
            });
        }, { threshold: [impressionThreshold, 0.5, 0.75] });

        nodes.forEach(function (node) {
            observer.observe(node);
        });
    }

    function init() {
        loadVercelAnalytics();
        loadGa4();
        trackPageView();
        setupClickTracking();
        setupTabTracking();
        setupEmailTracking();
        setupImpressionTracking();
    }

    window.ibdpalTrack = trackEvent;
    window.ibdpalTrackPageView = trackPageView;

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
