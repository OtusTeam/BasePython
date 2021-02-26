"""
Hello wold!
Module description

Our first program
"""

print("Hello world!")
print('Hello world!')

my_hello_world_string = "Hello world!"
print(my_hello_world_string)
my_hello_world_string = "Hello, world!!!"
print(my_hello_world_string)

MAX_RETRIES = 1_000_000
MINUTE_SECONDS = 60
HOUR_MINUTES = 60
DAY_HOURS = 24
DAY_SECONDS = MINUTE_SECONDS * HOUR_MINUTES * DAY_HOURS

print(MAX_RETRIES)
print(DAY_SECONDS)

import sys

print(sys.getsizeof(MAX_RETRIES))

multi_line = "hello\nwolrd"
my_multi_line = '''
hello
world
again
new line 
single quotes: ''
three double quotes: """
three single quotes: \'''
'''
