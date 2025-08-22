#!/usr/bin/env python
"""
Test the crawler with a limited number of pages to verify it works.
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from cascadeur_doc_crawler import CascadeurDocCrawler
import logging

# Modify the crawler to only crawl a few pages for testing
class TestCrawler(CascadeurDocCrawler):
    def crawl(self):
        """Modified crawl loop for testing - only crawl first 3 pages"""
        logger = logging.getLogger(__name__)
        logger.info("Starting TEST crawl (limited to 3 pages)...")
        
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
        
        # Limit to first 3 pages for testing
        test_pages = dict(list(remaining_pages.items())[:3])
        
        logger.info(f"TEST: Crawling {len(test_pages)} pages (out of {len(remaining_pages)} total)...")
        
        # Crawl pages
        for i, (page_url, symbols) in enumerate(test_pages.items(), 1):
            logger.info(f"Progress: {i}/{len(test_pages)} test pages")
            
            # Crawl the page
            self.crawl_page(page_url, symbols)
            
            # Save state after each page
            self.save_state()
        
        logger.info(f"TEST crawl complete! Extracted {self.state.extracted_symbols} symbols from {len(self.state.crawled_pages)} pages")
        
        # Create partial consolidated output
        self.create_consolidated_output()

def main():
    print("Running test crawler (limited to 3 pages)...")
    crawler = TestCrawler()
    
    try:
        crawler.crawl()
        print("\nTest crawl completed successfully!")
        print(f"Check output in: {crawler.state.to_dict()}")
    except Exception as e:
        print(f"Error during test crawl: {e}")
        raise

if __name__ == "__main__":
    main()