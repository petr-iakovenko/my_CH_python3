"""
Mutable immutable

Int, str, float, tuple, bool, None …. - неизменяемые типы данных
list, dict, set - изменяемые типы дынных
Разбираем примеры - operator, func
Разбираем примеры ошибок dict,
"""

""" OPERATORS """

a = None
b = None

print(a is b)  # Output: True

list1 = [1, 2, 3]
list2 = list1
print(list1 is list2)  # Output: True

list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2)  # Output: True
print(list1 is list2)  # Output: False

some_variable = True
print(some_variable == True)  # ONT USE # Output: True
print(some_variable is True)  # Output: True

some_variable = None
print(some_variable == None)  # ONT USE # Output: True
print(some_variable is None)            # Output: True

""" FUNCTIONS """

x = 42
y = x

print(id(x))  # Outputs the identity (memory address) of the object referred to by x
print(id(y))  # Outputs the same identity as that of x, since y refers to the same object as x
print(x, y)
y += 1
print(id(y))  # Outputs a different identity since y refers to a different object
print(x, y)

my_list = [1, 2, 3]
another_list = my_list

print(id(my_list))
print(id(another_list))
print(my_list, another_list)

another_list.append(4)
print(id(my_list))
print(id(another_list))
print(my_list)  # [1, 2, 3, 4]


""" MISTAKE dict"""


my_dict = {'x': 1, 'y': 2}
another_dict = my_dict
another_dict['x'] = 100

print(my_dict)  # my_dict - изменен  # Output: {'x': 100, 'y': 2}

my_dict = {'x': 1, 'y': 2}
another_dict = my_dict.copy()
another_dict['x'] = 100
print(my_dict)  # my_dict - изменен  # Output: {'x': 1, 'y': 2}
print(another_dict)                  # Output: {'x': 100, 'y': 2}

patient_data = {'heart_rate': [60, 61, 63, 60, 61]}
patient_data_copy = patient_data.copy()
patient_data_copy['heart_rate'].append(63)
print(patient_data)  # patient_data - изменен    # Output: {'heart_rate': [60, 61, 63, 60, 61, 63]}

# !!! самый правильный вид копирования словаря
from copy import deepcopy

patient_data = {'heart_rate': [60, 61, 63, 60, 61]}
patient_data_deep_copy = deepcopy(patient_data)  # deepcopy() - применен
patient_data_deep_copy['heart_rate'].append(63)
print(patient_data)  # patient_data - НЕ изменен  # Output: {'heart_rate': [60, 61, 63, 60, 61]}


"""MISTAKE func"""


def function_with_computatuon(*, lst: list[int]) -> None:
    # тут могут быть какие-то манипуляции с "lst"
    lst.clear()  # очищаем "lst"


my_list = [1, 2]
function_with_computatuon(lst=my_list)
print(my_list)  # my_list - изменен   # Output: []

# !!! самый правильный вид копирования
from copy import deepcopy
my_list = [1, 2]
function_with_computatuon(lst=deepcopy(my_list))  # deepcopy() - применен
print(my_list)  # my_list - НЕ изменен (as expected)


# модернизация функции function_with_computatuon() и запись, для осознанного переприсвоение значения в "my_list"
def function_with_computatuon(*, lst: list[int]) -> list[int]:
    # тут могут быть какие-то манипуляции с "lst"
    lst.clear()  # очищаем "lst"
    return lst


my_list = [1, 2]
my_list = function_with_computatuon(lst=my_list)  # переприсвоение "my_list" возвращенному значению из функции
print(my_list)  # my_list - был переприсвоен return функции # Output: []


""" MISTAKE Iteration"""


# Попытка добавить в список квадратное значение текущих чисел
# Бесконечная итерация которая постоянно все значения возводит в квадрат
# Квадраты числа НЕ будут добавлены в лист!
lst = [2, 3, 4]
for num in lst:
    lst.append(num ** 2)
    print(num)

# Квадраты числа будут добавлены в лист!
lst = [2, 3, 4]
another_list = [i ** 2 for i in lst]
lst.extend(another_list)
print(lst)  # [2, 3, 4, 4, 9, 16]


# Попытка убрать четные числа из листа
numbers = [1, 3, 5, 4, 8, 6]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)
print(numbers)  # в лист попала лишняя "8" # output [1, 3, 5, 8]

# Не пытаемся изменить текущий список.
# Создается пустой список и в него добавляется необходимое
numbers = [1, 3, 5, 4, 8, 6]
odd_numbers = []  # пустой список
for num in numbers:
    if num % 2 != 0:
        odd_numbers.append(num)
print(odd_numbers)

numbers = [1, 3, 5, 4, 8, 6]
odd_numbers = [num for num in numbers if num % 2 != 0]


""" MISTAKE with Arguments """


# пробрасывание immutable type в качестве дефолтного аргумента функции
# НЕ верное объявление дефолтного значения листа
def append_to_list(*, element: int, lst: list = []) -> list:  # по умолчанию "list = []"
    lst.append(element)
    return lst


my_list = append_to_list(element=1)
print(my_list)                                               # Output: [1]
my_other_list = append_to_list(element=2)
print(my_other_list)  # произошло добавление значения в лист # Output: [1, 2]


# верное объявление дефолтного значения листа
def append_to_list(*, element: int, lst: list = None) -> list: # по умолчанию "list = None"
    if lst is None:
        lst = []
    lst.append(element)
    return lst


my_list = append_to_list(element=1)
print(my_list)  # Output: [1]
my_other_list = append_to_list(element=2)
print(my_other_list)  # Output: [2]


""" MISTAKE with object """


my_list = [3, 1, 2]

my_list.sort()  # просто изменяет изначальную структуру данных
print(my_list)  # Output: [1, 2, 3]

another_list = my_list.sort()  # метод ".sort()" ничего не возвращает
print(another_list)  # неожидаемый результат  # Output: None

my_list = [3, 1, 2]
another_list = sorted(my_list)  # метод "sorted()" возвращает отсортированный список, а старый не меняется
print(another_list)  # Output: [1, 2, 3]
print(my_list)       # Output: [3, 1, 2]
