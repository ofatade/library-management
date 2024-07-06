class Author:
    def __init__(self, author_id, name, biography):
        self.__author_id = author_id
        self.__name = name
        self.__biography = biography

    def get_author_id(self):
        return self.__author_id

    def get_name(self):
        return self.__name

    def get_biography(self):
        return self.__biography

    def __str__(self):
        return f"Author ID: {self.__author_id} \nName: {self.__name} \nBiography: {self.__biography}"

class AuthorManager:
    def __init__(self):
        self.authors = {}

    def add_author(self, author_id, name, biography):
        if author_id in self.authors:
            print(f"Author with ID {author_id} already exists.")
            return
        new_author = Author(author_id, name, biography)
        self.authors[author_id] = new_author
        print(f"Author '{name}' added successfully.")

    def view_author_details(self, author_id):
        if author_id not in self.authors:
            print(f"Author with ID {author_id} not found.")
            return
        author = self.authors[author_id]
        print(author)

    def display_all_authors(self):
        if not self.authors:
            print("No authors available.")
            return
        for author in self.authors.values():
            print(author)

# To test the Author module:
# if __name__ == "__main__":
#     author_manager = AuthorManager()
#     author_manager.add_author(1, "George Orwell", "George Orwell was an English novelist, essayist, journalist and critic.")
#     author_manager.add_author(2, "J.K. Rowling", "J.K. Rowling is a British author, best known for writing the Harry Potter series.")
#     author_manager.display_all_authors()
#     author_manager.view_author_details(1)
