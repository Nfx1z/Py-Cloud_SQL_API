from flask_sqlalchemy import SQLAlchemy
from src.session.config import Config
from dotenv import set_key

db = SQLAlchemy()

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
    db.init_app(app)

def get_db_uri(db_name, db_user, db_password):
    try:
        # Cloud SQL connection
        if Config.CLOUD_SQL_CONNECTION_NAME:
            # connect to Cloud SQL
            print("Connecting to Cloud SQL...")
            uri = f"mysql+mysqlconnector://{db_user}:{db_password}@/cloudsql/{Config.CLOUD_SQL_CONNECTION_NAME}/{db_name}"
        else:
            # Check connection
            print("Connecting to local MySQL...")
            uri = f"mysql+mysqlconnector://{db_user}:{db_password}@localhost:3306/{db_name}"
        
        # Set the SQLALCHEMY_DATABASE_URI in the .env file
        set_key('.env', 'SQLALCHEMY_DATABASE_URI', uri)

        return True, "Successfully created database URI"
    except Exception as e:
        return False, f'Error connecting to database: {str(e)}'
