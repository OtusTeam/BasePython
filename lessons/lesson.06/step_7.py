from contextlib import contextmanager


@contextmanager
def my_open(f_path):
    print('started')
    # pre

    f_obj = open(f_path)

    yield f_obj
    # return f_obj

    # post
    f_obj.close()
    print('finished')


path_1 = 'step_1.py'
with my_open(path_1) as f:
    print(f.readline())
    print(f.closed)

print(f.closed)
