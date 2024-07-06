class Book:
    def __init__(self, book_id, title, author, genre, publication_date):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_date = publication_date
        self.is_borrowed = False

    def borrow_book(self):
        if self.is_borrowed:
            print(f"The book '{self.title}' is already borrowed.")
        else:
            self.is_borrowed = True
            print(f"You have successfully borrowed The book '{self.title}' ")

    def return_book(self):
        if not self.is_borrowed:
            print(f"The book '{self.title}' is available to be borrow.")
        else:
            self.is_borrowed = False
            print(f"The book '{self.title}' has been returned.")

    def __str__(self):
        return f"\nBook ID: {self.book_id} \nTitle: {self.title} \nAuthor: {self.author} \nGenre: {self.genre} \nPublished: {self.publication_date} \nStatus: {'Borrowed' if self.is_borrowed else 'Available'}"

class BookManager:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, title, author, genre, publication_date):
        if book_id in self.books:
            print(f"Book with ID {book_id} already exists.")
            return
        new_book = Book(book_id, title, author, genre, publication_date)
        self.books[book_id] = new_book
        print(f"Book '{title}' added successfully.")

    def search_book(self, book_id):
        return self.books.get(book_id, None)

    def display_all_books(self):
        if not self.books:
            print("No books available.")
            return
        for book in self.books.values():
            print(book)

# # To test the Book module:
# if __name__ == "__main__":
#     book_manager = BookManager()
#     book_manager.add_book(1, "1984", "George Orwell", "Dystopian", "1949-06-08")
#     book_manager.add_book(2, "To Kill a Mockingbird", "Harper Lee", "Fiction", "1960-07-11")
#     book_manager.display_all_books()
#     book = book_manager.search_book(1)
#     if book:
#         book.borrow_book()
#         book.return_book()
