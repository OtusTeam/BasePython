file_object = open('data/text_python.txt', 'r')
line = file_object.readline()
print(line)

line = file_object.readline()
print(line)

while line:
    print(line)
    line = file_object.readline()

file_object.close()

# print(data)





