# This is my FastAPI app

Run app:

```shell
gunicorn main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8002
```