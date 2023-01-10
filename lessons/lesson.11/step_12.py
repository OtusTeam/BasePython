import os

f_name = 'step_1.py'
# print(os.stat(f_name))

total_size = 0
for el in os.scandir('.'):
    # print(type(el), el, dir(el))
    print(type(el), el, el.is_dir())
    total_size += el.stat().st_size
print(total_size)
