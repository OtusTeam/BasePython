from pydantic import BaseModel
from pydantic import ConfigDict


class Config(BaseModel):
    model_config = ConfigDict(extra="forbid", hide_input_in_errors=True)
