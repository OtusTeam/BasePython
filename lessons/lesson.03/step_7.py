# f = open('step_1.py')
# print(f.closed)
# print(f.read())
# print(f.closed)
# # f.close()
# # print(f.closed)

with open('step_1.py') as f:
    print(f.read())
