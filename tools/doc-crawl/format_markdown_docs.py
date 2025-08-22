#!/usr/bin/env python
"""
Format Cascadeur Python API markdown documentation for better readability.
Takes the extracted markdown files and reformats them into clean Python library documentation.
"""

import re
import json
from pathlib import Path
from typing import Dict, List, Optional, Tuple
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
INPUT_DIR = PROJECT_ROOT / "casey-docs" / "markdown"
OUTPUT_DIR = PROJECT_ROOT / "casey-docs" / "markdown-revised"

class DocFormatter:
    def __init__(self):
        OUTPUT_DIR.mkdir(exist_ok=True, parents=True)
        
        # Regex patterns for parsing
        self.class_pattern = r'(\w+) class\s*(.*?)(?=\s*Methods|\s*Attributes|\s*$)'
        self.methods_pattern = r'Methods\s+(.*?)(?=\s*Attributes|\s*$)'
        self.attributes_pattern = r'Attributes\s+(.*?)(?=\s*$)'
        self.function_pattern = r'(\w+)\s*\([^)]*\)\s*(?:->?\s*([^$\n]+))?'
        self.enum_pattern = r'(\w+)\s+enumeration\s*(.*?)(?=Members|$)'
        
    def parse_metadata(self, content: str) -> Dict:
        """Extract YAML frontmatter metadata."""
        metadata = {}
        if content.startswith('---'):
            end_idx = content.find('---', 3)
            if end_idx != -1:
                frontmatter = content[3:end_idx].strip()
                for line in frontmatter.split('\n'):
                    if ':' in line:
                        key, value = line.split(':', 1)
                        metadata[key.strip()] = value.strip()
        return metadata
    
    def clean_text(self, text: str) -> str:
        """Clean up text by removing extra whitespace and formatting artifacts."""
        if not text:
            return ""
        
        # First, handle encoding issues by removing problematic characters
        text = text.encode('ascii', errors='ignore').decode('ascii')
        
        # Remove navigation and HTML artifacts
        try:
            text = re.sub(r'No newline at end of file.*?(?=\n|$)', '', text, flags=re.DOTALL)
            text = re.sub(r'\* \[.*?\]\(.*?\)', '', text)  # Remove navigation links
            text = re.sub(r'Language\s+English\s+Russian', '', text)
            text = re.sub(r'\[.*?\]\(.*?\)', '', text)  # Remove other links
            text = re.sub(r'PAGE CONTENTS.*?(?=\n#|\n\*|$)', '', text, flags=re.DOTALL)
            text = re.sub(r'Menu\s+.*?(?=\n#|\n\*|$)', '', text, flags=re.DOTALL)
            
            # Clean up spacing and formatting
            text = re.sub(r'\s+', ' ', text)
            text = re.sub(r'([.!?])\s+([A-Z])', r'\1\n\n\2', text)
        except Exception as e:
            # If regex fails, do basic cleanup
            text = ' '.join(text.split())
        
        text = text.strip()
        return text
    
    def extract_class_info(self, content: str) -> Dict:
        """Extract class information from content."""
        info = {
            'name': '',
            'description': '',
            'methods': [],
            'attributes': [],
            'is_enum': False,
            'enum_values': []
        }
        
        # Clean content first
        content = self.clean_text(content)
        
        # Extract class name from header
        header_match = re.search(r'# ([\w.]+)', content)
        if header_match:
            info['name'] = header_match.group(1)
        
        # Check if it's an enumeration
        if 'enumeration' in content.lower():
            info['is_enum'] = True
            # Extract enum values
            enum_values = re.findall(r'\b([A-Z][a-zA-Z_]*)\b', content)
            # Filter out common words that aren't enum values
            common_words = {'Methods', 'Attributes', 'Members', 'Get', 'Set', 'None', 'Bool'}
            info['enum_values'] = [v for v in set(enum_values) if v not in common_words][:10]
        
        # Extract class description
        desc_match = re.search(r'class\s+(.*?)(?=Methods|Attributes|$)', content, re.DOTALL | re.IGNORECASE)
        if desc_match:
            info['description'] = self.clean_text(desc_match.group(1))
        
        # Extract methods
        methods_match = re.search(r'Methods\s+(.*?)(?=Attributes|$)', content, re.DOTALL | re.IGNORECASE)
        if methods_match:
            methods_text = methods_match.group(1)
            info['methods'] = self.parse_methods(methods_text)
        
        # Extract attributes
        attr_match = re.search(r'Attributes\s+(.*?)$', content, re.DOTALL | re.IGNORECASE)
        if attr_match:
            attr_text = attr_match.group(1)
            info['attributes'] = self.parse_attributes(attr_text)
            
        return info
    
    def parse_methods(self, methods_text: str) -> List[Dict]:
        """Parse methods from text."""
        methods = []
        
        # Split by method patterns and clean
        method_parts = re.split(r'(?=\w+\s*\()', methods_text)
        
        for part in method_parts:
            if not part.strip():
                continue
                
            # Extract method signature
            sig_match = re.match(r'(\w+)\s*\([^)]*\)\s*(?:->?\s*([^$\n\s]+))?', part)
            if sig_match:
                method = {
                    'name': sig_match.group(1),
                    'signature': part.split('(')[0] + '(...)',
                    'return_type': sig_match.group(2) if sig_match.group(2) else None,
                    'description': ''
                }
                
                # Extract description (text after the signature)
                desc = re.sub(r'^\w+\s*\([^)]*\)\s*(?:->?\s*[^$\n\s]+)?', '', part).strip()
                method['description'] = self.clean_text(desc) if desc else ''
                
                methods.append(method)
        
        return methods[:20]  # Limit to prevent overwhelming output
    
    def parse_attributes(self, attr_text: str) -> List[Dict]:
        """Parse attributes from text."""
        attributes = []
        
        # Simple attribute extraction
        attr_parts = re.findall(r'(\w+)\s*[–-]\s*([^–-\n]+)', attr_text)
        
        for name, desc in attr_parts[:10]:  # Limit attributes
            attributes.append({
                'name': name.strip(),
                'description': self.clean_text(desc)
            })
            
        return attributes
    
    def format_class_doc(self, info: Dict) -> str:
        """Format class information into readable documentation."""
        lines = []
        
        # Header with class name
        class_name = info['name'].split('.')[-1] if '.' in info['name'] else info['name']
        lines.append(f"# {info['name']}")
        lines.append("")
        
        if info['is_enum']:
            lines.append(f"**Enumeration**")
            lines.append("")
            
            if info['description']:
                lines.append(info['description'])
                lines.append("")
            
            if info['enum_values']:
                lines.append("## Values")
                lines.append("")
                for value in sorted(info['enum_values']):
                    lines.append(f"- `{value}`")
                lines.append("")
        else:
            lines.append(f"**Class**: `{class_name}`")
            lines.append("")
            
            if info['description']:
                lines.append("## Description")
                lines.append("")
                lines.append(info['description'])
                lines.append("")
        
        # Methods section
        if info['methods']:
            lines.append("## Methods")
            lines.append("")
            
            for method in info['methods']:
                if method['name'] in ['__init__', '__module__', '__annotations__']:
                    continue
                    
                lines.append(f"### `{method['name']}()`")
                lines.append("")
                
                if method['return_type']:
                    lines.append(f"**Returns**: `{method['return_type']}`")
                    lines.append("")
                
                if method['description']:
                    lines.append(method['description'])
                    lines.append("")
        
        # Attributes section  
        if info['attributes']:
            lines.append("## Attributes")
            lines.append("")
            
            for attr in info['attributes']:
                lines.append(f"### `{attr['name']}`")
                lines.append("")
                if attr['description']:
                    lines.append(attr['description'])
                    lines.append("")
        
        return '\n'.join(lines)
    
    def process_file(self, file_path: Path) -> Tuple[str, bool]:
        """Process a single markdown file."""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Extract metadata
            metadata = self.parse_metadata(content)
            
            # Skip navigation files
            filename = file_path.stem.lower()
            if filename in ['index', 'search', 'genindex', 'py-modindex', 'readme']:
                return filename, False
            
            # Remove metadata from content for processing
            if content.startswith('---'):
                end_idx = content.find('---', 3)
                if end_idx != -1:
                    content = content[end_idx + 3:].strip()
            
            # Extract class information
            class_info = self.extract_class_info(content)
            
            # Format documentation
            formatted_doc = self.format_class_doc(class_info)
            
            # Add metadata header back
            final_content = "---\n"
            for key, value in metadata.items():
                final_content += f"{key}: {value}\n"
            final_content += "---\n\n"
            final_content += formatted_doc
            
            # Save formatted file
            output_path = OUTPUT_DIR / file_path.name
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(final_content)
            
            return file_path.stem, True
            
        except Exception as e:
            logger.error(f"Error processing {file_path}: {e}")
            return file_path.stem, False
    
    def process_all_files(self):
        """Process all markdown files in parallel."""
        markdown_files = list(INPUT_DIR.glob('*.md'))
        
        logger.info(f"Processing {len(markdown_files)} markdown files...")
        
        success_count = 0
        failed_files = []
        
        with ThreadPoolExecutor(max_workers=4) as executor:
            # Submit all tasks
            futures = {
                executor.submit(self.process_file, file_path): file_path
                for file_path in markdown_files
            }
            
            # Process results
            for i, future in enumerate(as_completed(futures), 1):
                try:
                    filename, success = future.result()
                    
                    if success:
                        success_count += 1
                        logger.info(f"[{i}/{len(markdown_files)}] ✓ {filename}")
                    else:
                        failed_files.append(filename)
                        logger.info(f"[{i}/{len(markdown_files)}] - {filename} (skipped)")
                        
                except Exception as e:
                    file_path = futures[future]
                    logger.error(f"Error processing {file_path}: {e}")
                    failed_files.append(file_path.stem)
        
        # Create summary
        self.create_summary_index()
        
        # Print results
        logger.info("\n" + "="*60)
        logger.info("FORMATTING COMPLETE")
        logger.info("="*60)
        logger.info(f"Total files: {len(markdown_files)}")
        logger.info(f"Successfully formatted: {success_count}")
        logger.info(f"Skipped: {len(failed_files)}")
        logger.info(f"Output directory: {OUTPUT_DIR}")
        
        if failed_files[:5]:  # Show first 5 failed files
            logger.info(f"Some skipped files: {', '.join(failed_files[:5])}")
    
    def create_summary_index(self):
        """Create a summary index of all formatted documentation."""
        index_content = """# Cascadeur Python API Documentation

This directory contains the formatted Python API documentation for Cascadeur animation software.

## Organization

The documentation is organized by module hierarchy:

### Core Modules
- **csc** - Main Cascadeur module
- **csc.app** - Application management
- **csc.domain** - Core domain objects
- **csc.layers** - Animation layers
- **csc.math** - Mathematical utilities
- **csc.model** - Data model objects
- **csc.tools** - Animation tools
- **csc.update** - Update system
- **csc.view** - Viewport and UI

### Key Classes

#### Scene Management
- `csc.domain.Scene` - Root scene object
- `csc.app.Application` - Main application interface
- `csc.app.SceneManager` - Scene management

#### Animation
- `csc.layers.Layer` - Animation layers
- `csc.layers.Editor` - Layer editing
- `csc.model.DataEditor` - Animation data editing

#### Mathematics
- `csc.math.Quaternion` - Quaternion operations
- `csc.math.Rotation` - Rotation utilities
- `csc.math.OrthogonalTransform` - Transformations

#### Tools
- `csc.tools.AutoPhysicTool` - Physics simulation
- `csc.tools.AttractorTool` - Attractor tools
- `csc.tools.MirrorTool` - Animation mirroring

## Usage

Each file contains:
- **Description** - Overview of the class or module
- **Methods** - Available methods with return types
- **Attributes** - Properties and attributes

## Source

Documentation extracted and formatted from: https://cascadeur.com/python-api/
"""
        
        with open(OUTPUT_DIR / "README.md", 'w', encoding='utf-8') as f:
            f.write(index_content)

def main():
    formatter = DocFormatter()
    formatter.process_all_files()

if __name__ == "__main__":
    main()