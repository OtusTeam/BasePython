import products
import users


def main():
    users.create('Ivan')
    users.update('Ivan', age=28)

    products.create('iphone')
    products.update('iphone', price=1000)


main()
