from functools import wraps
from flask import request, jsonify

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not hasattr(request, 'user') or not request.user:
            return jsonify({'error': 'Unauthorized'}), 401
        return f(*args, **kwargs)
    return decorated_function 