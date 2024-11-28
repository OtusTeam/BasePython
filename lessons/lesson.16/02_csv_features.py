import os
import csv
import logging

# Настройка логгера
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger()


def clear_terminal():
    """
    Очищает терминал.
    """
    os.system('clear')


def create_example_csv(file_path):
    """
    Создаёт пример CSV-файл с заданным содержимым.

    Args:
        file_path (str): Путь к создаваемому CSV-файлу.
    """
    csv_content = """Name,Age,City
Alice,30,New York
Bob,25,Los Angeles
Charlie,35,Chicago
Diana,40,Houston
"""
    with open(file_path, 'w') as csvfile:
        csvfile.write(csv_content)
    logger.info(f"Пример CSV-файл '{file_path}' создан.")


def read_csv(file_path):
    """
    Читает CSV-файл и выводит его содержимое построчно.

    Args:
        file_path (str): Путь к CSV-файлу для чтения.
    """
    logger.info(f"Чтение CSV-файла '{file_path}':")
    try:
        with open(file_path, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            headers = next(csvreader)
            logger.info(f"Заголовки: {headers}")
            for row in csvreader:
                logger.info(f"Строка: {row}")
    except FileNotFoundError:
        logger.error(f"Файл '{file_path}' не найден.")
    except Exception as e:
        logger.error(f"Ошибка при чтении CSV-файла '{file_path}': {e}")


def write_to_csv(file_path, data):
    """
    Записывает данные в CSV-файл.

    Args:
        file_path (str): Путь к CSV-файлу для записи.
        data (list): Список строк для записи в файл.
    """
    logger.info(f"Запись данных в CSV-файл '{file_path}':")
    try:
        with open(file_path, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(data)
        logger.info(f"Данные успешно записаны в файл '{file_path}'.")
    except Exception as e:
        logger.error(f"Ошибка при записи в CSV-файл '{file_path}': {e}")


def read_csv_with_dictreader(file_path):
    """
    Читает CSV-файл с использованием DictReader.

    Args:
        file_path (str): Путь к CSV-файлу для чтения.
    """
    logger.info(f"Чтение CSV-файла '{file_path}' с использованием DictReader:")
    try:
        with open(file_path, 'r') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                logger.info(f"Строка: {row}")
    except FileNotFoundError:
        logger.error(f"Файл '{file_path}' не найден.")
    except Exception as e:
        logger.error(f"Ошибка при чтении CSV-файла '{file_path}': {e}")


def write_to_csv_with_dictwriter(file_path, data, append=False):
    """
    Записывает данные в CSV-файл с использованием DictWriter.

    Args:
        file_path (str): Путь к CSV-файлу для записи.
        data (list): Список словарей для записи.
        append (bool): Если True, добавляет данные в конец файла, иначе перезаписывает.
    """
    mode = 'a' if append else 'w'
    logger.info(f"Запись данных в CSV-файл '{file_path}' с использованием DictWriter:")
    try:
        with open(file_path, mode, newline='') as csvfile:
            fieldnames = data[0].keys()
            csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if not append or os.path.getsize(file_path) == 0:
                csvwriter.writeheader()
            csvwriter.writerows(data)
        logger.info(f"Данные успешно записаны в файл '{file_path}'.")
    except Exception as e:
        logger.error(f"Ошибка при записи в CSV-файл '{file_path}': {e}")


if __name__ == "__main__":
    clear_terminal()

    # Путь к CSV-файлу
    csv_file_path = 'data.csv'

    # 1. Создание примерного CSV-файла
    create_example_csv(csv_file_path)

    # 2. Чтение созданного CSV-файла
    read_csv(csv_file_path)

    # 3. Запись новых данных в CSV-файл
    new_data = [
        ['Name', 'Age', 'City'],
        ['Alice', 30, 'New York'],
        ['Bob', 25, 'Los Angeles']
    ]
    write_to_csv(csv_file_path, new_data)

    # 4. Чтение записанного CSV-файла
    read_csv(csv_file_path)

    # 5. Чтение CSV-файла с использованием DictReader
    read_csv_with_dictreader(csv_file_path)

    # 6. Запись данных с использованием DictWriter
    additional_data = [
        {'Name': 'Charlie', 'Age': 35, 'City': 'Chicago'},
        {'Name': 'Diana', 'Age': 40, 'City': 'Houston'}
    ]
    write_to_csv_with_dictwriter(csv_file_path, additional_data, append=True)

    # 7. Чтение файла после добавления данных
    read_csv(csv_file_path)
