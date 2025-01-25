import json

FILE_LIBRARY = "python-nuggets/level-2/libraries.json"


class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True
    
    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Status: {status}"

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"Member: {self.name}, Borrowed Books: {len(self.borrowed_books)}"
    
class Library:
    def __init__ (self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")
        
    
    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Book '{book.title}' removed from the library.")
                return
        print("Book not found.")

    def search_book(self, query):
        results = []
        for book in self.books:
            if query.lower() in book.title.lower() or query.lower() in book.author.lower() or query == book.isbn:
                results.append(book)
        return results

    def borrow_book(self, member, isbn):
        for book in self.books:
            if book.isbn == isbn and book.available:
                book.available = False
                member.borrowed_books.append(book)
                print(f"Book '{book.title}' borrowed by {member.name}.")
                return
        print("Book not available or not found.")

    def return_book(self, member, isbn):
        for book in member.borrowed_books:
            if book.isbn == isbn:
                book.available = True
                member.borrowed_books.remove(book)
                print(f"Book '{book.title}' returned by {member.name}.")
                return
        print("Book not found in member's borrowed list.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("==============================")
            print("\nLibrary Books:\n")
            for book in self.books:
                print(f"📔 {book.title}")
                print(f"author: {book.author}")
                print(f"ISBN: {book.isbn}")
                print(f"status: {'Available' if book.available else 'Borrowed'}")
                print("")
            print("==============================")
            back = input("press enter to go back to home.")

    def save_data(self, filename = FILE_LIBRARY):
        import json
        data = {
            "books": [{"title": book.title, "author": book.author, "isbn": book.isbn, "available": book.available} for book in self.books],
            "members": [{"name": member.name, "borrowed_books": [book.isbn for book in member.borrowed_books]} for member in self.members]
        }
        with open(filename, "w") as file:
            json.dump(data, file)
        print("Library data saved successfully.")

    def load_data(self, filename = FILE_LIBRARY):
        import json
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.books = [Book(book["title"], book["author"], book["isbn"]) for book in data["books"]]
                for book, book_data in zip(self.books, data["books"]):
                    book.available = book_data["available"]
                self.members = [Member(member["name"]) for member in data["members"]]
                for member, member_data in zip(self.members, data["members"]):
                    member.borrowed_books = [book for book in self.books if book.isbn in member_data["borrowed_books"]]
            print("Library data loaded successfully.")
        except FileNotFoundError:
            print("No saved data found.")

def main():
    library = Library()
    library.load_data()

    while True:
        print("""
LIBRARY MANAGEMENT SYSTEM
              
1. Add a book
2. Remove a book
3. Search for a book
4. Borrow a book
5. Return a book
6. Display all books
7. Save and Exit
""")
        choice = input("Choose an option: ")
        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book isbn: ")
            library.add_book(Book(title, author, isbn))

        elif choice == "2":
            isbn = input("Enter ISBN of the book to remove: ")
            library.remove_book(isbn)

        elif choice == "3":
            query = input("Enter title, author, or ISBN to search: ")
            results = library.search_book(query)
            if results:
                print("==============================")
                print("\nLibrary Books:\n")
                for book in results:
                    status = "Available" if book.available else "Borrowed" 
                    print(f"📔 {book.title}")
                    print(f"Author: {book.author}")
                    print(f"ISBN: {book.isbn}")
                    print(f"Status: {status}")
                    print("")  
                print("==============================")
                back = input("Press Enter to go back to home.") 
            else:
                print("No books found.")

        elif choice == "4":
            member_name = input("Enter member name: ")
            isbn = input("Enter ISBN of the book to borrow: ")
            member = next((m for m in library.members if m.name == member_name), None)
            if not member:
                member = Member(member_name)
                library.members.append(member)
            library.borrow_book(member, isbn)

        elif choice == "5":
            member_name = input("Enter member name: ")
            isbn = input("Enter ISBN of the book to return: ")
            member = next((m for m in library.members if m.name == member_name), None)
            if member:
                library.return_book(member, isbn)
            else:
                print("Member not found.")
        elif choice == "6":
            library.display_books()
        elif choice == "7":
            library.save_data()
            print("Saving data. Exiting program.\nGoodbye! —hazellenuts\n")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()