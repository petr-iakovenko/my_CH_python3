"""
Декораторы - 3 часть:

Дополним декоратор для оборачивания функции с принимаемым аргументом и возращением значения.
"""


def my_decorator(func):
    """Декоратор выполняющий "print" до запуска обернутой функции func()"
    (с принимаемыми аргументами "*args, **kwargs") и после ее выполнения"""
    def wrapper(*args, **kwargs):
        print("Something is happening BEFORE the function is called.")
        result = func(*args, **kwargs)  # модернизация декоратора для return оборачиваемой функции
        print("Something is happening AFTER the function is called.")
        return result                   # модернизация декоратора для return оборачиваемой функции

    return wrapper


@my_decorator                       # оборачивание функции декоратором
def add_numbers(*, a: int, b: int) -> int:
    print("Adding numbers in decorators")
    return a + b

res = add_numbers(a=2, b=3)      # запуск функции обернутую в декоратор
print(res)                       # run: 5 - вывод возвращенного значения "result" выполненной функции add_numbers()
