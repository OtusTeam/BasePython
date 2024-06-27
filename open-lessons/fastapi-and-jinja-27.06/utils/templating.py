__all__ = (
    "templates",
    "TemplateResponse",
)

from starlette.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
TemplateResponse = templates.TemplateResponse
