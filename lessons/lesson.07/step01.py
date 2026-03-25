# file_object = open('file_name', 'режим', 'кодировка')
file_object = open('text_python.txt')
# print(file_object)
# print(type(file_object))

data = file_object.read()
print(type(data))
print(data)

file_object.close()

print(type(file_object))
print(file_object)

