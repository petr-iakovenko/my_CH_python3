"""
Декораторы - 1 часть:

Напишем простейший декоратор и применим его к функции без принимаемых аргументов.

Декораторы являются синтаксическим сахаром.
Декоратор, как функция принимает как аргумент другую функцию и "обогащает" ее поведение.
"""


def my_decorator(func):
    """Простой декоратор выполняющий "print" до запуска
    обернутой функции "func()" и после ее выполнения"""
    def wrapper():
        print("Something is happening BEFORE the function is called.")
        func()
        print("Something is happening AFTER the function is called.")

    return wrapper


def say_hello():
    print("Hello!")

my_decorator(say_hello)()   # запуск в "лоб"


@my_decorator               # обработка функции декоратором
def say_hello():
    print("Hello!")

say_hello()                 # запуск функции обернутую в декоратор
