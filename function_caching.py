'''
Function caching is a technique for improving the performance 
of a program by storing the results of a function call so that 
you can reuse the results instead of recomputing them every time 
the function is called. This can be particularly useful when a 
function is computationally expensive, or when the inputs to the 
function are unlikely to change frequently.

In Python, function caching can be achieved using the 
functools.lru_cache decorator. The functools.lru_cache decorator 
is used to cache the results of a function so that you can reuse 
the results instead of recomputing them every time the function is 
called. 
'''
# import functools

# @functools.lru_cache(maxsize=None)
# def fib(n):
#     if n < 2:
#         return n
#     return fib(n-1) + fib(n-2)

# print(fib(20))
# Output: 6765
'''
The maxsize parameter is used to specify the maximum number 
of results to cache. If maxsize is set to None, the cache will 
have an unlimited size.
'''

# -------------------------------------------------------------

from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(n):
  time.sleep(5)
  return n*5
    

print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(6))
print("done for 6")

print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(6))
print("done for 6")
print(fx(61))
print("done for 61")
# Output: 6765