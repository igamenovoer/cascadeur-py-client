# About LiteLLM Proxy for Local Endpoints with Different Formats

This guide covers how to use LiteLLM proxy to set up local endpoints that support different API formats, with special focus on `gemini-cli` integration and environment variable configuration.

## Overview

LiteLLM proxy can simultaneously expose multiple endpoint formats:
- **OpenAI format** (default): `http://localhost:4000/v1/chat/completions`
- **Gemini format**: `http://localhost:4000/gemini/v1beta/models/{model}:generateContent`
- **Anthropic format**: `http://localhost:4000/anthropic/v1/messages`
- **Vertex AI format**: `http://localhost:4000/vertex_ai/v1/...`

## Basic Configuration with Environment Variables

### 1. Environment Variables Setup

Create a `.env` file to store sensitive information:

```env
# Remote endpoints
OPENAI_API_KEY=sk-your-openai-key
ANTHROPIC_API_KEY=sk-ant-your-anthropic-key
GEMINI_API_KEY=your-gemini-api-key

# LiteLLM proxy settings
LITELLM_MASTER_KEY=sk-your-litellm-master-key

# Optional: Custom endpoints
CUSTOM_API_BASE=https://your-custom-endpoint.com/v1
CUSTOM_API_KEY=your-custom-key
```

### 2. Basic LiteLLM Configuration (`config.yaml`)

```yaml
model_list:
  # OpenAI models
  - model_name: gpt-4
    litellm_params:
      model: gpt-4
      api_key: os.environ/OPENAI_API_KEY

  # Anthropic models
  - model_name: claude-3-sonnet
    litellm_params:
      model: anthropic/claude-3-sonnet-20240229
      api_key: os.environ/ANTHROPIC_API_KEY

  # Gemini models
  - model_name: gemini-1.5-pro
    litellm_params:
      model: gemini/gemini-1.5-pro
      api_key: os.environ/GEMINI_API_KEY

  # Custom OpenAI-compatible endpoint
  - model_name: custom-model
    litellm_params:
      model: openai/custom-model-name
      api_base: os.environ/CUSTOM_API_BASE
      api_key: os.environ/CUSTOM_API_KEY

# Proxy settings
litellm_settings:
  master_key: os.environ/LITELLM_MASTER_KEY
```

## Gemini CLI Integration

### 3. Configuration for Gemini CLI Support

To use `gemini-cli` with LiteLLM proxy, you need to configure model aliases that map Gemini model names to your actual models:

```yaml
model_list:
  # Define your actual models
  - model_name: claude-sonnet-proxy
    litellm_params:
      model: anthropic/claude-3-sonnet-20240229
      api_key: os.environ/ANTHROPIC_API_KEY

  - model_name: gpt-4-proxy
    litellm_params:
      model: gpt-4
      api_key: os.environ/OPENAI_API_KEY

  - model_name: custom-llm-proxy
    litellm_params:
      model: openai/your-model
      api_base: os.environ/CUSTOM_API_BASE
      api_key: os.environ/CUSTOM_API_KEY

# Router settings for gemini-cli compatibility
router_settings:
  model_group_alias:
    # Map gemini-cli model names to your actual models
    "gemini-2.5-pro": "claude-sonnet-proxy"
    "gemini-2.0-flash": "gpt-4-proxy"
    "gemini-1.5-pro": "custom-llm-proxy"

litellm_settings:
  master_key: os.environ/LITELLM_MASTER_KEY
```

### 4. Start LiteLLM Proxy

```bash
# Load environment variables and start proxy
litellm --config config.yaml --port 4000 --host 0.0.0.0
```

### 5. Configure Gemini CLI

Set environment variables (preferred per LiteLLM docs):

```bash
export GOOGLE_GEMINI_BASE_URL="http://localhost:4000"
export GEMINI_API_KEY="sk-your-litellm-master-key"
```

Notes:
- GOOGLE_GEMINI_BASE_URL points to your LiteLLM Proxy base URL.
- The proxy exposes Gemini-compatible endpoints under /gemini; SDKs/CLI construct the correct path.
- Ensure the model alias (e.g., "gemini-2.5-pro") is mapped via router_settings.model_group_alias.

## Advanced Multi-Format Configuration

### 6. Complete Multi-Format Setup

```yaml
model_list:
  # OpenAI models
  - model_name: gpt-4-turbo
    litellm_params:
      model: gpt-4-turbo
      api_key: os.environ/OPENAI_API_KEY

  # Anthropic models  
  - model_name: claude-3-opus
    litellm_params:
      model: anthropic/claude-3-opus-20240229
      api_key: os.environ/ANTHROPIC_API_KEY

  # Vertex AI models
  - model_name: gemini-pro-vertex
    litellm_params:
      model: vertex_ai/gemini-pro
      vertex_project: os.environ/GOOGLE_CLOUD_PROJECT
      vertex_location: os.environ/GOOGLE_CLOUD_LOCATION

  # OpenAI-compatible endpoints
  - model_name: ollama-llama
    litellm_params:
      model: openai/llama3.1:8b
      api_base: os.environ/OLLAMA_API_BASE
      api_key: "ollama"

# Advanced routing for different formats
router_settings:

  # Model aliases for gemini-cli
  model_group_alias:
    "gemini-2.5-pro": "claude-3-opus"
    "gemini-2.0-flash": "gpt-4-turbo"
    "gemini-1.5-pro": "gemini-pro-vertex"
    "gemini-pro": "ollama-llama"

  # Load balancing and fallbacks
  routing_strategy: "round-robin"
  fallbacks:
    - "claude-3-opus": ["gpt-4-turbo", "gemini-pro-vertex"]
    - "gpt-4-turbo": ["claude-3-opus"]

litellm_settings:
  master_key: os.environ/LITELLM_MASTER_KEY
  
  # Format compatibility
  anthropic_compatible: true
  vertex_compatible: true
  openai_compatible: true
  
  # Optional: Enable admin UI
  ui: true
```

### 7. Environment Variables for Advanced Setup

```env
# API Keys
OPENAI_API_KEY=sk-your-openai-key
ANTHROPIC_API_KEY=sk-ant-your-anthropic-key
GEMINI_API_KEY=your-gemini-api-key

# Google Cloud for Vertex AI
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=us-central1
GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account.json

# Custom endpoints
OLLAMA_API_BASE=http://localhost:11434/v1
CUSTOM_API_BASE=https://your-endpoint.com/v1
CUSTOM_API_KEY=your-custom-key

# LiteLLM settings
LITELLM_MASTER_KEY=sk-your-secure-master-key

# Optional: Redis for caching
REDIS_URL=redis://localhost:6379
```

## Usage Examples

### 8. Using Different Endpoints

```bash
# OpenAI format (default)
curl http://localhost:4000/v1/chat/completions \
  -H "Authorization: Bearer sk-your-litellm-master-key" \
  -d '{"model": "gpt-4-turbo", "messages": [{"role": "user", "content": "Hello"}]}'

# Gemini format (for gemini-cli)
curl http://localhost:4000/gemini/v1beta/models/gemini-2.5-pro:generateContent \
  -H "Authorization: Bearer sk-your-litellm-master-key" \
  -H "Content-Type: application/json" \
  -d '{"contents": [{"parts": [{"text": "Hello"}]}]}'

# Anthropic format
curl http://localhost:4000/anthropic/v1/messages \
  -H "Authorization: Bearer sk-your-litellm-master-key" \
  -d '{"model": "claude-3-opus", "messages": [{"role": "user", "content": "Hello"}], "max_tokens": 100}'
```

### 9. Python Client Examples

```python
import openai
import os

# Load environment variables
litellm_key = os.environ['LITELLM_MASTER_KEY']

# OpenAI format client
openai_client = openai.OpenAI(
    api_key=litellm_key,
    base_url="http://localhost:4000"
)

# Use any configured model via OpenAI format
response = openai_client.chat.completions.create(
    model="gpt-4-turbo",  # Will route to actual OpenAI
    messages=[{"role": "user", "content": "Hello"}]
)

# Same client, different model (routes to Anthropic)
response = openai_client.chat.completions.create(
    model="claude-3-opus",  # Will route to Anthropic
    messages=[{"role": "user", "content": "Hello"}]
)
```

## Running LiteLLM Without Database

### 21. Database-Free Configuration

If you don't want to set up a PostgreSQL database, you can configure LiteLLM to run without database features:

```yaml
model_list:
  # Your model configurations
  - model_name: gpt-4
    litellm_params:
      model: gpt-4
      api_key: os.environ/OPENAI_API_KEY

# Database-free settings
general_settings:
  disable_spend_logs: true              # Turn off writing transactions to DB
  disable_adding_master_key_hash_to_db: true  # Turn off storing master key hash in DB
  allow_requests_on_db_unavailable: true      # Allow requests when DB is unavailable
  disable_reset_budget: true                  # Turn off reset budget scheduled task

litellm_settings:
  master_key: os.environ/LITELLM_MASTER_KEY
  ui: true                              # Admin UI still works with limited features
  openai_compatible: true
  anthropic_compatible: true
  vertex_compatible: true

### 21a. Strict / No-DB (Suppress Warnings) Configuration

If you want LiteLLM to start with zero attempts to touch a database (no schema update, no UI calls, minimal warnings), use this stricter variant:

```yaml
model_list:
  - model_name: gpt-4
    litellm_params:
      model: gpt-4
      api_key: os.environ/OPENAI_API_KEY

# Keep only protocol / format options here
litellm_settings:
  ui: false                  # Avoids admin UI DB code paths
  openai_compatible: true
  anthropic_compatible: true
  vertex_compatible: true

# Put master_key + all DB disabling flags together
general_settings:
  master_key: os.environ/LITELLM_MASTER_KEY
  disable_spend_logs: true
  disable_error_logs: true
  disable_adding_master_key_hash_to_db: true
  allow_requests_on_db_unavailable: true
  disable_reset_budget: true
  # Intentionally no database_url / DATABASE_URL

# Optional routing / alias config can follow
router_settings:
  enable_anthropic_endpoint: true
  enable_vertex_endpoint: true
  enable_gemini_endpoint: true
```

Recommended environment variables (PowerShell shown; Bash just use `export`):

```powershell
$env:LITELLM_MASTER_KEY = "sk-your-master-key"
$env:OPENAI_API_KEY = "sk-your-openai-key"
# Hard-disable schema migrations / admin endpoints if you won't use them
$env:DISABLE_SCHEMA_UPDATE = "true"          # Skip prisma schema update attempts
$env:DISABLE_ADMIN_UI = "true"               # Redundant if ui:false, extra safety
$env:DISABLE_ADMIN_ENDPOINTS = "true"        # Hides /key, /team, /user (they need DB)
# DO NOT set DISABLE_LLM_API_ENDPOINTS unless you want to turn off model routes
```

Startup example:

```powershell
litellm --config config.yaml --port 4000 --host 0.0.0.0
```

Key differences vs Section 21:
* Moves `master_key` into `general_settings` (avoids hashing step when that feature is disabled).
* Adds `disable_error_logs: true` so no error log writes are attempted.
* Turns off UI entirely to skip any DB-backed pages.
* Adds environment flags to prevent schema updates and admin endpoint registration.
* Provides explicit note not to set `DATABASE_URL`.

What you still get: full routing, multi-format endpoints, streaming, caching (if you enable Redis separately). What you lose: virtual key generation, spend/budget analytics, per-team controls.

If you later introduce a DB, simply: (1) remove the disable_* flags you want to re-enable, (2) set `DATABASE_URL`, (3) set `ui: true` (optional), (4) remove `DISABLE_SCHEMA_UPDATE` so migrations run.
```

### 22. Environment Variables for Database-Free Setup

```env
# Required for basic operation
LITELLM_MASTER_KEY=sk-your-secure-master-key
OPENAI_API_KEY=sk-your-openai-key
ANTHROPIC_API_KEY=sk-ant-your-anthropic-key
GEMINI_API_KEY=your-gemini-api-key

# Note: DATABASE_URL is NOT required when database features are disabled
```

### 23. What Works Without Database

✅ **Fully Functional Features:**
- **Core Proxy Functionality**: Route requests to different LLM providers
- **Model Access**: All configured models remain accessible
- **Multiple API Formats**: OpenAI, Anthropic, Gemini, Vertex AI endpoints
- **Authentication**: Master key authentication still works
- **Request Processing**: Chat completions, embeddings, etc.
- **Load Balancing**: Round-robin and failover routing
- **Caching**: Redis-based caching (if configured)
- **Admin UI**: Basic interface for testing and monitoring
- **Model Aliases**: Gemini CLI integration via model_group_alias
- **Streaming**: Real-time response streaming
- **Custom Parameters**: Temperature, reasoning_effort, etc.

### 24. What Doesn't Work Without Database

❌ **Disabled Features:**
- **Virtual Key Management**: Cannot create/manage API keys through UI or API
- **User Management**: No user accounts, teams, or organizations
- **Spend Tracking**: No logging of usage costs or token consumption
- **Budget Controls**: No rate limiting or budget enforcement per user/key
- **Usage Analytics**: No historical usage data or reporting
- **Key Permissions**: No fine-grained access control per model/endpoint
- **Audit Logs**: No detailed logging of API requests and responses
- **Team Collaboration**: No shared workspaces or team-based access
- **Webhook Integration**: No spend alerts or usage notifications

### 25. Database-Free Startup Commands

```bash
# PowerShell (Windows)
$env:LITELLM_MASTER_KEY="sk-your-master-key"
$env:OPENAI_API_KEY="sk-your-openai-key"
litellm --config config.yaml --port 4000 --host 0.0.0.0

# Bash (Linux/macOS)
export LITELLM_MASTER_KEY="sk-your-master-key"
export OPENAI_API_KEY="sk-your-openai-key"
litellm --config config.yaml --port 4000 --host 0.0.0.0

# Docker without database
docker run -p 4000:4000 \
  -e LITELLM_MASTER_KEY=sk-your-master-key \
  -e OPENAI_API_KEY=sk-your-openai-key \
  -v $(pwd)/config.yaml:/app/config.yaml \
  ghcr.io/berriai/litellm:main-stable \
  --config /app/config.yaml --port 4000 --host 0.0.0.0
```

### 26. Testing Database-Free Setup

```bash
# Verify proxy is running without database
curl http://localhost:4000/health

# Test model access with master key
curl http://localhost:4000/v1/models \
  -H "Authorization: Bearer sk-your-litellm-master-key"

# Test chat completion
curl http://localhost:4000/v1/chat/completions \
  -H "Authorization: Bearer sk-your-litellm-master-key" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4",
    "messages": [{"role": "user", "content": "Hello without database!"}],
    "max_tokens": 100
  }'

# Test Gemini CLI integration (should work normally)
export GOOGLE_GEMINI_BASE_URL="http://localhost:4000"
export GEMINI_API_KEY="sk-your-litellm-master-key"
gemini chat "Test without database"
```

### 27. When to Use Database-Free Mode

**Ideal for:**
- **Development and Testing**: Quick setup for local development
- **Simple Proxy Use Cases**: Just need model routing without user management
- **Personal Projects**: Single-user scenarios where tracking isn't needed
- **Proof of Concepts**: Demonstrating LiteLLM capabilities
- **CI/CD Pipelines**: Automated testing environments
- **Edge Deployments**: Minimal infrastructure requirements

**Not Recommended for:**
- **Production Multi-User Systems**: Need user management and tracking
- **Commercial Applications**: Require spend tracking and billing
- **Team Environments**: Need access control and collaboration features
- **Compliance Requirements**: Need audit logs and usage tracking
- **Rate-Limited APIs**: Need budget controls to prevent overuse

### 28. Migration Considerations

If you later decide you need database features:

```yaml
# Add database configuration to existing setup
general_settings:
  # Remove or set to false
  disable_spend_logs: false
  disable_adding_master_key_hash_to_db: false
  allow_requests_on_db_unavailable: false
  disable_reset_budget: false

# Add database URL
# Note: You'll need to set this in environment variables
# DATABASE_URL=postgresql://user:password@localhost:5432/litellm
```

**Migration Steps:**
1. Set up PostgreSQL database
2. Add `DATABASE_URL` to environment variables
3. Update `general_settings` in config.yaml
4. Restart LiteLLM proxy
5. Create initial admin keys through UI or API

## Troubleshooting

### Common Issues

1. **Environment variables not loaded**: Ensure `.env` file is in the correct location and variables are properly formatted
2. **Model not found**: Check model names in configuration match those used in requests
3. **Authentication errors**: Verify API keys are valid and properly set in environment variables
4. **Gemini CLI connection issues**: Ensure `baseUrl` in gemini settings points to the correct LiteLLM endpoint
5. **Database connection errors**: If seeing database-related errors, ensure database features are properly disabled in config
6. **Missing DATABASE_URL warnings**: Normal when running database-free; can be ignored

### Debugging Commands

```bash
# Test model listing
curl http://localhost:4000/v1/models \
  -H "Authorization: Bearer sk-your-litellm-master-key"

# Check health
curl http://localhost:4000/health

# View logs with debug mode
litellm --config config.yaml --debug

# Test database-free operation
curl -i http://localhost:4000/v1/chat/completions \
  -H "Authorization: Bearer sk-your-litellm-master-key" \
  -d '{"model": "gpt-4", "messages": [{"role": "user", "content": "test"}]}'
```

## Model-Specific Settings

### 10. Advanced Model Parameters

LiteLLM allows you to set model-specific parameters that control behavior on the remote side:

```yaml
model_list:
  # Basic model with standard parameters
  - model_name: claude-basic
    litellm_params:
      model: anthropic/claude-3-sonnet-20240229
      api_key: os.environ/ANTHROPIC_API_KEY
      temperature: 0.7
      max_tokens: 4096
      top_p: 0.9

  # Model with reasoning/thinking parameters
  - model_name: claude-reasoning
    litellm_params:
      model: anthropic/claude-3-7-sonnet-20250219
      api_key: os.environ/ANTHROPIC_API_KEY
      temperature: 0.5
      max_tokens: 8192
      # Enable reasoning capabilities
      supports_reasoning: true
      reasoning_effort: "medium"  # Options: "disable", "low", "medium", "high"

  # Model with prompt caching enabled
  - model_name: claude-cached
    litellm_params:
      model: anthropic/claude-3-5-sonnet-20241022
      api_key: os.environ/ANTHROPIC_API_KEY
      max_tokens: 4096
      # Auto-inject cache control for system messages
      cache_control_injection_points:
        - location: message
          role: system
      # Custom headers for prompt caching
      headers:
        anthropic-beta: "prompt-caching-2024-07-31"

  # Gemini model example
  - model_name: gemini-thinking
    litellm_params:
      model: gemini/gemini-2.5-flash-preview-04-17
      api_key: os.environ/GEMINI_API_KEY
      temperature: 0.8
      max_tokens: 2048
      # Thinking is configured per-request via `thinking` or `reasoning_effort`
  # OpenAI model with custom parameters
  - model_name: gpt-4-custom
    litellm_params:
      model: gpt-4-turbo
      api_key: os.environ/OPENAI_API_KEY
      temperature: 0.3
      max_tokens: 4096
      top_p: 0.95
      frequency_penalty: 0.1
      presence_penalty: 0.1
      # Custom organization (if applicable)
      organization: os.environ/OPENAI_ORG_ID

  # Custom endpoint with verbosity settings
  - model_name: custom-verbose
    litellm_params:
      model: openai/custom-model
      api_base: os.environ/CUSTOM_API_BASE
      api_key: os.environ/CUSTOM_API_KEY
      temperature: 0.6
      max_tokens: 3072
      # Custom parameters passed to remote endpoint
      custom_llm_provider_params:
        verbosity: "high"
        debug_mode: true
        stream_options:
          include_usage: true
```

### 11. Parameter Categories

#### **Temperature and Sampling Parameters**
```yaml
litellm_params:
  temperature: 0.7          # Controls randomness (0.0-2.0)
  top_p: 0.9               # Nucleus sampling
  top_k: 40                # Top-k sampling (provider specific)
  frequency_penalty: 0.1    # Reduce repetition
  presence_penalty: 0.1     # Encourage diversity
```

#### **Reasoning and Thinking Parameters**
```yaml
litellm_params:
  # For Anthropic models
  reasoning_effort: "medium"  # "disable", "low", "medium", "high"
  supports_reasoning: true    # Enable reasoning capabilities
# For Gemini models:
# - Prefer request-level overrides on the OpenAI route:
#     "thinking": {"type": "enabled", "budget_tokens": 1024}
# - Or send "reasoning_effort": "low" (LiteLLM maps to Gemini thinking)
```

#### **Prompt Caching Parameters**
```yaml
litellm_params:
  # Auto-inject cache control
  cache_control_injection_points:
    - location: message      # Where to inject cache control
      role: system          # Which role to target
  
  # Custom headers for caching
  headers:
    anthropic-beta: "prompt-caching-2024-07-31"
    
  # Manual cache control (can be overridden per request)
  cache_control:
    type: "ephemeral"
    ttl: "7200s"            # Cache duration
```

#### **Provider-Specific Parameters**
```yaml
litellm_params:
  # OpenAI specific
  organization: os.environ/OPENAI_ORG_ID
  user: "user-identifier"
  
  # Anthropic specific
  headers:
    anthropic-beta: "prompt-caching-2024-07-31,pdfs-2024-09-25"
  
  # Vertex AI specific
  vertex_project: os.environ/GOOGLE_CLOUD_PROJECT
  vertex_location: os.environ/GOOGLE_CLOUD_LOCATION
  vertex_safety_settings:
    - category: "HARM_CATEGORY_DANGEROUS_CONTENT"
      threshold: "BLOCK_MEDIUM_AND_ABOVE"
  
  # Custom endpoint specific
  custom_llm_provider_params:
    verbosity: "detailed"
    debug_mode: true
    custom_parameter: "value"
```

### 12. Request-Level Parameter Override

You can override model-specific settings at request time:

```bash
# Override temperature and reasoning effort
curl http://localhost:4000/v1/chat/completions \
  -H "Authorization: Bearer sk-your-litellm-master-key" \
  -d '{
    "model": "claude-reasoning",
    "messages": [{"role": "user", "content": "Solve this complex problem"}],
    "temperature": 0.2,
    "reasoning_effort": "high",
    "max_tokens": 6000
  }'

# Enable prompt caching for specific request
curl http://localhost:4000/v1/chat/completions \
  -H "Authorization: Bearer sk-your-litellm-master-key" \
  -d '{
    "model": "claude-cached",
    "messages": [
      {
        "role": "system",
        "content": "You are a helpful assistant...",
        "cache_control": {"type": "ephemeral"}
      },
      {"role": "user", "content": "What is AI?"}
    ]
  }'

# Gemini with thinking parameters (request-level override on OpenAI route)
curl http://localhost:4000/v1/chat/completions \
  -H "Authorization: Bearer sk-your-litellm-master-key" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "vertex_ai/gemini-2.5-flash-preview-04-17",
    "messages": [{"role": "user", "content": "Explain quantum computing"}],
    "thinking": {"type": "enabled", "budget_tokens": 1024},
    "temperature": 0.9
  }'
```

### 13. Environment Variables for Model Parameters

```env
# Model-specific API keys
OPENAI_API_KEY=sk-your-openai-key
ANTHROPIC_API_KEY=sk-ant-your-anthropic-key
GEMINI_API_KEY=your-gemini-api-key

# Organization and project settings
OPENAI_ORG_ID=org-your-organization
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=us-central1

# Custom endpoint configurations
CUSTOM_API_BASE=https://your-endpoint.com/v1
CUSTOM_API_KEY=your-custom-key
CUSTOM_ORG_ID=your-org

# Model behavior defaults
DEFAULT_TEMPERATURE=0.7
DEFAULT_MAX_TOKENS=4096
DEFAULT_REASONING_EFFORT=medium

# Caching settings
ANTHROPIC_BETA_FEATURES=prompt-caching-2024-07-31,pdfs-2024-09-25
CACHE_TTL=7200
```

### 14. Model Information and Capabilities

```yaml
model_list:
  - model_name: claude-full-featured
    litellm_params:
      model: anthropic/claude-3-7-sonnet-20250219
      api_key: os.environ/ANTHROPIC_API_KEY
    # Model metadata and capabilities
    model_info:
      supports_reasoning: true      # Enable reasoning features
      supports_function_calling: true
      supports_vision: true
      supports_prompt_caching: true
      max_tokens: 200000           # Maximum context length
      input_cost_per_token: 0.000003
      output_cost_per_token: 0.000015
      # Custom model tags
      tags:
        - "reasoning"
        - "large-context"
        - "production"

  - model_name: gemini-specialized
    litellm_params:
      model: gemini/gemini-2.5-flash-preview-04-17
      api_key: os.environ/GEMINI_API_KEY
    model_info:
      supports_thinking: true
      supports_multimodal: true
      max_thinking_tokens: 4096
      tags:
        - "thinking"
        - "multimodal"
        - "experimental"
```

### 15. Dynamic Parameter Configuration

```python
# Example: Using model parameters in Python
import openai
import os

client = openai.OpenAI(
    api_key=os.environ['LITELLM_MASTER_KEY'],
    base_url="http://localhost:4000"
)

# Request with reasoning
response = client.chat.completions.create(
    model="claude-reasoning",
    messages=[
        {"role": "user", "content": "Solve this step by step: What is 15% of 240?"}
    ],
    reasoning_effort="high",        # Override model default
    temperature=0.1,               # Override model default
    max_tokens=2000               # Override model default
)

# Access reasoning content (if available)
if hasattr(response.choices[0].message, 'reasoning_content'):
    print("Reasoning:", response.choices[0].message.reasoning_content)
print("Answer:", response.choices[0].message.content)
```

## Testing LiteLLM Endpoints with CLI Tools

### 16. curl Examples

#### **Basic Health Check**
```bash
# Simple health check
curl http://localhost:4000/health

# Health check with timing
curl -w "@curl-format.txt" http://localhost:4000/health

# Verbose health check
curl -v http://localhost:4000/health
```

#### **List Available Models**
```bash
# List all models
curl http://localhost:4000/v1/models \
  -H "Authorization: Bearer sk-your-litellm-master-key"

# Pretty print model list
curl -s http://localhost:4000/v1/models \
  -H "Authorization: Bearer sk-your-litellm-master-key" | jq '.'

# Filter for specific model types
curl -s http://localhost:4000/v1/models \
  -H "Authorization: Bearer sk-your-litellm-master-key" | \
  jq '.data[] | select(.id | contains("claude"))'
```

#### **Test Chat Completions**
```bash
# Basic OpenAI format request
curl http://localhost:4000/v1/chat/completions \
  -H "Authorization: Bearer sk-your-litellm-master-key" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4-turbo",
    "messages": [{"role": "user", "content": "Hello, world!"}],
    "max_tokens": 100
  }'

# Claude model with reasoning
curl http://localhost:4000/v1/chat/completions \
  -H "Authorization: Bearer sk-your-litellm-master-key" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "claude-3-5-sonnet",
    "messages": [{"role": "user", "content": "Explain quantum computing"}],
    "reasoning_effort": "medium",
    "temperature": 0.7,
    "max_tokens": 2000
  }'

# Gemini model with thinking
curl http://localhost:4000/v1/chat/completions \
  -H "Authorization: Bearer sk-your-litellm-master-key" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-2.0-flash-thinking-exp-1219",
    "messages": [{"role": "user", "content": "Solve this step by step: What is 25% of 160?"}],
    "thinking": {"type": "enabled", "budget_tokens": 1024},
    "temperature": 0.5
  }'

# Streaming response
curl http://localhost:4000/v1/chat/completions \
  -H "Authorization: Bearer sk-your-litellm-master-key" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4-turbo",
    "messages": [{"role": "user", "content": "Count from 1 to 10"}],
    "stream": true
  }'
```

#### **Test Gemini Native Format**
```bash
# Gemini generateContent endpoint
curl http://localhost:4000/gemini/v1/models/gemini-2.0-flash-thinking-exp-1219:generateContent \
  -H "Authorization: Bearer sk-your-litellm-master-key" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{
      "parts": [{"text": "Explain the theory of relativity"}]
    }],
    "generationConfig": {
      "temperature": 0.7,
      "maxOutputTokens": 1500
    }
  }'

# Gemini with thinking configuration
curl http://localhost:4000/gemini/v1/models/gemini-2.0-flash-thinking-exp-1219:generateContent \
  -H "Authorization: Bearer sk-your-litellm-master-key" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{
      "parts": [{"text": "What is the square root of 144?"}]
    }],
    "generationConfig": {
      "temperature": 0.3,
      "maxOutputTokens": 1000
    },
    "thinkingConfig": {
      "budgetTokens": 512
    }
  }'

# Gemini streaming
curl http://localhost:4000/gemini/v1/models/gemini-2.0-flash-thinking-exp-1219:streamGenerateContent \
  -H "Authorization: Bearer sk-your-litellm-master-key" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{
      "parts": [{"text": "Tell me a short story"}]
    }],
    "generationConfig": {
      "temperature": 0.8,
      "maxOutputTokens": 800
    }
  }'
```

### 17. HTTPie Examples

HTTPie provides a more user-friendly syntax for testing APIs:

#### **Installation and Basic Usage**
```bash
# Install HTTPie
pip install httpie

# Or using conda
conda install httpie

# Or using pipx
pipx install httpie
```

#### **Health and Model Checks**
```bash
# Health check
http GET localhost:4000/health

# List models with authentication
http GET localhost:4000/v1/models \
  Authorization:"Bearer sk-your-litellm-master-key"

# Pretty print with colors
http --print=HhBb GET localhost:4000/v1/models \
  Authorization:"Bearer sk-your-litellm-master-key"
```

#### **Chat Completions**
```bash
# Basic chat completion
http POST localhost:4000/v1/chat/completions \
  Authorization:"Bearer sk-your-litellm-master-key" \
  model="gpt-4-turbo" \
  messages:='[{"role": "user", "content": "Hello!"}]' \
  max_tokens:=150

# Claude with reasoning
http POST localhost:4000/v1/chat/completions \
  Authorization:"Bearer sk-your-litellm-master-key" \
  model="claude-3-5-sonnet" \
  messages:='[{"role": "user", "content": "Explain machine learning"}]' \
  reasoning_effort="high" \
  temperature:=0.6 \
  max_tokens:=3000

# Gemini with thinking
http POST localhost:4000/v1/chat/completions \
  Authorization:"Bearer sk-your-litellm-master-key" \
  model="gemini-2.0-flash-thinking-exp-1219" \
  messages:='[{"role": "user", "content": "Calculate 15 * 23"}]' \
  thinking:='{"type": "enabled", "budget_tokens": 256}' \
  temperature:=0.2

# Upload file (if multimodal supported)
http --form POST localhost:4000/v1/chat/completions \
  Authorization:"Bearer sk-your-litellm-master-key" \
  model="gpt-4-vision" \
  messages:='[{"role": "user", "content": "Describe this image", "image_url": {"url": "data:image/jpeg;base64,..."}}]'
```

#### **Gemini Native Format with HTTPie**
```bash
# Gemini generateContent
http POST localhost:4000/gemini/v1/models/gemini-2.0-flash-thinking-exp-1219:generateContent \
  Authorization:"Bearer sk-your-litellm-master-key" \
  contents:='[{"parts": [{"text": "What is artificial intelligence?"}]}]' \
  generationConfig:='{"temperature": 0.7, "maxOutputTokens": 2000}'

# Gemini with thinking config
http POST localhost:4000/gemini/v1/models/gemini-2.0-flash-thinking-exp-1219:generateContent \
  Authorization:"Bearer sk-your-litellm-master-key" \
  contents:='[{"parts": [{"text": "Solve: 2x + 5 = 15"}]}]' \
  generationConfig:='{"temperature": 0.3, "maxOutputTokens": 1000}' \
  thinkingConfig:='{"budgetTokens": 512}'
```

### 18. Advanced Testing and Debugging

#### **Performance Testing**
```bash
# Test response time
curl -w "@curl-format.txt" -o /dev/null -s http://localhost:4000/v1/chat/completions \
  -H "Authorization: Bearer sk-your-litellm-master-key" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4-turbo",
    "messages": [{"role": "user", "content": "Hi"}],
    "max_tokens": 50
  }'

# Create curl-format.txt for timing
echo '     time_namelookup:  %{time_namelookup}\n
        time_connect:  %{time_connect}\n
     time_appconnect:  %{time_appconnect}\n
    time_pretransfer:  %{time_pretransfer}\n
       time_redirect:  %{time_redirect}\n
  time_starttransfer:  %{time_starttransfer}\n
                     ----------\n
          time_total:  %{time_total}\n' > curl-format.txt

# Load testing with concurrent requests
for i in {1..10}; do
  curl -s http://localhost:4000/v1/chat/completions \
    -H "Authorization: Bearer sk-your-litellm-master-key" \
    -H "Content-Type: application/json" \
    -d '{"model": "gpt-4-turbo", "messages": [{"role": "user", "content": "Test '${i}'"}]}' &
done
wait
```

#### **Error Testing**
```bash
# Test invalid model
curl http://localhost:4000/v1/chat/completions \
  -H "Authorization: Bearer sk-your-litellm-master-key" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "nonexistent-model",
    "messages": [{"role": "user", "content": "Test"}]
  }'

# Test invalid auth
curl http://localhost:4000/v1/chat/completions \
  -H "Authorization: Bearer invalid-key" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4-turbo",
    "messages": [{"role": "user", "content": "Test"}]
  }'

# Test malformed request
curl http://localhost:4000/v1/chat/completions \
  -H "Authorization: Bearer sk-your-litellm-master-key" \
  -H "Content-Type: application/json" \
  -d '{"invalid": "json"}'
```

#### **Monitoring and Logs**
```bash
# Check LiteLLM proxy status
curl http://localhost:4000/health/stats

# Get detailed health information
curl http://localhost:4000/health/verbose \
  -H "Authorization: Bearer sk-your-litellm-master-key"

# Monitor logs in real-time (if running locally)
# PowerShell
Get-Content "litellm.log" -Wait -Tail 10

# Or if using Docker
docker logs -f litellm-proxy
```

### 19. LiteLLM CLI Testing Commands

#### **Direct LiteLLM CLI Usage**
```bash
# Test configuration file
litellm --test --config litellm-config.yaml

# Debug mode with verbose logging
litellm --config litellm-config.yaml --debug --port 4000

# Test specific model
litellm --model gpt-4-turbo --test

# Check model compatibility
litellm --model anthropic/claude-3-sonnet --provider anthropic --test
```

#### **Environment Testing**
```bash
# Test with environment variables
export LITELLM_MASTER_KEY="sk-your-litellm-master-key"
export OPENAI_API_KEY="sk-your-openai-key"
export ANTHROPIC_API_KEY="sk-ant-your-anthropic-key"

# Verify environment setup
litellm --config litellm-config.yaml --test

# Test individual providers
litellm --provider openai --test
litellm --provider anthropic --test
litellm --provider gemini --test
```

### 20. Troubleshooting with CLI Tools

#### **Common Issues and Solutions**
```bash
# 1. Connection refused
curl -v http://localhost:4000/health
# Solution: Ensure LiteLLM proxy is running

# 2. Authentication errors
curl -I http://localhost:4000/v1/models \
  -H "Authorization: Bearer sk-your-litellm-master-key"
# Solution: Check master key in environment variables

# 3. Model not found
curl -s http://localhost:4000/v1/models | jq '.data[].id'
# Solution: Verify model names in configuration

# 4. Rate limiting
curl -i http://localhost:4000/v1/chat/completions \
  -H "Authorization: Bearer sk-your-litellm-master-key" \
  -d '{"model": "gpt-4-turbo", "messages": [{"role": "user", "content": "test"}]}'
# Check for HTTP 429 status codes

# 5. Timeout issues
curl --max-time 30 http://localhost:4000/v1/chat/completions \
  -H "Authorization: Bearer sk-your-litellm-master-key" \
  -d '{"model": "gpt-4-turbo", "messages": [{"role": "user", "content": "test"}]}'
```

#### **Debug Information Collection**
```bash
# Collect system information
echo "=== System Info ==="
curl -s http://localhost:4000/health | jq '.'

echo "=== Available Models ==="
curl -s http://localhost:4000/v1/models \
  -H "Authorization: Bearer sk-your-litellm-master-key" | jq '.data[].id'

echo "=== Configuration Test ==="
litellm --config litellm-config.yaml --test --debug

echo "=== Environment Variables ==="
env | grep -E "(OPENAI|ANTHROPIC|GEMINI|LITELLM)" | sort
```

## References

- [LiteLLM Gemini CLI Documentation](https://docs.litellm.ai/docs/tutorials/litellm_gemini_cli)
- [LiteLLM Proxy Configuration](https://docs.litellm.ai/docs/proxy/configs)
- [LiteLLM Model-Specific Settings](https://docs.litellm.ai/docs/proxy/config_settings)
- [LiteLLM Reasoning Content](https://docs.litellm.ai/docs/reasoning_content)
- [LiteLLM Prompt Caching](https://docs.litellm.ai/docs/tutorials/prompt_caching)
- [Gemini CLI Official Docs](https://cloud.google.com/gemini/docs/codeassist/gemini-cli)
- [LiteLLM Environment Variables](https://docs.litellm.ai/docs/proxy/configs#environment-variables)
- [HTTPie Documentation](https://httpie.io/docs/cli)
- [curl Documentation](https://curl.se/docs/manpage.html)
- [LiteLLM CLI Testing](https://docs.litellm.ai/docs/proxy/cli)
