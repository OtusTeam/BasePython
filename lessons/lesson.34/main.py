from typing import Optional

from fastapi import FastAPI, exceptions, Depends, Header, Cookie, Response
from fastapi.responses import FileResponse, StreamingResponse

from models import Item, ItemUpdate, UserBase, User, UserOut, UserUpdateUsername

app = FastAPI()


USERS_BY_IDS = {}
USERS_BY_TOKENS = {}


@app.get("/")
def read_root(
    name: str = "World",
    cookie_spam: str = Cookie(None, alias="spam"),
):
    """
    Returns Hello World and cookie spam value
    """
    return {"Hello": name, "cookie-spam": cookie_spam}


@app.get("/cookies")
def get_cookies(response: Response):
    response.headers["X-App-Name"] = __name__
    response.set_cookie("spam", "eggs", httponly=True)
    return {"message": "sending cookies and headers"}


@app.get("/file")
def get_file():
    return FileResponse("file.txt")
    # return StreamingResponse("big_buck_bunny_720p_1mb.mp4")
    # return FileResponse("qwe.bin")


@app.get("/items/{item_id}", tags=["Items"])
def read_item(item_id: int):
    return {"item_id": item_id}


@app.post("/items", tags=["Items"])
def create_item(item: Item):
    # item.name, item.id
    print("create item #", item.id, "with name", item.name)
    return {"item": item.dict()}


@app.patch("/items/{item_id}", tags=["Items"])
def update_item(item_id: int, item_update: ItemUpdate):
    return {"id": item_id, "name": item_update.name}


@app.get("/get-qs", tags=["Items"])
def get_qs_q(q: Optional[str] = None):
    return {"q": q}


#

def get_user_by_token(token: str) -> User:
    return USERS_BY_TOKENS.get(token)


def get_current_user(token: str = Header(..., description="user auth token")) -> User:
    user = get_user_by_token(token)
    if not user:
        raise exceptions.HTTPException(404, {"message": f"User by token not found!"})

    return user


@app.get("/users/me", response_model=UserOut, tags=["Users"])
def get_me(
    user: User = Depends(get_current_user),
):
    return user


@app.patch("/users/me/update-username", response_model=UserOut, tags=["Users"])
def update_my_username(
    upd: UserUpdateUsername,
    user: User = Depends(get_current_user),
):
    user.update_username(upd)
    return user


@app.post("/users", response_model=UserOut, tags=["Users"])
def create_user(user_in: UserBase):
    user = User(id=len(USERS_BY_IDS) + 1, **user_in.dict(exclude_none=True))
    USERS_BY_IDS[user.id] = user
    USERS_BY_TOKENS[user.token] = user
    return user


@app.get("/users/{user_id}", response_model=UserOut, tags=["Users"])
def get_user(user_id: int):
    user = USERS_BY_IDS.get(user_id)
    if not user:
        raise exceptions.HTTPException(404, {"message": f"User #{user_id} not found!", "value": user_id})

    return user
