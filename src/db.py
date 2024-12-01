import MySQLdb
from src.session.config import Config

def get_db_connection(db_name, db_user, db_password):
    try:
        # Cloud SQL connection
        connection = MySQLdb.connect(
            user=db_user,
            passwd=db_password,
            db=db_name,
            host=f"/cloudsql/{Config.CLOUD_SQL_CONNECTION_NAME}"
        )
        # connect to Cloud SQL
        print("Connecting to Cloud SQL...")

        return True, connection
    except Exception as e:
        return False, f'Error connecting to database: {str(e)}'
