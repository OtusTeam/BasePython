from typing import Optional, List
from datetime import datetime, date
from pydantic import BaseModel, Field


class UserInfo(BaseModel):
    joined_date: datetime
    username: str
    # age: int = 0
    birth_date: Optional[date] = None
    email: Optional[str] = None
    gender: Optional[str] = None
    interests: List[str] = []
    # interests: list = []
    # interests: List[str] = Field(default_factory=list)

    def add_interest(self, interest):
        self.interests.append(interest)


def get_user_data_from_response(data: dict) -> UserInfo:
    username = "user"
    birth_date = "1984-12-23"
    # age = 23
    email = "abc@example.com"
    user_info = UserInfo(
        joined_date="2020-06-01 12:23:45.678",
        username=username,
        birth_date=birth_date,
        email=email,
    )
    return user_info


def fetch_and_save_user():
    # requests.get(...)
    data = {}
    user_info = get_user_data_from_response(data)
    user_info2 = get_user_data_from_response(data)
    print(user_info)
    print("user_info == user_info2", user_info == user_info2)
    user_info.add_interest("cars")
    # user_info.age = "unknown"
    print(user_info)
    print(user_info2)
    print("user_info == user_info2", user_info == user_info2)
    # print(user_info.dict(exclude_none=True))
    # print(user_info.dict(exclude={"age"}))
    # print(user_info.dict(exclude_unset=True))


if __name__ == '__main__':
    # print(get_user_data_from_response({}))
    fetch_and_save_user()
