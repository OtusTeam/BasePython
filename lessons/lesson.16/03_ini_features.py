import os
import configparser
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


def create_example_ini(file_path):
    """
    Создаёт пример INI-файл с заданным содержимым.

    Args:
        file_path (str): Путь к создаваемому INI-файлу.
    """
    ini_content = """[DEFAULT]
ServerAliveInterval = 45
Compression = yes
CompressionLevel = 9

[Settings]
parameter = value
another_parameter = another_value
"""
    with open(file_path, 'w') as inifile:
        inifile.write(ini_content)
    logger.info(f"Пример INI-файл '{file_path}' создан.")


def read_ini_file(file_path):
    """
    Читает INI-файл и выводит его содержимое.

    Args:
        file_path (str): Путь к INI-файлу для чтения.
    """
    config = configparser.ConfigParser()
    config.read(file_path)
    logger.info(f"Секция DEFAULT: {dict(config['DEFAULT'])}")
    logger.info(f"Секция Settings: {dict(config['Settings'])}")
    logger.info(f"Значение параметра 'parameter': {config['Settings']['parameter']}")


def write_ini_file(file_path, data):
    """
    Записывает данные в INI-файл.

    Args:
        file_path (str): Путь к INI-файлу для записи.
        data (dict): Данные для записи в формате, совместимом с ConfigParser.
    """
    config = configparser.ConfigParser()
    for section, values in data.items():
        config[section] = values
    with open(file_path, 'w') as configfile:
        config.write(configfile)
    logger.info(f"Данные записаны в INI-файл '{file_path}'.")


def modify_ini_file(file_path, section, parameter, new_value):
    """
    Изменяет значение параметра в INI-файле и записывает изменения.

    Args:
        file_path (str): Путь к INI-файлу для изменения.
        section (str): Секция, в которой нужно изменить параметр.
        parameter (str): Параметр, который нужно изменить.
        new_value (str): Новое значение параметра.
    """
    config = configparser.ConfigParser()
    config.read(file_path)
    if section in config and parameter in config[section]:
        config[section][parameter] = new_value
        with open(file_path, 'w') as configfile:
            config.write(configfile)
        logger.info(f"Параметр '{parameter}' в секции '{section}' изменён на '{new_value}'.")
    else:
        logger.warning(f"Секция '{section}' или параметр '{parameter}' не найдены в '{file_path}'.")


def verify_ini_file(file_path):
    """
    Читает и выводит содержимое INI-файла для проверки.

    Args:
        file_path (str): Путь к INI-файлу для проверки.
    """
    config = configparser.ConfigParser()
    config.read(file_path)
    logger.info(f"Содержимое файла '{file_path}':")
    for section in config.sections():
        logger.info(f"Секция {section}: {dict(config[section])}")


if __name__ == "__main__":
    clear_terminal()

    # Путь к INI-файлу
    ini_file_path = 'config.ini'

    # 1. Создание примерного INI-файла
    create_example_ini(ini_file_path)

    # 2. Чтение INI-файла
    read_ini_file(ini_file_path)

    # 3. Запись новых данных в INI-файл
    new_data = {
        'DEFAULT': {
            'ServerAliveInterval': '60',
            'Compression': 'no',
            'CompressionLevel': '0',
        },
        'Settings': {
            'parameter': 'another_value',
            'another_parameter': 'True',
        },
    }
    write_ini_file(ini_file_path, new_data)

    # 4. Чтение INI-файла после записи
    read_ini_file(ini_file_path)

    # 5. Изменение значения параметра
    modify_ini_file(ini_file_path, 'Settings', 'parameter', 'new_value')

    # 6. Проверка INI-файла после изменений
    verify_ini_file(ini_file_path)
