import mysql.connector
from db_con import connect_to_database
from search import *
conn=connect_to_database()


def add_book(conn):
    try:
        title=input("please enter the book title!")
        author_id=input("please enter author ID!")
        genre_id=input("please enter genre ID")
        isbn=input("please enter isbn")
        publication_date=input("Enter the publication date (YYYY-MM-DD): ")
        cursor = conn.cursor()
        sql = "INSERT INTO books (title, author_id, genre_id, isbn, publication_date) VALUES (%s, %s, %s, %s, %s)"
        val = (title, author_id, genre_id, isbn, publication_date)
        cursor.execute(sql, val)
        conn.commit()
        print("Book added successfully.")
    except mysql.connector.Error as e:
        print("Error adding book:", e)


def display_books(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
        for book in books:
            print(book)
    except mysql.connector.Error as e:
        print("Error fetching books:", e)


def borrow_book(conn):
    try:
        user_id=input("please enter user ID :")
        book_id=input("please enter book ID :")
        borrow_date=input("please enter borrow date (YYYY-MM-DD):")
        cursor = conn.cursor()
        # Insert a record into borrowed_books
        sql_borrow = "INSERT INTO borrowed_books (user_id, book_id, borrow_date) VALUES (%s, %s, %s)"
        cursor.execute(sql_borrow, (user_id, book_id, borrow_date))
        
        # Update the book's availability
        sql_update = "UPDATE books SET availability = 0 WHERE id = %s"
        cursor.execute(sql_update, (book_id,))
        
        conn.commit()
        print("Book marked as borrowed successfully.")
    except mysql.connector.Error as e:
        conn.rollback()
        print("Error marking book as borrowed:", e)

def return_book(conn):
    try:
        book_id=input("please enter book ID :")
        return_date=input("please enter return date (YYYY-MM-DD):")
        cursor = conn.cursor()
        # Update the return date in borrowed_books
        sql_return = "UPDATE borrowed_books SET return_date = %s WHERE book_id = %s AND return_date IS NULL"
        cursor.execute(sql_return, (return_date, book_id))
        
        # Update the book's availability
        sql_update = "UPDATE books SET availability = 1 WHERE id = %s"
        cursor.execute(sql_update, (book_id,))
        
        conn.commit()
        print("Book marked as returned successfully.")
    except mysql.connector.Error as e:
        conn.rollback()
        print("Error marking book as returned:", e)


def search_menu():
        print("\nSearch Menu:")
        print("1. Search by ISBN")
        print("2. Search by Title")
        print("3. Search by Author")
        print("4. Search by Genre")
        print("5. Quit")

        while True:
        
            choice = input("Please select an option (1-5): ")

            if choice == '1':
                isbn = input("Enter the ISBN: ")
                search_books_by_isbn(conn, isbn)
            elif choice == '2':
                title = input("Enter the title (or part of it): ")
                search_books_by_title(conn, title)
            elif choice == '3':
                author_name = input("Enter the author name (or part of it): ")
                search_books_by_author(conn, author_name)
            elif choice == '4':
                genre_name = input("Enter the genre name (or part of it): ")
                search_books_by_genre(conn, genre_name)
            elif choice == '5':
                print("Exiting the search menu.")
                break
            else:
                print("Invalid choice. Please select a valid option.")

