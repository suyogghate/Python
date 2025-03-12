# Python Class and Objects
# A class is a blueprint or a template for creating objects, providing
# initial values for state (member variables or attributes), and 
# implementations of behavior (member functions or methods). 
# The user-defined objects are created using the class keyword.
# class Details:
#     name = "Rohan"
#     age = 20

# Object is the instance of the class used to access the properties of the class 
# Now lets create an object of the class.
# obj1 = Details()

# class Details:
#     name = "Rohan"
#     age = 20

# obj1 = Details()
# print(obj1.name)
# print(obj1.age)

# self parameter
# The self parameter is a reference to the current instance of the 
# class, and is used to access variables that belongs to the class.
# It must be provided as the extra parameter inside the method definition.

# class Details:
#     name = "Rohan"
#     age = 20

#     def desc(self):
#         print("My name is", self.name, "and I'm", self.age, "years old.")

# obj1 = Details()
# obj1.desc()

# ------------------------------------------------------------

# class Person:
#   name = "Harry"
#   occupation = "Software Developer"
#   networth = 10
#   def info(self):
#     print(f"{self.name} is a {self.occupation}")


# a = Person()
# b = Person()
# c = Person()

# a.name = "Shubham"
# a.occupation = "Accountant"

# b.name = "Nitika"
# b.occupation = "HR"

# # print(a.name, a.occupation)
# a.info()
# b.info()
# c.info()

# ---------------------------------------------------------------
# Constructors
# A constructor is a special method in a class used to create and 
# initialize an object of a class. There are different types of 
# constructors. Constructor is invoked automatically when an object of a 
# class is created.

'''
    A constructor is a unique function that gets called automatically 
    when an object is created of a class. 
    The main purpose of a constructor is to initialize or assign 
    values to the data members of that class. 
    It cannot return any value other than None.
'''
# def __init__(self):
	# initializations
# init is one of the reserved functions in Python. 
# In Object Oriented Programming, it is known as a constructor.

# Parameterized Constructor in Python
# When the constructor accepts arguments along with self, 
# it is known as parameterized constructor.

# class Details:
#     def __init__(self, animal, group):
#         self.animal = animal
#         self.group = group

# obj1 = Details("Crab", "Crustaceans")
# print(obj1.animal, "belongs to the", obj1.group, "group.")

'''
Default Constructor in Python
When the constructor doesn't accept any arguments from the object 
and has only one argument, self, in the constructor, it is known as a 
Default constructor.
'''

# class Details:
#   def __init__(self):
#     print("animal Crab belongs to Crustaceans group")
# obj1=Details()

class Person:

  def __init__(self, name, occ):
    print("Hey I am a person")
    self.name = name
    self.occ = occ

  def info(self):
    print(f"{self.name} is a {self.occ}")


a = Person("Harry", "Developer")
b = Person("Divya", "HR") 
a.info()
b.info()
# print(a.name)
# a.name = "Divya"
# a.occ = "HR"
# a.info()
