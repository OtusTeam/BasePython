from pathlib import Path
from tempfile import TemporaryDirectory
import shutil
import os

os.system("clear")

# 1. Создание директории для нового проекта
project_dir = Path("my_new_project")

# if not project_dir.exists():
#     project_dir.mkdir()
#     print(f"Директория '{project_dir}' создана.")
# else:
#     print(f"Директория '{project_dir}' уже существует.")

# 2. Создание файлов в этой директории
# files = ["index.html", "main.css", "app.js"]
# for file_name in files:
#     file_path = project_dir / file_name
#     file_path.write_text(f'{file_name}')
#     # print(f"Файл '{file_name}' создан в '{project_dir}'.")

# 3. Переименование файлов
# for file_name in files:
#     old_file_path = project_dir / file_name
#     # print(f'---> {old_file_path}')
#     new_file_path = project_dir / f'new_{file_name}'
#     old_file_path.rename(new_file_path)
#     # print(f"Файл '{file_name}' переименован в 'new_{file_name}'.")

# 4. Проверка существования файлов и директорий
# for file_name in files:
#     new_file_path = project_dir / f'new_{file_name}'
#     if new_file_path.exists():
#         print(f"Файл '{new_file_path}' существует.")
#     else:
#         print(f"Файл '{new_file_path}' не найден.")

# Проверка существования директории
# if project_dir.exists():
#     print(f"Директория '{project_dir}' существует.")
# else:
#     print(f"Директория '{project_dir}' не найдена.")

# # 5. Удаление непустого каталога
# Создание дополнительной директории для логов
# log_dir = project_dir / 'logs'
# log_dir.mkdir(exist_ok=True)
# print(f"Директория для логов '{log_dir}' создана.")

# Создание файла в каталоге логов
# log_file = log_dir / 'setup.log'
# log_file.write_text('Setup log content')
# print(f"Файл логов '{log_file}' создан.")

# Удаление непустого каталога
# if project_dir.exists() and project_dir.is_dir():
#     shutil.rmtree(project_dir)
#     print(f"Каталог '{project_dir}' и его содержимое удалены.")
# else:
#     print(f"Каталог '{project_dir}' не существует или не является директорией.")

# 6. Рекурсивный обход директорий
# Создание новой структуры директорий и файлов для демонстрации
# project_dir.mkdir()
# sub_dir = project_dir / 'subdir'
# sub_dir.mkdir()
# (sample_file := sub_dir / 'sample.txt').write_text('Sample content')

# Рекурсивный обход директорий
# for file in project_dir.rglob('*'):
#     print(f"Найден файл или директория: {file}")

# # 7. Получение имени файла, расширения и родительской директории
file_path = Path("example.txt")
# print(f"Имя файла: {file_path.name}")
# print(f"Расширение файла: {file_path.suffix}")
# print(f"Родительская директория: {file_path.parent}")

# # 8. Преобразование относительного пути в абсолютный
rel_path = Path("my_project")
abs_path = rel_path.resolve()
# print(f"Абсолютный путь: {abs_path}")

# # 9. Изменение прав на файл
# file_path = Path('example.sh')
# file_path.write_text("#!/bin/bash\necho 'Hello, World!'")
# file_path.chmod(0o755)  # Делает файл исполняемым
""" * Оффтопик: Что такое 0o755?
Права доступа к файлам задаются в формате триады: владелец, группа, остальные.
Каждая цифра права складывается из следующих значений:
4 - чтение (r), 2 - запись (w), 1 - выполнение (x).
Комбинации:
    7 - rwx (чтение, запись, выполнение),
    6 - rw- (чтение и запись),
    5 - r-x (чтение и выполнение),
    4 - r-- (только чтение),
    0 - нет прав.
Пример: 0o755 - владелец может читать, писать и выполнять (7), группа и остальные могут только читать и выполнять (5).
"""
# print(f"Права файла '{file_path}' изменены на исполняемые.")

# # 10. Сравнение путей
# path1 = Path("/home/user/my_project")
# path2 = Path("/home/user/my_project/..").resolve()
# print(path2)
# print(f"Пути равны: {path1 == path2}")

# 11. Кросс-платформенность с использованием Path().joinpath()
joined_path = Path('folder')
joined_path.joinpath('subfolder', 'file.txt')
# print(f"Путь к файлу: {joined_path.resolve()}")

# 12. Работа с временными директориями и файлами
# with TemporaryDirectory() as temp_dir:
#     print(f"Создана временная директория: {temp_dir}")
#     temp_path = Path(temp_dir) / 'temp_file.txt'
#     temp_path.write_text("Временный файл создан.")
#     print(f"Файл временной директории: {temp_path}")
#     print(f"Содержимое директории /tmp - {os.popen('ls /tmp').read()}")
#     input('После выхода из контекстного менеджера директория удалится:\n>>> ')
# print(f"Содержимое директории /tmp - {os.popen('ls /tmp').read()}")
