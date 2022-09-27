from datetime import datetime

from pydantic import BaseModel, Extra, conint, constr


# class My:
#     def __repr__(self):
#         1/0
#         return "my"


class User(BaseModel):
    # id: int
    # id: conint(ge=1)
    id: conint(gt=0)
    name: constr(min_length=3, max_length=40) = 'John Doe'
    signup_ts: datetime | None = None
    friends: list[int] = []
    archived: bool = False
    # m: My = My()

    class Config:
        # extra = Extra.allow
        extra = Extra.ignore
        # extra = Extra.forbid
        # frozen = True
        # arbitrary_types_allowed = True


def main():
    # print(datetime.now().timestamp())
    options = {
        # "signup_ts": 0,
        "signup_ts": 1664302679,
        "friends": [b"12", "34", 56],

        # extra:
        "profile": {"abc": "qwe"},
    }
    user = User(id=1, name="John", **options)
    # print(user)
    print(user.__str__())
    print(repr(user))
    user.name = "Sam"
    # print(user.profile)
    print(user.dict())
    print(user.json())


if __name__ == '__main__':
    main()
