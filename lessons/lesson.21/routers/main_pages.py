from fastapi import APIRouter, Query, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(request, "index.html", {"title": 'Главная страница'})


@router.get("/about/", response_class=HTMLResponse)
async def about(request: Request):

    # return {"message": f"About us  {about_id}, {author_id}"}
    return templates.TemplateResponse(request, "about.html", {"title": 'Cтраница о нас'})
#
#
# @router.get("/contact/")
# async def contact(
#     name: str = Query(None, description="Name of contact"),
#     age: int = Query(None, description="Age of contact"),
# ):
#     print(name)
#     print(type(name))
#     print(age)
#     print(type(age))
#     return {"message": f"Contact {name} {age}"}
