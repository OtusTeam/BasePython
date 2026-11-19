import uvicorn
from fastapi import FastAPI

from routers.movies import router as movies_router
from routers.main_pages import router as main_router


app = FastAPI()

app.include_router(main_router, tags=["Main Pages"])
app.include_router(movies_router, tags=["Movies"], prefix="/api/v2/movies")

if __name__ == '__main__':
    uvicorn.run('main:app', host="127.0.0.1", port=8000, reload=True)