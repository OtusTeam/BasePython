import os

os.system("clear")

"""
Внимание, для работы необходимо установить библиотеку termcolor:
pip3 install termcolor
"""
import asyncio
from termcolor import colored
import time

start_time = time.time()  # Время начала выполнения программы


# Функция для вывода текущего времени относительно начала выполнения программы
def current_time():
    return round(time.time() - start_time, 2)


# Асинхронная функция для записи заказа
async def take_order(order):
    print(colored(f"[{current_time()}s] Официант записывает заказ {order}", "green"))
    await asyncio.sleep(1)  # Имитация времени на запись заказа
    print(colored(f"[{current_time()}s] Официант закончил запись заказа {order}", "green"))


# Асинхронная функция для ожидания приготовления заказа
async def wait_for_food(order, cooking_time):
    print(colored(f"[{current_time()}s] Официант ожидает приготовления заказа {order}","yellow"))
    await asyncio.sleep(cooking_time)  # Имитация времени ожидания приготовления
    print(colored(f"[{current_time()}s] Заказ {order} готов", "yellow"))


# Асинхронная функция для подачи заказа
async def serve_order(order):
    print(colored(f"[{current_time()}s] Официант подает заказ {order}", "red"))
    await asyncio.sleep(1)  # Имитация времени на подачу заказа
    print(colored(f"[{current_time()}s] Официант подал заказ {order}", "red"))


# Асинхронная функция, выполняющая все три этапа для одного заказа
async def handle_order(order, cooking_time):
    await take_order(order)  # Вызов функции записи заказа
    await wait_for_food(order, cooking_time)  # Вызов функции ожидания приготовления
    await serve_order(order)  # Вызов функции подачи заказа


# Основная асинхронная функция
async def main():
    # Словарь заказов и времени приготовления для каждого из них
    orders = {
        "стейк": 5,
        "цезарь": 1,
        "бургер": 2,
    }

    # Создание списка задач для каждого заказа
    tasks = [
        handle_order(order, cooking_time) for order, cooking_time in orders.items()
    ]

    # Ожидание выполнения всех задач параллельно
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    start = time.time()  # Запоминаем время начала выполнения программы
    print(f"Время начала: {time.strftime('%X', time.localtime(start))}")
    asyncio.run(main())  # Запуск асинхронной функции main
    end = time.time()  # Запоминаем время окончания выполнения программы
    print(f"Время окончания: {time.strftime('%X', time.localtime(end))}")
    print(f"Общее время выполнения: {round(end-start, 2)} секунд")
