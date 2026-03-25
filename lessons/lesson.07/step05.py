file_object = open('data/text_python.txt', 'r')

chunk_size = 100
chunk = file_object.read(chunk_size)
# for line in file_object:
#     print(f'{line}')

print(chunk)

print('*' * 50)

chunk = file_object.read(10)
print(chunk)

file_object.close()




