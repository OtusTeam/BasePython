import os

os.system("clear")

'''
Внимание!
Для работы необходимо:
1) Установить библиотеку aiohttp
pip3 install aiohttp

2) Получить API ключ с сайта https://home.openweathermap.org регистрируемся,
подтверждаем почту и в письме вам прийдет ключ (активация в течении пары часов)
'''
import asyncio  # Импортируем модуль для асинхронного программирования
import time
from aiohttp import ClientSession  # Импортируем модуль для выполнения асинхронных HTTP-запросов

API_KEY = 'your_api'

# Функция для получения данных о погоде для указанного города
async def get_weather(city):
    async with ClientSession() as session:  # Создаем сессию для выполнения HTTP-запросов
        url = f'http://api.openweathermap.org/data/2.5/weather'  # URL API
        params = {'q': city, 'APPID': API_KEY}  # Параметры запроса, включая город и API ключ

        async with session.get(url=url, params=params) as response:  # Выполняем асинхронный HTTP-запрос
            weather_json = await response.json()  # Получаем JSON ответ
            print(f'{city}: {weather_json["weather"][0]["main"]}')  # Выводим информацию о погоде

# Основная асинхронная функция
async def main(cities_):
    tasks = []
    for city in cities_:  # Перебираем список городов
        tasks.append(asyncio.create_task(get_weather(city)))  # Создаем и добавляем задачи в список

    for task in tasks:  # Ожидаем завершения каждой задачи
        await task

if __name__ == '__main__':
    cities = ['Moscow', 'St. Petersburg', 'Rostov-on-Don', 'Kaliningrad', 'Vladivostok',
              'Minsk', 'Beijing', 'Delhi', 'Istanbul', 'Tokyo', 'London', 'New York']  # Список городов

    start = time.time()
    print(f"Время начала: {time.strftime('%X', time.localtime(start))}")
    asyncio.run(main(cities))  # Запуск основной асинхронной функции
    end = time.time()
    print(f"Время окончания: {time.strftime('%X', time.localtime(end))}")
    print(f"Общее время выполнения: {round(end-start, 2)} секунд")
