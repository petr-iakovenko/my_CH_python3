"""
Функции - 2 часть:

Множество аргументов передаваемые по одному - *args.
Способы передачи аргументов в функцию.
"""


def add_all(*args) -> None:
    print(args)
    print(type(args))


add_all(1, 2, 3, "text")  # первый способ передачи аргументов в "*args"
# Результат вывода:
# (1, 2, 3, 'text')
# <class 'tuple'> - класс "args" кортеж


def total_numbers(*args) -> int:
    summery = 0
    for num in args:
        summery += num
    return summery

values = [1, 2, 3, 4]
other_values = [6, 5, 7]

print(total_numbers(*values, *other_values))  # второй способ передачи аргументов в "*args"
# Результат вывода:
# 28
