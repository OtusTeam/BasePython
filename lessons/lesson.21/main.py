from fastapi import FastAPI, HTTPException, Query
# from pydantic import BaseModel
import uvicorn
from models import Movie
from routers.main_router import router as main_router
from routers.movies_router import router as movies_router
from routers.api_movies_router import router as api_movies_router


app = FastAPI()

app.include_router(main_router, tags=["main"])
app.include_router(movies_router, prefix="/movies", tags=["movies"])
app.include_router(api_movies_router, prefix="/api/movies", tags=["api movies"])


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)