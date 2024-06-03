Library Management System with Database Integration
Introduction
This Library Management System is a command-line application designed to manage books, users, authors, and genres in a library. The system integrates with a MySQL database to store and retrieve data, ensuring data persistence and scalability.

Features
Book Operations:

Add a new book
Borrow a book
Return a book
Search for a book
Display all books
User Operations:

Add a new user
View user details
Display all users
Author Operations:

Add a new author
View author details
Display all authors
Genre Operations:

Add a new genre
View genre details
Display all genres

Book Operations
Add a New Book:

Prompts for title, author ID, genre ID, ISBN, and publication date.
Borrow a Book:

Prompts for user ID, book ID, and borrow date.
Return a Book:

Prompts for user ID, book ID, and return date.
Search for a Book:

Options to search by ISBN, title, author, or genre.
Display All Books:

Lists all books in the library.
User Operations
Add a New User:

Prompts for name and library ID.
View User Details:

Prompts for user ID to display user details.
Display All Users:

Lists all users in the library.
Author Operations
Add a New Author:

Prompts for name and biography.
View Author Details:

Prompts for author ID to display author details.
Display All Authors:

Lists all authors in the library.
Genre Operations
Add a New Genre:

Prompts for name, description, and category.
View Genre Details:

Prompts for genre ID to display genre details.
Display All Genres:

Lists all genres in the library.


Error Handling
The application uses try-except blocks to handle errors gracefully. Common errors such as foreign key constraint violations, invalid input, and database connection issues are managed to provide informative messages to the user.

Clean Code Principles
Meaningful variable and function names to convey purpose.
Clear comments and docstrings to explain functionality.
PEP 8 style guidelines for code formatting and structure.
Proper indentation and spacing for readability.


Modular Design
The code is organized into separate modules to promote modularity and maintainability. This includes distinct modules for database operations, user interactions, error handling, and core functionalities.

Conclusion
This Library Management System provides a comprehensive and user-friendly interface for managing library operations. By integrating with a MySQL database, it ensures data persistence and scalability, making it suitable for real-world applications.
