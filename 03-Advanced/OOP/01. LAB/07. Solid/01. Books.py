class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page

    def __repr__(self):
        return f'{self.title} by {self.author}'


class Library:
    def __init__(self, books: list):
        self.books = books

    def find_book(self, title):
        for book in self.books:
            if title == book.title:
                return book


godfather = Book('The Godfather', 'Mario Puzo')
principles = Book('Principles', 'Ray Dalio')

library = Library([godfather, principles])
print(library.find_book('The Godfather'))