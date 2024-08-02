import os

os.system("clear")
import asyncio

async def fetch_data(task_name):
    print(f"{task_name} начата")
    try:
        await asyncio.sleep(5)  # Увеличил время для наглядности отмены
        print(f"{task_name} завершена")
        return f"Результат {task_name}"
    except asyncio.CancelledError:
        print(f"{task_name} отменена")
        raise

async def main():
    tasks = ['Задача 1', 'Задача 2', 'Задача 3']
    
    # Создание списка задач для выполнения
    tasks = [asyncio.create_task(fetch_data(task)) for task in tasks]
    
    # Отмена одной из задач через некоторое время
    await asyncio.sleep(1)
    tasks[0].cancel()  # Отменяем первую задачу

    results = []
    for task in tasks:
        try:
            result = await task  # Явно ожидаем завершения каждой задачи
            results.append(result)
        except asyncio.CancelledError:
            results.append(f"{task.get_name()} отменена")

    for result in results:
        print(result)

asyncio.run(main())
