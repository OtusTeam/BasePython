from fastapi import APIRouter, Query


router = APIRouter()


@router.get("/")
async def main_page():
    return {"Hello": "World2"}


@router.get("/about/{about_id}/author/{author_id}/")
async def about_page(about_id: int, author_id: str):
    print(about_id)
    print(type(about_id))
    print(author_id)
    print(type(author_id))
    return {"Hello": f"World {about_id} - Имя {author_id}"}


@router.get("/contact/")
async def contact_page(
    name: str = Query(None, description="Name of the contact"),
    age: int = Query(None, description="Age of the contact")
):
    print(name)
    print(type(name))
    print(age)
    print(type(age))
    return {"message": f"Contact: Name - {name}, Age - {age}"}
