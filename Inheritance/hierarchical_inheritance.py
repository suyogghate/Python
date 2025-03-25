'''
Hierarchical Inheritance
Hierarchical Inheritance is a type of inheritance in Object-Oriented 
Programming where multiple subclasses inherit from a single base class. 
In other words, a single base class acts as a parent class for multiple 
subclasses. This is a way of establishing relationships between classes 
in a hierarchical manner.
'''
class Animal:
    def __init__(self, name):
        self.name = name

    def show_details(self):
        print("Name:", self.name)

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name)
        self.breed = breed

    def show_details(self):
        Animal.show_details(self)
        print("Species: Dog")
        print("Breed:", self.breed)

class Cat(Animal):
    def __init__(self, name, color):
        Animal.__init__(self, name)
        self.color = color

    def show_details(self):
        Animal.show_details(self)
        print("Species: Cat")
        print("Color:", self.color)

dog = Dog("Max", "Golden Retriever")
dog.show_details()
cat = Cat("Luna", "Black")
cat.show_details()

'''
# Hierarchical Inheritance
class BaseClass:
  pass

class D1(BaseClass):
  pass

class D2(BaseClass):
  pass

class D3(D1):
  pass
'''