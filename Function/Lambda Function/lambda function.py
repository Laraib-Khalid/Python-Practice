# 🔹 Example 1 — Basic Lambda Function
# Normal function
def add(a, b):
    return a + b

# Lambda equivalent
add_lambda = lambda a, b: a + b

# Using both
print("Normal function:", add(3, 5))
print("Lambda function:", add_lambda(3, 5))



# 🔹 Example 2 — Lambda with map()

# Apply a function to every element of a list.

numbers = [1, 2, 3, 4, 5]

# Multiply each number by 2
doubled = list(map(lambda x: x * 2, numbers))

print("Doubled List:", doubled)


# 🔹 Example 3 — Lambda with filter()
#
# Filter elements from a list based on a condition.

numbers = [10, 15, 20, 25, 30]

# Keep only numbers divisible by 10
divisible_by_10 = list(filter(lambda x: x % 10 == 0, numbers))

print("Divisible by 10:", divisible_by_10)


# 🔹 Example 4 — Lambda with sorted()
#
# Sort tuples based on the second element.

pairs = [(1, 3), (2, 2), (4, 1)]

# Sort by second value in tuple
sorted_pairs = sorted(pairs, key=lambda x: x[1])

print("Sorted Pairs:", sorted_pairs)


# 🔹 Example 5 — Inline Conditional (Ternary) Lambda
# Lambda to check even or odd
check = lambda x: "Even" if x % 2 == 0 else "Odd"

print(check(4))
print(check(7))


# 🔹 Example 6 — Lambda as Return Value
def power(n):
    return lambda x: x ** n  # returns a lambda function

square = power(2)
cube = power(3)

print("Square of 4:", square(4))
print("Cube of 3:", cube(3))