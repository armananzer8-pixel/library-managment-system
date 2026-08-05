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

library = Library()

book1 = "Book"("Python Basics", "John")
book2 = "Book"("Data Structures", "Alice")

library.add_book(book1)
library.add_book(book2)

user = User("Arman")

library.display_books()

library.borrow_book(user, "Python Basics")

user.show_books()

library.return_book(user, "Python Basics")