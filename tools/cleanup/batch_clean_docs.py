#!/usr/bin/env python3
"""
Batch clean API documentation using LiteLLM.
Transforms raw markdown files into standardized format.
"""

import os
import re
import json
import asyncio
import time
import hashlib
import argparse
from functools import lru_cache
from pathlib import Path
from typing import Dict, List, Optional, Set, Any, Tuple
from dataclasses import dataclass, field, asdict
from datetime import datetime
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Disable unicode emojis in console output (Windows environment)
# Using simple ASCII indicators instead

@dataclass
class CleaningState:
    """State tracking for cleaning progress."""
    processed: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    failed: List[str] = field(default_factory=list)
    skipped: List[str] = field(default_factory=list)
    cleaned: List[str] = field(default_factory=list)
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'CleaningState':
        """Create from dictionary."""
        return cls(**data)


class DocumentCleaner:
    """Main document cleaning orchestrator using LiteLLM."""
    
    def __init__(
        self,
        src_dir: Path,
        state_path: Path,
        api_key: str,
        base_url: Optional[str] = None,
        model: str = 'gpt-5',
        guide_path: Optional[Path] = None,
        max_concurrency: int = 5,
        max_input_chars: int = 40000,
        include_guide: bool = True
    ):
        # Core configuration
        self.src_dir = src_dir
        self.state_path = state_path
        self.guide_path = guide_path or Path('context/hints/howto-clean-api-documentation.md')
        self.max_concurrency = max_concurrency
        self.max_input_chars = max_input_chars
        self.include_guide = include_guide

        # LiteLLM configuration
        self.model = model
        self.base_url = base_url
        self.api_key = api_key

        # Validate configuration
        if not self.api_key:
            raise ValueError("API key must be provided")

        # State
        self.state: CleaningState = self._load_state()
        self.clean_marker = "[CLEAN]"
        
    def _load_state(self) -> CleaningState:
        """Load cleaning state from disk."""
        if self.state_path.exists():
            try:
                data = json.loads(self.state_path.read_text(encoding='utf-8'))
                return CleaningState.from_dict(data)
            except Exception as e:
                logger.warning(f"Failed to load state: {e}. Starting fresh.")
        return CleaningState()
    
    def _save_state(self) -> None:
        """Save cleaning state to disk."""
        self.state_path.parent.mkdir(parents=True, exist_ok=True)
        self.state_path.write_text(
            json.dumps(self.state.to_dict(), indent=2),
            encoding='utf-8'
        )
    
    def _build_system_prompt(self) -> str:
        """Build the system prompt for LLM."""
        base_prompt = """You are a precise documentation cleaning assistant for the Cascadeur Python API.

Your task is to transform raw API documentation into a standardized, professional format.

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
7. Remove ALL navigation menus, social media links, footer content, and non-API content"""
        
        if self.include_guide and self.guide_path.exists():
            try:
                guide_text = self.guide_path.read_text(encoding='utf-8', errors='ignore')
                # Truncate if too long
                max_guide_chars = 20000
                if len(guide_text) > max_guide_chars:
                    guide_text = guide_text[:max_guide_chars] + f"\n... [GUIDE TRUNCATED {len(guide_text)-max_guide_chars} CHARS]"
                base_prompt += f"\n\nADDITIONAL FORMATTING GUIDE:\n{guide_text}"
            except Exception as e:
                logger.warning(f"Failed to include guide: {e}")
        
        return base_prompt
    
    def _should_process_file(self, path: Path) -> bool:
        """Check if a file should be processed."""
        if not path.suffix == '.md':
            return False
        
        # Skip if already processed in current session
        if str(path) in self.state.processed:
            return False
        
        try:
            content = path.read_text(encoding='utf-8', errors='ignore')
            # Skip if already has clean marker
            if self.clean_marker in content:
                return False
            # Skip if empty or too small
            if len(content.strip()) < 50:
                return False
            return True
        except Exception as e:
            logger.error(f"Error checking file {path}: {e}")
            return False
    
    def _extract_api_info(self, content: str) -> Set[str]:
        """Extract method names from original content for validation."""
        # Look for common patterns indicating method names
        patterns = [
            r'\b([A-Za-z_][A-Za-z0-9_]*)\s*\(',  # method_name(
            r'def\s+([A-Za-z_][A-Za-z0-9_]*)',    # def method_name
            r'`([A-Za-z_][A-Za-z0-9_]*)\(`',      # `method_name(`
        ]
        
        methods = set()
        for pattern in patterns:
            matches = re.findall(pattern, content)
            methods.update(matches)
        
        # Filter out common false positives
        exclude = {'self', 'None', 'True', 'False', 'print', 'import', 'from', 'class', 'def', 'return'}
        methods = {m for m in methods if m not in exclude and not m.startswith('__')}
        
        return methods
    
    def _validate_cleaned_content(self, original: str, cleaned: str) -> Tuple[bool, Optional[str]]:
        """Validate that cleaned content preserves essential information."""
        # Check for clean marker
        if self.clean_marker not in cleaned:
            return False, "Missing [CLEAN] marker"
        
        # Check for basic markdown structure
        if not re.search(r'^#\s+', cleaned, re.MULTILINE):
            return False, "Missing markdown headers"
        
        # Extract methods from both versions
        original_methods = self._extract_api_info(original)
        cleaned_methods = self._extract_api_info(cleaned)
        
        # Allow some flexibility but check for major omissions
        if original_methods and len(original_methods) < 50:  # Only validate for smaller APIs
            missing = original_methods - cleaned_methods
            if len(missing) > len(original_methods) * 0.3:  # More than 30% missing
                return False, f"Too many missing methods: {list(missing)[:10]}"
        
        # Check for hallucination indicators
        hallucination_patterns = [
            r'\bTODO\b',
            r'\bPLACEHOLDER\b',
            r'This method might',
            r'probably',
            r'Unable to determine'
        ]
        for pattern in hallucination_patterns:
            if re.search(pattern, cleaned, re.IGNORECASE):
                return False, f"Potential hallucination detected: {pattern}"
        
        return True, None
    
    async def _clean_with_llm(self, path: Path, content: str, semaphore: asyncio.Semaphore) -> Optional[str]:
        """Clean a single document using LiteLLM."""
        try:
            # Import LiteLLM here to handle import errors gracefully
            from litellm import acompletion
        except ImportError:
            logger.error("LiteLLM not installed. Run: pip install litellm")
            return None
        
        # Truncate if too long
        original_content = content
        if len(content) > self.max_input_chars:
            content = content[:self.max_input_chars] + f"\n... [TRUNCATED: {len(content)-self.max_input_chars} BYTES REMOVED]"
        
        # Extract source URL if present
        source_url = "https://cascadeur.com/python-api/"
        url_match = re.search(r'source_url:\s*(https?://[^\s]+)', content)
        if url_match:
            source_url = url_match.group(1)
        
        # Build prompts
        system_prompt = self._build_system_prompt()
        user_prompt = f"""<ORIGINAL_PATH>{path}</ORIGINAL_PATH>
<SOURCE_URL>{source_url}</SOURCE_URL>
<ORIGINAL_MARKDOWN>
{content}
</ORIGINAL_MARKDOWN>

Provide the cleaned markdown now. Remember to start with [CLEAN] marker."""
        
        async with semaphore:
            max_retries = 3
            for attempt in range(max_retries):
                try:
                    # Make LLM call
                    logger.info(f"Processing {path.name} (attempt {attempt + 1}/{max_retries})")
                    
                    # Determine model prefix for OpenAI-compatible endpoints
                    model_name = self.model
                    if self.base_url and not self.base_url.startswith("https://api.openai.com"):
                        # Add openai/ prefix for custom OpenAI-compatible endpoints
                        if not model_name.startswith("openai/"):
                            model_name = f"openai/{model_name}"
                    
                    # Use temperature=1 for models that don't support other values (like gpt-5)
                    temp = 1 if 'gpt-5' in self.model.lower() else 0.2
                    
                    response = await acompletion(
                        model=model_name,
                        messages=[
                            {"role": "system", "content": system_prompt},
                            {"role": "user", "content": user_prompt}
                        ],
                        api_base=self.base_url,
                        api_key=self.api_key,
                        temperature=temp,  # Model-specific temperature
                        max_tokens=8192,  # Generous token limit
                        num_retries=2,    # LiteLLM internal retries
                        timeout=120,
                    )
                    
                    # Extract content defensively (LiteLLM may return object with model_dump or dict)
                    cleaned = None
                    try:
                        if isinstance(response, dict):
                            choices = response.get('choices') or []
                            if choices:
                                first = choices[0] or {}
                                if isinstance(first, dict):
                                    cleaned = (first.get('message') or {}).get('content', '')
                        else:
                            # Try attribute access
                            if hasattr(response, 'choices'):
                                choices = response.choices  # type: ignore
                                if choices:
                                    first = choices[0]
                                    if isinstance(first, dict):
                                        cleaned = first.get('message', {}).get('content', '')
                                    else:
                                        msg = getattr(first, 'message', None) or getattr(first, 'delta', None)
                                        if msg:
                                            cleaned = getattr(msg, 'content', '') or (msg.get('content') if isinstance(msg, dict) else '')
                        if cleaned is None:
                            raise ValueError("Could not extract content from response")
                        cleaned = cleaned.strip()
                    except Exception as ex:
                        logger.error(f"Failed to extract content for {path.name}: {ex}")
                        raise
                    
                    # Ensure clean marker is present
                    if not cleaned.startswith(self.clean_marker):
                        cleaned = f"{self.clean_marker}\n\n{cleaned}"
                    
                    # Validate the cleaned content
                    is_valid, error_msg = self._validate_cleaned_content(original_content, cleaned)
                    if not is_valid:
                        logger.warning(f"Validation failed for {path.name}: {error_msg}")
                        
                        if attempt < max_retries - 1:
                            # Retry with additional guidance
                            user_prompt += f"\n\nIMPORTANT: {error_msg}. Please correct this issue."
                            await asyncio.sleep(2 ** attempt)  # Exponential backoff
                            continue
                    
                    return cleaned
                    
                except Exception as e:
                    logger.error(f"Error processing {path.name}: {e}")
                    if attempt < max_retries - 1:
                        await asyncio.sleep(2 ** attempt)
                    else:
                        return None
        
        return None
    
    async def _process_file(self, path: Path, semaphore: asyncio.Semaphore) -> str:
        """Process a single file."""
        try:
            # Read file content
            content = path.read_text(encoding='utf-8', errors='ignore')
            
            # Check if already clean
            if self.clean_marker in content:
                self.state.skipped.append(str(path))
                return 'skipped'
            
            # Clean with LLM
            cleaned = await self._clean_with_llm(path, content, semaphore)
            
            if cleaned:
                # Calculate checksums for tracking
                original_hash = hashlib.sha256(content.encode()).hexdigest()[:8]
                
                # Add provenance comment if not present
                if "<!-- Cleaned by" not in cleaned:
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
                    cleaned = cleaned.replace(
                        f"{self.clean_marker}",
                        f"{self.clean_marker}\n<!-- Cleaned by batch script {timestamp} | Original: {original_hash} -->"
                    )
                
                # Write back to file
                path.write_text(cleaned, encoding='utf-8')
                
                # Update state
                self.state.cleaned.append(str(path))
                self.state.processed[str(path)] = {
                    'status': 'cleaned',
                    'timestamp': datetime.now().isoformat(),
                    'original_hash': original_hash
                }
                self._save_state()
                
                logger.info(f"[OK] Cleaned: {path.name}")
                return 'cleaned'
            else:
                # Failed to clean
                self.state.failed.append(str(path))
                self.state.processed[str(path)] = {
                    'status': 'failed',
                    'timestamp': datetime.now().isoformat()
                }
                self._save_state()
                
                logger.error(f"[FAIL] Failed: {path.name}")
                return 'failed'
                
        except Exception as e:
            logger.error(f"Unexpected error processing {path}: {e}")
            self.state.failed.append(str(path))
            return 'failed'
    
    async def clean_all(self, force: bool = False) -> Dict[str, int]:
        """Clean all markdown files in the source directory."""
        # Reset state if forcing
        if force:
            self.state = CleaningState()
            logger.info("Force mode: resetting state")
        
        # Find all markdown files
        all_files = list(self.src_dir.glob('*.md'))
        logger.info(f"Found {len(all_files)} markdown files")
        
        # Filter files to process
        files_to_process = []
        for path in all_files:
            if self._should_process_file(path):
                files_to_process.append(path)
            else:
                # Check if already has clean marker
                try:
                    content = path.read_text(encoding='utf-8', errors='ignore')
                    if self.clean_marker in content:
                        if str(path) not in self.state.skipped:
                            self.state.skipped.append(str(path))
                except Exception:
                    pass
        
        logger.info(f"Processing {len(files_to_process)} files (skipping {len(all_files) - len(files_to_process)} already clean/processed)")
        
        if not files_to_process:
            logger.info("No files to process!")
            return {
                'total': len(all_files),
                'skipped': len(self.state.skipped),
                'cleaned': len(self.state.cleaned),
                'failed': len(self.state.failed)
            }
        
        # Process files with concurrency control
        semaphore = asyncio.Semaphore(self.max_concurrency)
        tasks = [
            self._process_file(path, semaphore)
            for path in files_to_process
        ]
        
        # Process with progress tracking
        results = []
        for i, task in enumerate(asyncio.as_completed(tasks)):
            result = await task
            results.append(result)
            if (i + 1) % 10 == 0:
                logger.info(f"Progress: {i + 1}/{len(tasks)} files processed")
        
        # Generate summary
        summary = {
            'total': len(all_files),
            'processed': len(files_to_process),
            'skipped': results.count('skipped') + (len(all_files) - len(files_to_process)),
            'cleaned': results.count('cleaned'),
            'failed': results.count('failed')
        }
        
        return summary


@lru_cache()
def _read_first_line(path: Path) -> Optional[str]:
    try:
        if path.exists():
            line = path.read_text(encoding='utf-8', errors='ignore').strip().splitlines()[0].strip()
            return line or None
    except Exception:
        pass
    return None


async def main():
    """Main entry point."""
    # Parse command line arguments (no defaults so we can resolve hierarchy uniformly)
    parser = argparse.ArgumentParser(description='Batch clean API documentation using LiteLLM')
    parser.add_argument('--api-key', help='API key for LLM service (arg > env > .api_key)')
    parser.add_argument('--base-url', help='Base URL for LLM service (arg > env > .api_base_url)')
    parser.add_argument('--model', help='Model name (arg > env > .api_model_name > gpt-5)')
    parser.add_argument('--src-dir', type=Path, default=Path('casey-docs/markdown'), 
                        help='Source directory with markdown files')
    parser.add_argument('--state-path', type=Path, default=Path('tmp/cleanup/clean_state.json'),
                        help='Path to state file for resumability')
    parser.add_argument('--guide-path', type=Path, default=Path('context/hints/howto-clean-api-documentation.md'),
                        help='Path to cleaning guide')
    parser.add_argument('--max-concurrency', type=int, default=3, 
                        help='Maximum concurrent requests (default: 3)')
    parser.add_argument('--no-guide', action='store_true', 
                        help='Do not include formatting guide in prompts')
    
    args = parser.parse_args()

    # Hierarchical resolution helpers
    cleanup_dir = Path(__file__).resolve().parent
    api_key = (
        args.api_key
        or os.getenv('CUSTOM_LLM_API_KEY')
        or _read_first_line(cleanup_dir / '.api_key')
    )
    if not api_key:
        logger.error("No API key resolved. Provide --api-key, set CUSTOM_LLM_API_KEY, or create tools/cleanup/.api_key")
        return

    base_url = (
        args.base_url
        or os.getenv('CUSTOM_LLM_BASE_URL')
        or _read_first_line(cleanup_dir / '.api_base_url')
    )

    model = (
        args.model
        or os.getenv('CUSTOM_LLM_MODEL')
        or _read_first_line(cleanup_dir / '.api_model_name')
        or 'gpt-5'
    )
    
    # Check for LiteLLM
    try:
        import litellm
        try:
            ver = getattr(litellm, '__version__', 'unknown')
        except Exception:
            ver = 'unknown'
        logger.info(f"LiteLLM version: {ver}")
    except ImportError:
        logger.error("LiteLLM not installed. Please run: pixi add litellm")
        return
    
    # Log configuration
    logger.info("Configuration:")
    logger.info(f"  Model: {model}")
    logger.info(f"  Base URL: {base_url or 'default'}")
    logger.info(f"  Source: {args.src_dir}")
    logger.info(f"  State: {args.state_path}")
    logger.info(f"  Max Concurrency: {args.max_concurrency}")
    
    # Create cleaner and run
    cleaner = DocumentCleaner(
        src_dir=args.src_dir,
        state_path=args.state_path,
        api_key=api_key,
        base_url=base_url,
        model=model,
        guide_path=args.guide_path,
        max_concurrency=args.max_concurrency,
        include_guide=not args.no_guide
    )
    
    # Run cleaning
    start_time = time.time()
    summary = await cleaner.clean_all()
    elapsed = time.time() - start_time
    
    # Print summary
    print("\n" + "="*50)
    print("CLEANING SUMMARY")
    print("="*50)
    print(f"Total files:    {summary['total']}")
    print(f"Already clean:  {summary['skipped']}")
    print(f"Cleaned:        {summary['cleaned']}")
    print(f"Failed:         {summary['failed']}")
    print(f"Time elapsed:   {elapsed:.1f} seconds")
    print("="*50)
    
    # Save final state
    cleaner._save_state()
    
    if summary['failed'] > 0:
        print(f"\n[!] {summary['failed']} files failed to clean. Check logs for details.")
        print(f"    Failed files saved in state file: {args.state_path}")


if __name__ == '__main__':
    # Run the async main function
    asyncio.run(main())