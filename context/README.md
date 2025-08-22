# Context Directory

This directory contains all the context, documentation, and reference materials needed for effective AI collaboration on the Cascadeur Python Client project.

## Directory Structure

```
context/
├── design/          # Technical specifications and architecture
├── hints/           # How-to guides and troubleshooting tips
├── instructions/    # Reusable prompt snippets and commands
├── logs/            # Development session records and outcomes
├── plans/           # Implementation roadmaps and strategies
├── refcode/         # Reference implementations and examples
├── roles/           # Role-based system prompts and memory
├── summaries/       # Knowledge base and analysis documents
├── tasks/           # Current and planned work items
│   ├── features/    # Feature implementation tasks
│   ├── fixes/       # Bug fix tasks
│   ├── refactor/    # Code refactoring tasks
│   └── tests/       # Testing-related tasks
└── tools/           # Custom development utilities
```

## Usage Guidelines

1. **Document as you develop** - Add new context documents during development sessions
2. **Use consistent naming** - Follow the naming patterns defined in each subdirectory
3. **Include HEADER sections** - Every document should start with metadata headers
4. **Keep content current** - Update or remove outdated information regularly
5. **Reference from CLAUDE.md** - AI assistants are directed here for project context

## Quick Start

- For architectural decisions, see `design/`
- For common issues and solutions, check `hints/`
- For current work items, browse `tasks/`
- For development history, review `logs/`

## Project-Specific Context

This context directory is specifically tailored for the Cascadeur Python Client project, which provides a pythonic interface to the Cascadeur animation software. Key areas of focus include:

- Client-server architecture with JSON-RPC communication
- Multiple server implementations (async, threaded, sync)
- Base64 encoding for code transmission
- Integration with Cascadeur's Python API