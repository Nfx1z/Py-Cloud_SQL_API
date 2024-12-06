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
        rows = cursor.fetchall()

        # Get column names from cursor.description
        columns = [col[0] for col in cursor.description]

        # Create a list of dictionaries, each row mapped to column names
        result = [dict(zip(columns, row)) for row in rows]

        # Close cursor and connection
        cursor.close()
        conn.close()
        
        # Check if the result is empty
        if rows is None or len(rows) == 0:
            return jsonify({"error": f"No data found in table '{table_name}'"}), 404
        
        # Return results
        return jsonify({"table": table_name, "contents": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500