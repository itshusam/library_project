import mysql.connector
from db_con import connect_to_database
conn=connect_to_database()

def add_user(conn):
    try:
        name=input("please enter name")
        library_id=input("please enter library ID")
        cursor = conn.cursor()
        sql = "INSERT INTO users (name, library_id) VALUES (%s, %s)"
        cursor.execute(sql, (name, library_id))
        conn.commit()
        print("User added successfully.")
    except mysql.connector.Error as e:
        print("Error adding user:", e)


def view_user(conn):
    try:
        user_id=input("please enter the ID of the user you want to view")
        cursor = conn.cursor()
        sql = "SELECT * FROM users WHERE id = %s"
        cursor.execute(sql, (user_id,))
        user = cursor.fetchone()
        if user:
            print("User details:")
            print("ID:", user[0])
            print("Name:", user[1])
            print("Library ID:", user[2])
        else:
            print("User not found with ID:", user_id)
    except mysql.connector.Error as e:
        print("Error viewing user details:", e)


def display_users(conn):
    try:
        cursor = conn.cursor()
        sql = "SELECT * FROM users"
        cursor.execute(sql)
        users = cursor.fetchall()
        if users:
            print("All users:")
            for user in users:
                print("ID:", user[0], "Name:", user[1], "Library ID:", user[2])
        else:
            print("No users found.")
    except mysql.connector.Error as e:
        print("Error displaying users:", e)