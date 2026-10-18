class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        print("Title: " + self.title)
        print("Author: " + self.author)
        print("Year: " + self.year)

Book("Я женщина", "Аня", "1999").info()