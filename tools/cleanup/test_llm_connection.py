#!/usr/bin/env python3
"""
Test script to verify LiteLLM connection and configuration.
Run this before the main batch cleaning to ensure everything is set up correctly.
"""

import os
import asyncio
import logging
import argparse
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def test_connection(api_key: str, base_url: str = None, model: str = 'gpt-4o'):
    """Test the LiteLLM connection with a simple prompt."""
    try:
        from litellm import acompletion
    except ImportError:
        logger.error("LiteLLM not installed. Please run: pixi add litellm")
        return False
    
    if not api_key:
        logger.error("API key not provided!")
        return False
    
    # Determine model name
    model_name = model
    if base_url and not base_url.startswith("https://api.openai.com"):
        if not model_name.startswith("openai/"):
            model_name = f"openai/{model_name}"
    
    logger.info(f"Testing connection to LLM...")
    logger.info(f"  Model: {model_name}")
    logger.info(f"  Base URL: {base_url or 'default'}")
    
    try:
        # Simple test prompt
        # Use temperature=1 for models that don't support temperature=0 (like gpt-5)
        temp = 1 if 'gpt-5' in model.lower() else 0
        
        response = await acompletion(
            model=model_name,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Reply with exactly: 'Connection successful!'"}
            ],
            api_base=base_url,
            api_key=api_key,
            temperature=temp,
            max_tokens=50,
            timeout=30,
        )
        
        result = response['choices'][0]['message']['content'].strip()
        logger.info(f"Response: {result}")
        
        if "successful" in result.lower():
            logger.info("[OK] LLM connection test passed!")
            return True
        else:
            logger.warning(f"Unexpected response: {result}")
            return False
            
    except Exception as e:
        logger.error(f"Connection test failed: {e}")
        return False


async def test_cleaning_sample(api_key: str, base_url: str = None, model: str = 'gpt-4o'):
    """Test cleaning a small sample document."""
    try:
        from litellm import acompletion
    except ImportError:
        logger.error("LiteLLM not installed")
        return False
    
    # Sample messy documentation
    sample_doc = """---
source_url: https://cascadeur.com/test
---

# csc.test.Sample

Sample class Methods __init__ (*args, **kwargs) test_method (self, arg1) -> str
    """
    
    model_name = model
    if base_url and not base_url.startswith("https://api.openai.com"):
        if not model_name.startswith("openai/"):
            model_name = f"openai/{model_name}"
    
    logger.info("\nTesting document cleaning on sample...")
    
    try:
        # Use temperature=1 for models that don't support other values (like gpt-5)
        temp = 1 if 'gpt-5' in model.lower() else 0.2
        
        response = await acompletion(
            model=model_name,
            messages=[
                {
                    "role": "system", 
                    "content": "Clean this API documentation. Add [CLEAN] marker at the start. Format it properly with sections: Overview, Class Definition, Methods, Usage Example."
                },
                {
                    "role": "user",
                    "content": f"Clean this markdown:\n{sample_doc}"
                }
            ],
            api_base=base_url,
            api_key=api_key,
            temperature=temp,
            max_tokens=500,
            timeout=30,
        )
        
        result = response['choices'][0]['message']['content'].strip()
        
        # Check if result has expected structure
        if "[CLEAN]" in result and "## Overview" in result:
            logger.info("[OK] Sample cleaning test passed!")
            logger.info("Sample output preview:")
            print("-" * 40)
            print(result[:300] + "..." if len(result) > 300 else result)
            print("-" * 40)
            return True
        else:
            logger.warning("Sample cleaning didn't produce expected format")
            return False
            
    except Exception as e:
        logger.error(f"Sample cleaning test failed: {e}")
        return False


async def main():
    """Run all tests."""
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Test LiteLLM connection and configuration')
    parser.add_argument('--api-key', required=True, help='API key for LLM service')
    parser.add_argument('--base-url', help='Base URL for LLM service (e.g., https://yunwu.ai/v1)')
    parser.add_argument('--model', default='gpt-4o', help='Model name (default: gpt-4o)')
    
    args = parser.parse_args()
    
    print("="*50)
    print("LiteLLM Configuration Test")
    print("="*50)
    print()
    
    # Test 1: Connection
    connection_ok = await test_connection(args.api_key, args.base_url, args.model)
    print()
    
    if connection_ok:
        # Test 2: Sample cleaning
        cleaning_ok = await test_cleaning_sample(args.api_key, args.base_url, args.model)
        print()
        
        if cleaning_ok:
            print("[SUCCESS] All tests passed! Ready to run batch cleaning.")
            print("\nTo start batch cleaning, run:")
            print(f"  python tools/cleanup/batch_clean_docs.py --api-key <KEY> --base-url {args.base_url} --model {args.model}")
        else:
            print("[WARNING] Cleaning test failed. Check your prompts and try again.")
    else:
        print("[ERROR] Connection test failed. Please check your configuration:")
        print("  - API key")
        print("  - Base URL (if using custom endpoint)")
        print("  - Model name")


if __name__ == '__main__':
    asyncio.run(main())