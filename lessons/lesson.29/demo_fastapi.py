from typing import Optional, Dict

from fastapi import FastAPI, exceptions, Query, Header, Depends

from demo_pydantic import User, UserBase, UserOut


app = FastAPI()


ids = iter(range(1, 100000))


USERS = {}

USERS_BY_TOKEN: Dict[str, User] = {}



@app.get("/")
# def hello_world(name: str = Query(...)):
def hello_world(name: str = Query("world")):
    """
    ## Returns greeting
    1. is json
    1. is documented
    1. greets the world
    """
    return {"message": f"Hello {name}!"}


@app.get("/{item_id}/")
def item(item_id: int):
    """
    Returns item id

    """
    return {"item_id": item_id}


@app.post("/user/", response_model=UserOut, tags=["User"])
def create_user(user_in: UserBase):
    user = User(id=next(ids), **user_in.dict())
    USERS[user.id] = user
    USERS_BY_TOKEN[user.token] = user
    return {"user": user.dict()}


def get_current_user(token: str = Header(..., description="user auth token (user token)")) -> User:
    print("check for token", token)
    if token not in USERS_BY_TOKEN:
        raise exceptions.HTTPException(404, f"user token {token!r} not found")
    user = USERS_BY_TOKEN[token]
    return user


@app.get("/user/me/", response_model=User, tags=["User"])
def get_me(user: User = Depends(get_current_user)):
    return user


@app.get("/user/{id}/", response_model=User, tags=["User"])
def get_user(id: int):
    """
    Returns user if found
    """
    try:
        user = USERS[id]
    except KeyError:
        raise exceptions.HTTPException(404, f"user {id} not found")

    return user
