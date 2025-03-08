# Importing in Python is the process of 
# loading code from a Python module into the current script. 
# This allows you to use the functions and variables defined 
# in the module in your current script, as well as any additional 
# modules that the imported module may depend on.

# To import a module in Python, you use the import statement followed 
# by the name of the module.
# import math

# result = math.sqrt(9)
# print(result)  # Output: 3.0

# from math import sqrt

# result = sqrt(9)
# print(result)  # Output: 3.0

# from math import sqrt, pi

# result = sqrt(9)
# print(result)  # Output: 3.0

# print(pi)  # Output: 3.141592653589793

# from math import *

# result = sqrt(9)
# print(result)  # Output: 3.0

# print(pi)  # Output: 3.141592653589793

# import math as m

# result = m.sqrt(9)
# print(result)  # Output: 3.0

# print(m.pi)  # Output: 3.141592653589793

# import math

# print(dir(math))

# ---------------------------------------
# from math import sqrt, pi
# from math import pi, sqrt as s
# import math as math_builtin_python

# result = math_builtin_python.sqrt(9) * math_builtin_python.pi
# print(result)  # Output: 3.0

# from harry import welcome, harry
import suyog as hr
import math

print(dir(math))
print(math.nan, type(math.nan))
hr.welcome()
print(hr.suyog)