from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Register blueprints
    from src.routes.questions import bp as questions_bp
    app.register_blueprint(questions_bp)
    
    # Add any other configuration here
    app.config['SECRET_KEY'] = 'your-secret-key-here'  # Change this!
    
    return app
