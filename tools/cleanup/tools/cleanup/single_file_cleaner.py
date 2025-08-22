#!/usr/bin/env python3
"""
Single file cleaner for use with PowerShell batch processor.
Cleans one markdown file at a time with LLM.
"""

import argparse
import asyncio
import sys
from pathlib import Path
from typing import Optional
import hashlib
from datetime import datetime
import os

async def clean_single_file(
    file_path: Path,
    api_key: str,
    base_url: Optional[str] = None,
    model: str = 'gpt-5'
) -> bool:
    """Clean a single markdown file."""
    try:
        from litellm import acompletion
    except ImportError:
        print("Error: LiteLLM not installed", file=sys.stderr)
        return False
    
    # Read file
    try:
        content = file_path.read_text(encoding='utf-8', errors='ignore')
    except Exception as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        return False
    
    # Check if already clean
    if content.startswith("[CLEAN]"):
        print(f"File already clean: {file_path}")
        return True
    
    # Build prompts
    system_prompt = """You are a precise documentation cleaning assistant for the Cascadeur Python API.
Transform the raw API documentation into a standardized, professional format.

STRICT RULES:
1. Preserve ALL factual API information exactly
2. Add [CLEAN] marker at the very beginning
3. Follow the standard structure (Overview, Class Definition, Methods, etc.)
4. Remove navigation menus and non-API content
5. Output ONLY valid Markdown"""
    
    user_prompt = f"""Clean this markdown documentation:

{content}

Remember to start with [CLEAN] marker."""
    
    # Determine model name for LiteLLM
    model_name = model
    if base_url and not base_url.startswith("https://api.openai.com"):
        if not model_name.startswith("openai/"):
            model_name = f"openai/{model_name}"
    
    # Use appropriate temperature for model
    temp = 1 if 'gpt-5' in model.lower() else 0.2
    
    try:
        # Make LLM call
        response = await acompletion(
            model=model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            api_base=base_url,
            api_key=api_key,
            temperature=temp,
            max_tokens=8192,
            timeout=120,
        )

        cleaned = None
        # Dict path
        if isinstance(response, dict):
            choices = response.get('choices') or []
            if choices:
                first = choices[0] or {}
                if isinstance(first, dict):
                    msg = first.get('message') or {}
                    cleaned = msg.get('content')
        # Attribute path
        if cleaned is None:
            ch = getattr(response, 'choices', None)
            if ch:
                try:
                    first = ch[0]
                    msg = getattr(first, 'message', None)
                    if msg and hasattr(msg, 'content'):
                        cleaned = msg.content
                except Exception:
                    pass
        if not cleaned:
            raise RuntimeError('Could not extract content from response structure')
        cleaned = cleaned.strip()
        
        # Ensure [CLEAN] marker
        if not cleaned.startswith("[CLEAN]"):
            cleaned = f"[CLEAN]\n\n{cleaned}"
        
        # Add metadata comment
        original_hash = hashlib.md5(content.encode()).hexdigest()[:8]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        cleaned = cleaned.replace(
            "[CLEAN]",
            f"[CLEAN]\n<!-- Cleaned by batch script {timestamp} | Original: {original_hash} -->"
        )
        
        # Write back to file
        file_path.write_text(cleaned, encoding='utf-8')
        print(f"Successfully cleaned: {file_path}")
        return True
        
    except Exception as e:
        print(f"Error cleaning file: {e}", file=sys.stderr)
        return False

async def main():
    parser = argparse.ArgumentParser(description='Clean a single markdown file')
    parser.add_argument('--file', required=True, type=Path, help='File to clean')
    parser.add_argument('--api-key', required=True, help='API key')
    parser.add_argument('--base-url', help='Base URL for LLM')
    parser.add_argument('--model', help='Model name (arg > env CUSTOM_LLM_MODEL > gpt-5)')
    
    args = parser.parse_args()
    
    resolved_model = args.model or os.getenv('CUSTOM_LLM_MODEL') or 'gpt-5'
    success = await clean_single_file(
        file_path=args.file,
        api_key=args.api_key,
        base_url=args.base_url,
        model=resolved_model
    )
    
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    asyncio.run(main())
