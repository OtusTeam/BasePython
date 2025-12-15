from fastapi import APIRouter


router = APIRouter()


@router.get("/")
async def index():
    """Главная страница."""
    return {"message": "Hello World"}


@router.get("/about/{about_id}/")
async def about(about_id: int):
    """Страница о нас."""
    print(type(about_id))
    print(about_id * 10)
    return {"message": f"About us - {about_id}"}
