def add_numbers(a, b):
    """
    This function takes two numbers as input and returns their sum.

    Parameters:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The sum of a and b.
    """
    return a + b

a = 5
b = 6
# Accessing the docstring
print(add_numbers.__doc__)
print(f"Add Number {a} and {b} = {add_numbers(a, b)}")
