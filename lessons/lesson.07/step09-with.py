file_object = open('data/text_python.txt', 'r')
data = file_object.read()
file_object.close()

print(data)

print('*' * 50)


with open('data/text_python.txt', 'r') as file:
    data = file.read()


print(data)