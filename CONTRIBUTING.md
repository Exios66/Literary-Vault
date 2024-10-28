---
icon: github
---

# Contributing to the Literary Vault

Thank you for your interest in contributing to Literary Vault! This document provides guidelines and instructions for contributing.

## Table of Contents

* [Code of Conduct](CONTRIBUTING.md#code-of-conduct)
* [How Can I Contribute?](CONTRIBUTING.md#how-can-i-contribute)
* [Style Guidelines](CONTRIBUTING.md#style-guidelines)
* [Commit Messages](CONTRIBUTING.md#commit-messages)
* [Pull Request Process](CONTRIBUTING.md#pull-request-process)

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

## How Can I Contribute?

### Adding New Literature

1. Place PDF files in the appropriate subdirectory under `pdfs/`
2. Create corresponding analysis in the `analysis/` directory
3. Update relevant documentation
4. Add entry to changelog using the update script

### Adding Analysis

1. Create a new markdown file in the appropriate analysis subdirectory
2. Follow the established analysis template
3. Include proper citations and references
4. Link to the corresponding PDF if available

### Improving Documentation

1. Ensure documentation is clear and concise
2. Update README files when adding new features
3. Maintain consistent formatting
4. Keep directory documentation up to date

## Style Guidelines

### Markdown Files

* Use consistent heading levels
* Include a table of contents for longer documents
* Use proper formatting for code blocks and quotes
* Include metadata section when applicable

### Directory Structure

* Maintain the established directory hierarchy
* Use clear, descriptive folder names
* Include README.md files in new directories
* Follow the naming conventions

### Analysis Documents

* Start with a clear summary
* Include methodology section
* Provide proper citations
* Use consistent formatting
* Include relevant diagrams or figures when helpful

## Commit Messages

* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters or less
* Reference issues and pull requests liberally after the first line
* Consider starting the commit message with an applicable emoji:
  * 📚 `:books:` when adding or updating documentation
  * 📝 `:memo:` when adding or updating analysis
  * 🔧 `:wrench:` when fixing something
  * ✨ `:sparkles:` when adding new features

## Pull Request Process

1. Update the README.md with details of changes if applicable
2. Update the CHANGELOG.md using the provided script
3. The PR will be merged once you have the sign-off of at least one maintainer

## Script Usage

### Updating the Changelog

Use the provided Python script to update the changelog:

```bash
# Add a new entry
python scripts/update_changelog.py add "Added" "New analysis for Paper X"

# Create a new release
python scripts/update_changelog.py release "1.0.0"
```

## Questions?

If you have questions about contributing, please open an issue in the repository.
