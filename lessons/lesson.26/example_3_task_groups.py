import os

os.system("clear")
import asyncio

async def fetch_data(task_name):
    print(f"{task_name} начата")
    try:
        await asyncio.sleep(5)  # Имитация длительной задачи
        print(f"{task_name} завершена")
        return f"Результат {task_name}"
    except asyncio.CancelledError:
        print(f"{task_name} отменена")
        raise  # Передаем исключение в вызывающую функцию

async def main():
    tasks = ['Задача 1', 'Задача 2', 'Задача 3']

    async with asyncio.TaskGroup() as tg:
        # Создание задач в группе
        task_objects = [tg.create_task(fetch_data(task)) for task in tasks]

        await asyncio.sleep(1)
        task_objects[0].cancel()  # Отменяем первую задачу

    # Результаты задач
    results = []
    for task in task_objects:
        try:
            result = await task
            results.append(result)
        except asyncio.CancelledError:
            results.append(f"{task.get_name()} отменена")

    for result in results:
        print(result)

asyncio.run(main())
