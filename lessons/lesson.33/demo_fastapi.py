from fastapi import FastAPI, Query, Request, exceptions, Header, Depends, Response, Cookie
from demo_pydantic import Item, UserBase, User, UserOut, UpdateUsername

app = FastAPI()

ids = iter(range(1, 100))

USERS_BY_IDS = {}
USERS_BY_TOKENS = {}


def get_user_by_token(token: str) -> User:
    if token not in USERS_BY_TOKENS:
        raise exceptions.HTTPException(404, f"User token {token!r} not found!")
    return USERS_BY_TOKENS[token]


@app.get("/")
def hello_world(
    name: str = Query("World"),
    cookie_spam: str = Cookie(None, alias="spam"),
    request: Request = None,
):
    """
    ### Returns greeting
    1. is json
    1. is documented
    1. greets world / name
    """
    print("cookies:", request.cookies)
    return {"message": f"Hello {name}!", "cookie_spam": cookie_spam}


@app.get("/item/{item_id}/", tags=["Items"])
def get_item(item_id: int):
    return {"item_id": item_id}


@app.post("/item/", tags=["Items"])
def create_item(item: Item):
    return {"item": item.dict()}


@app.get("/items/{item_id}/", tags=["Items"])
def read_root(item_id: str, request: Request):
    client_host = request.client.host
    return {"client_host": client_host, "item_id": item_id}


#


@app.post("/users/", response_model=UserOut, tags=["Users"])
def create_user(user_in: UserBase):
    user = User(id=next(ids), **user_in.dict(exclude_none=True))
    USERS_BY_IDS[user.id] = user
    USERS_BY_TOKENS[user.token] = user
    return {"user": user.dict()}


@app.get("/users/{user_id}", response_model=User, tags=["Users"])
def get_user_by_id(user_id: int):
    user = USERS_BY_IDS.get(user_id)
    if user is None:
        raise exceptions.HTTPException(404, {"message": f"User #{user_id} not found!", "value": user_id})
    return user


def get_current_user(token: str = Header(..., description="user auth token")) -> User:
    return get_user_by_token(token)


def update_username_username(upd_username: UpdateUsername):
    return upd_username.username


@app.patch("/users/me/update-username/", response_model=User, tags=["Users"])
def update_my_username(
    # upd_username: UpdateUsername,
    new_username: str = Depends(update_username_username),
    user: User = Depends(get_current_user)
):
    # user.update_username(upd_username)
    user.update_username_from_str(new_username)
    return user


@app.get("/users/me/", response_model=User, tags=["Users"])
def get_me(user: User = Depends(get_current_user)):
    # ok
    # user.update_last_visit_time()
    # never!
    # user.last_visit = datetime.now()
    # user.save()
    return user


@app.get("/cookies/")
def get_cookies(response: Response):
    response.headers["X-App-Name"] = __name__
    response.set_cookie("spam", "eggs", httponly=True)
    return {"message": "sending cookies and headers"}
