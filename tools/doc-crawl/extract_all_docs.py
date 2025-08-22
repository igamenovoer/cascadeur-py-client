#!/usr/bin/env python
"""
Extract all Cascadeur API documentation to clean Markdown files.
Processes all 214 HTML files and creates organized markdown documentation.
"""

import json
import re
import subprocess
from pathlib import Path
from typing import Dict, List, Optional
from bs4 import BeautifulSoup, NavigableString, Tag
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed

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

class BulkDocExtractor:
    def __init__(self):
        # Create output directories
        OUTPUT_DIR.mkdir(exist_ok=True)
        TEMP_DIR.mkdir(exist_ok=True, parents=True)
        
        # Statistics
        self.success_count = 0
        self.failed_files = []
    
    def extract_main_content(self, html_path: Path) -> Optional[str]:
        """Extract main documentation content using markitdown."""
        try:
            # First clean the HTML with BeautifulSoup
            with open(html_path, 'r', encoding='utf-8') as f:
                html_content = f.read()
            
            soup = BeautifulSoup(html_content, 'lxml')
            
            # Remove all navigation and unnecessary elements
            for elem in soup.find_all(['nav', 'script', 'style', 'header', 'footer']):
                elem.decompose()
            
            # Remove sidebar and navigation elements
            for elem in soup.find_all(class_=['sidebar', 'navigation', 'breadcrumb', 'toc']):
                elem.decompose()
            
            # Find main content
            main_content = soup.find('div', {'role': 'main'})
            if not main_content:
                main_content = soup.find('section', class_='document')
            if not main_content:
                main_content = soup.find('div', class_='body')
            
            if main_content:
                # Save cleaned HTML
                temp_file = TEMP_DIR / f"{html_path.stem}_clean.html"
                with open(temp_file, 'w', encoding='utf-8') as f:
                    # Create a minimal HTML document
                    clean_html = f"""
                    <!DOCTYPE html>
                    <html>
                    <head><meta charset="utf-8"></head>
                    <body>
                    {str(main_content)}
                    </body>
                    </html>
                    """
                    f.write(clean_html)
                
                # Use markitdown to convert
                result = subprocess.run(
                    ['markitdown', str(temp_file)],
                    capture_output=True,
                    text=True,
                    encoding='utf-8',
                    errors='ignore'
                )
                
                if result.returncode == 0:
                    markdown = self.clean_markdown(result.stdout)
                    
                    # Delete temp file
                    temp_file.unlink(missing_ok=True)
                    
                    return markdown
                else:
                    logger.error(f"markitdown failed for {html_path.name}: {result.stderr}")
            
        except Exception as e:
            logger.error(f"Error extracting {html_path.name}: {e}")
        
        return None
    
    def clean_markdown(self, markdown: str) -> str:
        """Clean and format the markdown output."""
        lines = []
        in_main_content = False
        
        for line in markdown.split('\n'):
            # Skip until we find main content
            if not in_main_content:
                # Look for start of actual API documentation
                if re.match(r'^#+ (csc|class |def |CSC)', line, re.IGNORECASE):
                    in_main_content = True
                elif 'body' in line.lower() and not lines:
                    continue
                elif not line.strip():
                    continue
                else:
                    continue
            
            # Clean the line
            line = line.rstrip()
            
            # Remove body tags
            if line == 'body' or line == '/body':
                continue
            
            # Remove permalink symbols
            line = re.sub(r'[ÂÃ]¶', '', line)
            
            # Fix code formatting
            line = re.sub(r'(\w+)\(self[^)]*\)→(\w+)', r'`\1(self) -> \2`', line)
            line = re.sub(r'(\w+)\(self[^)]*\)→None', r'`\1(self) -> None`', line)
            
            # Add spacing around headers
            if re.match(r'^#+\s', line):
                if lines and lines[-1]:
                    lines.append('')
                lines.append(line)
                lines.append('')
            else:
                lines.append(line)
        
        # Join and clean up
        markdown = '\n'.join(lines)
        
        # Fix method/attribute lists
        markdown = re.sub(r'(Methods|Attributes|Properties)(.*?)(?=\n\n|\Z)', 
                         lambda m: f"\n**{m.group(1)}:**\n" + self.format_member_list(m.group(2)), 
                         markdown, flags=re.DOTALL)
        
        # Clean up excessive newlines
        markdown = re.sub(r'\n{3,}', '\n\n', markdown)
        
        # Ensure proper spacing around code blocks
        markdown = re.sub(r'```\n', '```\n', markdown)
        markdown = re.sub(r'\n```', '\n\n```', markdown)
        
        return markdown.strip()
    
    def format_member_list(self, text: str) -> str:
        """Format method/attribute lists."""
        # Split by common delimiters
        items = re.split(r'(?=[A-Z_][a-z_]*(?:\(|=))', text)
        formatted = []
        
        for item in items:
            item = item.strip()
            if not item:
                continue
            
            # Format as list item
            if '(' in item or '=' in item:
                formatted.append(f"- `{item}`")
            elif item and not item.startswith('-'):
                formatted.append(f"- {item}")
        
        return '\n'.join(formatted) if formatted else text
    
    def process_file(self, page_info: Dict) -> tuple:
        """Process a single file and return result."""
        url = page_info['url']
        html_file = INPUT_DIR / "html" / page_info['filename']
        
        # Generate output filename
        url_path = url.replace('https://cascadeur.com/python-api/', '')
        url_path = url_path.replace('_generate/', '')
        url_path = url_path.replace('.html', '')
        url_path = url_path.replace('/', '_')
        
        markdown_file = OUTPUT_DIR / f"{url_path}.md"
        
        # Extract content
        markdown = self.extract_main_content(html_file)
        
        if markdown:
            # Add metadata header
            header = f"""---
source_url: {url}
html_file: {page_info['filename']}
module: {url_path}
---

"""
            markdown = header + markdown
            
            # Save file
            with open(markdown_file, 'w', encoding='utf-8', errors='ignore') as f:
                f.write(markdown)
            
            return (url_path, True, str(markdown_file))
        else:
            return (url_path, False, None)
    
    def process_all(self):
        """Process all HTML files in parallel."""
        # Load pages index
        index_file = INPUT_DIR / "pages_index.json"
        with open(index_file, 'r') as f:
            pages_index = json.load(f)
        
        total = len(pages_index)
        logger.info(f"Processing {total} HTML files...")
        
        # Process files in parallel
        results = []
        with ThreadPoolExecutor(max_workers=4) as executor:
            # Submit all tasks
            futures = {
                executor.submit(self.process_file, page_info): page_info
                for page_info in pages_index
            }
            
            # Process results as they complete
            for i, future in enumerate(as_completed(futures), 1):
                try:
                    url_path, success, output_file = future.result()
                    results.append({
                        'module': url_path,
                        'success': success,
                        'markdown_file': output_file
                    })
                    
                    if success:
                        self.success_count += 1
                        logger.info(f"[{i}/{total}] ✓ {url_path}")
                    else:
                        self.failed_files.append(url_path)
                        logger.warning(f"[{i}/{total}] ✗ {url_path}")
                    
                    # Progress update
                    if i % 20 == 0:
                        logger.info(f"Progress: {i}/{total} ({i*100//total}%)")
                        
                except Exception as e:
                    page_info = futures[future]
                    logger.error(f"Error processing {page_info['url']}: {e}")
                    self.failed_files.append(page_info['url'])
        
        # Save results index
        index_file = OUTPUT_DIR / "extraction_results.json"
        with open(index_file, 'w', encoding='utf-8') as f:
            json.dump({
                'total_files': total,
                'success_count': self.success_count,
                'failed_count': len(self.failed_files),
                'results': results
            }, f, indent=2)
        
        # Print summary
        logger.info("\n" + "="*50)
        logger.info("EXTRACTION COMPLETE")
        logger.info("="*50)
        logger.info(f"Total files: {total}")
        logger.info(f"Success: {self.success_count}")
        logger.info(f"Failed: {len(self.failed_files)}")
        logger.info(f"Output directory: {OUTPUT_DIR}")
        logger.info(f"Results saved to: {index_file}")
        
        if self.failed_files:
            logger.warning(f"\nFailed files ({len(self.failed_files)}):")
            for f in self.failed_files[:10]:
                logger.warning(f"  - {f}")
            if len(self.failed_files) > 10:
                logger.warning(f"  ... and {len(self.failed_files) - 10} more")
    
    def create_index_file(self):
        """Create a main index file for all documentation."""
        index_content = """# Cascadeur Python API Documentation

This directory contains the extracted Python API documentation for Cascadeur animation software.

## Directory Structure

The documentation is organized by module:

- `csc.md` - Main CSC module documentation
- `csc.*.md` - Individual class and function documentation

## Quick Links

### Core Modules
- [CSC Main Module](csc.md)
- [Domain Module](csc.domain.*.md)
- [Math Module](csc.math.*.md)
- [Tools Module](csc.tools.*.md)
- [View Module](csc.view.*.md)
- [Update Module](csc.update.*.md)

## Usage

Each markdown file contains:
- Complete API documentation for the module/class
- Method signatures
- Property descriptions
- Usage examples (where available)

## Source

Documentation extracted from: https://cascadeur.com/python-api/
"""
        
        index_file = OUTPUT_DIR / "README.md"
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(index_content)
        
        logger.info(f"Created index file: {index_file}")

def main():
    extractor = BulkDocExtractor()
    extractor.process_all()
    extractor.create_index_file()

if __name__ == "__main__":
    main()