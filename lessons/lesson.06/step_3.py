class User:

    # name = None
    # age = None

    def __init__(self, name):
        self.name = name
        self.age = None

# print(len([]))
# print(len())
# User()

# print(User.name)

print(User.__init__)
help(User.__init__)
user1 = User("Jack")
print(user1.name)
# print((User()).name)
user2 = User("Kate")
print(user2.name)

print("user1.__dict__", user1.__dict__)

user1.name = "Sam"
user2.name = "Ann"
user2.age = 42

print(user1.name)
print(user2.name)
print(user2.age)

# print(User.name)

print(User.__dict__)
print(user1.__dict__)
print(user2.__dict__)


# class Product:
#     pass
#
#
# def init_product(product_object):
#     product_object.name = "Laptop"
#
#
# Product.__init__ = init_product
#
#
# product = Product()
# print(product.name)
# # init_product(product)
# # print(product)
# # print(product.name)
