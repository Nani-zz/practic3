from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print_info(self):
        pass


class Book(Printable):
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def print_info(self):
        print(f"«{self.title}», автор: {self.author}, год: {self.year}")


book = Book("Мастер и Маргарита", "Михаил Булгаков", 1967)
book.print_info()
