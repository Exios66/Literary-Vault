#!/usr/bin/env python3

import os
import sys
import re
import subprocess
from datetime import datetime
from enum import Enum
from typing import List, Tuple

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

class GitChangeAnalyzer:
    def __init__(self):
        self.root_dir = os.path.dirname(os.path.dirname(__file__))

    def get_changes(self) -> List[Tuple[str, str, str]]:
        """Get list of changes from git status."""
        os.chdir(self.root_dir)
        try:
            # Get staged and unstaged changes
            status = subprocess.check_output(['git', 'status', '--porcelain']).decode()
            changes = []
            
            for line in status.split('\n'):
                if not line:
                    continue
                    
                status_code = line[:2]
                file_path = line[3:]
                
                # Determine change type
                if status_code.startswith('A') or (status_code.startswith('??') and os.path.exists(file_path)):
                    changes.append(('Added', file_path, self._categorize_file(file_path)))
                elif status_code.startswith('M'):
                    changes.append(('Changed', file_path, self._categorize_file(file_path)))
                elif status_code.startswith('D'):
                    changes.append(('Removed', file_path, self._categorize_file(file_path)))
                
            return changes
        except subprocess.CalledProcessError:
            print("Error: Not a git repository or git command failed")
            return []

    def _categorize_file(self, file_path: str) -> str:
        """Categorize file based on its path and type."""
        path_lower = file_path.lower()
        
        # Security-related changes
        if any(s in path_lower for s in ['.env', 'security', 'auth', 'password', 'credential']):
            return 'Security'
            
        # Documentation changes
        if any(s in path_lower for s in ['readme', 'docs/', 'documentation', '.md']):
            return 'Documentation'
            
        # Test changes
        if 'test' in path_lower:
            return 'Tests'
            
        # Configuration changes
        if any(s in path_lower for s in ['.json', '.yaml', '.yml', '.toml', '.ini', 'config']):
            return 'Configuration'
            
        return 'Feature'

class ChangelogManager:
    def __init__(self):
        self.changelog_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'CHANGELOG.md')
        self.git_analyzer = GitChangeAnalyzer()
    
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

    def analyze_and_update(self):
        """Analyze git changes and update changelog automatically."""
        changes = self.git_analyzer.get_changes()
        if not changes:
            print("No changes detected")
            return False

        # Group changes by type
        changes_by_type = {}
        for change_type, file_path, category in changes:
            if change_type not in changes_by_type:
                changes_by_type[change_type] = []
            changes_by_type[change_type].append((file_path, category))

        # Add entries for each type of change
        for change_type, files in changes_by_type.items():
            # Group files by category
            files_by_category = {}
            for file_path, category in files:
                if category not in files_by_category:
                    files_by_category[category] = []
                files_by_category[category].append(file_path)

            # Create and add entries
            for category, file_paths in files_by_category.items():
                if len(file_paths) == 1:
                    description = f"{category}: {file_paths[0]}"
                else:
                    description = f"{category}: Multiple files updated ({len(file_paths)} files)"
                self.add_entry(change_type, description)

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

def main():
    manager = ChangelogManager()
    
    if len(sys.argv) == 1:
        # Default behavior: analyze changes and update changelog
        if manager.analyze_and_update():
            print("Successfully updated changelog with detected changes")
        return
    
    command = sys.argv[1].lower()
    
    if command == "release":
        version_bump = sys.argv[2].upper() if len(sys.argv) > 2 else "PATCH"
        if manager.create_release(version_bump):
            print(f"Successfully created new release")
    else:
        print("""
Usage:
    Update changelog:  cl
    Create release:    cl release [version_bump]

Version Bump:
    major    - Breaking changes (1.0.0)
    minor    - New features (0.1.0)
    patch    - Bug fixes (0.0.1) [default]
        """)

if __name__ == "__main__":
    main()
