def hello(name, age, dish, *args):
    print(
        f"Hello, {name}!",
        "You are",
        age,
        "and your favorite dish is",
        dish,
    )


hello("John", 22, "Spaghetti")
hello("Sam", 18, "Pizza")

# hello("Pete", None, None, None)
# hello("Pete")

nick_data = ["Nick", 42, "Salad", "nick@example.com"]
hello(nick_data[0], nick_data[1], nick_data[2])
hello(*nick_data)
hello("Kyle", age=33, dish="Pizza")
hello("Kyle", dish="Pizza", age=33)
