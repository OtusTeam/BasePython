from typing import Optional

from .schemas import User, UserIn


USER_ID_TO_USER: dict[int, User] = {}
USER_TOKEN_TO_USER: dict[str, User] = {}


def list_users() -> list[User]:
    return list(USER_ID_TO_USER.values())


def create_user(user_in: UserIn) -> User:
    new_id = len(USER_ID_TO_USER) + 1
    user = User(id=new_id, **user_in.dict())

    USER_ID_TO_USER[new_id] = user
    USER_TOKEN_TO_USER[user.token] = user

    return user


def get_user(user_id: int) -> Optional[User]:
    return USER_ID_TO_USER.get(user_id)


def get_user_by_token(token: str) -> Optional[User]:
    return USER_TOKEN_TO_USER.get(token)
