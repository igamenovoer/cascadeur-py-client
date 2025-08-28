#!/usr/bin/env python3
"""
Cascadeur CSC Module Documentation Extractor

This script should be run INSIDE Cascadeur's Python console to extract
all docstrings from the csc module and create documentation files.

Usage:
1. Open Cascadeur
2. Open Python console in Cascadeur
3. Run: exec(open(r'path\\to\\this\\script.py').read())
"""

import inspect
from pathlib import Path
import json
from datetime import datetime

def safe_getattr(obj, attr, default=None):
    """Safely get attribute without causing exceptions."""
    try:
        return getattr(obj, attr, default)
    except Exception:
        return default

def safe_getdoc(obj):
    """Safely get docstring without causing exceptions."""
    try:
        return inspect.getdoc(obj) or ""
    except Exception:
        return ""

def get_signature_str(obj):
    """Get function/method signature as string."""
    try:
        return str(inspect.signature(obj))
    except Exception:
        return ""

def extract_module_info(module, module_path="", visited=None):
    """
    Extract comprehensive information from a module including all classes,
    functions, and submodules with their docstrings.
    """
    if visited is None:
        visited = set()
    
    module_name = getattr(module, '__name__', str(module))
    
    # Avoid infinite recursion
    if module_name in visited:
        return None
    visited.add(module_name)
    
    info = {
        'name': module_name,
        'path': module_path,
        'docstring': safe_getdoc(module),
        'file': safe_getattr(module, '__file__', ''),
        'classes': {},
        'functions': {},
        'submodules': {},
        'constants': {},
        'extracted_at': datetime.now().isoformat()
    }
    
    try:
        members = inspect.getmembers(module)
    except Exception:
        return info
    
    for name, obj in members:
        # Skip private members and special attributes
        if name.startswith('_'):
            continue
            
        try:
            # Check if this object belongs to this module
            obj_module = safe_getattr(obj, '__module__', '')
            
            if inspect.isclass(obj):
                class_info = extract_class_info(obj)
                if class_info:
                    info['classes'][name] = class_info
                    
            elif inspect.isfunction(obj) or inspect.ismethod(obj):
                func_info = extract_function_info(obj)
                if func_info:
                    info['functions'][name] = func_info
                    
            elif inspect.ismodule(obj):
                # Only traverse submodules that belong to the same package
                if (obj_module.startswith(module_name) or 
                    name in getattr(module, '__all__', []) or
                    hasattr(module, '__path__')):  # It's a package
                    
                    submodule_path = f"{module_path}.{name}" if module_path else name
                    submodule_info = extract_module_info(obj, submodule_path, visited)
                    if submodule_info:
                        info['submodules'][name] = submodule_info
                        
            else:
                # Check if it's a constant or variable with documentation
                if hasattr(obj, '__doc__') and obj.__doc__:
                    info['constants'][name] = {
                        'value': repr(obj) if len(repr(obj)) < 200 else f"{type(obj).__name__} object",
                        'type': type(obj).__name__,
                        'docstring': safe_getdoc(obj)
                    }
                elif not callable(obj) and not inspect.ismodule(obj):
                    # Simple constant without docstring
                    try:
                        value_repr = repr(obj)
                        if len(value_repr) < 100:  # Only store small values
                            info['constants'][name] = {
                                'value': value_repr,
                                'type': type(obj).__name__,
                                'docstring': ''
                            }
                    except Exception:
                        pass
                        
        except Exception as e:
            print(f"Error processing {name}: {e}")
            continue
    
    return info

def extract_class_info(cls):
    """Extract information from a class including methods and attributes."""
    try:
        info = {
            'name': cls.__name__,
            'docstring': safe_getdoc(cls),
            'module': safe_getattr(cls, '__module__', ''),
            'bases': [base.__name__ for base in getattr(cls, '__bases__', [])],
            'methods': {},
            'properties': {},
            'class_variables': {}
        }
        
        # Get all members of the class
        try:
            members = inspect.getmembers(cls)
        except Exception:
            return info
            
        for name, obj in members:
            if name.startswith('_') and name not in ['__init__', '__str__', '__repr__']:
                continue
                
            try:
                if inspect.ismethod(obj) or inspect.isfunction(obj):
                    method_info = extract_function_info(obj)
                    if method_info:
                        info['methods'][name] = method_info
                        
                elif isinstance(obj, property):
                    info['properties'][name] = {
                        'docstring': safe_getdoc(obj),
                        'getter': obj.fget is not None,
                        'setter': obj.fset is not None,
                        'deleter': obj.fdel is not None
                    }
                    
                elif not callable(obj):
                    # Class variable
                    try:
                        value_repr = repr(obj)
                        if len(value_repr) < 100:
                            info['class_variables'][name] = {
                                'value': value_repr,
                                'type': type(obj).__name__
                            }
                    except Exception:
                        pass
                        
            except Exception as e:
                print(f"Error processing class member {name}: {e}")
                continue
                
        return info
        
    except Exception as e:
        print(f"Error extracting class info: {e}")
        return None

def extract_function_info(func):
    """Extract information from a function or method."""
    try:
        info = {
            'name': getattr(func, '__name__', str(func)),
            'docstring': safe_getdoc(func),
            'signature': get_signature_str(func),
            'module': safe_getattr(func, '__module__', ''),
            'is_method': inspect.ismethod(func),
            'is_function': inspect.isfunction(func),
            'is_builtin': inspect.isbuiltin(func)
        }
        return info
    except Exception as e:
        print(f"Error extracting function info: {e}")
        return None

def create_markdown_docs(module_info, output_dir):
    """Create markdown documentation files from extracted module info."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    def write_module_md(info, path_parts):
        """Write markdown file for a module."""
        if not path_parts:
            filename = "index.md"
        else:
            filename = f"{'_'.join(path_parts)}.md"
            
        file_path = output_path / filename
        
        with open(file_path, 'w', encoding='utf-8') as f:
            # Module header
            module_name = info['name']
            f.write(f"# {module_name}\n\n")
            
            if info['docstring']:
                f.write(f"{info['docstring']}\n\n")
            
            # Module info
            f.write("## Module Information\n\n")
            f.write(f"- **Name**: `{info['name']}`\n")
            f.write(f"- **File**: `{info['file']}`\n")
            f.write(f"- **Extracted**: {info['extracted_at']}\n\n")
            
            # Constants
            if info['constants']:
                f.write("## Constants\n\n")
                for name, const_info in info['constants'].items():
                    f.write(f"### {name}\n\n")
                    f.write(f"- **Type**: `{const_info['type']}`\n")
                    f.write(f"- **Value**: `{const_info['value']}`\n")
                    if const_info['docstring']:
                        f.write(f"\n{const_info['docstring']}\n")
                    f.write("\n")
            
            # Functions
            if info['functions']:
                f.write("## Functions\n\n")
                for name, func_info in info['functions'].items():
                    f.write(f"### {name}{func_info['signature']}\n\n")
                    if func_info['docstring']:
                        f.write(f"{func_info['docstring']}\n\n")
                    else:
                        f.write("*No documentation available.*\n\n")
            
            # Classes
            if info['classes']:
                f.write("## Classes\n\n")
                for name, class_info in info['classes'].items():
                    f.write(f"### {name}\n\n")
                    if class_info['docstring']:
                        f.write(f"{class_info['docstring']}\n\n")
                    
                    if class_info['bases']:
                        f.write(f"**Inherits from**: {', '.join(class_info['bases'])}\n\n")
                    
                    # Class methods
                    if class_info['methods']:
                        f.write("#### Methods\n\n")
                        for method_name, method_info in class_info['methods'].items():
                            f.write(f"##### {method_name}{method_info['signature']}\n\n")
                            if method_info['docstring']:
                                f.write(f"{method_info['docstring']}\n\n")
                            else:
                                f.write("*No documentation available.*\n\n")
                    
                    # Properties
                    if class_info['properties']:
                        f.write("#### Properties\n\n")
                        for prop_name, prop_info in class_info['properties'].items():
                            f.write(f"##### {prop_name}\n\n")
                            if prop_info['docstring']:
                                f.write(f"{prop_info['docstring']}\n\n")
                            access = []
                            if prop_info['getter']:
                                access.append("get")
                            if prop_info['setter']:
                                access.append("set")
                            if prop_info['deleter']:
                                access.append("del")
                            f.write(f"*Access: {', '.join(access)}*\n\n")
            
            # Submodules
            if info['submodules']:
                f.write("## Submodules\n\n")
                for submod_name, submod_info in info['submodules'].items():
                    f.write(f"- [`{submod_name}`]({submod_name}.md)")
                    if submod_info['docstring']:
                        first_line = submod_info['docstring'].split('\n')[0]
                        f.write(f" - {first_line}")
                    f.write("\n")
                f.write("\n")
        
        print(f"Created: {file_path}")
    
    # Write main module
    write_module_md(module_info, [])
    
    # Write submodules recursively
    def write_submodules(info, path_parts):
        for submod_name, submod_info in info['submodules'].items():
            new_path_parts = path_parts + [submod_name]
            write_module_md(submod_info, new_path_parts)
            write_submodules(submod_info, new_path_parts)
    
    write_submodules(module_info, [])

def main():
    """Main function to extract CSC documentation."""
    print("Cascadeur CSC Documentation Extractor")
    print("=" * 50)
    
    try:
        # Import the csc module (this will only work in Cascadeur)
        import csc
        print(f"Successfully imported csc module: {csc}")
    except ImportError as e:
        print("ERROR: Cannot import csc module. This script must be run inside Cascadeur!")
        print(f"Import error: {e}")
        return
    
    # Set output directory
    output_dir = "csc_documentation"
    
    print("Extracting documentation from csc module...")
    print(f"Output directory: {output_dir}")
    
    try:
        # Extract all information from csc module
        csc_info = extract_module_info(csc)
        
        # Save raw data as JSON for debugging
        json_file = Path(output_dir) / "csc_raw_data.json"
        json_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(csc_info, f, indent=2, default=str)
        print(f"Raw data saved to: {json_file}")
        
        # Create markdown documentation
        print("Creating markdown documentation...")
        create_markdown_docs(csc_info, output_dir)
        
        print("\nDocumentation extraction completed!")
        print(f"Check the '{output_dir}' directory for generated files.")
        print("\nGenerated files:")
        for file_path in Path(output_dir).glob("*.md"):
            print(f"  - {file_path.name}")
            
    except Exception as e:
        print(f"ERROR during extraction: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
