"""
Lambda function

Используется для упрощения функции для разового использования
Для примера:
def some_func(el):
    return list(el)

Разобран пример с сортировкой по 2 условиям с применением лямбды
"""

nums = ["1", "245", "3", "431", "2341", "23", "345"]

sorted_list = sorted(nums, key=lambda element: int(element))
num_is_max = max(nums, key=lambda element: len(element))

print(sorted_list)
print(num_is_max)


"""
Написать сортировку с лямбдой, которая вернет максимальный элемент
из списка "people", сортировка должна быть сначала по возрасту, а 
потом по имени.
"""

people = [
    {"name": "Alice", "age": 17},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 19},
    {"name": "David", "age": 40},
]

sorted_people_one = max(
    people,
    key=lambda element: (element["age"], element["name"])
)
print(sorted_people_one)