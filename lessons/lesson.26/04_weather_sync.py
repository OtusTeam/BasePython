import os

# os.system("clear")

"""
Внимание, для работы необходимо установить библиотеку requests:
pip3 install requests
"""
import requests  # Импортируем библиотеку для выполнения HTTP-запросов
import time  # Импортируем библиотеку для работы со временем

API_KEY = 'your_api'

# Функция для получения данных о погоде для указанного города
def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather'  # URL API
    params = {'q': city, 'APPID': API_KEY}  # Параметры запроса, включая город и API ключ
    response = requests.get(url, params=params)  # Выполняем HTTP-запрос
    weather_json = response.json()  # Получаем JSON ответ
    print(f'{city}: {weather_json["weather"][0]["main"]}')  # Выводим информацию о погоде

# Основная функция
def main(cities):
    for city in cities:  # Перебираем список городов
        get_weather(city)  # Вызываем функцию получения погоды для каждого города

if __name__ == '__main__':
    # Список городов для получения данных о погоде
    cities = ['Moscow', 'St. Petersburg', 'Rostov-on-Don', 'Kaliningrad', 'Vladivostok',
              'Minsk', 'Beijing', 'Delhi', 'Istanbul', 'Tokyo', 'London', 'New York']

    start = time.time()
    print(f"Время начала: {time.strftime('%X', time.localtime(start))}")
    main(cities)  # Запуск основной функции
    end = time.time()
    print(f"Время окончания: {time.strftime('%X', time.localtime(end))}")
    print(f"Общее время выполнения: {round(end - start, 2)} секунд")
