"""
List Comprehension (Списковое включение)

Примеры: If / else; dict.
"""

even_squares = [x**2 for x in range(20) if x % 2 == 0]
print(even_squares)

bool_squares = [f"Yes: {x}" if x % 2 == 0 else f"No: {x}" for x in range(7)]
print(bool_squares)

square_dict = {x: x ** 2 for x in range(5)}
print(square_dict)