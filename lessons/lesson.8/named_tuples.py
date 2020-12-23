from collections import namedtuple

UserInfo = namedtuple("UserInfo", ["username", "email", "age", "gender"])


def get_user_data_from_response(data: dict) -> UserInfo:
    username = "user"
    age = 23
    email = "abc@example.com"
    gender = ""
    user_info = UserInfo(username=username, age=age, email=email, gender=gender)
    return user_info


def fetch_and_save_user():
    # requests.get(...)
    data = {}
    user_info = get_user_data_from_response(data)
    print(user_info)
    print("info[0], info[2]", user_info[0], user_info[2])
    # (None,   0,    "")
    # (username, age, email, gender) = user_info
    # user = User(username=username, age=age, ...)
    # print(username, age, email)
    print(user_info.username, user_info.email)


if __name__ == '__main__':
    # print(get_user_data_from_response({}))
    fetch_and_save_user()
