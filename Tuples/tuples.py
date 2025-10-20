"""
🔹 Python Tuples

A tuple is an ordered, immutable collection of elements.

Once created, tuples cannot be modified (no adding, removing, or changing elements).

Tuples are defined using parentheses ( ) or sometimes just commas ,.

Tuples can contain numbers, strings, booleans, lists, or other tuples.
"""


# 1️⃣ Creating Tuples
# Example 1: Different ways to create tuples

numbers = (1, 2, 3, 4, 5)         # Tuple of integers
fruits = ("Apple", "Banana", "Cherry")  # Tuple of strings
mixed = (1, "Hello", True, 3.14)  # Mixed data types
empty = ()                        # Empty tuple
single = (5,)                     # Single element tuple (comma is necessary)

print(numbers)
print(fruits)
print(mixed)
print(empty)
print(single)


# 2️⃣ Accessing Tuple Elements
fruits = ("Apple", "Banana", "Cherry")

print(fruits[0])   # First element -> Apple
print(fruits[1])   # Second element -> Banana
print(fruits[-1])  # Last element -> Cherry



# 3️⃣ Slicing Tuples
numbers = (10, 20, 30, 40, 50, 60, 70)

print(numbers[1:4])   # Index 1 to 3 -> (20, 30, 40)
print(numbers[:3])     # First 3 elements -> (10, 20, 30)
print(numbers[2:])     # From index 2 to end -> (30, 40, 50, 60, 70)
print(numbers[::2])    # Every 2nd element -> (10, 30, 50, 70)
print(numbers[::-1])   # Reverse tuple -> (70, 60, 50, 40, 30, 20, 10)



# 4️⃣ Tuple Immutability
fruits = ("Apple", "Banana", "Cherry")

# fruits[1] = "Mango"  # ❌ This will give an error because tuples are immutable

# We can, however, create a new tuple by combining existing tuples
new_fruits = fruits + ("Mango", "Orange")
print(new_fruits)



# 5️⃣ Tuple Methods

# Tuples have very few methods because they are immutable.

numbers = (1, 2, 3, 2, 4, 2, 5)

print(numbers.count(2))  # Count occurrences of 2 -> 3
print(numbers.index(4))  # Index of first occurrence of 4 -> 4


# 6️⃣ Looping Through a Tuple
fruits = ("Apple", "Banana", "Cherry")

# Using for loop
for fruit in fruits:
    print(fruit)

# Using while loop
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1


# 7️⃣ Nested Tuples
nested = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

# Accessing elements in nested tuple
print(nested[1])      # Second tuple -> (4, 5, 6)
print(nested[1][2])   # Element at row 2, col 3 -> 6



# 8️⃣ Tuple Unpacking
person = ("Laraib", 25, "Lahore")

name, age, city = person
print("Name:", name)
print("Age:", age)
print("City:", city)