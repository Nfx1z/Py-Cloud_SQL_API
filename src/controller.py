from src.handler import fetch_data_from_db, add_data_to_db
from src.session.cookies import verify_jwt, generate_jwt
from src.db import get_db_connection, generate_uri
from flask import jsonify, make_response
from src.session.config import Config
import MySQLdb

def user_config_controller(request):
    # DB credentials for connection
    db_name = request.json.get('db_name')
    db_user = request.json.get('db_user')
    db_password = request.json.get('db_password')
    
    # Validate input parameters
    if not db_name or not db_user:
        return jsonify({"error": "Both 'db_name' and 'db_user' are required"}), 400
    
    db_ip ='35.232.130.180'
    print(generate_uri(db_name, db_ip, db_user, db_password))


    # Generate JWT token for the user's configuration
    token = generate_jwt(db_name, db_user, db_password)
    success_message = (
        jsonify({"status_code": 200, "message": "User configuration received successfully!"}), 200
    )

    # Set cookie
    response = make_response(success_message)
    response.set_cookie(
        "SQL_TOKEN", token, httponly=True, samesite="lax", expires=Config.EXPIRES
    )

    return response

def home_controller(token):
    db_name, db_user, db_password = verify_jwt(token)
    isValid, message = get_db_connection(db_name, db_user, db_password)
    if not isValid:
        return jsonify({"error": message}), 400

    return jsonify({"status_code": 200, "message": "Home page"}), 200