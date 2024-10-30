from flask import Flask
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Register blueprints and initialize extensions here
    
    return app

if __name__ == '__main__':
    app = create_app()
    # Remove debug=True and use environment variables instead
    app.run(host='0.0.0.0', port=5000) 