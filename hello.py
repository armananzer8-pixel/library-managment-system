class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

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
            for book in self.borrowed_books:
                print(book.title)


class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            book.display()

    def borrow_book(self, user, title):

        for book in self.books:

            if book.title == title and book.available:
                book.available = False
                user.borrowed_books.append(book)

                print("Book Borrowed Successfully")
                return

        print("Book Not Available")

    def return_book(self, user, title):

        for book in user.borrowed_books:

            if book.title == title:
                book.available = True
                user.borrowed_books.remove(book)

                print("Book Returned")
                return

        print("Book Not Found")


# Create library
library = Library()

# Create books
book1 = Book("Python Basics", "John")
book2 = Book("Data Structures", "Alice")

# Add books
library.add_book(book1)
library.add_book(book2)

# Create user
user = User("Arman")

# Display books
library.display_books()

# Borrow book
library.borrow_book(user, "Python Basics")

# Show user's borrowed books
user.show_books()

# Return book
library.return_book(user, "Python Basics")

# Show books again
user.show_books()