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
    def __init__(self, title, author, year, format):
        super().__init__(title, author, year)
        self.format = format

    def info(self):
        print("Title: " + self.title)
        print("Author: " + self.author)
        print("Year: " + self.year)
        print(f"Формат: {self.format}")

book = Book("Я женщина", "Аня", "1999")
ebook = Ebook("Я женщина", "Аня", "2000", "PDF")
book.info()
ebook.info()