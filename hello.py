def update_book(books, title):

    book = next((book for book in books if book.get("title") == title), None)

    if book is None:
        print("Book not found.")
        return

    new_author = input("Enter new author: ").strip()

    if not new_author:
        print("Author cannot be empty.")
        return

    book["author"] = new_author

    print("Book updated successfully!")

    book["author"] = new_author