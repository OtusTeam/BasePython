def render_user(name, age):
    return ', '.join(map(str, [name, age]))


print(render_user(name='Peter', age=5))
print(render_user('Peter', 5))
