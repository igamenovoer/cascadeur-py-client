"""
Cascadeur API Documentation Crawler
A robust crawler for Sphinx-based documentation with retry logic and resume capability.
"""

import json
import hashlib
import time
import logging
from pathlib import Path
from typing import Set, Dict, List, Optional, Tuple
from dataclasses import dataclass, asdict
from datetime import datetime
from urllib.parse import urljoin, urlparse
import random

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import sphobjinv
from bs4 import BeautifulSoup
from collections import defaultdict

# Configure logging
log_dir = Path('tmp')
log_dir.mkdir(exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_dir / 'crawler.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Constants
BASE_URL = "https://cascadeur.com/python-api/"
INVENTORY_URL = urljoin(BASE_URL, "objects.inv")

# Use absolute paths based on project root
PROJECT_ROOT = Path(__file__).parent.parent.parent
OUTPUT_DIR = PROJECT_ROOT / "casey-docs"
STATE_DIR = PROJECT_ROOT / "tmp" / "crawler_state"
STATE_FILE = STATE_DIR / "crawler_state.json"
PROGRESS_FILE = STATE_DIR / "progress.json"

@dataclass
class CrawlState:
    """Track crawler state for recovery"""
    inventory_hash: str = ""
    total_pages: int = 0
    crawled_pages: Set[str] = None
    failed_pages: Set[str] = None
    total_symbols: int = 0
    extracted_symbols: int = 0
    last_update: str = ""
    
    def __post_init__(self):
        if self.crawled_pages is None:
            self.crawled_pages = set()
        if self.failed_pages is None:
            self.failed_pages = set()

    def to_dict(self):
        return {
            'inventory_hash': self.inventory_hash,
            'total_pages': self.total_pages,
            'crawled_pages': list(self.crawled_pages),
            'failed_pages': list(self.failed_pages),
            'total_symbols': self.total_symbols,
            'extracted_symbols': self.extracted_symbols,
            'last_update': self.last_update
        }
    
    @classmethod
    def from_dict(cls, data):
        state = cls()
        state.inventory_hash = data.get('inventory_hash', '')
        state.total_pages = data.get('total_pages', 0)
        state.crawled_pages = set(data.get('crawled_pages', []))
        state.failed_pages = set(data.get('failed_pages', []))
        state.total_symbols = data.get('total_symbols', 0)
        state.extracted_symbols = data.get('extracted_symbols', 0)
        state.last_update = data.get('last_update', '')
        return state

class RobustSession:
    """HTTP session with exponential backoff retry"""
    
    def __init__(self, max_retries=5, backoff_factor=0.5):
        self.session = requests.Session()
        
        # Configure retry strategy
        retry_strategy = Retry(
            total=max_retries,
            backoff_factor=backoff_factor,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["HEAD", "GET", "OPTIONS"]
        )
        
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)
        
        # Set reasonable timeout
        self.timeout = 30
        
        # Add headers
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def get(self, url, **kwargs):
        """GET with exponential backoff on failure"""
        kwargs.setdefault('timeout', self.timeout)
        
        for attempt in range(5):
            try:
                response = self.session.get(url, **kwargs)
                response.raise_for_status()
                return response
            except requests.exceptions.RequestException as e:
                wait_time = (2 ** attempt) + random.uniform(0, 1)
                logger.warning(f"Attempt {attempt + 1} failed for {url}: {e}. Waiting {wait_time:.2f}s")
                
                if attempt < 4:  # Don't sleep on last attempt
                    time.sleep(wait_time)
                else:
                    raise
        
        return None

class CascadeurDocCrawler:
    """Main crawler class"""
    
    def __init__(self):
        self.session = RobustSession()
        self.state = self.load_state()
        self.inventory = None
        self.pages_to_crawl = {}
        
        # Create directories
        OUTPUT_DIR.mkdir(exist_ok=True)
        STATE_DIR.mkdir(exist_ok=True)
        (OUTPUT_DIR / "pages").mkdir(exist_ok=True)
        (OUTPUT_DIR / "symbols").mkdir(exist_ok=True)
    
    def load_state(self) -> CrawlState:
        """Load previous crawler state if exists"""
        if STATE_FILE.exists():
            try:
                with open(STATE_FILE, 'r') as f:
                    data = json.load(f)
                state = CrawlState.from_dict(data)
                logger.info(f"Loaded previous state: {state.extracted_symbols}/{state.total_symbols} symbols crawled")
                return state
            except Exception as e:
                logger.error(f"Failed to load state: {e}")
        
        return CrawlState()
    
    def save_state(self):
        """Save current crawler state"""
        self.state.last_update = datetime.now().isoformat()
        with open(STATE_FILE, 'w') as f:
            json.dump(self.state.to_dict(), f, indent=2)
    
    def fetch_inventory(self) -> bool:
        """Fetch and parse objects.inv"""
        logger.info(f"Fetching inventory from {INVENTORY_URL}")
        
        try:
            response = self.session.get(INVENTORY_URL)
            inv_bytes = response.content
            
            # Check if inventory changed
            inv_hash = hashlib.sha256(inv_bytes).hexdigest()
            if inv_hash == self.state.inventory_hash:
                logger.info("Inventory unchanged, using cached data")
                # Still need to load it
                self.inventory = sphobjinv.Inventory(inv_bytes)
                return True
            
            logger.info("Inventory changed or new, parsing...")
            self.inventory = sphobjinv.Inventory(inv_bytes)
            self.state.inventory_hash = inv_hash
            self.state.total_symbols = len(self.inventory.objects)
            
            # Group symbols by page
            self.pages_to_crawl = defaultdict(list)
            for obj in self.inventory.objects:
                page_url = urljoin(BASE_URL, obj.uri.split('#')[0])
                self.pages_to_crawl[page_url].append(obj)
            
            self.state.total_pages = len(self.pages_to_crawl)
            logger.info(f"Found {self.state.total_symbols} symbols across {self.state.total_pages} pages")
            
            # Save inventory locally
            inv_path = OUTPUT_DIR / "objects.inv"
            with open(inv_path, 'wb') as f:
                f.write(inv_bytes)
            
            return True
            
        except Exception as e:
            logger.error(f"Failed to fetch inventory: {e}")
            return False
    
    def extract_symbol_doc(self, soup: BeautifulSoup, obj, page_url: str) -> Optional[Dict]:
        """Extract documentation for a single symbol"""
        anchor = obj.uri.split('#')[1] if '#' in obj.uri else None
        
        # Try to find the anchor
        node = None
        if anchor:
            # Direct ID match
            node = soup.find(id=anchor)
            
            # Fallback: partial match (for truncated IDs)
            if not node:
                node = soup.find(id=lambda x: x and x.startswith(anchor[:30]))
            
            # Fallback: search by class and text
            if not node:
                # Try to find by searching for the symbol name
                for tag in soup.find_all(['dt', 'h1', 'h2', 'h3', 'h4']):
                    if obj.name in tag.get_text():
                        node = tag
                        break
        
        if not node:
            logger.debug(f"Could not find anchor {anchor} for {obj.name} on {page_url}")
            return None
        
        # Extract signature
        sig_node = self._find_signature_node(node)
        signature_text = sig_node.get_text(' ', strip=True) if sig_node else ""
        
        # Extract documentation
        doc_text = self._extract_documentation(sig_node or node)
        
        return {
            "name": obj.name,
            "domain": obj.domain,
            "role": obj.role,
            "priority": obj.priority,
            "page_url": page_url,
            "anchor": anchor,
            "source_url": page_url + (f"#{anchor}" if anchor else ''),
            "signature": signature_text,
            "documentation": doc_text,
            "uri": obj.uri,
            "dispname": obj.dispname
        }
    
    def _find_signature_node(self, node):
        """Find the signature/heading node"""
        current = node
        for _ in range(6):
            if current.name in ('dt', 'h1', 'h2', 'h3', 'h4', 'code'):
                return current
            if current.parent:
                current = current.parent
        return node
    
    def _extract_documentation(self, sig_node):
        """Extract documentation text following a signature"""
        doc_parts = []
        
        # Look for dd element (definition)
        if sig_node.name == 'dt':
            dd = sig_node.find_next_sibling('dd')
            if dd:
                doc_parts.append(dd.get_text('\n', strip=True))
        
        # Look for following paragraphs
        for sibling in sig_node.find_next_siblings():
            if sibling.name in ('dt', 'h1', 'h2', 'h3', 'h4'):
                break  # Stop at next symbol
            if sibling.name in ('p', 'div', 'pre', 'blockquote'):
                text = sibling.get_text('\n', strip=True)
                if text:
                    doc_parts.append(text)
        
        return '\n\n'.join(doc_parts)
    
    def crawl_page(self, page_url: str, symbols: List) -> int:
        """Crawl a single page and extract symbols"""
        logger.info(f"Crawling {page_url} ({len(symbols)} symbols)")
        
        try:
            response = self.session.get(page_url)
            soup = BeautifulSoup(response.text, 'lxml')
            
            # Save the raw HTML
            page_path = OUTPUT_DIR / "pages" / (hashlib.md5(page_url.encode()).hexdigest() + ".html")
            with open(page_path, 'w', encoding='utf-8') as f:
                f.write(response.text)
            
            # Extract symbols
            extracted_count = 0
            symbols_data = []
            
            for obj in symbols:
                symbol_doc = self.extract_symbol_doc(soup, obj, page_url)
                if symbol_doc:
                    symbols_data.append(symbol_doc)
                    extracted_count += 1
            
            # Save symbols for this page
            if symbols_data:
                symbols_file = OUTPUT_DIR / "symbols" / (hashlib.md5(page_url.encode()).hexdigest() + ".json")
                with open(symbols_file, 'w', encoding='utf-8') as f:
                    json.dump(symbols_data, f, indent=2, ensure_ascii=False)
            
            self.state.crawled_pages.add(page_url)
            self.state.extracted_symbols += extracted_count
            
            logger.info(f"Extracted {extracted_count}/{len(symbols)} symbols from {page_url}")
            return extracted_count
            
        except Exception as e:
            logger.error(f"Failed to crawl {page_url}: {e}")
            self.state.failed_pages.add(page_url)
            return 0
    
    def crawl(self):
        """Main crawl loop"""
        logger.info("Starting Cascadeur documentation crawl...")
        
        # Fetch inventory
        if not self.fetch_inventory():
            logger.error("Failed to fetch inventory, aborting")
            return
        
        # Determine pages to crawl (skip already crawled)
        remaining_pages = {
            url: symbols 
            for url, symbols in self.pages_to_crawl.items() 
            if url not in self.state.crawled_pages
        }
        
        if not remaining_pages:
            logger.info("All pages already crawled!")
            return
        
        logger.info(f"Crawling {len(remaining_pages)} remaining pages...")
        
        # Crawl pages with progress tracking
        for i, (page_url, symbols) in enumerate(remaining_pages.items(), 1):
            logger.info(f"Progress: {i}/{len(remaining_pages)} pages")
            
            # Crawl the page
            self.crawl_page(page_url, symbols)
            
            # Save state after each page
            self.save_state()
            
            # Small delay to be polite
            time.sleep(0.5 + random.uniform(0, 0.5))
        
        # Retry failed pages once
        if self.state.failed_pages:
            logger.info(f"Retrying {len(self.state.failed_pages)} failed pages...")
            failed = list(self.state.failed_pages)
            self.state.failed_pages.clear()
            
            for page_url in failed:
                if page_url in self.pages_to_crawl:
                    self.crawl_page(page_url, self.pages_to_crawl[page_url])
                    self.save_state()
        
        # Create consolidated output
        self.create_consolidated_output()
        
        logger.info(f"Crawl complete! Extracted {self.state.extracted_symbols}/{self.state.total_symbols} symbols")
        logger.info(f"Successfully crawled {len(self.state.crawled_pages)}/{self.state.total_pages} pages")
        
        if self.state.failed_pages:
            logger.warning(f"Failed pages: {self.state.failed_pages}")
    
    def create_consolidated_output(self):
        """Create a consolidated JSON file with all symbols"""
        logger.info("Creating consolidated output...")
        
        all_symbols = []
        symbols_dir = OUTPUT_DIR / "symbols"
        
        for json_file in symbols_dir.glob("*.json"):
            with open(json_file, 'r', encoding='utf-8') as f:
                symbols = json.load(f)
                all_symbols.extend(symbols)
        
        # Sort by name and domain
        all_symbols.sort(key=lambda x: (x.get('domain', ''), x.get('name', '')))
        
        # Save consolidated file
        output_file = OUTPUT_DIR / "cascadeur_api_docs.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump({
                'metadata': {
                    'source': BASE_URL,
                    'timestamp': datetime.now().isoformat(),
                    'total_symbols': len(all_symbols),
                    'total_pages': self.state.total_pages
                },
                'symbols': all_symbols
            }, f, indent=2, ensure_ascii=False)
        
        logger.info(f"Consolidated output saved to {output_file}")
        
        # Also create a JSONL file for easier streaming
        jsonl_file = OUTPUT_DIR / "cascadeur_api_docs.jsonl"
        with open(jsonl_file, 'w', encoding='utf-8') as f:
            for symbol in all_symbols:
                f.write(json.dumps(symbol, ensure_ascii=False) + '\n')
        
        logger.info(f"JSONL output saved to {jsonl_file}")

def main():
    """Main entry point"""
    crawler = CascadeurDocCrawler()
    
    try:
        crawler.crawl()
    except KeyboardInterrupt:
        logger.info("Crawl interrupted by user, saving state...")
        crawler.save_state()
        logger.info("State saved. Run again to resume.")
    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
        crawler.save_state()
        raise

if __name__ == "__main__":
    main()