#!/usr/bin/env python3
"""
Install Firecrawl Python SDK and create example usage
"""

import subprocess
import sys
import os

def install_firecrawl():
    """Install the Firecrawl Python SDK"""
    try:
        print("Installing Firecrawl Python SDK...")
        subprocess.run([sys.executable, "-m", "pip", "install", "firecrawl-py"], check=True)
        print("✅ Firecrawl SDK installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install Firecrawl SDK: {e}")
        return False

def create_env_template():
    """Create a template .env file"""
    env_content = """# Firecrawl API Configuration
# Get your API key from: https://firecrawl.dev/
FIRECRAWL_API_KEY=your_api_key_here
"""
    
    with open('.env.example', 'w') as f:
        f.write(env_content)
    
    print("📝 Created .env.example file")
    print("👆 Copy this to .env and add your Firecrawl API key")

def main():
    print("🔥 Firecrawl Setup for Cascadeur Documentation Crawling")
    print("=" * 60)
    
    # Install the SDK
    if install_firecrawl():
        create_env_template()
        
        print("\n🎉 Setup complete!")
        print("\nNext steps:")
        print("1. Get a Firecrawl API key from https://firecrawl.dev/")
        print("2. Copy .env.example to .env and add your API key")
        print("3. Run: python crawl_cascadeur_docs.py")
    else:
        print("\n❌ Setup failed. Please check your Python environment.")

if __name__ == "__main__":
    main()
