
```shell
gunicorn --workers=1 --worker-class=uvicorn.workers.UvicornWorker --bind=localhost:8001 main:app
```
