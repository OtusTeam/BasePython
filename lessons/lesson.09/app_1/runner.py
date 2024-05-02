from users import USERS_MAGIC_VARIABLE
from products import product_key_id

print("runner module, name:", repr(__name__))


def run():
    print("Run main app, magic variable:",
          USERS_MAGIC_VARIABLE)
    print("product_key_id:", product_key_id)


CONST_MODULE_IS_RUNNING_NAME = "__main__"

if __name__ == CONST_MODULE_IS_RUNNING_NAME:
    run()
