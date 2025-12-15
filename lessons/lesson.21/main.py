from fastapi import FastAPI
import uvicorn
from routers.movies import router as movies_router
from routers.main_pages import router as main_pages_router
from routers.html_movies import router as html_router


app = FastAPI()
app.include_router(movies_router, tags=["api movies"], prefix="/api/v2/movies")
app.include_router(main_pages_router, tags=["Main"])
app.include_router(html_router, tags=["HTML Movies"], prefix="/movies")


if __name__ == '__main__':
    uvicorn.run('main:app', host="127.0.0.1", port=8000, reload=True)