from src.utils.cookies import verify_jwt, generate_jwt, generate_secret_key
from service.db import test_connection
from flask import jsonify, make_response
from src.utils.config import EXPIRES

def user_controller(request):
    try:
        # DB credentials for connection
        db_name = request.json.get('db_name')
        db_user = request.json.get('db_user')
        user_password = request.json.get('user_password')
        
        # Validate input parameters
        if not db_name or not db_user or not user_password:
            return jsonify({"error": "Both 'db_name', 'db_user', and 'user_password' are required"}), 400

        # Initiate database connection
        isValid, message = test_connection(db_name, db_user, user_password)
        if not isValid:
            return jsonify({"error": message}), 400
        
        # Generate secret key for the user's configuration
        generate_secret_key()

        # Generate JWT token for the user's configuration
        token = generate_jwt(db_name, db_user, user_password)
        
        # Return success message
        success_message = (
            jsonify({"status_code": 200, "message": "Connected!"}), 200
        )

        # Set cookie
        response = make_response(success_message)
        response.set_cookie(
            "SQL_TOKEN", token, httponly=True, samesite="lax", expires=EXPIRES
        )

        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def home_controller(token):
    try:
        db_name, db_user, user_password = verify_jwt(token)
        return jsonify({"status_code": 200, "message": "Home page"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    # if not isValid:
    #     return jsonify({"error": message}), 400

    # return jsonify({"status_code": 200, "message": "Home page"}), 200