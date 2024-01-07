"""
Mutable immutable

Int, str, float, tuple, bool, None …. - неизменяемые типы данных
list, dict, set - изменяемые типы дынных
Разбираем примеры - operator, func
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