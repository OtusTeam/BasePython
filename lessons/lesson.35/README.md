

```shell
gunicorn --workers 4 --worker-class uvicorn.workers.UvicornWorker main:app
```


```shell
gunicorn main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8001
```

