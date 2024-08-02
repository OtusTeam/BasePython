import os

os.system("clear")
import time

def fetch_data(task_name):
    print(f"{task_name} начата")  # Сообщение о начале выполнения задачи
    time.sleep(2)  # Имитация длительной операции
    print(f"{task_name} завершена")  # Сообщение о завершении задачи

def main():
    tasks = ['Задача 1', 'Задача 2', 'Задача 3']
    start_time = time.time()
    
    for task in tasks:
        fetch_data(task)
    
    end_time = time.time()
    print(f"Время выполнения: {end_time - start_time} секунд")

if __name__ == '__main__':
    main()
