# Импорт необходимых модулей
import os
from functools import partial
from termcolor import colored

os.system('clear')

# Функция для цветного вывода
def print_color(message, color):
    print(colored(message, color))

# Создание новых функций для цветного вывода
print_green = partial(print_color, color='green')

# Определяем путь к файлу
file_path = 'example.txt'

# Проверяем, существует ли файл, и удаляем его, если он существует
if os.path.exists(file_path):
    os.remove(file_path)

# Создаем и записываем данные в файл
with open(file_path, 'w') as file:
    file.write("Hello, world!\n")
    file.write("This is a test file.\n")

print_green("Файл создан и записан.")

# Выводим содержимое файла для проверки
with open(file_path, 'r') as file:
    content = file.read()
    print_green("Содержимое файла после записи:")
    print(content)

'''Чтение файла'''

# Чтение всего файла
with open(file_path, 'r') as file:
    content = file.read()
    print_green("Содержимое всего файла:")
    print(content)

# Чтение файла построчно с помощью цикла
with open(file_path, 'r') as file:
    print_green("Чтение файла построчно:")
    for line in file:
        print(line.strip())

# Чтение файла построчно с использованием readline()
with open(file_path, 'r') as file:
    print_green("Чтение файла построчно с помощью readline():")
    line = file.readline()
    while line:
        print(line.strip())
        line = file.readline()

'''Дополнение файла'''

# Дополнение файла
with open(file_path, 'a') as file:
    file.write("Appending new line.\n")

print_green("Файл дополнен.")

# Выводим обновленное содержимое файла для проверки
with open(file_path, 'r') as file:
    content = file.read()
    print_green("Содержимое файла после дополнения:")
    print(content)

'''Работа с большими файлами'''

# Генератор для чтения файла частями
def read_file_in_chunks(file_name, chunk_size=1024):
    with open(file_name, 'r') as file:
        while chunk := file.read(chunk_size):
            yield chunk

# Использование генератора для чтения файла частями
print_green("Чтение файла частями:")
for chunk in read_file_in_chunks(file_path):
    print(chunk.strip())
