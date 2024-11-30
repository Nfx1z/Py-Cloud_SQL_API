import mysql.connector
from google.cloud import sqlconnector
from src.config import Config

def mysql_db_connection():

    # Cloud SQL connection
    if Config.CLOUD_SQL_CONNECTION_NAME:
        # Using google-cloud-sql-connector to connect to Cloud SQL securely
        connector = sqlconnector.connect(
            instance_connection_string=Config.CLOUD_SQL_CONNECTION_NAME,
            driver="mysql",
        )
        # connect to database
        connection = connector.connect(
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            db=Config.DB_NAME,
        )
        # Check connection
        print("Connected to Cloud SQL database")
    else:
        # For local development (assuming MySQL is running on localhost)
        connection = mysql.connector.connect(
            host="localhost",
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            database=Config.DB_NAME
        )
        # Check connection
        print("Connected to MySQL database")
    
    return connection
