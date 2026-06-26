library = []

def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    quantity = int(input("Enter Quantity: "))

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "quantity": quantity
    }

    library.append(book)
    print("Book added successfully")


def view_books():
    if not library:
        print("No books available")
        return

    print("\n----- Book List -----")
    for book in library:
        print(f"""
Book ID : {book['id']}
Title   : {book['title']}
Author  : {book['author']}
Quantity: {book['quantity']}
-----------------------
""")


def search_book():
    search = input("Enter book title: ").lower()

    found = False

    for book in library:
        if search in book["title"].lower():
            print("Book Found")
            print(book)
            found = True

    if not found:
        print("Book not found")


def issue_book():
    book_id = input("Enter Book ID: ")

    for book in library:
        if book["id"] == book_id:
            if book["quantity"] > 0:
                book["quantity"] -= 1
                print("Book issued successfully")
            else:
                print("Book out of stock")
            return

    print("Book not found")


def return_book():
    book_id = input("Enter Book ID: ")

    for book in library:
        if book["id"] == book_id:
            book["quantity"] += 1
            print("Book returned successfully")
            return

    print("Book not found")


while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        issue_book()

    elif choice == "5":
        return_book()

    elif choice == "6":
        print("Program closed")
        break

    else:
        print("Invalid choice")
