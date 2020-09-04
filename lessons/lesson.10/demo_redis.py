from time import sleep
import redis

USERS_FUNDS = {}

r = redis.Redis()

print("foo:", r.get("foo"))

print("spam:", r.get("spam"))

print("A, B, D:", r.mget(("A", "B", "D")))
print(r.set("qwe", 123))
print(r.get("qwe"))

print(r.setex("qwerty", 1, "foobar"))
print(r.get("qwerty"))
sleep(1)
print(r.get("qwerty"))

print(r.hgetall("lessons"))
