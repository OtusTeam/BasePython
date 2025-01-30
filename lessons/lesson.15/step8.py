from pathlib import Path


folder_path = Path('new_folder')
subfolder_path = folder_path / 'subfolder'
sub_subfolder_path = subfolder_path / 'sub_subfolder'
file_path = sub_subfolder_path / 'file.txt'

print(folder_path)
print(subfolder_path)
print(sub_subfolder_path)
print(file_path)


print(file_path.parts)
print(file_path.name)
print(file_path.suffix)
print(file_path.stem)
print(file_path.parent)


