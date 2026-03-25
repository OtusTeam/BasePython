# from pprint import pprint


file_object = open('data/text_python.txt', 'r')

for line in file_object:
    print(f'{line}')

file_object.close()

# print(data)


