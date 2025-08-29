#!/usr/bin/env python3
"""
Script to fix KaTeX parse errors in Cascadeur documentation files.

This script fixes issues where numpy type annotations with square brackets
cause KaTeX "Undefined control sequence" errors by converting them to
proper code formatting.

Usage:
    python fix_katex_errors.py [directory_path]

If no directory is provided, it will process the cascadeur-docs directory.
"""

import os
import re
import argparse
from pathlib import Path
from typing import List, Tuple


def find_markdown_files(directory: Path) -> List[Path]:
    """Find all markdown files in the given directory and subdirectories."""
    markdown_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                markdown_files.append(Path(root) / file)
    return markdown_files


def fix_numpy_type_annotations(content: str) -> Tuple[str, int]:
    """
    Fix numpy type annotations that cause KaTeX errors.
    
    Converts patterns like:
    - numpy.ndarray\\[numpy.float32\\[3, 1\\]\\]
    - numpy.ndarray[numpy.float32[3, 1]]
    
    To:
    - `numpy.ndarray[numpy.float32[3, 1]]`
    
    Returns tuple of (fixed_content, number_of_fixes)
    """
    fixes_count = 0
    
    # Pattern 1: Fix escaped square brackets in numpy type annotations
    # Matches: numpy.ndarray\[numpy.float32\[3, 1\]\]
    pattern1 = r'numpy\.ndarray\\?\[numpy\.float32\\?\[([^\]]+)\]\\?\]'
    def replace1(match):
        nonlocal fixes_count
        fixes_count += 1
        dimensions = match.group(1)
        return f'`numpy.ndarray[numpy.float32[{dimensions}]]`'
    
    content = re.sub(pattern1, replace1, content)
    
    # Pattern 2: Fix unescaped numpy type annotations that aren't already in code blocks
    # Matches: numpy.ndarray[numpy.float32[3, 1]] (not already in backticks)
    pattern2 = r'(?<!`)\bnumpy\.ndarray\[numpy\.float32\[([^\]]+)\]\](?!`)'
    def replace2(match):
        nonlocal fixes_count
        fixes_count += 1
        dimensions = match.group(1)
        return f'`numpy.ndarray[numpy.float32[{dimensions}]]`'
    
    content = re.sub(pattern2, replace2, content)
    
    # Pattern 3: Fix other numpy array type patterns
    # Matches: numpy.ndarray\[numpy.int32\[...\]\] etc.
    pattern3 = r'numpy\.ndarray\\?\[numpy\.(\w+)\\?\[([^\]]+)\]\\?\]'
    def replace3(match):
        nonlocal fixes_count
        # Only fix if not already in code formatting
        full_match = match.group(0)
        if '`' in full_match:
            return full_match
        fixes_count += 1
        dtype = match.group(1)
        dimensions = match.group(2)
        return f'`numpy.ndarray[numpy.{dtype}[{dimensions}]]`'
    
    content = re.sub(pattern3, replace3, content)
    
    # Pattern 4: Fix standalone numpy types
    # Matches: numpy.float32\[3, 1\]
    pattern4 = r'(?<!`)\bnumpy\.(\w+)\\?\[([^\]]+)\](?!`)'
    def replace4(match):
        nonlocal fixes_count
        # Check if this is part of a larger type annotation already handled
        dtype = match.group(1)
        dimensions = match.group(2)
        # Only fix if it's a standalone type, not part of ndarray
        full_text = f'numpy.{dtype}[{dimensions}]'
        if 'ndarray[' not in content[max(0, match.start()-20):match.start()]:
            fixes_count += 1
            return f'`{full_text}`'
        return match.group(0)
    
    content = re.sub(pattern4, replace4, content)
    
    return content, fixes_count


def process_file(file_path: Path, dry_run: bool = False) -> Tuple[bool, int]:
    """
    Process a single markdown file to fix KaTeX errors.
    
    Returns tuple of (was_modified, number_of_fixes)
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        fixed_content, fixes_count = fix_numpy_type_annotations(original_content)
        
        if fixes_count > 0 and not dry_run:
            # Create backup
            backup_path = file_path.with_suffix(file_path.suffix + '.bak')
            with open(backup_path, 'w', encoding='utf-8') as f:
                f.write(original_content)
            
            # Write fixed content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(fixed_content)
            
            print(f"✅ Fixed {fixes_count} issues in: {file_path}")
            print(f"   Backup saved as: {backup_path}")
            return True, fixes_count
        elif fixes_count > 0 and dry_run:
            print(f"🔍 Would fix {fixes_count} issues in: {file_path}")
            return False, fixes_count
        else:
            print(f"✨ No issues found in: {file_path}")
            return False, 0
            
    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")
        return False, 0


def main():
    parser = argparse.ArgumentParser(description='Fix KaTeX parse errors in markdown files')
    parser.add_argument('directory', nargs='?', 
                       help='Directory to process (default: cascadeur-docs)')
    parser.add_argument('--dry-run', action='store_true',
                       help='Show what would be changed without making changes')
    parser.add_argument('--pattern', default='*.md',
                       help='File pattern to match (default: *.md)')
    
    args = parser.parse_args()
    
    # Set default directory
    if args.directory:
        target_dir = Path(args.directory)
    else:
        # Default to cascadeur-docs directory
        script_dir = Path(__file__).parent
        target_dir = script_dir.parent / 'cascadeur-docs'
    
    if not target_dir.exists():
        print(f"❌ Directory not found: {target_dir}")
        return 1
    
    print(f"🔍 Searching for markdown files in: {target_dir}")
    markdown_files = find_markdown_files(target_dir)
    
    if not markdown_files:
        print(f"❌ No markdown files found in: {target_dir}")
        return 1
    
    print(f"📄 Found {len(markdown_files)} markdown files")
    
    if args.dry_run:
        print("🧪 DRY RUN MODE - No files will be modified")
    
    total_files_modified = 0
    total_fixes = 0
    
    for file_path in markdown_files:
        was_modified, fixes_count = process_file(file_path, args.dry_run)
        if was_modified:
            total_files_modified += 1
        total_fixes += fixes_count
    
    print("\n" + "="*60)
    print("📊 SUMMARY:")
    print(f"   Files processed: {len(markdown_files)}")
    print(f"   Files modified: {total_files_modified}")
    print(f"   Total fixes applied: {total_fixes}")
    
    if total_fixes > 0 and not args.dry_run:
        print("\n💡 TIP: Backup files (.bak) were created for all modified files")
        print("   You can restore originals if needed with:")
        print(f"   find {target_dir} -name '*.bak' -exec bash -c 'mv \"$1\" \"${{1%.bak}}\"' _ {{}} \\;")
    elif total_fixes > 0 and args.dry_run:
        print("\n▶️  Run without --dry-run to apply the fixes")
    
    return 0


if __name__ == '__main__':
    exit(main())
