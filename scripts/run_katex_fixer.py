#!/usr/bin/env python3
"""
Example usage of the KaTeX error fixer script.
"""

import subprocess
import sys
from pathlib import Path

def run_fix_script():
    """Run the KaTeX error fixer script with examples."""
    
    script_path = Path(__file__).parent / "fix_katex_errors.py"
    
    print("🔧 KaTeX Error Fixer - Usage Examples")
    print("=" * 50)
    
    print("\n1. DRY RUN - See what would be fixed without making changes:")
    print(f"   python {script_path} --dry-run")
    
    print("\n2. Fix all files in cascadeur-docs directory:")
    print(f"   python {script_path}")
    
    print("\n3. Fix files in a specific directory:")
    print(f"   python {script_path} /path/to/your/docs")
    
    print("\n4. Process the current file's directory:")
    current_dir = Path(__file__).parent.parent / "cascadeur-docs"
    print(f"   python {script_path} {current_dir}")
    
    # Ask user what they want to do
    print("\nWhat would you like to do?")
    print("1. Run dry-run on cascadeur-docs")
    print("2. Fix all files in cascadeur-docs")
    print("3. Exit")
    
    choice = input("\nEnter choice (1-3): ").strip()
    
    if choice == "1":
        print("\n🧪 Running dry-run...")
        subprocess.run([sys.executable, str(script_path), "--dry-run"])
    elif choice == "2":
        print("\n⚠️  This will modify files! Backups will be created.")
        confirm = input("Continue? (y/N): ").strip().lower()
        if confirm == 'y':
            print("\n🔧 Fixing files...")
            subprocess.run([sys.executable, str(script_path)])
        else:
            print("Cancelled.")
    else:
        print("Goodbye!")

if __name__ == "__main__":
    run_fix_script()
