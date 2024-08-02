import os

os.system("clear")

"""
Внимание, для работы необходимо установить библиотеку termcolor:
pip3 install termcolor
"""
import time
from termcolor import colored

start_time = time.time()  # Время начала выполнения программы


# Функция для вывода текущего времени относительно начала выполнения программы
def current_time():
    return round(time.time() - start_time, 2)


# Функция для записи заказа
def take_order(order):
    print(colored(f"[{current_time()}s] Официант записывает заказ {order}", "green"))
    time.sleep(1)  # Имитация времени на запись заказа
    print(colored(f"[{current_time()}s] Официант закончил запись заказа {order}", "green"))


# Функция для ожидания приготовления заказа
def wait_for_food(order, cooking_time):
    print(colored(f"[{current_time()}s] Официант ожидает приготовления заказа {order}","yellow"))
    time.sleep(cooking_time)  # Имитация времени ожидания приготовления
    print(colored(f"[{current_time()}s] Заказ {order} готов", "yellow"))


# Функция для подачи заказа
def serve_order(order):
    print(colored(f"[{current_time()}s] Официант подает заказ {order}", "red"))
    time.sleep(1)  # Имитация времени на подачу заказа
    print(colored(f"[{current_time()}s] Официант подал заказ {order}", "red"))


# Основная функция
def main():
    # Словарь заказов и времени приготовления для каждого из них
    orders = {
        "стейк": 5,
        "цезарь": 1,
        "бургер": 2,
    }

    for order, cooking_time in orders.items():
        take_order(order)
        wait_for_food(order, cooking_time)
        serve_order(order)


if __name__ == "__main__":
    start = time.time()  # Запоминаем время начала выполнения программы
    print(f"Время начала: {time.strftime('%X', time.localtime(start))}")
    main()  # Запуск основной функции
    end = time.time()  # Запоминаем время окончания выполнения программы
    print(f"Время окончания: {time.strftime('%X', time.localtime(end))}")
    print(f"Общее время выполнения: {round(end-start, 2)} секунд")
