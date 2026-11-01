FILE = "library.txt"

def add_book():
    books = open(FILE, "a")
    id = len(load_books()) + 1
    title = input("Enter title: ")
    author = input("Enter author: ")
    books.write(f"{id}|{title}|{author}\n")
    books.close()
    print("Book added successfully")

def load_books():
    try:
        f = open(FILE, "r")
        books = [line.strip().split("|") for line in f]
        f.close()
        return books
    except:
        return []

def search():
    key = input("Enter title or author: ").lower()
    for b in load_books():
        if key in b[1].lower() or key in b[2].lower():
            print(b[0], b[1], "by", b[2])

def total():
    print("Total books:", len(load_books()))

def author_report():
    name = input("Enter author name: ").lower()
    for b in load_books():
        if name in b[2].lower():
            print(b[1], "by", b[2])

while True:
    print("\n1. Add Book")
    print("2. Search Book")
    print("3. Total Books")
    print("4. Books by Author")
    print("5. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        add_book()
    elif ch == "2":
        search()
    elif ch == "3":
        total()
    elif ch == "4":
        author_report()
    elif ch == "5":
        break
    else:
        print("Invalid choice")