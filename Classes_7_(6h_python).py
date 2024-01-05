"""
Классы - 7 часть:

Реализуем наследование из родительского класса. Сымитируем поединок 2 существ.

Изменяем родительский метод ".attack()" для описание действий и ее логики в поединке.
Создадим несколько разных экземпляров класса "Ork" и "Elf"
Имитируем простой поединок.
"""


class Character:
    """Базовый класс"""
    def __init__(self, *, level: int) -> None:
        self.level = level
        self.health_points = self.base_health_points * level
        self.attack_power = self.base_attack_power * level

    def attack(self, *, target: "Character") -> None:       # измененный родительский метод
        """экземпляр класса {self.character_name} наносит урон в размере {self.attack_power}
        по {target.health_points} экземпляра класса {target.character_name}"""
        print(
            f"{self.character_name} (LVL: {self.level}; HP: {self.health_points}; AP: {self.attack_power}) attacks "
            f"{target.character_name} (LVL: {target.level}; HP: {target.health_points}; AP: {target.attack_power})."
        )
        target.health_points -= self.attack_power
        print(f"After attack {target.character_name} has {target.health_points} HP")

    def is_alive(self) -> bool:         # метод проверяющий живо ли существо(экземпляр класса {self.character_name})
        return self.health_points > 0

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


def fight(*, character_1: Character, character_2: Character) -> str:
    """character_1 и character_2 атакуют друг
    друга по очереди пока кто-то из них жив"""
    while character_1.is_alive() and character_2.is_alive():
        character_1.attack(target=character_2)
        if character_2.is_alive():
            character_2.attack(target=character_1)
    if character_1.is_alive():
        return f"{character_1} is winner!"
    else:
        return f"{character_2} is winner!"


ork_1 = Ork(level=1)  # экземпляр класса "Ork(Character)"
elf_1 = Elf(level=2)  # экземпляр класса "Elf(Character)"

print(ork_1)        # run: Ork (LVL: 1), (HP: 100), (AP: 10)
print(elf_1)        # run: Elf (LVL: 2), (HP: 100), (AP: 30)
print(fight(character_1=ork_1, character_2=elf_1))