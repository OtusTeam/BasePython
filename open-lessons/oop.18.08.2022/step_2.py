class User:
    name = "John"
    age = "30"


"""
# дескрипторы: поиск атрибутов на объектах
- на экземпляре
- на классе экземпляра
- на родителях класса (типа)
- на родителях родителя (до самого верха -- object)
!- если не найдено - ошибка!
"""

print("User name", User.name)
print("User age", User.age)


user1 = User()
print(User.mro())
print("user1 name", user1.name)
print("user1 age", user1.age)
print("user1 dict", user1.__dict__)

user1.name = "Nick"
print("user1 name", user1.name)
print("user1 dict", user1.__dict__)
print("User name", User.name)

user2 = User()
print("user2 name", user2.name)

User.name = "Bob"
print("user1 name", user1.name)
print("user2 name", user2.name)

