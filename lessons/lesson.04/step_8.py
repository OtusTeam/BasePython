# shared
f_name = 'step_1.py'
f = open(f_name)
content = f.read()
# f.write('hello ...')  # flush
print(content)
# print(dir(f))
print(f.closed)
f.close()
print(f.closed)
