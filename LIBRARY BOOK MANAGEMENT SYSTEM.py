import csv

file = "books.csv"

def add_book():
    b = input("Enter book name: ")
    with open(file, "a", newline="") as f:
        csv.writer(f).writerow([b])
    print("Book Added")

def search_book():
    try:
        b = input("Enter book name: ")
        with open(file, "r") as f:
            for row in csv.reader(f):
                if b in row:
                    print("Book Found")
                    return
        print("Book Not Found")
    except FileNotFoundError:
        print("File Not Found")

def remove_book():
    try:
        b = input("Enter book name: ")
        books = []
        with open(file, "r") as f:
            for row in csv.reader(f):
                if row[0] != b:
                    books.append(row)

        with open(file, "w", newline="") as f:
            csv.writer(f).writerows(books)
        print("Book Removed")
    except FileNotFoundError:
        print("File Not Found")

add_book()
search_book()
remove_book()