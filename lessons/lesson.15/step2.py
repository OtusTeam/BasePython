import os

new_folder = 'new_folder'

# if os.path.exists(new_folder):
#     print(f' {new_folder} - папка уже существует')
# else:
#     os.mkdir(new_folder)    # создаем папку
#     print(f' {new_folder} - папка создана')
#
# print('Завершение программы')


if not os.path.exists(new_folder):
    os.mkdir(new_folder)    # создаем папку
    print(f' {new_folder} - папка создана')

print('Завершение программы')


