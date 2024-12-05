from src.utils.cookies import verify_jwt, generate_jwt, generate_secret_key
from src.service.db import test_connection, get_connection
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
        
        # Return success message
        success_message = (
            jsonify({"status_code": 200, "message": "Connected!"}), 200
        )
        response = make_response(success_message)
        
        # Generate secret key for the user's configuration
        generate_secret_key(6)

        # Generate JWT token for the user's configuration
        token = generate_jwt(db_name, db_user, user_password)
        print(token)
        # Set cookie
        response.set_cookie(
            "SQL_TOKEN", token, 
            secure=True, httponly=True, 
            samesite=None, max_age=30
        )

        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_tables_controller(token):
    try:
        # Verify and Decode JWT token
        db_name, db_user, user_password = verify_jwt(token)
        
        # Initiate database connection
        conn = get_connection(db_name, db_user, user_password)
        cursor = conn.cursor()

        # Query database
        query = f"""
        SHOW TABLES FROM {db_name};
        """
        cursor.execute(query)
        tables = cursor.fetchall()

        # Close cursor and connection
        cursor.close()
        conn.close()

        # Return results
        return jsonify({"tables": tables}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

