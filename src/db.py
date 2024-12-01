import mysql.connector
from google.cloud import sqlconnector
from session.config import Config

def get_db_connection(db_name, db_user, db_password):
    try:
        # Cloud SQL connection
        if Config.CLOUD_SQL_CONNECTION_NAME:
            # Using google-cloud-sql-connector to connect to Cloud SQL securely
            connector = sqlconnector.connect(
                instance_connection_string=Config.CLOUD_SQL_CONNECTION_NAME,
                driver="mysql",
            )
            # connect to database
            connection = connector.connect(
                user=db_user,
                password=db_password,
                db=db_name,
            )
            # Check connection
            print("Connected to Cloud SQL database")
        else:
            # For local development (assuming MySQL is running on localhost)
            connection = mysql.connector.connect(
                host="localhost",
                user=db_user,
                password=db_password,
                database=db_name
            )
            # Check connection
            print("Connected to MySQL database")
        return True, connection
    except Exception as e:
        return False, f'Error connecting to database: {str(e)}'
