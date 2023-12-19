def foo():
    res = ["abc"]
    err = None
    if ...:
        err = "something happened"

    return res, err


def bar():
    # res = foo()
    res, err = foo()
    if err is not None:
        return None, err
    ...
    return "abc", err


def main():
    res, err = foo()
    if err is not None:
        return None, err
