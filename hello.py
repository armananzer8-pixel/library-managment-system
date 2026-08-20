import json
import os


class Book:

    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    def display(self):
        status = "Available" if self.available else "Borrowed"
        print(f"{self.title} by {self.author} - {status}")


class User:

    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def show_books(self):
        if not self.borrowed_books:
            print("No books borrowed.")
        else:
            print("\nYour Borrowed Books:")
            for book in self.borrowed_books:
                print(f"- {book.title}")


class Library:

    def __init__(self, data_file="books.json"):
        self.books = []
        self.data_file = data_file

    # Add a book
    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully.")

    # Display all books
    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return

        print("\n===== LIBRARY BOOKS =====")

        for book in self.books:
            book.display()

    # Borrow a book
    def borrow_book(self, user, title):

        for book in self.books:

            if book.title.lower() == title.lower():

                if book.available:
                    book.available = False
                    user.borrowed_books.append(book)

                    print("Book borrowed successfully.")
                    self.save_data()
                    return

                else:
                    print("Book is already borrowed.")
                    return

        print("Book not found.")

    # Return a book
    def return_book(self, user, title):

        for book in user.borrowed_books:

            if book.title.lower() == title.lower():

                book.available = True
                user.borrowed_books.remove(book)

                print("Book returned successfully.")
                self.save_data()
                return

        print("You haven't borrowed this book.")

    # Delete a book
    def delete_book(self, title):

        for book in self.books:

            if book.title.lower() == title.lower():

                if not book.available:
                    print("Cannot delete a borrowed book.")
                    return

                self.books.remove(book)
                print("Book deleted successfully.")
                self.save_data()
                return

        print("Book not found.")

    # Find / search books by title or author (case-insensitive substring)
    def search_books(self, query):
        if not query or not query.strip():
            print("Search query cannot be empty.")
            return []

        needle = query.strip().lower()
        results = [
            book for book in self.books
            if needle in book.title.lower() or needle in book.author.lower()
        ]

        if not results:
            print(f'No books found matching "{query}".')
            return []

        print(f'\n===== SEARCH RESULTS FOR "{query}" =====')
        for book in results:
            book.display()
        print(f"{len(results)} match(es) found.")
        return results

    # Search helper (kept from earlier fix)
    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    # Save books to JSON
    def save_data(self):

        data = []

        for book in self.books:

            data.append({
                "title": book.title,
                "author": book.author,
                "available": book.available
            })

        with open(self.data_file, "w") as file:
            json.dump(data, file, indent=4)

    # Load books from JSON
    def load_data(self):

        if not os.path.exists(self.data_file):
            print("No saved library data found.")
            print("Starting with an empty library.")
            return

        try:

            with open(self.data_file, "r") as file:
                data = json.load(file)

            self.books = [
                Book(item["title"], item["author"], item.get("available", True))
                for item in data
            ]

        except (json.JSONDecodeError, KeyError) as e:
            print(f"Saved data is corrupted ({e}). Starting with an empty library.")
            self.books = []


# =========================
# Main Program
# =========================

if __name__ == "__main__":

    library = Library()
    library.load_data()
    user = User("Arman")

    while True:

        print("\n==============================")
        print("   LIBRARY MANAGEMENT SYSTEM")
        print("==============================")

        print("1. Display Books")
        print("2. Add Book")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. My Borrowed Books")
        print("6. Delete Book")
        print("7. Find Book")
        print("8. Exit")

        choice = input("\nEnter your choice: ")

        # Display books
        if choice == "1":
            library.display_books()

        # Add book
        elif choice == "2":
            title = input("Enter book title: ").strip()
            author = input("Enter author name: ").strip()
            if not title or not author:
                print("Title and author cannot be empty.")
                continue
            book = Book(title, author)
            library.add_book(book)
            library.save_data()

        # Borrow book
        elif choice == "3":
            title = input("Enter book title to borrow: ").strip()
            library.borrow_book(user, title)

        # Return book
        elif choice == "4":
            title = input("Enter book title to return: ").strip()
            library.return_book(user, title)

        # Show borrowed books
        elif choice == "5":
            user.show_books()

        # Delete book
        elif choice == "6":
            title = input("Enter book title to delete: ").strip()
            library.delete_book(title)

        # Find / search book
        elif choice == "7":
            query = input("Search by title or author: ").strip()
            library.search_books(query)

        # Exit
        elif choice == "8":
            library.save_data()
            print("Library data saved.")
            print("Thank you for using the Library Management System!")
            break

        else:
            print("Invalid choice. Please enter 1-8.")
