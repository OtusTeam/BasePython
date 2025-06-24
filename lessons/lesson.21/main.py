from fastapi import FastAPI
import uvicorn
from routers.movie_router import router as movie_router
from routers.index_routers import router as index_routers

app = FastAPI()


app.include_router(index_routers)
app.include_router(movie_router)


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)