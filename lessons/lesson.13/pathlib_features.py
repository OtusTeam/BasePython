from pathlib import Path
import shutil
import os

os.system('clear')

'''
Для лучшего понимания скрывайте многострочными комментариями код по частям
'''

# 1. Создание директории для нового проекта
project_dir = Path('my_new_project')

if not project_dir.exists():
    project_dir.mkdir()
    print(f"Директория '{project_dir}' создана.")
else:
    print(f"Директория '{project_dir}' уже существует.")

# 2. Создание файлов в этой директории
files = ['index.html', 'main.css', 'app.js']
for file_name in files:
    file_path = project_dir / file_name
    file_path.write_text(f'// {file_name}')
    print(f"Файл '{file_name}' создан в '{project_dir}'.")

# 3. Переименование файлов
for file_name in files:
    old_file_path = project_dir / file_name
    new_file_path = project_dir / f'new_{file_name}'
    old_file_path.rename(new_file_path)
    print(f"Файл '{file_name}' переименован в 'new_{file_name}'.")

# 4. Проверка существования файлов и директорий
for file_name in files:
    new_file_path = project_dir / f'new_{file_name}'
    if new_file_path.exists():
        print(f"Файл '{new_file_path}' существует.")
    else:
        print(f"Файл '{new_file_path}' не найден.")

# Проверка существования директории
if project_dir.exists():
    print(f"Директория '{project_dir}' существует.")
else:
    print(f"Директория '{project_dir}' не найдена.")

# 5. Удаление непустого каталога
# Создание дополнительной директории для логов
log_dir = project_dir / 'logs'
log_dir.mkdir(exist_ok=True)
print(f"Директория для логов '{log_dir}' создана.")

# Создание файла в каталоге логов
log_file = log_dir / 'setup.log'
log_file.write_text('Setup log content')
print(f"Файл логов '{log_file}' создан.")

# Удаление непустого каталога
if project_dir.exists() and project_dir.is_dir():
    shutil.rmtree(project_dir)
    print(f"Каталог '{project_dir}' и его содержимое удалены.")
else:
    print(f"Каталог '{project_dir}' не существует или не является директорией.")

# 6. Рекурсивный обход директорий
# Создание новой структуры директорий и файлов для демонстрации
project_dir.mkdir()
sub_dir = project_dir / 'subdir'
sub_dir.mkdir()
(sample_file := sub_dir / 'sample.txt').write_text('Sample content')

# Рекурсивный обход директорий
for file in project_dir.rglob('*'):
    print(f"Найден файл или директория: {file}")
