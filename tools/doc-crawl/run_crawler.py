#!/usr/bin/env python
"""
Run the Cascadeur documentation crawler.
This script provides a simple interface to start, resume, or reset the crawler.
"""

import sys
import argparse
import shutil
from pathlib import Path
import json

# Add current directory to path
sys.path.insert(0, str(Path(__file__).parent))

from cascadeur_doc_crawler import CascadeurDocCrawler, STATE_FILE, OUTPUT_DIR, STATE_DIR

def show_status():
    """Show current crawler status"""
    if STATE_FILE.exists():
        with open(STATE_FILE, 'r') as f:
            state = json.load(f)
        
        print("Crawler Status:")
        print("-" * 50)
        print(f"Total pages: {state['total_pages']}")
        print(f"Crawled pages: {len(state['crawled_pages'])}")
        print(f"Failed pages: {len(state['failed_pages'])}")
        print(f"Total symbols: {state['total_symbols']}")
        print(f"Extracted symbols: {state['extracted_symbols']}")
        print(f"Last update: {state['last_update']}")
        
        if state['failed_pages']:
            print("\nFailed pages:")
            for url in state['failed_pages']:
                print(f"  - {url}")
    else:
        print("No crawler state found. Run crawler to start.")

def reset_crawler():
    """Reset crawler state and optionally clean output"""
    response = input("This will delete all crawler state. Continue? (y/N): ")
    if response.lower() != 'y':
        print("Cancelled.")
        return
    
    # Remove state
    if STATE_DIR.exists():
        shutil.rmtree(STATE_DIR)
        print(f"Removed state directory: {STATE_DIR}")
    
    response = input("Also delete downloaded content? (y/N): ")
    if response.lower() == 'y':
        if OUTPUT_DIR.exists():
            shutil.rmtree(OUTPUT_DIR)
            print(f"Removed output directory: {OUTPUT_DIR}")
    
    print("Reset complete.")

def run_crawler():
    """Run or resume the crawler"""
    print("Starting Cascadeur documentation crawler...")
    print("Press Ctrl+C to interrupt (progress will be saved)")
    print("-" * 50)
    
    crawler = CascadeurDocCrawler()
    
    try:
        crawler.crawl()
        print("\n" + "=" * 50)
        print("Crawl completed successfully!")
        
        # Show final statistics
        show_status()
        
    except KeyboardInterrupt:
        print("\n\nCrawl interrupted. Progress has been saved.")
        print("Run again to resume from where you left off.")
        show_status()
    except Exception as e:
        print(f"\nError during crawl: {e}")
        print("Progress has been saved. You can resume after fixing the issue.")
        raise

def main():
    parser = argparse.ArgumentParser(description="Cascadeur Documentation Crawler")
    parser.add_argument('action', choices=['run', 'status', 'reset'], 
                       default='run', nargs='?',
                       help='Action to perform (default: run)')
    
    args = parser.parse_args()
    
    if args.action == 'status':
        show_status()
    elif args.action == 'reset':
        reset_crawler()
    else:  # run
        run_crawler()

if __name__ == "__main__":
    main()