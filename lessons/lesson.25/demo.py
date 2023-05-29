import json


def show_dump():
    for elem in [
        None,
        True,
        False,
        "spam and eggs",
        ["foo", "bar"],
        {"data": ["abc"]}
    ]:
        as_string = json.dumps(elem)
        print("elem", elem, "as json:", repr(as_string))


if __name__ == '__main__':
    show_dump()
