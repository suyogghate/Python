# In Python, a lambda function is a small anonymous function without a name. 
# It is defined using the lambda keyword.
# Lambda functions are often used in situations where a small function is required for a short period of time. 
# They are commonly used as arguments to higher-order functions, such as map, filter, and reduce.

# Function to double the input
# def double(x):
#   return x * 2

# Lambda function to double the input
# double = lambda x: x * 2

# print(double(5))

# Lambda functions can have multiple arguments, just like regular functions. 
# Here is an example of a lambda function with multiple arguments:
# Function to calculate the product of two numbers
# def multiply(x, y):
#     return x * y

# Lambda function to calculate the product of two numbers
# fun = lambda x, y: x * y

# print(fun(3,6))

# Lambda functions can also include multiple statements, but they are limited to a 
# single expression. For example:
# Lambda function to calculate the product of two numbers,
# with additional print statement
# twoArgs = lambda x, y: print(f'{x} * {y} = {x * y}')

# print(twoArgs(5,10))

# ------------------------------------------------------
# def double(x):
#   return x*2

def appl(fx, value):
  return 6 + fx(value)

double = lambda x: x * 2
cube = lambda x: x * x * x
avg = lambda x, y, z: (x + y + z) / 3

print(double(5))
print(cube(5))
print(avg(3, 5, 10))
print(appl(lambda x: x * x , 2))