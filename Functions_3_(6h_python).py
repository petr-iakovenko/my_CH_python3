"""
Функции - 3 часть:

Множество аргументов передаваемые по одному **kwargs.
Способы передачи аргументов в функцию.
"""


def add_kwargs(**kwargs) -> None:
    print(kwargs)
    print(type(kwargs))

add_kwargs(name="Petr", age=32)  # первый способ передачи аргументов в "*kwargs"
# Результат вывода:
# {'name': 'Petr', 'age': 32}
# <class 'dict'> - класс "kwargs" словарь

person = {
    "name": "Petr",
    "age": 32,
    "city": "Batumi",
}

add_kwargs(**person)             # второй способ передачи аргументов в "*kwargs"
# Результат вывода:
# {'name': 'Petr', 'age': 32, 'city': 'Batumi'}
# <class 'dict'>
