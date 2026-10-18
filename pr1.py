class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary

    def __str__(self):
        return f"{type(self).__name__} {self.name}: {self.calculate_salary():,} руб."


class Manager(Employee):
    def __init__(self, name, base_salary, work_time, bonus_per_member):
        super().__init__(name, base_salary)
        self.bonus = work_time
        self.bonus_per_member = bonus_per_member

    def calculate_salary(self):
        return super().calculate_salary() + self.bonus * self.bonus_per_member


class Developer(Employee):
    levels = {"junior": 1.0, "middle": 1.5, "senior": 2.0}

    def __init__(self, name, base_salary, level):
        super().__init__(name, base_salary)
        if level not in self.levels:
            raise ValueError(f"Неизвестный уровень: {level}")
        self.level = level

    def calculate_salary(self):
        base = super().calculate_salary() * self.levels[self.level]
        return int(base)


workers = [
    Employee("Иван", 60_000),
    Manager("Ольга", 120_000, work_time=5, bonus_per_member=8_000),
    Developer("Пётр", 100_000, level="junior"),
    Developer("Анна", 100_000, level="senior"),
]

for person in workers:
    print(person)