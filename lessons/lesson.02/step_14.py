users = ['a.ivanov', 'o.petrova', 's.sergeev']

...
messages = [el.upper() for el in users]  # memory O(n)
print(messages)


def my_processor(item: str) -> str:
    # return item.title()
    return item.upper()


# messages_2 = map(str.upper, users)  # memory O(1)
messages_2 = map(my_processor, users)  # memory O(1)
for el in messages_2:
    print(el)
