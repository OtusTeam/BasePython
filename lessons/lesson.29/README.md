
```shell
gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

```Dockerfile
WORKDIR /var/app

COPY fastapi-users-app ./
```
