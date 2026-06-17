names = ['Bob', 123456, True]
print(names)

# names_dict = {}
# new1 = dict()
names_dict = {
    'name': 'Bob',
    'tel': 123456,
    'f': True
}

print(names_dict)
print(type(names_dict))

print(names_dict['name'])

names_dict['name'] = 'Alice'
print(names_dict)

names_dict['name123'] = 'Alice123'
print(names_dict)

del names_dict['name']
print(names_dict)

friend = names_dict.pop('f')
print(names_dict)

# new1 = dict(name='Mary', tel=123456)
# print(new1)


# print(names_dict['name'])
print(names_dict.get('name'))
# print(names_dict.tel)

# print(names_dict.keys())
# print(names_dict.values())
# print(names_dict.items())