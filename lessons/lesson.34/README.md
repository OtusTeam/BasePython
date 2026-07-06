
```shell
gunicorn app:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

```shell
uvicorn app:app --host 0.0.0.0 --port 8000 --workers 4 --log-level info
```


```shell
uv run uvicorn app:app --host 0.0.0.0 --port 8002 --workers 1 --log-level info
```
