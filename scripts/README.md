---
icon: python
---

# Scripts Directory

This directory contains utility scripts for managing the Literary Vault repository.

## Available Scripts

### Changelog Management (cl)

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
* `patch` - Bug fixes (0.0.1) \[default]

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

#### Features

* Automatic semantic versioning
* Short command aliases
* Maintains Keep a Changelog format
* Prevents empty releases
* Automatic section management

## Requirements

* Python 3.x
* No additional dependencies required

## Installation

The scripts are automatically executable. You can run them directly from the scripts directory:

```bash
cd scripts
./cl add a "New feature"
```
