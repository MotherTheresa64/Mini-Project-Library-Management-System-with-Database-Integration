from models import Book, User, Author
from database import Database

def book_operations(db):
    while True:
        print("\nBook Operations:")
        print("1. Add a new book")
        print("2. Display all books")
        print("3. Return to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter book title: ")
            author_id = int(input("Enter author ID: "))
            
            # Check if author_id exists
            db.cursor.execute("SELECT * FROM authors WHERE id = %s", (author_id,))
            if not db.cursor.fetchone():
                print("Author ID does not exist. Please add the author first.")
                continue
            
            isbn = input("Enter ISBN: ")
            publication_date = input("Enter publication date (YYYY-MM-DD): ")
            book = Book(title, author_id, isbn, publication_date)
            book.add_book(db)
            print("Book added successfully!")
        elif choice == '2':
            books = Book.get_all_books(db)
            for book in books:
                print(book)
        elif choice == '3':
            break
        else:
            print("Invalid choice, please try again.")


def user_operations(db):
    while True:
        print("\nUser Operations:")
        print("1. Add a new user")
        print("2. Display all users")
        print("3. Return to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter user name: ")
            library_id = input("Enter library ID: ")
            user = User(name, library_id)
            user.add_user(db)
            print("User added successfully!")
        elif choice == '2':
            users = User.get_all_users(db)
            for user in users:
                print(user)
        elif choice == '3':
            break
        else:
            print("Invalid choice, please try again.")

def author_operations(db):
    while True:
        print("\nAuthor Operations:")
        print("1. Add a new author")
        print("2. Display all authors")
        print("3. Return to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter author name: ")
            biography = input("Enter author biography: ")
            author = Author(name, biography)
            author.add_author(db)
            print("Author added successfully!")
        elif choice == '2':
            authors = Author.get_all_authors(db)
            for author in authors:
                print(author)
        elif choice == '3':
            break
        else:
            print("Invalid choice, please try again.")
