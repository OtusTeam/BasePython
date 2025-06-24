from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
def index(request: Request):
    title1 = 'Главная страница'
    text = "Главная страница компании"
    context = {"request": request,
               "title": title1,
               "text": text}
    return templates.TemplateResponse("index.html", context=context)


@router.get("/about/", response_class=HTMLResponse)
def about(request: Request):
    title1 = 'О нас'
    text = "Подробная статья о нас"
    context = {"request": request,
               "title": title1,
               "text": text}
    return templates.TemplateResponse("about.html", context=context)