import os
from pathlib import Path
import shutil
import logging

# Настройка логгера
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def clear_terminal():
    """
    Очищает терминал.
    """
    os.system("clear")


def create_project_directory():
    """
    Создает директорию проекта, если она не существует.

    Returns:
        Path: Путь к созданной или существующей директории проекта.
    """
    project_dir = Path("my_new_project")
    if not project_dir.exists():
        project_dir.mkdir()
        logger.info(f"Директория '{project_dir}' создана.")
    else:
        logger.info(f"Директория '{project_dir}' уже существует.")
    return project_dir


def create_files(project_dir):
    """
    Создает файлы в указанной директории проекта.

    Args:
        project_dir (Path): Директория, где будут созданы файлы.

    Returns:
        list: Список имен созданных файлов.
    """
    files = ["index.html", "main.css", "app.js"]
    for file_name in files:
        file_path = project_dir / file_name
        file_path.write_text(f"// {file_name}")
        logger.info(f"Файл '{file_name}' создан в '{project_dir}'.")
    return files


def rename_files(project_dir, files):
    """
    Переименовывает файлы в указанной директории.

    Args:
        project_dir (Path): Директория проекта.
        files (list): Список имен файлов для переименования.
    """
    for file_name in files:
        old_file_path = project_dir / file_name
        new_file_path = project_dir / f"new_{file_name}"
        old_file_path.rename(new_file_path)
        logger.info(f"Файл '{file_name}' переименован в 'new_{file_name}'.")


def check_existence(project_dir, files):
    """
    Проверяет существование указанных файлов и директорий.

    Args:
        project_dir (Path): Директория проекта.
        files (list): Список имен файлов для проверки.
    """
    for file_name in files:
        new_file_path = project_dir / f"new_{file_name}"
        if new_file_path.exists():
            logger.info(f"Файл '{new_file_path}' существует.")
        else:
            logger.warning(f"Файл '{new_file_path}' не найден.")
    if project_dir.exists():
        logger.info(f"Директория '{project_dir}' существует.")
    else:
        logger.warning(f"Директория '{project_dir}' не найдена.")


def manage_log_directory(project_dir):
    """
    Создает лог-директорию, создает файл логов и удаляет директорию проекта.

    Args:
        project_dir (Path): Директория проекта.
    """
    log_dir = project_dir / "logs"
    log_dir.mkdir(exist_ok=True)
    logger.info(f"Директория для логов '{log_dir}' создана.")
    log_file = log_dir / "setup.log"
    log_file.write_text("Setup log content")
    logger.info(f"Файл логов '{log_file}' создан.")

    if project_dir.exists() and project_dir.is_dir():
        shutil.rmtree(project_dir)
        logger.info(f"Каталог '{project_dir}' и его содержимое удалены.")
    else:
        logger.warning(
            f"Каталог '{project_dir}' не существует или не является директорией."
        )


def create_sample_structure():
    """
    Создает пример структуры директорий и файлов для демонстрации.

    Returns:
        tuple: Путь к директории проекта и созданному файлу.
    """
    project_dir = Path("my_new_project")
    project_dir.mkdir(exist_ok=True)
    sub_dir = project_dir / "subdir"
    sub_dir.mkdir(exist_ok=True)
    sample_file = sub_dir / "sample.txt"
    sample_file.write_text("Sample content")
    return project_dir, sample_file


def walk_through_directories(project_dir):
    """
    Обходит директории и выводит найденные файлы и подкаталоги.

    Args:
        project_dir (Path): Директория проекта.
    """
    all_files_and_dirs = project_dir.rglob("*")
    logger.info(f"Содержимое директории {project_dir}:")
    for file in all_files_and_dirs:
        logger.info(f"Найден файл или директория: {file}")


def copy_and_move_files(project_dir, sample_file):
    """
    Копирует указанный файл в корень проекта.

    Args:
        project_dir (Path): Директория проекта.
        sample_file (Path): Путь к файлу для копирования.
    """
    copied_file_path = project_dir / "copied_sample.txt"
    shutil.copy(sample_file, copied_file_path)
    logger.info(f"Файл '{sample_file}' скопирован в '{copied_file_path}'.")


def delete_file(sample_file):
    """
    Удаляет указанный файл.

    Args:
        sample_file (Path): Путь к файлу для удаления.
    """
    if sample_file.exists():
        sample_file.unlink()
        logger.info(f"Файл '{sample_file}' удален.")


def create_archive(project_dir):
    """
    Создает архив из указанной директории.

    Args:
        project_dir (Path): Директория для архивирования.
    """
    archive_path = shutil.make_archive("backup", "zip", project_dir)
    logger.info(f"Архив '{archive_path}' создан.")


# Основной блок программы
if __name__ == "__main__":
    clear_terminal()
"""
    # Создаем проект и файлы
    project_dir = create_project_directory()
    files = create_files(project_dir)
    rename_files(project_dir, files)
    check_existence(project_dir, files)

    # Управляем логами и удаляем каталог
    manage_log_directory(project_dir)

    # Создаем структуру для демонстрации обхода
    project_dir, sample_file = create_sample_structure()
    walk_through_directories(project_dir)

    # Копируем и удаляем файлы, создаем архив
    copy_and_move_files(project_dir, sample_file)
    delete_file(sample_file)
    create_archive(project_dir)
    walk_through_directories(Path('.'))
    """
