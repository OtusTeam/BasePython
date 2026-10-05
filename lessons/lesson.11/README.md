```pycon
>>> data = {"foo": "bar"}
>>> isinstance(data, dict | int | str | list)
True
>>> 
>>> isinstance(data, dict)
True
>>> isinstance(data, int | str | list)
False
>>> numbers = set()
>>> numbers.add(1)
>>> numbers
{1}
>>> isinstance(data, numbers | int | str | list)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: unsupported operand type(s) for |: 'set' and 'type'
>>> isinstance(numbers, dict | int | str | list)
False
>>> isinstance(data, numbers | int | str | list | set)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: unsupported operand type(s) for |: 'set' and 'type'
>>> isinstance(numbers, dict | int | str | list | set)
True
>>> isinstance(numbers, set)
True
>>> number = "forty two"
>>> isinstance(numbers, int | str)
False
>>> isinstance(number, int | str)
True
>>> isinstance(number, str)
True
>>> isinstance(number, int)
False
>>> number = 42
>>> isinstance(number, int)
True
>>> isinstance(number, int | str)
True
>>> isinstance(number, str)
False
>>> z = ZeroDivisionError()
>>> z
ZeroDivisionError()
>>> isinstance(z, ZeroDivisionError)
True
>>> isinstance(z, TypeError)
False
>>> isinstance(z, ArithmeticError)
True
>>> is_number = True
>>> type(is_number)
<class 'bool'>
>>> has_name = True
>>> 
>>> type(has_name)
<class 'bool'>
>>> isinstance(has_name, str | int | bool)
True
>>> isinstance(has_name, int | bool)
True
>>> isinstance(has_name, bool)
True
>>> isinstance(has_name, int)
True
>>> int(True)
1
>>> int(False)
0
>>> True == 1
True
>>> False = 0
  File "<input>", line 1
    False = 0
    ^^^^^
SyntaxError: cannot assign to False
>>> False == 0
True
```
