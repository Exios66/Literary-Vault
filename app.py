from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    try:
        # Initialize Flask app
        app = Flask(__name__)
        app.config.from_object(config_class)
        
        # Initialize extensions with app context
        db.init_app(app)
        migrate.init_app(app, db)
        
        # Register blueprints
        try:
            from src.routes.questions import bp as questions_bp
            app.register_blueprint(questions_bp, url_prefix='/api')
        except ImportError as e:
            logger.error(f"Failed to import blueprint: {str(e)}")
            raise
        
        # Log successful initialization
        logger.info("Application initialized successfully")
        
        return app
        
    except Exception as e:
        logger.error(f"Failed to create app: {str(e)}")
        raise

if __name__ == '__main__':
    try:
        app = create_app()
        app.run(debug=True)
    except Exception as e:
        logger.error(f"Failed to run app: {str(e)}")

@app.errorhandler(404)
@app.route('/404')
def not_found_error(_):
    return render_template('404.html'), 404