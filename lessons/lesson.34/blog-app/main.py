from fastapi import FastAPI
from api import router as api_router

app = FastAPI()
app.include_router(api_router)


@app.get("/")
def hello_world():
    return {"message": "Hello World"}
