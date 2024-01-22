# from datetime import datetime
# import datetime

import products
import users
# from users import *

# from users.create import create as user_create
# from users.update import update
# import products, users


def main():
    # user_create('Ivan')
    # update('Ivan', age=28)
    users.create('Ivan')
    users.update('Ivan', age=28)

    products.create('iphone')
    products.update('iphone', price=1000)


main()
