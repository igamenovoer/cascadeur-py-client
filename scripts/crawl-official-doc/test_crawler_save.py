#!/usr/bin/env python3
"""
Offline functional test for the crawler save pipeline.

This test:
- Sets CRAWL_OUTPUT_DIR to a test directory
- Loads functions from scripts/crawl-official-doc/crawl_cascadeur_docs.py via runpy
- Feeds mock crawl results and pages into save_results
- Verifies markdown files are saved into the configured output dir
"""

import os
import json
import runpy
from pathlib import Path


def main():
    # 1) Configure test output dir via env (tests resolve_output_dir env precedence)
    test_output_dir = "cascadeur-docs/python/_generate/firecrawl-test"
    os.environ["CRAWL_OUTPUT_DIR"] = test_output_dir

    # 2) Load the crawler module WITHOUT executing its main()
    mod = runpy.run_path("scripts/crawl-official-doc/crawl_cascadeur_docs.py", run_name="__not_main__")

    resolve_output_dir = mod["resolve_output_dir"]
    save_results = mod["save_results"]

    # 3) Resolve output dir (env precedence)
    resolved = resolve_output_dir(None)
    print(f"[TEST] Resolved output dir: {resolved}")
    if resolved != test_output_dir:
        raise SystemExit(f"[TEST] resolve_output_dir failed. Expected {test_output_dir}, got {resolved}")

    # 4) Prepare mock crawl result with various shapes
    pages = [
        {
            "markdown": "Content 1\n\nHello from page one.",
            "metadata": {"title": "Test Page One", "sourceURL": "https://cascadeur.com/python-api/t1"},
        },
        {
            # nested under data
            "data": {
                "markdown": "Content 2\n\nHello from page two.",
                "metadata": {"title": "Test Page Two", "sourceURL": "https://cascadeur.com/python-api/t2"},
            }
        },
        {
            # no markdown -> should be skipped
            "metadata": {"title": "No Markdown", "sourceURL": "https://cascadeur.com/python-api/nomd"},
        },
    ]

    crawl_result = {"status": "completed", "data": pages}

    # 5) Execute save
    saved, skipped = save_results(resolved, crawl_result, pages)
    print(json.dumps({"saved": saved, "skipped": skipped, "output_dir": resolved}, indent=2))

    # 6) Verify filesystem outputs
    out_path = Path(resolved)
    md_files = sorted(p.name for p in out_path.glob("*.md"))
    json_exists = (out_path / "crawl_results.json").exists()

    print(f"[TEST] Markdown files: {md_files}")
    print(f"[TEST] crawl_results.json exists: {json_exists}")

    # Basic assertions
    if saved < 2:
        raise SystemExit(f"[TEST] Expected at least 2 saved files, got {saved}")
    if skipped < 1:
        raise SystemExit(f"[TEST] Expected at least 1 skipped page, got {skipped}")
    if not json_exists:
        raise SystemExit("[TEST] Missing crawl_results.json")

    print("[TEST] PASS: Save pipeline functional and output dir honored.")


if __name__ == "__main__":
    main()