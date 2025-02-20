from fastapi import APIRouter

router = APIRouter()


@router.get("/hello")
def reply_hello(name: str):
    return {"message": f"Hello, {name}!"}
