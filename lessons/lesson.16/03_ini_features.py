import os
from functools import partial
from termcolor import colored
import configparser

os.system('clear')

# # Функция для цветного вывода
# def print_color(message, color):
#     print(colored(message, color))
# 
# # Создание новых функций для цветного вывода
# print_green = partial(print_color, color='green')
# 
# '''Чтение INI-файлов'''
# 
# # Создаем пример INI-файла
# ini_content = """[DEFAULT]
# ServerAliveInterval = 45
# Compression = yes
# CompressionLevel = 9
# 
# [Settings]
# parameter = value
# another_parameter = another_value
# """
# 
# with open('config.ini', 'w') as inifile:
#     inifile.write(ini_content)
# 
# # Чтение INI-файла
# print_green("Чтение INI-файла:")
# config = configparser.ConfigParser()
# config.read('config.ini')
# 
# print("Секция DEFAULT:", dict(config['DEFAULT']))
# print("Секция Settings:", dict(config['Settings']))
# print("Значение параметра:", config['Settings']['parameter'])
# 
# '''Запись в INI-файлы'''
# config = dict(config)
# print(config)
# # Создание объекта ConfigParser
# config = configparser.ConfigParser()
# 
# # Добавление данных
# config['DEFAULT'] = {
#     'ServerAliveInterval': '60',
#     'Compression': 'no',
#     'CompressionLevel': '0'
# }
# 
# config['Settings'] = {
#     'parameter': 'another_value',
#     'another_parameter': 'True'
# }
# 
# # Запись в INI-файл
# print_green("Запись в INI-файл:")
# with open('config.ini', 'w') as configfile:
#     config.write(configfile)
# 
# # Чтение записанных данных для проверки
# config.read('config.ini')
# print("Секция DEFAULT:", dict(config['DEFAULT']))
# print("Секция Settings:", dict(config['Settings']))
# print("Значение параметра:", config['Settings']['parameter'])
# # 
# '''Изменение и запись значений в INI-файл'''
# 
# # Изменение значения параметра
# config['Settings']['parameter'] = 'new_value'
# 
# # Запись изменений обратно в файл
# print_green("Запись изменений в INI-файл:")
# with open('config.ini', 'w') as configfile:
#     config.write(configfile)
# 
# # Чтение записанных данных для проверки
# config.read('config.ini')
# print("Секция Settings после изменения:", dict(config['Settings']))
