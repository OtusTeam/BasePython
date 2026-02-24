import uvicorn
from fastapi import FastAPI
from routers.main_pages import router as main_pages_router
from routers.movies import router as movies_router
from routers.html_movies import router as html_router


app = FastAPI()
app.include_router(main_pages_router, tags=["Main pages"])
app.include_router(movies_router, tags=["API movies"], prefix="/api/v1/movies")
app.include_router(html_router, tags=["HTML movies"], prefix="/movies")


if __name__ == '__main__':
    uvicorn.run('main:app', host="127.0.0.1", port=8000, reload=True)
