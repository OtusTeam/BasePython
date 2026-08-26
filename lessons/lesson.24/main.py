from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_root():
    return {"By": "World 12345"}