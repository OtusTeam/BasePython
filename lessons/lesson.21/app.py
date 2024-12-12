from fastapi import FastAPI
from pydantic import BaseModel, validator, HttpUrl, EmailStr
from routers.product_router import router as product_router
import uvicorn


app = FastAPI()


class User(BaseModel):
    username: str
    # email: EmailStr
    age: int | None = None
    address: Address

app.include_router(product_router, prefix='/api', tags=['item_product'])

@app.get("/")
async def index(request: Request):
    item = request.headers.get('item')
    return {"message": "Hello World"}

if __name__ == '__main__':
    uvicorn.run("app:app", host='127.0.0.1', port=8000)