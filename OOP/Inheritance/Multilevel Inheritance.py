# Multilevel Inheritance Example
# One method call shows details of all parent classes

class A:   # Grandfather
    def show(self):
        print("Class A: Grandfather property and behavior")

class B(A):  # Father
    def show(self):
        super().show()  # Call A's method
        print("Class B: Father property and behavior")

class C(B):  # Son
    def show(self):
        super().show()  # Call B's method (which calls A as well)
        print("Class C: Son property and behavior")

# Create object of last class
obj = C()

# Single method call
obj.show()

print("-" * 50)


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


o = Dog("Tommy", "Black")
o.show_details()
print(GoldenRetriever.mro())