# 🎯 dir() gives list of methods & attributes of an object

name = "Hello"

print(dir(name))  # Shows all methods available for string like upper(), lower(), etc.
name.removeprefix("Hel")
print(name.removeprefix("Hel"))
print(name.removesuffix("lo"))



# ✅ Example of __dict__
#
# __dict__ shows the instance variables stored inside an object (as a dictionary)

class Person:
    def __init__(self, name, age):
        self.name = name      # instance variable
        self.age = age        # instance variable

p = Person("Ali", 22)

print(p.__dict__)  # Shows object's data as dictionary



# ✅ Example of help()
#
# help() gives explanation/documentation about Python functions, classes, keywords, etc.

# 🎯 help() shows information about a function or class

help(len)       # Gives documentation about len() function
help(str)       # Shows details about string class
help(print)     # Help for print() function


print("-" * 50)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1


p = Person("John", 30)
print(p.__dict__)

print(help(Person))