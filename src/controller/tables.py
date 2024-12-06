from flask import jsonify
from src.utils.cookies import verify_jwt
from src.db import get_connection

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

        # Flatten the result
        flattened_result = [item[0] for item in tables]

        # Close cursor and connection
        cursor.close()
        conn.close()

        # Return results
        return ({"database": db_name, "tables": flattened_result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def create_table_controller(token, request):
    try:
        # Get table name and columns
        table = request.json.get('table')
        columns = request.json.get('columns')

        # Validate input parameters
        if not table or not columns:
            return jsonify({"error": "Both 'table' and 'columns' are required"}), 400
        
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
        CREATE TABLE `{table}` (
            id INT AUTO_INCREMENT PRIMARY KEY,
            {columns_str}
        );
        """
        cursor.execute(query)

        # Close cursor and connection
        cursor.close()
        conn.close()

        # Return results
        return jsonify({"message": f"Table '{table}' created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def describe_table_controller(token, table):
    try:
        # Verify and Decode JWT token
        db_name, db_user, user_password = verify_jwt(token)

        # Initiate database connection
        conn = get_connection(db_name, db_user, user_password)
        cursor = conn.cursor()

        # Query database
        query = f"""
        DESCRIBE {table}
        """
        cursor.execute(query)
        columns = cursor.fetchall()

        # Prepare the formatted output
        formatted_columns = []
        for column in columns:
            name = column[0]  # Column name
            data_type = column[1]  # Data type
            is_nullable = "NULL" if column[2] == "YES" else "NOT NULL"  # Nullability
            key = ""  # Initialize key as empty
            if column[3] == "PRI":
                key = "PRIMARY KEY"
            elif column[3] == "UNI":
                key = "UNIQUE"
            extra = column[5]  # Extra info (like auto_increment)

            # Combine all parts into a readable string
            column_info = f"{name} = {data_type} {is_nullable}"
            if key:
                column_info += f" {key}"
            if extra:
                column_info += f" {extra}"

            formatted_columns.append(column_info)
            
        # Close cursor and connection
        cursor.close()
        conn.close()

        # Return results
        return jsonify({"table": table, "columns": formatted_columns}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
def rename_table_controller(token, table, new_table):
    try:
        # Verify and Decode JWT token
        db_name, db_user, user_password = verify_jwt(token)

        # Initiate database connection
        conn = get_connection(db_name, db_user, user_password)
        cursor = conn.cursor()

        # Query database
        query = f"""
        RENAME TABLE `{table}` TO `{new_table}`;
        """
        cursor.execute(query)

        # Close cursor and connection
        cursor.close()
        conn.close()

        # Return results
        return jsonify({"message": f"Table '{table}' renamed to '{new_table}' successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
def drop_table_controller(token, table):
    try:
        # Verify and Decode JWT token
        db_name, db_user, user_password = verify_jwt(token)

        # Initiate database connection
        conn = get_connection(db_name, db_user, user_password)
        cursor = conn.cursor()

        # Query database
        query = f"""
        DROP TABLE `{table}`;
        """
        cursor.execute(query)

        # Close cursor and connection
        cursor.close()
        conn.close()

        # Return results
        return jsonify({"message": f"Table '{table}' dropped successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500