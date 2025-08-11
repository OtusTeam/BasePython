from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    context = {
        "request": request,
        "title": "Кинотеатр",
        "user": "Боб"}
    return templates.TemplateResponse("index.html", context)


@router.get("/about/")
async def about():
    return {"message": "About us!"}
