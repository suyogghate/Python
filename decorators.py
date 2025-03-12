'''
Python Decorators
    Python decorators are a powerful and versatile tool that allow you 
    to modify the behavior of functions and methods. 
    They are a way to extend the functionality of a function or method 
    without modifying its source code.

    A decorator is a function that takes another function as an 
    argument and returns a new function that modifies the behavior of 
    the original function. The new function is often referred to as 
    a "decorated" function. The basic syntax for using a decorator is 
    the following:
'''
# @decorator_function
# def my_function():
#     pass

# def my_function():
#     pass
# my_function = decorator_function(my_function)

# Decorators are often used to add functionality to functions and 
# methods,such as logging, memoization, and access control.

'''
One common use of decorators is to add logging to a function. 
For example, you could use a decorator to log the arguments and 
return value of a function each time it is called:
'''
# import logging

# def log_function_call(func):
#     def decorated(*args, **kwargs):
#         logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
#         result = func(*args, **kwargs)
#         logging.info(f"{func.__name__} returned {result}")
#         return result
#     return decorated

# @log_function_call
# def my_function(a, b):
#     return a + b

# print(my_function(2, 3))

# ------------------------------------------------------------
def greet(fx):
  print("Inside fx")
  def mfx(*args, **kwargs):
    print("Good Morning")
    fx(*args, **kwargs)
    print("Thanks for using this function")
  return mfx

# @greet
# def hello():
#   print("Hello world")

@greet
def add(a, b):
  print(a+b)
  
# greet(hello)()
# hello()
# greet(add)(1, 2)
add(1, 2)