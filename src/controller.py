from src.handler import fetch_data_from_db, add_data_to_db
from src.session.cookies import verify_jwt, generate_jwt
from src.db import get_db_connection
from flask import jsonify, make_response
from src.session.config import Config

def user_config_controller(request):
    # DB credentials for connection
    db_name = request.json.get('db_name')
    db_user = request.json.get('db_user')
    db_password = request.json.get('db_password')
    
    # Validate input parameters
    if not db_name or not db_user or not db_password:
        return jsonify({"error": "Both 'db_name', 'db_user', and 'db_password' are required"}), 400
    
    # Validate database credentials
    isValid, message = get_db_connection(db_name, db_user, db_password)
    if not isValid:
        return jsonify({"error": message}), 400
    
    # Generate JWT token for the user's configuration
    token = generate_jwt(db_name, db_user, db_password)
    success_message = (
        jsonify({"status_code": 200, "message": "User configuration received successfully!"}),
    )

    # Set cookie
    response = make_response(success_message, 200)
    response.set_cookie(
        "SQL_TOKEN", token, httponly=True, samesite="lax", expires=Config.EXPIRES
    )

    return response

def home_controller(token):
    user_id = verify_jwt(token)
    response = jsonify({"status_code": 200, "message": f"Hello {user_id}"}), 200
    # set cookie
    # response.set_cookie(
    #     "X-LIVENESS-TOKEN", token, httponly=True, samesite="lax", expires=Config.EXPIRES
    # )

    return response