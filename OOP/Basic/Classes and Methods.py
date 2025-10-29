# 🧩 What are Classes and Methods?
#
# A class is a blueprint for creating objects.
# A method is a function that belongs to a class.
# Objects are instances of a class.
#
# ✅ Example 1: Basic Class and Method


# Define a simple class named Dog
class Dog:
    # This is a method (like a function but inside a class)
    def bark(self):
        print("Woof! Woof!")

# Create an object (instance) of the class
my_dog = Dog()

# Call the method using the object
my_dog.bark()




class Person:
  name = "Harry"
  occupation = "Software Developer"
  networth = 10
  def info(self):
    print(f"{self.name} is a {self.occupation}")


a = Person()
b = Person()
c = Person()

a.name = "Shubham"
a.occupation = "Accountant"

b.name = "Nitika"
b.occupation = "HR"

# print(a.name, a.occupation)
a.info()
b.info()
c.info()
