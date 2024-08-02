import os

os.system("clear")
import asyncio
import time

async def fetch_data(task_name):
    print(f"{task_name} начата")  # Сообщение о начале выполнения задачи
    await asyncio.sleep(2)  # Имитация длительной операции
    print(f"{task_name} завершена")  # Сообщение о завершении задачи

async def main():
    tasks = ['Задача 1', 'Задача 2', 'Задача 3']
    start_time = time.time()
    
    coroutines = [fetch_data(task) for task in tasks]
    await asyncio.gather(*coroutines)
    
    end_time = time.time()
    print(f"Время выполнения: {round(end_time - start_time, 2)} секунд")

if __name__ == '__main__':
    asyncio.run(main())
