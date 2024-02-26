a = 1
b = 1.5
s = "abc"
is_active = True

ids = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
data = {
    "foo": "bar",
    "fizz": "buz",
}

user_john_data = {
    "name": "John",
    "age": 25,
}
user_sam_data = {
    "name": "Sam",
    "age": 42,
}

print(user_john_data)
print(user_sam_data)


def increase_age(user_data):
    user_data["age"] += 1
    # user_data["meta"] = {"abc": "foobar"}


increase_age(user_john_data)
increase_age(user_sam_data)
print(user_john_data)
print(user_sam_data)

user_nick_data = {
    "nmae": "Nick",
    "email": "nick@example.com",
}
print(user_nick_data)
increase_age(user_nick_data)
