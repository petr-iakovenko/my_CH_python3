"""
Функции - 4 часть:

Множество аргументов передаваемые по одному **kwargs.
Способы передачи аргументов в функцию и возвращение 2 типов данных.
"""


def modify_dict(*, old_dict: dict, **kwargs) -> tuple[dict, bool]:
    is_modified = False

    for key, value in kwargs.items():
        if old_dict.get(key) != value:
            old_dict[key] = value
            is_modified = True

    return old_dict, is_modified  # модификация old_dict и статус is_modified


product = {
    "id": 1,
    "name": "Laptop",
    "price": 999.99,
}

structure = modify_dict(old_dict=product, in_stock=True)  # модификация значением key:value
product, was_modified = modify_dict(old_dict=product, name="Laptop")  # модификация не сработает

print(structure, type(structure), sep="\n")
# Результат вывода:
# ({'id': 1, 'name': 'Laptop', 'price': 999.99, 'in_stock': True}, True)
# <class 'tuple'>

print(product, was_modified, type(product), type(was_modified), sep="\n")
# Результат вывода:
# {'id': 1, 'name': 'Laptop', 'price': 999.99, 'in_stock': True}
# False
# <class 'dict'>
# <class 'bool'>
