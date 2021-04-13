from time import sleep
import redis

r = redis.Redis()

print("foo:", r.get("foo"))
print("spam:", r.get("spam"))

print("mset", r.mset({"bar": "baz", "spam": "eggs", "abc": "123"}))

print("setex token", r.setex("token", 3, "qwert1234"))

print("mget", r.mget(("foo", "bar", "abc", "token")))

sleep(3)

print(r.get("token"))

print("lessons", r.hgetall("lesson"))
