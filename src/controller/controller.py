from src.utils.cookies import generate_jwt, generate_secret_key
from src.db import test_connection
from flask import jsonify, make_response

def login_controller(request):
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
        
        # Return success message
        success_message = (
            jsonify({"status_code": 200, "message": "Connected!"}), 200
        )
        response = make_response(success_message)
        
        # Generate secret key for the user's configuration
        generate_secret_key(6)

        # Generate JWT token for the user's configuration
        token = generate_jwt(db_name, db_user, user_password)

        # Set cookie
        response.set_cookie(
            "SQL_TOKEN", token, 
            secure=True, httponly=True, 
            samesite=None, max_age=60*15 # 15 minutes
        )

        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 500