from typing import Any

from fastapi.templating import Jinja2Templates

from config import BASE_DIR

TEMPLATES_DIR = BASE_DIR / "templates"
templates = Jinja2Templates(
    directory=TEMPLATES_DIR,
)


def render_string(
    name: str,
    **context: Any,  # noqa: ANN401
) -> str:
    return templates.env.get_template(name).render(**context)
