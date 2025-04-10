'''
Multilevel Inheritance in Python
Multilevel inheritance is a type of inheritance in object-oriented 
programming where a derived class inherits from another derived 
class. This type of inheritance allows you to build a hierarchy of 
classes where one class builds upon another, leading to a more 
specialized class.
'''
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
        
    def show_details(self):
        Animal.show_details(self)
        print(f"Breed: {self.breed}")
        
class GoldenRetriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed="Golden Retriever")
        self.color = color
        
    def show_details(self):
        Dog.show_details(self)
        print(f"Color: {self.color}")

# dog = GoldenRetriever("Max", "Golden")
# dog.show_details()

o = Dog("tommy", "Black")
o.show_details()
print(GoldenRetriever.mro())