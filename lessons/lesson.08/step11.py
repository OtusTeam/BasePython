# from os import path
from pathlib import Path


# #linux
# with open("data/cat.jpg", "rb") as my_file:
# #windows
# with open("data\\cat.jpg", "rb") as my_file:
#     data = my_file.read(10)



my_path = Path("data/cat.jpg")
print(my_path)
print(type(my_path))

print(my_path.name)
print(my_path.parent)
print(my_path.parent.parent)
print(my_path.is_file())
print(my_path.is_dir())

print(my_path.resolve())
print(my_path.resolve().parent.parent.parent)

new_path = Path(__file__).parent
print(new_path)

dir_path = new_path / "data"
print(dir_path)

file_path = dir_path / "cat.jpg"
print(file_path)


file_path1 = dir_path / "cat1.jpg"
print(file_path1)


if file_path.exists():
    print(123)

if file_path1.exists():
    print(345)


dir_path_1 = new_path / "data123/data345/data567"
print(dir_path_1)

# if not dir_path_1.exists():
#     dir_path_1.mkdir()

dir_path_1.mkdir(exist_ok=True, parents=True)


dir_path_2 = new_path / "data123/data345/data567"
dir_path_2.rmdir()

print("--------------")

text_path = dir_path / "otus.txt"
print(text_path)

my_file =  open(text_path, "rt", encoding="utf-8")
data = my_file.read()
my_file.close()
print(data)