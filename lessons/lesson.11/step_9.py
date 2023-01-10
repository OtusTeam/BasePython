import os

print(os.path.sep)

f_name = 'step_1.py'
f_abs_path = os.path.abspath(f_name)
print(f_abs_path)
print(os.path.split(f_abs_path))

file_path, file_name = os.path.split(f_abs_path)
print(file_path, file_name)
