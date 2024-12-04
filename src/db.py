import os, sys
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from src.session.config import Config

# Add the root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def init_database(db_name, db_ip, db_user, db_password):
    try:
        # Initialize SQLAlchemy
        db = SQLAlchemy()

        # Import the Flask app from the main module
        from main import app

        # Construct the MySQL URI
        # there is bunch of uri pattern that you can use
        uri = f"mysql+mysqldb://{db_user}:{db_password}@{db_ip}/{db_name}?unix_socket=/cloudsql/{Config.PROJECT_ID}:{Config.INSTANCE_NAME}"

        # Examples without using cloud sql proxy: 
        # uri = "mysql+mysqldb://<DB_USER>:<USER_PASSWORD>@/<DB_NAME>?unix_socket=/cloudsql/<CONNECTION_NAME>"
        # uri = "mysql+mysqldb://<DB_USER>:<USER_PASSWORD>@<IP_ADDRESS>/<DB_NAME>?unix_socket=/cloudsql/<CONNECTION_NAME>"
        # uri = "mysql+pymysql://<DB_USER>:<USER_PASSWORD>@<IP_ADDRESS>:3306/<DB_NAME>"

        # Examples using cloud sql proxy:
        # uri = "mysql+mysqldb://<DB_USER>:<USER_PASSWORD>@127.0.0.1/<DB_NAME>?unix_socket=/cloudsql/<CONNECTION_NAME>"
        # uri = "mysql+pymysql://<DB_USER>:<USER_PASSWORD>@127.0.0.1:3306/<DB_NAME>"

        # Set the SQLAlchemy database URI
        app.config['SQLALCHEMY_DATABASE_URI'] = uri

        # Disable SQLAlchemy tracking for better performance
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        db.init_app(app)
        return True, db
    except Exception as e:
        return False, f"error: {str(e)}"

# def init_db(app):
#     app.config['SQLALCHEMY_DATABASE_URI'] = generate_uri(
#         Config.DB_NAME, Config.DB_USER, Config.DB_PASSWORD
#     )
#     db.init_app(app)

def get_db_connection(db_name, db_user, db_password):
    try:
        # For local development
        

        return True
    except Exception as e:
        return False, jsonify({"error": "uv", "message": "Error connecting to database in "}), 500
