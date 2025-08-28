# How to Scrape Cascadeur Python API Documentation

## Overview

This guide explains how to scrape the official Cascadeur Python API documentation using Firecrawl. The documentation is available at `https://cascadeur.com/python-api/` and follows a structured format that we can systematically crawl and convert to markdown.

## Prerequisites

### Install Firecrawl Python SDK

```bash
pip install firecrawl-py
```

### Get Firecrawl API Key

1. Sign up at [firecrawl.dev](https://firecrawl.dev)
2. Get your API key from the dashboard
3. Set environment variable:
   ```bash
   export FIRECRAWL_API_KEY="fc-YOUR-API-KEY"
   ```

## Understanding Cascadeur API Documentation Structure

### Website Analysis

**Base URL**: `https://cascadeur.com/python-api/`

**Documentation Pattern**:
- Generated docs are in `_generate/` folder
- Follow format: `csc.<module>.<class>.html`
- Main modules include:
  - `csc.model` - Core model classes
  - `csc.layers` - Layer management
  - `csc.tools` - Animation tools
  - `csc.view` - UI and viewport
  - `csc.domain` - Scene domain
  - `csc.rig` - Rigging functionality
  - `csc.fbx` - FBX import/export
  - `csc.update` - Update system
  - `csc.math` - Mathematical operations
  - `csc.physics` - Physics simulation

### Content Structure

Each API page contains:
- Class name and description
- Constructor information
- Methods table with signatures
- Detailed method documentation
- Parameter types and return values
- Cross-references to related classes

## Scraping Strategy

### Phase 1: Discovery - Map All Documentation URLs

Use Firecrawl's **map** functionality to discover all documentation pages:

```python
from firecrawl import Firecrawl
import os
from pathlib import Path
import json
import time

# Initialize Firecrawl
firecrawl = Firecrawl(api_key=os.getenv("FIRECRAWL_API_KEY"))

def discover_api_urls():
    """Discover all Cascadeur API documentation URLs"""
    
    # Map the entire documentation site
    urls = firecrawl.map(
        url="https://cascadeur.com/python-api/",
        limit=1000,
        search="python api documentation",
        ignore_sitemap=False
    )
    
    # Filter for API documentation pages
    api_urls = []
    for url_info in urls:
        url = url_info.get('url', '')
        if '_generate/csc.' in url and url.endswith('.html'):
            api_urls.append(url_info)
    
    print(f"Found {len(api_urls)} API documentation pages")
    return api_urls
```

### Phase 2: Batch Scraping - Extract Content

Use **batch scraping** for efficient parallel processing:

```python
def batch_scrape_api_docs(urls, batch_size=50):
    """Scrape API documentation in batches"""
    
    results = []
    
    for i in range(0, len(urls), batch_size):
        batch_urls = [url_info['url'] for url_info in urls[i:i+batch_size]]
        
        print(f"Processing batch {i//batch_size + 1}: {len(batch_urls)} URLs")
        
        try:
            # Use async batch scraping for better performance
            job = firecrawl.batch_scrape(
                urls=batch_urls,
                formats=['markdown'],
                params={
                    'onlyMainContent': True,
                    'maxAge': 3600000,  # Use 1-hour cache for performance
                    'timeout': 30000
                }
            )
            
            # Process results
            for result in job.data:
                if result.get('success'):
                    results.append(result)
                else:
                    print(f"Failed to scrape: {result.get('url')}")
                    
        except Exception as e:
            print(f"Batch scraping error: {e}")
            # Fallback to individual scraping
            for url in batch_urls:
                try:
                    result = firecrawl.scrape(url, formats=['markdown'])
                    results.append(result)
                    time.sleep(1)  # Rate limiting
                except Exception as err:
                    print(f"Individual scraping error for {url}: {err}")
    
    return results
```

### Phase 3: Content Processing and Directory Structure

Create the directory structure matching the website organization:

```python
def process_and_save_docs(scraped_results, output_dir="cascadeur-docs/python"):
    """Process scraped content and save with proper directory structure"""
    
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    for result in scraped_results:
        url = result.get('sourceURL', '')
        content = result.get('markdown', '')
        
        if not url or not content:
            continue
            
        # Extract module and class from URL
        # e.g., csc.model.BehaviourViewer.html -> model/BehaviourViewer.md
        if '_generate/csc.' in url:
            parts = url.split('_generate/csc.')[1].replace('.html', '').split('.')
            
            if len(parts) >= 2:
                module = parts[0]  # e.g., "model"
                class_name = parts[1]  # e.g., "BehaviourViewer"
                
                # Create module directory
                module_dir = output_path / module
                module_dir.mkdir(exist_ok=True)
                
                # Clean and process content
                processed_content = clean_api_content(content, class_name, url)
                
                # Save as markdown file
                file_path = module_dir / f"{class_name}.md"
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(processed_content)
                
                print(f"Saved: {file_path}")

def clean_api_content(content, class_name, source_url):
    """Clean and format API documentation content"""
    
    # Add metadata header
    header = f"""---
title: {class_name}
source: {source_url}
module: csc.{class_name.split('.')[0] if '.' in class_name else 'unknown'}
---

"""
    
    # Clean up content
    cleaned_content = content
    
    # Remove navigation elements and add source reference
    cleaned_content = cleaned_content.replace(
        "Tutorials Video lessons Documentation Articles. Community. Forum Discord Youtube Twitter Facebook Vkontakte. Support. Report a bug Road map. Download. Cascadeur ...", 
        ""
    )
    
    # Add source attribution
    cleaned_content += f"\n\n---\n*Source: {source_url}*\n"
    
    return header + cleaned_content
```

### Phase 4: Advanced Features - LLM Extraction

For structured data extraction, use Firecrawl's LLM capabilities:

```python
def extract_structured_api_data(url):
    """Extract structured API information using LLM"""
    
    schema = {
        "type": "object",
        "properties": {
            "class_name": {"type": "string"},
            "description": {"type": "string"},
            "methods": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "description": {"type": "string"},
                        "parameters": {"type": "array"},
                        "return_type": {"type": "string"}
                    }
                }
            },
            "module": {"type": "string"}
        }
    }
    
    result = firecrawl.scrape(
        url,
        formats=[{
            "type": "json",
            "prompt": "Extract the class name, description, and all methods with their parameters and return types from this Python API documentation.",
            "schema": schema
        }],
        only_main_content=True
    )
    
    return result.get('json', {})
```

## Complete Scraping Script

Here's the complete script that implements all phases:

```python
#!/usr/bin/env python3
"""
Cascadeur Python API Documentation Scraper

This script scrapes the official Cascadeur Python API documentation
and saves it as structured markdown files.
"""

import os
import json
import time
from pathlib import Path
from firecrawl import Firecrawl
from urllib.parse import urlparse
import argparse

class CascadeurAPIDocsScraper:
    def __init__(self, api_key=None, output_dir="cascadeur-docs/python"):
        self.firecrawl = Firecrawl(api_key=api_key or os.getenv("FIRECRAWL_API_KEY"))
        self.output_dir = Path(output_dir)
        self.base_url = "https://cascadeur.com/python-api/"
        
    def discover_urls(self):
        """Phase 1: Discover all API documentation URLs"""
        print("🔍 Discovering API documentation URLs...")
        
        try:
            urls = self.firecrawl.map(
                url=self.base_url,
                limit=1000,
                search="csc",
                ignore_sitemap=False
            )
            
            # Filter for API pages
            api_urls = []
            for url_info in urls:
                url = url_info.get('url', '')
                if '_generate/csc.' in url and url.endswith('.html'):
                    api_urls.append(url_info)
            
            print(f"✅ Found {len(api_urls)} API documentation pages")
            return api_urls
            
        except Exception as e:
            print(f"❌ Discovery failed: {e}")
            return []
    
    def batch_scrape(self, urls, batch_size=25):
        """Phase 2: Batch scrape all documentation pages"""
        print(f"📥 Scraping {len(urls)} pages in batches of {batch_size}...")
        
        results = []
        
        for i in range(0, len(urls), batch_size):
            batch_urls = [url_info['url'] for url_info in urls[i:i+batch_size]]
            
            print(f"  Processing batch {i//batch_size + 1}/{(len(urls) + batch_size - 1)//batch_size}")
            
            try:
                # Batch scrape with optimized settings
                job = self.firecrawl.batch_scrape(
                    urls=batch_urls,
                    formats=['markdown'],
                    params={
                        'onlyMainContent': True,
                        'maxAge': 3600000,  # 1-hour cache
                        'timeout': 45000
                    }
                )
                
                # Collect successful results
                if hasattr(job, 'data') and job.data:
                    for result in job.data:
                        if result.get('success') and result.get('markdown'):
                            results.append(result)
                        else:
                            print(f"    ⚠️ Failed: {result.get('url', 'unknown')}")
                            
            except Exception as e:
                print(f"    ❌ Batch error: {e}")
                # Fallback to individual scraping
                for url in batch_urls:
                    try:
                        result = self.firecrawl.scrape(
                            url, 
                            formats=['markdown'],
                            only_main_content=True
                        )
                        if result.get('markdown'):
                            results.append(result)
                        time.sleep(0.5)  # Rate limiting
                    except Exception as err:
                        print(f"      ❌ Individual error for {url}: {err}")
                        
            # Progress indicator
            print(f"  ✅ Completed: {len(results)} successful scrapes")
        
        return results
    
    def process_and_save(self, results):
        """Phase 3: Process content and save with directory structure"""
        print(f"💾 Processing and saving {len(results)} documents...")
        
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        saved_count = 0
        module_stats = {}
        
        for result in results:
            url = result.get('sourceURL', '')
            content = result.get('markdown', '')
            
            if not url or not content:
                continue
                
            try:
                # Parse URL to get module and class
                if '_generate/csc.' in url:
                    parts = url.split('_generate/csc.')[1].replace('.html', '').split('.')
                    
                    if len(parts) >= 2:
                        module = parts[0]
                        class_name = parts[1]
                        
                        # Track module statistics
                        module_stats[module] = module_stats.get(module, 0) + 1
                        
                        # Create module directory
                        module_dir = self.output_dir / module
                        module_dir.mkdir(exist_ok=True)
                        
                        # Process content
                        processed_content = self._clean_content(content, class_name, url, module)
                        
                        # Save file
                        file_path = module_dir / f"{class_name}.md"
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(processed_content)
                        
                        saved_count += 1
                        
            except Exception as e:
                print(f"    ❌ Processing error for {url}: {e}")
        
        print(f"✅ Saved {saved_count} documents")
        print("📊 Module Statistics:")
        for module, count in sorted(module_stats.items()):
            print(f"  {module}: {count} classes")
        
        return saved_count
    
    def _clean_content(self, content, class_name, source_url, module):
        """Clean and format API documentation content"""
        
        # Metadata header
        header = f"""---
title: {class_name}
module: csc.{module}
source: {source_url}
---

"""
        
        # Clean up common navigation elements
        cleaned = content
        unwanted_patterns = [
            "Tutorials Video lessons Documentation Articles. Community. Forum Discord Youtube Twitter Facebook Vkontakte. Support. Report a bug Road map. Download. Cascadeur ...",
            "Social, Learn, Tutorials, Video lessons, Documentation, Articles, Community, Forum, Discord, Youtube, Twitter, Facebook, Vkontakte.",
        ]
        
        for pattern in unwanted_patterns:
            cleaned = cleaned.replace(pattern, "")
        
        # Add source attribution
        cleaned += f"\n\n---\n**Source**: [{source_url}]({source_url})\n"
        
        return header + cleaned
    
    def create_index(self):
        """Create an index file for the scraped documentation"""
        print("📋 Creating documentation index...")
        
        index_content = """# Cascadeur Python API Documentation

This documentation was scraped from the official Cascadeur Python API docs.

## Modules

"""
        
        # Scan output directory for modules
        if self.output_dir.exists():
            modules = []
            for module_dir in sorted(self.output_dir.iterdir()):
                if module_dir.is_dir():
                    files = list(module_dir.glob("*.md"))
                    modules.append((module_dir.name, len(files)))
                    
                    index_content += f"### {module_dir.name}\n\n"
                    for file_path in sorted(files):
                        class_name = file_path.stem
                        index_content += f"- [{class_name}]({module_dir.name}/{class_name}.md)\n"
                    index_content += "\n"
            
            # Save index
            index_path = self.output_dir / "README.md"
            with open(index_path, 'w', encoding='utf-8') as f:
                f.write(index_content)
            
            print(f"✅ Created index with {len(modules)} modules")
        
    def run(self, batch_size=25):
        """Execute the complete scraping workflow"""
        print("🚀 Starting Cascadeur API Documentation Scraper\n")
        
        # Phase 1: Discovery
        urls = self.discover_urls()
        if not urls:
            print("❌ No URLs discovered. Exiting.")
            return
        
        # Phase 2: Scraping
        results = self.batch_scrape(urls, batch_size)
        if not results:
            print("❌ No content scraped. Exiting.")
            return
            
        # Phase 3: Processing
        saved_count = self.process_and_save(results)
        
        # Phase 4: Index creation
        self.create_index()
        
        print(f"\n🎉 Scraping completed!")
        print(f"📁 Output directory: {self.output_dir.absolute()}")
        print(f"📄 Documents saved: {saved_count}")

def main():
    parser = argparse.ArgumentParser(description='Scrape Cascadeur Python API Documentation')
    parser.add_argument('--output-dir', '-o', default='cascadeur-docs/python',
                        help='Output directory for scraped docs')
    parser.add_argument('--batch-size', '-b', type=int, default=25,
                        help='Batch size for scraping')
    parser.add_argument('--api-key', '-k', help='Firecrawl API key (or use FIRECRAWL_API_KEY env var)')
    
    args = parser.parse_args()
    
    scraper = CascadeurAPIDocsScraper(
        api_key=args.api_key,
        output_dir=args.output_dir
    )
    
    scraper.run(batch_size=args.batch_size)

if __name__ == "__main__":
    main()
```

## Running the Scraper

### Basic Usage

```bash
# Make sure you have your API key
export FIRECRAWL_API_KEY="fc-YOUR-API-KEY"

# Run the scraper
python cascadeur-docs/scripts/scrape_api_docs.py

# Custom output directory
python cascadeur-docs/scripts/scrape_api_docs.py -o custom-docs/python

# Adjust batch size for rate limiting
python cascadeur-docs/scripts/scrape_api_docs.py -b 10
```

### Output Structure

The scraper will create:
```
cascadeur-docs/python/
├── README.md                 # Index of all modules
├── model/
│   ├── BehaviourViewer.md
│   ├── DataEditor.md
│   └── ...
├── layers/
│   ├── CyclesViewer.md
│   ├── Selector.md
│   └── ...
├── tools/
│   ├── RiggingModeTool.md
│   └── ...
└── [other modules]/
```

## Advanced Features

### Custom LLM Extraction

For more structured data extraction:

```python
def extract_api_summary():
    """Extract structured API summary using LLM"""
    
    result = firecrawl.scrape(
        "https://cascadeur.com/python-api/",
        formats=[{
            "type": "json",
            "prompt": "Extract a summary of all available Python API modules and their main purposes.",
            "schema": {
                "type": "object",
                "properties": {
                    "modules": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "name": {"type": "string"},
                                "purpose": {"type": "string"},
                                "key_classes": {"type": "array", "items": {"type": "string"}}
                            }
                        }
                    }
                }
            }
        }]
    )
    
    return result.get('json', {})
```

### Performance Optimization

- **Use caching**: Set `maxAge` parameter for frequently accessed pages
- **Batch processing**: Process multiple URLs simultaneously
- **Rate limiting**: Add delays between requests if needed
- **Error handling**: Implement robust retry mechanisms
- **Monitoring**: Track scraping progress and success rates

### Compliance and Best Practices

1. **Respect robots.txt**: Firecrawl automatically checks robots.txt
2. **Rate limiting**: Don't overwhelm the server
3. **Caching**: Use cached results to minimize requests
4. **Attribution**: Always include source links in scraped content
5. **Legal compliance**: Ensure scraping is allowed by terms of service

## Troubleshooting

### Common Issues

1. **Rate Limiting**:
   ```python
   # Reduce batch size and add delays
   time.sleep(1)  # Between requests
   ```

2. **Large Pages**:
   ```python
   # Use onlyMainContent to reduce content size
   firecrawl.scrape(url, only_main_content=True)
   ```

3. **Authentication Errors**:
   ```bash
   # Verify API key
   echo $FIRECRAWL_API_KEY
   ```

4. **Network Timeouts**:
   ```python
   # Increase timeout values
   timeout=60000  # 60 seconds
   ```

## Next Steps

After scraping the documentation:

1. **Validate Content**: Check that all important classes are captured
2. **Create Search Index**: Build a searchable index of the documentation
3. **Generate Summaries**: Use LLM to create module summaries
4. **Cross-Reference**: Link related classes and methods
5. **Update Regularly**: Set up periodic scraping for updates

## Source Links

- **Firecrawl Documentation**: [docs.firecrawl.dev](https://docs.firecrawl.dev)
- **Firecrawl Python SDK**: [GitHub](https://github.com/mendableai/firecrawl)
- **Cascadeur Python API**: [cascadeur.com/python-api](https://cascadeur.com/python-api/)