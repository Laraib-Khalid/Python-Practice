# Example 1: Handling division by zero
try:
    result = 10 / 0  # This will cause ZeroDivisionError
    print("Result:", result)
except ZeroDivisionError:
    print("Error: You cannot divide by zero!")


# Example 2: Handling different types of errors separately
try:
    num = int(input("Enter a number: "))  # May raise ValueError if input is not numeric
    result = 10 / num                     # May raise ZeroDivisionError if input = 0
    print(f"Result is: {result:.2f}")

except ValueError:
    print("Error: Please enter a valid number.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")


# Example 3: Using else (runs if no exception) and finally (always runs)
try:
    num = int(input("Enter a positive number: "))
    print("Square is:", num ** 2)
except ValueError:
    print("Error: Invalid input, please enter a number.")
else:
    print("No errors occurred! Well done.")
finally:
    print("Program ended (finally block always executes).")


# Example 4: Generic exception handling
try:
    value = int("abc")  # This will raise ValueError
except Exception as e:
    print("An error occurred:", e)  # Prints the actual error message


# Example 5: Nested try-except blocks
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    try:
        result = num1 / num2
        print("Result:", result)
    except ZeroDivisionError:
        print("Inner Error: Cannot divide by zero.")
except ValueError:
    print("Outer Error: Please enter numeric values.")
