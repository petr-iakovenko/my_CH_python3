"""
Классы - 5 часть:

Реализуем наследование из родительского класса.
Создадим несколько разных экземпляров класса "Ork"
"""


class Character:
    """Базовый класс"""
    def __init__(self, *, level: int) -> None:
        self.level = level
        self.health_points = self.base_health_points * level
        self.attack_power = self.base_attack_power * level

    def attack(self) -> None:
        print(f"{self.character_name} attack with {self.attack_power} power")

    def __str__(self) -> str:
        return f"{self.character_name} (LVL: {self.level}), (HP: {self.health_points}), (AP: {self.attack_power})"


class Ork(Character):
    """Наследник класса Character"""
    base_health_points = 100    # объявление атрибута класса Ork
    base_attack_power = 10      # объявление атрибута класса Ork
    character_name = "Ork"      # объявление атрибута класса Ork


ork_1 = Ork(level=1)        # экземпляр класса "Ork(Character)"
ork_2 = Ork(level=6)
print(ork_1)    # run: Ork (LVL: 1), (HP: 100), (AP: 10)
print(ork_2)    # run: Ork (LVL: 6), (HP: 600), (AP: 60)
