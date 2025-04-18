'''
Single inheritance is a type of inheritance where a class inherits 
properties and behaviors from a single parent class. This is the 
simplest and most common form of inheritance.
'''
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound made by the animal")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
        
    def make_sound(self):
        print("Bark!")

class Cat(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Cat")
        self.breed = breed

    def make_sound(self):
        return print("Meow!")
    
d = Dog("Dog", "Doggerman")
d.make_sound()

a = Animal("Dog", "Dog")
a.make_sound()

# Quick Quiz: Implement a Cat class by using the animal class. Add some methods 

c = Cat("Tom", "Sphinx")
c.make_sound()