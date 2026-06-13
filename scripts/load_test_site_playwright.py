#!/usr/bin/env python3
"""Browser load test for ibdpal.org — real clicks, search, tabs (feeds Vercel Analytics)."""
from __future__ import annotations

import argparse
import asyncio
import json
import os
import random
import statistics
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
from urllib.parse import urlparse
from urllib.error import URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "scripts") not in sys.path:
    sys.path.insert(0, str(ROOT / "scripts"))

from load_test_site import (  # noqa: E402
    DEFAULT_BASE,
    SEARCH_TERMS,
    parse_resource_urls,
    parse_sitemap_paths,
)

try:
    from playwright.async_api import Browser, Page, async_playwright
except ImportError:
    print("Playwright is required: pip install playwright && playwright install chromium")
    raise

MAIN_TABS = ["app", "resources", "research", "blogs", "community", "overview"]
APP_SUBTABS = ["features", "how-it-works", "screenshots"]
HUB_PATHS = ["/ibd-nutrition", "/flare-help", "/crohns-disease", "/ulcerative-colitis"]
TOPIC_ARTICLES = [
    "/blog/dairy-lactose-ibd",
    "/blog/gluten-wheat-ibd",
    "/blog/immunosuppressants-ibd-basics",
]
US_STATES = ["NC", "CA", "TX", "NY", "FL", "IL", "PA", "OH", "GA", "WA"]
# Standalone pages not already visited in hub/topic flows
EXTRA_NAV_PAGES = ["/guides", "/glossary", "/research", "/blog"]
# Normal Chrome UA — avoid generic automation signatures in analytics
CHROME_USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)
STEALTH_INIT_SCRIPT = """
Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
window.chrome = window.chrome || { runtime: {} };
"""
DEFAULT_PROXIES_FILE = ROOT / "load-test-proxies.txt"
PROXY_ROTATE_PLACEHOLDERS = ("{session}", "{user}", "{uid}")


@dataclass
class ProxyPlan:
    """How egress IPs are assigned across virtual users."""

    mode: str  # none | list | rotate
    entries: list[str] = field(default_factory=list)
    rotate_template: str = ""

    def for_user(self, user_id: int) -> dict[str, str] | None:
        if self.mode == "rotate" and self.rotate_template:
            url = self.rotate_template
            for token in PROXY_ROTATE_PLACEHOLDERS:
                url = url.replace(token, str(user_id))
            return parse_proxy_url(url)
        if self.mode == "list" and self.entries:
            if user_id < len(self.entries):
                return parse_proxy_url(self.entries[user_id])
            return parse_proxy_url(self.entries[user_id % len(self.entries)])
        return None

    def describe(self) -> str:
        if self.mode == "rotate":
            return f"rotating ({self.rotate_template[:60]}...)"
        if self.mode == "list":
            return f"{len(self.entries)} proxies (1 per user when count >= users)"
        return "none (all users share your machine IP)"


def parse_proxy_url(raw: str) -> dict[str, str]:
    """Playwright proxy dict from http(s)/socks5 URL."""
    url = raw.strip()
    if not url:
        raise ValueError("empty proxy URL")
    parsed = urlparse(url)
    if not parsed.hostname or not parsed.scheme:
        raise ValueError(f"invalid proxy URL: {raw}")
    port = parsed.port or (1080 if parsed.scheme.startswith("socks") else 8080)
    proxy: dict[str, str] = {"server": f"{parsed.scheme}://{parsed.hostname}:{port}"}
    if parsed.username:
        proxy["username"] = parsed.username
    if parsed.password:
        proxy["password"] = parsed.password
    return proxy


def webshare_line_to_url(line: str) -> str:
    parts = line.strip().split(":")
    if len(parts) < 4:
        raise ValueError(f"invalid webshare line: {line[:80]}")
    host, port, user = parts[0], parts[1], parts[2]
    password = ":".join(parts[3:])
    from urllib.parse import quote

    return f"http://{quote(user, safe='')}:{quote(password, safe='')}@{host}:{port}"


def fetch_webshare_proxies(download_url: str, timeout: float = 60.0) -> list[str]:
    import ssl as _ssl
    from urllib.request import Request, urlopen

    req = Request(download_url, headers={"User-Agent": "IBDPalProxyFetch/1.0"})
    try:
        ctx = _ssl.create_default_context()
        with urlopen(req, context=ctx, timeout=timeout) as resp:
            body = resp.read().decode("utf-8", errors="replace")
    except (_ssl.SSLError, URLError):
        with urlopen(req, context=_ssl._create_unverified_context(), timeout=timeout) as resp:
            body = resp.read().decode("utf-8", errors="replace")

    if not body.strip() or body.lstrip().startswith("{"):
        raise ValueError("Webshare download returned no proxy list")
    urls: list[str] = []
    for line in body.splitlines():
        line = line.strip()
        if line:
            urls.append(webshare_line_to_url(line))
    if not urls:
        raise ValueError("Webshare download contained zero proxies")
    return urls


def load_proxy_plan(
    proxies_file: Path | None,
    rotate_template: str,
    webshare_url: str = "",
) -> ProxyPlan:
    rotate_template = (rotate_template or os.environ.get("IBDPAL_PROXY_ROTATE", "")).strip()
    if rotate_template:
        parse_proxy_url(rotate_template.replace("{session}", "0"))
        return ProxyPlan(mode="rotate", rotate_template=rotate_template)

    entries: list[str] = []

    path = proxies_file or DEFAULT_PROXIES_FILE
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "://" not in line and line.count(":") >= 3:
                line = webshare_line_to_url(line)
            entries.append(line)

    if not entries:
        webshare = (webshare_url or os.environ.get("WEBSHARE_DOWNLOAD_URL", "")).strip()
        if webshare:
            entries.extend(fetch_webshare_proxies(webshare))

    env_list = os.environ.get("IBDPAL_LOAD_TEST_PROXIES", "").strip()
    if env_list and not entries:
        entries.extend(p.strip() for p in env_list.split(",") if p.strip())

    if entries:
        for entry in entries:
            parse_proxy_url(entry)
        return ProxyPlan(mode="list", entries=entries)
    return ProxyPlan(mode="none")


@dataclass
class StepResult:
    scenario: str
    ok: bool
    latency_ms: float
    detail: str = ""
    user_id: int = -1


@dataclass
class UserSessionReport:
    user_id: int
    steps: list[StepResult] = field(default_factory=list)
    vercel_beacons: int = 0
    vercel_beacons_ok: int = 0
    page_views_tracked: int = 0
    clicks_tracked: int = 0
    analytics_events_total: int = 0
    egress_ip: str = ""
    egress_country: str = ""
    proxy_server: str = ""
    errors: list[str] = field(default_factory=list)

    @property
    def successes(self) -> int:
        return sum(1 for s in self.steps if s.ok)

    @property
    def failures(self) -> int:
        return sum(1 for s in self.steps if not s.ok)


@dataclass
class PlaywrightLoadReport:
    base_url: str
    concurrency: int
    started_at: str
    duration_sec: float
    total_steps: int
    step_successes: int
    step_failures: int
    sessions_completed: int
    sessions_failed: int
    vercel_beacons_total: int
    vercel_beacons_ok: int
    analytics_events_total: int
    workers: int
    proxy_mode: str
    unique_egress_ips: int
    unique_egress_countries: int
    latency_ms: dict[str, float]
    scenario_counts: dict[str, int]
    scenario_failures: dict[str, int]
    errors_sample: list[dict[str, Any]]


async def timed_step(
    user_id: int,
    scenario: str,
    fn,
) -> StepResult:
    start = time.perf_counter()
    try:
        detail = await fn()
        elapsed = (time.perf_counter() - start) * 1000
        return StepResult(scenario=scenario, ok=True, latency_ms=elapsed, detail=detail or "", user_id=user_id)
    except Exception as exc:  # noqa: BLE001 — load test should capture all step errors
        elapsed = (time.perf_counter() - start) * 1000
        return StepResult(scenario=scenario, ok=False, latency_ms=elapsed, detail=str(exc), user_id=user_id)


async def click_tab(page: Page, tab_id: str) -> None:
    btn = page.locator(f'.tab-navigation .tab-button[data-tab="{tab_id}"]')
    await btn.wait_for(state="visible", timeout=15_000)
    await btn.click()
    await page.locator(f".tab-content#{tab_id}.active").wait_for(state="visible", timeout=10_000)


async def safe_goto(page: Page, url: str, timeout_ms: int, retries: int = 3) -> None:
    last_err: Exception | None = None
    for attempt in range(retries):
        try:
            await page.goto(url, wait_until="domcontentloaded", timeout=timeout_ms)
            return
        except Exception as exc:  # noqa: BLE001
            last_err = exc
            await page.wait_for_timeout(400 * (attempt + 1))
    raise last_err or RuntimeError(f"goto failed: {url}")


async def click_first_visible(page: Page, selector: str, timeout_ms: int = 10_000) -> str:
    """Click the first element matching selector that is actually visible (not filter-hidden)."""
    loc = page.locator(selector)
    deadline = time.perf_counter() + timeout_ms / 1000
    while time.perf_counter() < deadline:
        count = await loc.count()
        for i in range(count):
            item = loc.nth(i)
            if await item.is_visible():
                tag = await item.evaluate("el => el.tagName")
                href = await item.get_attribute("href") if tag == "A" else None
                await item.click()
                return href or selector
        await page.wait_for_timeout(200)
    raise TimeoutError(f"No visible element for {selector}")


async def fetch_egress_geo(page: Page) -> tuple[str, str]:
    """Return (ip, countryCode) for the current browser egress (via proxy if set)."""
    try:
        resp = await page.goto(
            "http://ip-api.com/json/?fields=query,countryCode,status",
            wait_until="commit",
            timeout=20_000,
        )
        if not resp or not resp.ok:
            return "", ""
        data = await resp.json()
        if data.get("status") != "success":
            return "", ""
        return str(data.get("query") or ""), str(data.get("countryCode") or "")
    except Exception:
        return "", ""


async def fetch_egress_ip(page: Page) -> str:
    ip, _ = await fetch_egress_geo(page)
    return ip


async def wait_for_vercel_analytics(page: Page, timeout_ms: int = 20_000) -> None:
    await page.wait_for_function(
        "() => typeof window.va === 'function' || (window.vaq && window.vaq.length)",
        timeout=timeout_ms,
    )


async def flush_analytics(page: Page, seconds: float = 8.0) -> None:
    """Give /_vercel/insights/ beacons time to POST before closing the browser."""
    await page.wait_for_timeout(int(seconds * 1000))


async def allow_vercel_insights_routes(context) -> None:
    """Never block /_vercel/insights/ analytics beacons."""

    async def _continue(route) -> None:
        await route.continue_()

    await context.route("**/_vercel/insights/**", _continue)


async def run_user_session(
    browser: Browser,
    base_url: str,
    user_id: int,
    sitemap_paths: list[str],
    resource_urls: list[str],
    rng: random.Random,
    timeout_ms: int,
    fast_mode: bool,
    proxy_plan: ProxyPlan,
    verify_ip: bool,
    visitor_test: bool = False,
) -> UserSessionReport:
    report = UserSessionReport(user_id=user_id)
    proxy = proxy_plan.for_user(user_id)
    if proxy:
        report.proxy_server = proxy.get("server", "")

    context_opts: dict[str, Any] = {
        "user_agent": CHROME_USER_AGENT,
        "viewport": {"width": 1280, "height": 800},
        "ignore_https_errors": True,
        "locale": "en-US",
        "timezone_id": "America/New_York",
    }
    if proxy:
        context_opts["proxy"] = proxy

    context = await browser.new_context(**context_opts)
    await context.add_init_script(STEALTH_INIT_SCRIPT)
    await allow_vercel_insights_routes(context)
    context.set_default_timeout(timeout_ms)
    page = await context.new_page()

    try:
        if visitor_test:
            return await _run_visitor_session_body(
                page, report, base_url, user_id, timeout_ms, proxy_plan, verify_ip,
            )
        return await _run_user_session_body(
            page, report, base_url, user_id, sitemap_paths, resource_urls,
            rng, timeout_ms, fast_mode, proxy_plan, verify_ip,
        )
    finally:
        try:
            await context.close()
        except Exception:
            pass


async def _run_visitor_session_body(
    page: Page,
    report: UserSessionReport,
    base_url: str,
    user_id: int,
    timeout_ms: int,
    proxy_plan: ProxyPlan,
    verify_ip: bool,
) -> UserSessionReport:
    """Short, reliable session aimed at Vercel *visitor* counts (1 IP + fresh cookie each user)."""
    vercel_beacons_ok = 0

    def on_response(response) -> None:
        nonlocal vercel_beacons_ok
        if "/_vercel/insights" in response.url and response.status in (200, 204):
            vercel_beacons_ok += 1

    page.on("response", on_response)

    async def step(scenario: str, fn) -> None:
        result = await timed_step(user_id, scenario, fn)
        report.steps.append(result)
        if not result.ok:
            report.errors.append(f"{scenario}: {result.detail}")

    if verify_ip or proxy_plan.mode != "none":
        ip, country = await fetch_egress_geo(page)
        report.egress_ip = ip
        report.egress_country = country

    async def visit_and_click() -> str:
        await safe_goto(page, base_url.rstrip("/") + "/", timeout_ms)
        await wait_for_vercel_analytics(page)
        await page.wait_for_timeout(1500)

        for tab in ("resources", "blogs", "community"):
            await click_tab(page, tab)
            await page.wait_for_timeout(1200)

        card = page.locator("#blogs .blog-card").first
        if await card.is_visible():
            await card.click()
            await page.wait_for_load_state("domcontentloaded")
            await page.wait_for_timeout(1000)
            href = page.url
        else:
            tile = page.locator(".start-here-hub__tile").first
            await tile.click()
            await page.wait_for_load_state("domcontentloaded")
            href = page.url

        await flush_analytics(page, 8.0)
        geo = f" ip={report.egress_ip} ({report.egress_country})" if report.egress_ip else ""
        return f"{href}{geo}"

    await step("visitor_journey", visit_and_click)

    report.vercel_beacons = vercel_beacons_ok
    report.vercel_beacons_ok = vercel_beacons_ok
    return report


async def _run_user_session_body(
    page: Page,
    report: UserSessionReport,
    base_url: str,
    user_id: int,
    sitemap_paths: list[str],
    resource_urls: list[str],
    rng: random.Random,
    timeout_ms: int,
    fast_mode: bool,
    proxy_plan: ProxyPlan,
    verify_ip: bool,
) -> UserSessionReport:

    vercel_beacons: list[str] = []
    vercel_beacons_ok = 0

    def on_request(request) -> None:
        url = request.url
        if "/_vercel/insights" in url:
            vercel_beacons.append(url)

    def on_response(response) -> None:
        nonlocal vercel_beacons_ok
        if "/_vercel/insights" in response.url and response.status in (200, 204):
            vercel_beacons_ok += 1

    page.on("request", on_request)
    page.on("response", on_response)

    if verify_ip or proxy_plan.mode != "none":
        ip, country = await fetch_egress_geo(page)
        report.egress_ip = ip
        report.egress_country = country

    blogs = [p for p in sitemap_paths if p.startswith("/blog/")]
    guides = [p for p in sitemap_paths if p.startswith("/guides/")]
    support = [p for p in sitemap_paths if p.startswith("/support/")]
    term = SEARCH_TERMS[user_id % len(SEARCH_TERMS)]
    state_abbr = US_STATES[user_id % len(US_STATES)]

    async def step(scenario: str, fn) -> None:
        result = await timed_step(user_id, scenario, fn)
        report.steps.append(result)
        if not result.ok:
            report.errors.append(f"{scenario}: {result.detail}")

    async def goto_home() -> str:
        await safe_goto(page, base_url.rstrip("/") + "/", timeout_ms)
        await wait_for_vercel_analytics(page)
        return page.url

    # --- Homepage & analytics bootstrap ---
    await step("overview_home", goto_home)

    async def click_hub_tiles() -> str:
        await goto_home()
        tile = page.locator(".start-here-hub__tile").nth(user_id % 8)
        label = await tile.locator(".start-here-hub__label").inner_text()
        await tile.click()
        await page.wait_for_load_state("domcontentloaded")
        return label.strip()

    await step("hub_tile_click", click_hub_tiles)

    # --- Main nav tabs (real button clicks) ---
    for tab_id in MAIN_TABS:
        if tab_id == "overview":
            continue

        async def click_main_tab(tid: str = tab_id) -> str:
            await goto_home()
            await click_tab(page, tid)
            return tid

        await step("nav_tab_click", click_main_tab)

    # --- App subtabs ---
    async def click_app_subtab() -> str:
        await goto_home()
        await click_tab(page, "app")
        sub = APP_SUBTABS[user_id % len(APP_SUBTABS)]
        sub_btn = page.locator(f'.app-subtab-button[data-app-subtab="{sub}"]')
        await sub_btn.click()
        await page.locator(f".app-subcontent#{sub}").wait_for(state="visible", timeout=10_000)
        return sub

    await step("app_subtab_click", click_app_subtab)

    # --- Resources search + filter + card click ---
    async def resources_search_flow() -> str:
        await goto_home()
        await click_tab(page, "resources")
        search = page.locator("#resources .resource-library__search")
        await search.wait_for(state="visible", timeout=10_000)
        await search.fill(term)
        await page.wait_for_timeout(300)
        pill = page.locator('#resources .resource-pill[data-category="nutrition"]')
        await pill.click()
        href = await click_first_visible(page, "#resources .resource-card a")
        await page.wait_for_load_state("domcontentloaded")
        return f"q={term} -> {href}"

    await step("resources_search_click", resources_search_flow)

    # --- Standalone resources page ---
    async def resources_page_search() -> str:
        await safe_goto(page, base_url.rstrip("/") + "/resources", timeout_ms)
        search = page.locator(".resource-library__search").first
        await search.wait_for(state="visible", timeout=10_000)
        await search.fill(term)
        pill = page.locator('.resource-pill[data-category="treatment"]').first
        await pill.click()
        visible = await page.locator(".resource-card").count()
        return f"/resources q={term} cards={visible}"

    await step("resources_page_search", resources_page_search)

    # --- Articles filter + card click ---
    async def articles_filter_click() -> str:
        await goto_home()
        await click_tab(page, "blogs")
        filt = page.locator('[data-blog-filter="nutrition"]').first
        await filt.click()
        await page.wait_for_timeout(300)
        href = await click_first_visible(page, "#blogs .blog-card")
        await page.wait_for_load_state("domcontentloaded")
        return href

    await step("article_filter_click", articles_filter_click)

    # --- Community state select (+ map click when ready) ---
    async def community_interaction() -> str:
        await goto_home()
        await click_tab(page, "community")
        select = page.locator("#community-state-select")
        await select.wait_for(state="attached", timeout=15_000)
        await page.wait_for_function(
            "() => { const s = document.getElementById('community-state-select'); return s && s.options.length > 1; }",
            timeout=20_000,
        )
        await select.select_option(value=state_abbr)
        await page.wait_for_timeout(500)
        map_state = page.locator(f".community-map-svg .state[data-state='{state_abbr}']").first
        if await map_state.count():
            await map_state.click(force=True)
        detail = await page.locator("#community-detail").inner_text()
        return f"state={state_abbr} detail_chars={len(detail)}"

    await step("community_state_click", community_interaction)

    # --- Standalone nav pages (deduped from hub/topic coverage) ---
    for nav_path in EXTRA_NAV_PAGES:

        async def visit_nav(path: str = nav_path) -> str:
            await safe_goto(page, base_url.rstrip("/") + path, timeout_ms)
            title = await page.title()
            return f"{path} ({title[:60]})"

        await step("nav_page_visit", visit_nav)

    # --- Hub pages ---
    for hub in HUB_PATHS:
        async def visit_hub(path: str = hub) -> str:
            await safe_goto(page, base_url.rstrip("/") + path, timeout_ms)
            return path

        await step("hub_page_visit", visit_hub)

    # --- Topic articles from search ---
    for slug in TOPIC_ARTICLES:
        if slug not in sitemap_paths and slug not in resource_urls:
            continue

        async def visit_topic(path: str = slug) -> str:
            await safe_goto(page, base_url.rstrip("/") + path, timeout_ms)
            h1 = await page.locator("h1").first.inner_text()
            return f"{path} — {h1[:50]}"

        await step("search_topic_article", visit_topic)

    # --- Extra blog & guide clicks ---
    for _ in range(2):
        if not blogs:
            break
        pick = rng.choice(blogs)

        async def visit_blog(path: str = pick) -> str:
            await safe_goto(page, base_url.rstrip("/") + path, timeout_ms)
            return path

        await step("article_click", visit_blog)

    if guides:
        pick_guide = rng.choice(guides)

        async def visit_guide(path: str = pick_guide) -> str:
            await safe_goto(page, base_url.rstrip("/") + path, timeout_ms)
            return path

        await step("guide_click", visit_guide)

    if support:
        pick_support = rng.choice(support)

        async def visit_support(path: str = pick_support) -> str:
            await safe_goto(page, base_url.rstrip("/") + path, timeout_ms)
            return path

        await step("support_page_visit", visit_support)

    # --- Research source outbound link click (tracked as click event) ---
    async def research_link_click() -> str:
        await goto_home()
        await click_tab(page, "research")
        link = page.locator("#research .research-source-card a").first
        await link.wait_for(state="visible", timeout=10_000)
        href = await link.get_attribute("href") or ""
        await link.click(modifiers=["Control"])
        return href

    await step("research_outbound_click", research_link_click)

    # --- Distribute sitemap coverage across users (skip in --fast mode) ---
    if not fast_mode:
        pool = [p for p in sitemap_paths if p not in TOPIC_ARTICLES]
        rng.shuffle(pool)
        for extra in pool[user_id :: 100][:3]:

            async def visit_extra(path: str = extra) -> str:
                await safe_goto(page, base_url.rstrip("/") + path, timeout_ms)
                return path

            await step("sitemap_coverage", visit_extra)

    # Flush analytics beacons before closing context
    await flush_analytics(page, 5.0)
    report.vercel_beacons = len(vercel_beacons)
    report.vercel_beacons_ok = vercel_beacons_ok

    try:
        analytics = await page.evaluate(
            """() => {
                const q = window.vaq || [];
                const events = q.filter(a => a && a[0] === 'event').map(a => a[1]?.name || 'unknown');
                return {
                    queue_len: q.length,
                    page_views: events.filter(n => n === 'page_view').length,
                    clicks: events.filter(n => n === 'click').length,
                    tab_views: events.filter(n => n === 'tab_view').length,
                };
            }"""
        )
        report.page_views_tracked = int(analytics.get("page_views", 0))
        report.clicks_tracked = int(analytics.get("clicks", 0))
        report.analytics_events_total = int(analytics.get("queue_len", 0))
    except Exception:
        report.analytics_events_total = 0

    return report


def percentile(values: list[float], pct: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    k = (len(ordered) - 1) * (pct / 100)
    f = int(k)
    c = min(f + 1, len(ordered) - 1)
    if f == c:
        return ordered[f]
    return ordered[f] + (ordered[c] - ordered[f]) * (k - f)


def build_report(
    base_url: str,
    concurrency: int,
    started: float,
    session_reports: list[UserSessionReport],
) -> PlaywrightLoadReport:
    duration = time.time() - started
    all_steps = [s for r in session_reports for s in r.steps]
    ok_steps = [s for s in all_steps if s.ok]
    bad_steps = [s for s in all_steps if not s.ok]
    latencies = [s.latency_ms for s in ok_steps]

    scenario_counts: dict[str, int] = {}
    scenario_failures: dict[str, int] = {}
    for s in all_steps:
        scenario_counts[s.scenario] = scenario_counts.get(s.scenario, 0) + 1
        if not s.ok:
            scenario_failures[s.scenario] = scenario_failures.get(s.scenario, 0) + 1

    sessions_failed = sum(1 for r in session_reports if r.failures > 0)

    return PlaywrightLoadReport(
        base_url=base_url,
        concurrency=concurrency,
        started_at=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(started)),
        duration_sec=round(duration, 2),
        total_steps=len(all_steps),
        step_successes=len(ok_steps),
        step_failures=len(bad_steps),
        sessions_completed=len(session_reports),
        sessions_failed=sessions_failed,
        vercel_beacons_total=sum(r.vercel_beacons for r in session_reports),
        vercel_beacons_ok=sum(r.vercel_beacons_ok for r in session_reports),
        analytics_events_total=sum(
            getattr(r, "analytics_events_total", 0) for r in session_reports
        ),
        workers=0,
        proxy_mode="none",
        unique_egress_ips=0,
        unique_egress_countries=0,
        latency_ms={
            "min": round(min(latencies), 1) if latencies else 0,
            "p50": round(percentile(latencies, 50), 1),
            "p95": round(percentile(latencies, 95), 1),
            "p99": round(percentile(latencies, 99), 1),
            "max": round(max(latencies), 1) if latencies else 0,
            "mean": round(statistics.mean(latencies), 1) if latencies else 0,
        },
        scenario_counts=scenario_counts,
        scenario_failures=scenario_failures,
        errors_sample=[
            {"user_id": s.user_id, "scenario": s.scenario, "error": s.detail}
            for s in bad_steps[:30]
        ],
    )


def print_report(report: PlaywrightLoadReport) -> None:
    print()
    print("=" * 60)
    print("IBDPal Playwright load test (real clicks)")
    print("=" * 60)
    print(f"Target:              {report.base_url}")
    print(f"Virtual users:       {report.concurrency}")
    if report.workers:
        print(f"Parallel workers:    {report.workers}")
    if report.proxy_mode:
        print(f"Proxy mode:          {report.proxy_mode}")
    if report.unique_egress_ips:
        print(f"Unique egress IPs:   {report.unique_egress_ips}")
    if report.unique_egress_countries:
        print(f"Unique countries:    {report.unique_egress_countries}")
    print(f"Duration:            {report.duration_sec}s")
    print(
        f"Steps:               {report.total_steps} total | "
        f"{report.step_successes} OK | {report.step_failures} failed"
    )
    print(
        f"Sessions:            {report.sessions_completed} completed | "
        f"{report.sessions_failed} with failures"
    )
    print(
        f"Vercel beacons:      {report.vercel_beacons_ok} OK / "
        f"{report.vercel_beacons_total} sent to /_vercel/insights/"
    )
    print(
        f"Step latency (OK):   p50={report.latency_ms['p50']}ms  "
        f"p95={report.latency_ms['p95']}ms  max={report.latency_ms['max']}ms"
    )
    print()
    if report.scenario_failures:
        print("Scenario failures:")
        for name, count in sorted(report.scenario_failures.items(), key=lambda x: -x[1]):
            print(f"  {name}: {count}")
        print()
    print("Scenarios exercised:")
    for name, count in sorted(report.scenario_counts.items(), key=lambda x: -x[1]):
        print(f"  {name}: {count}")
    print("=" * 60)
    print(
        "Vercel may filter datacenter/headless traffic from visitor counts. "
        "Check vercel_beacons_ok in the report for beacon delivery."
    )


async def launch_browser(pw, channel: str | None, headless: bool) -> Browser:
    """Prefer system Chrome/Edge when Playwright browser bundle is unavailable."""
    channels = [channel] if channel else ["chrome", "msedge", None]
    launch_args = [
        "--disable-blink-features=AutomationControlled",
        "--disable-dev-shm-usage",
    ]
    last_err: Exception | None = None
    for ch in channels:
        opts: dict[str, Any] = {
            "headless": headless,
            "args": launch_args,
            "ignore_default_args": ["--enable-automation"],
        }
        if ch:
            opts["channel"] = ch
        try:
            return await pw.chromium.launch(**opts)
        except Exception as exc:  # noqa: BLE001
            last_err = exc
    raise RuntimeError(f"Could not launch browser (tried {channels}): {last_err}")


async def run_load_test(
    base_url: str,
    concurrency: int,
    workers: int,
    timeout_ms: int,
    channel: str | None,
    headless: bool,
    fast_mode: bool,
    output_path: Path | None,
    proxy_plan: ProxyPlan,
    verify_ip: bool,
    visitor_test: bool,
) -> tuple[PlaywrightLoadReport, list[UserSessionReport]]:
    sitemap_paths = parse_sitemap_paths()
    resource_urls = parse_resource_urls()
    rng = random.Random(42)
    started = time.time()
    sem = asyncio.Semaphore(workers)
    completed = 0
    session_reports: list[UserSessionReport | None] = [None] * concurrency

    print(f"Egress IPs:          {proxy_plan.describe()}")
    if proxy_plan.mode == "rotate":
        print(
            "WARN: Rotating proxy gateway (e.g. p.webshare.io) may reuse IPs across workers. "
            "For visitor simulation prefer static/direct IPs in load-test-proxies.txt (1 per user).",
            flush=True,
        )
    if proxy_plan.mode == "list" and len(proxy_plan.entries) < concurrency:
        print(
            f"WARN: {len(proxy_plan.entries)} proxies for {concurrency} users — "
            "IPs will repeat (round-robin). Use --proxy-rotate or add more proxies.",
            flush=True,
        )

    async with async_playwright() as pw:
        browser = await launch_browser(pw, channel, headless)

        async def run_one(uid: int) -> None:
            nonlocal completed
            async with sem:
                try:
                    session_reports[uid] = await run_user_session(
                        browser,
                        base_url,
                        uid,
                        sitemap_paths,
                        resource_urls,
                        rng,
                        timeout_ms,
                        fast_mode,
                        proxy_plan,
                        verify_ip,
                        visitor_test,
                    )
                except Exception as exc:  # noqa: BLE001
                    session_reports[uid] = UserSessionReport(
                        user_id=uid,
                        errors=[str(exc)],
                        steps=[StepResult("session", False, 0, str(exc), uid)],
                    )
                completed += 1
                if completed % 10 == 0 or completed == concurrency:
                    ok_beacons = sum(
                        (r.vercel_beacons_ok if r else 0) for r in session_reports if r
                    )
                    print(
                        f"  progress: {completed}/{concurrency} sessions | "
                        f"vercel beacons OK so far: {ok_beacons}",
                        flush=True,
                    )
                    if output_path and completed % 25 == 0:
                        partial = build_report(
                            base_url, concurrency, started,
                            [r for r in session_reports if r],
                        )
                        partial.workers = workers
                        partial.proxy_mode = proxy_plan.mode
                        partial.unique_egress_ips = len(
                            {r.egress_ip for r in session_reports if r and r.egress_ip}
                        )
                        partial.unique_egress_countries = len(
                            {r.egress_country for r in session_reports if r and r.egress_country}
                        )
                        partial.duration_sec = round(time.time() - started, 2)
                        output_path.write_text(
                            json.dumps({**partial.__dict__, "partial": True}, indent=2),
                            encoding="utf-8",
                        )

        await asyncio.gather(*(run_one(uid) for uid in range(concurrency)))
        try:
            await asyncio.wait_for(browser.close(), timeout=30.0)
        except asyncio.TimeoutError:
            print("WARN: browser.close() timed out; continuing.", flush=True)

    final_sessions = [r for r in session_reports if r is not None]
    report = build_report(base_url, concurrency, started, final_sessions)
    report.workers = workers
    report.proxy_mode = proxy_plan.mode
    report.unique_egress_ips = len({r.egress_ip for r in final_sessions if r.egress_ip})
    report.unique_egress_countries = len(
        {r.egress_country for r in final_sessions if r.egress_country}
    )
    return report, final_sessions


def main() -> int:
    parser = argparse.ArgumentParser(description="Playwright browser load test for ibdpal.org")
    parser.add_argument("--base-url", default=os.environ.get("IBDPAL_LOAD_TEST_URL", DEFAULT_BASE))
    parser.add_argument("--users", type=int, default=int(os.environ.get("IBDPAL_LOAD_TEST_USERS", "100")))
    parser.add_argument(
        "--workers",
        type=int,
        default=int(os.environ.get("IBDPAL_LOAD_TEST_WORKERS", "15")),
        help="Max parallel browser sessions (default 15; 100 users are queued through workers)",
    )
    parser.add_argument("--timeout", type=float, default=30.0, help="Per-action timeout (seconds)")
    parser.add_argument(
        "--fast",
        action="store_true",
        help="Skip per-user sitemap sweep (faster; still exercises all click/search flows)",
    )
    parser.add_argument(
        "--visitor-test",
        action="store_true",
        help=(
            "Short session per user for Vercel visitor counting (home + tabs + 1 click). "
            "Uses 1 worker by default when proxies are set."
        ),
    )
    parser.add_argument(
        "--channel",
        default=os.environ.get("PLAYWRIGHT_CHANNEL", ""),
        help="System browser channel: chrome, msedge (default: auto-detect)",
    )
    parser.add_argument("--headed", action="store_true", help="Show browser windows")
    parser.add_argument(
        "--proxies-file",
        type=Path,
        default=None,
        help=f"Proxy list file (default: {DEFAULT_PROXIES_FILE.name} if present). One URL per line.",
    )
    parser.add_argument(
        "--webshare-url",
        default="",
        help="Webshare download URL (or set WEBSHARE_DOWNLOAD_URL). Fetches ip:port:user:pass list.",
    )
    parser.add_argument(
        "--proxy-rotate",
        default="",
        help=(
            "Rotating proxy gateway URL with {session}/{user}/{uid} placeholder, e.g. "
            "'http://user-{session}:pass@gate.provider.com:10000'"
        ),
    )
    parser.add_argument(
        "--verify-ip",
        action="store_true",
        help="Resolve egress IP per user via ipify (always on when proxies are configured)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "load-test-playwright-results.json",
    )
    args = parser.parse_args()

    channel = args.channel.strip() or None

    try:
        proxy_plan = load_proxy_plan(args.proxies_file, args.proxy_rotate, args.webshare_url)
    except ValueError as exc:
        print(f"Proxy config error: {exc}")
        return 2

    workers = max(1, min(args.workers, args.users))
    if args.visitor_test and proxy_plan.mode != "none":
        workers = 1

    print(f"Starting Playwright load test: {args.users} users, {workers} parallel -> {args.base_url}")
    if channel:
        print(f"Browser channel: {channel}")
    else:
        print("Browser: auto (chrome -> msedge -> playwright chromium)")
    if args.visitor_test:
        print("Mode: --visitor-test (short journey for Vercel visitor counts)")
    elif args.fast:
        print("Mode: --fast (skipping sitemap sweep per user)")

    verify_ip = args.verify_ip or proxy_plan.mode != "none"

    report, sessions = asyncio.run(
        run_load_test(
            args.base_url,
            args.users,
            workers,
            int(args.timeout * 1000),
            channel,
            headless=not args.headed,
            fast_mode=args.fast,
            output_path=args.output,
            proxy_plan=proxy_plan,
            verify_ip=verify_ip,
            visitor_test=args.visitor_test,
        )
    )
    print_report(report)

    payload = {
        **report.__dict__,
        "per_user_vercel_beacons": [r.vercel_beacons for r in sessions],
        "per_user_vercel_beacons_ok": [r.vercel_beacons_ok for r in sessions],
        "per_user_clicks_tracked": [r.clicks_tracked for r in sessions],
        "per_user_page_views_tracked": [r.page_views_tracked for r in sessions],
        "per_user_egress_ips": [r.egress_ip for r in sessions],
        "per_user_egress_countries": [r.egress_country for r in sessions],
        "per_user_proxy_servers": [r.proxy_server for r in sessions],
    }
    args.output.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"Full report written to {args.output}")

    return 1 if report.step_failures else 0


if __name__ == "__main__":
    sys.exit(main())
