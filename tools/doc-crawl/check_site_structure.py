"""
Check the structure of the Cascadeur API documentation site.
This script helps understand what crawling approach to use.
"""

import requests
from urllib.parse import urljoin
import json
from pathlib import Path

BASE_URL = "https://cascadeur.com/python-api/"

def check_site():
    results = {}
    
    # Check for objects.inv (Sphinx inventory)
    print("Checking for Sphinx inventory...")
    inv_urls = [
        urljoin(BASE_URL, "objects.inv"),
        urljoin(BASE_URL, "_static/objects.inv"),
        BASE_URL.rstrip('/') + "/objects.inv"
    ]
    
    for url in inv_urls:
        try:
            response = requests.head(url, timeout=10, allow_redirects=True)
            if response.status_code == 200:
                results['has_objects_inv'] = True
                results['objects_inv_url'] = url
                print(f"Found objects.inv at: {url}")
                break
        except Exception as e:
            print(f"Failed to check {url}: {e}")
    else:
        results['has_objects_inv'] = False
        print("No objects.inv found")
    
    # Check main page
    print("\nChecking main page structure...")
    try:
        response = requests.get(BASE_URL, timeout=10)
        if response.status_code == 200:
            results['main_page_accessible'] = True
            results['main_page_size'] = len(response.content)
            
            # Check for common Sphinx patterns
            content_lower = response.text.lower()
            results['looks_like_sphinx'] = (
                'sphinx' in content_lower or 
                '_static' in content_lower or
                'searchindex.js' in content_lower
            )
            
            # Look for API links
            if 'cascadeur' in content_lower:
                results['has_cascadeur_content'] = True
            
            print(f"Main page accessible: {results['main_page_accessible']}")
            print(f"Page size: {results['main_page_size']} bytes")
            print(f"Looks like Sphinx: {results['looks_like_sphinx']}")
            
    except Exception as e:
        results['main_page_accessible'] = False
        results['error'] = str(e)
        print(f"Failed to access main page: {e}")
    
    # Save results
    output_path = Path("tmp/site_check_results.json")
    output_path.parent.mkdir(exist_ok=True)
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\nResults saved to: {output_path}")
    return results

if __name__ == "__main__":
    results = check_site()
    print("\n" + "="*50)
    print("Summary:")
    for key, value in results.items():
        print(f"  {key}: {value}")