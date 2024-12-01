import MySQLdb
from src.session.config import Config

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

        return True, connection
    except Exception as e:
        return False, f'Error connecting to database: {str(e)}'
