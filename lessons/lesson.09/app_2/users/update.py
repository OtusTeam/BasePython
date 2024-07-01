def update(name: str, **kwargs):
    print("updating user", name, "with", kwargs)
    return {"name": name, "details": kwargs}
