class Book:
    """This class creates a book object with the following specified/required attributes:
    title, author, isbn, num_pages, is_available"""

    def __init__(self, title, author, isbn, num_pages):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.num_pages = num_pages

    def book_info(self):
        """This method returns a string with the book's title, author, isbn, and number of pages"""
        return (
            f"{self.title} by {self.author} ISBN: {self.isbn} Pages: {self.num_pages}"
        )

class Member:
    """This class creates a member object with the following specified/required attributes:
    name, member_id, books_borrowed"""

    def __init__(self, name, member_id, books_borrowed):
        self.name = name
        self.member_id = member_id
        self.books_borrowed = books_borrowed

    def member_info(self):
        """This method returns a string with the member's name, id, and books borrowed"""
        return f"{self.name} Member ID: {self.member_id} Books Borrowed: {self.books_borrowed}"

    def check_out_book(self, book):
        """This method adds a book to the member's list of books borrowed"""
        self.books_borrowed.append(book)

    def return_book(self, book):
        """This method removes a book object from the member's list of books borrowed from the library's list of available books"""
        self.books_borrowed.remove(book)


class Library:
    """This class creates a library object with the following specified/required attributes:
    books, members"""

    def __init__(self, books, members):
        self.books = books
        self.members = members

    def add_book(self, book):
        """This method adds a book object to the library's list of books"""
        self.books.append(book)

    def remove_book(self, book):
        """This method removes a book from the library's list of books"""
        self.books.remove(book)

    def add_member(self, member):
        """This method adds a member object to the library's list of members"""
        self.members.append(member)

    def remove_member(self, member):
        """This method removes a member from the library's list of members"""
        self.members.remove(member)

    def book_search(self, title):
        """This method searches for a book by title and returns a list of book objects if found"""
        matching_books = [book for book in self.books if book.title == title]
        if matching_books:
            return matching_books
        else:
            return "No books found with that title, please revise your search."

