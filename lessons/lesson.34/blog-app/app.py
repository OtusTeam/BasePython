import logging

from fastapi import FastAPI

from api import router as api_router

logging.getLogger("uvicorn.access").disabled = True

app = FastAPI()
app.include_router(api_router)
