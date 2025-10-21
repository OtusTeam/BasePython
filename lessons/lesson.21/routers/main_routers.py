from fastapi import APIRouter


router = APIRouter()


@router.get("/")
async def index():
    return {"message": "Hello World"}


@router.get("/about/")
async def index():
    return {"message": "About us"}