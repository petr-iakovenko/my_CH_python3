"""
Работа с файлами

Разберем примеры работы с файлами json, csv
"""
import json
import csv

""" JSON """

data = {"name": "Mike", "age": 40, "city": "New York"}

# ЗАПИСЬ
file = open("files/data.json", "w")
# .dump - запить json в файл
# indent= - отступы для читаемости
json.dump(data, file, indent=4)
file.close()  # закрытие файла после работы с ним

# ЧТЕНИЕ
file = open("files/data.json", "r")
loaded_data = json.load(file)  # прочитанный файл в переменной loaded_data
file.close()


""" CSV """

rows = [['name', 'age', 'occupation'],
        ['John', 29, 'Engineer'],
        ['Marie', 24, 'Designer'],
        ['Petr', 32, 'Data Engineer']]

file = open("files/persons.csv", "w")
# ЗАПИСЬ
csv_writer = csv.writer(file)
csv_writer.writerows(rows)  # все строки
file.close()

# ЧТЕНИЕ
file = open("files/persons.csv", "w")
csv_dict_rider = csv.DictReader(file)
for row in csv_dict_rider:
    print(row["name"], row["age"], row["occupation"])  # вывод построчно без вывода названия столбцов
file.close()


# ДОБАВЛЕНИЕ
persons = [
    {'name': 'Jack', 'age': 26, 'occupation': 'Artist'},
    {'name': 'Emma', 'age': 32, 'occupation': 'Programmer'}
]
file = open("files/persons.csv", "a")
fields = ['name', 'age', 'occupation']
csv_dict_writer = csv.DictWriter(file, fieldnames=fields)
csv_dict_writer.writerows(persons)
file.close()