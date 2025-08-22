#!/usr/bin/env python
"""
Extract and convert Cascadeur API documentation from HTML to clean Markdown.
Uses BeautifulSoup to parse HTML and extract only the essential API documentation.
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Optional
from bs4 import BeautifulSoup, NavigableString, Tag
import html2text
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Paths
PROJECT_ROOT = Path(__file__).parent.parent.parent
INPUT_DIR = PROJECT_ROOT / "casey-docs"
OUTPUT_DIR = PROJECT_ROOT / "casey-docs" / "markdown"

class APIDocExtractor:
    def __init__(self):
        self.h2t = html2text.HTML2Text()
        self.h2t.ignore_links = False
        self.h2t.ignore_images = True
        self.h2t.ignore_emphasis = False
        self.h2t.body_width = 0  # No line wrapping
        self.h2t.unicode_snob = True
        self.h2t.skip_internal_links = False
        
        # Create output directory
        OUTPUT_DIR.mkdir(exist_ok=True)
    
    def extract_main_content(self, html_path: Path) -> Optional[str]:
        """Extract main documentation content from HTML file."""
        try:
            with open(html_path, 'r', encoding='utf-8') as f:
                html_content = f.read()
            
            soup = BeautifulSoup(html_content, 'lxml')
            
            # Find the main content area - typically in <section> or <div role="main">
            main_content = None
            
            # Try different selectors for main content
            selectors = [
                'div[role="main"]',
                'main',
                'section.document',
                'div.document',
                'div.body',
                'article'
            ]
            
            for selector in selectors:
                main_content = soup.select_one(selector)
                if main_content:
                    break
            
            if not main_content:
                # Fallback: look for the content after the navigation
                # Find all dl tags with class="sig sig-object py"
                api_elements = soup.find_all('dl', class_='sig sig-object py')
                if api_elements:
                    # Create a new div to hold the API content
                    main_content = soup.new_tag('div')
                    
                    # Add title if found
                    title = soup.find('h1')
                    if title:
                        main_content.append(title)
                    
                    # Add all API elements and their descriptions
                    for api_elem in api_elements:
                        main_content.append(api_elem)
                        
                        # Also get the description that follows (usually a dd tag)
                        next_elem = api_elem.find_next_sibling()
                        while next_elem and next_elem.name in ['dd', 'p', 'div', 'blockquote']:
                            main_content.append(next_elem)
                            next_elem = next_elem.find_next_sibling()
                            if next_elem and next_elem.name == 'dl':
                                break
            
            if not main_content:
                logger.warning(f"Could not find main content in {html_path}")
                return None
            
            # Remove navigation elements
            for nav in main_content.select('nav, .nav, .navigation, .sidebar, .toc, .breadcrumb'):
                nav.decompose()
            
            # Remove script and style tags
            for elem in main_content.select('script, style'):
                elem.decompose()
            
            # Clean up the HTML
            return self.clean_and_convert(main_content)
            
        except Exception as e:
            logger.error(f"Error extracting from {html_path}: {e}")
            return None
    
    def clean_and_convert(self, element) -> str:
        """Clean HTML element and convert to Markdown."""
        # Convert to string first
        html_str = str(element)
        
        # Use html2text for conversion
        markdown = self.h2t.handle(html_str)
        
        # Post-process the markdown
        markdown = self.post_process_markdown(markdown)
        
        return markdown
    
    def post_process_markdown(self, markdown: str) -> str:
        """Clean up and improve the generated markdown."""
        lines = markdown.split('\n')
        cleaned_lines = []
        
        for line in lines:
            # Remove excessive whitespace
            line = line.rstrip()
            
            # Skip empty header links
            if line == '##' or line == '###':
                continue
            
            # Clean up weird characters (Â¶ is often used for permalinks)
            line = re.sub(r'[ÂÃ]¶', '', line)
            
            # Fix code blocks
            line = re.sub(r'`{3,}', '```', line)
            
            # Clean up excessive backticks
            line = re.sub(r'``+', '`', line)
            
            cleaned_lines.append(line)
        
        # Join and remove multiple blank lines
        markdown = '\n'.join(cleaned_lines)
        markdown = re.sub(r'\n{3,}', '\n\n', markdown)
        
        return markdown.strip()
    
    def extract_api_info(self, html_path: Path) -> Dict:
        """Extract structured API information from HTML."""
        try:
            with open(html_path, 'r', encoding='utf-8') as f:
                html_content = f.read()
            
            soup = BeautifulSoup(html_content, 'lxml')
            
            # Extract title
            title = soup.find('title')
            title_text = title.get_text(strip=True) if title else ""
            
            # Extract all API signatures
            signatures = []
            for sig in soup.find_all('dt', class_='sig'):
                sig_text = sig.get_text(strip=True)
                # Get the ID for linking
                sig_id = sig.get('id', '')
                signatures.append({
                    'signature': sig_text,
                    'id': sig_id
                })
            
            # Extract module/class name
            module_name = ""
            h1 = soup.find('h1')
            if h1:
                module_name = h1.get_text(strip=True)
            
            return {
                'title': title_text,
                'module': module_name,
                'signatures': signatures,
                'filename': html_path.name
            }
            
        except Exception as e:
            logger.error(f"Error extracting API info from {html_path}: {e}")
            return {}
    
    def process_all_files(self):
        """Process all HTML files and convert to Markdown."""
        # Load the pages index
        index_file = INPUT_DIR / "pages_index.json"
        with open(index_file, 'r') as f:
            pages_index = json.load(f)
        
        logger.info(f"Processing {len(pages_index)} HTML files...")
        
        # Create a mapping of URLs to output files
        url_to_markdown = {}
        api_index = []
        
        for i, page_info in enumerate(pages_index, 1):
            url = page_info['url']
            html_file = INPUT_DIR / "html" / page_info['filename']
            
            # Generate output filename based on URL
            # Convert URL to a filename-friendly format
            url_path = url.replace('https://cascadeur.com/python-api/', '')
            url_path = url_path.replace('_generate/', '')
            url_path = url_path.replace('.html', '')
            url_path = url_path.replace('/', '_')
            
            markdown_file = OUTPUT_DIR / f"{url_path}.md"
            
            logger.info(f"[{i}/{len(pages_index)}] Processing {url_path}")
            
            # Extract and convert content
            markdown_content = self.extract_main_content(html_file)
            
            if markdown_content:
                # Add metadata header
                header = f"---\nsource: {url}\nfilename: {page_info['filename']}\n---\n\n"
                markdown_content = header + markdown_content
                
                # Save markdown file
                with open(markdown_file, 'w', encoding='utf-8') as f:
                    f.write(markdown_content)
                
                url_to_markdown[url] = str(markdown_file.relative_to(PROJECT_ROOT))
                
                # Extract API info for index
                api_info = self.extract_api_info(html_file)
                if api_info:
                    api_info['markdown_file'] = str(markdown_file.relative_to(PROJECT_ROOT))
                    api_info['url'] = url
                    api_index.append(api_info)
            
            # Process in batches to avoid memory issues
            if i % 50 == 0:
                logger.info(f"Processed {i} files...")
        
        # Save the mapping index
        mapping_file = OUTPUT_DIR / "url_to_markdown_mapping.json"
        with open(mapping_file, 'w', encoding='utf-8') as f:
            json.dump(url_to_markdown, f, indent=2)
        
        # Save API index
        api_index_file = OUTPUT_DIR / "api_index.json"
        with open(api_index_file, 'w', encoding='utf-8') as f:
            json.dump(api_index, f, indent=2)
        
        logger.info(f"Conversion complete! Markdown files saved to {OUTPUT_DIR}")
        logger.info(f"Mapping saved to {mapping_file}")
        logger.info(f"API index saved to {api_index_file}")

def main():
    extractor = APIDocExtractor()
    extractor.process_all_files()

if __name__ == "__main__":
    main()