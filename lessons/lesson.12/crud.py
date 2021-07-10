from typing import Optional, Dict

from models import UserIn, User, AuthorIn, Author, Post, PostIn


USERS_BY_ID: Dict[int, User] = {}
USERS_BY_TOKEN: Dict[str, User] = {}

AUTHORS_BY_USER_ID: Dict[int, Author] = {}

POSTS_BY_ID: Dict[int, Post] = {}


def create_user(user_in: UserIn):
    user = User(id=len(USERS_BY_ID) + 1, **user_in.dict())
    USERS_BY_ID[user.id] = user
    USERS_BY_TOKEN[user.token] = user
    return user


def get_user(user_id: int) -> Optional[User]:
    return USERS_BY_ID.get(user_id)


def get_user_by_token(token: str) -> Optional[User]:
    return USERS_BY_TOKEN.get(token)


def get_author(user_id: int) -> Optional[Author]:
    return AUTHORS_BY_USER_ID.get(user_id)


def create_author(author_in: AuthorIn, user: User) -> Author:
    author = Author(**author_in.dict(), user=user)
    AUTHORS_BY_USER_ID[user.id] = author
    return author


def get_post(post_id: int) -> Optional[Post]:
    return POSTS_BY_ID.get(post_id)


def create_post(post_in: PostIn, author: Author) -> Post:
    post = Post(id=len(POSTS_BY_ID) + 1, **post_in.dict(), author=author)
    POSTS_BY_ID[post.id] = post
    return post
