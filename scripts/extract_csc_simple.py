#!/usr/bin/env python3
"""
Simple CSC Module Documentation Extractor for Cascadeur

A lightweight script to quickly extract basic documentation from the csc module.
This script should be run INSIDE Cascadeur's Python console.

Usage in Cascadeur Python console:
exec(open(r'path\\to\\extract_csc_simple.py').read())
"""

import inspect
import json
from datetime import datetime


def extract_basic_info(obj, name="", max_depth=3, current_depth=0):
    """Extract basic information from any Python object."""
    if current_depth >= max_depth:
        return {"name": name, "type": type(obj).__name__, "truncated": True}
    
    info = {
        "name": name,
        "type": type(obj).__name__,
        "docstring": getattr(obj, '__doc__', '') or '',
        "module": getattr(obj, '__module__', ''),
    }
    
    # Add signature for callable objects
    if callable(obj):
        try:
            info["signature"] = str(inspect.signature(obj))
        except (ValueError, TypeError):
            info["signature"] = "(...)"
    
    # If it's a module or class, get its members
    if inspect.ismodule(obj) or inspect.isclass(obj):
        info["members"] = {}
        try:
            members = inspect.getmembers(obj)
            for member_name, member_obj in members:
                # Skip private members and avoid circular references
                if (not member_name.startswith('_') or member_name == '__init__') and member_obj is not obj:
                    try:
                        # Only go deeper for objects that belong to this module/class
                        if (hasattr(member_obj, '__module__') and 
                            (member_obj.__module__ == info.get('module') or 
                             member_name in getattr(obj, '__all__', []))):
                            info["members"][member_name] = extract_basic_info(
                                member_obj, member_name, max_depth, current_depth + 1
                            )
                        else:
                            # Just basic info for external objects
                            info["members"][member_name] = {
                                "name": member_name,
                                "type": type(member_obj).__name__,
                                "docstring": getattr(member_obj, '__doc__', '') or '',
                                "external": True
                            }
                    except Exception as e:
                        info["members"][member_name] = {
                            "name": member_name, 
                            "error": str(e)
                        }
        except Exception as e:
            info["members_error"] = str(e)
    
    return info


def save_to_files(data, base_name="csc_docs"):
    """Save the extracted data to both JSON and readable text files."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Save as JSON
    json_filename = f"{base_name}_{timestamp}.json"
    with open(json_filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"JSON data saved to: {json_filename}")
    
    # Save as readable text
    txt_filename = f"{base_name}_{timestamp}.txt"
    with open(txt_filename, 'w', encoding='utf-8') as f:
        write_readable_docs(data, f)
    print(f"Readable docs saved to: {txt_filename}")
    
    return json_filename, txt_filename


def write_readable_docs(info, file, indent=0):
    """Write human-readable documentation to a file."""
    prefix = "  " * indent
    
    file.write(f"{prefix}{info['name']} ({info['type']})\n")
    
    if info.get('signature'):
        file.write(f"{prefix}  Signature: {info['signature']}\n")
    
    if info.get('module'):
        file.write(f"{prefix}  Module: {info['module']}\n")
    
    if info.get('docstring'):
        file.write(f"{prefix}  Documentation:\n")
        for line in info['docstring'].split('\n'):
            file.write(f"{prefix}    {line}\n")
    
    if info.get('members'):
        file.write(f"{prefix}  Members:\n")
        for member_name, member_info in info['members'].items():
            if isinstance(member_info, dict) and not member_info.get('error'):
                write_readable_docs(member_info, file, indent + 2)
            else:
                file.write(f"{prefix}    {member_name}: {member_info}\n")
    
    file.write("\n")


def main():
    """Main function to extract and save CSC documentation."""
    print("=" * 60)
    print("Simple CSC Documentation Extractor")
    print("=" * 60)
    
    try:
        import csc  # This will only work inside Cascadeur
        print(f"Successfully imported csc module: {csc}")
    except ImportError as e:
        print("ERROR: Cannot import csc module!")
        print("This script must be run inside Cascadeur's Python console.")
        print(f"Import error: {e}")
        return None
    
    print("Extracting documentation...")
    
    try:
        # Extract information from the csc module
        csc_info = extract_basic_info(csc, "csc", max_depth=4)
        
        # Save to files
        json_file, txt_file = save_to_files(csc_info)
        
        print("\n" + "=" * 60)
        print("Extraction completed successfully!")
        print("Files created:")
        print(f"  - {json_file} (machine-readable)")
        print(f"  - {txt_file} (human-readable)")
        print("=" * 60)
        
        # Print a quick summary
        members_count = len(csc_info.get('members', {}))
        print(f"Summary: Found {members_count} top-level members in csc module")
        
        if csc_info.get('docstring'):
            print(f"Module description: {csc_info['docstring'][:100]}...")
        
        return csc_info
        
    except Exception as e:
        print(f"ERROR during extraction: {e}")
        import traceback
        traceback.print_exc()
        return None


if __name__ == "__main__":
    result = main()
