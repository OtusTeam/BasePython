'Медведь'
kind = 'Медведь'
name = 'Борис'
age = 11
weight = 20.1
is_man = True


# список, словарь, множество, кортеж
kinds = ['Bear', 'Fox', 'Rabbit', 'Python', 'Crocodile']

animals = [{
    'name': 'Борис',
    'age': 11,
    'is_man': True,
    'kind': 'Bear'
},
{
    'name': 'Гена',
    'age': 12,
    'is_man': True,
    'kind': 'Crocodile'
}
]

roles = ('Администратор', 'Директор', 'Наемники')

if len(animals) > 10:
    print('Большой')
else:
    if (len(roles) > 5) or ('Bear' in kinds):
        print('Возможно большой')
    else:
        print('Маленький')


