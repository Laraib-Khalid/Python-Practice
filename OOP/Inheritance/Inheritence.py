# Inheritance and Access Modifiers Example in Python

# Base (Parent) class
class Animal:
    def speak(self):
        print("Animal speaks")

# Derived (Child) class
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Create object of child class
d = Dog()

# Access methods from both parent and child
d.speak()   # inherited from Animal
d.bark()    # defined in Dog


print("*" * 50)



# 🧩 2. Access Modifiers (Simple Example)
class Person:
    def __init__(self):
        self.name = "Laraib"      # Public
        self._age = 25            # Protected (convention)
        self.__salary = 70000     # Private

    def show(self):
        print("Name:", self.name)
        print("Age:", self._age)
        print("Salary:", self.__salary)


p = Person()

# Public attribute → can access directly
print(p.name)       # ✅ OK

# Protected attribute → can access (not recommended)
print(p._age)       # ⚠️ OK but for internal use

# Private attribute → cannot access directly
# print(p.__salary) # ❌ Error
# Correct way (access inside class)
p.show()

# Access private variable using name mangling (not recommended)
print(p._Person__salary)  # ✅ Works but not a good practice


print("*" * 50)

# ==============================
# Base Class (Parent Class)
# ==============================
class Person:
    def __init__(self, name, age, salary):
        # Public attribute (can be accessed anywhere)
        self.name = name

        # Protected attribute (single underscore -> internal use only)
        self._age = age

        # Private attribute (double underscore -> not directly accessible)
        self.__salary = salary

    # Public method
    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self._age}")
        print(f"Salary (inside class): {self.__salary}")

    # Private method (only accessible inside the class)
    def __show_salary(self):
        print(f"Private Salary: {self.__salary}")

    # Public method that calls the private one
    def access_private_method(self):
        self.__show_salary()


# ==============================
# Derived Class (Child Class)
# ==============================
class Employee(Person):
    def __init__(self, name, age, salary, department):
        # Call the parent class constructor
        super().__init__(name, age, salary)
        self.department = department

    def show_employee_details(self):
        # Accessing public member (✅ Allowed)
        print(f"Employee Name: {self.name}")

        # Accessing protected member (✅ Allowed in subclass)
        print(f"Employee Age: {self._age}")

        # Trying to access private member (❌ Not allowed directly)
        # print(self.__salary)  # This would cause an AttributeError

        # Accessing private member using name mangling (⚠️ Not recommended)
        print(f"Employee Salary (accessed using name mangling): {self._Person__salary}")

        print(f"Department: {self.department}")


# ==============================
# Object Creation and Usage
# ==============================

# Create an object of the child class
emp = Employee("Laraib", 25, 70000, "QA Department")

# Access public method from base class
print("\n--- Using Base Class Method ---")
emp.show_info()

# Access method defined in child class
print("\n--- Using Derived Class Method ---")
emp.show_employee_details()

# Access protected attribute directly (⚠️ Possible, but not recommended)
print("\n--- Accessing Protected Attribute Directly ---")
print(emp._age)   # works, but not good practice

# Trying to access private attribute directly (❌ Causes error)
print("\n--- Trying to Access Private Attribute Directly ---")
try:
    print(emp.__salary)
except AttributeError:
    print("Cannot access private attribute '__salary' directly!")

# Access private method through public method
print("\n--- Accessing Private Method through Public Method ---")
emp.access_private_method()
