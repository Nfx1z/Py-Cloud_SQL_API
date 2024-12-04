import os
import datetime

# Socket path for cloud sql proxy
SOCKET_PATH= f"/cloudsql/{os.getenv('CLOUD_SQL_CONNECTION_NAME')}"
# Database configuration
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_IP=os.getenv('DB_IP')

# JWT authentication
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

# Expired token after 15 minutes
EXPIRES = datetime.datetime.utcnow() + datetime.timedelta(seconds=30)