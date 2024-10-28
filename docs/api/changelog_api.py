#!/usr/bin/env python3

from flask import Flask, jsonify, request
from functools import wraps
import os
import requests
from typing import List, Dict, Any
from update_changelog import ChangelogManager  # Changed from relative to absolute import

app = Flask(__name__)
manager = ChangelogManager()

def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return jsonify({'error': 'Missing or invalid authorization token'}), 401
        
        # Validate token here
        token = auth_header.split(' ')[1]
        if not is_valid_token(token):
            return jsonify({'error': 'Invalid authorization token'}), 401
            
        return f(*args, **kwargs)
    return decorated

def is_valid_token(token: str) -> bool:
    # Implement token validation logic
    return token == os.getenv('API_TOKEN')

def update_gitbook(content: str, path: str) -> bool:
    """Update content in GitBook."""
    api_key = os.getenv('GITBOOK_API_KEY')
    space_id = os.getenv('GITBOOK_SPACE_ID')
    
    if not api_key or not space_id:
        raise ValueError("GitBook API key or space ID not configured")
    
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    
    response = requests.post(
        f'https://api.gitbook.com/v1/spaces/{space_id}/content',
        headers=headers,
        json={
            'path': path,
            'content': content
        }
    )
    
    return response.status_code == 200

@app.route('/api/repository/changes', methods=['GET'])
@require_auth
def get_changes():
    """Get list of changes in the repository."""
    try:
        changes = manager.git_analyzer.get_changes()
        return jsonify({
            'success': True,
            'changes': [
                {
                    'type': change[0],
                    'path': change[1],
                    'category': change[2]
                }
                for change in changes
            ]
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/changelog/update', methods=['POST'])
@require_auth
def update_changelog():
    """Update changelog with new changes."""
    try:
        data = request.json
        changes = data.get('changes', [])
        sync_gitbook = data.get('sync_gitbook', True)
        
        # Update changelog
        success = all(
            manager.add_entry(change['type'], change['description'])
            for change in changes
        )
        
        if not success:
            return jsonify({
                'success': False,
                'error': 'Failed to update changelog'
            }), 400
        
        # Sync with GitBook if requested
        if sync_gitbook:
            with open(manager.changelog_path, 'r') as f:
                content = f.read()
            gitbook_success = update_gitbook(content, '/changelog.md')
            if not gitbook_success:
                return jsonify({
                    'success': False,
                    'error': 'Failed to sync with GitBook'
                }), 500
        
        return jsonify({
            'success': True,
            'message': 'Changelog updated successfully'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/changelog/release', methods=['POST'])
@require_auth
def create_release():
    """Create a new release."""
    try:
        data = request.json
        version_bump = data.get('version_bump', 'PATCH')
        sync_gitbook = data.get('sync_gitbook', True)
        create_github_release = data.get('create_github_release', False)
        
        # Create release
        success = manager.create_release(version_bump)
        if not success:
            return jsonify({
                'success': False,
                'error': 'Failed to create release'
            }), 400
        
        # Sync with GitBook if requested
        if sync_gitbook:
            with open(manager.changelog_path, 'r') as f:
                content = f.read()
            gitbook_success = update_gitbook(content, '/changelog.md')
            if not gitbook_success:
                return jsonify({
                    'success': False,
                    'error': 'Failed to sync with GitBook'
                }), 500
        
        # Create GitHub release if requested
        if create_github_release:
            # Implement GitHub release creation
            pass
        
        return jsonify({
            'success': True,
            'version': str(manager.get_current_version()),
            'message': 'Release created successfully'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/gitbook/content', methods=['GET'])
@require_auth
def get_gitbook_content():
    """Get content from GitBook."""
    try:
        path = request.args.get('path')
        space_id = request.args.get('space_id')
        
        if not path or not space_id:
            return jsonify({
                'success': False,
                'error': 'Missing required parameters'
            }), 400
        
        api_key = os.getenv('GITBOOK_API_KEY')
        if not api_key:
            return jsonify({
                'success': False,
                'error': 'GitBook API key not configured'
            }), 500
        
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
        
        response = requests.get(
            f'https://api.gitbook.com/v1/spaces/{space_id}/content',
            headers=headers,
            params={'path': path}
        )
        
        if response.status_code != 200:
            return jsonify({
                'success': False,
                'error': 'Failed to fetch GitBook content'
            }), response.status_code
        
        return jsonify({
            'success': True,
            'content': response.json()
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True)
