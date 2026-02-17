
```shell
gunicorn app:app \
  --workers 2 \
  --worker-class uvicorn_worker.UvicornWorker \
  --bind 0.0.0.0:8000 \
  --access-logfile -
```