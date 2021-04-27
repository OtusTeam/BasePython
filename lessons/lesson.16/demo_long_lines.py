

LONG_LINE = """
hello
'''darkness'''
''my''
"old"
'friend'
"""

print("long line:")
print(LONG_LINE)
print("repr long line:")
print(repr(LONG_LINE))


def my_func():
    """
    This is docstring
    :return:
    """


print("my_func", my_func, "doc:", my_func.__doc__)


def my_another_func():
    'thi' "s is" " a d" """oc t""" '''oo'''
    "this is not a doc already"


print("my_another_func", my_another_func, "doc:", my_another_func.__doc__)
