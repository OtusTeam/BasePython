# with open('otus', 'r') as file:
#     print(file.read())


# file = open('otus')
# print(file.read())
# file.close()

# try:
#     file = open('otus', 'r')
#     print(file.read())
# except FileNotFoundError as e:
#     print(e)
# finally:
#     file.close()

try:
    with open('o', 'r') as file:
        print(file.read())
except FileNotFoundError as e:
    print(e)
