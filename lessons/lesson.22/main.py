import uvicorn
from blog_app.app import app


if __name__ == '__main__':
    uvicorn.run(app)
