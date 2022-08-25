import logging

logger = logging.getLogger(__name__)


def div_safe(a, b):
    try:
        c = a / b
    # except ArithmeticError:
    #     return 1
    except ZeroDivisionError:
        # logger.exception("divide by zero")
        # logger.error("divide by zero")
        # logger.warning("divide by zero", exc_info=True)

        print("please don't divide by zero")
        return 42
    except TypeError as e:
        # print(e.__traceback__)
        # logger.warning("type error", exc_info=e)

        print("oops", e.args, repr(e))
        # return None
    # except Exception:
    #     pass
    else:
        print("ok div, res:", [a, b], c)
        return c
    finally:
        print("finally for", [a, b])

    print("leaving func, args:", [a, b])



print(div_safe(1, 0))
print(div_safe(2, 1))
print(div_safe(10, 2))
print(div_safe("10", 2))
