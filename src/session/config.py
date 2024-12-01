import os
import datetime

class Config:

    # Cloud SQL connection name
    CLOUD_SQL_CONNECTION_NAME = os.getenv('CLOUD_SQL_CONNECTION_NAME')
    # app-liveness:asia-southeast2:db-liveness

    # JWT authentication
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

    # Expired token after 15 minutes
    EXPIRES = datetime.datetime.now() + datetime.timedelta(minutes=15)

    # Google Cloud configuration
    GOOGLE_APPLICATION_CREDENTIALS = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

