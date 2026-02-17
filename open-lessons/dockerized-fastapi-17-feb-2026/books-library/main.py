import uvicorn
from config.settings import settings


def main():
    uvicorn.run(
        "app:app",
        host=settings.app.host,
        port=settings.app.port,
        reload=True,
    )


if __name__ == "__main__":
    main()
