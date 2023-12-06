def render_list(items, sep=', '):
    return f'{sep}'.join(items)


fruits = ['apple', 'peach', 'lemon']
print(render_list(fruits))

phones = ['iPhone', 'Galaxy', 'Xiaomi']
# print(render_list(phones, ' | '))
print(render_list(phones, sep=' | '))
# print(render_list(items=phones, sep=' | '))
print(render_list(sep=' | ', items=phones))

print(sorted(fruits, key=lambda x: x[1]))
print(sorted(fruits, reverse=True))
print(sorted(fruits, reverse=True, key=lambda x: x[1]))
