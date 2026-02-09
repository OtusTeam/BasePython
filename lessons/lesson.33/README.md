```python
class User: 
    ...

user = User()
user.username = "alice"
user.save()

user = get_from_db_by_username("bob")
user.email = "bob@new-address.com"
user.save()


bonus = get_daily_bonus()
users = get_active_users()
for user in users:
    # user.topup_daily_bonus()
    bonus.topup_user(user)

```

```shell
gunicorn "app:app" \
  --workers 1 \
  --worker-class uvicorn_worker.UvicornWorker \
  --bind 0.0.0.0:8001
```

```shell
gunicorn "simple_aiohttp_webserver:app" \
  --bind 0.0.0.0:5050 \
  --workers 2 \
  --worker-class aiohttp.GunicornWebWorker
```
