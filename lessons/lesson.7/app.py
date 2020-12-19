# from pprint import pprint
# pprint(locals())
#
# from models import *
# pprint(locals())
#
# from models import BaseModel
# pprint(locals())

# import dis
import mypackage
# from operator import div
from helpers import add, mul
# from helpers import *  # NEVER

# print(div)
# print(mypackage.foobar)

HOURS_IN_DAY = 24
MINUTES_IN_DAY = HOURS_IN_DAY * 60
SECONDS_IN_DAY = MINUTES_IN_DAY * 60
# MINUTES_IN_DAY = 1440


class Spam:
    foo = "bar"
    baz = foo * 3

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.baz + other.baz
        return self + other

def demo_add():
    s = Spam()
    s2 = Spam()
    print(s + s2)


b = None

for i in range(0):
    b = i * 3

if b is None:
    b = -1

# print("b:", b)
#
# print(Spam.baz)

def consts():
    print(HOURS_IN_DAY)
    # HOURS_IN_DAY = 24
    # MINUTES_IN_DAY = HOURS_IN_DAY * 60
    # SECONDS_IN_DAY = MINUTES_IN_DAY * 60
    S_IN_D = 86400
    print(S_IN_D)
    # print(HOURS_IN_DAY, MINUTES_IN_DAY, SECONDS_IN_DAY, S_IN_D)
    # MINUTES_IN_DAY = 1440
    return S_IN_D

# print(dis.dis(consts))


def demo_1():
    import helpers
    # 'a' + 'b' + 'c'
    # "".join(("a", "b", "c"))

    a = 'abc'
    print("Imports 1", a)
    print(helpers)
    print(helpers.add)
    print(helpers.add(1, 2))
    print(helpers.mul(3, 4))


def demo_2():
    print("Imports 2")
    print(add)
    print(add(5, 6))
    print(mul(7, 8))


def demo_models_old():
    import models
    print(models)
    print(models.BaseModelOld)

    from models import BaseModelOld
    print(BaseModelOld)


def demo_models():
    import models
    print(models.BaseModel, models.BaseModelOld)
    import models.base
    print(models.base)
    print(models.base.foobar)
    print(models.base.BaseModel)

    print("models.BaseModel is models.base.BaseModel", models.BaseModel is models.base.BaseModel)


def demo_models_new():
    from models.user import User
    from models.article import Article
    print(User, Article)

    from models import User, Article
    print(User, Article)


if __name__ == "__main__":
    print("main app", __name__)
    print("main app", __file__)
    # consts()
    # demo_1()
    # demo_1()
    # demo_1()
    # demo_2()
    demo_models_old()
    demo_models()
    demo_models_new()
