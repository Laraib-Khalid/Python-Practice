# Getter and Setter Example in Python

class Person:
    def __init__(self, name, age):
        # Private attributes (using underscore)
        self._name = name
        self._age = age

    # Getter method for 'name'
    @property
    def name(self):
        return self._name

    # Setter method for 'name'
    @name.setter
    def name(self, value):
        if not value:  # check if empty
            print("Name cannot be empty!")
        else:
            self._name = value

    # Getter method for 'age'
    @property
    def age(self):
        return self._age

    # Setter method for 'age'
    @age.setter
    def age(self, value):
        if value < 0:
            print("Age cannot be negative!")
        else:
            self._age = value


# Create object of Person class
p = Person("Laraib", 25)

# Accessing values using getter
print("Name:", p.name)
print("Age:", p.age)

# Setting values using setter
p.name = "Khalid"
p.age = 30

print("\nAfter updating values:")
print("Name:", p.name)
print("Age:", p.age)

# Trying to set invalid values
p.age = -5     # Invalid -> shows validation message
p.name = ""    # Invalid -> shows validation message


print("-" * 50)


# ✅ Example 2: Using property and setter
class MyClass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"Value is {self._value}")

    @property
    def ten_value(self):
        return 10 * self._value

    @ten_value.setter
    def ten_value(self, new_value):
        self._value = new_value / 10


obj = MyClass(10)
obj.ten_value = 67
print(obj.ten_value)
obj.show()



# | Type                   | Example       | Access Outside Class    | Meaning                  |
# | ---------------------- | ------------- | ----------------------- | ------------------------ |
# | Public                 | `self.name`   | ✅ Yes                   | Normal, fully accessible |
# | Protected (convention) | `self._name`  | ✅ Yes (not recommended) | Internal use             |
# | Private (name-mangled) | `self.__name` | ⚠️ No (without trick)   | Strongly internal        |
