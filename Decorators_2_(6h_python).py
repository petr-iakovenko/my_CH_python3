"""
Декораторы - 2 часть:

Дополним декоратор для оборачивания функции с принимаемым аргументом.
"""


def my_decorator(func):
    """Декоратор выполняющий "print" до запуска обернутой функции func()"
    (с принимаемыми аргументами "*args, **kwargs") и после ее выполнения"""
    def wrapper(*args, **kwargs):
        print("Something is happening BEFORE the function is called.")
        func(*args, **kwargs)
        print("Something is happening AFTER the function is called.")

    return wrapper


@my_decorator               # оборачивание функции декоратором
def say_hello(*, name: str) -> None:
    print(f"Hello, {name}!")

say_hello(name="Petr")      # запуск функции обернутую в декоратор
