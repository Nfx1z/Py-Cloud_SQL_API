import MySQLdb
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from src.session.config import Config

db = SQLAlchemy()

def generate_uri(db_name, db_ip, db_user, db_password):
    based_uri = f'mysql+pymysql://{db_user}:{db_password}@{db_ip}:3306/{db_name}'

    return based_uri

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = generate_uri(
        Config.DB_NAME, Config.DB_USER, Config.DB_PASSWORD
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

def get_db_connection(db_name, db_user, db_password):
    try:
        # For local development
        if Config.DB_HOST == 'localhost':
            connection = MySQLdb.connect(
                user=db_user,
                passwd=db_password,
                db=db_name,
                host='localhost'
            )
        # Cloud SQL connection
        else:
            connection = MySQLdb.connect(
                user=db_user,
                passwd=db_password,
                db=db_name,
                host=f"/cloudsql/{Config.CLOUD_SQL_CONNECTION_NAME}"
            )
            print("hello")

        return True, connection
    except Exception as e:
        return False, jsonify({"error": "uv", "message": "Error connecting to database in "}), 500
