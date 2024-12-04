import os

# Socket path for cloud sql proxy
SOCKET_PATH= f"/cloudsql/{os.getenv('CLOUD_SQL_CONNECTION_NAME')}"
# Database configuration
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_IP=os.getenv('DB_IP')