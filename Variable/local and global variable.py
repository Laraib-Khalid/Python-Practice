# 🌍 Global variable — accessible anywhere in this file
x = 10

def my_function():
    # ⚠️ Local variable — only accessible inside this function
    y = 5

    print("Inside function:")
    print("Local variable y =", y)      # local variable
    print("Global variable x =", x)     # accessing global variable inside the function

# Call the function
my_function()

print("\nOutside function:")
print("Global variable x =", x)          # works fine
# print(y)   # ❌ This will cause an error: NameError (y is not defined outside function)


print("-" * 50)

# 2nd Example

count = 0  # Global variable

def increase_count():
    global count  # Declare that we want to use the global variable
    count += 1
    print("Inside function, count =", count)

increase_count()
print("Outside function, count =", count)
