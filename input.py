# Taking input from user
name = input("Enter your name: ")    # Input as string
age = input("Enter your age: ")      # Even numeric input is a string

print("Your name is:", name)
print("Your age is:", age)
print("Type of age:", type(age))     # Output: <class 'str'>

# Converting string input to integer using int()
num1 = int(input("Enter first number: "))
num2 = input("Enter second number: ")

print("You entered:", num1, "and", num2)
print("Type of num1:", type(num1))   # <class 'int'>
print("Type of num2:", type(int(num2)))   # <class 'int'>

# Without Type Casting
x = input("Enter first number: ")    # e.g. 10
y = input("Enter second number: ")   # e.g. 20

print("Result without type casting:", x + y)
# Output: 1020  (because '10' + '20' → string concatenation)


# With Type Casting
x = int(input("Enter first number: "))   # e.g. 10
y = int(input("Enter second number: "))  # e.g. 20

# Performing arithmetic operations
print("Addition:", x + y)         # 10 + 20 = 30
print("Subtraction:", x - y)      # 10 - 20 = -10
print("Multiplication:", x * y)   # 10 * 20 = 200
print("Division:", x / y)         # 10 / 20 = 0.5
print("Modulus:", x % y)          # 10 % 20 = 10
print("Floor Division:", x // y)  # 10 // 20 = 0
print("Exponentiation:", x ** y)  # 10^20 (large number)



# Example
a=input("kitne dost hain: ")
b=input("total bill: ")
c=float(b)/float(a)
print("har ek ka bill",c)