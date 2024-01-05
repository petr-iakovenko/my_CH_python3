"""
Классы - 5 часть:

Реализуем наследование(с переопределением метода у наследника класса) из родительского класса.
Создадим несколько разных экземпляров класса "Ork" и "Elf"
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


class Elf(Character):
    """Наследник класса Character"""
    base_health_points = 50     # объявление атрибута класса Ork
    base_attack_power = 15      # объявление атрибута класса Ork
    character_name = "Elf"      # объявление атрибута класса Ork

    def attack(self) -> None:   # предопределение метода
        print("This method from class - Elf")


ork_1 = Ork(level=1)  # экземпляр класса "Ork(Character)"
elf_1 = Elf(level=2)  # экземпляр класса "Elf(Character)"

print(ork_1)        # run: Ork (LVL: 1), (HP: 100), (AP: 10)
ork_1.attack()      # run: Ork attack with 10 power
print(elf_1)        # run: Elf (LVL: 2), (HP: 100), (AP: 30)
elf_1.attack()      # run: This method from class - Elf
