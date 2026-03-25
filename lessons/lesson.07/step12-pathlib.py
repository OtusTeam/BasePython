from pathlib import Path


# path_obj = Path('data123/')
# # path_obj = Path('data')
#
# # if path_obj.exists():
# #     path_obj.mkdir(exist_ok=True)
#
# path_obj.mkdir(exist_ok=True)


path_obj = Path('data')
file_path = path_obj / 'info.txt'
abs_path = file_path.resolve()
# abs_path = path_obj.resolve()
# print(abs_path.parent.parent.parent)
print(abs_path)

