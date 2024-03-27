from fastapi import APIRouter

router = APIRouter(
    prefix="/hello",
    tags=["hello"],
)


@router.get("")
def hello_user(name: str, age: int):
    return {"message": f"Hello {name} of age {age}!"}


@router.get("/{name}")
def hello_name_path(name: str):
    return {"message": f"Hello {name}!"}
