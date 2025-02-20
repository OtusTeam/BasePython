"""
Create
Read
Update
Delete
"""


from pydantic import BaseModel

from . import schemas


class UsersCRUD(BaseModel):
    count: int = 0
    users_by_id: dict[int, schemas.User] = {}
    users_by_token: dict[str, schemas.User] = {}

    @property
    def next_id(self) -> int:
        self.count += 1
        return self.count

    def get(self) -> list[schemas.User]:
        return list(self.users_by_id.values())

    def get_by_id(self, user_id: int) -> schemas.User | None:
        return self.users_by_id.get(user_id)

    def get_by_token(self, token: str) -> schemas.User | None:
        return self.users_by_token.get(token)

    def create(self, user_in: schemas.UserCreate) -> schemas.User:
        user = schemas.User(
            id=self.next_id,
            **user_in.model_dump(),
        )
        self.users_by_id[user.id] = user
        self.users_by_token[user.token] = user
        return user


users = UsersCRUD()

users.create(
    user_in=schemas.UserCreate(
        username="bob",
        email="bob@example.com",
        full_name="Bob Smith",
    ),
)
users.create(
    user_in=schemas.UserCreate(
        username="john",
        full_name="John Black",
    ),
)
