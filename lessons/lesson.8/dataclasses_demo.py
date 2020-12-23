from typing import Optional
from dataclasses import dataclass, asdict
# from dataclasses import *


@dataclass
class UserInfo:
    username: str
    age: int = 0
    email: Optional[str] = None


def get_user_data_from_response(data: dict) -> UserInfo:
    username = "user"
    age = 23
    email = "abc@example.com"
    user_info = UserInfo(username=username, age=age, email=email)
    return user_info


def fetch_and_save_user():
    # requests.get(...)
    data = {}
    user_info = get_user_data_from_response(data)
    user_info2 = get_user_data_from_response(data)
    print(user_info)
    print("user_info == user_info2", user_info == user_info2)
    user_info.age = "unknown"
    print(user_info)
    print("user_info == user_info2", user_info == user_info2)
    print(asdict(user_info))
    print(asdict(user_info2))


if __name__ == '__main__':
    # print(get_user_data_from_response({}))
    fetch_and_save_user()
