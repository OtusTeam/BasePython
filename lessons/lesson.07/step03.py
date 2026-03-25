# from pprint import pprint


file_object = open('data/text_python.txt', 'r')

# data = file_object.read()
data = file_object.readlines()
file_object.close()

print(data)

# for index, line in enumerate(data, start=1):
#     print(f'{index} - {line}')
