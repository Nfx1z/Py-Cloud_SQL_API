from src.db import get_db_uri

def fetch_data_from_db(query, table):
    try:
        conn = get_db_uri()
    except Exception as e:
        return f'Error connecting to database: {str(e)}'
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute(f'SELECT * FROM {table} LIMIT 5')
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows

def add_data_to_db(name, age):

    conn = get_db_uri()
    cursor = conn.cursor()

    cursor.execute('INSERT INTO your_table (name, age) VALUES (%s, %s)', (name, age))
    conn.commit()

    cursor.close()
    conn.close()
