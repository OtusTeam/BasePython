from typing import Annotated

from fastapi import (
    Header,
    HTTPException,
    APIRouter,
    Depends,
    status,
)
from pydantic import (
    BaseModel,
    Field,
)

router = APIRouter(
    prefix="/secret",
    tags=["secret"],
)


class SecretInfo(BaseModel):
    answer: int = Field(example=33)
    token: str = Field(
        example="spam-and-eggs",
        description="The secret token provided by user",
    )


VALID_TOKENS = {
    "qwertyabc",
    "aksdfhgasdhfgaf",
    "foobar",
}


def check_token(token: str = Header(alias="x-secret-token")) -> str:
    if token in VALID_TOKENS:
        return token
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid token",
    )


@router.get(
    "/",
    response_model=SecretInfo,
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "description": "Invalid token provided",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Invalid token"
                    },
                },
            },
        },
    },
)
def get_secret(
    token: Annotated[str, Depends(check_token)],
):
    return {
        "answer": 42,
        "token": token,
    }
