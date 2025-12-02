import json
from pathlib import Path
from .book import Book

class LibraryInventory:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def search_by_title(self, title):
        return [b for b in self.books if title.lower() in b.title.lower()]

    def search_by_isbn(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    def display_all(self):
        return [str(book) for book in self.books]

    # Save to JSON
    def save_to_file(self, filename="catalog.json"):
        data = [book.to_dict() for book in self.books]
        try:
            with open(filename, "w") as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            print("Error saving file:", e)

    # Load from JSON
    def load_from_file(self, filename="catalog.json"):
        try:
            file_path = Path(filename)
            if not file_path.exists():
                self.books = []
                return

            with open(filename, "r") as f:
                data = json.load(f)

            self.books = [Book(**item) for item in data]

        except Exception:
            print("Error reading file — file may be corrupted.")
            self.books = []
