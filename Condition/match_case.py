"""
========================================
Python 'match' and 'case' Statement Example
========================================
Introduced in Python 3.10, the 'match' statement is used for structural pattern matching.
It works similarly to a switch-case in other languages but is more powerful and flexible.
"""

# Example 1: Simple string matching
# ----------------------------------
command = "start"

# 'match' evaluates the expression (here, the variable 'command')
# and compares it to each 'case' until one matches.
match command:
    case "start":
        print("System is starting...")
    case "stop":
        print("System is stopping...")
    case "restart":
        print("System is restarting...")
    case _:
        # The underscore (_) acts like a default case
        print("Unknown command")

# Output: System is starting...


# Example 2: Matching numeric values
# ----------------------------------
status_code = 404

match status_code:
    case 200:
        print("OK – Request successful")
    case 400:
        print("Bad Request")
    case 401 | 403:
        # You can use the OR operator (|) for multiple options
        print("Unauthorized or Forbidden")
    case 404:
        print("Not Found")
    case _:
        print("Unknown status code")

# Output: Not Found


# Example 3: Matching tuples and destructuring
# --------------------------------------------
# match can unpack data from sequences, making it great for structured data.

point = (3, 0)

match point:
    case (0, 0):
        print("Origin point")
    case (x, 0):
        # The second value is 0, and the first is captured into variable x
        print(f"Point is on the X-axis at x={x}")
    case (0, y):
        print(f"Point is on the Y-axis at y={y}")
    case (x, y):
        print(f"Point is somewhere else: ({x}, {y})")
    case _:
        print("Not a valid point")

# Output: Point is on the X-axis at x=3


# Example 4: Matching dictionaries
# --------------------------------
person = {"name": "Laraib", "role": "QA Engineer"}

match person:
    case {"name": name, "role": "QA Engineer"}:
        # Extract 'name' and check role
        print(f"Hello {name}, you’re a QA Engineer.")
    case {"name": name, "role": "Developer"}:
        print(f"Hello {name}, you’re a Developer.")
    case _:
        print("Unrecognized role")

# Output: Hello Laraib, you’re a QA Engineer.


# Example 5: Adding conditions (guards)
# -------------------------------------
number = 15

match number:
    case x if x < 0:
        print("Negative number")
    case x if 0 <= x < 10:
        print("Single-digit positive number")
    case x if 10 <= x < 100:
        print("Double-digit positive number")
    case _:
        print("Number is too large or unrecognized")

# Output: Double-digit positive number


# Example 6: Combining patterns and using wildcards
# -------------------------------------------------
data = ["error", 500, "server down"]

match data:
    case ["error", code, _]:
        print(f"Error detected! Code: {code}")
    case ["warning", *_]:
        print("Warning message received")
    case _:
        print("Unknown data format")

# Output: Error detected! Code: 500


# # Example 7: Matching class instances
# # -----------------------------------
# class Employee:
#     def __init__(self, name, role):
#         self.name = name
#         self.role = role
#
#
# emp = Employee("Laraib", "SQA Engineer")
#
# match emp:
#     case Employee(name="Laraib", role="SQA Engineer"):
#         print("This is Laraib from QA team.")
#     case Employee(name=name, role=role):
#         print(f"Employee: {name}, Role: {role}")
#     case _:
#         print("Unknown employee")
#
# # Output: This is Laraib from QA team.


# Example 7: Nested pattern matching
# ----------------------------------
data = {"user": {"name": "Sara", "role": "Admin"}}

match data:
    case {"user": {"name": name, "role": "Admin"}}:
        print(f"Welcome Admin {name}!")
    case {"user": {"name": name, "role": role}}:
        print(f"Welcome {name}, your role is {role}")
    case _:
        print("Invalid user data")

# Output: Welcome Admin Sara!
