#!/usr/bin/env python
"""
Scrape Cascadeur Python API documentation using Firecrawl.

This script discovers and scrapes all API documentation pages,
converting them to markdown format with proper directory structure.

Optimized for Firecrawl free tier (2 concurrent requests, rate limits).
"""

import json
import os
import re
import time
import random
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import urlparse

from firecrawl import FirecrawlApp  # type: ignore[import-untyped]
from firecrawl.v2.types import MapData, LinkResult  # type: ignore[import-untyped]


class CascadeurAPIDocsScraper:
    """Scraper for Cascadeur Python API documentation.

    Improvements over original version:
    - Adaptive pacing respecting Firecrawl Free Tier limits (10 /scrape rpm, 2 concurrent browsers)
    - Configurable rate limit and max retries via CLI / env
    - Exponential backoff with jitter for rate limit / timeout
    - Persistent checkpoint (resume) support
    - Skip already scraped pages unless --force / TTL expired
    - Structured progress logging & periodic state flush
    """

    DEFAULT_SCRAPE_RPM = 10  # Free tier /scrape requests per minute
    DEFAULT_TIMEOUT_SECONDS = 90      # per-request timeout (seconds)
    DEFAULT_CACHE_MAX_AGE_SECONDS = 3600  # cache reuse window
    DEFAULT_MAX_RETRIES = 4
    STATE_FILENAME = "scrape_state.json"

    def __init__(self,
                 base_url: str = "https://cascadeur.com/python-api/",
                 output_dir: str = "../python",
                 scrape_rpm: Optional[int] = None,
                 max_retries: Optional[int] = None,
                 force: bool = False,
                 ttl_seconds: int = 6 * 3600,
                 state_path: Optional[str] = None) -> None:
        self.base_url = base_url.rstrip('/') + '/'
        self.output_dir = Path(output_dir).resolve()
        self.force = force
        self.ttl_seconds = ttl_seconds

        # Rate limiting configuration
        env_rpm = os.getenv("FIRECRAWL_SCRAPE_RPM")
        self.scrape_rpm = scrape_rpm or (int(env_rpm) if env_rpm else self.DEFAULT_SCRAPE_RPM)
        self.min_interval = 60.0 / max(self.scrape_rpm, 1)
        self.max_retries = max_retries or self.DEFAULT_MAX_RETRIES
        self.timeout_ms = int(self.DEFAULT_TIMEOUT_SECONDS * 1000)
        self.cache_max_age = self.DEFAULT_CACHE_MAX_AGE_SECONDS

        # Initialize Firecrawl with API key from environment
        api_key = os.getenv('FIRECRAWL_API_KEY')
        if not api_key:
            raise ValueError("FIRECRAWL_API_KEY environment variable not set")
        self.firecrawl = FirecrawlApp(api_key=api_key)

        # Track statistics
        self.stats = {
            'total_urls': 0,
            'scraped': 0,
            'skipped': 0,
            'failed': 0,
            'errors': 0
        }

        # Timing bookkeeping for adaptive pacing
        self._last_request_ts = 0.0

        # Persistent state
        self.state_path = Path(state_path) if state_path else (self.output_dir / self.STATE_FILENAME)
        self.state = self._load_state()

    # ------------------------------------------------------------
    # State management
    # ------------------------------------------------------------
    def _load_state(self) -> Dict[str, Any]:
        try:
            if self.state_path.exists():
                return json.loads(self.state_path.read_text(encoding='utf-8'))
        except Exception:
            pass
        return {"completed": {}, "failed": {}, "config": {"base_url": self.base_url}}

    def _save_state(self) -> None:
        try:
            self.state_path.parent.mkdir(parents=True, exist_ok=True)
            tmp = self.state_path.with_suffix('.tmp')
            tmp.write_text(json.dumps(self.state, indent=2), encoding='utf-8')
            tmp.replace(self.state_path)
        except Exception as e:
            print(f"[WARN] Failed to persist state: {e}")
    
    def discover_urls(self) -> List[str]:
        """Phase 1: Discover all API documentation URLs using Firecrawl map.
        
        Returns:
            List of discovered documentation URLs
        """
        print("[DISCOVER] Discovering API documentation URLs...")
        
        try:
            # Use Firecrawl map to discover all pages
            map_result: MapData = self.firecrawl.map(
                url=self.base_url,
                limit=1000  # Adjust based on expected documentation size
            )
            
            # Extract URLs from LinkResult objects
            api_urls: List[str] = []
            
            if hasattr(map_result, 'links') and map_result.links:
                for link in map_result.links:
                    if isinstance(link, LinkResult) and link.url:
                        # Filter for API documentation pages
                        if self._is_api_doc_url(link.url):
                            api_urls.append(link.url)
            
            # Remove duplicates while preserving order
            seen: set[str] = set()
            unique_urls: List[str] = []
            for url in api_urls:
                if url not in seen:
                    seen.add(url)
                    unique_urls.append(url)
            
            self.stats['total_urls'] = len(unique_urls)
            print(f"[SUCCESS] Discovered {len(unique_urls)} unique API documentation URLs")
            
            # Show sample URLs for verification
            if unique_urls:
                print("[LIST] Sample URLs found:")
                for i, url in enumerate(unique_urls[:5]):
                    print(f"  {i+1}. {url}")
                if len(unique_urls) > 5:
                    print(f"  ... and {len(unique_urls) - 5} more")
            
            return unique_urls
            
        except Exception as e:
            print(f"[ERROR] Discovery failed: {e}")
            self.stats['errors'] += 1
            return []
    
    def _is_api_doc_url(self, url: str) -> bool:
        """Check if URL is an API documentation page.
        
        Args:
            url: URL to check
            
        Returns:
            True if URL is an API documentation page
        """
        # Include pages under the base URL
        if not url.startswith(self.base_url):
            return False
        
        # Exclude non-documentation pages
        exclude_patterns = [
            r'/search',
            r'/index\.html?$',
            r'#',  # Anchor links
            r'\.(?:css|js|png|jpg|gif|svg|ico)$',  # Assets
        ]
        
        for pattern in exclude_patterns:
            if re.search(pattern, url):
                return False
        
        # Include pages with API patterns
        include_patterns = [
            r'/_generate/',  # Generated API docs
            r'/csc\.',  # CSC module pages
            r'/modules/',  # Module pages
        ]
        
        for pattern in include_patterns:
            if re.search(pattern, url):
                return True
        
        # Default: include if under base URL
        return True
    
    def _rate_limit_sleep(self) -> None:
        now = time.time()
        elapsed = now - self._last_request_ts
        if self._last_request_ts > 0 and elapsed < self.min_interval:
            # Add small random jitter (±15%) to desynchronize patterns
            base_sleep = self.min_interval - elapsed
            jitter = base_sleep * random.uniform(-0.15, 0.15)
            sleep_time = max(0.0, base_sleep + jitter)
            time.sleep(sleep_time)
        self._last_request_ts = time.time()

    def _should_skip(self, url: str, file_path: Path) -> bool:
        if self.force:
            return False
        if not file_path.exists():
            return False
        # TTL check
        age = time.time() - file_path.stat().st_mtime
        if age > self.ttl_seconds:
            return False
        # Already scraped & fresh
        return True

    def sequential_scrape(self, urls: List[str]) -> List[Dict[str, Any]]:
        print(f"[SCRAPE] Sequential mode (Free Tier). Target RPM={self.scrape_rpm}, interval≈{self.min_interval:.2f}s")
        all_results: List[Dict[str, Any]] = []

        for i, url in enumerate(urls, 1):
            existing_path = self.output_dir / self._url_to_filepath(url)
            if self._should_skip(url, existing_path):
                self.stats['skipped'] += 1
                self.state['completed'][url] = {"skipped": True, "path": str(existing_path)}
                if i % 5 == 0:
                    self._save_state()
                continue

            print(f"[PROGRESS] {i}/{len(urls)}: {url}")
            retry = 0
            backoff_base = 8  # seconds
            while retry <= self.max_retries:
                # Respect pacing before each attempt (except immediate first if large gap already elapsed)
                if retry == 0:
                    self._rate_limit_sleep()
                try:
                    # Firecrawl Python SDK expects camelCase option names; timeout in ms
                    # Use minimal arguments to avoid signature mismatches; rely on defaults for main content & timeout
                    result = self.firecrawl.scrape(
                        url=url,
                        formats=['markdown']
                    )
                    md = getattr(result, 'markdown', None) if result else None
                    title = ''
                    if result and hasattr(result, 'metadata') and isinstance(result.metadata, dict):
                        title = result.metadata.get('title', '')
                    if md:
                        rec = {'url': url, 'markdown': md, 'title': title, 'success': True}
                        all_results.append(rec)
                        self.stats['scraped'] += 1
                        self.state['completed'][url] = {"success": True, "title": title}
                        print(f"[SUCCESS] {url}")
                    else:
                        warn_msg = 'No content'
                        rec = {'url': url, 'success': False, 'error': warn_msg}
                        all_results.append(rec)
                        self.stats['failed'] += 1
                        self.state['failed'][url] = {"error": warn_msg}
                        print(f"[WARNING] {warn_msg} {url}")
                    break  # exit retry loop
                except Exception as e:
                    err = str(e)
                    transient = any(k in err.lower() for k in ["rate limit", "timeout", "timed out", "429", "too many"])
                    retry += 1
                    if transient and retry <= self.max_retries:
                        sleep_for = backoff_base * (2 ** (retry - 1))
                        # Cap sleep so we don't exceed cache TTL; add jitter
                        sleep_for = min(sleep_for, 180) * random.uniform(0.85, 1.15)
                        print(f"[RETRY {retry}/{self.max_retries}] transient error: {err[:120]} | sleeping {sleep_for:.1f}s")
                        time.sleep(sleep_for)
                        continue
                    # Permanent failure or exhausted retries
                    print(f"[ERROR] {url} -> {err[:200]}")
                    all_results.append({'url': url, 'success': False, 'error': err})
                    self.stats['failed'] += 1
                    self.state['failed'][url] = {"error": err}
                    break
            if i % 5 == 0:
                self._save_state()

        # Final state flush
        self._save_state()
        return all_results
    
    def process_and_save(self, results: List[Dict[str, Any]]) -> None:
        """Phase 3: Process scraped content and save with proper directory structure.
        
        Args:
            results: List of scraping results to process and save
        """
        print("[PROCESS] Processing and saving documentation...")
        
        # Create output directory
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Track saved files for index generation
        saved_files: List[Tuple[str, str, str]] = []  # (path, title, module)
        
        for result in results:
            if not result.get('success'):
                continue
            
            url = result['url']
            markdown = result['markdown']
            title = result.get('title', '')
            
            # Determine file path based on URL structure
            file_path = self._url_to_filepath(url)
            full_path = self.output_dir / file_path
            
            # Create parent directories
            full_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Add metadata header to markdown
            enhanced_markdown = self._add_metadata(markdown, url, title)
            
            # Save the file
            try:
                full_path.write_text(enhanced_markdown, encoding='utf-8')
                
                # Extract module name for categorization
                module = self._extract_module(url, title)
                saved_files.append((str(file_path), title, module))
                
                print(f"[SAVED] {file_path}")
                
            except Exception as e:
                print(f"[ERROR] Failed to save {file_path}: {e}")
                self.stats['errors'] += 1
        
        # Generate index files
        self._generate_index(saved_files)
        
        print("[SUCCESS] Documentation processing complete!")
    
    def _url_to_filepath(self, url: str) -> Path:
        """Convert URL to appropriate file path.
        
        Args:
            url: URL to convert
            
        Returns:
            Path object for the file
        """
        # Parse URL
        parsed = urlparse(url)
        path = parsed.path
        
        # Remove base path
        base_path = urlparse(self.base_url).path
        if path.startswith(base_path):
            path = path[len(base_path):]
        
        # Clean up path
        path = path.strip('/')
        
        # Handle different URL patterns
        if '/_generate/' in path:
            # Extract class/function name from generated docs
            parts = path.split('/_generate/')[-1]
            if parts.endswith('.html'):
                parts = parts[:-5]  # Remove .html
            
            # Split by dots to create directory structure
            components = parts.split('.')
            if len(components) > 2 and components[0] == 'csc':
                # e.g., csc.model.ClassName -> model/ClassName.md
                module = components[1]
                name = '.'.join(components[2:])
                return Path(module) / f"{name}.md"
        
        # Default: use URL path structure
        if path.endswith('.html'):
            path = path[:-5]  # Remove .html
        
        # Ensure .md extension
        if not path.endswith('.md'):
            path += '.md'
        
        return Path(path)
    
    def _extract_module(self, url: str, title: str) -> str:
        """Extract module name from URL or title.
        
        Args:
            url: Page URL
            title: Page title
            
        Returns:
            Module name
        """
        # Try to extract from URL
        if 'csc.' in url:
            match = re.search(r'csc\.([a-z_]+)', url)
            if match:
                return f"csc.{match.group(1)}"
        
        # Try to extract from title
        if 'csc.' in title:
            match = re.search(r'csc\.([a-z_]+)', title)
            if match:
                return f"csc.{match.group(1)}"
        
        return "csc"
    
    def _add_metadata(self, markdown: str, url: str, title: str) -> str:
        """Add metadata header to markdown content.
        
        Args:
            markdown: Original markdown content
            url: Source URL
            title: Page title
            
        Returns:
            Enhanced markdown with metadata
        """
        metadata = [
            "---",
            f"title: {title}",
            f"source: {url}",
            f"scraped: {time.strftime('%Y-%m-%d %H:%M:%S')}",
            "---",
            "",
        ]
        
        return '\n'.join(metadata) + markdown
    
    def _generate_index(self, saved_files: List[Tuple[str, str, str]]) -> None:
        """Generate index files for navigation.
        
        Args:
            saved_files: List of (path, title, module) tuples
        """
        print("[INDEX] Generating index files...")
        
        # Generate main README
        readme_path = self.output_dir / "README.md"
        readme_content = [
            "# Cascadeur Python API Documentation",
            "",
            f"Generated: {time.strftime('%Y-%m-%d %H:%M:%S')}",
            f"Total pages: {len(saved_files)}",
            "",
            "## Modules",
            "",
        ]
        
        # Group files by module
        modules: Dict[str, List[Tuple[str, str]]] = {}
        for path, title, module in saved_files:
            if module not in modules:
                modules[module] = []
            modules[module].append((path, title))
        
        # Sort modules and add to README
        for module in sorted(modules.keys()):
            readme_content.append(f"### {module}")
            readme_content.append("")
            
            # Sort files within module
            for path, title in sorted(modules[module]):
                readme_content.append(f"- [{title or path}]({path})")
            readme_content.append("")
        
        # Add statistics
        readme_content.extend([
            "## Statistics",
            "",
            f"- Total URLs discovered: {self.stats['total_urls']}",
            f"- Successfully scraped: {self.stats['scraped']}",
            f"- Failed: {self.stats['failed']}",
            f"- Errors: {self.stats['errors']}",
            "",
        ])
        
        readme_path.write_text('\n'.join(readme_content), encoding='utf-8')
        print(f"[SAVED] {readme_path}")
        
        # Generate JSON reference
        json_path = self.output_dir / "api_reference.json"
        api_reference = {
            "generated": time.strftime('%Y-%m-%d %H:%M:%S'),
            "stats": self.stats,
            "modules": modules,
            "files": [
                {
                    "path": path,
                    "title": title,
                    "module": module
                }
                for path, title, module in saved_files
            ]
        }
        
        json_path.write_text(json.dumps(api_reference, indent=2), encoding='utf-8')
        print(f"[SAVED] {json_path}")
    
    def run(self) -> None:
        """Run the complete scraping pipeline."""
        print("=== Starting Cascadeur API Documentation Scraper ===")
        print("=== Optimized for Firecrawl Free Tier ===")
        print(f"Base URL: {self.base_url}")
        print(f"Output Directory: {self.output_dir}")
        print(f"Requests / min target: {self.scrape_rpm} (interval ≈ {self.min_interval:.2f}s)")
        print(f"Force re-scrape: {self.force} | TTL: {self.ttl_seconds}s")
        print(f"Max retries: {self.max_retries}")
        print(f"State file: {self.state_path}")
        print(f"API Key: {'SET' if os.getenv('FIRECRAWL_API_KEY') else 'NOT SET'}")
        print("")

        # Phase 1: Discovery
        print("Phase 1: Discovering API documentation URLs...")
        urls = self.discover_urls()

        if not urls:
            print("ERROR: No URLs discovered. Check the base URL and try again.")
            return

        # Phase 2: Sequential Scraping (optimized for free tier)
        print("")
        print("Phase 2: Sequential scraping documentation pages...")
        results = self.sequential_scrape(urls)

        if not results:
            print("ERROR: No content scraped. Check your API key and network connection.")
            return

        # Phase 3: Processing and Saving
        print("")
        print("Phase 3: Processing and saving documentation...")
        self.process_and_save(results)

        # Final statistics
        print("")
        print("=== Scraping Complete ===")
        print(f"Total URLs: {self.stats['total_urls']}")
        print(f"Scraped: {self.stats['scraped']}")
        print(f"Skipped (fresh): {self.stats.get('skipped', 0)}")
        print(f"Failed: {self.stats['failed']}")
        print(f"Errors: {self.stats['errors']}")
        print(f"Output: {self.output_dir}")
        # Fallback suggestion if mostly failed
        if self.stats['scraped'] == 0 and self.stats['failed'] >= self.stats['total_urls']:
            print("[HINT] All scrapes failed. Possible causes: wrong parameter casing, timeout too low, or site requires crawl. Try using the crawl endpoint (single request) to gather pages or increase --rpm to 5 and --timeout to 120s.")


def main() -> None:
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Scrape Cascadeur Python API documentation (optimized for free tier)"
    )
    parser.add_argument("-o", "--output", default="../python", help="Output directory (default: ../python)")
    parser.add_argument("--rpm", type=int, default=None, help="Target /scrape requests per minute (default 10 free tier)")
    parser.add_argument("--max-retries", type=int, default=None, help="Max retries for transient errors (default 4)")
    parser.add_argument("--force", action="store_true", help="Force re-scrape even if file exists and fresh")
    parser.add_argument("--ttl", type=int, default=6*3600, help="Freshness TTL seconds to skip existing (default 6h)")
    parser.add_argument("--state", default=None, help="Path to persistent state JSON (default <output>/scrape_state.json)")
    
    args = parser.parse_args()
    
    try:
        scraper = CascadeurAPIDocsScraper(
            output_dir=args.output,
            scrape_rpm=args.rpm,
            max_retries=args.max_retries,
            force=args.force,
            ttl_seconds=args.ttl,
            state_path=args.state
        )
        scraper.run()
    except KeyboardInterrupt:
        print("\n[INTERRUPTED] Scraping cancelled by user")
    except Exception as e:
        print(f"\n[FATAL ERROR] {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()