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