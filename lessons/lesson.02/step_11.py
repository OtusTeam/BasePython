def render_list(items, sep):
    return f'{sep}'.join(items)


fruits = ['apple', 'peach', 'lemon']
print(render_list(fruits, ', '))
#
#
# def render_list(items):
#     return ', '.join(items)

phones = ['iPhone', 'Galaxy', 'Xiaomi']
print(render_list(phones, ' | '))
