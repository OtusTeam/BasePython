from fastapi import FastAPI

from api_v1 import router as router_v1
from api_v2 import router as router_v2
from api_v3 import router as router_v3

app = FastAPI()
app.include_router(router_v1, prefix="/api/v1", tags=["v1"])
app.include_router(router_v2, prefix="/api/v2", tags=["v2"])
app.include_router(router_v3, prefix="/api/v3", tags=["v3"])
