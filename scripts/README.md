---
icon: python
---

# Scripts Directory

This directory contains utility scripts for managing the Literary Vault repository.

## Available Scripts

### 1. Changelog Management (cl)

A streamlined tool for maintaining the project's CHANGELOG.md file with automatic semantic versioning.

#### Quick Usage

```bash
# Add new entry
./cl add <type> "<description>" [version_bump]

# Create new release
./cl release [version_bump]
```

#### Change Types

Short codes are supported for convenience:

* `a` or `added` - Added
* `c` or `changed` - Changed
* `d` or `dep` - Deprecated
* `r` or `removed` - Removed
* `f` or `fixed` - Fixed
* `s` or `sec` - Security

#### Version Bump Options

* `major` - Breaking changes (1.0.0)
* `minor` - New features (0.1.0)
* `patch` - Bug fixes (0.0.1) [default]

#### Examples

```bash
# Add new feature (minor version bump)
./cl add a "New analysis template" minor

# Fix a bug (patch version bump)
./cl add f "Fixed formatting issue" patch

# Create new release with major version bump
./cl release major

# Quick add with default patch bump
./cl add a "Added new documentation"
```

### 2. Changelog Update Script (update_changelog.py)

Python script for programmatic changelog management with API integration.

```bash
# Add new changelog entry
python update_changelog.py add <type> "description"

# Create new release
python update_changelog.py release <version>
```

Features:
* JSON schema validation
* API integration for automated updates
* Semantic versioning support
* Markdown formatting
* Git integration

### 3. API Integration Scripts

#### Questions API (questions_api.py)
REST API for managing and serving questions from various categories:
* Astronomy
* Literature
* Mathematics
* General Knowledge

Features:
* Question retrieval by category
* Random question selection
* Customizable result limits
* Input validation
* Error handling
* OpenAPI documentation

#### Changelog API (changelog_api.py)
API for programmatic changelog management:
* Add changelog entries
* Create releases
* Query changelog history
* Validate entry formats

## Requirements

* Python 3.x
* FastAPI (for API servers)
* Pydantic (for data validation)
* uvicorn (ASGI server)
* Additional requirements in requirements.txt

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Scripts are automatically executable from the scripts directory:
```bash
cd scripts
./cl add a "New feature"
```

3. Start API servers:
```bash
# Questions API
python questions_api.py

# Changelog API
python changelog_api.py
```

## Features

* Automatic semantic versioning
* JSON schema validation
* API integration
* Markdown formatting
* Git integration
* Error handling
* Documentation generation
* Type safety
* Caching support

## Development

* Follow PEP 8 style guide
* Add type hints
* Update tests when adding features
* Document new functionality
* Validate against schemas
* Handle errors appropriately

## Documentation

* API documentation available at:
  - Questions API: http://localhost:8000/docs
  - Changelog API: http://localhost:8001/docs
* JSON schemas in docs/openai-functions/
* Integration guides in docs/Integration/
