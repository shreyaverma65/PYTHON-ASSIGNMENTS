import unittest
from library_manager.book import Book
from library_manager.inventory import LibraryInventory

class TestBook(unittest.TestCase):

    def test_book_initialization(self):
        book = Book("Python 101", "Guido", "12345")
        self.assertEqual(book.title, "Python 101")
        self.assertEqual(book.status, "available")

    def test_issue_book(self):
        book = Book("Python 101", "Guido", "12345")
        book.issue()
        self.assertEqual(book.status, "issued")

    def test_return_book(self):
        book = Book("Python 101", "Guido", "12345")
        book.issue()
        book.return_book()
        self.assertEqual(book.status, "available")

class TestInventory(unittest.TestCase):

    def setUp(self):
        self.inventory = LibraryInventory()
        self.book = Book("Python 101", "Guido", "12345")
        self.inventory.add_book(self.book)

    def test_add_book(self):
        self.assertEqual(len(self.inventory.books), 1)

    def test_search_by_title(self):
        result = self.inventory.search_by_title("Python")
        self.assertEqual(result[0].title, "Python 101")

    def test_search_by_isbn(self):
        result = self.inventory.search_by_isbn("12345")
        self.assertEqual(result.title, "Python 101")

if __name__ == '__main__':
    unittest.main()
