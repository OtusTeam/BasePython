import os

f_name = 'step_1.py'
# print(os.stat(f_name))

total_size = 0
for el in os.listdir('.'):
    print(type(el), el, os.path.isdir(el))
    total_size += os.stat(el).st_size
print(total_size)
