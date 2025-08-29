#!/usr/bin/env python3
"""
Improved script to fix KaTeX parse errors in Cascadeur documentation files.
This version handles edge cases better and avoids double-escaping.
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


def fix_numpy_type_annotations_v2(content: str) -> Tuple[str, int]:
    """
    Fix numpy type annotations that cause KaTeX errors - improved version.
    
    Handles patterns like:
    - numpy.ndarray\\[numpy.float32\\[3, 1\\]\\]  (escaped)
    - numpy.ndarray[numpy.float32[3, 1]]         (unescaped)
    - ``numpy.ndarray[numpy.float32[3, 1\\]]``   (already partially fixed)
    
    Converts to:
    - `numpy.ndarray[numpy.float32[3, 1]]`
    
    Returns tuple of (fixed_content, number_of_fixes)
    """
    fixes_count = 0
    
    # Pattern 1: Clean up double backticks that may have been created
    pattern_double_backticks = r'``([^`]+)``'
    def replace_double_backticks(match):
        nonlocal fixes_count
        content_inside = match.group(1)
        if 'numpy' in content_inside:
            fixes_count += 1
            return f'`{content_inside}`'
        return match.group(0)
    
    content = re.sub(pattern_double_backticks, replace_double_backticks, content)
    
    # Pattern 2: Fix escaped numpy arrays with backslashes
    pattern_escaped = r'(?<!`)\bnumpy\.ndarray\\?\[numpy\.(\w+)\\?\[([^\]\\]+)(?:\\?\]){2}(?!`)'
    def replace_escaped(match):
        nonlocal fixes_count
        fixes_count += 1
        dtype = match.group(1)
        dimensions = match.group(2).replace('\\', '')  # Remove any escaping
        return f'`numpy.ndarray[numpy.{dtype}[{dimensions}]]`'
    
    content = re.sub(pattern_escaped, replace_escaped, content)
    
    # Pattern 3: Fix unescaped numpy arrays that aren't in code blocks
    pattern_unescaped = r'(?<!`)\bnumpy\.ndarray\[numpy\.(\w+)\[([^\]]+)\]\](?!`)'
    def replace_unescaped(match):
        nonlocal fixes_count
        fixes_count += 1
        dtype = match.group(1)
        dimensions = match.group(2)
        return f'`numpy.ndarray[numpy.{dtype}[{dimensions}]]`'
    
    content = re.sub(pattern_unescaped, replace_unescaped, content)
    
    # Pattern 4: Fix standalone numpy types
    pattern_standalone = r'(?<!`)\bnumpy\.(\w+)\\?\[([^\]\\]+)(?:\\?\])(?!`)'
    def replace_standalone(match):
        nonlocal fixes_count
        # Only fix if it's not part of an ndarray (already handled above)
        full_match = match.group(0)
        before_text = content[max(0, match.start()-15):match.start()]
        if 'ndarray[' not in before_text:
            fixes_count += 1
            dtype = match.group(1)
            dimensions = match.group(2).replace('\\', '')
            return f'`numpy.{dtype}[{dimensions}]`'
        return full_match
    
    content = re.sub(pattern_standalone, replace_standalone, content)
    
    # Pattern 5: Clean up any remaining escaped brackets in code blocks
    pattern_cleanup = r'`([^`]*numpy[^`]*?)\\(\[|\])([^`]*)`'
    def replace_cleanup(match):
        nonlocal fixes_count
        before = match.group(1)
        bracket = match.group(2)
        after = match.group(3)
        if '\\' in before or '\\' in after:
            fixes_count += 1
        return f'`{before}{bracket}{after}`'
    
    content = re.sub(pattern_cleanup, replace_cleanup, content)
    
    return content, fixes_count


def process_file_v2(file_path: Path, dry_run: bool = False) -> Tuple[bool, int]:
    """Process a single markdown file to fix KaTeX errors - improved version."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        fixed_content, fixes_count = fix_numpy_type_annotations_v2(original_content)
        
        if fixes_count > 0 and not dry_run:
            # Write fixed content (don't create backup if already exists)
            backup_path = file_path.with_suffix(file_path.suffix + '.bak')
            if not backup_path.exists():
                with open(backup_path, 'w', encoding='utf-8') as f:
                    f.write(original_content)
                backup_msg = f"   Backup saved as: {backup_path}"
            else:
                backup_msg = f"   (Backup already exists: {backup_path})"
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(fixed_content)
            
            print(f"✅ Fixed {fixes_count} issues in: {file_path}")
            print(backup_msg)
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
    parser = argparse.ArgumentParser(description='Fix KaTeX parse errors in markdown files (improved version)')
    parser.add_argument('directory', nargs='?', 
                       help='Directory to process (default: cascadeur-docs)')
    parser.add_argument('--dry-run', action='store_true',
                       help='Show what would be changed without making changes')
    
    args = parser.parse_args()
    
    # Set default directory
    if args.directory:
        target_dir = Path(args.directory)
    else:
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
        was_modified, fixes_count = process_file_v2(file_path, args.dry_run)
        if was_modified:
            total_files_modified += 1
        total_fixes += fixes_count
    
    print("\n" + "="*60)
    print("📊 SUMMARY:")
    print(f"   Files processed: {len(markdown_files)}")
    print(f"   Files modified: {total_files_modified}")
    print(f"   Total fixes applied: {total_fixes}")
    
    if total_fixes > 0 and not args.dry_run:
        print("\n💡 TIP: Backup files (.bak) were preserved for safety")
        print("   You can restore originals if needed")
    elif total_fixes > 0 and args.dry_run:
        print("\n▶️  Run without --dry-run to apply the fixes")
    
    return 0


if __name__ == '__main__':
    exit(main())
