#!/usr/bin/env python3

import os
import sys
import re
from datetime import datetime
from enum import Enum

class ChangeType(Enum):
    ADDED = "Added"
    CHANGED = "Changed"
    DEPRECATED = "Deprecated"
    REMOVED = "Removed"
    FIXED = "Fixed"
    SECURITY = "Security"

class Version:
    def __init__(self, major=0, minor=0, patch=0):
        self.major = major
        self.minor = minor
        self.patch = patch
    
    @classmethod
    def from_string(cls, version_str):
        if not version_str:
            return cls()
        match = re.match(r'(\d+)\.(\d+)\.(\d+)', version_str)
        if match:
            return cls(*map(int, match.groups()))
        return cls()
    
    def increment(self, change_type):
        """Increment version based on change type"""
        if change_type in ["BREAKING", "MAJOR"]:
            self.major += 1
            self.minor = 0
            self.patch = 0
        elif change_type in ["FEATURE", "MINOR"]:
            self.minor += 1
            self.patch = 0
        else:  # PATCH
            self.patch += 1
        return self
    
    def __str__(self):
        return f"{self.major}.{self.minor}.{self.patch}"

class ChangelogManager:
    def __init__(self):
        self.changelog_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'CHANGELOG.md')
    
    def read_changelog(self):
        """Read the current changelog file."""
        try:
            with open(self.changelog_path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return self._create_initial_changelog()
    
    def _create_initial_changelog(self):
        """Create initial changelog structure."""
        initial_content = """# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- None

### Changed
- None

### Deprecated
- None

### Removed
- None

### Fixed
- None

### Security
- None
"""
        with open(self.changelog_path, 'w') as file:
            file.write(initial_content)
        return initial_content

    def get_current_version(self):
        """Extract the latest version from changelog."""
        content = self.read_changelog()
        versions = re.findall(r'## \[(\d+\.\d+\.\d+)\]', content)
        return Version.from_string(versions[0] if versions else "0.0.0")

    def add_entry(self, change_type, description, version_bump="PATCH"):
        """Add a new entry to the changelog."""
        content = self.read_changelog()
        
        # Find the [Unreleased] section
        unreleased_pos = content.find('## [Unreleased]')
        if unreleased_pos == -1:
            print("Error: Could not find [Unreleased] section")
            return False
        
        # Find the appropriate subsection
        section_pos = content.find(f"### {change_type}", unreleased_pos)
        next_section_pos = content.find("###", section_pos + 1)
        
        if section_pos == -1:
            print(f"Error: Could not find {change_type} section")
            return False
        
        # Replace "- None" with the new entry if it's the only item
        current_section = content[section_pos:next_section_pos]
        if "- None" in current_section:
            updated_section = current_section.replace("- None", f"- {description}")
        else:
            # Add the new entry
            updated_section = current_section.rstrip() + f"\n- {description}\n"
        
        # Update the content
        new_content = (
            content[:section_pos] +
            updated_section +
            content[next_section_pos:]
        )
        
        with open(self.changelog_path, 'w') as file:
            file.write(new_content)
        
        return True

    def create_release(self, version_bump="PATCH"):
        """Create a new release from the [Unreleased] section."""
        content = self.read_changelog()
        current_version = self.get_current_version()
        new_version = current_version.increment(version_bump)
        
        # Get the unreleased content
        unreleased_pos = content.find('## [Unreleased]')
        next_version_pos = content.find('## [', unreleased_pos + 1)
        
        if unreleased_pos == -1:
            print("Error: Could not find [Unreleased] section")
            return False
        
        unreleased_content = content[unreleased_pos:next_version_pos]
        
        # Skip release if no changes
        if all(x in unreleased_content for x in ["- None\n"] * 6):
            print("No changes to release")
            return False
        
        # Create the new release section
        today = datetime.now().strftime('%Y-%m-%d')
        new_release = f"## [{new_version}] - {today}\n" + unreleased_content[unreleased_content.find('\n### '):]
        
        # Reset the unreleased section
        empty_unreleased = """## [Unreleased]

### Added
- None

### Changed
- None

### Deprecated
- None

### Removed
- None

### Fixed
- None

### Security
- None

"""
        
        # Update the changelog
        new_content = (
            content[:unreleased_pos] +
            empty_unreleased +
            new_release +
            (content[next_version_pos:] if next_version_pos != -1 else "")
        )
        
        with open(self.changelog_path, 'w') as file:
            file.write(new_content)
        
        return True

def print_usage():
    """Print usage instructions."""
    print("""
Usage:
    Add entry:    cl add <type> "<description>" [version_bump]
    New release:  cl release [version_bump]

Types:
    a, added     - Added
    c, changed   - Changed
    d, dep       - Deprecated
    r, removed   - Removed
    f, fixed     - Fixed
    s, sec       - Security

Version Bump:
    major    - Breaking changes (1.0.0)
    minor    - New features (0.1.0)
    patch    - Bug fixes (0.0.1) [default]

Example:
    cl add a "New feature X" minor
    cl release major
    """)

def parse_change_type(type_str):
    """Convert short codes to full change types."""
    type_map = {
        'a': 'Added',
        'c': 'Changed',
        'd': 'Deprecated',
        'r': 'Removed',
        'f': 'Fixed',
        's': 'Security',
        'added': 'Added',
        'changed': 'Changed',
        'dep': 'Deprecated',
        'removed': 'Removed',
        'fixed': 'Fixed',
        'sec': 'Security'
    }
    return type_map.get(type_str.lower(), type_str)

def main():
    manager = ChangelogManager()
    
    if len(sys.argv) < 2:
        print_usage()
        return
    
    command = sys.argv[1].lower()
    
    if command == "add" and len(sys.argv) >= 4:
        change_type = parse_change_type(sys.argv[2])
        description = sys.argv[3]
        version_bump = sys.argv[4].upper() if len(sys.argv) > 4 else "PATCH"
        
        if manager.add_entry(change_type, description, version_bump):
            print(f"Successfully added {change_type} entry: {description}")
    
    elif command == "release":
        version_bump = sys.argv[2].upper() if len(sys.argv) > 2 else "PATCH"
        if manager.create_release(version_bump):
            print(f"Successfully created new release")
    
    else:
        print_usage()

if __name__ == "__main__":
    main()
