#!/usr/bin/env python3
"""
Crawl Cascadeur Python API documentation using Firecrawl Python SDK
"""

import os
from firecrawl import FirecrawlApp
import json

def crawl_cascadeur_docs():
    """Crawl the Cascadeur Python API documentation"""
    
    # Initialize Firecrawl (you'll need your API key)
    api_key = os.getenv('FIRECRAWL_API_KEY')
    if not api_key:
        print("Please set FIRECRAWL_API_KEY environment variable")
        return
    
    app = FirecrawlApp(api_key=api_key)
    
    # Crawl configuration
    crawl_params = {
        'crawlerOptions': {
            'includes': ['**/python-api/**'],  # Only crawl Python API docs
            'excludes': ['**/search**', '**/genindex**'],  # Skip search and index pages
            'limit': 20,  # Limit number of pages
            'allowBackwardCrawling': False,
            'allowExternalContentLinks': False
        },
        'pageOptions': {
            'includeHtml': False,
            'includeRawHtml': False,
            'onlyMainContent': True,
            'waitFor': 1000,
            'screenshot': False,
            'fullPageScreenshot': False
        }
    }
    
    print("Starting crawl of Cascadeur Python API documentation...")
    
    try:
        # Start the crawl
        crawl_result = app.crawl_url(
            'https://cascadeur.com/python-api/',
            params=crawl_params
        )
        
        print(f"Crawl completed! Found {len(crawl_result)} pages")
        
        # Save results to files
        output_dir = "cascadeur_docs_crawled"
        os.makedirs(output_dir, exist_ok=True)
        
        # Save as JSON
        with open(f"{output_dir}/crawl_results.json", 'w', encoding='utf-8') as f:
            json.dump(crawl_result, f, indent=2, ensure_ascii=False)
        
        # Save individual markdown files
        for i, page in enumerate(crawl_result):
            if 'markdown' in page:
                # Create filename from URL
                url_path = page['metadata']['sourceURL'].replace('https://cascadeur.com/', '').replace('/', '_')
                filename = f"{output_dir}/{i:02d}_{url_path}.md"
                
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(f"# {page['metadata'].get('title', 'Untitled')}\n\n")
                    f.write(f"Source: {page['metadata']['sourceURL']}\n\n")
                    f.write(page['markdown'])
                
                print(f"Saved: {filename}")
        
        print(f"\nAll files saved to: {output_dir}/")
        return crawl_result
        
    except Exception as e:
        print(f"Error during crawl: {e}")
        return None

if __name__ == "__main__":
    crawl_cascadeur_docs()
