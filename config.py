import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev'
    DEBUG = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true' 