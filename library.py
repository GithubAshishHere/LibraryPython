class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
        self.reserved_by = None
    
    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False
    
    def return_book(self):
        self.is_borrowed = False
        self.reserved_by = None
    
    def reserve(self, member):
        if not self.reserved_by:
            self.reserved_by = member
            return True
        return False
    
    def __str__(self):
        status = " [Borrowed]" if self.is_borrowed else ""
        return f"{self.title} by {self.author} (ISBN: {self.isbn}){status}"


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
    
    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            return True
        return False
    
    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            return True
        return False
    
    def __str__(self):
        return f"{self.name} (ID: {self.member_id})"


class Library:
    def __init__(self):
        self.books = []
        self.members = []
    
    def add_book(self, title, author, isbn):
        self.books.append(Book(title, author, isbn))
    
    def register_member(self, name, member_id):
        self.members.append(Member(name, member_id))
    
    def get_member(self, name):
        return next((m for m in self.members if m.name == name), None)
    
    def get_book(self, title):
        return next((b for b in self.books if b.title == title), None)
    
    def __str__(self):
        return f"Library has {len(self.books)} books and {len(self.members)} members."


# Example Usage
library = Library()

# Dynamic inputs
book_title = "Squid Book"
book_author = "Aashish"
book_isbn = "1122334455"
member_name = "Aashish"
member_id = 99

library.add_book(book_title, book_author, book_isbn)
library.register_member(member_name, member_id)

aashish = library.get_member(member_name)
book = library.get_book(book_title)

if aashish and book:
    if aashish.borrow_book(book):
        print(f"{aashish.name} borrowed {book.title}")
    else:
        print(f"{book.title} is already borrowed.")

    print(book)
