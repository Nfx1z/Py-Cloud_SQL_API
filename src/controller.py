from src.handler import fetch_data_from_db, add_data_to_db
from src.session.cookies import verify_jwt, generate_jwt
from src.db import init_database, get_db_connection
from flask import jsonify, make_response
from src.session.config import Config

def user_config_controller(request):
    try:
        # DB credentials for connection
        db_name = request.json.get('db_name')
        db_user = request.json.get('db_user')
        user_password = request.json.get('user_password')
        
        # Validate input parameters
        if not db_name or not db_user:
            return jsonify({"error": "Both 'db_name', 'db_user', and 'user_password' are required"}), 400

        # Initiate database connection
        isValid, err_or_db = init_database(db_name, db_user, user_password)
        if not isValid:
            return jsonify({"error": err_or_db}), 400
        
        # Generate JWT token for the user's configuration
        token = generate_jwt(err_or_db)
        success_message = (
            jsonify({"status_code": 200, "message": "User configuration received successfully!"}), 200
        )

        # Set cookie
        response = make_response(success_message)
        response.set_cookie(
            "SQL_TOKEN", token, httponly=True, samesite="lax", expires=Config.EXPIRES
        )

        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def home_controller(token):
    db_name, db_user, user_password = verify_jwt(token)
    isValid, message = get_db_connection(db_name, db_user, user_password)
    if not isValid:
        return jsonify({"error": message}), 400

    return jsonify({"status_code": 200, "message": "Home page"}), 200