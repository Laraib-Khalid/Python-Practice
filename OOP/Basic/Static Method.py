class MathOperations:
    def __init__(self, number):
        self.number = number  # Instance variable

    def square(self):
        """Instance method: operates on instance data."""
        return self.number ** 2

    @staticmethod
    def add(a, b):
        """
        Static method: does not depend on instance variables.
        Can be called using the class name or an object.
        """
        return a + b


# Create an object of the class
obj = MathOperations(5)

# Calling instance method (works on object's own data)
print("Square:", obj.square())   # Output: 25

# Calling static method using the class name (recommended way)
print("Addition (via class):", MathOperations.add(3, 7))  # Output: 10

# Static method can also be called using object (not recommended, but valid)
print("Addition (via object):", obj.add(2, 8))  # Output: 10
