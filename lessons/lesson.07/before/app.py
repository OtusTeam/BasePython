import baskets

print("I am app.py")
print(__name__)
print("baskets.__name__ = ", baskets.__name__)


def test():
    print('test')


if __name__ == "__main__":
    print("app.py is main module")
    basket = baskets.Basket()
    print(basket)
