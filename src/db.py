import mysql.connector
from flask import jsonify
from src.utils.config import  DB_PORT, DB_IP, SOCKET_PATH

def test_connection(db_name, db_user, user_password):
    try:
        # only for cloud SQL using cloud sql proxy for more secure connection
        conn = mysql.connector.connect(
            user=db_user,
            password=user_password,
            database=db_name,
            unix_socket=SOCKET_PATH  # Use the Cloud SQL Unix socket
        )
        # this method also works for local connections
        # conn = mysql.connector.connect(
        #     user=db_user,
        #     password=user_password,
        #     database=db_name,
        #     host=DB_IP,  # Use the public IP address of the Cloud SQL instance
        #     port=DB_PORT  # Default MySQL port
        # )
        
        # Close the connection
        conn.close()
        return True, f"message: Connection successful"
    except mysql.connector.Error as error:
        return False, f"error 1: {str(error)}"
    
def get_connection(db_name, db_user, user_password):
    try:
        # only for cloud SQL using cloud sql proxy for more secure connection
        conn = mysql.connector.connect(
            user=db_user,
            password=user_password,
            database=db_name,
            unix_socket=SOCKET_PATH  # Use the Cloud SQL Unix socket
        )
        # this method also works for local connections
        # conn = mysql.connector.connect(
        #     user=db_user,
        #     password=user_password,
        #     database=db_name,
        #     host=DB_IP,  # Use the public IP address of the Cloud SQL instance
        #     port=DB_PORT  # Default MySQL port
        # )
        return conn
    except mysql.connector.Error as error:
        raise error

# # Initialize SQLAlchemy
# db = SQLAlchemy()

# def init_database(app):
#     # Construct the MySQL URI
#     # there is bunch of uri pattern that you can use
#     uri = f"mysql+mysqldb://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}?unix_socket=/cloudsql/{CLOUD_SQL_CONNECTION_NAME}"

#     # Examples without using cloud sql proxy for cloud SQL connections: 
#     # uri = f"mysql+mysqldb://{DB_USER}:{USER_PASSWORD}@/{DB_NAME}?unix_socket=/cloudsql/{CONNECTION_NAME}"
#     # uri = f"mysql+mysqldb://{DB_USER}:{USER_PASSWORD}@{IP_ADDRESS}/{DB_NAME}?unix_socket=/cloudsql/{CONNECTION_NAME}"
#     # uri = f"mysql+pymysql://{DB_USER}:{USER_PASSWORD}@{IP_ADDRESS}:{DB_PORT}/{DB_NAME}"
#     # Examples using cloud sql proxy for cloud SQL connections:
#     # uri = f"mysql+mysqldb://{DB_USER}:{USER_PASSWORD}@127.0.0.1/{DB_NAME}?unix_socket=/cloudsql/{CONNECTION_NAME}"
#     # uri = f"mysql+pymysql://{DB_USER}:{USER_PASSWORD}@127.0.0.1:{DB_PORT}/{DB_NAME}"

#     # For local connections
#     # uri = f"mysql+mysqldb://{DB_USER}:{USER_PASSWORD}@localhost/{DB_NAME}"

#     # Set the SQLAlchemy database URI
#     app.config['SQLALCHEMY_DATABASE_URI'] = uri
    
#     # Disable SQLAlchemy tracking for better performance
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#     db.init_app(app)
