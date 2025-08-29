#!/usr/bin/env python3
"""
Direct API approach to crawl Cascadeur documentation using Firecrawl API
- Supports configurable output directory via CLI/env
- Robustly saves all successful pages to markdown
"""

import argparse
import json
import os
import re
import time
from typing import Any, Dict, List, Optional, Tuple

import requests


DEFAULT_OUTPUT_DIR = "cascadeur-docs/python/_generate/firecrawl"


def sanitize_filename(name: str, max_len: int = 80) -> str:
    """Sanitize a string for use as a safe filename."""
    name = name.replace("\\", "_").replace("/", "_").strip()
    name = "".join(c for c in name if c.isalnum() or c in (" ", "-", "_", "."))
    name = re.sub(r"\s+", " ", name).strip()
    name = name[:max_len].rstrip()
    return name or "untitled"


def resolve_output_dir(cli_dir: Optional[str]) -> str:
    """
    Resolve the output directory with precedence:
    1) CLI flag --output-dir / -o (if provided)
    2) Env CRAWL_OUTPUT_DIR
    3) Env FIRECRAWL_OUTPUT_DIR
    4) DEFAULT_OUTPUT_DIR
    """
    if cli_dir:
        return cli_dir
    env_dir = os.getenv("CRAWL_OUTPUT_DIR") or os.getenv("FIRECRAWL_OUTPUT_DIR")
    return env_dir or DEFAULT_OUTPUT_DIR


def extract_pages(crawl_result: Any) -> List[Dict[str, Any]]:
    """
    Normalize Firecrawl direct API crawl result into a list of page dicts.
    Expected shape (completed):
    {
      "status": "completed",
      "data": [ {page}, {page}, ... ],
      ...
    }
    But handle variants defensively.
    """
    if isinstance(crawl_result, list):
        return crawl_result

    if isinstance(crawl_result, dict):
        data = crawl_result.get("data")
        if isinstance(data, list):
            return data
        if isinstance(data, dict):
            # Some shapes nest under 'pages'
            pages = data.get("pages")
            if isinstance(pages, list):
                return pages
            # or a single page dict
            if "markdown" in data or "content" in data or "metadata" in data:
                return [data]
        # Direct pages property
        if isinstance(crawl_result.get("pages"), list):
            return crawl_result["pages"]
        # Single page dict
        if any(k in crawl_result for k in ("markdown", "content", "metadata")):
            return [crawl_result]

    return []


def extract_markdown_and_meta(page: Dict[str, Any]) -> Tuple[Optional[str], Dict[str, Any]]:
    """
    Extract markdown and metadata across possible shapes:
    - page['markdown']
    - page['data']['markdown']
    - page['content']['markdown']
    """
    md: Optional[str] = None
    meta: Dict[str, Any] = {}

    if not isinstance(page, dict):
        return None, {}

    md = page.get("markdown")
    meta = page.get("metadata") or {}

    if md is None and isinstance(page.get("data"), dict):
        data = page["data"]
        md = data.get("markdown", md)
        if not meta:
            meta = data.get("metadata") or meta

    if md is None and isinstance(page.get("content"), dict):
        content = page["content"]
        md = content.get("markdown", md)
        if not meta and isinstance(content.get("metadata"), dict):
            meta = content.get("metadata")

    return md, (meta or {})


def infer_filename_from_page(idx: int, page: Dict[str, Any]) -> str:
    """Build a stable filename using title or URL path fallback."""
    meta = page.get("metadata") or {}
    title = meta.get("title")

    source_url = meta.get("sourceURL") or meta.get("sourceUrl") or ""
    if not title and source_url:
        url_path = re.sub(r"^https?://[^/]+/", "", source_url)
        url_path = url_path.replace("/", "_")
        title = url_path

    if not title:
        title = f"page_{idx}"

    safe = sanitize_filename(title, max_len=80)
    return f"{idx:02d}_{safe}.md"


def save_results(output_dir: str, crawl_result: Any, pages: List[Dict[str, Any]]) -> Tuple[int, int]:
    """
    Save crawl_results.json and individual page markdown files.
    Returns (saved_count, skipped_count).
    """
    os.makedirs(output_dir, exist_ok=True)

    # Save full raw result
    with open(os.path.join(output_dir, "crawl_results.json"), "w", encoding="utf-8") as f:
        json.dump(crawl_result, f, indent=2, ensure_ascii=False)

    saved = 0
    skipped = 0

    for i, page in enumerate(pages):
        markdown, meta = extract_markdown_and_meta(page)
        if not markdown:
            skipped += 1
            continue

        # Merge meta back for filename inference
        merged = {"metadata": meta, **page}
        filename = infer_filename_from_page(i, merged)
        fullpath = os.path.join(output_dir, filename)

        with open(fullpath, "w", encoding="utf-8") as f:
            title = meta.get("title", "Untitled")
            source = meta.get("sourceURL") or meta.get("sourceUrl") or "Unknown"
            f.write(f"# {title}\n\n")
            f.write(f"Source: {source}\n\n")
            f.write(markdown)

        print(f"Saved: {fullpath}")
        saved += 1

    return saved, skipped


class FirecrawlDirectAPI:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.firecrawl.dev/v1"
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }

    def scrape(self, url: str, options: Optional[Dict] = None) -> Dict:
        """Scrape a single URL"""
        payload: Dict[str, Any] = {"url": url}
        if options:
            payload.update(options)

        try:
            response = requests.post(
                f"{self.base_url}/scrape", headers=self.headers, json=payload
            )
            response.raise_for_status()
            return response.json()
        except requests.HTTPError as e:
            resp = e.response
            body = None
            if resp is not None:
                try:
                    body = resp.json()
                except Exception:
                    body = resp.text
            else:
                body = str(e)
            print("❌ Firecrawl /scrape HTTPError")
            print(f"- Status: {getattr(e.response, 'status_code', 'unknown')}")
            print(f"- Response: {body}")
            print(f"- Sent payload: {json.dumps(payload, indent=2)}")
            raise

    def crawl(self, url: str, options: Optional[Dict] = None) -> str:
        """Start a crawl job and return job ID with API-compat fallback and 429 retry."""
        base_opts: Dict[str, Any] = options or {}
        scrape_opts: Dict[str, Any] = base_opts.get("scrapeOptions", {}) or {}
        co: Dict[str, Any] = base_opts.get("crawlerOptions", {}) or {}

        limit = co.get("limit", base_opts.get("limit"))
        includes = co.get("includes")
        excludes = co.get("excludes")
        allow_backward = co.get("allowBackwardCrawling")
        allow_external = co.get("allowExternalContentLinks")

        def clean(d: Dict[str, Any]) -> Dict[str, Any]:
            return {k: v for k, v in d.items() if v is not None}

        # Prefer legacy structure first (observed to be accepted), then fallbacks that caused 400 earlier.
        legacy_payload: Dict[str, Any] = {"url": url}
        legacy_payload.update(base_opts)

        flat_payload_a = clean(
            {
                "url": url,
                "limit": limit,
                "includes": includes,
                "excludes": excludes,
                "allowBackwardCrawling": allow_backward,
                "allowExternalContentLinks": allow_external,
                "scrapeOptions": scrape_opts,
            }
        )
        flat_payload_b = clean(
            {
                "url": url,
                "limit": limit,
                "includePaths": includes,
                "excludePaths": excludes,
                "allowBackwardCrawling": allow_backward,
                "allowExternalContentLinks": allow_external,
                "scrapeOptions": scrape_opts,
            }
        )

        candidates: List[Dict[str, Any]] = [legacy_payload, flat_payload_a, flat_payload_b]

        last_error: Optional[Exception] = None

        for idx, payload in enumerate(candidates, start=1):
            attempt = 0
            while True:
                attempt += 1
                try:
                    if attempt == 1:
                        print(f"🔁 Trying payload variant #{idx} for /crawl")
                    else:
                        print(f"🔁 Retrying payload variant #{idx} (attempt {attempt}) after 429 backoff")

                    response = requests.post(
                        f"{self.base_url}/crawl", headers=self.headers, json=payload
                    )
                    response.raise_for_status()
                    data = response.json()
                    if "id" not in data:
                        raise RuntimeError(f"Firecrawl returned 200 but no 'id' field: {data}")
                    return data["id"]
                except requests.HTTPError as e:
                    resp = e.response
                    status = getattr(resp, "status_code", None)
                    body: Any = None
                    if resp is not None:
                        try:
                            body = resp.json()
                        except Exception:
                            body = resp.text

                    print("❌ Firecrawl /crawl HTTPError")
                    print(f"- Status: {status if status is not None else 'unknown'}")
                    print(f"- Response: {body}")
                    print(f"- Sent payload: {json.dumps(payload, indent=2)}")
                    last_error = e

                    # Handle rate limit with backoff and retry same payload
                    if status == 429:
                        # Retry-After header (seconds) or parse rough seconds from message
                        retry_after = 60
                        try:
                            hdr = resp.headers.get("Retry-After")
                            if hdr is not None and str(hdr).isdigit():
                                retry_after = int(hdr)
                        except Exception:
                            pass
                        # Cap backoff to reasonable window
                        retry_after = max(30, min(retry_after, 180))
                        print(f"⏳ Rate limited, sleeping {retry_after}s before retry...")
                        time.sleep(retry_after)
                        continue  # retry same payload

                    # If BAD_REQUEST unrecognized keys, break to try next variant
                    try:
                        if isinstance(body, dict) and body.get("code") == "BAD_REQUEST":
                            details = body.get("details", [])
                            if any(
                                isinstance(d, dict)
                                and d.get("code") == "unrecognized_keys"
                                for d in details
                            ):
                                # try next candidate
                                break
                    except Exception:
                        pass

                    # Other errors: do not continue with this or next payloads
                    return self._raise_with_context(last_error)

        # If we get here, all variants failed
        return self._raise_with_context(last_error)

    def _raise_with_context(self, err: Optional[Exception]):
        if err:
            raise err
        raise RuntimeError("Unknown error starting crawl: no payload variants succeeded")

    def get_crawl_status(self, job_id: str) -> Dict:
        """Get crawl job status"""
        response = requests.get(f"{self.base_url}/crawl/{job_id}", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def wait_for_crawl(self, job_id: str, timeout: int = 300) -> Dict:
        """Wait for crawl to complete"""
        start_time = time.time()

        while time.time() - start_time < timeout:
            status = self.get_crawl_status(job_id)

            if status.get("status") == "completed":
                return status
            if status.get("status") == "failed":
                raise Exception(f"Crawl failed: {status.get('error', 'Unknown error')}")

            print(
                f"Crawl status: {status.get('status')} - "
                f"{status.get('current', 0)}/{status.get('total', '?')} pages"
            )
            time.sleep(10)

        raise TimeoutError(f"Crawl did not complete within {timeout} seconds")


def crawl_cascadeur_api_docs(output_dir: Optional[str] = None) -> Optional[Dict[str, Any]]:
    """Crawl Cascadeur Python API docs using direct API and save results."""
    api_key = os.getenv("FIRECRAWL_API_KEY")
    if not api_key:
        print("❌ Please set FIRECRAWL_API_KEY environment variable")
        print("Get your API key from: https://firecrawl.dev/")
        return None

    resolved_dir = resolve_output_dir(output_dir)
    client = FirecrawlDirectAPI(api_key)

    crawl_options: Dict[str, Any] = {
        "scrapeOptions": {
            "formats": ["markdown"],
            "onlyMainContent": True,
            "waitFor": 1000,
        },
        "crawlerOptions": {
            "limit": 15,
            "includes": ["**/python-api/**"],
            "excludes": ["**/search**", "**/genindex**", "**/_static/**"],
            "allowBackwardCrawling": False,
            "allowExternalContentLinks": False,
        },
    }

    try:
        print("🔥 Starting Cascadeur Python API documentation crawl...")

        # Log payload being sent for easier debugging if Firecrawl rejects it
        print("📦 Crawl payload:")
        print(json.dumps(crawl_options, indent=2))

        job_id = client.crawl("https://cascadeur.com/python-api/", crawl_options)
        print(f"📋 Crawl job started: {job_id}")

        result = client.wait_for_crawl(job_id)

        if result.get("status") == "completed":
            pages = extract_pages(result)
            print(f"✅ Crawl completed! Found {len(pages)} page items")

            saved, skipped = save_results(resolved_dir, result, pages)

            print("\nSummary:")
            print(f"- Output directory: {resolved_dir}")
            print(f"- Total items: {len(pages)}")
            print(f"- Saved markdown: {saved}")
            print(f"- Skipped (no markdown): {skipped}")
            print(f"\n🎉 All documentation saved to: {resolved_dir}/")
            return result

        print(f"❌ Crawl finished with unexpected status: {result.get('status')}")
        return None

    except Exception as e:
        print(f"❌ Error during crawl: {e}")
        return None


def scrape_single_page(output_dir: Optional[str] = None) -> Optional[Dict[str, Any]]:
    """Scrape just the main documentation page and save markdown."""
    api_key = os.getenv("FIRECRAWL_API_KEY")
    if not api_key:
        print("❌ Please set FIRECRAWL_API_KEY environment variable")
        print("Get your API key from: https://firecrawl.dev/")
        return None

    resolved_dir = resolve_output_dir(output_dir)
    client = FirecrawlDirectAPI(api_key)

    try:
        print("📄 Scraping main documentation page...")
        result = client.scrape(
            "https://cascadeur.com/python-api/",
            {"formats": ["markdown"], "onlyMainContent": True},
        )

        # Save raw result
        os.makedirs(resolved_dir, exist_ok=True)
        with open(os.path.join(resolved_dir, "scrape_result.json"), "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)

        data = result.get("data", {})
        page = data if isinstance(data, dict) else {"data": data}
        markdown, meta = extract_markdown_and_meta(page)

        if markdown:
            title = meta.get("title") or "main_page"
            fname = f"00_{sanitize_filename(title)}.md"
            fullpath = os.path.join(resolved_dir, fname)
            with open(fullpath, "w", encoding="utf-8") as f:
                f.write(f"# {meta.get('title', 'Main Page')}\n\n")
                f.write(f"Source: {meta.get('sourceURL') or meta.get('sourceUrl') or 'https://cascadeur.com/python-api/'}\n\n")
                f.write(markdown)
            print(f"✅ Saved main documentation to: {fullpath}")
        else:
            print("⚠️ No markdown content found in scrape result")

        return result

    except Exception as e:
        print(f"❌ Error scraping page: {e}")
        return None


def main():
    parser = argparse.ArgumentParser(
        description="Firecrawl Direct API - Cascadeur Documentation Crawler"
    )
    parser.add_argument(
        "-m",
        "--mode",
        choices=["crawl", "scrape"],
        default=None,
        help="Mode to run: crawl entire docs or scrape main page",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        dest="output_dir",
        default=None,
        help=f"Directory to save results (default precedence: --output-dir | CRAWL_OUTPUT_DIR | FIRECRAWL_OUTPUT_DIR | {DEFAULT_OUTPUT_DIR})",
    )
    args = parser.parse_args()

    # Backwards compatible interactive choice if mode not provided
    if args.mode is None:
        print("🔥 Firecrawl Direct API - Cascadeur Documentation Crawler")
        print("=" * 60)
        choice = input(
            "Choose option:\n1. Crawl all documentation (recommended)\n2. Scrape main page only\nEnter choice (1/2): "
        )
        if choice == "1":
            crawl_cascadeur_api_docs(args.output_dir)
        elif choice == "2":
            scrape_single_page(args.output_dir)
        else:
            print("Invalid choice. Please run again and select 1 or 2.")
        return

    if args.mode == "crawl":
        crawl_cascadeur_api_docs(args.output_dir)
    else:
        scrape_single_page(args.output_dir)


if __name__ == "__main__":
    main()
