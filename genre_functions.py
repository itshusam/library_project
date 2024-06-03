import mysql.connector
from db_con import connect_to_database
conn=connect_to_database()


def add_genre(conn):
    try:
        name=input("please enter name:")
        description=input("please enter the genre description:")
        category=input("please enter the category")
        cursor = conn.cursor()
        sql = "INSERT INTO genres (name, description, category) VALUES (%s, %s, %s)"
        cursor.execute(sql, (name, description, category))
        conn.commit()
        print("Genre added successfully.")
    except mysql.connector.Error as e:
        print("Error adding genre:", e)


def view_genre(conn):
    try:
        genre_id=input("please enter the genre ID :")
        cursor = conn.cursor()
        sql = "SELECT * FROM genres WHERE id = %s"
        cursor.execute(sql, (genre_id,))
        genre = cursor.fetchone()
        if genre:
            print("Genre details:")
            print("ID:", genre[0])
            print("Name:", genre[1])
            print("Description:", genre[2])
            print("Category:", genre[3])
        else:
            print("Genre not found with ID:", genre_id)
    except mysql.connector.Error as e:
        print("Error viewing genre details:", e)

def display_genres(conn):
    try:
        cursor = conn.cursor()
        sql = "SELECT * FROM genres"
        cursor.execute(sql)
        genres = cursor.fetchall()
        if genres:
            print("All genres:")
            for genre in genres:
                print("ID:", genre[0], "Name:", genre[1], "Description:", genre[2], "Category:", genre[3])
        else:
            print("No genres found.")
    except mysql.connector.Error as e:
        print("Error displaying genres:", e)