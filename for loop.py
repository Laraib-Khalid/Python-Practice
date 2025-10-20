"""
========================================
PYTHON FOR LOOP — COMPLETE EXAMPLES
========================================
This script demonstrates many ways to use Python's `for` loop,
including range(), nested loops, control flow, and useful functions.
"""

# ----------------------------------------
# Example 1: Basic for loop with a list
# ----------------------------------------
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry


# ----------------------------------------
# Example 2: Using range() with stop only
# range(stop) → starts from 0 to stop-1
# ----------------------------------------
for i in range(5):
    print("Value:", i)
# Output: 0, 1, 2, 3, 4


# ----------------------------------------
# Example 3: Using range(start, stop)
# ----------------------------------------
for i in range(2, 7):
    print(i)
# Output: 2, 3, 4, 5, 6


# ----------------------------------------
# Example 4: Using range(start, stop, step)
# The third argument is the STEP parameter
# ----------------------------------------
for i in range(0, 20, 5):
    print("Counting by 5:", i)
# Output: 0, 5, 10, 15


# ----------------------------------------
# Example 5: Looping backward using negative step
# ----------------------------------------
for i in range(10, 0, -2):
    print("Reverse count:", i)
# Output: 10, 8, 6, 4, 2


# ----------------------------------------
# Example 6: Iterating over a string
# ----------------------------------------
word = "Python"
for letter in word:
    print("Letter:", letter)
# Output: P y t h o n


# 🔹 Using end parameter in print()
print("Example 6: Using 'end' parameter")
for char in "HELLO":
    print(char, end="-")  # print on same line separated by "-"
print("\n" + "-" * 50)

# ----------------------------------------
# Example 7: Iterating over a tuple
# ----------------------------------------
colors = ("red", "green", "blue")
for color in colors:
    print(color)
# Output: red, green, blue


# ----------------------------------------
# Example 8: Iterating over a dictionary (keys only)
# ----------------------------------------
person = {"name": "Laraib", "age": 25, "city": "Lahore"}

for key in person:
    print(key)
# Output: name, age, city


# ----------------------------------------
# Example 9: Iterating over a dictionary (key + value)
# ----------------------------------------
for key, value in person.items():
    print(f"{key} → {value}")
# Output:
# name → Laraib
# age → 25
# city → Lahore


# ----------------------------------------
# Example 10: Using enumerate() to get index + value
# ----------------------------------------
animals = ["cat", "dog", "bird"]
for index, animal in enumerate(animals):
    print(f"Index {index} has animal: {animal}")
# Output:
# Index 0 has animal: cat
# Index 1 has animal: dog
# Index 2 has animal: bird


# ----------------------------------------
# Example 11: Using zip() to iterate multiple lists
# ----------------------------------------
names = ["Ali", "Sara", "John"]
scores = [85, 90, 78]

for name, score in zip(names, scores):
    print(f"{name} scored {score}")
# Output:
# Ali scored 85
# Sara scored 90
# John scored 78


# ----------------------------------------
# Example 12: Nested for loops
# ----------------------------------------
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i},{j})", end=" ")
    print()  # newline after inner loop
# Output:
# (1,1) (1,2) (1,3)
# (2,1) (2,2) (2,3)
# (3,1) (3,2) (3,3)


# ----------------------------------------
# Example 13: Using break to stop the loop early
# ----------------------------------------
for num in range(1, 10):
    if num == 5:
        print("Breaking at 5")
        break
    print(num)
# Output: 1 2 3 4 Breaking at 5


# ----------------------------------------
# Example 14: Using continue to skip a value
# ----------------------------------------
for num in range(1, 6):
    if num == 3:
        print("Skipping 3")
        continue
    print(num)
# Output:
# 1
# 2
# Skipping 3
# 4
# 5


# ----------------------------------------
# Example 15: For loop with else
# The else block runs only if loop finishes normally (no break)
# ----------------------------------------
for num in range(3):
    print(num)
else:
    print("Loop completed without break!")
# Output:
# 0 1 2
# Loop completed without break!


# ----------------------------------------
# Example 16: For loop with break — else won’t execute
# ----------------------------------------
for num in range(5):
    if num == 2:
        break
    print(num)
else:
    print("This will NOT run because loop broke")
# Output:
# 0
# 1


# ----------------------------------------
# Example 17: Looping through a set
# (Note: sets are unordered)
# ----------------------------------------
myset = {10, 20, 30}
for item in myset:
    print(item)
# Output: order may vary


# ----------------------------------------
# Example 18: Using range with len()
# ----------------------------------------
students = ["Ayesha", "Bilal", "Hamza"]

for i in range(len(students)):
    print(f"Student {i}: {students[i]}")
# Output:
# Student 0: Ayesha
# Student 1: Bilal
# Student 2: Hamza


# ----------------------------------------
# Example 19: Using reversed() in loop
# ----------------------------------------
for num in reversed(range(1, 6)):
    print(num, end=" ")
# Output: 5 4 3 2 1


# ----------------------------------------
# Example 20: List comprehension (short form of for loop)
# ----------------------------------------
# Create a list of squares
squares = [x**2 for x in range(1, 6)]
print("\nSquares list:", squares)
# Output: [1, 4, 9, 16, 25]


# ----------------------------------------
# Example 21: For loop with step parameter and condition
# ----------------------------------------
for i in range(0, 21, 2):  # step = 2 (even numbers)
    if i % 4 == 0:
        print(f"{i} is divisible by 4")
    else:
        print(f"{i} is even but not divisible by 4")
# Output shows even numbers up to 20 with conditions


# ----------------------------------------
# Example 22: Nested loop – multiplication table
# ----------------------------------------
for i in range(1, 4):
    for j in range(1, 6):
        print(f"{i} x {j} = {i*j}")
    print("------")
# Output: 1–3 tables up to 5


print("\n===== END OF FOR LOOP EXAMPLES =====")
