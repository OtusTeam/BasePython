from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from utils.templating import TemplateResponse

router = APIRouter()


@router.get(
    "/",
    name="main:index",
    response_class=HTMLResponse,
)
def index(request: Request):
    return TemplateResponse(
        request=request,
        name="index.html",
    )
