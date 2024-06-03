import mysql.connector
from db_con import connect_to_database
conn=connect_to_database()

# Function to search for books by ISBN
def search_books_by_isbn(conn, isbn):
    try:
        cursor = conn.cursor()
        sql = "SELECT * FROM books WHERE isbn = %s"
        cursor.execute(sql, (isbn,))
        books = cursor.fetchall()
        if books:
            print("Books found with ISBN:", isbn)
            for book in books:
                print(book)
        else:
            print("No books found with ISBN:", isbn)
    except mysql.connector.Error as e:
        print("Error searching books by ISBN:", e)

# Function to search for books by title
def search_books_by_title(conn, title):
    try:
        cursor = conn.cursor()
        sql = "SELECT * FROM books WHERE title LIKE %s"
        cursor.execute(sql, ('%' + title + '%',))
        books = cursor.fetchall()
        if books:
            print("Books found with title containing:", title)
            for book in books:
                print(book)
        else:
            print("No books found with title containing:", title)
    except mysql.connector.Error as e:
        print("Error searching books by title:", e)

# Function to search for books by author
def search_books_by_author(conn, author_name):
    try:
        cursor = conn.cursor()
        sql = "SELECT books.* FROM books INNER JOIN authors ON books.author_id = authors.id WHERE authors.name LIKE %s"
        cursor.execute(sql, ('%' + author_name + '%',))
        books = cursor.fetchall()
        if books:
            print("Books found by author:", author_name)
            for book in books:
                print(book)
        else:
            print("No books found by author:", author_name)
    except mysql.connector.Error as e:
        print("Error searching books by author:", e)

# Function to search for books by genre
def search_books_by_genre(conn, genre_name):
    try:
        cursor = conn.cursor()
        sql = "SELECT books.* FROM books INNER JOIN genres ON books.genre_id = genres.id WHERE genres.name LIKE %s"
        cursor.execute(sql, ('%' + genre_name + '%',))
        books = cursor.fetchall()
        if books:
            print("Books found in genre:", genre_name)
            for book in books:
                print(book)
        else:
            print("No books found in genre:", genre_name)
    except mysql.connector.Error as e:
        print("Error searching books by genre:", e)