class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        print("Title: " + self.title)
        print("Author: " + self.author)
        print("Year: " + self.year)

class Ebook(Book):
    def format(self, format):
        print("Format: " + format)

book = Ebook("женщина", "Аня", "1949")
book.info()
book.format("PDF")