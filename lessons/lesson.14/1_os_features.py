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
    os.system("clear")


def create_project_directory(project_name):
    """
    Создает директорию проекта с указанным именем, если она не существует.

    Args:
        project_name (str): Название директории проекта.

    Returns:
        str: Название созданной или существующей директории.
    """
    if not os.path.exists(project_name):
        os.mkdir(project_name)
        logger.info(f"Директория '{project_name}' создана.")
    else:
        logger.info(f"Директория '{project_name}' уже существует.")
    return project_name


def create_files(project_dir):
    """
    Создает файлы в указанной директории проекта.

    Args:
        project_dir (str): Директория, где будут созданы файлы.

    Returns:
        list: Список имен созданных файлов.
    """
    files = ["index.html", "main.css", "app.js"]
    for file in files:
        file_path = os.path.join(project_dir, file)
        with open(file_path, "w") as f:
            f.write(f"// {file}")
        logger.info(f"Файл '{file}' создан в '{project_dir}'.")
    return files


def rename_files(project_dir, files):
    """
    Переименовывает указанные файлы в директории проекта.

    Args:
        project_dir (str): Директория проекта.
        files (list): Список имен файлов для переименования.
    """
    for file in files:
        old_file_path = os.path.join(project_dir, file)
        new_file_path = os.path.join(project_dir, f"new_{file}")
        os.rename(old_file_path, new_file_path)
        logger.info(f"Файл '{file}' переименован в 'new_{file}'.")


def check_existence(project_dir, files):
    """
    Проверяет существование указанных файлов и директории.

    Args:
        project_dir (str): Директория проекта.
        files (list): Список имен файлов для проверки.
    """
    for file in files:
        new_file_path = os.path.join(project_dir, f"new_{file}")
        if os.path.exists(new_file_path):
            logger.info(f"Файл '{new_file_path}' существует.")
        else:
            logger.warning(f"Файл '{new_file_path}' не найден.")

    if os.path.exists(project_dir):
        logger.info(f"Директория '{project_dir}' существует.")
    else:
        logger.warning(f"Директория '{project_dir}' не найдена.")


def get_and_change_directory(project_dir):
    """
    Получает текущую рабочую директорию и меняет ее на указанную.

    Args:
        project_dir (str): Директория, на которую нужно сменить текущую.
    """
    current_dir = os.getcwd()
    logger.info(f"Текущая рабочая директория: {current_dir}")
    os.chdir(project_dir)
    logger.info(f"Рабочая директория изменена на: {os.getcwd()}")


def delete_file(file_to_delete):
    """
    Удаляет указанный файл, если он существует.

    Args:
        file_to_delete (str): Путь к файлу для удаления.
    """
    if os.path.exists(file_to_delete):
        os.remove(file_to_delete)
        logger.info(f"Файл '{file_to_delete}' удален.")
    else:
        logger.warning(f"Файл '{file_to_delete}' не найден.")


def delete_empty_directory(dir_to_delete):
    """
    Удаляет пустую директорию, если она существует.

    Args:
        dir_to_delete (str): Путь к директории для удаления.
    """
    if os.path.exists(dir_to_delete):
        os.rmdir(dir_to_delete)
        logger.info(f"Директория '{dir_to_delete}' удалена.")
    else:
        logger.warning(f"Директория '{dir_to_delete}' не найдена.")


def walk_directory():
    """
    Обходит дерево директорий и выводит информацию о подкаталогах и файлах.
    """
    for root, dirs, files in os.walk("my_new_project"):
        logger.info(f"Текущая директория: {root}")
        logger.info(f"Подкаталоги: {dirs}")
        logger.info(f"Файлы: {files}")


def get_file_size(project_dir):
    """
    Получает размер указанного файла в байтах.

    Args:
        project_dir (str): Директория проекта.
    """
    file_path = os.path.join(project_dir, "new_index.html")
    if os.path.exists(file_path):
        file_size = os.path.getsize(file_path)
        logger.info(f"Размер файла '{file_path}': {file_size} байт")
    else:
        logger.warning(f"Файл '{file_path}' не найден.")


def get_absolute_path():
    """
    Получает и выводит абсолютный путь к файлу.
    """
    relative_path = "new_main.css"
    absolute_path = os.path.abspath(relative_path)
    logger.info(f"Абсолютный путь: {absolute_path}")


def create_log_file(project_dir):
    """
    Создает лог-файл в директории проекта.

    Args:
        project_dir (str): Директория проекта.

    Returns:
        str: Путь к созданному лог-файлу.
    """
    log_dir = os.path.join(project_dir, "logs")
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, "setup.log")
    os.system(f'echo "Setup log created on $(date)" > {log_file}')
    logger.info(f"Файл логов '{log_file}' создан.")
    return log_file


def list_directory_contents():
    """
    Выводит список файлов и директорий в текущем каталоге.
    """
    result = os.popen("ls").read()
    logger.info("Список файлов и директорий в текущем каталоге:")
    logger.info(result)


def read_log_file(log_file):
    """
    Читает и выводит содержимое указанного лог-файла.

    Args:
        log_file (str): Путь к лог-файлу.
    """
    log_content = os.popen(f"cat {log_file}").read()
    logger.info(f"Содержимое лог-файла '{log_file}':")
    logger.info(log_content)


DIR_NAME = "new_directory"

if __name__ == "__main__":
    # Очищаем терминал
    clear_terminal()

    # Создаем директорию проекта
    """project_dir = create_project_directory(DIR_NAME)

        # Создаем файлы в директории проекта
    files = create_files(project_dir)

    # Переименовываем созданные файлы
    rename_files(project_dir, files)

    # Проверяем существование файлов и директории
    check_existence(project_dir, files)

    # Получаем текущую рабочую директорию и меняем ее на директорию проекта
    get_and_change_directory(project_dir)

    # Удаляем ненужный файл, если он существует
    delete_file("unwanted_file.txt")

    # Удаляем пустую директорию, если она существует
    delete_empty_directory("empty_directory")

    # Обходим дерево директорий и выводим его содержимое
    walk_directory()

    # Получаем размер файла и выводим его
    get_file_size(project_dir)

    # Получаем и выводим абсолютный путь к файлу
    get_absolute_path()

    # Создаем лог-файл и записываем в него информацию
    log_file = create_log_file(project_dir)

    # Выводим содержимое текущей директории
    list_directory_contents()

    # Читаем и выводим содержимое лог-файла
    read_log_file(log_file)"""
