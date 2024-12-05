from flask import jsonify
from src.utils.cookies import verify_jwt
from src.db import get_connection

def create_table_controller(token, request):
    try:
        # Get table name and columns
        table_name = request.json.get('table_name')
        columns = request.json.get('columns')

        # Validate input parameters
        if not table_name or not columns:
            return jsonify({"error": "Both 'table_name' and 'columns' are required"}), 400
        # Verify and Decode JWT token
        db_name, db_user, user_password = verify_jwt(token)
        
        # Initiate database connection
        conn = get_connection(db_name, db_user, user_password)
        cursor = conn.cursor()

        # Construct the CREATE TABLE query using a loop
        column_definitions = []
        for col in columns:
            column_name = col['name']
            column_type = col['type']
            column_definitions.append(f"`{column_name}` {column_type}")
        columns_str = ", ".join(column_definitions)
        
        # Query database
        query = f"""
        CREATE TABLE `{table_name}` (
            id INT AUTO_INCREMENT PRIMARY KEY,
            {columns_str}
        );
        """
        cursor.execute(query)

        # Close cursor and connection
        cursor.close()
        conn.close()

        # Return results
        return jsonify({"message": "Table created successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
