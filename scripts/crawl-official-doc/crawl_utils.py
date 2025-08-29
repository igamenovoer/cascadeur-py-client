#!/usr/bin/env python3
"""
Shared utilities for Cascadeur documentation crawling.

Provides:
- DEFAULT_OUTPUT_DIR
- sanitize_filename
- resolve_output_dir
- extract_pages
- extract_markdown_and_meta
- infer_filename_from_page
- save_results
"""

import json
import os
import re
from typing import Any, Dict, List, Optional, Tuple


DEFAULT_OUTPUT_DIR = "cascadeur-docs/python/_generate/firecrawl"


def sanitize_filename(name: str, max_len: int = 80) -> str:
    """Sanitize a string for use as a safe filename."""
    # Replace path separators and illegal characters
    name = name.replace("\\", "_").replace("/", "_").strip()
    # Allow alphanumeric, space, dash, underscore, dot
    name = "".join(c for c in name if c.isalnum() or c in (" ", "-", "_", "."))
    # Collapse whitespace
    name = re.sub(r"\s+", " ", name).strip()
    # Truncate
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
    Normalize various possible result shapes into a list of page dicts.
    Known shapes:
    - List[Dict]: direct list of pages
    - Dict with key 'data': might be List[Dict] or Dict with 'pages'
    - Dict with key 'pages': List[Dict]
    - Single page dict (wrap as list)
    """
    if isinstance(crawl_result, list):
        return crawl_result

    if isinstance(crawl_result, dict):
        if "data" in crawl_result:
            data = crawl_result["data"]
            if isinstance(data, list):
                return data
            if isinstance(data, dict):
                if "pages" in data and isinstance(data["pages"], list):
                    return data["pages"]
                # Some shapes put single page under data
                if "markdown" in data or "content" in data or "metadata" in data:
                    return [data]
        if "pages" in crawl_result and isinstance(crawl_result["pages"], list):
            return crawl_result["pages"]
        # Single page dict
        if "markdown" in crawl_result or "content" in crawl_result or "metadata" in crawl_result:
            return [crawl_result]

    # Fallback: unknown shape - return empty list
    return []


def extract_markdown_and_meta(page: Dict[str, Any]) -> Tuple[Optional[str], Dict[str, Any]]:
    """
    Extract markdown content and metadata from a page dict, handling multiple shapes.
    Priority order for markdown:
    - page['markdown']
    - page['data']['markdown']
    - page['content']['markdown']
    """
    md = None
    meta: Dict[str, Any] = {}

    if isinstance(page, dict):
        # Top-level
        md = page.get("markdown")
        meta = page.get("metadata") or {}

        # Nested under 'data'
        if md is None and isinstance(page.get("data"), dict):
            data = page["data"]
            md = data.get("markdown", md)
            if not meta:
                meta = data.get("metadata") or meta

        # Nested under 'content'
        if md is None and isinstance(page.get("content"), dict):
            content = page["content"]
            md = content.get("markdown", md)
            if not meta and isinstance(content.get("metadata"), dict):
                meta = content.get("metadata")

    return md, (meta or {})


def infer_filename_from_page(idx: int, page: Dict[str, Any]) -> str:
    """
    Build a stable filename for a page using title or URL path fallback.
    """
    # Prefer title
    meta = page.get("metadata") or {}
    title = meta.get("title")

    # Fallback to URL path
    source_url = meta.get("sourceURL") or meta.get("sourceUrl") or ""
    if not title and source_url:
        # Remove domain and make path-like name
        url_path = re.sub(r"^https?://[^/]+/", "", source_url)
        url_path = url_path.replace("/", "_")
        title = url_path

    # Final fallback
    if not title:
        title = f"page_{idx}"

    safe = sanitize_filename(title, max_len=80)
    return f"{idx:02d}_{safe}.md"


def save_results(output_dir: str, crawl_result: Any, pages: List[Dict[str, Any]]) -> Tuple[int, int]:
    """
    Save crawl_results.json and individual page markdown files.
    Returns (saved_count, skipped_count)
    """
    os.makedirs(output_dir, exist_ok=True)

    # Save raw crawl results (entire object)
    results_path = os.path.join(output_dir, "crawl_results.json")
    with open(results_path, "w", encoding="utf-8") as f:
        json.dump(crawl_result, f, indent=2, ensure_ascii=False)

    saved = 0
    skipped = 0

    for i, page in enumerate(pages):
        markdown, meta = extract_markdown_and_meta(page)
        if not markdown:
            skipped += 1
            continue

        # Ensure extracted meta takes precedence
        filename = infer_filename_from_page(i, {**page, "metadata": meta})
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