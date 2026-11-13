
class SpaceShip:
    def __init__(self, name, fuel, hull, speed):
        self.name = name
        self.fuel = fuel
        self.hull = hull
        self.speed = speed

    def fly(self):
        if self.fuel >= 10:
            self.fuel -= 10
            self.speed += 100
            print(f"{self.name} летит. Скорость: {self.speed}")
        else:
            print("Недостаточно топлива!")

    def repair(self):
        self.hull += 20
        if self.hull > 100:
            self.hull = 100
        print("Корпус корабля отремонтирован.")

    def show_status(self):
        print(f"\nКорабль: {self.name}")
        print(f"Топливо: {self.fuel}")
        print(f"Состояние корпуса: {self.hull}")
        print(f"Скорость: {self.speed}")



class CrewMember:
    workers = []

    def __init__(self, name, role, health, skill):
        self.name = name
        self.role = role
        self.health = health
        self.skill = skill

        CrewMember.workers.append(self)

    def work(self):
        if self.health > 0:
            print(f"{self.name} ({self.role}) выполняет работу.")
        else:
            print(f"{self.name} не может работать.")

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"Здоровье {self.name}: {self.health}")

    @classmethod
    def check_all_workers(cls):
        print("\n--- Состав экипажа ---")

        for worker in cls.workers:
            status = "Работает" if worker.health > 0 else "Не может работать"

            print(f"Имя: {worker.name}")
            print(f"Роль: {worker.role}")
            print(f"Здоровье: {worker.health}")
            print(f"Статус: {status}")
            print("-------------------")


class Mission:
    def __init__(self, goal, resources):
        self.goal = goal
        self.resources = resources
        self.events = []

    def add_event(self, event):
        self.events.append(event)
        print(f"Событие миссии: {event}")

    def show_mission(self):
        print("\nЦель миссии:", self.goal)
        print("Ресурсы:", self.resources)
        print("События:", self.events)


# Создание объектов
ship = SpaceShip("Звездолёт", 100, 100, 0)

pilot = CrewMember("Иван", "Пилот", 100, 90)
engineer = CrewMember("Алексей", "Инженер", 100, 85)

mission = Mission("Достичь Марса", 500)

# Выполнение миссии
ship.show_status()

pilot.work()
engineer.work()

ship.fly()
mission.add_event("Встреча с астероидами")

ship.hull -= 30
engineer.work()
ship.repair()

pilot.take_damage(10)

ship.show_status()
mission.show_mission()


pilot = CrewMember("Иван", "Пилот", 100, 90)
engineer = CrewMember("Алексей", "Инженер", 100, 85)

CrewMember.check_all_workers()
