from library_manager.inventory import LibraryInventory
from library_manager.book import Book

def menu():
    inventory = LibraryInventory()
    inventory.load_from_file()

    while True:
        print("\n--- Library Menu ---")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Search Book By Title")
        print("6. Exit")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                title = input("Title: ")
                author = input("Author: ")
                isbn = input("ISBN: ")
                inventory.add_book(Book(title, author, isbn))
                inventory.save_to_file()
                print("Book Added Successfully!")

            elif choice == "2":
                isbn = input("Enter ISBN to issue: ")
                book = inventory.search_by_isbn(isbn)
                if book and book.issue():
                    inventory.save_to_file()
                    print("Book Issued.")
                else:
                    print("Cannot issue book.")

            elif choice == "3":
                isbn = input("Enter ISBN to return: ")
                book = inventory.search_by_isbn(isbn)
                if book and book.return_book():
                    inventory.save_to_file()
                    print("Book Returned.")
                else:
                    print("Cannot return book.")

            elif choice == "4":
                for b in inventory.display_all():
                    print(b)

            elif choice == "5":
                t = input("Enter title to search: ")
                results = inventory.search_by_title(t)
                if results:
                    for r in results:
                        print(r)
                else:
                    print("No books found.")

            elif choice == "6":
                print("Goodbye!")
                break

            else:
                print("Invalid choice!")

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    menu()
