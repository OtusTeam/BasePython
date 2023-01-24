a = 1
b = 2

print(a + b)

names = [
    "bob",
    "sam",
    "alice",
    "admin",
    "john",
    "george",
    "jim",
    "kate",
    "nick",
]


if len(names) > 5:
    print("error! too many users:", len(names))


# if re.match('abc', 'qwe'):
#     match = re.match('abc', 'qwe')
#     match...

users_len = len(names)

if users_len > 5:
    print("error! too many users:", users_len)


if (n := len(names)) > 5:
    print("error! too many users:", n)

if (v := a + b) > 5:
    print("a + b =", v)
else:
    print("too low")


def find_value(data: dict, key: str):
    return data.get(key)


if v := find_value({"w": "wasd"}, "w"):
    print("found", v)

if (v := find_value({"q": "qwe"}, "q")) is not None:
    print("found", v)
else:
    print("not found")

if (v := find_value({"w": "wasd"}, "d")) is not None:
    print("found", v)
else:
    print("not found")

gender = "M"

line = "boy" if gender == "M" else "girl"
print(line)

