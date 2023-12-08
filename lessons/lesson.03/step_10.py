# f = open('step_1.py')
# content = f.read()
# print(content)
#
# print(f.closed)
# f.close()
# print(f.closed)

# __enter__
# __exit__

with open('step_1.py') as f:
    content = f.read()

print(content)
