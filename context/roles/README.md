# Roles Directory

## Purpose
Contains role-based system prompts, memory, and context for different AI assistant personas working on the Cascadeur Python Client.

## Structure
Each role gets its own subdirectory containing:
- `system-prompt.md` - Role-specific instructions
- `memory.md` - Accumulated knowledge for the role
- `context.md` - Role-specific context and background

## Available Roles
Create subdirectories for roles such as:
- `python-developer/` - Python implementation expertise
- `api-designer/` - API design and JSON-RPC expertise
- `test-engineer/` - Testing and quality assurance
- `documentation-writer/` - Documentation and examples
- `performance-engineer/` - Optimization and benchmarking

## Naming Convention
- `[role-name]/system-prompt.md` - Core role definition
- `[role-name]/memory.md` - Role-specific knowledge base
- `[role-name]/context.md` - Background and context

## Usage
AI assistants can be assigned specific roles to provide specialized expertise in different areas of the project.