import os

os.system('clear')

'''
Для лучшего понимания скрывайте многострочными комментариями код по частям
'''

# 1. Создание директории для нового проекта
project_dir = 'my_new_project'

if not os.path.exists(project_dir):
    os.mkdir(project_dir)
    print(f"Директория '{project_dir}' создана.")
else:
    print(f"Директория '{project_dir}' уже существует.")

# 2. Создание файлов в этой директории
files = ['index.html', 'main.css', 'app.js']
for file in files:
    file_path = os.path.join(project_dir, file)
    with open(file_path, 'w') as f:
        f.write(f'// {file}')
    print(f"Файл '{file}' создан в '{project_dir}'.")

# 3. Переименование файлов
for file in files:
    old_file_path = os.path.join(project_dir, file)
    new_file_path = os.path.join(project_dir, f'new_{file}')
    os.rename(old_file_path, new_file_path)
    print(f"Файл '{file}' переименован в 'new_{file}'.")

# 4. Проверка существования файлов и директорий
for file in files:
    new_file_path = os.path.join(project_dir, f'new_{file}')
    if os.path.exists(new_file_path):
        print(f"Файл '{new_file_path}' существует.")
    else:
        print(f"Файл '{new_file_path}' не найден.")

# Проверка существования директории
if os.path.exists(project_dir):
    print(f"Директория '{project_dir}' существует.")
else:
    print(f"Директория '{project_dir}' не найдена.")

# 5. Выполнение системных команд для автоматизации
# Создание дополнительной директории для логов
log_dir = os.path.join(project_dir, 'logs')
os.mkdir(log_dir)
print(f"Директория для логов '{log_dir}' создана.")

# Выполнение системной команды для создания текстового файла с логами
log_file = os.path.join(log_dir, 'setup.log')
os.system(f'echo "Setup log created on $(date)" > {log_file}')
print(f"Файл логов '{log_file}' создан.")

# Выполнение команды и получение результата
result = os.popen('ls').read()
print("Список файлов и директорий в текущем каталоге:")
print(result)

# Дополнительно: вывод содержимого лог-файла
log_content = os.popen(f'cat {log_file}').read()
print(f"Содержимое лог-файла '{log_file}':")
print(log_content)

