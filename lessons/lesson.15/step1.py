import os
# import pathlib
# import functools
# import itertools
#
# print(dir(os))
# print(dir(pathlib))
# # print(dir(os))
# # print(dir(os))

cur_dir  = os.getcwd()
print(f' {cur_dir} - наша текущая директория')

# Создание новой папки
new_folder = 'new_folder'
os.mkdir(new_folder)    # создаем папку
print(f' {new_folder} - папка создана')
