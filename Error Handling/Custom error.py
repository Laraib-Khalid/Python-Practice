# Practice

str = input("Enter any command: ")
if str == "quit":
    print(str)
else:
    raise ValueError


User = input("Enter The Value Between 5 And 9 : ")
if (User == "quit"):
     print("Better Luck Next Time!")
elif (int(User) < 5 or int(User) > 9):
     raise ValueError("Error : Invalid Input (Value Should Be In 5 And 9)")


# ------------------------------------------
# Example: Simple Custom Error Handling (No Class)
# ------------------------------------------

def divide_numbers(a, b):
    """Divide two numbers with simple error handling."""
    # Manually raise an error if denominator is zero
    if b == 0:
        raise ValueError("Division by zero is not allowed!")  # Custom message
    return a / b


try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = divide_numbers(num1, num2)
    print(f"Result: {result:.2f}")

except ValueError as e:
    # Handles both invalid input and our raised ValueError
    print(f"Error: {e}")

except Exception as e:
    # Handles any other unexpected errors
    print(f"Unexpected error occurred: {e}")

else:
    print("Division successful!")

finally:
    print("Program ended.")
