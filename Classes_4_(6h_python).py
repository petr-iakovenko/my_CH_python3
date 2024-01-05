"""
Классы - 4 часть:

Дополняем методом "__str__" для "красивого" "print" экземпляра "ork"
"""


class Ork:
    def __init__(self, *, level: int) -> None:
        self.level = level
        self.health_points = 100 * level
        self.attack_power = 10 * level

    def attack(self) -> None:
        print(f"Ork attack with {self.attack_power} power")

    def __str__(self) -> str:  # метод класса
        """__str__ - для более понятного print экземпляра"""
        return f"Ork (LVL: {self.level}), (HP: {self.health_points}), (AP: {self.attack_power})"


ork = Ork(level=6)
print(ork)
# run: <__main__.Ork object at 0x100b1beb0>     - без метода __str__
# run: Ork (LVL: 6), (HP: 600), (AP: 60)        - с методом __str__
