from typing import Optional

from fastapi import FastAPI, exceptions, Header, Depends

import crud
from models import UserIn, UserOut, User, AuthorIn, AuthorOut, PostOut, Author, PostIn

app = FastAPI()


@app.get("/", summary="Get a hello world json")
def hello(
    name: str = "World",
):
    """
    Hello world view
    1. processes `request`
    1. returns greeting
    """
    return {"Hello": name}


#

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


#

@app.post("/users", response_model=UserOut, tags=["Users"])
def create_user(user_in: UserIn):
    user = crud.create_user(user_in)
    return user


def get_user_by_token(token: str = Header(..., description="User auth token")) -> User:
    user = crud.get_user_by_token(token)
    if user:
        return user

    raise exceptions.HTTPException(
        401,
        {"message": "Invalid token"}
    )


def get_author_by_user_token(token: str = Header(..., description="User auth token")) -> Author:
    user = crud.get_user_by_token(token)
    if not user:
        raise exceptions.HTTPException(
            401,
            {"message": "Invalid token"}
        )

    author = crud.get_author(user.id)
    if author:
        return author

    raise exceptions.HTTPException(
        400,
        {"message": "User is not registered as Author"}
    )


@app.get("/users/me", response_model=UserOut, tags=["Users"])
def get_me(user: User = Depends(get_user_by_token)):
    return user


@app.get("/users/{user_id}", response_model=UserOut, tags=["Users"])
def get_user(user_id: int):
    user = crud.get_user(user_id)
    if user:
        return user

    raise exceptions.HTTPException(
        404,
        {"message": f"No user with id #{user_id}", "value": user_id},
    )


@app.post("/authors", response_model=AuthorOut, tags=["Authors"])
def create_author(
    author_in: AuthorIn,
    user: User = Depends(get_user_by_token),
):
    author = crud.get_author(user.id)
    if author:
        return author
    author = crud.create_author(author_in, user)
    return author


@app.post("/posts", response_model=PostOut, tags=["Posts"])
def create_post(
    post_in: PostIn,
    author: Author = Depends(get_author_by_user_token),
):
    post = crud.create_post(post_in, author)
    return post


@app.get("/posts/{post_id}", response_model=PostOut, tags=["Posts"])
def get_post(post_id: int):
    post = crud.get_post(post_id)
    if post:
        return post

    raise exceptions.HTTPException(
        404,
        {"message": f"No post with id #{post_id}", "value": post_id},
    )
