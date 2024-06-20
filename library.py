from book import Book


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        if not isinstance(book, Book):
            raise ValueError("Invalid book object")
        self.books[book.title.lower()] = book

    def remove_book(self, title):
        if not self.books:
            print("No books in the library")
        else:
            try:
                del self.books[title.lower()]
            except KeyError:
                print(f"Book '{title}' not found")

    def display_books(self):
        if not self.books:
            print("No books in the library")
        else:
            for book in self.books.values():
                print(book)

    def search_book(self, title):
        if not self.books:
            self.display_books()
        else:
            books = [
                book
                for book in self.books.values()
                if book.title.lower() == title.lower()
            ]
            if not books:
                print(f"No books found with title '{title}'")
            else:
                for book in books:
                    print(book)
