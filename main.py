from menu import book_operations, user_operations, author_operations
from database import Database

def main_menu():
    db = Database()
    while True:
        print("\nWelcome to the Library Management System with Database Integration!")
        print("**** Main Menu ****")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Quit")
        choice = input("Choose an option: ")

        if choice == '1':
            book_operations(db)
        elif choice == '2':
            user_operations(db)
        elif choice == '3':
            author_operations(db)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()
