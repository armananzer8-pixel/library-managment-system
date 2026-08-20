import json


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

    def __init__(self):
        self.books = []

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

    # Save books to JSON
    def save_data(self):

        data = []

        for book in self.books:

            data.append({
                "title": book.title,
                "author": book.author,
                "available": book.available
            })

        with open("books.json", "w") as file:
            json.dump(data, file, indent=4)

    # Load books from JSON
    def load_data(self):

        try:

            with open("books.json", "r") as file:
                data = json.load(file)

            for item in data:

                book = Book(
                    item["title"],
                    item["author"],
                    item["available"]
                )

                self.books.append(book)

        except FileNotFoundError:

            print("No saved library data found.")
            print("Starting with an empty library.")


# =========================
# Main Program
# =========================

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
    print("7. Exit")

    choice = input("\nEnter your choice: ")

    # Display books
    if choice == "1":

        library.display_books()

    # Add book
    elif choice == "2":

        title = input("Enter book title: ")
        author = input("Enter author name: ")

        book = Book(title, author)

        library.add_book(book)
        library.save_data()

    # Borrow book
    elif choice == "3":

        title = input("Enter book title to borrow: ")

        library.borrow_book(user, title)

    # Return book
    elif choice == "4":

        title = input("Enter book title to return: ")

        library.return_book(user, title)

    # Show borrowed books
    elif choice == "5":

        user.show_books()

    # Delete book
    elif choice == "6":

        title = input("Enter book title to delete: ")

        library.delete_book(title)

    # Exit
    elif choice == "7":

        library.save_data()

        print("Library data saved.")
        print("Thank you for using the Library Management System!")

        break

    else:

        print("Invalid choice. Please enter 1-7.")