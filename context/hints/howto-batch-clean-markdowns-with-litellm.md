# How to Batch-Clean API Markdown Docs with LiteLLM

This guide shows how to automatically rewrite ("clean") the API markdown files that do **not** yet contain the marker `[CLEAN]`, using your **OpenAI‑compatible** LLM endpoint through **LiteLLM**.

## Goal
Transform each raw `casey-docs/markdown/*.md` file into the standardized format defined in `howto-clean-api-documentation.md`, then save it back (in‑place) with improved structure and add a marker (e.g. `<!-- [CLEAN] -->`) so it is skipped in future runs.

## When to Process a File
Process a file if **all** are true:
- Filename ends with `.md`
- File content does **not** contain the literal string `[CLEAN]`
- File is not empty

## Recommended Marker
Add at the very top (after any initial comment block if you choose) to mark completion:
```markdown
<!-- [CLEAN] -->
```
(You may also append a short provenance note like: `<!-- Cleaned by script YYYY-MM-DD -->`.)

## Environment Setup
Install LiteLLM:
```bash
pip install litellm
```
Set environment variables for your OpenAI‑compatible service (choose names that fit your infra):
- `CUSTOM_LLM_API_KEY` – your API key
- `CUSTOM_LLM_BASE_URL` – base URL (no trailing slash) such as `https://llm.mycompany.com/v1`
- `CUSTOM_LLM_MODEL` – model identifier your endpoint expects (e.g. `gpt-4o`, `claude-opus-4-20250514`, `my-hosted/llama-3-70b`)

Example (PowerShell):
```powershell
$env:CUSTOM_LLM_API_KEY = "sk-..."
$env:CUSTOM_LLM_BASE_URL = "https://llm.mycompany.com/v1"
$env:CUSTOM_LLM_MODEL = "gpt-4o"
```

## Prompt Design
Use **system** + **user** messages. Keep instructions crisp; *never* let the model hallucinate missing methods—if unsure, it must preserve content.

### System Message (Example)
```
You are a precise documentation cleaning assistant.
Rewrite the provided raw API markdown into the standardized format.
Rules:
1. Preserve all factual API elements (class names, method names, signatures, parameters, return info).
2. Do not invent or remove APIs.
3. Convert to the target structure sections: Title, Module/Source block, Overview, Class Definition, Constructor, Methods, Usage Notes.
4. Each method: signature line in code tick format + short description + Parameters/Returns (omit section if truly none) + minimal example when meaningful.
5. Add the marker <!-- [CLEAN] --> at top.
6. Output ONLY valid Markdown starting with '# '.
7. If input already appears clean (has marker), echo it unchanged.
8. If input is too malformed to safely parse, return a conservative cleaned version with all original textual method fragments preserved verbatim.
```

### User Message Template
```
<ORIGINAL_PATH>{path}</ORIGINAL_PATH>
<ORIGINAL_MARKDOWN>
{original_markdown_truncated_if_needed}
</ORIGINAL_MARKDOWN>
Provide cleaned markdown now.
```
(Truncate very large originals to stay within token limits; then append a `... [TRUNCATED: N BYTES REMOVED]` notice *inside* `<ORIGINAL_MARKDOWN>` so you can re‑run in a second pass if desired.)

## LiteLLM Usage Patterns (Validated Against Official Docs)
LiteLLM exposes a unified interface via `completion` / `acompletion` (see official parameter list: `api_base`, `num_retries`, `stream`, etc.).

Key points validated from docs:
1. `api_base` (optional) lets you point directly at a custom OpenAI‑compatible server.
2. If the target is an OpenAI **compatible** endpoint (not the official OpenAI domain) you should usually prefix the model with `openai/` so LiteLLM routes it through the OpenAI adapter (cf. embedding + image generation examples). Example: `model="openai/gpt-4o"`.
3. For official OpenAI you can simply use `model="gpt-4o"` and rely on `OPENAI_API_KEY`.
4. Built‑in retry: prefer `num_retries` over fully manual loops for transient failures; keep custom backoff only for advanced validation retry logic.
5. Streaming: set `stream=True`; each chunk matches OpenAI streaming `chat.completion.chunk` schema (see docs JSON example). Accumulate `chunk['choices'][0]['delta']['content']`.

Minimal non‑stream call:
```python
from litellm import completion
response = completion(
    model="openai/gpt-4o",              # prefix for custom OpenAI-compatible base
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_payload}
    ],
    api_base=base_url,                   # e.g. https://llm.mycompany.com/v1
    api_key=api_key,
    temperature=0.2,
    max_tokens=4096,
    num_retries=2,                       # LiteLLM-managed retry
    timeout=90,
)
clean_md = response["choices"][0]["message"]["content"].strip()
```

Async variant:
```python
from litellm import acompletion
resp = await acompletion(
    model="openai/gpt-4o",
    messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": user_payload}],
    api_base=base_url,
    api_key=api_key,
    temperature=0.2,
    max_tokens=4096,
    num_retries=2,
    timeout=120,
)
```

Streaming accumulation:
```python
parts = []
for chunk in completion(
    model="openai/gpt-4o",
    messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": user_payload}],
    api_base=base_url,
    api_key=api_key,
    stream=True,
    temperature=0.2,
    max_tokens=4096,
):
    delta = chunk['choices'][0]['delta'].get('content')
    if delta:
        parts.append(delta)
clean_md = ''.join(parts).strip()
```

Note: Some providers (Azure, Anthropic, etc.) require other env vars; for this workflow you only need the OpenAI‑compatible endpoint + key.

## Validation Steps (Post‑Generation)
1. Ensure output starts with `<!-- [CLEAN] -->` (add if model forgot).
2. Ensure first Markdown heading begins with `#`.
3. Optionally verify all method names appearing in original also appear in cleaned version (simple substring checks / regex).
4. Reject outputs containing obvious hallucination cues (e.g. `TODO`, `Placeholder`, `This method might`). If found, retry with a stricter follow‑up prompt.
5. Preserve original file on parsing failure (write to `.failed/` for manual inspection).

## Idempotency
On re‑runs, skip files containing `[CLEAN]`. Optionally support `--force` flag to reprocess.

## Rate Limiting / Backoff
Implement exponential backoff (e.g. 1s, 2s, 4s, max 30s) for transient HTTP status codes (429, 500, 502, 503, 504). Cap retries (e.g. 5 attempts). Log failures.

## Concurrency Guidance
- Start with a small parallelism (e.g. 3–5) to avoid upstream throttling.
- Use a semaphore in async code.
- Persist partial progress to a JSON state file so interrupted runs resume.

## Example Script (Simplified)
```python
import os, re, json, asyncio, time, pathlib
from litellm import acompletion

SRC_DIR = pathlib.Path('casey-docs/markdown')
STATE_PATH = pathlib.Path('tmp/clean_state.json')
GUIDE_PATH = pathlib.Path('context/hints/howto-batch-clean-markdowns-with-litellm.md')  # include this guide
MODEL = os.getenv('CUSTOM_LLM_MODEL', 'gpt-4o')
BASE_URL = os.getenv('CUSTOM_LLM_BASE_URL')
API_KEY = os.getenv('CUSTOM_LLM_API_KEY')
MAX_INPUT_CHARS = 40_000
SEM_LIMIT = int(os.getenv('CLEANER_MAX_CONCURRENCY', '5'))
INCLUDE_GUIDE = os.getenv('CLEANER_INCLUDE_GUIDE', '1') == '1'

RAW_SYSTEM_CORE = (
    "You are a precise documentation cleaning assistant. Follow all rules exactly."
)

def load_state():
    if STATE_PATH.exists():
        return json.loads(STATE_PATH.read_text())
    return {}

def save_state(state):
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(json.dumps(state, indent=2))

def build_system_prompt():
    if not INCLUDE_GUIDE or not GUIDE_PATH.exists():
        return RAW_SYSTEM_CORE
    guide_text = GUIDE_PATH.read_text(encoding='utf-8', errors='ignore')
    # Trim to avoid token overflow
    max_chars = 25_000
    if len(guide_text) > max_chars:
        guide_text = guide_text[:max_chars] + f"\n... [GUIDE TRUNCATED {len(guide_text)-max_chars} CHARS]"
    return (
        RAW_SYSTEM_CORE
        + "\nThe following guide defines formatting rules. Obey it.\n<GUIDE>\n"
        + guide_text
        + "\n</GUIDE>"
    )

async def clean_file(path, sem, state):
    text = path.read_text(encoding='utf-8', errors='ignore')
    if '[CLEAN]' in text:
        return 'skipped'
    original = text
    truncated = False
    if len(original) > MAX_INPUT_CHARS:
        original = original[:MAX_INPUT_CHARS] + f"\n... [TRUNCATED: {len(text)-MAX_INPUT_CHARS} BYTES REMOVED]"
        truncated = True
    user_payload = (
        f"<ORIGINAL_PATH>{path}</ORIGINAL_PATH>\n<ORIGINAL_MARKDOWN>\n{original}\n"\
        "</ORIGINAL_MARKDOWN>\nProvide cleaned markdown now."
    )
    system_prompt = build_system_prompt()

    async with sem:
        for attempt in range(5):  # manual loop kept for validation-driven retries beyond num_retries
            try:
                resp = await acompletion(
                    model=MODEL,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_payload},
                    ],
                    api_base=BASE_URL,
                    api_key=API_KEY,
                    temperature=0.2,
                    max_tokens=4096,
                    num_retries=2,  # built-in LiteLLM retry (transient errors)
                    timeout=120,
                )
                content = resp['choices'][0]['message']['content'].strip()
                if not content.startswith('<!-- [CLEAN] -->'):
                    content = '<!-- [CLEAN] -->\n' + content
                # Simple validation
                orig_methods = set(re.findall(r'\b([A-Za-z_][A-Za-z0-9_]*)\s*\(', text))
                missing = [m for m in orig_methods if m not in content]
                if missing and len(missing) > 0 and len(orig_methods) < 200:
                    if attempt < 4:  # Retry with reminder
                        reminder = (
                            f"The previous output omitted: {missing[:15]}. Include them without inventing details."
                        )
                        user_payload += f"\n\nREMINDER: {reminder}"
                        continue
                path.write_text(content, encoding='utf-8')
                state[str(path)] = {'status': 'cleaned', 'truncated': truncated}
                save_state(state)
                return 'cleaned'
            except Exception as e:  # noqa: F841 (placeholder for logging)
                wait = min(30, 2 ** attempt)
                time.sleep(wait)  # exponential backoff after LiteLLM's internal retries
        state[str(path)] = {'status': 'failed'}
        save_state(state)
        return 'failed'

async def main():
    state = load_state()
    sem = asyncio.Semaphore(SEM_LIMIT)
    targets = [p for p in SRC_DIR.glob('*.md') if '[CLEAN]' not in p.read_text(errors='ignore')]
    tasks = [asyncio.create_task(clean_file(p, sem, state)) for p in targets]
    results = await asyncio.gather(*tasks)
    summary = {k: results.count(k) for k in set(results)}
    print('Summary:', summary)

if __name__ == '__main__':
    asyncio.run(main())
```

### Presenting This Guide to the LLM
Set `CLEANER_INCLUDE_GUIDE=1` (default) to automatically inject the full (possibly truncated) content of `howto-batch-clean-markdowns-with-litellm.md` inside `<GUIDE>` tags within the **system** message. This ensures every call has consistent formatting instructions. To reduce token usage for later incremental runs, set `CLEANER_INCLUDE_GUIDE=0`.

You can further slim the injected text by maintaining a separate condensed rule file (e.g. `context/hints/rules-clean-short.md`) and pointing `GUIDE_PATH` to it.

## Streaming (Optional)
If you prefer to stream tokens (useful for very large rewrites), set `stream=True` and accumulate parts:
```python
from litellm import completion
parts = []
for chunk in completion(..., stream=True):
    delta = chunk['choices'][0]['delta'].get('content')
    if delta: parts.append(delta)
full = ''.join(parts)
```

## Safety & Quality Tips
- Keep temperature low (<=0.3) for deterministic restructuring.
- Log each original + cleaned pair (optionally in a `diffs/` directory) for auditing.
- Run a dry-run mode that *only* validates the model output without overwriting.
- Consider checksum tagging: store original SHA256 in a hidden comment to detect upstream changes.

## Retry Enhancement Example
Add a short *feedback* prompt when validation fails (missing methods or hallucinations) instead of blind retry.

## Cost Awareness
Estimate tokens: `(len(original_chars)/4) * 2` (request + response). Multiply by number of files to budget.

## Next Improvements
- Parallel second pass for truncated files.
- HTML artifact detection (e.g. stray `<nav>` / `<footer>`) cleanup *before* sending to LLM to reduce tokens.
- Unit tests for validator functions.

## Source References
- Internal guide: `howto-clean-api-documentation.md`
- LiteLLM Docs (OpenAI-Compatible): https://docs.litellm.ai/docs/providers/openai_compatible
- LiteLLM GitHub: https://github.com/BerriAI/litellm

---
Use this pattern to safely and repeatedly clean the entire documentation set with minimal manual intervention.
