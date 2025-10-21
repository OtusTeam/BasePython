from fastapi import FastAPI
from routers.main_routers import router as main_router
from routers.movies_router import router as movies_router
from routers.api_movies_router import  router as api_movies_router
import uvicorn

app = FastAPI()

app.include_router(main_router, tags=["main"])
app.include_router(api_movies_router, tags=["api_movies"], prefix="/api/v2/movies")
app.include_router(movies_router, tags=["movies"], prefix="/movies")


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


