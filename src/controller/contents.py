from flask import jsonify
from src.utils.cookies import verify_jwt
from src.db import get_connection

def get_contents_controller(token, table):
    try:
        # Verify and Decode JWT token
        db_name, db_user, user_password = verify_jwt(token)

        # Initiate database connection
        conn = get_connection(db_name, db_user, user_password)
        cursor = conn.cursor()

        # Query database
        query = f"""
        SELECT * FROM {table};
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
            return jsonify({"error": f"No data found in table '{table}'"}), 404
        
        # Return results
        return jsonify({"table": table, "contents": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def insert_contents_controller(token, request):
    try:
        # Get table name and columns
        table = request.json.get('table')
        columns = request.json.get('columns')
        values = request.json.get('values')

        # Validate input parameters
        if not table or not columns or not values:
            return jsonify({"error": "Both 'table', 'columns', and 'values' are required"}), 400
        
        # Verify and Decode JWT token
        db_name, db_user, user_password = verify_jwt(token)

        # Initiate database connection
        conn = get_connection(db_name, db_user, user_password)
        cursor = conn.cursor()

        # Construct the INSERT INTO query using a loop
        column_names = ", ".join(columns)
        value_placeholders = ", ".join(["%s"] * len(columns))

        # Execute the query
        query = f"""        
        INSERT INTO {table} ({column_names}) VALUES ({value_placeholders});
        """
        cursor.executemany(query, values)

        # Commit the transaction
        conn.commit()

        # Close cursor and connection
        cursor.close()
        conn.close()

        # Return results
        return jsonify({"message": f"{cursor.rowcount} rows inserted successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
def update_contents_controller(token, request):
    try:
        # Get table name and columns
        table = request.json.get('table')
        data = request.json.get('data')
        conditions = request.json.get('conditions')

        # Validate input parameters
        if not table or not conditions or not data:
            return jsonify({"error": "Both 'table', 'conditions', and 'data' are required"}), 400
        
        # Verify and Decode JWT token
        db_name, db_user, user_password = verify_jwt(token)

        # Initiate database connection
        conn = get_connection(db_name, db_user, user_password)
        rows = conn.cursor()
        
        # Construct the SET part of the UPDATE query dynamically
        set_clause = ", ".join([f"{key} = %s" for key in data.keys()])
        
        # Construct the WHERE part of the UPDATE query dynamically
        where_clause = " AND ".join([f"{key} = %s" for key in conditions.keys()])
        
        # Final query
        query = f"UPDATE {table} SET {set_clause} WHERE {where_clause}"
        
        # Collect the new values for the SET clause and the WHERE clause
        values = list(data.values()) + list(conditions.values())

        # Execute the query
        rows.execute(query, values)
        
        # Commit the transaction
        conn.commit()
        
        # Close cursor and connection
        rows.close()
        conn.close()
        
        # Return results
        return jsonify({"message": f"{rows.rowcount} rows updated successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
def delete_contents_controller(token, request):
    try:
        # Get table name and columns
        table = request.json.get('table')
        conditions = request.json.get('conditions')

        # Validate input parameters
        if not table or not conditions:
            return jsonify({"error": "Both 'table' and 'conditions' are required"}), 400
        
        # Verify and Decode JWT token
        db_name, db_user, user_password = verify_jwt(token)

        # Initiate database connection
        conn = get_connection(db_name, db_user, user_password)
        rows = conn.cursor()
        
        # Construct the WHERE part of the DELETE query dynamically
        where_clause = " AND ".join([f"{key} = %s" for key in conditions.keys()])
        
        # Final query
        query = f"DELETE FROM {table} WHERE {where_clause}"
        
        # Collect the new values for the WHERE clause
        values = list(conditions.values())

        # Execute the query
        rows.execute(query, values)
        
        # Commit the transaction
        conn.commit()
        
        # Close cursor and connection
        rows.close()
        conn.close()
        
        # Return results
        return jsonify({"message": f"{rows.rowcount} rows deleted successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
def search_contents_controller(token, request):
    try:
        # Get table name and columns
        table = request.json.get('table')
        conditions = request.json.get('conditions')

        # Validate input parameters
        if not table or not conditions:
            return jsonify({"error": "Both 'table' and 'conditions' are required"}), 400
        
        # Verify and Decode JWT token
        db_name, db_user, user_password = verify_jwt(token)

        # Initiate database connection
        conn = get_connection(db_name, db_user, user_password)
        rows = conn.cursor()
        
        # Construct the WHERE part of the DELETE query dynamically
        where_clause = " AND ".join([f"{key} = %s" for key in conditions.keys()])
        
        # Final query
        query = f"SELECT * FROM {table} WHERE {where_clause}"
        
        # Collect the new values for the WHERE clause
        values = list(conditions.values())

        # Execute the query
        rows.execute(query, values)
        
        # Commit the transaction
        conn.commit()
        
        # Close cursor and connection
        rows.close()
        conn.close()
        
        # Return results
        return jsonify(rows.fetchall()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500