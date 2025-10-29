# 🧩 1. Function
#
# A function is a block of code that performs a specific task.
# It can exist inside or outside a class.
#
# ✅ Example:
# A simple function (outside any class)
def add(a, b):
    return a + b

result = add(5, 10)
print(result)
#
# 🧠 Key Points:
#
# Defined using def keyword.
#
# Can be called anywhere in the program.
#
# Not related to any object or class.
#



# 🧩 2. Method
#
# A method is just a function defined inside a class.
# It always takes self as the first parameter to access class attributes.
#
# ✅ Example:
class Calculator:
    def add(self, a, b):   # <-- method
        return a + b

# Create object
calc = Calculator()
print(calc.add(5, 10))

# 🧠 Key Points:
#
# Methods are functions inside classes.
#
# They work on objects and can access object data (self).
#
# Called using the object name like object.method().
#


# 🧩 3. Constructor
#
# A constructor is a special method in a class that runs automatically when an object is created.
# In Python, the constructor is always named __init__.
#
# ✅ Example:
class Student:
    def __init__(self, name, age):   # <-- constructor
        self.name = name
        self.age = age

    def show(self):  # normal method
        print(f"Name: {self.name}, Age: {self.age}")

# Creating object -> constructor runs automatically
s1 = Student("Laraib", 25)
s1.show()

# 🧠 Key Points:
#
# Constructor name is always __init__.
#
# Used to initialize object attributes.
#
# Automatically called when you create an object.
#
# No need to call it manually.