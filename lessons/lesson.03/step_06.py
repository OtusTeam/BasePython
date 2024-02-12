def flatten_list(elems):
    new_list = []
    for element in elems:
        if isinstance(element, (list, tuple)):
            new_list.extend(flatten_list(element))
        else:
            new_list.append(element)
    return new_list


elements = [
    "foo",
    "bar",
    ["spam", "eggs"],
    "abc",
    "qwe",
    ["biz", ["fizz", ("j", "k"), "buzz", ["true", "false"]]],
]

# print(flatten_list(elements))

for elem in elements:
    print(elem)

print()
for elem in flatten_list(elements):
    print(elem)
