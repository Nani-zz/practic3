from datetime import datetime

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        return f"«{self.title}», автор: {self.author}, год: {self.year}"

    def __str__(self):
        return self.info()

    def __eq__(self, other):
        return (
            isinstance(other, Book)
            and self.title == other.title
            and self.author == other.author
        )

    @property
    def age(self):
        """Сколько лет прошло с года издания."""
        return datetime.now().year - self.year

    @age.setter
    def age(self, value):
        """Задаёт возраст, а год издания пересчитывается сам."""
        self.year = datetime.now().year - value

    @classmethod
    def from_string(cls, data):
        """Создаёт книгу из строки вида 'Название;Автор;Год'."""
        title, author, year = data.split(";")
        return cls(title, author, int(year))


book1 = Book("1984", "Кто-то там", 1949)
book2 = Book.from_string("1984;Кто-то там;1949")
book3 = Book.from_string("Война и мир; Лев Толстой; 1869")

print(book1)
print(book3)

print(book1 == book2)        # True  — одинаковые название и автор
print(book1 == book3)        # False — разные книги
print(book1 == "1984")       # False — не объект Book

print(f"Возраст «{book1.title}»: {book1.age} лет")

book1.age = 10
print(f"Если возраст книги {book1.age} год издания: {book1.year}")