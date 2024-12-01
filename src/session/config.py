import os
import datetime

class Config:

    # JWT authentication
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

    # Expired token after 15 minutes
    EXPIRES = datetime.datetime.now() + datetime.timedelta(minutes=15)

    # Google Cloud configuration
    GOOGLE_APPLICATION_CREDENTIALS = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

    # Cloud SQL configuration
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
