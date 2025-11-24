
import os
BOOKS_FILE = "books.txt"

def load_books():
    if not os.path.exists(BOOKS_FILE):
        return []
    with open(BOOKS_FILE, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_books(books):
    with open(BOOKS_FILE, "w") as f:
        for book in books:
            f.write(book + "\n")

def add_book():
    title = input("Enter book title: ")
    books = load_books()
    books.append(title)
    save_books(books)
    print("Book added.")

def issue_book():
    title = input("Enter book title to issue: ")
    books = load_books()
    if title in books:
        books.remove(title)
        save_books(books)
        print("Book issued.")
    else:
        print("Book not available.")

def return_book():
    title = input("Enter book title to return: ")
    books = load_books()
    books.append(title)
    save_books(books)
    print("Book returned.")

def display_books():
    books = load_books()
    print("Available books:")
    for b in books:
        print(" -", b)

def menu():
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Display Books")
        print("5. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            issue_book()
        elif choice == "3":
            return_book()
        elif choice == "4":
            display_books()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()
