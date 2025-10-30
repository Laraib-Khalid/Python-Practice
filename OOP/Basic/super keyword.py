class Employee:
  def __init__(self, name, id):
    self.name = name
    self.id = id

class Programmer(Employee):
  def __init__(self, name, id, lang):
    super().__init__(name, id)
    self.lang = lang

rohan = Employee("Rohan Das", "420")
harry = Programmer("Harry", "2345", "Python")
print(harry.name)
print(harry.id)
print(harry.lang)

print("-" * 50)


# ✅ Example 1: Using super() to call parent constructor
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

# Child class
class Dog(Animal):
    def __init__(self, name, breed):
        # Using super() to call parent class __init__
        super().__init__(name)
        self.breed = breed

dog1 = Dog("Tommy", "German Shepherd")
print(dog1.name)   # From Animal class
print(dog1.breed)  # From Dog class


print("-" * 50)



# ✅ Example 2: Calling parent method using super()
class A:
    def show(self):
        print("This is method of Class A")

class B(A):
    def show(self):
        # Call parent method
        super().show()
        print("This is method of Class B")

obj = B()
obj.show()



print("-" * 50)


# ✅ Example 3: Real-life Example (Employee → Manager)
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def details(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        # Calling parent constructor
        super().__init__(name, salary)
        self.bonus = bonus

    def details(self):
        # Call parent method first
        super().details()
        print(f"Bonus: {self.bonus}")

m = Manager("Ali", 50000, 10000)
m.details()