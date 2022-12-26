from pydantic import BaseModel, Field, constr, conint, validator


class UserFoo(BaseModel):
    id: int
    name: str
    email: str = None
    username: constr(min_length=5, max_length=32)
    age: conint(ge=13)


class Bar(BaseModel):
    apple = 'x'
    banana = 'y'


class Spam(BaseModel):
    user: UserFoo
    bars: list[Bar]


class User(BaseModel):
    id: int
    name: str
    email: str = None
    username: constr(min_length=5, max_length=32)
    age: conint(ge=13)

    account_id: int = Field(default=None, alias="accountId")
    numbers: list[int] = []

    # @validator("numbers", pre=True)
    # def validate(cls: Type['User'], values: list[Any]) -> list[int]:
    #     # print(values)
    #     new_values = []
    #     for v in values:
    #         if isinstance(v, str):
    #             if v.startswith("0x"):
    #                 v = int(v, 16)
    #         new_values.append(v)
    #
    #     return new_values

    # class Config:
    #     validate_assignment = True
    #     allow_population_by_field_name = True

    def inc_age(self):
        self.age += 1


class Author(BaseModel):
    user: User
    bio: str


def categories_factory() -> list[str]:
    return ["sale", "promo"]


class Product(BaseModel):
    price: float
    weight: int
    # categories: list[str] = ["sale"]
    categories: list[str] = Field(default_factory=categories_factory)

    class Config:
        frozen = False

    def is_valid(self):
        ...
        return True

def main():
    m = Spam(
        # user={'count': 4},
        # user={'count': 4},
        user={"id": 4, "name": "Jack", "username": "jack2", "age": 13},
        bars=[{'apple': 'x1'}, {'apple': 'x2'}],
    )

    print(m)
    # return

    admin = User(
        id=1,
        name="Admin",
        username="admin",
        age=42,
    )

    # print(admin)
    # admin.username = "ad"
    print(admin)
    print([admin])
    print(repr(admin))

    user_data = {
        "age": 50,
        # "numbers": [1, 2, 3, "12", "34", b"123", "32", "0xFF"],
        "numbers": [1, 2, 3, "12", "34", b"123", "32", ],
        # "accountId": 1,
    }
    john = User(
        id=2,
        name="John",
        username="john1",
        **user_data,
        account_id=123,
    )
    print(john.account_id)
    print(john)
    john.inc_age()
    print(john)

    author = Author(user=john, bio="hello")
    print("author", repr(author))

    author2 = Author(
        user={"id": 4, "name": "Jack", "username": "jack2", **user_data},
        bio="hello again",
    )
    # print(repr(author2))
    # print(repr(author2.user.age))

    bread = Product(price=55.5, weight=450)
    print(bread)
    bread.categories.append("food")
    print(bread)

    milk = Product(price=95.9, weight=950)
    print(milk)
    milk.categories.append("drinks")
    print(milk)
    # milk.price = 100
    # print(milk)


if __name__ == '__main__':
    main()
