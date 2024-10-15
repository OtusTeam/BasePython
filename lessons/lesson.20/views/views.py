from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi import APIRouter

router = APIRouter()


templates = Jinja2Templates(directory="templates")


@router.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "title": "Home"}
    )


@router.get("/buttons")
async def read_buttons(request: Request):
    return templates.TemplateResponse(
        "buttons.html", {"request": request, "title": "Buttons"}
    )


@router.get("/carousel")
async def read_carousel(request: Request):
    return templates.TemplateResponse(
        "carousel.html", {"request": request, "title": "Carousel"}
    )


@router.get("/forms")
async def read_forms(request: Request):
    return templates.TemplateResponse(
        "forms.html", {"request": request, "title": "Forms"}
    )


@router.get("/columns")
async def read_columns(request: Request):
    return templates.TemplateResponse(
        "columns.html", {"request": request, "title": "Responsive Columns"}
    )


@router.get("/accordeon")
async def read_columns(request: Request):
    return templates.TemplateResponse(
        "accordeon.html", {"request": request, "title": "Accordeon"}
    )


@router.get("/cards")
async def read_columns(request: Request):
    return templates.TemplateResponse(
        "cards.html", {"request": request, "title": "Cards"}
    )


@router.get("/modal")
async def read_modal(request: Request):
    return templates.TemplateResponse(
        "modal.html", {"request": request, "title": "Modal Example"}
    )


@router.get("/navbar")
async def read_modal(request: Request):
    return templates.TemplateResponse(
        "navbar.html", {"request": request, "title": "Navbar Example"}
    )


@router.get("/clicker")
async def read_clicker(request: Request):
    return templates.TemplateResponse(
        "clicker.html", {"request": request, "title": "Clicker Game"}
    )


@router.get("/dropdown")
async def read_clicker(request: Request):
    return templates.TemplateResponse(
        "dropdown.html", {"request": request, "title": "Dropdown"}
    )
