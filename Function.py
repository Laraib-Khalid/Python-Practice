# Example 1: Simple function that prints a message

def greet():
    """
    This function prints a greeting message
    """
    print("Hello! Welcome to Python functions.")

# Calling the function
greet()


# Example 2: Function with parameters

def greet_person(name):
    """
    This function greets the person whose name is passed as a parameter
    """
    print(f"Hello, {name}! How are you?")

# Calling the function with different arguments
greet_person("Laraib")
greet_person("Ali")


# Example 3: Function that returns a value

def add_numbers(a, b):
    """
    This function takes two numbers, adds them, and returns the sum
    """
    return a + b

# Call the function and store the result
result = add_numbers(5, 3)
print("Sum is:", result)


# Example 4: Function with default parameter

def greet_user(name="Guest"):
    """
    Greets the user. If no name is provided, defaults to 'Guest'
    """
    print(f"Hello, {name}!")

greet_user("Sara")  # Argument provided
greet_user()        # No argument, uses default

# Example 5: Function with multiple parameters

def multiply(a, b):
    """
    Multiplies two numbers and returns the result
    """
    return a * b

print("Multiplication:", multiply(4, 5))


# Example 6: Function that prints values without returning

def print_square(num):
    """
    Prints the square of the number
    """
    print(f"Square of {num} is {num**2}")

print_square(6)
