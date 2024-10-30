from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
try:
    from config import Config
except ImportError:
    class Config:
        SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev'
        DEBUG = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
import os

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    CORS(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/api/theme', methods=['GET'])
    def get_theme():
        # Could be expanded to fetch theme from user preferences/database
        return jsonify({'theme': 'light'})

    @app.route('/api/theme', methods=['POST'])
    def set_theme():
        theme = request.json.get('theme')
        # Could be expanded to save theme to user preferences/database
        return jsonify({'success': True, 'theme': theme})

    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        return render_template('500.html'), 500

    return app

if __name__ == '__main__':
    app = create_app()
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(host='0.0.0.0', port=port, debug=debug)