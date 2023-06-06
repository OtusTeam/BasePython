users = ['a.ivanov', 'o.petrova', 's.sergeev']


def my_condition(item: str) -> bool:
    return item.startswith('a')


messages_2 = filter(my_condition, users)  # memory O(1)
for el in messages_2:
    print(el)
