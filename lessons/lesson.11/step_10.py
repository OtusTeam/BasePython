import os
import shutil

# dir_name = 'users'
# # os.mkdir(dir_name)
# if not os.path.exists(dir_name):
#     os.mkdir(dir_name)


dir_name_2 = 'users/files'
# os.makedirs(dir_name_2)
if not os.path.isdir(dir_name_2):
    # os.mkdir(dir_name_2)
    os.makedirs(dir_name_2)


if os.path.isdir(dir_name_2):
    # os.rmdir(dir_name_2)
    shutil.rmtree(dir_name_2)
