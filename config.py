class Config:
    # Basic Flask configuration
    SECRET_KEY = 'dev'  # Change this to a secure key in production
    
    # Database configuration
    SQLALCHEMY_DATABASE_URI = 'sqlite:///literary_vault.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Upload folder configuration
    UPLOAD_FOLDER = 'uploads'  # This is referenced in your file_metadata route 