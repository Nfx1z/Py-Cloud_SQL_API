import os
import secrets

class Config:
    # Cloud SQL configuration (for production on Google Cloud)
    CLOUD_SQL_CONNECTION_NAME = os.getenv('CLOUD_SQL_CONNECTION_NAME')  # Use environment variable
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_NAME = os.getenv('DB_NAME')

    # Local development configuration
    # DB_HOST = 'localhost'
    # DB_PORT = 3306

    # JWT authentication
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

    # Google Cloud configuration
    GOOGLE_APPLICATION_CREDENTIALS = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

    # Flask configuration
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')
    DEBUG = os.getenv('DEBUG', True)

def generate_secret_key():
    secret_key = secrets.token_hex(16)