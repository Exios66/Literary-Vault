#!/usr/bin/env python3

import os
import sys
from datetime import datetime

def get_changelog_path():
    """Returns the path to the CHANGELOG.md file."""
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'CHANGELOG.md')

def read_changelog():
    """Reads the current changelog file."""
    try:
        with open(get_changelog_path(), 'r') as file:
            return file.read()
    except FileNotFoundError:
        return ""

def write_changelog(content):
    """Writes the updated changelog content to file."""
    with open(get_changelog_path(), 'w') as file:
        file.write(content)

def add_changelog_entry(type_of_change, description):
    """Adds a new entry to the changelog under [Unreleased] section."""
    changelog = read_changelog()
    
    # Find the [Unreleased] section
    unreleased_pos = changelog.find('## [Unreleased]')
    if unreleased_pos == -1:
        print("Error: Could not find [Unreleased] section in changelog")
        return False
    
    # Find the appropriate subsection
    section_pos = changelog.find(f"### {type_of_change}", unreleased_pos)
    next_section_pos = changelog.find("###", section_pos + 1)
    
    if section_pos == -1:
        print(f"Error: Could not find {type_of_change} section")
        return False
    
    # Add the new entry
    current_content = changelog[section_pos:next_section_pos]
    updated_content = current_content.rstrip() + f"\n- {description}\n"
    
    # Replace the old section with updated content
    new_changelog = (
        changelog[:section_pos] +
        updated_content +
        changelog[next_section_pos:]
    )
    
    write_changelog(new_changelog)
    return True

def create_release(version):
    """Creates a new release from the [Unreleased] section."""
    changelog = read_changelog()
    
    # Get the unreleased content
    unreleased_pos = changelog.find('## [Unreleased]')
    next_version_pos = changelog.find('## [', unreleased_pos + 1)
    
    if unreleased_pos == -1:
        print("Error: Could not find [Unreleased] section")
        return False
    
    unreleased_content = changelog[unreleased_pos:next_version_pos]
    
    # Create the new release section
    today = datetime.now().strftime('%Y-%m-%d')
    new_release = f"## [{version}] - {today}\n" + unreleased_content[unreleased_content.find('\n### '):]
    
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
    new_changelog = (
        changelog[:unreleased_pos] +
        empty_unreleased +
        new_release +
        changelog[next_version_pos:]
    )
    
    write_changelog(new_changelog)
    return True

def print_usage():
    """Prints usage instructions."""
    print("""
Usage:
    Add entry:    python update_changelog.py add <type> "<description>"
    New release:  python update_changelog.py release <version>

Types:
    - Added
    - Changed
    - Deprecated
    - Removed
    - Fixed
    - Security

Example:
    python update_changelog.py add Added "New feature X"
    python update_changelog.py release 1.0.0
    """)

def main():
    if len(sys.argv) < 2:
        print_usage()
        return
    
    command = sys.argv[1].lower()
    
    if command == "add" and len(sys.argv) == 4:
        type_of_change = sys.argv[2]
        description = sys.argv[3]
        if add_changelog_entry(type_of_change, description):
            print(f"Successfully added {type_of_change} entry: {description}")
    
    elif command == "release" and len(sys.argv) == 3:
        version = sys.argv[2]
        if create_release(version):
            print(f"Successfully created release {version}")
    
    else:
        print_usage()

if __name__ == "__main__":
    main()
