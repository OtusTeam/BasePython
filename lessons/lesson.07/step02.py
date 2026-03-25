# file_object = open('text_python.txt')
file_object = open('data/text_python.txt', 'r')
# file_object = open('data/text_python.txt', 'w')
# file_object = open('data/text_python.txt', 'a')
# file_object = open('data/text_python.txt', 'r+')
# file_object = open('data/text_python.txt', 'w+')
# file_object = open('data/text_python.txt', 'a+')

data = file_object.read()
file_object.close()

print(data)


