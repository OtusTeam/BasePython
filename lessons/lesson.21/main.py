from fastapi import FastAPI
import uvicorn
from routers.main_pages import router as main_page_router
from routers.movies import router as movies_router
from routers.html_movie import router as html_movie_router


app = FastAPI()
app.include_router(main_page_router, tags=["Main page"])
app.include_router(movies_router, tags=["Movies"], prefix="/api/v1/movies")
app.include_router(html_movie_router, tags=["HTML Movies"], prefix="/movies")



if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)