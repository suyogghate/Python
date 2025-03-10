# The map function applies a function to each element in a sequence 
# and returns a new sequence containing the transformed elements. 
# The map function has the following syntax:

# map(function, iterable)

# List of numbers
# numbers = [1, 2, 3, 4, 5]

# Double each number using the map function
# doubled = map(lambda x: x * 2, numbers)

# Print the doubled numbers
# print(list(doubled))

# filter
# The filter function filters a sequence of elements based on a 
# given predicate (a function that returns a boolean value) and 
# returns a new sequence containing only the elements that meet 
# the predicate. The filter function has the following syntax:

# filter(predicate, iterable)

# List of numbers
# numbers = [1, 2, 3, 4, 5]

# Get only the even numbers using the filter function
# evens = filter(lambda x: x % 2 == 0, numbers)

# Print the even numbers
# print(list(evens))

# reduce
# The reduce function is a higher-order function that applies a 
# function to a sequence and returns a single value. 
# It is a part of the functools module in Python and has the following syntax:

# reduce(function, iterable)

# from functools import reduce

# List of numbers
# numbers = [1, 2, 3, 4, 5]

# Calculate the sum of the numbers using the reduce function
# sum = reduce(lambda x, y: x + y, numbers)

# Print the sum
# print(sum)

# -----------------------------------
# l = [1, 2, 4, 6, 4, 3]

# newl = list(map(lambda x: x*x*x, l))
# print(newl)

# newnewl = list(filter(lambda x: x>2 , l))
# print(newnewl)

from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5] 

# Calculate the sum of the numbers using the reduce function
def mysum(x, y):
  return x + y
  
sum = reduce(mysum, numbers)

# Print the sum
print(sum)

