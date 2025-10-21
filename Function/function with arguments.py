# Function to add two numbers using positional arguments
def add_numbers(a, b):
    """
    Adds two numbers and returns the sum
    """
    return a + b

result = add_numbers(5, 10)  # 5 -> a, 10 -> b
print("Sum:", result)

# Function with keyword arguments
def greet(name, age):
    """
    Greets a person with their name and age
    """
    return f"Hello {name}, you are {age} years old!"

message = greet(age=25, name="Laraib")  # order doesn't matter
print(message)


# Function with a default argument
def greet_user(name="Guest"):
    """
    Greets the user. Default is 'Guest' if no name is provided
    """
    return f"Hello {name}!"

print(greet_user("Ali"))  # Argument provided
print(greet_user())       # Uses default value


# Function that accepts multiple numbers and returns their sum
# ✅ Here, args is a tuple of all positional arguments.
def sum_numbers(*tuple):
    """
    Accepts any number of positional arguments and returns the sum
    """
    total = 0
    for num in tuple:
        total += num
    return total

print("Sum:", sum_numbers(1, 2, 3, 4, 5, 9))  # Pass multiple numbers


# Function that prints details from a dictionary
# ✅ Here, kwargs is a dictionary containing all keyword arguments.
def show_details(**dic):
    """
    Accepts any number of keyword arguments and prints them
    """
    for key, value in dic.items():
        print(f"{key}: {value}")

show_details(name="Laraib", age=25, city="Lahore")

# Function that returns multiple values as a tuple
def arithmetic_operations(a, b):
    """
    Returns sum, difference, product of two numbers as a tuple
    """
    return a+b, a-b, a*b

result = arithmetic_operations(10, 5)
print("Sum, Difference, Product:", result)


# Function that returns a dictionary
def create_person(name, age, city):
    """
    Returns a dictionary with person details
    """
    return {"name": name, "age": age, "city": city}

person_info = create_person("Ali", 30, "Karachi")
print(person_info)

