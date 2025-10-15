# Implicit Type Conversion Example

# Integer and Float addition
num_int = 10        # int
num_float = 5.5     # float

# When you add an int and float, Python automatically converts the int into a float
result = num_int + num_float

print("Value:", result)           # Output: 15.5
print("Type of result:", type(result))   # Output: <class 'float'>
# Python promotes the int (10) to float (10.0) before performing the operation


# Boolean + Integer
a = True     # Boolean (internally True = 1, False = 0)
b = 5        # Integer
sum_result = a + b
print("Value:", sum_result)       # Output: 6
print("Type:", type(sum_result))  # Output: <class 'int'>
# Here, True is implicitly converted to 1 and added to 5




