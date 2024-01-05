"""
Классы - 3 часть:

Дополняем класс атрибутами и методом из "Class_2_(6h_python).py" для расширения функционала.
Проверяем работу атрибутов и метода ".attack()" экземпляра "ork".
"""


class Ork:
    def __init__(self, *, level: int) -> None:
        self.level = level                  # атрибут класса
        self.health_points = 100 * level    # атрибут класса
        self.attack_power = 10 * level      # атрибут класса

    def attack(self) -> None:               # метод класса
        print(f"Ork attack with {self.attack_power} power")

ork = Ork(level=6)          # создан экземпляр класса Ork
print(ork.level)            # run: 6
print(ork.attack_power)     # run: 60
ork.attack()                # run: Ork attack with 60 power
