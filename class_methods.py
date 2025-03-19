'''
What are Python Class Methods?
A class method is a type of method that is bound to the class and 
not the instance of the class. In other words, it operates on the 
class as a whole, rather than on a specific instance of the class. 
Class methods are defined using the "@classmethod" decorator, 
followed by a function definition. The first argument of the 
function is always "cls," which represents the class itself.
'''
# class ExampleClass:
#     @classmethod
#     def factory_method(cls, argument1, argument2):
#         return cls(argument1, argument2)

# ----------------------------------------------------

# class Employee:
#   company = "Apple"
#   def show(self):
#     print(f"The name is {self.name} and company is {self.company}")

#   @classmethod
#   def changeCompany(cls, newCompany):
#     cls.company = newCompany


# e1 = Employee()
# e1.name = "Harry"
# e1.show()
# e1.changeCompany("Tesla")
# e1.show()
# print(Employee.company)

# -----------------------------------------------------------------

# Class Methods as Alternative Constructors
'''
A class method belongs to the class rather than to an instance of 
the class. One common use case for class methods as alternative 
constructors is when you want to create an object from data that 
is stored in a different format, such as a string or a dictionary. 
For example, consider a class named "Person" that has two attributes: "name" and "age". 
'''
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def from_string(cls, string):
#         name, age = string.split(',')
#         return cls(name, int(age))

# person = Person.from_string("John Doe, 30")
# print(person.name)
# print(person.age)

'''
Another common use case for class methods as alternative constructors is when 
you want to create an object with a different set of default values than what is 
provided by the default constructor. For example, consider a class named "Rectangle" 
that has two attributes: "width" and "height"
'''
# class Rectangle:
#   def __init__(self, width, height):
#     self.width = width
#     self.height = height

#   @classmethod
#   def square(cls, size):
#     return cls(size, size)

# rectangle = Rectangle.square(10)
# print(rectangle.height)
# print(rectangle.width)

# --------------------------------------------

class Employee:
  def __init__(self, name, salary):
    self.name = name 
    self.salary = salary
    
  @classmethod
  def fromStr(cls, string):
    return cls(string.split("-")[0], int(string.split("-")[1]))
    
e1 = Employee("Harry", 12000)
print(e1.name)
print(e1.salary)

string = "John-12000"
e2 = Employee.fromStr(string)
print(e2.name)
print(e2.salary)