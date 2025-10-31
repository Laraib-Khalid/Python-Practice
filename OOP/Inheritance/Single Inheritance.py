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
        print("Meow!")


d = Dog("Dog", "Doggerman")
d.make_sound()

c = Cat("Cat", "Cat")
c.make_sound()

a = Animal("Dog", "Dog")
a.make_sound()



print("-" * 50)


# Parent Class (Base Class)
class Animal:
    def speak(self):       # Parent method
        print("Animals can make sounds")

# Child Class (Derived Class)
# This class inherits from Animal class
class Dog(Animal):
    def bark(self):        # Child class method
        print("Dog barks: Woof! Woof!")

# Create object of child class
d = Dog()

# Calling parent class method using child object
d.speak()   # Inherited from Animal

# Calling child class method
d.bark()
