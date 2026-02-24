from fastapi import APIRouter, Query, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.get("/about/{about_id}/{my_id}/")
async def about(about_id: int, my_id: int):
    print(type(about_id))
    print(type(my_id))
    print(about_id * my_id)

    return {"message": f"About us {about_id}"}


@router.get("/contact/")
async def contact(
    name: str = Query(None, description="Name of contact"),
    age: int = Query(None, description="Age of contact"),
):
    print(type(name))
    print(type(age))
    print(f"Contact  {name} {age}")

    return {"message": f"Contact  {name} {age}"}
