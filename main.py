import mysql.connector
from db_con import connect_to_database
from books_functions import *
from authors_functions import *
from users_functions import *
from genre_functions import *




conn=connect_to_database()


def book_operations():
    while True:
        print("\nBook Operations:")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Search for a book")
        print("5. Display all books")
        print("6. Back to Main Menu")

        choice = input("Select an option: ")
        if choice == '1':
            add_book(conn)
        elif choice == '2':
            borrow_book(conn)
        elif choice == '3':
            return_book(conn)
        elif choice == '4':
            search_menu()
        elif choice == '5':
            display_books(conn)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

def user_operations():
    while True:
        print("\nUser Operations:")
        print("1. Add a new user")
        print("2. View user details")
        print("3. Display all users")
        print("4. Back to Main Menu")

        choice = input("Select an option: ")
        if choice == '1':
            add_user(conn)
        elif choice == '2':
            view_user(conn)
        elif choice == '3':
            display_users(conn)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def author_operations():
    while True:
        print("\nAuthor Operations:")
        print("1. Add a new author")
        print("2. View author details")
        print("3. Display all authors")
        print("4. Back to Main Menu")

        choice = input("Select an option: ")
        if choice == '1':
            add_author(conn)
        elif choice == '2':
            view_author(conn)
        elif choice == '3':
            display_authors(conn)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def genre_operations():
        while True:
            print("\nGenre Operations:")
            print("1. Add a new genre")
            print("2. View genre details")
            print("3. Display all genres")
            print("4. Back to Main Menu")

            choice = input("Select an option: ")
            if choice == '1':
                add_genre(conn)
            elif choice == '2':
                view_genre(conn)
            elif choice == '3':
                display_genres(conn)
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")
while True:
    print("\nWelcome to the Library Management System!")
    print("Main Menu:")
    print("1. Book Operations")
    print("2. User Operations")
    print("3. Author Operations")
    print("4. Genre Operations")
    print("5. Quit")

    choice = input("Select an option: ")
    if choice == '1':
        book_operations()
    elif choice == '2':
        user_operations()
    elif choice == '3':
        author_operations()
    elif choice == '4':
        genre_operations()
    elif choice == '5':
        print("Exiting the Library Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")