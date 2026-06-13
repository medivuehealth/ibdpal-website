#!/usr/bin/env python3
"""Concurrent HTTP load test for ibdpal.org (pages + assets; no JS).

For real browser clicks and Vercel Analytics beacons, use load_test_site_playwright.py.
"""
from __future__ import annotations

import argparse
import json
import os
import random
import re
import ssl
import statistics
import sys
import time
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
SITEMAP = ROOT / "sitemap.xml"
RESOURCES_JS = ROOT / "resources-data.js"
KEYWORDS_JSON = ROOT / "data" / "ibd-resource-keywords.json"
DEFAULT_BASE = "https://www.ibdpal.org"

# Assets loaded by homepage / resources / community (search & click paths)
STATIC_ASSETS = [
    "/styles.css",
    "/site-layout-icn.css",
    "/site-polish.css",
    "/script.js",
    "/site-global.js",
    "/resources-data.js",
    "/resource-library.js",
    "/blog-index-filter.js",
    "/community-data.js",
    "/community-map.js",
    "/community-states-extra.js",
    "/community-zip-loader.js",
    "/analytics.js",
    "/analytics-config.js",
    "/canonical-host.js",
    "/llms.txt",
    "/favicon.ico",
    "/IBDPal_Logo.png",
]

# Homepage tab hash routes are client-side; these pages back each tab/action
TAB_ENTRY_PAGES = [
    "/",
    "/resources",
    "/research",
    "/blog",
    "/support",
    "/ibd-nutrition",
    "/flare-help",
    "/newly-diagnosed",
    "/visit-prep",
    "/faq",
    "/glossary",
    "/guides",
]

SEARCH_TERMS = [
    "dairy",
    "gluten",
    "glutten",
    "immune",
    "immunosuppressant",
    "flare",
    "nutrition",
    "ostomy",
    "school",
    "biologics",
]


@dataclass
class FetchResult:
    path: str
    status: int
    latency_ms: float
    bytes_read: int
    error: str = ""
    user_id: int = -1
    scenario: str = ""


@dataclass
class LoadTestReport:
    base_url: str
    concurrency: int
    started_at: str
    duration_sec: float
    total_requests: int
    successes: int
    failures: int
    unique_paths: int
    paths_tested: list[str] = field(default_factory=list)
    paths_failed: list[str] = field(default_factory=list)
    latency_ms: dict[str, float] = field(default_factory=dict)
    status_counts: dict[str, int] = field(default_factory=dict)
    scenario_counts: dict[str, int] = field(default_factory=dict)
    errors_sample: list[dict[str, Any]] = field(default_factory=list)


def parse_sitemap_paths() -> list[str]:
    tree = ET.parse(SITEMAP)
    paths: list[str] = []
    for loc in tree.findall(".//{*}loc"):
        url = (loc.text or "").strip()
        if not url:
            continue
        path = url.replace("https://www.ibdpal.org", "").replace("http://www.ibdpal.org", "")
        if not path:
            path = "/"
        paths.append(path)
    return sorted(set(paths))


def parse_resource_urls() -> list[str]:
    if not RESOURCES_JS.exists():
        return []
    text = RESOURCES_JS.read_text(encoding="utf-8")
    urls = re.findall(r'url:\s*["\']([^"\']+)["\']', text)
    internal = []
    for u in urls:
        if u.startswith("http"):
            continue
        if not u.startswith("/"):
            u = "/" + u
        internal.append(u)
    return sorted(set(internal))


_SSL_CTX: ssl.SSLContext | None = None


def build_ssl_context(insecure: bool) -> ssl.SSLContext | None:
    if insecure:
        return ssl._create_unverified_context()
    try:
        ctx = ssl.create_default_context()
        with urlopen(Request("https://www.ibdpal.org/"), context=ctx, timeout=10) as _:
            pass
        return ctx
    except (URLError, OSError, ssl.SSLError):
        print("WARN: SSL verify failed; using unverified context for load test only.")
        return ssl._create_unverified_context()


def fetch_one(
    base: str,
    path: str,
    user_id: int,
    scenario: str,
    timeout: float,
    ssl_ctx: ssl.SSLContext | None,
) -> FetchResult:
    url = base.rstrip("/") + (path if path.startswith("/") else "/" + path)
    headers = {
        "User-Agent": f"IBDPalLoadTest/1.0 (user-{user_id}; {scenario})",
        "Accept": "*/*",
    }
    start = time.perf_counter()
    try:
        req = Request(url, headers=headers, method="GET")
        kw: dict[str, Any] = {"timeout": timeout}
        if url.startswith("https://") and ssl_ctx is not None:
            kw["context"] = ssl_ctx
        with urlopen(req, **kw) as resp:
            data = resp.read(256 * 1024)  # cap read; enough to verify body
            while True:
                chunk = resp.read(65536)
                if not chunk:
                    break
                data += chunk
            elapsed = (time.perf_counter() - start) * 1000
            return FetchResult(
                path=path,
                status=getattr(resp, "status", 200),
                latency_ms=elapsed,
                bytes_read=len(data),
                user_id=user_id,
                scenario=scenario,
            )
    except HTTPError as e:
        elapsed = (time.perf_counter() - start) * 1000
        return FetchResult(
            path=path,
            status=e.code,
            latency_ms=elapsed,
            bytes_read=0,
            error=str(e),
            user_id=user_id,
            scenario=scenario,
        )
    except (URLError, TimeoutError, OSError) as e:
        elapsed = (time.perf_counter() - start) * 1000
        return FetchResult(
            path=path,
            status=0,
            latency_ms=elapsed,
            bytes_read=0,
            error=str(e),
            user_id=user_id,
            scenario=scenario,
        )


def build_user_session(
    user_id: int,
    sitemap_paths: list[str],
    resource_urls: list[str],
    rng: random.Random,
) -> list[tuple[str, str]]:
    """Realistic click/search journey per virtual user."""
    blogs = [p for p in sitemap_paths if p.startswith("/blog/")]
    guides = [p for p in sitemap_paths if p.startswith("/guides/")]
    support = [p for p in sitemap_paths if p.startswith("/support/")]
    hubs = [p for p in sitemap_paths if p.count("/") == 1 and p not in TAB_ENTRY_PAGES]

    session: list[tuple[str, str]] = []

    # Overview + app assets
    session.append(("/", "overview_home"))
    for asset in ["/styles.css", "/site-polish.css", "/script.js", "/resources-data.js"]:
        session.append((asset, "overview_assets"))

    # Tab entry pages (clickable nav)
    for page in TAB_ENTRY_PAGES:
        if page != "/":
            session.append((page, "nav_tab"))

    # Guides & tools + search data
    session.append(("/resources", "resources_tab"))
    session.append(("/resource-library.js", "resources_search_js"))
    session.append(("/resources-data.js", "resources_search_data"))
    term = SEARCH_TERMS[user_id % len(SEARCH_TERMS)]
    session.append((f"/resources?q={term}", "resources_search_sim"))

    # Articles tab assets
    session.append(("/blog-index-filter.js", "articles_filter_js"))
    if blogs:
        for _ in range(3):
            session.append((rng.choice(blogs), "article_click"))

    # Sources / research
    session.append(("/research", "sources_tab"))

    # Community map assets
    session.append(("/community-data.js", "community_data"))
    session.append(("/community-map.js", "community_map_js"))
    if support:
        session.append((rng.choice(support), "community_state_click"))

    # Hubs from start-here tiles
    for hub in ["/ibd-nutrition", "/flare-help", "/crohns-disease", "/ulcerative-colitis"]:
        if hub in sitemap_paths or hub in resource_urls:
            session.append((hub, "hub_tile"))

    if guides:
        session.append((rng.choice(guides), "guide_click"))

    # Resource library deep links (searchable topics)
    topic_slugs = [
        "/blog/dairy-lactose-ibd",
        "/blog/gluten-wheat-ibd",
        "/blog/immunosuppressants-ibd-basics",
    ]
    for slug in topic_slugs:
        if slug in sitemap_paths or slug in resource_urls:
            session.append((slug, "search_topic_article"))

    # Extra random coverage
    pool = [p for p in sitemap_paths if p not in {x[0] for x in session}]
    for _ in range(2):
        if pool:
            session.append((rng.choice(pool), "random_page"))

    return session


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


def run_load_test(
    base_url: str,
    concurrency: int,
    timeout: float,
    full_coverage: bool,
    insecure_ssl: bool,
) -> LoadTestReport:
    global _SSL_CTX
    _SSL_CTX = build_ssl_context(insecure_ssl) if base_url.startswith("https://") else None
    sitemap_paths = parse_sitemap_paths()
    resource_urls = parse_resource_urls()
    all_paths = sorted(set(sitemap_paths + STATIC_ASSETS + resource_urls))

    rng = random.Random(42)
    work: list[tuple[str, str, int]] = []

    # 100 user sessions
    for user_id in range(concurrency):
        for path, scenario in build_user_session(user_id, sitemap_paths, resource_urls, rng):
            work.append((path, scenario, user_id))

    # Ensure every sitemap/asset URL is hit at least once (full clickable coverage)
    if full_coverage:
        for i, path in enumerate(all_paths):
            work.append((path, "full_coverage", i % concurrency))

    started = time.time()
    results: list[FetchResult] = []

    with ThreadPoolExecutor(max_workers=concurrency) as pool:
        futures = [
            pool.submit(fetch_one, base_url, path, user_id, scenario, timeout, _SSL_CTX)
            for path, scenario, user_id in work
        ]
        for fut in as_completed(futures):
            results.append(fut.result())

    duration = time.time() - started
    ok = [r for r in results if 200 <= r.status < 400]
    bad = [r for r in results if r.status < 200 or r.status >= 400]

    latencies = [r.latency_ms for r in ok]
    status_counts: dict[str, int] = {}
    scenario_counts: dict[str, int] = {}
    for r in results:
        key = str(r.status)
        status_counts[key] = status_counts.get(key, 0) + 1
        scenario_counts[r.scenario] = scenario_counts.get(r.scenario, 0) + 1

    paths_tested = sorted({r.path for r in results})
    paths_failed = sorted({r.path for r in bad})

    report = LoadTestReport(
        base_url=base_url,
        concurrency=concurrency,
        started_at=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(started)),
        duration_sec=round(duration, 2),
        total_requests=len(results),
        successes=len(ok),
        failures=len(bad),
        unique_paths=len(paths_tested),
        paths_tested=paths_tested,
        paths_failed=paths_failed,
        latency_ms={
            "min": round(min(latencies), 1) if latencies else 0,
            "p50": round(percentile(latencies, 50), 1),
            "p95": round(percentile(latencies, 95), 1),
            "p99": round(percentile(latencies, 99), 1),
            "max": round(max(latencies), 1) if latencies else 0,
            "mean": round(statistics.mean(latencies), 1) if latencies else 0,
        },
        status_counts=status_counts,
        scenario_counts=scenario_counts,
        errors_sample=[
            {"path": r.path, "status": r.status, "error": r.error, "scenario": r.scenario}
            for r in bad[:25]
        ],
    )
    return report


def print_report(report: LoadTestReport, sitemap_count: int) -> None:
    print()
    print("=" * 60)
    print("IBDPal website load test report")
    print("=" * 60)
    print(f"Target:        {report.base_url}")
    print(f"Concurrency:   {report.concurrency} users")
    print(f"Duration:      {report.duration_sec}s")
    print(f"Requests:      {report.total_requests} total | {report.successes} OK | {report.failures} failed")
    print(f"Coverage:      {report.unique_paths} unique paths tested (sitemap has ~{sitemap_count})")
    print(f"Latency (OK):  p50={report.latency_ms['p50']}ms  p95={report.latency_ms['p95']}ms  p99={report.latency_ms['p99']}ms  max={report.latency_ms['max']}ms")
    print(f"Status codes:  {report.status_counts}")
    print()
    if report.paths_failed:
        print(f"Failed paths ({len(report.paths_failed)}):")
        for p in report.paths_failed[:20]:
            print(f"  - {p}")
        if len(report.paths_failed) > 20:
            print(f"  ... and {len(report.paths_failed) - 20} more")
    else:
        print("All requests succeeded.")
    print()
    print("Scenarios exercised:")
    for name, count in sorted(report.scenario_counts.items(), key=lambda x: -x[1]):
        print(f"  {name}: {count}")
    print("=" * 60)


def main() -> int:
    parser = argparse.ArgumentParser(description="Concurrent load test for ibdpal.org")
    parser.add_argument("--base-url", default=os.environ.get("IBDPAL_LOAD_TEST_URL", DEFAULT_BASE))
    parser.add_argument("--users", type=int, default=int(os.environ.get("IBDPAL_LOAD_TEST_USERS", "100")))
    parser.add_argument("--timeout", type=float, default=30.0)
    parser.add_argument("--no-full-coverage", action="store_true", help="Skip exhaustive sitemap sweep")
    parser.add_argument(
        "--insecure-ssl",
        action="store_true",
        help="Skip TLS certificate verification (use if local CA store blocks Python)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "load-test-results.json",
        help="JSON report path",
    )
    args = parser.parse_args()

    sitemap_count = len(parse_sitemap_paths())
    print(f"Starting load test: {args.users} concurrent users -> {args.base_url}")
    print(f"Sitemap URLs: {sitemap_count} | Search terms: {len(SEARCH_TERMS)}")

    report = run_load_test(
        args.base_url,
        args.users,
        args.timeout,
        full_coverage=not args.no_full_coverage,
        insecure_ssl=args.insecure_ssl,
    )

    print_report(report, sitemap_count)

    out = args.output
    payload = {
        k: v
        for k, v in report.__dict__.items()
        if k not in {"paths_tested"}  # keep JSON smaller
    }
    payload["paths_tested_count"] = len(report.paths_tested)
    payload["paths_failed"] = report.paths_failed
    out.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"Full report written to {out}")

    return 1 if report.failures else 0


if __name__ == "__main__":
    sys.exit(main())
