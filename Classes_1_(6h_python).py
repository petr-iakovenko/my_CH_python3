"""
Классы - 1 часть:

Разбор примера между Клссом и Экземпляром класса.

Класс - это «чертеж», на основе которого создается экземпляр.
Синоним слова "экземпляр" - "инстанс", "объект".
"""


class MyClass:
    pass


my_class = MyClass()
print(type(MyClass))   # run: <class 'type'> - класс
print(type(my_class))  # run: <class '__main__.MyClass'> - экземпляр класса
