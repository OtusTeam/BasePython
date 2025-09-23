from typing import Annotated, Literal

# from annotated_types import MaxLen, MinLen

from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from fastapi import Path
from fastapi import Query
from fastapi import Header
from fastapi import Depends
from pydantic import PositiveInt, BaseModel

app = FastAPI()


NameInQuery = Annotated[
    str,
    Query(
        min_length=2,
        max_length=20,
    ),
]


USERS_DATA = {
    1: {"username": "bob", "id": 1},
    2: {"username": "john", "id": 2},
    3: {"username": "kate", "id": 3},
}


MESSAGES_BY_CHAT = [
    None,
    [
        None,
        {"id": 1, "text": "Hello"},
        {"id": 2, "text": "Hello you"},
    ],
    [
        None,
        {"id": 1, "text": "Hi!"},
        {"id": 2, "text": "Hi, nice to meet you"},
        {"id": 3, "text": "What's up?"},
    ],
]


@app.get("/hello")
def hello_view(
    # name: str = "Bob",
    # name: str = Query("Nick"),
    # account_id: str = Header(""),
    # name: Annotated[
    #     str,
    #     # MinLen(2),
    #     # MaxLen(20),
    #     Query(
    #         min_length=2,
    #         max_length=20,
    #     ),
    # ] = "Nick",
    name: NameInQuery = "",
    account_id: Annotated[
        str,
        Header(),
    ] = "",
):
    """
    Handles GET requests to /hello

    **list:**

    - foo
    - bar
    - spam
    - eggs
    """

    return {
        "message": f"Hello {name}!",
        "account_id": account_id,
    }


@app.get("/bye")
def bye_view(
    name: NameInQuery = "John",
):
    return {"message": f"Bye, {name}!"}


@app.get("/users")
def users_view():
    return list(USERS_DATA.values())


@app.get("/users/{user_id}")
def user_detail_view(
    user_id: Annotated[
        PositiveInt,
        Path(),
    ],
):
    if user_id in USERS_DATA:
        return USERS_DATA[user_id]

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User #{user_id} not found.",
    )


def chat_messages_by_id(
    chat_id: Annotated[
        PositiveInt,
        Path(),
    ],
):
    try:
        return MESSAGES_BY_CHAT[chat_id]
    except IndexError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Chat #{chat_id} not found",
        )


ChatMessages = Annotated[
    list[list],
    Depends(chat_messages_by_id),
]


def get_message_details_by_id(
    chat_messages: ChatMessages,
    message_id: Annotated[PositiveInt, Path()],
):
    try:
        return chat_messages[message_id]
    except IndexError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Message #{message_id} not found",
        )


@app.get("/messages/{chat_id}")
def get_chat_messages(
    chat_messages: ChatMessages,
):
    # # open connection
    # yield res
    # # close conn
    return chat_messages[1:]


@app.get("/messages/{chat_id}/message/{message_id}")
def get_message_details(
    message: Annotated[
        dict,
        Depends(get_message_details_by_id),
    ],
):
    return message


class UserAccessInfo(BaseModel):
    username: str


class TokenAccessDependency:

    def __init__(self, access_token: str):
        # на самом деле здесь мы бы инициализировали работу с БД
        self.access_token = access_token

    def __call__(
        self,
        x_access_token: Annotated[
            str,
            Header(),
        ],
    ) -> UserAccessInfo:
        # тут мы бы через БД проверяли токен пользователя
        if x_access_token == self.access_token:
            # взять из токена инфу
            return UserAccessInfo(username="dummy")

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid access token",
        )


token_auth = TokenAccessDependency(
    access_token="super-secret-token",
)


@app.get("/secret-info")
def get_secret_info(
    access_info: Annotated[
        UserAccessInfo,
        Depends(token_auth),
    ],
):
    return {
        "secret-answer": 42,
        "auth-username": access_info.username,
    }
