#!/usr/bin/env python3
"""
Sequential crawler: scrape web documentation page-by-page with Firecrawl /scrape
- Strictly sequential, no parallel requests
- Rate limit: --rate pages/minute (default 5 => 12s between requests)
- Discovers links by fetching HTML and extracting hrefs
- Saves all successful pages to a single, configurable output directory
- Configurable target URL and path filtering via --start-url and --base-path

Examples:
  # Scrape Cascadeur Python API docs (default)
  python sequential_scrape.py -o output_dir

  # Scrape a different documentation site
  python sequential_scrape.py --start-url https://docs.python.org/3/ --base-path /3/ -o python_docs

  # Scrape with custom path filtering
  python sequential_scrape.py --start-url https://example.com/docs/api/ --base-path /docs/ -o api_docs

  # Scrape with higher rate limit
  python sequential_scrape.py --start-url https://site.com/guides/ --rate 10 -o guides
"""

import argparse
import json
import os
import re
import time
from typing import Any, Dict, List, Optional, Set
from urllib.parse import urljoin, urlparse

import requests

# Reuse save/sanitize helpers
# Load crawl_utils from the same directory without requiring a Python package name (hyphens in dir).
try:
    from crawl_utils import (  # type: ignore
        DEFAULT_OUTPUT_DIR,
        resolve_output_dir,
        extract_markdown_and_meta,
        infer_filename_from_page,
        sanitize_filename,
    )
except Exception:
    import importlib.util
    import sys
    _utils_path = os.path.join(os.path.dirname(__file__), "crawl_utils.py")
    spec = importlib.util.spec_from_file_location("crawl_utils", _utils_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load crawl_utils from {_utils_path}")
    _cu = importlib.util.module_from_spec(spec)
    sys.modules["crawl_utils"] = _cu
    spec.loader.exec_module(_cu)  # type: ignore[attr-defined]
    DEFAULT_OUTPUT_DIR = _cu.DEFAULT_OUTPUT_DIR
    resolve_output_dir = _cu.resolve_output_dir
    extract_markdown_and_meta = _cu.extract_markdown_and_meta
    infer_filename_from_page = _cu.infer_filename_from_page
    sanitize_filename = _cu.sanitize_filename

BASE_URL = "https://cascadeur.com/python-api/"
FIRECRAWL_API = "https://api.firecrawl.dev/v1"


def get_api_key() -> Optional[str]:
    return os.getenv("FIRECRAWL_API_KEY")


def normalize_url(u: str, base: str) -> Optional[str]:
    """Join relative links, filter schemes, and strip fragments."""
    try:
        abs_u = urljoin(base, u)
        parsed = urlparse(abs_u)
        if parsed.scheme not in ("http", "https"):
            return None
        # Remove fragment
        abs_u = abs_u.split("#", 1)[0]
        return abs_u
    except Exception:
        return None


def match_includes_excludes(u: str, base_path: str = "/python-api/") -> bool:
    """Basic filter similar to previous includes/excludes."""
    # Includes - check if URL contains the base path
    if base_path not in u:
        return False
    # Excludes
    exclude_substrings = ["/search", "/genindex", "/_static", "/_images", "/_sources"]
    if any(x in u for x in exclude_substrings):
        return False
    return True


def extract_links_from_html(html: str, base: str, base_path: str = "/python-api/") -> List[str]:
    """Extract hrefs from HTML using a simple regex and normalize."""
    hrefs: List[str] = []
    # Find href="..."; also consider single quotes
    for m in re.findall(r'href=["\']([^"\']+)["\']', html, flags=re.IGNORECASE):
        n = normalize_url(m, base)
        if not n:
            continue
        if match_includes_excludes(n, base_path):
            hrefs.append(n)
    return hrefs


def discover_urls(start_url: str, max_pages: int, base_path: Optional[str] = None) -> List[str]:
    """
    BFS-like discovery starting from start_url, limited by max_pages.
    We fetch HTML (not Firecrawl) to find links; everything stays under the configured base path.
    """
    # Extract base path from start_url if not provided
    if base_path is None:
        parsed = urlparse(start_url)
        base_path = parsed.path.rstrip('/')
        if not base_path:
            base_path = "/"
    
    queue: List[str] = [start_url]
    seen: Set[str] = set(queue)
    result: List[str] = []

    session = requests.Session()
    session.headers.update({"User-Agent": "cascadeur-py-client/seq-crawler"})

    while queue and len(result) < max_pages:
        current = queue.pop(0)
        result.append(current)

        # Fetch and parse links
        try:
            resp = session.get(current, timeout=20)
            resp.raise_for_status()
            links = extract_links_from_html(resp.text, current, base_path)
            for link in links:
                if link not in seen:
                    seen.add(link)
                    queue.append(link)
        except Exception:
            # Ignore discovery failures, continue
            continue

    return result[:max_pages]


def firecrawl_scrape(api_key: str, url: str) -> Optional[Dict[str, Any]]:
    """Call Firecrawl /scrape for a single URL."""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload: Dict[str, Any] = {
        "url": url,
        "formats": ["markdown"],
        "onlyMainContent": True,
        "waitFor": 1000,
    }

    try:
        r = requests.post(f"{FIRECRAWL_API}/scrape", headers=headers, json=payload, timeout=60)
        r.raise_for_status()
        data = r.json()
        # Expected shape: {'success': True, 'data': {...}}
        return data
    except requests.HTTPError as e:
        resp = e.response
        status = getattr(resp, "status_code", None)
        body: Any = None
        if resp is not None:
            try:
                body = resp.json()
            except Exception:
                body = resp.text
        print("❌ Firecrawl /scrape HTTPError")
        print(f"- URL: {url}")
        print(f"- Status: {status if status is not None else 'unknown'}")
        print(f"- Response: {body}")
        return None
    except Exception as e:
        print(f"❌ Error scraping {url}: {e}")
        return None


def save_page_markdown(output_dir: str, idx: int, page: Dict[str, Any]) -> Optional[str]:
    """
    Save a single page as markdown using infer_filename_from_page() and metadata.
    Returns path of saved file or None if no markdown content present.
    """
    os.makedirs(output_dir, exist_ok=True)
    markdown, meta = extract_markdown_and_meta(page)
    if not markdown:
        return None

    merged = {"metadata": meta, **page}
    filename = infer_filename_from_page(idx, merged)
    fullpath = os.path.join(output_dir, filename)

    title = meta.get("title", "Untitled")
    source = meta.get("sourceURL") or meta.get("sourceUrl") or "Unknown"

    with open(fullpath, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n")
        f.write(f"Source: {source}\n\n")
        f.write(markdown)

    print(f"📄 Saved: {fullpath}")
    return fullpath


def run_sequential(
    start_url: str,
    output_dir: str,
    limit: int,
    rate: float,
    resume: bool = True,
    base_path: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Sequential scraping:
    - Discover up to 'limit' URLs starting from start_url
    - Scrape each via Firecrawl /scrape
    - Respect rate limit: 'rate' pages per minute => sleep between requests
    - Save per-page markdown and aggregate crawl_results.json
    """
    api_key = get_api_key()
    if not api_key:
        raise SystemExit("FIRECRAWL_API_KEY not found in environment")

    print("🔎 Discovering URLs...")
    urls = discover_urls(start_url, max_pages=limit, base_path=base_path)
    
    # Get the actual base path for display
    if base_path is None:
        parsed = urlparse(start_url)
        display_path = parsed.path.rstrip('/') if parsed.path.rstrip('/') else "/"
    else:
        display_path = base_path
    
    print(f"🧭 Discovered {len(urls)} URLs under {display_path}")

    # Rate limiting
    delay_sec = max(12.0, 60.0 / max(1.0, rate))  # Ensure at least 12s for 5/min or stricter

    # Load existing crawl_results.json if resume
    results_path = os.path.join(output_dir, "crawl_results.json")
    aggregate: List[Dict[str, Any]] = []
    if resume and os.path.exists(results_path):
        try:
            with open(results_path, "r", encoding="utf-8") as f:
                existing = json.load(f)
                if isinstance(existing, list):
                    aggregate = existing
                elif isinstance(existing, dict) and "data" in existing and isinstance(existing["data"], list):
                    aggregate = existing["data"]
        except Exception:
            pass

    visited_urls: Set[str] = set(
        p.get("metadata", {}).get("sourceURL", "") for p in aggregate if isinstance(p, dict)
    )

    saved = 0
    skipped = 0
    failed = 0

    for i, url in enumerate(urls):
        if url in visited_urls:
            print(f"⏭️ Skipping already saved: {url}")
            continue

        print(f"🧰 [{i+1}/{len(urls)}] Scraping: {url}")
        data = firecrawl_scrape(api_key, url)
        # Enforce rate limit regardless of success
        time.sleep(delay_sec)

        if not data or "data" not in data:
            failed += 1
            continue

        page_data = data["data"]
        # Ensure metadata includes sourceURL
        if isinstance(page_data, dict):
            meta = page_data.get("metadata") or {}
            if not meta.get("sourceURL"):
                meta["sourceURL"] = url
                page_data["metadata"] = meta

        # Save single page
        path = save_page_markdown(output_dir, len(aggregate), page_data)
        if path:
            aggregate.append(page_data)
            saved += 1
            # Persist aggregate results after each save to be robust
            try:
                with open(results_path, "w", encoding="utf-8") as f:
                    json.dump(aggregate, f, indent=2, ensure_ascii=False)
            except Exception as e:
                print(f"⚠️ Failed to update aggregate results: {e}")
        else:
            skipped += 1

    summary = {
        "discovered": len(urls),
        "saved": saved,
        "skipped": skipped,
        "failed": failed,
        "output_dir": output_dir,
        "results_path": results_path,
    }
    print("\n📊 Summary")
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return summary


def main():
    parser = argparse.ArgumentParser(description="Sequential Firecrawl scraper for web documentation")
    parser.add_argument(
        "-o",
        "--output-dir",
        dest="output_dir",
        default=None,
        help=f"Directory to save results (default precedence: --output-dir | CRAWL_OUTPUT_DIR | FIRECRAWL_OUTPUT_DIR | {DEFAULT_OUTPUT_DIR})",
    )
    parser.add_argument(
        "--start-url",
        default=BASE_URL,
        help=f"Start URL for discovery (default: {BASE_URL})",
    )
    parser.add_argument(
        "--base-path",
        default=None,
        help="Base path to filter URLs (e.g., '/python-api/', '/docs/'). If not provided, will be inferred from start-url path",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=120,
        help="Maximum number of pages to scrape (default: 120)",
    )
    parser.add_argument(
        "--rate",
        type=float,
        default=5.0,
        help="Pages per minute (default: 5 => ~12s/request). This enforces spacing between requests.",
    )
    parser.add_argument(
        "--no-resume",
        action="store_true",
        help="Do not resume from existing crawl_results.json (always start fresh aggregation)",
    )
    args = parser.parse_args()

    out_dir = resolve_output_dir(args.output_dir)
    run_sequential(
        start_url=args.start_url,
        output_dir=out_dir,
        limit=args.limit,
        rate=args.rate,
        resume=(not args.no_resume),
        base_path=args.base_path,
    )


if __name__ == "__main__":
    main()