from src.MySQL.db import get_db_connection

def fetch_data_from_db():

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute('SELECT * FROM your_table LIMIT 5')
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows

def add_data_to_db(name, age):

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('INSERT INTO your_table (name, age) VALUES (%s, %s)', (name, age))
    conn.commit()

    cursor.close()
    conn.close()
