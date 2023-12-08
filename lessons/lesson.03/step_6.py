def render_user(name, age, **kwargs):
    print('kwargs', kwargs)
    if kwargs.get('country'):
        print('got country')

    # country = kwargs['country']

    return ', '.join(map(str, [name, age]))


def render_page(name, age, country, city=None):
    user = render_user(name, age, country=country, city=city)
    # user = render_user(name, age)
    country = f'country {country}'

    return f'{user} from {country}'


# print(render_user(name='Peter', age=5))
# print(render_user('Peter', 5))
print(render_page('Peter', 5, 'Russia'))
# print(render_page('Peter', 5, None))
