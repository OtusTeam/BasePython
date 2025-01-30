import os

cur_dir  = os.getcwd()
items_list = os.listdir(cur_dir)
print(items_list)

file_to_del = 'temp.py'
if os.path.exists(file_to_del):
    os.remove(file_to_del)   # удаляем файл
    print(f' {file_to_del} - файл удален')


file_to_ren = 'еуьз.py'
if os.path.exists(file_to_ren):
    os.rename(file_to_ren, 'temp.py')   # переименовываем файл
    print(f' {file_to_ren} - файл переименован')