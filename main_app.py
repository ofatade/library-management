from book import BookManager
from user import UserManager
from author import AuthorManager

def main():
    book_manager = BookManager()
    user_manager = UserManager()
    author_manager = AuthorManager()

    while True:
        print('''
Welcome to the Library Management System!

Main Menu:
1. Book Operations
2. User Operations
3. Author Operations
4. Quit
''')
        choice = input("Enter your choice: ")
        
        if choice == '1':
            book_operations(book_manager)
        elif choice == '2':
            user_operations(user_manager)
        elif choice == '3':
            author_operations(author_manager)
        elif choice == '4':
            print("Quitting the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

def book_operations(book_manager):
    while True:
        print('''
Book Operations:
1. Add a new book
2. Borrow a book
3. Return a book
4. Search for a book
5. Display all books
6. Back to Main Menu
''')
        choice = input("Enter your choice: ")
        
        if choice == '1':
            book_id = int(input("Enter book ID: "))
            title = input("Enter book title: ")
            author = input("Enter author: ")
            genre = input("Enter genre: ")
            publication_date = input("Enter publication date (YYYY-MM-DD): ")
            book_manager.add_book(book_id, title, author, genre, publication_date)
        elif choice == '2':
            book_id = int(input("Enter book ID to borrow: "))
            book = book_manager.search_book(book_id)
            if book:
                book.borrow_book()
            else:
                print("Book not found.")
        elif choice == '3':
            book_id = int(input("Enter book ID to return: "))
            book = book_manager.search_book(book_id)
            if book:
                book.return_book()
            else:
                print("Book not found.")
        elif choice == '4':
            book_id = int(input("Enter book ID to search: "))
            book = book_manager.search_book(book_id)
            if book:
                print(book)
            else:
                print("Book not found.")
        elif choice == '5':
            book_manager.display_all_books()
        elif choice == '6':
            break
        else:
            print("Invalid choice, please try again.")

def user_operations(user_manager):
    while True:
        print('''
User Operations:
1. Add a new user
2. View user details
3. Display all users
4. Back to Main Menu
''')
        choice = input("Enter your choice: ")
        
        if choice == '1':
            user_id = int(input("Enter user ID: "))
            name = input("Enter user name: ")
            email = input("Enter user email: ")
            user_manager.add_user(user_id, name, email)
        elif choice == '2':
            user_id = int(input("Enter user ID to view: "))
            user_manager.view_user_details(user_id)
        elif choice == '3':
            user_manager.display_all_users()
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")

def author_operations(author_manager):
    while True:
        print('''
Author Operations:
1. Add a new author
2. View author details
3. Display all authors
4. Back to Main Menu
''')
        choice = input("Enter your choice: ")
        
        if choice == '1':
            author_id = int(input("Enter author ID: "))
            name = input("Enter author name: ")
            biography = input("Enter author biography: ")
            author_manager.add_author(author_id, name, biography)
        elif choice == '2':
            author_id = int(input("Enter author ID to view: "))
            author_manager.view_author_details(author_id)
        elif choice == '3':
            author_manager.display_all_authors()
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
