#!/usr/bin/env python
"""
Simple extraction of Cascadeur API documentation from HTML to Markdown.
Uses BeautifulSoup to extract main content and convert to markdown format.
"""

import json
import re
import subprocess
from pathlib import Path
from typing import Dict, List, Optional
from bs4 import BeautifulSoup, NavigableString, Tag
import logging
import os

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
TEMP_DIR = PROJECT_ROOT / "tmp" / "doc_extraction"

class SimpleDocExtractor:
    def __init__(self):
        # Create output directories
        OUTPUT_DIR.mkdir(exist_ok=True)
        TEMP_DIR.mkdir(exist_ok=True, parents=True)
    
    def extract_with_beautifulsoup(self, html_path: Path) -> Optional[str]:
        """Extract main content using BeautifulSoup and convert to markdown-like format."""
        try:
            with open(html_path, 'r', encoding='utf-8') as f:
                html_content = f.read()
            
            soup = BeautifulSoup(html_content, 'lxml')
            
            # Find the main content
            main_content = None
            
            # Try to find the main documentation content
            # First try role="main"
            main_content = soup.find('div', {'role': 'main'})
            
            if not main_content:
                # Try finding section with document class
                main_content = soup.find('section', class_='document')
            
            if not main_content:
                # Look for the body content
                main_content = soup.find('div', class_='body')
            
            if not main_content:
                # Fallback: extract API documentation elements
                main_content = self.extract_api_elements(soup)
            
            if not main_content:
                logger.warning(f"Could not find main content in {html_path.name}")
                return None
            
            # Clean the content
            self.clean_html(main_content)
            
            # Convert to markdown-like format
            markdown = self.html_to_markdown(main_content)
            
            return markdown
            
        except Exception as e:
            logger.error(f"Error processing {html_path}: {e}")
            return None
    
    def extract_api_elements(self, soup):
        """Extract API documentation elements."""
        # Create a container for API elements
        container = soup.new_tag('div')
        
        # Get the main title
        h1 = soup.find('h1')
        if h1:
            container.append(h1.extract())
        
        # Find all API signature blocks
        api_blocks = soup.find_all('dl', class_='sig sig-object')
        
        for block in api_blocks:
            # Add the signature block
            container.append(block.extract())
            
            # Look for the description that follows
            current = block.find_next_sibling()
            while current and current.name in ['dd', 'p', 'blockquote', 'div']:
                if 'class' in current.attrs:
                    classes = current.get('class', [])
                    if any('sig' in c for c in classes):
                        break
                container.append(current.extract())
                current = current.find_next_sibling() if current else None
        
        return container if container.contents else None
    
    def clean_html(self, element):
        """Remove unwanted elements from HTML."""
        # Remove navigation, scripts, styles
        for tag in element.find_all(['nav', 'script', 'style', 'aside']):
            tag.decompose()
        
        # Remove elements with specific classes
        unwanted_classes = ['navigation', 'sidebar', 'toc', 'breadcrumb', 'header', 'footer']
        for cls in unwanted_classes:
            for elem in element.find_all(class_=cls):
                elem.decompose()
        
        # Remove permalink symbols
        for link in element.find_all('a', class_='headerlink'):
            link.decompose()
    
    def html_to_markdown(self, element):
        """Convert HTML element to markdown format."""
        output = []
        
        def process_element(elem, level=0):
            if isinstance(elem, NavigableString):
                text = str(elem).strip()
                if text:
                    output.append(text)
            elif isinstance(elem, Tag):
                # Handle different HTML tags
                if elem.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                    level_num = int(elem.name[1])
                    prefix = '#' * level_num
                    text = elem.get_text(strip=True)
                    if text:
                        output.append(f"\n{prefix} {text}\n")
                
                elif elem.name == 'p':
                    text = elem.get_text(strip=True)
                    if text:
                        output.append(f"\n{text}\n")
                
                elif elem.name == 'code':
                    text = elem.get_text(strip=True)
                    if text:
                        # Check if it's inline or block code
                        parent = elem.parent
                        if parent and parent.name == 'pre':
                            output.append(f"\n```python\n{text}\n```\n")
                        else:
                            output.append(f"`{text}`")
                
                elif elem.name == 'pre':
                    # Check if we already handled this via code tag
                    code = elem.find('code')
                    if not code:
                        text = elem.get_text(strip=True)
                        if text:
                            output.append(f"\n```\n{text}\n```\n")
                    else:
                        # Process the code element
                        process_element(code, level)
                        return
                
                elif elem.name == 'dt':
                    # Definition term (often used for API signatures)
                    text = elem.get_text(strip=True)
                    if text:
                        # Clean up the text
                        text = re.sub(r'[ÂÃ]¶', '', text)  # Remove permalink symbols
                        output.append(f"\n### `{text}`\n")
                
                elif elem.name == 'dd':
                    # Definition description
                    text = elem.get_text(strip=True)
                    if text:
                        output.append(f"\n{text}\n")
                
                elif elem.name == 'ul':
                    output.append("\n")
                    for li in elem.find_all('li', recursive=False):
                        text = li.get_text(strip=True)
                        if text:
                            output.append(f"- {text}\n")
                    output.append("\n")
                
                elif elem.name == 'ol':
                    output.append("\n")
                    for i, li in enumerate(elem.find_all('li', recursive=False), 1):
                        text = li.get_text(strip=True)
                        if text:
                            output.append(f"{i}. {text}\n")
                    output.append("\n")
                
                elif elem.name == 'blockquote':
                    text = elem.get_text(strip=True)
                    if text:
                        lines = text.split('\n')
                        quoted = '\n'.join(f"> {line}" for line in lines if line)
                        output.append(f"\n{quoted}\n")
                
                elif elem.name == 'a':
                    text = elem.get_text(strip=True)
                    href = elem.get('href', '')
                    if text and href and not href.startswith('#'):
                        output.append(f"[{text}]({href})")
                    elif text:
                        output.append(text)
                
                elif elem.name == 'strong' or elem.name == 'b':
                    text = elem.get_text(strip=True)
                    if text:
                        output.append(f"**{text}**")
                
                elif elem.name == 'em' or elem.name == 'i':
                    text = elem.get_text(strip=True)
                    if text:
                        output.append(f"*{text}*")
                
                elif elem.name == 'dl':
                    # Process children
                    for child in elem.children:
                        process_element(child, level)
                
                elif elem.name in ['div', 'section', 'article']:
                    # Container elements - process children
                    for child in elem.children:
                        process_element(child, level)
                
                else:
                    # For other elements, just get the text
                    text = elem.get_text(strip=True)
                    if text:
                        output.append(text)
        
        # Process the main element
        process_element(element)
        
        # Join and clean up
        markdown = ''.join(output)
        
        # Clean up excessive newlines
        markdown = re.sub(r'\n{3,}', '\n\n', markdown)
        
        # Clean up spaces
        markdown = re.sub(r' +', ' ', markdown)
        
        return markdown.strip()
    
    def extract_with_markitdown(self, html_path: Path) -> Optional[str]:
        """Use markitdown tool as fallback."""
        try:
            # First extract main content with BeautifulSoup
            with open(html_path, 'r', encoding='utf-8') as f:
                html_content = f.read()
            
            soup = BeautifulSoup(html_content, 'lxml')
            
            # Find and extract main content
            main_content = soup.find('div', {'role': 'main'})
            if not main_content:
                main_content = soup.find('section', class_='document')
            
            if main_content:
                # Save cleaned HTML to temp file
                temp_file = TEMP_DIR / f"{html_path.stem}_clean.html"
                
                # Clean the content
                self.clean_html(main_content)
                
                with open(temp_file, 'w', encoding='utf-8') as f:
                    f.write(str(main_content))
                
                # Use markitdown on the cleaned HTML
                result = subprocess.run(
                    ['markitdown', str(temp_file)],
                    capture_output=True,
                    text=True,
                    encoding='utf-8'
                )
                
                if result.returncode == 0:
                    return self.post_process_markdown(result.stdout)
            
            # Fallback to using markitdown on full file
            result = subprocess.run(
                ['markitdown', str(html_path)],
                capture_output=True,
                text=True,
                encoding='utf-8'
            )
            
            if result.returncode == 0:
                return self.post_process_markdown(result.stdout)
            
        except Exception as e:
            logger.error(f"Error with markitdown on {html_path}: {e}")
        
        return None
    
    def post_process_markdown(self, markdown: str) -> str:
        """Clean up markdown output."""
        lines = []
        skip_until_main = True
        
        for line in markdown.split('\n'):
            # Skip navigation and header content
            if skip_until_main:
                # Look for the start of main content
                if any(marker in line.lower() for marker in ['# csc', 'class csc', '## csc']):
                    skip_until_main = False
                elif 'role="main"' in line or 'document' in line:
                    skip_until_main = False
                    continue
                else:
                    continue
            
            # Clean up the line
            line = line.rstrip()
            
            # Remove permalink symbols
            line = re.sub(r'[ÂÃ]¶', '', line)
            
            # Skip empty headers
            if line in ['##', '###', '####']:
                continue
            
            lines.append(line)
        
        markdown = '\n'.join(lines)
        
        # Clean up excessive newlines
        markdown = re.sub(r'\n{3,}', '\n\n', markdown)
        
        return markdown.strip()
    
    def process_file(self, html_path: Path, url: str) -> Optional[str]:
        """Process a single HTML file."""
        # Try BeautifulSoup extraction first
        markdown = self.extract_with_beautifulsoup(html_path)
        
        # If that fails, try markitdown
        if not markdown or len(markdown) < 100:
            logger.info(f"Trying markitdown for {html_path.name}")
            markdown = self.extract_with_markitdown(html_path)
        
        if markdown:
            # Add metadata header
            header = f"---\nsource_url: {url}\nhtml_file: {html_path.name}\n---\n\n"
            markdown = header + markdown
        
        return markdown
    
    def process_all(self):
        """Process all HTML files."""
        # Load pages index
        index_file = INPUT_DIR / "pages_index.json"
        with open(index_file, 'r') as f:
            pages_index = json.load(f)
        
        logger.info(f"Processing {len(pages_index)} files...")
        
        success_count = 0
        failed_files = []
        
        for i, page_info in enumerate(pages_index[:10], 1):  # Process first 10 for testing
            url = page_info['url']
            html_file = INPUT_DIR / "html" / page_info['filename']
            
            # Generate output filename
            url_path = url.replace('https://cascadeur.com/python-api/', '')
            url_path = url_path.replace('_generate/', '')
            url_path = url_path.replace('.html', '')
            url_path = url_path.replace('/', '_')
            
            markdown_file = OUTPUT_DIR / f"{url_path}.md"
            
            logger.info(f"[{i}/10] Processing {url_path}")
            
            # Process the file
            markdown = self.process_file(html_file, url)
            
            if markdown:
                with open(markdown_file, 'w', encoding='utf-8') as f:
                    f.write(markdown)
                success_count += 1
                logger.info(f"  Saved {markdown_file.name}")
            else:
                failed_files.append(url_path)
                logger.warning(f"  Failed to extract content")
        
        logger.info(f"\nProcessing complete!")
        logger.info(f"Success: {success_count}/10")
        if failed_files:
            logger.warning(f"Failed files: {failed_files}")

def main():
    extractor = SimpleDocExtractor()
    extractor.process_all()

if __name__ == "__main__":
    main()