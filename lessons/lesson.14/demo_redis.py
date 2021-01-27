import redis

# r = redis.Redis(host="localhost", port=6379)
r = redis.Redis(db=7)


print("get foo", r.get("foo"))
print("get A", r.get("A"))
print("mget", r.mget(["A", "C", "foo", "D"]))
print("get D", r.get("D"))

print("set spam", r.set("spam", "eggs"))
print("setex secret_key", r.setex("secret_key", 10, "secret value"))
