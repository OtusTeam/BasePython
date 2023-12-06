def render_list(items, sep=', ', to_title=False):
# def render_list(sep=', ', items):
    return f'{sep}'.join(items)


fruits = ['apple', 'peach', 'lemon']
print(render_list(fruits))

phones = ['iPhone', 'Galaxy', 'Xiaomi']
print(render_list(phones, ' | '))
