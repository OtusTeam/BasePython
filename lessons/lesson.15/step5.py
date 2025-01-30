from pathlib import Path

# p = Path("new_folder_1")
# print('Объект Path:', p)
#
# p.mkdir(exist_ok=True)
# print('Папка создана')

my_folder = Path("new_folder")
if my_folder.exists():
    print(f' {my_folder} - папка уже существует')
else:
    my_folder.mkdir(exist_ok=True)
    print(f' {my_folder} - папка создана')

print('Завершение программы')