Базовое приложение отсюда:
https://github.com/mahenzon/fastapi-users-intro/

# FastAPI Example App

FastAPI-Users:
- GitHub https://github.com/fastapi-users/fastapi-users
- Docs https://fastapi-users.github.io/fastapi-users/latest/


FastAPI Base app:
- https://github.com/mahenzon/FastAPI-base-app


Run with usage of env params:

```shell
./run

# or

python run_main.py
```

or

```shell
gunicorn main:main_app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```


```shell
http OPTIONS http://localhost:8000/api/v1/auth/login 'Access-Control-Request-Method:GET' 'Origin: http://localhost:8000'
```
