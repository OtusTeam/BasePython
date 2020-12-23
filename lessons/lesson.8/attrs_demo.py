from typing import Optional
import attr
from attr import attrs, attrib
# import attr.validators

# attr.validators
# attr.attrs
# attr.attrib

# class UserInfo:
#     def __init__(self, username=None, email="", age=0, gender=None, interests=None):
#         self.username = username
#         self.email = email
#         self.age = age
#         if interests is None:
#             interests = []
#         self.interests = interests
#
#     # def __repr__(self):
#     #     return f"{self.__class__.__name__}"


validator_gender = attr.validators.in_(["male", "female"])

# @attr.attrs
# @attr.s
@attrs
class UserInfo:
    username = attrib(default=None, type=Optional[str])
    email = attrib(default="")
    age = attrib(default=0)
    gender = attrib(default=None, validator=attr.validators.optional(validator_gender))
    interests = attrib(factory=list)

    def add_interest(self, interest):
        self.interests.append(interest)


def get_user_data_from_response(data: dict) -> UserInfo:
    username = "user"
    age = 23
    gender = "male"
    user_info = UserInfo(username=username, age=age, gender=gender)
    return user_info


def fetch_and_save_user():
    # requests.get(...)
    data = {}
    user_info = get_user_data_from_response(data)
    user_info2 = get_user_data_from_response(data)
    print(user_info)
    print("user_info == user_info2", user_info == user_info2)
    user_info.add_interest("cars")
    print("user_info, user_info2", user_info, user_info2)
    print("user_info == user_info2", user_info == user_info2)
    print(user_info.username, user_info.age, user_info.interests)
    print(attr.asdict(user_info))


if __name__ == '__main__':
    # print(get_user_data_from_response({}))
    fetch_and_save_user()

