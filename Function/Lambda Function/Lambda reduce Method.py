# ----------------------------------------
# Example: Lambda and Reduce Function
# ----------------------------------------

# Import reduce function from functools module
from functools import reduce

# ----------------------------------------
# 1️⃣ Basic Lambda Function Example
# ----------------------------------------

# Lambda function to add two numbers
add = lambda a, b: a + b
print("Lambda Add Example:", add(5, 7))  # Output: 12


# ----------------------------------------
# 2️⃣ Using reduce() to Sum a List
# ----------------------------------------

numbers = [1, 2, 3, 4, 5]

# reduce() applies lambda to accumulate the sum of all elements
total_sum = reduce(lambda x, y: x + y, numbers)

print("\nTotal Sum using reduce():", total_sum)  # Output: 15


# ----------------------------------------
# 3️⃣ Using reduce() to Find the Product
# ----------------------------------------

# Multiply all elements of the list
product = reduce(lambda x, y: x * y, numbers)

print("Product using reduce():", product)  # Output: 120


# ----------------------------------------
# 4️⃣ Using reduce() to Find Maximum Value
# ----------------------------------------

# Compare two numbers and keep the greater one each time
max_value = reduce(lambda x, y: x if x > y else y, numbers)

print("Maximum Value using reduce():", max_value)  # Output: 5


# ----------------------------------------
# 5️⃣ Using reduce() with Strings
# ----------------------------------------

words = ["Hello", "World", "Python"]

# Join all strings with a space using reduce
sentence = reduce(lambda x, y: x + " " + y, words)

print("\nJoined Sentence:", sentence)  # Output: Hello World Python


# ----------------------------------------
# 6️⃣ Using reduce() with Initializer
# ----------------------------------------

# Initializer sets a starting value before reduction begins
numbers = [2, 4, 6]
sum_with_initial = reduce(lambda x, y: x + y, numbers, 10)

print("Sum with Initializer (10):", sum_with_initial)  # Output: 22


# ----------------------------------------
# 7️⃣ Combining map(), filter(), and reduce()
# ----------------------------------------

nums = [1, 2, 3, 4, 5, 6]

# Step 1: Double the even numbers (filter + map)
doubled_evens = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, nums)))

# Step 2: Add all doubled evens using reduce
sum_doubled_evens = reduce(lambda x, y: x + y, doubled_evens)

print("\nDoubled Evens:", doubled_evens)         # [4, 8, 12]
print("Sum of Doubled Evens:", sum_doubled_evens)  # 24
