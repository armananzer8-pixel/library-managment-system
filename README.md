# 📚 LBMS — Library Management System

A simple **Library Management System built using Python, Object-Oriented Programming (OOP), and JSON**.

The project allows users to manage books by adding, displaying, borrowing, returning, and deleting books. Library data is stored in a JSON file so that it can be loaded again when the program starts.

---

## 🚀 Features

* 📖 Display all books
* ➕ Add new books
* 📚 Borrow books
* 🔄 Return books
* 👤 View borrowed books
* 🗑️ Delete books
* 💾 Save book data to JSON
* 📂 Load saved book data from JSON
* ⚠️ Handle missing JSON files

---

## 🛠️ Technologies Used

* Python
* Object-Oriented Programming (OOP)
* JSON
* Git
* GitHub

---

## 📂 Project Structure

```text
LBMS/
│
├── hello.py
├── books.json
└── README.md
```

### `hello.py`

Contains the main Library Management System program.

### `books.json`

Stores the library's book information.

### `README.md`

Contains information and documentation about the project.

---

## 🧠 OOP Concepts Used

### Book Class

The `Book` class stores:

* Book title
* Author name
* Book availability

### User Class

The `User` class stores:

* User name
* Borrowed books

### Library Class

The `Library` class manages:

* Adding books
* Displaying books
* Borrowing books
* Returning books
* Deleting books
* Saving data
* Loading data

---

## 💾 JSON Data Storage

The project uses JSON to store library data.

Example:

```json
[
    {
        "title": "Python Basics",
        "author": "John",
        "available": true
    },
    {
        "title": "Data Structures",
        "author": "Alice",
        "available": true
    }
]
```

### Reading JSON

The program uses:

```python
json.load()
```

to read data from `books.json`.

### Saving JSON

The program uses:

```python
json.dump()
```

to save changes to `books.json`.

---

## ▶️ How to Run

### 1. Make sure Python is installed

Check your Python version:

```bash
python --version
```

### 2. Open the project in VS Code

Open the `LBMS` folder in VS Code.

### 3. Run the program

Open the VS Code terminal and run:

```bash
python hello.py
```

---

## 🎮 Menu

When the program starts, you will see:

```text
==============================
   LIBRARY MANAGEMENT SYSTEM
==============================

1. Display Books
2. Add Book
3. Borrow Book
4. Return Book
5. My Borrowed Books
6. Delete Book
7. Exit
```

Enter a number from `1` to `7` to select an option.

---

## 📌 Example

### Adding a book

```text
Enter your choice: 2

Enter book title: Python Basics
Enter author name: John

Book added successfully.
```

### Borrowing a book

```text
Enter your choice: 3

Enter book title to borrow: Python Basics

Book borrowed successfully.
```

### Returning a book

```text
Enter your choice: 4

Enter book title to return: Python Basics

Book returned successfully.
```

---

## 🎯 Learning Objectives

This project helps practice:

* Python fundamentals
* Variables and data types
* Lists
* Loops
* Conditional statements
* Functions and methods
* Classes and objects
* Object-Oriented Programming
* File handling
* JSON
* Exception handling
* Git and GitHub

---

## 🔮 Future Improvements

Possible future features:

* 👥 Multiple users
* 🔐 User login system
* 💾 Save users and borrowed books to JSON
* 🔍 Search for books
* 📊 Library statistics
* 📅 Book due dates
* 💰 Fine calculation
* 🖥️ Graphical User Interface (GUI)
* 🗄️ Database support

---

## 👨‍💻 Author

**Arman**

**Project:** LBMS — Library Management System

Built as a Python learning and portfolio project.

---

## ⭐ Conclusion

LBMS is a beginner-friendly Python project designed to demonstrate practical use of **OOP, JSON, file handling, and GitHub**.

**Happy Coding! 🐍📚**
