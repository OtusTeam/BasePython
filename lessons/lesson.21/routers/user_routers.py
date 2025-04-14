from fastapi import APIRouter


router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.get("/contact/")
async def contact():
    return {"message": "Hello contact"}