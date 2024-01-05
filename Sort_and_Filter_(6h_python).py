"""
Sort / Filter

Sort: Dict by age and name
Filter: List people is adult
"""

people = [
    {"name": "Alice", "age": 17},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 19},
    {"name": "David", "age": 40},
]


def sort_by_age_name(element: dict) -> tuple[int, str]:
    return element["age"], element["name"]

sorted_people = sorted(people, key=sort_by_age_name)
print(*sorted_people, sep="\n")


def is_adult(person: dict) -> bool:
    return person["age"] >= 18

filtered_people = list(filter(is_adult, people))
print(*filtered_people, sep="\n")