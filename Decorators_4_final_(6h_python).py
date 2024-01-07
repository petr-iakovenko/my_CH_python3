"""
Декораторы - 4 часть (финал):

Напишем декоратор для повторной попытки подключения к url по определенным интервалом с обработкой ошибки.
"""

import requests
from settings import TOKEN_API_VC
import time
from requests.exceptions import RequestException


def retry_conn(func):
    """
    Декоратор для повторной попытки подключения к url через 5 и 30 секунд
    """
    def wrapper_retry(*args, **kwargs):
        retries = [5, 30]
        for second in retries:
            try:
                return func(*args, **kwargs)
            except RequestException as exp:
                print(f"Failed to get data. Retrying in {second} second")
                time.sleep(second)
    return wrapper_retry


@retry_conn
def get_weather_by_hours_for_day_from_api(*, date: str, location: str) -> list[dict]:
    """
    Получаем список прогноза погоды по часам в условиях выбранной локации и даты
    """
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{date}/{date}?key={TOKEN_API_VC} "
    resource = requests.get(url)
    weather_by_days = resource.json()["days"]
    weather_by_hours = weather_by_days[0]["hours"]

    return weather_by_hours


def fahrenheit_to_celsius(*, fahrenheit_temperature: float) -> int:
    """
    Перевод фаренгейт в цельсий
    """
    return round((fahrenheit_temperature - 32) * 5 / 9)


def get_dangerous_hours(*, weather_by_hour: list[dict]) -> list[dict]:
    """
    Получаем список опасных часов по условию: "uvindex" >= 3
    """
    dangerous_hours = []
    for weather in weather_by_hour:
        uvindex = weather["uvindex"]
        time = weather["datetime"]
        celsius_temperature = fahrenheit_to_celsius(fahrenheit_temperature=weather["temp"])
        if uvindex >= 3:
            dangerous_hours.append({"time": time, 'uvindex': uvindex, "temperature": celsius_temperature})

    return dangerous_hours


date = "2024-01-08"
location = "Batumi"
weather_by_hour = get_weather_by_hours_for_day_from_api(date=date, location=location)
dangerous_hours = get_dangerous_hours(weather_by_hour=weather_by_hour)
print(dangerous_hours)