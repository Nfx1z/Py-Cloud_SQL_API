from flask import jsonify
from src.utils.cookies import verify_jwt
from src.db import get_connection

def get_contents_controller(token, table_name):
    try:
        # Verify and Decode JWT token
        db_name, db_user, user_password = verify_jwt(token)

        # Initiate database connection
        conn = get_connection(db_name, db_user, user_password)
        cursor = conn.cursor()

        # Query database
        query = f"""
        SELECT * FROM {table_name};
        """
        cursor.execute(query)
        contents = cursor.fetchall()

        # Remove double quotes from strings to avoid JSON parsing errors
        for items in contents:
            cleaned_result = [item.replace("\"", "") if isinstance(item, str) else item for item in items]
        # cleaned_result = [[item.replace("\"", "") if isinstance(item, str) else item for item in items] for items in contents]
        
        # Close cursor and connection
        cursor.close()
        conn.close()

        # Return results
        return jsonify({"contents": cleaned_result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500