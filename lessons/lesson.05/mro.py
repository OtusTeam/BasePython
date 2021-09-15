class Mammal:
    pass


class HomoSapiens(Mammal):
    pass


class Human(HomoSapiens, Mammal):
    pass


print(Mammal.mro())
print(HomoSapiens.mro())
print(Human.mro())
