f_name = 'step_1.py'

with open(f_name) as f:
    content = f.read()
    # content = f.readline()
    # content = f.readlines()
    # f.write('hello ...')  # flush

print(content)
# print(dir(f))
print(f.closed)

# yield
