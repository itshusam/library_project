import mysql.connector
from mysql.connector import Error

# Connect to MySQL database
def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="library"
        )
        
        return conn
    except mysql.connector.Error as e:
        print("Error connecting to the database:", e)
        return None
    


def close_connection(conn):
    if conn:
        conn.close()

conn=connect_to_database()
