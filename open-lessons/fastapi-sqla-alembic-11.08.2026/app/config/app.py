from pydantic import BaseModel
from pydantic import Field


class AppConfig(BaseModel):
    name: str = "FastAPI application"
    debug: bool = False
    api_v1_prefix: str = Field(
        default="/api/v1",
        min_length=2,
    )
