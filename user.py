class User:
    def __init__(self, user_id, name, email):
        self.__user_id = user_id
        self.__name = name
        self.__email = email
        self.borrowed_books = []

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def borrow_book(self, book):
        if book.is_borrowed:
            print(f"The book '{book.title}' is already borrowed.")
        else:
            book.borrow_book()
            self.borrowed_books.append(book)

    def return_book(self, book):
        if book not in self.borrowed_books:
            print(f"The book '{book.title}' was not borrowed by {self.__name}.")
        else:
            book.return_book()
            self.borrowed_books.remove(book)

    def __str__(self):
        return f"User ID: {self.__user_id} \nName: {self.__name} \nEmail: {self.__email} \nBorrowed Books: {[book.title for book in self.borrowed_books]}"

class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, user_id, name, email):
        if user_id in self.users:
            print(f"User with ID {user_id} already exists.")
            return
        new_user = User(user_id, name, email)
        self.users[user_id] = new_user
        print(f"User '{name}' added successfully.")

    def view_user_details(self, user_id):
        if user_id not in self.users:
            print(f"User with ID {user_id} not found.")
            return
        user = self.users[user_id]
        print(user)

    def display_all_users(self):
        if not self.users:
            print("No users available.")
            return
        for user in self.users.values():
            print(user)

# # To test the User module:
# if __name__ == "__main__":
#     user_manager = UserManager()
#     user_manager.add_user(1, "Alice", "alice@example.com")
#     user_manager.add_user(2, "Bob", "bob@example.com")
#     user_manager.display_all_users()
#     user_manager.view_user_details(1)
