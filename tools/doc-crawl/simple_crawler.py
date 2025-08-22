#!/usr/bin/env python
"""
Simplified Cascadeur documentation crawler.
Downloads HTML pages and saves them without complex parsing.
"""

import json
import hashlib
import time
import logging
from pathlib import Path
from urllib.parse import urljoin, urlparse
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import sphobjinv
from collections import defaultdict
from datetime import datetime

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

class SimpleCrawler:
    def __init__(self):
        self.session = self.create_session()
        self.pages = set()
        self.inventory_data = []
        
        # Create output directory
        OUTPUT_DIR.mkdir(exist_ok=True)
        (OUTPUT_DIR / "html").mkdir(exist_ok=True)
    
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
    
    def download_inventory(self):
        """Download and parse objects.inv"""
        logger.info(f"Downloading inventory from {INVENTORY_URL}")
        
        try:
            response = self.session.get(INVENTORY_URL, timeout=30)
            response.raise_for_status()
            
            # Save inventory
            inv_path = OUTPUT_DIR / "objects.inv"
            with open(inv_path, 'wb') as f:
                f.write(response.content)
            
            # Parse inventory
            inventory = sphobjinv.Inventory(response.content)
            
            # Extract pages and save inventory data
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
                self.pages.add(page_url)
            
            # Save inventory as JSON for easier processing
            self.inventory_data = []
            for page_url, symbols in pages_dict.items():
                self.inventory_data.append({
                    'page_url': page_url,
                    'symbol_count': len(symbols),
                    'symbols': symbols
                })
            
            inv_json_path = OUTPUT_DIR / "inventory.json"
            with open(inv_json_path, 'w', encoding='utf-8') as f:
                json.dump({
                    'metadata': {
                        'source': BASE_URL,
                        'timestamp': datetime.now().isoformat(),
                        'total_pages': len(self.pages),
                        'total_symbols': len(inventory.objects)
                    },
                    'pages': self.inventory_data
                }, f, indent=2, ensure_ascii=False)
            
            logger.info(f"Found {len(inventory.objects)} symbols across {len(self.pages)} pages")
            logger.info(f"Inventory saved to {inv_json_path}")
            
            return True
            
        except Exception as e:
            logger.error(f"Failed to download inventory: {e}")
            return False
    
    def download_page(self, url):
        """Download a single HTML page"""
        try:
            logger.info(f"Downloading {url}")
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            
            # Generate filename from URL
            url_hash = hashlib.md5(url.encode()).hexdigest()
            filename = f"{url_hash}.html"
            filepath = OUTPUT_DIR / "html" / filename
            
            # Save HTML
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(response.text)
            
            logger.info(f"Saved to {filename}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to download {url}: {e}")
            return False
    
    def download_all_pages(self, limit=None):
        """Download all pages found in inventory"""
        pages_to_download = list(self.pages)
        
        if limit:
            pages_to_download = pages_to_download[:limit]
            logger.info(f"Limiting download to {limit} pages")
        
        # Create index file
        index = []
        
        logger.info(f"Downloading {len(pages_to_download)} pages...")
        
        for i, url in enumerate(pages_to_download, 1):
            logger.info(f"Progress: {i}/{len(pages_to_download)}")
            
            if self.download_page(url):
                url_hash = hashlib.md5(url.encode()).hexdigest()
                index.append({
                    'url': url,
                    'filename': f"{url_hash}.html",
                    'downloaded': datetime.now().isoformat()
                })
                
                # Small delay to be polite
                time.sleep(0.5)
        
        # Save index
        index_path = OUTPUT_DIR / "pages_index.json"
        with open(index_path, 'w', encoding='utf-8') as f:
            json.dump(index, f, indent=2, ensure_ascii=False)
        
        logger.info(f"Downloaded {len(index)} pages")
        logger.info(f"Index saved to {index_path}")
    
    def run(self, page_limit=None):
        """Run the crawler"""
        logger.info("Starting simple Cascadeur documentation crawler...")
        
        # Download inventory
        if not self.download_inventory():
            logger.error("Failed to download inventory")
            return False
        
        # Download pages
        self.download_all_pages(limit=page_limit)
        
        logger.info("Crawl complete!")
        logger.info(f"Output saved to: {OUTPUT_DIR}")
        
        # Print summary
        print("\n" + "="*50)
        print("SUMMARY")
        print("="*50)
        print(f"Output directory: {OUTPUT_DIR}")
        print(f"Inventory: {OUTPUT_DIR / 'inventory.json'}")
        print(f"HTML pages: {OUTPUT_DIR / 'html'}")
        print(f"Pages index: {OUTPUT_DIR / 'pages_index.json'}")
        
        return True

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Simple Cascadeur Documentation Crawler")
    parser.add_argument('--limit', type=int, help='Limit number of pages to download')
    args = parser.parse_args()
    
    crawler = SimpleCrawler()
    crawler.run(page_limit=args.limit)

if __name__ == "__main__":
    main()