# =====================================================
# Python Tuple Methods and Modifications Example
# =====================================================

# 1️⃣ Creating tuples
numbers = (1, 2, 3, 2, 4, 2, 5)
fruits = ("Apple", "Banana", "Cherry", "Banana")
nested = ((1, 2), (3, 4), (5, 6))

print("Original numbers tuple:", numbers)
print("Original fruits tuple:", fruits)
print("Nested tuple:", nested)

# -----------------------------------------------------
# 2️⃣ Tuple methods
# -----------------------------------------------------

# a) count() -> Count occurrences of a value
print("Count of 2 in numbers:", numbers.count(2))  # 3
print("Count of 'Banana' in fruits:", fruits.count("Banana"))  # 2

# b) index() -> Return index of first occurrence of value
print("Index of 4 in numbers:", numbers.index(4))  # 4

# index() with start and end parameters
print("Index of 2 between index 2 and 6:", numbers.index(2, 2, 6))  # 3

# -----------------------------------------------------
# 3️⃣ Accessing elements and slicing
# -----------------------------------------------------

print("First element of fruits:", fruits[0])    # Apple
print("Last element:", fruits[-1])             # Banana

# Slicing
print("Slice from index 1 to 3:", fruits[1:3])  # ('Banana', 'Cherry')
print("Slice with step 2:", numbers[::2])       # (1, 3, 4, 5)
print("Reverse tuple:", numbers[::-1])          # (5, 2, 4, 2, 3, 2, 1)

# -----------------------------------------------------
# 4️⃣ Modifying tuples (convert to list and back)
# -----------------------------------------------------

# Tuples are immutable, but we can convert to a list to modify
numbers_list = list(numbers)       # Convert tuple to list
numbers_list.append(6)             # Add element
numbers_list.remove(2)             # Remove first occurrence of 2
numbers_list[0] = 10               # Change first element
numbers = tuple(numbers_list)      # Convert back to tuple
print("Modified numbers tuple:", numbers)  # (10, 3, 4, 2, 5, 6)

# -----------------------------------------------------
# 5️⃣ Concatenating tuples
# -----------------------------------------------------
t1 = (1, 2, 3)
t2 = (4, 5)
combined = t1 + t2
print("Combined tuple:", combined)  # (1, 2, 3, 4, 5)

# Repeating a tuple
repeated = t2 * 3
print("Repeated tuple:", repeated)  # (4, 5, 4, 5, 4, 5)

# -----------------------------------------------------
# 6️⃣ Unpacking tuples
# -----------------------------------------------------
person = ("Laraib", 25, "Lahore")
name, age, city = person
print("Name:", name)
print("Age:", age)
print("City:", city)

# -----------------------------------------------------
# 7️⃣ Looping through tuples
# -----------------------------------------------------
for fruit in fruits:
    print("Fruit:", fruit)

i = 0
while i < len(fruits):
    print("While loop fruit:", fruits[i])
    i += 1

# -----------------------------------------------------
# 8️⃣ Nested tuples
# -----------------------------------------------------
print("Nested element (1,2):", nested[0])     # (1,2)
print("Nested element 2:", nested[1][1])     # 4


# ==========================================================
# Example 1 — Tuple Packing, Unpacking, and Nested Access
# ==========================================================

# Tuple packing — combining multiple values into one tuple
person = "Laraib", 25, "Lahore"
print("Packed tuple:", person)
# Output: ('Laraib', 25, 'Lahore')

# Tuple unpacking — extract values back into variables
name, age, city = person
print("Name:", name)
print("Age:", age)
print("City:", city)

# You can also unpack partially using * (star expression)
data = (1, 2, 3, 4, 5)
a, *b, c = data
print("a:", a)     # 1
print("b (middle values):",type(b) , b)  # [2, 3, 4]
print("c:", c)     # 5

# Nested tuple unpacking
employee = ("John", ("Developer", "IT"), 55000)
name, (role, dept), salary = employee
print(f"{name} works as a {role} in {dept} department earning {salary}")
# Output: John works as a Developer in IT department earning 55000



# ==========================================================
# Example 2 — Conversion, Sorting, and Aggregation
# ==========================================================

# Converting between list and tuple
nums_tuple = (5, 2, 8, 1, 9)
nums_list = list(nums_tuple)  # Convert to list for modifications
nums_list.sort()              # Sort ascending
nums_list.append(10)
nums_tuple = tuple(nums_list) # Convert back to tuple
print("Modified and sorted tuple:", nums_tuple)
# Output: (1, 2, 5, 8, 9, 10)

# Using built-in functions on tuples
print("Length:", len(nums_tuple))          # Count of elements
print("Max value:", max(nums_tuple))       # Highest value
print("Min value:", min(nums_tuple))       # Lowest value
print("Sum of elements:", sum(nums_tuple)) # Sum of all values

# Using sorted() directly on tuple (returns a new list)
sorted_tuple = sorted(nums_tuple, reverse=True)
print("Sorted in descending order:", sorted_tuple)
# Output: [10, 9, 8, 5, 2, 1]



# ==========================================================
# Example 3 — Iterating, Membership, and Zipping Tuples
# ==========================================================

# Tuple of students and marks
students = ("Ali", "Sara", "John", "Hina")
marks = (85, 90, 78, 92)

# 1️⃣ Iterating with index using enumerate()
for i, name in enumerate(students):
    print(f"Index {i} → Student: {name}")

# 2️⃣ Checking membership (using 'in' and 'not in')
print("Is 'Sara' in students?", 'Sara' in students)       # True
print("Is 'Bilal' not in students?", 'Bilal' not in students)  # True

# 3️⃣ Zipping two tuples together
# zip() pairs elements by position into tuples
for student, mark in zip(students, marks):
    print(f"{student} scored {mark}")

# 4️⃣ Converting zipped tuples into a dictionary
result = dict(zip(students, marks))
print("Dictionary created from tuples:", result)
# Output: {'Ali': 85, 'Sara': 90, 'John': 78, 'Hina': 92}

# 5️⃣ Using tuple comprehension-like pattern (through generator)
# Although tuples don’t have their own comprehension, we can use tuple()
squares = tuple(x**2 for x in range(1, 6))
print("Tuple of squares:", squares)
# Output: (1, 4, 9, 16, 25)


# -----------------------------------------------------
# ✅ Summary of tuple methods
# -----------------------------------------------------
# count(x)       -> Count occurrences of x
# index(x)       -> Find first index of x
# index(x, start, end) -> Find index of x in a range
# Tuples are immutable, but you can modify by converting to list and back
# Tuples support slicing, loops, nested tuples, concatenation, repetition, and unpacking



