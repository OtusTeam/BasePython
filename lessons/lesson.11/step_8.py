import os

# ROOT = '/home/jo/221128_python_basic/230109'
ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    '../'
))

f_name = 'step_1.py'
print(os.path.abspath(f_name))
print(os.path.basename(f_name))
print(os.path.dirname(f_name))
print(os.path.relpath(f_name, ROOT))
