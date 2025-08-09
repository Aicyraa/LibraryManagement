import library_utils

class Library:

    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = {
            "title": title.lower(),
            "author": author,
            "isAvailable": True
        }
        self.books.append(book) # appends the book

    def borrow_book(self, title):
        for book in self.books:
            if title.lower() == book.get("title").lower() :
                book["isAvailable"] = False

    def return_book(self, title):
        for book in self.books:
             if title.lower() == book.get("title").lower() :
                book["isAvailable"] = True

    def show_books(self):
        for book in self.books:
            print(book)


library = Library()
library.add_book("Romeo And Juliet", "William Shakespear")
library.add_book("Harry Potter", "JK Rowling")
library.add_book("The lord of the rings", "J.R.R. Tolkien.")
library.add_book("The Twilight Saga ", "Stephenie Meyer")
library.add_book("The Da Vinci Code ", "Dan Brown.")


