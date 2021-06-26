from sys import getsizeof
from collections import namedtuple

UserTuple = namedtuple("UserTuple", "user_id, age, username, email, full_name")


def get_user():
    user_id = 42
    age = 21
    username = "john"
    email = "john@example.com"
    full_name = "John Smith"
    # return user_id, age, username, email, full_name
    return UserTuple(user_id, age, username, email, full_name)


def get_user_dict():
    user_id = 42
    age = 21
    username = "john"
    email = "john@example.com"
    full_name = "John Smith"

    return {
        "user_id": user_id,
        "age": age,
        "username": username,
        "email": email,
        "full_name": full_name,
    }


def main():
    res: UserTuple = get_user()
    # res.email
    # user_id, age, username, email, full_name = res
    # user_id, username, email = res
    print(res)
    print("hash res", hash(res))
    user_id = res.user_id
    username = res.username
    email = res.email
    age = res.age
    full_name = res.full_name
    # print(res)
    print("user_id", user_id)
    print("age", age)
    print("full_name", full_name)
    print("username", username)
    print("email", email)

    user_dict = get_user_dict()
    print(user_dict["user_id"])
    print(res.user_id)
    print("getsizeof user_dict", getsizeof(user_dict))
    print("getsizeof res", getsizeof(res))
    print("res[0]", res[0])


def compare():
    user = get_user()
    user2 = get_user()
    print(user)
    print(user2)
    print(('abc', 'qwe') == ('abc', 'qwe'))
    print("hash equal?", hash(user) == hash(user2))
    print("equal?", user == user2)
    print("equal?", user is user2)


if __name__ == '__main__':
    main()
    compare()
    u = UserTuple(user_id=42, age=21, username='john', email='john@example.com', full_name='John Smith')
    print(u)
