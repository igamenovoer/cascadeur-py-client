#!/usr/bin/env python
"""
Batch crawler for Cascadeur documentation.
Downloads pages in batches with resume capability.
"""

import json
import hashlib
import time
import logging
from pathlib import Path
from urllib.parse import urljoin
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import sphobjinv
from collections import defaultdict
from datetime import datetime
import sys

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Constants
BASE_URL = "https://cascadeur.com/python-api/"
INVENTORY_URL = urljoin(BASE_URL, "objects.inv")
PROJECT_ROOT = Path(__file__).parent.parent.parent
OUTPUT_DIR = PROJECT_ROOT / "casey-docs"
STATE_FILE = PROJECT_ROOT / "tmp" / "batch_crawler_state.json"

class BatchCrawler:
    def __init__(self, batch_size=10):
        self.batch_size = batch_size
        self.session = self.create_session()
        self.state = self.load_state()
        
        # Create directories
        OUTPUT_DIR.mkdir(exist_ok=True)
        (OUTPUT_DIR / "html").mkdir(exist_ok=True)
        STATE_FILE.parent.mkdir(exist_ok=True, parents=True)
    
    def create_session(self):
        """Create HTTP session with retry"""
        session = requests.Session()
        retry = Retry(
            total=3,
            backoff_factor=0.5,
            status_forcelist=[429, 500, 502, 503, 504]
        )
        adapter = HTTPAdapter(max_retries=retry)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        return session
    
    def load_state(self):
        """Load previous state if exists"""
        if STATE_FILE.exists():
            with open(STATE_FILE, 'r') as f:
                return json.load(f)
        return {
            'downloaded_urls': [],
            'failed_urls': [],
            'last_batch': 0
        }
    
    def save_state(self):
        """Save current state"""
        with open(STATE_FILE, 'w') as f:
            json.dump(self.state, f, indent=2)
    
    def load_inventory(self):
        """Load inventory from file or download"""
        inv_json_path = OUTPUT_DIR / "inventory.json"
        
        if inv_json_path.exists():
            logger.info("Loading existing inventory...")
            with open(inv_json_path, 'r') as f:
                data = json.load(f)
            return [page['page_url'] for page in data['pages']]
        
        logger.info("Downloading inventory...")
        try:
            response = self.session.get(INVENTORY_URL, timeout=30)
            response.raise_for_status()
            
            # Save raw inventory
            inv_path = OUTPUT_DIR / "objects.inv"
            with open(inv_path, 'wb') as f:
                f.write(response.content)
            
            # Parse and extract pages
            inventory = sphobjinv.Inventory(response.content)
            pages_dict = defaultdict(list)
            
            for obj in inventory.objects:
                page = obj.uri.split('#')[0]
                page_url = urljoin(BASE_URL, page)
                pages_dict[page_url].append({
                    'name': obj.name,
                    'domain': obj.domain,
                    'role': obj.role,
                    'priority': obj.priority,
                    'uri': obj.uri,
                    'dispname': obj.dispname
                })
            
            # Save as JSON
            inventory_data = []
            for page_url, symbols in pages_dict.items():
                inventory_data.append({
                    'page_url': page_url,
                    'symbol_count': len(symbols),
                    'symbols': symbols
                })
            
            with open(inv_json_path, 'w', encoding='utf-8') as f:
                json.dump({
                    'metadata': {
                        'source': BASE_URL,
                        'timestamp': datetime.now().isoformat(),
                        'total_pages': len(pages_dict),
                        'total_symbols': len(inventory.objects)
                    },
                    'pages': inventory_data
                }, f, indent=2, ensure_ascii=False)
            
            logger.info(f"Found {len(inventory.objects)} symbols across {len(pages_dict)} pages")
            return list(pages_dict.keys())
            
        except Exception as e:
            logger.error(f"Failed to download inventory: {e}")
            return []
    
    def download_page(self, url):
        """Download a single page"""
        try:
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            
            # Save HTML
            url_hash = hashlib.md5(url.encode()).hexdigest()
            filepath = OUTPUT_DIR / "html" / f"{url_hash}.html"
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(response.text)
            
            return True
            
        except Exception as e:
            logger.error(f"Failed to download {url}: {e}")
            return False
    
    def run(self):
        """Run the batch crawler"""
        logger.info("Starting batch crawler...")
        
        # Load all pages
        all_pages = self.load_inventory()
        if not all_pages:
            logger.error("No pages to download")
            return
        
        # Filter out already downloaded
        downloaded_set = set(self.state['downloaded_urls'])
        remaining_pages = [url for url in all_pages if url not in downloaded_set]
        
        if not remaining_pages:
            logger.info("All pages already downloaded!")
            return
        
        logger.info(f"Total pages: {len(all_pages)}")
        logger.info(f"Already downloaded: {len(downloaded_set)}")
        logger.info(f"Remaining: {len(remaining_pages)}")
        
        # Process in batches
        total_batches = (len(remaining_pages) + self.batch_size - 1) // self.batch_size
        
        for batch_num in range(total_batches):
            batch_start = batch_num * self.batch_size
            batch_end = min(batch_start + self.batch_size, len(remaining_pages))
            batch_pages = remaining_pages[batch_start:batch_end]
            
            logger.info(f"\nBatch {batch_num + 1}/{total_batches} ({len(batch_pages)} pages)")
            logger.info("-" * 50)
            
            for i, url in enumerate(batch_pages, 1):
                logger.info(f"  [{i}/{len(batch_pages)}] Downloading {url}")
                
                if self.download_page(url):
                    self.state['downloaded_urls'].append(url)
                    logger.info(f"  [{i}/{len(batch_pages)}] Success")
                else:
                    self.state['failed_urls'].append(url)
                    logger.info(f"  [{i}/{len(batch_pages)}] Failed")
                
                # Small delay
                time.sleep(0.3)
            
            # Save state after each batch
            self.state['last_batch'] = batch_num + 1
            self.save_state()
            logger.info(f"Batch {batch_num + 1} complete. State saved.")
        
        # Create index
        self.create_index()
        
        # Print summary
        print("\n" + "="*50)
        print("CRAWL COMPLETE")
        print("="*50)
        print(f"Total downloaded: {len(self.state['downloaded_urls'])}")
        print(f"Failed: {len(self.state['failed_urls'])}")
        print(f"Output directory: {OUTPUT_DIR}")
        
        if self.state['failed_urls']:
            print("\nFailed URLs:")
            for url in self.state['failed_urls'][:10]:
                print(f"  - {url}")
            if len(self.state['failed_urls']) > 10:
                print(f"  ... and {len(self.state['failed_urls']) - 10} more")
    
    def create_index(self):
        """Create index of downloaded pages"""
        index = []
        
        for url in self.state['downloaded_urls']:
            url_hash = hashlib.md5(url.encode()).hexdigest()
            index.append({
                'url': url,
                'filename': f"{url_hash}.html"
            })
        
        index_path = OUTPUT_DIR / "pages_index.json"
        with open(index_path, 'w', encoding='utf-8') as f:
            json.dump(index, f, indent=2, ensure_ascii=False)
        
        logger.info(f"Index saved to {index_path}")

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Batch Cascadeur Documentation Crawler")
    parser.add_argument('--batch-size', type=int, default=10, 
                       help='Number of pages per batch (default: 10)')
    parser.add_argument('--reset', action='store_true',
                       help='Reset crawler state and start fresh')
    
    args = parser.parse_args()
    
    if args.reset:
        if STATE_FILE.exists():
            STATE_FILE.unlink()
            print("State reset. Starting fresh.")
    
    crawler = BatchCrawler(batch_size=args.batch_size)
    
    try:
        crawler.run()
    except KeyboardInterrupt:
        print("\n\nInterrupted! State saved. Run again to resume.")
        crawler.save_state()
        sys.exit(0)

if __name__ == "__main__":
    main()