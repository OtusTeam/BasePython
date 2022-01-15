# Create
# Read
# Update
# Delete
from typing import Optional

from schemas import UserIn, User


USER_ID_TO_USER: dict[int, User] = {}
USER_TOKEN_TO_USER: dict[str, User] = {}


def create_user(user_in: UserIn) -> User:
    new_id = len(USER_ID_TO_USER) + 1
    user = User(id=new_id, **user_in.dict())

    # kinda db
    USER_ID_TO_USER[user.id] = user
    USER_TOKEN_TO_USER[user.token] = user

    return user


def list_users() -> list[User]:
    return list(USER_ID_TO_USER.values())


def get_user_by_id(user_id: int) -> Optional[User]:
    return USER_ID_TO_USER.get(user_id)


def get_user_by_token(token: str) -> Optional[User]:
    return USER_TOKEN_TO_USER.get(token)


# def get_user_by_email_and_password(email: str, password: str) -> Optional[User]:
#     user = get_user_by_email(email)
#     if user and user.check_password(password):
#         return user
