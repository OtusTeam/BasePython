from pathlib import Path


path_obj = Path('data/text_python.txt')
# path_obj = Path('data')

print(path_obj)
print(path_obj.name)
print(path_obj.parent)
print(path_obj.exists())
print(path_obj.is_file())
print(path_obj.is_dir())



# file_object = open(path_obj, 'r')
# data = file_object.read()
# print(data)
# file_object.close()

# print(data)


