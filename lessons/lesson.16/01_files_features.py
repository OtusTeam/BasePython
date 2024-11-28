import os
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


def create_and_write_file(file_path):
    """
    Создает файл и записывает в него данные.

    Args:
        file_path (str): Путь к создаваемому файлу.
    """
    with open(file_path, 'w') as file:
        file.write("Hello, world!\n")
        file.write("This is a test file.\n")
    logger.info(f"Файл '{file_path}' создан и записан.")


def read_file(file_path):
    """
    Считывает и выводит содержимое файла.

    Args:
        file_path (str): Путь к файлу для чтения.
    """
    with open(file_path, 'r') as file:
        content = file.read()
        logger.info(f"Содержимое файла '{file_path}':\n{content}")

def safe_read_file(file_path):
    """
    Безопасно считывает содержимое файла, обрабатывая возможные ошибки.

    Args:
        file_path (str): Путь к файлу для чтения.
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            logger.info(f"Содержимое файла '{file_path}':\n{content}")
    except FileNotFoundError:
        logger.error(f"Файл '{file_path}' не найден.")
    except PermissionError:
        logger.error(f"Нет доступа к файлу '{file_path}'.")
    except Exception as e:
        logger.error(f"Произошла ошибка при чтении файла '{file_path}': {e}")


def read_file_line_by_line(file_path):
    """
    Читает файл построчно с помощью цикла.

    Args:
        file_path (str): Путь к файлу для чтения.
    """
    with open(file_path, 'r') as file:
        logger.info(f"Чтение файла '{file_path}' построчно:")
        for line in file:
            logger.info(line.strip())


def read_file_with_readline(file_path):
    """
    Читает файл построчно с использованием readline().

    Args:
        file_path (str): Путь к файлу для чтения.
    """
    with open(file_path, 'r') as file:
        logger.info(f"Чтение файла '{file_path}' с помощью readline():")
        line = file.readline()
        while line:
            logger.info(line.strip())
            line = file.readline()


def append_to_file(file_path):
    """
    Дополняет файл новой строкой.

    Args:
        file_path (str): Путь к файлу для дополнения.
    """
    with open(file_path, 'a') as file:
        file.write("Appending new line.\n")
    logger.info(f"Файл '{file_path}' дополнен новой строкой.")


def read_file_in_chunks(file_path, chunk_size=3):
    """
    Генератор для чтения файла частями.

    Args:
        file_path (str): Путь к файлу для чтения.
        chunk_size (int): Размер части для чтения.

    Yields:
        str: Часть содержимого файла.
    """
    with open(file_path, 'r') as file:
        while chunk := file.read(chunk_size):
            yield chunk


def read_large_file_in_chunks(file_path, chunk_size=3):
    """
    Читает файл частями, используя генератор.

    Args:
        file_path (str): Путь к файлу для чтения.
        chunk_size (int): Размер части для чтения.
    """
    logger.info(f"Чтение файла '{file_path}' частями (chunk_size={chunk_size}):")
    for chunk in read_file_in_chunks(file_path, chunk_size):
        logger.info(chunk.strip())


if __name__ == "__main__":
    clear_terminal()

    # Путь к файлу
    file_path = 'example.txt'

    # Проверяем, существует ли файл, и удаляем его, если он существует
    if os.path.exists(file_path):
        os.remove(file_path)
        logger.info(f"Файл '{file_path}' удален.")

    # Создание и запись данных в файл
    create_and_write_file(file_path)

    # Чтение файла полностью
    read_file(file_path)

    # Чтение файла с обработкой исключений
    safe_read_file(file_path)

    # Чтение файла построчно
    read_file_line_by_line(file_path)

    # Чтение файла построчно с использованием readline()
    read_file_with_readline(file_path)

    # Дополнение файла
    append_to_file(file_path)

    # Чтение дополненного файла
    read_file(file_path)

    # Чтение файла частями
    read_large_file_in_chunks(file_path, chunk_size=5)
