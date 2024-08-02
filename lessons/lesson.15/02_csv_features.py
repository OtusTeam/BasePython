import os
from functools import partial
from termcolor import colored
import csv

os.system('clear')

# Функция для цветного вывода
def print_color(message, color):
    print(colored(message, color))

# Создание новых функций для цветного вывода
print_green = partial(print_color, color='green')
print_cyan = partial(print_color, color='cyan')

'''Чтение CSV-файлов'''

# Создаем пример CSV-файл
csv_content = """Name,Age,City
Alice,30,New York
Bob,25,Los Angeles
Charlie,35,Chicago
Diana,40,Houston
"""

with open('data.csv', 'w') as csvfile:
    csvfile.write(csv_content)

# Чтение CSV-файла
print_green("Чтение CSV-файла:")
with open('data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    headers = next(csvreader)
    print_cyan(f"Заголовки: {headers}")
    for row in csvreader:
        print(row)

'''Запись в CSV-файлы'''

# Запись в CSV-файл
print_green("Запись в CSV-файл:")
with open('data.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Name', 'Age', 'City'])
    csvwriter.writerow(['Alice', 30, 'New York'])
    csvwriter.writerow(['Bob', 25, 'Los Angeles'])

# Чтение записанных данных для проверки
with open('data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        print(row)

'''Использование DictReader и DictWriter'''

# Использование DictReader для чтения CSV-файла
print_green("Чтение CSV-файла с использованием DictReader:")
with open('data.csv', 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        print(dict(row))

# Использование DictWriter для записи в CSV-файл
print_green("Запись в CSV-файл с использованием DictWriter:")
with open('data.csv', 'w', newline='') as csvfile:
    fieldnames = ['Name', 'Age', 'City']
    csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    csvwriter.writeheader()
    csvwriter.writerow({'Name': 'Charlie', 'Age': 35, 'City': 'Chicago'})
    csvwriter.writerow({'Name': 'Diana', 'Age': 40, 'City': 'Houston'})

# Чтение записанных данных для проверки
with open('data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        print(row)
