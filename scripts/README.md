# Scripts Directory

This directory contains utility scripts for managing the Literary Vault repository.

## Available Scripts

### update_changelog.py

A Python script for maintaining the project's CHANGELOG.md file.

#### Usage

```bash
# Add a new changelog entry
python update_changelog.py add <type> "<description>"

# Create a new release
python update_changelog.py release <version>
```

#### Entry Types

- Added
- Changed
- Deprecated
- Removed
- Fixed
- Security

#### Examples

```bash
# Add new feature
python update_changelog.py add "Added" "New analysis template for EEG papers"

# Create release
python update_changelog.py release "1.0.0"
```

## Requirements

- Python 3.x
- No additional dependencies required
