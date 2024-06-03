import mysql.connector
from db_con import connect_to_database
conn=connect_to_database()

def add_author(conn):
    try:
        name=input("please enter name:")
        biography=input("please enter biography:")
        cursor = conn.cursor()
        sql = "INSERT INTO authors (name, biography) VALUES (%s, %s)"
        cursor.execute(sql, (name, biography))
        conn.commit()
        print("Author added successfully.")
    except mysql.connector.Error as e:
        print("Error adding author:", e)


def view_author(conn):
    try:
        author_id=input("please enter author ID:")
        cursor = conn.cursor()
        sql = "SELECT * FROM authors WHERE id = %s"
        cursor.execute(sql, (author_id,))
        author = cursor.fetchone()
        if author:
            print("Author details:")
            print("ID:", author[0])
            print("Name:", author[1])
            print("Biography:", author[2])
        else:
            print("Author not found with ID:", author_id)
    except mysql.connector.Error as e:
        print("Error viewing author details:", e)

def display_authors(conn):
    try:
        cursor = conn.cursor()
        sql = "SELECT * FROM authors"
        cursor.execute(sql)
        authors = cursor.fetchall()
        if authors:
            print("All authors:")
            for author in authors:
                print("ID:", author[0], "Name:", author[1], "Biography:", author[2])
        else:
            print("No authors found.")
    except mysql.connector.Error as e:
        print("Error displaying authors:", e)