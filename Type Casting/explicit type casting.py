# Explicit Type Conversion Example

# Converting float to int
x = 9.8
y = int(x)   # Manually convert float → int (decimal part is removed)
print("Value:", y)          # Output: 9
print("Type:", type(y))     # Output: <class 'int'>

# Converting int to float
a = 5
b = float(a)
print("Value:", b)          # Output: 5.0
print("Type:", type(b))     # Output: <class 'float'>

# Converting string to integer
s = "100"
num = int(s)
print("Value:", num)        # Output: 100
print("Type:", type(num))   # Output: <class 'int'>

# Converting integer to string
n = 50
text = str(n)
print("Value:", text)       # Output: "50"
print("Type:", type(text))  # Output: <class 'str'>

# Converting to complex number
val = 7
comp = complex(val)
print("Value:", comp)       # Output: (7+0j)
print("Type:", type(comp))  # Output: <class 'complex'>

# Converting list to tuple
list1 = [1, 2, 3]
tuple1 = tuple(list1)
print("Value:", tuple1)     # Output: (1, 2, 3)
print("Type:", type(tuple1))# Output: <class 'tuple'>
