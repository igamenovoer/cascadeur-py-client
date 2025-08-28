#!/usr/bin/env python3
"""
Direct API approach to crawl Cascadeur documentation using Firecrawl API
"""

import requests
import json
import time
import os
from typing import Dict, List, Optional

class FirecrawlDirectAPI:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.firecrawl.dev/v1"
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
    
    def scrape(self, url: str, options: Optional[Dict] = None) -> Dict:
        """Scrape a single URL"""
        payload = {"url": url}
        if options:
            payload.update(options)
        
        response = requests.post(
            f"{self.base_url}/scrape",
            headers=self.headers,
            json=payload
        )
        response.raise_for_status()
        return response.json()
    
    def crawl(self, url: str, options: Optional[Dict] = None) -> str:
        """Start a crawl job and return job ID"""
        payload = {"url": url}
        if options:
            payload.update(options)
        
        response = requests.post(
            f"{self.base_url}/crawl",
            headers=self.headers,
            json=payload
        )
        response.raise_for_status()
        return response.json()["id"]
    
    def get_crawl_status(self, job_id: str) -> Dict:
        """Get crawl job status"""
        response = requests.get(
            f"{self.base_url}/crawl/{job_id}",
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()
    
    def wait_for_crawl(self, job_id: str, timeout: int = 300) -> Dict:
        """Wait for crawl to complete"""
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            status = self.get_crawl_status(job_id)
            
            if status["status"] == "completed":
                return status
            elif status["status"] == "failed":
                raise Exception(f"Crawl failed: {status.get('error', 'Unknown error')}")
            
            print(f"Crawl status: {status['status']} - {status.get('current', 0)}/{status.get('total', '?')} pages")
            time.sleep(10)
        
        raise TimeoutError(f"Crawl did not complete within {timeout} seconds")

def crawl_cascadeur_api_docs():
    """Crawl Cascadeur Python API docs using direct API"""
    
    # Get API key
    api_key = os.getenv('FIRECRAWL_API_KEY')
    if not api_key:
        print("❌ Please set FIRECRAWL_API_KEY environment variable")
        print("Get your API key from: https://firecrawl.dev/")
        return
    
    # Initialize API client
    client = FirecrawlDirectAPI(api_key)
    
    # Crawl options
    crawl_options = {
        "limit": 15,
        "scrapeOptions": {
            "formats": ["markdown"],
            "onlyMainContent": True,
            "waitFor": 1000
        },
        "crawlerOptions": {
            "includes": ["**/python-api/**"],
            "excludes": ["**/search**", "**/genindex**", "**/_static/**"],
            "allowBackwardCrawling": False,
            "allowExternalContentLinks": False
        }
    }
    
    try:
        print("🔥 Starting Cascadeur Python API documentation crawl...")
        
        # Start crawl
        job_id = client.crawl("https://cascadeur.com/python-api/", crawl_options)
        print(f"📋 Crawl job started: {job_id}")
        
        # Wait for completion
        result = client.wait_for_crawl(job_id)
        
        if result["status"] == "completed":
            pages = result["data"]
            print(f"✅ Crawl completed! Found {len(pages)} pages")
            
            # Save results
            output_dir = "cascadeur_api_docs"
            os.makedirs(output_dir, exist_ok=True)
            
            # Save complete results as JSON
            with open(f"{output_dir}/crawl_results.json", 'w', encoding='utf-8') as f:
                json.dump(result, f, indent=2, ensure_ascii=False)
            
            # Save individual markdown files
            for i, page in enumerate(pages):
                if 'markdown' in page:
                    # Create safe filename
                    title = page.get('metadata', {}).get('title', f'page_{i}')
                    safe_title = "".join(c for c in title if c.isalnum() or c in (' ', '-', '_')).rstrip()
                    filename = f"{output_dir}/{i:02d}_{safe_title[:50]}.md"
                    
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write(f"# {page.get('metadata', {}).get('title', 'Untitled')}\n\n")
                        f.write(f"**Source:** {page.get('metadata', {}).get('sourceURL', 'Unknown')}\n\n")
                        f.write("---\n\n")
                        f.write(page.get('markdown', ''))
                    
                    print(f"📄 Saved: {filename}")
            
            print(f"\n🎉 All documentation saved to: {output_dir}/")
            return result
            
    except Exception as e:
        print(f"❌ Error during crawl: {e}")
        return None

def scrape_single_page():
    """Example: Scrape just the main documentation page"""
    api_key = os.getenv('FIRECRAWL_API_KEY')
    if not api_key:
        print("❌ Please set FIRECRAWL_API_KEY environment variable")
        return
    
    client = FirecrawlDirectAPI(api_key)
    
    try:
        print("📄 Scraping main documentation page...")
        result = client.scrape("https://cascadeur.com/python-api/", {
            "formats": ["markdown"],
            "onlyMainContent": True
        })
        
        if 'markdown' in result['data']:
            with open('cascadeur_main_docs.md', 'w', encoding='utf-8') as f:
                f.write(result['data']['markdown'])
            print("✅ Saved main documentation to: cascadeur_main_docs.md")
        
        return result
        
    except Exception as e:
        print(f"❌ Error scraping page: {e}")
        return None

if __name__ == "__main__":
    print("🔥 Firecrawl Direct API - Cascadeur Documentation Crawler")
    print("=" * 60)
    
    choice = input("Choose option:\n1. Crawl all documentation (recommended)\n2. Scrape main page only\nEnter choice (1/2): ")
    
    if choice == "1":
        crawl_cascadeur_api_docs()
    elif choice == "2":
        scrape_single_page()
    else:
        print("Invalid choice. Please run again and select 1 or 2.")
