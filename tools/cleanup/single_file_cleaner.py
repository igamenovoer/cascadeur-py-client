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
import json
import os

CACHE_DIR = Path(os.getenv("DOC_CLEAN_CACHE_DIR", "tmp/clean_cache"))
CACHE_DIR.mkdir(parents=True, exist_ok=True)
CACHE_VERSION = 2  # bump if prompt / logic changes

def cache_key(file_content: str, model: str, base_url: Optional[str], system_prompt: str) -> str:
    h = hashlib.sha256()
    h.update(str(CACHE_VERSION).encode())
    h.update(model.encode())
    if base_url:
        h.update(base_url.encode())
    # include prompt fingerprint
    h.update(hashlib.sha256(system_prompt.encode()).hexdigest().encode())
    # Use first 120k chars to bound hash work for huge files
    snippet = file_content[:120_000]
    h.update(snippet.encode())
    return h.hexdigest()

def try_load_cache(key: str) -> Optional[str]:
    p = CACHE_DIR / f"{key}.json"
    if not p.exists():
        return None
    try:
        data = json.loads(p.read_text(encoding='utf-8'))
        return data.get("cleaned")
    except Exception:
        return None

def save_cache(key: str, cleaned: str):
    p = CACHE_DIR / f"{key}.json"
    try:
        payload = {"cleaned": cleaned, "ts": datetime.utcnow().isoformat()} 
        p.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding='utf-8')
    except Exception:
        pass

async def clean_single_file(
    file_path: Path,
    api_key: str,
    base_url: Optional[str] = None,
    model: str = 'gpt-4o'
) -> bool:
    """Clean a single markdown file."""
    debug = os.getenv('DOC_CLEAN_DEBUG', '0') == '1'
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
    
    # Check if already clean (support both markers)
    cleaned_marker_found = content.startswith("[CLEAN]") or content.lstrip().startswith("<!-- [CLEAN] -->")
    if cleaned_marker_found:
        if debug:
            print(f"DEBUG: Skip already clean {file_path}")
        return True
    
    # Build prompts
    system_prompt = """You are a precise documentation cleaning assistant for the Cascadeur Python API.
Transform the raw API documentation into a standardized, professional format.

STRICT RULES:
1. Preserve ALL factual API information exactly (class names, method names, signatures, parameters, return types)
2. NEVER invent or remove API methods or parameters
3. Add [CLEAN] marker at the very beginning of the output
4. Follow this exact structure:

[CLEAN]

# module.name.ClassName

**Module:** `module.name.ClassName`  
**Source:** [Cascadeur Python API Documentation](original_url)

## Overview

Brief description of the class/module purpose and functionality.

## Class Definition

```python
class module.name.ClassName
```

Additional context about the class.

## Constructor

### `__init__(params) -> None`

Description of constructor.

**Parameters:**
- `param_name` (type): Description

**Returns:**
- None

## Methods

### `method_name(params) -> return_type`

Method description.

**Parameters:**
- `param` (type): Description

**Returns:**
- return_type: Description

## Usage Example

```python
import module.name

# Practical usage example
instance = module.name.ClassName()
result = instance.method_name(params)
```

## Usage Notes

- Key usage information
- Important considerations
- Best practices

## See Also

- Related classes and modules

5. If the input is too malformed, preserve all method information verbatim
6. Output ONLY valid Markdown
7. Remove ALL navigation menus, social media links, footer content, and non-API content

GPT-5 SPECIFIC INSTRUCTIONS (if applicable):
- Minimize reasoning tokens; use concise internal reasoning only when necessary.
- Obey requested verbosity level (default low) and do not add extraneous commentary.
- Deterministic, stable formatting is higher priority than creative paraphrasing.
"""
    
    # Extract source URL if present
    source_url = "https://cascadeur.com/python-api/"
    import re
    url_match = re.search(r'source_url:\s*(https?://[^\s]+)', content)
    if url_match:
        source_url = url_match.group(1)
    
    user_prompt = f"""<ORIGINAL_PATH>{file_path}</ORIGINAL_PATH>
<SOURCE_URL>{source_url}</SOURCE_URL>
<ORIGINAL_MARKDOWN>
{content}
</ORIGINAL_MARKDOWN>

Provide the cleaned markdown now. Remember to start with [CLEAN] marker."""
    
    # Determine model name for LiteLLM
    model_name = model
    if base_url and not base_url.startswith("https://api.openai.com"):
        if not model_name.startswith("openai/"):
            model_name = f"openai/{model_name}"
    
    # Temperature: provider requires temperature=1 for gpt-5 (error if not). We'll conform.
    if 'gpt-5' in model.lower():
        temp = 1
    else:
        temp = 0.2

    # GPT-5 additional controls (env override)
    reasoning_effort = os.getenv('DOC_CLEAN_REASONING_EFFORT', 'minimal')  # minimal|medium|max
    verbosity = os.getenv('DOC_CLEAN_VERBOSITY', 'low')  # low|medium|high
    max_output_tokens_env = os.getenv('DOC_CLEAN_MAX_OUTPUT_TOKENS')
    try:
        max_output_tokens = int(max_output_tokens_env) if max_output_tokens_env else None
    except ValueError:
        max_output_tokens = None
    
    # Prompt cache
    key = cache_key(content, model_name, base_url, system_prompt)
    if os.getenv('DISABLE_DOC_CLEAN_CACHE', '0') != '1':
        cached = try_load_cache(key)
        if cached:
            # Ensure marker presence & rewrite metadata but skip LLM
            if not cached.startswith("[CLEAN]"):
                cached = f"[CLEAN]\n{cached}"
            original_hash = hashlib.md5(content.encode()).hexdigest()[:8]
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
            # Replace prior metadata line if exists
            lines = cached.splitlines()
            if len(lines) > 1 and lines[1].startswith("<!-- Cleaned by batch"):
                lines[1] = f"<!-- Cached reuse {timestamp} | Original: {original_hash} -->"
                cached = "\n".join(lines)
            else:
                cached = cached.replace(
                    "[CLEAN]",
                    f"[CLEAN]\n<!-- Cached reuse {timestamp} | Original: {original_hash} -->",
                    1,
                )
            file_path.write_text(cached, encoding='utf-8')
            print(f"Cache hit: {file_path}")
            return True

    try:
        response = None
        if 'gpt-5' in model_name:
            try:
                if max_output_tokens:
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
                        reasoning_effort=reasoning_effort,  # type: ignore[arg-type]
                        verbosity=verbosity,               # type: ignore[arg-type]
                        max_output_tokens=max_output_tokens,  # type: ignore[arg-type]
                    )
                else:
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
                        reasoning_effort=reasoning_effort,  # type: ignore[arg-type]
                        verbosity=verbosity,               # type: ignore[arg-type]
                    )
            except Exception as gpt5_param_err:
                em = str(gpt5_param_err)
                unsupported = any(tok in em.lower() for tok in [
                    'unexpected', 'reasoning_effort', 'verbosity', 'max_output_tokens', 'invalid param'
                ])
                if unsupported:
                    print("Warning: GPT-5 extended params unsupported by backend. Falling back to basic call.", file=sys.stderr)
                else:
                    # pass through unknown error
                    raise
        if response is None:
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
        # Extract content; LiteLLM may return dict-like or object; ensure dict
        # Normalize response to dict structure
        cleaned = None
        if isinstance(response, dict):
            try:
                cleaned = response['choices'][0]['message']['content']
            except Exception:
                pass
        if cleaned is None:
            # Attempt to serialize via model_dump() or to_json()
            data_obj = None
            for attr in ("model_dump", "dict"):
                if hasattr(response, attr):
                    try:
                        data_obj = getattr(response, attr)()
                        break
                    except Exception:
                        continue
            # Skip to_json path to avoid unknown attribute errors
            if isinstance(data_obj, dict):
                try:
                    cleaned = data_obj['choices'][0]['message']['content']
                except Exception:
                    pass
        if cleaned is None:
            # Attribute style
            choices = getattr(response, 'choices', None)
            if choices:
                first = choices[0]
                msg = getattr(first, 'message', None)
                if msg and hasattr(msg, 'content'):
                    cleaned = msg.content
        if cleaned is None:
            if debug:
                print(f"DEBUG: Response type={type(response)} attrs={dir(response)[:12]}")
            raise RuntimeError('Could not extract LLM content from response structure')
        cleaned = (cleaned or '').strip()
        if not cleaned.startswith("[CLEAN]"):
            cleaned = f"[CLEAN]\n\n{cleaned}"
        original_hash = hashlib.md5(content.encode()).hexdigest()[:8]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        cleaned = cleaned.replace(
            "[CLEAN]",
            f"[CLEAN]\n<!-- Cleaned by batch script {timestamp} | Original: {original_hash} -->"
        )
        file_path.write_text(cleaned, encoding='utf-8')
        save_cache(key, cleaned)
        print(f"Successfully cleaned: {file_path}")
        return True
    except Exception as e:
        # Provide more detailed error information
        error_msg = str(e)
        if debug:
            print(f"DEBUG ERROR type={type(e)} message={error_msg}")
        if "timeout" in error_msg.lower():
            print("Error: LLM request timeout after 120 seconds", file=sys.stderr)
        elif "connection" in error_msg.lower():
            print(f"Error: Connection failed - {error_msg}", file=sys.stderr)
        elif "rate" in error_msg.lower() or "429" in error_msg:
            print(f"Error: Rate limit exceeded - {error_msg}", file=sys.stderr)
        else:
            # Add minimal debug context (first 80 chars of file, length)
            snippet = content[:80].replace("\n", " ")
            print(f"Error cleaning file: {error_msg} | snippet='{snippet}' len={len(content)}", file=sys.stderr)
        return False

async def main():
    parser = argparse.ArgumentParser(description='Clean a single markdown file')
    parser.add_argument('--file', required=True, type=Path, help='File to clean')
    parser.add_argument('--api-key', required=False, help='API key (optional if env CUSTOM_LLM_API_KEY or tools/cleanup/.api_key present)')
    parser.add_argument('--base-url', help='Base URL for LLM (optional if env CUSTOM_LLM_BASE_URL or .api_base_url present)')
    parser.add_argument('--model', help='Model name (optional, overrides env/.api_model_name)')
    
    args = parser.parse_args()
    api_key = args.api_key or os.getenv('CUSTOM_LLM_API_KEY')
    if not api_key:
        # Try local .api_key file relative to script
        key_path = Path(__file__).parent / '.api_key'
        if key_path.exists():
            api_key = key_path.read_text(encoding='utf-8').strip()
    if not api_key:
        print("ERROR: Missing API key. Provide via --api-key, CUSTOM_LLM_API_KEY env, or tools/cleanup/.api_key", file=sys.stderr)
        print(f"DEBUG argv: {sys.argv}", file=sys.stderr)
        sys.exit(2)
    # Resolve base_url (arg > env > file)
    base_url = args.base_url or os.getenv('CUSTOM_LLM_BASE_URL')
    if not base_url:
        f = Path(__file__).parent / '.api_base_url'
        if f.exists():
            base_url = f.read_text(encoding='utf-8').strip()
    # Resolve model (arg > env > .api_model_name > default gpt-5)
    model_arg = args.model.strip() if args.model else ''
    if not model_arg:
        env_model = os.getenv('CUSTOM_LLM_MODEL', '').strip()
        model_arg = env_model
    if not model_arg:
        mf = Path(__file__).parent / '.api_model_name'
        if mf.exists():
            try:
                model_arg = mf.read_text(encoding='utf-8').strip()
            except Exception:
                model_arg = ''
    if not model_arg:
        model_arg = 'gpt-5'
    if not model_arg:
        print("ERROR: Could not determine model name", file=sys.stderr)
        sys.exit(2)
    if os.getenv('DOC_CLEAN_DEBUG','0')=='1':
        print(f"DEBUG using model={model_arg} base_url={base_url} api_key_len={len(api_key)}")
    
    success = await clean_single_file(
        file_path=args.file,
        api_key=api_key,
        base_url=base_url,
        model=model_arg
    )
    
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    asyncio.run(main())