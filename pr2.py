class Transport:
    def __init__(self, brand, max_speed):
        self.brand = brand
        self.max_speed = max_speed

    def describe(self):
        return f"Транспорт {self.brand}, макс. скорость {self.max_speed} км/ч"


class Car(Transport):
    def __init__(self, brand, max_speed, seats):
        super().__init__(brand, max_speed)
        self.seats = seats

    def describe(self):
        return (f"Автомобиль {self.brand}: едет до {self.max_speed} км/ч, "
                f"мест — {self.seats}")


class Bicycle(Transport):
    def __init__(self, brand, max_speed, speed):
        super().__init__(brand, max_speed)
        self.speed = speed

    def describe(self):
        return (f"Велосипед {self.brand}: крутим педали, до {self.max_speed} км/ч, "
                f"скоростей — {self.speed}")


class Airplane(Transport):
    def __init__(self, brand, max_speed, max_hight):
        super().__init__(brand, max_speed)
        self.max_hight = max_hight

    def describe(self):
        return (f"Самолёт {self.brand}: летит до {self.max_speed} км/ч "
                f"на высоте до {self.max_hight} м")


def show(vehicle):
    print(vehicle.describe())


all_transport = [
    Car("Lada", 180, seats=5),
    Bicycle("Stels", 35, speed=20),
    Airplane("МС-21", 870, max_hight=12_000),
]

for vehicle in all_transport:
    show(vehicle)