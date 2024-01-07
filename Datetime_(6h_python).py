"""
Datetime

Разбор примеров работы с date_time
"""

import datetime

# Вычитание времени от текущего (пример)
current_datetime = datetime.datetime.now()
day_ago = current_datetime - datetime.timedelta(days=1)
print(day_ago)

# Перевод в читаемый вид (пример)
current_datetime = datetime.datetime.now()
print(current_datetime.strftime("%A, %d %B %Y"))  # run: Sunday, 07 January 2024


# Если нам передают дату в isoformat (пример)
isoformat = "2023-08-07T20:00:00.340000"
my_datetime = datetime.datetime.fromisoformat(isoformat)
print(type(my_datetime), my_datetime, sep=" = ")  # run: <class 'datetime.datetime'> = 2023-08-07 20:00:00.340000
