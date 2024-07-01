def update(name: str, **kwargs):
    print("updating product", name, "with params", kwargs)
    return {"name": name, "params": kwargs}
