# Пример декоратора

# def sample_decorator(func):
#     def wrapper():
#         print("wrapper start")
#         func()
#         print("wrapper end")
#     return wrapper
#
#
# def say_hi():
#     print("Hi!")
#
#
# greet = sample_decorator(say_hi)
# # print(greet)
# greet()

# Синтаксический Сахар
# def sample_decorator(func):
#     def wrapper():
#         print("wrapper start")
#         func()
#         print("wrapper end")
#     return wrapper
# 
#
# @sample_decorator
# def say_hi():
#     print("Hi!")
#
# say_hi()

