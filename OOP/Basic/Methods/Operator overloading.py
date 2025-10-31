# Example: Operator Overloading in Python

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overload + operator
    def __add__(self, other):
        # Add x and y values of two objects
        return Point(self.x + other.x, self.y + other.y)

    # Overload == operator
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # Overload > operator (greater than)
    def __gt__(self, other):
        return (self.x + self.y) > (other.x + other.y)

    # Overload string print
    def __str__(self):
        return f"({self.x}, {self.y})"


# Creating objects
p1 = Point(3, 5)
p2 = Point(2, 4)

# Using overloaded +
result = p1 + p2   # Calls __add__()
print("Addition:", result)

# Using overloaded ==
print("Equal?:", p1 == p2)   # Calls __eq__()

# Using overloaded >
print("Greater?:", p1 > p2)  # Calls __gt__()

print(f"{'-' * 50}")


class Vector:
  def __init__(self, i, j, k):
    self.i = i
    self.j = j
    self.k = k

  def __str__(self):
    return f"{self.i}i + {self.j}j + {self.k}k"

  def __add__(self, x):
    return Vector(self.i + x.i,  self.j+x.j, self.k+x.k)
v1 = Vector(3, 5, 6)
print(v1)

v2 = Vector(1, 2, 9)
print(v2)

print(v1 + v2)
print(type(v1 + v2))