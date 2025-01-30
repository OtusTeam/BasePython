from pathlib import Path


file_path = Path('text.txt')

file_path.write_text('Hello world111!')
print('Файл записан')


if file_path.exists():
    print('Файл существует')
    content = file_path.read_text()
    print(content)
else:
    print('Файл не существует')


if file_path.exists():
    print('Файл существует')
    file_path.unlink()
else:
    print('Файл не существует')


file_path_1 = Path('temp.py')
file_path_2 = Path('temp123.py')

if file_path_1.exists():
    print('Файл существует')
    file_path_1.rename(file_path_2)
else:
    print('Файл не существует')
