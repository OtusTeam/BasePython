a = {15, 85.2, 'hello', 'hello'}
print(a, type(a), 15 in a)

b = [15, 85.2, 'hello', 'hello']
print(b, type(b), 15 in b)

# print(hash(15), hash('hello'), hash([15, 55]))

c = {'one', tuple(b)}
print(c)
# .__hash__()
# .__eq__()

try:
    hash(b)
    print('hashable')
except Exception as e:
    print('non hashable')
